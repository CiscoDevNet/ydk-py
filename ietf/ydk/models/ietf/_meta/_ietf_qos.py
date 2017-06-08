


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'DscpCodeAllValuesTypeEnum' : _MetaInfoEnum('DscpCodeAllValuesTypeEnum', 'ydk.models.ietf.ietf_qos',
        {
            'af11':'af11',
            'af12':'af12',
            'af13':'af13',
            'af21':'af21',
            'af22':'af22',
            'af23':'af23',
            'af31':'af31',
            'af32':'af32',
            'af33':'af33',
            'af41':'af41',
            'af42':'af42',
            'af43':'af43',
            'cs0':'cs0',
            'cs1':'cs1',
            'cs2':'cs2',
            'cs3':'cs3',
            'cs4':'cs4',
            'cs5':'cs5',
            'cs6':'cs6',
            'cs7':'cs7',
            'df':'df',
            'ef':'ef',
            'all':'all',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.ClassDefinitions.ClassDefinition.Qos_' : {
        'meta_info' : _MetaInfoClass('Qos.ClassDefinitions.ClassDefinition.Qos_',
            False, 
            [
            _MetaInfoClassMember('class', ATTRIBUTE, 'str' , None, None, 
                [(1, 39)], [], 
                '''                class name
                ''',
                'class_',
                'ietf-qos', True),
            _MetaInfoClassMember('dscp-code', ATTRIBUTE, 'int' , None, None, 
                [('1', '63')], [], 
                '''                dscp-code
                ''',
                'dscp_code',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'qos',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassDefinitions.ClassDefinition' : {
        'meta_info' : _MetaInfoClass('Qos.ClassDefinitions.ClassDefinition',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                qos-class-definition name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('qos', REFERENCE_LIST, 'Qos_' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassDefinitions.ClassDefinition.Qos_', 
                [], [], 
                '''                qos class
                ''',
                'qos',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class-definition',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassDefinitions' : {
        'meta_info' : _MetaInfoClass('Qos.ClassDefinitions',
            False, 
            [
            _MetaInfoClassMember('class-definition', REFERENCE_LIST, 'ClassDefinition' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassDefinitions.ClassDefinition', 
                [], [], 
                '''                class-definition
                ''',
                'class_definition',
                'ietf-qos', False, max_elements=14),
            ],
            'ietf-qos',
            'class-definitions',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Atm.In_.Atm_' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Atm.In_.Atm_',
            False, 
            [
            _MetaInfoClassMember('class', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                class
                ''',
                'class_',
                'ietf-qos', True),
            _MetaInfoClassMember('to-qos', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                to-qos
                ''',
                'to_qos',
                'ietf-qos', False),
            _MetaInfoClassMember('use-ethernet', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                use-ethernet
                ''',
                'use_ethernet',
                'ietf-qos', False),
            _MetaInfoClassMember('use-ip', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                use-ip
                ''',
                'use_ip',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'atm',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Atm.In_' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Atm.In_',
            False, 
            [
            _MetaInfoClassMember('atm', REFERENCE_LIST, 'Atm_' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Atm.In_.Atm_', 
                [], [], 
                '''                atm list
                ''',
                'atm',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'in',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Atm.Out.Qos_' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Atm.Out.Qos_',
            False, 
            [
            _MetaInfoClassMember('dscp-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                dscp-code
                ''',
                'dscp_code',
                'ietf-qos', True),
            _MetaInfoClassMember('to-atm', ATTRIBUTE, 'int' , None, None, 
                [('0', '1')], [], 
                '''                to-atm
                ''',
                'to_atm',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'qos',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Atm.Out' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Atm.Out',
            False, 
            [
            _MetaInfoClassMember('qos', REFERENCE_LIST, 'Qos_' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Atm.Out.Qos_', 
                [], [], 
                '''                qos list
                ''',
                'qos',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'out',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Atm' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Atm',
            False, 
            [
            _MetaInfoClassMember('in', REFERENCE_CLASS, 'In_' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Atm.In_', 
                [], [], 
                '''                in
                ''',
                'in_',
                'ietf-qos', False),
            _MetaInfoClassMember('out', REFERENCE_CLASS, 'Out' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Atm.Out', 
                [], [], 
                '''                out
                ''',
                'out',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'atm',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Ethernet.In_.Ethernet_' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Ethernet.In_.Ethernet_',
            False, 
            [
            _MetaInfoClassMember('class', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                class
                ''',
                'class_',
                'ietf-qos', True),
            _MetaInfoClassMember('to-qos', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                to-qos
                ''',
                'to_qos',
                'ietf-qos', False),
            _MetaInfoClassMember('use-ip', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                use-ip
                ''',
                'use_ip',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ethernet',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Ethernet.In_.MappingSchemaEnum' : _MetaInfoEnum('MappingSchemaEnum', 'ydk.models.ietf.ietf_qos',
        {
            '5P3D':'Y_5P3D',
            '6P2D':'Y_6P2D',
            '7P1D':'Y_7P1D',
            '8P0D':'Y_8P0D',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.ClassMaps.ClassMap.Ethernet.In_' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Ethernet.In_',
            False, 
            [
            _MetaInfoClassMember('ethernet', REFERENCE_LIST, 'Ethernet_' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Ethernet.In_.Ethernet_', 
                [], [], 
                '''                ethernet list
                ''',
                'ethernet',
                'ietf-qos', False),
            _MetaInfoClassMember('mapping-schema', REFERENCE_ENUM_CLASS, 'MappingSchemaEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Ethernet.In_.MappingSchemaEnum', 
                [], [], 
                '''                mapping-schema
                ''',
                'mapping_schema',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'in',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Ethernet.Out.Qos_' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Ethernet.Out.Qos_',
            False, 
            [
            _MetaInfoClassMember('dscp-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                dscp-code
                ''',
                'dscp_code',
                'ietf-qos', True),
            _MetaInfoClassMember('to-ethernet', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                to-ethernet
                ''',
                'to_ethernet',
                'ietf-qos', False),
            _MetaInfoClassMember('use-ethernet', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                use-ethernet
                ''',
                'use_ethernet',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'qos',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Ethernet.Out.MappingSchemaEnum' : _MetaInfoEnum('MappingSchemaEnum', 'ydk.models.ietf.ietf_qos',
        {
            '5P3D':'Y_5P3D',
            '6P2D':'Y_6P2D',
            '7P1D':'Y_7P1D',
            '8P0D':'Y_8P0D',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.ClassMaps.ClassMap.Ethernet.Out' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Ethernet.Out',
            False, 
            [
            _MetaInfoClassMember('mapping-schema', REFERENCE_ENUM_CLASS, 'MappingSchemaEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Ethernet.Out.MappingSchemaEnum', 
                [], [], 
                '''                mapping-schema
                ''',
                'mapping_schema',
                'ietf-qos', False),
            _MetaInfoClassMember('qos', REFERENCE_LIST, 'Qos_' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Ethernet.Out.Qos_', 
                [], [], 
                '''                qos list
                ''',
                'qos',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'out',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Ethernet' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Ethernet',
            False, 
            [
            _MetaInfoClassMember('in', REFERENCE_CLASS, 'In_' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Ethernet.In_', 
                [], [], 
                '''                in
                ''',
                'in_',
                'ietf-qos', False),
            _MetaInfoClassMember('out', REFERENCE_CLASS, 'Out' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Ethernet.Out', 
                [], [], 
                '''                out
                ''',
                'out',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ethernet',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Ip.In_.Ip_' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Ip.In_.Ip_',
            False, 
            [
            _MetaInfoClassMember('dscp-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                dscp-code
                ''',
                'dscp_code',
                'ietf-qos', True),
            _MetaInfoClassMember('to-qos', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                to-qos
                ''',
                'to_qos',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ip',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Ip.In_' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Ip.In_',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_LIST, 'Ip_' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Ip.In_.Ip_', 
                [], [], 
                '''                ip list
                ''',
                'ip',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'in',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Ip.Out.Qos_' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Ip.Out.Qos_',
            False, 
            [
            _MetaInfoClassMember('dscp-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                dscp-code
                ''',
                'dscp_code',
                'ietf-qos', True),
            _MetaInfoClassMember('to-ip', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                to-ip
                ''',
                'to_ip',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'qos',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Ip.Out' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Ip.Out',
            False, 
            [
            _MetaInfoClassMember('qos', REFERENCE_LIST, 'Qos_' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Ip.Out.Qos_', 
                [], [], 
                '''                qos list
                ''',
                'qos',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'out',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Ip' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Ip',
            False, 
            [
            _MetaInfoClassMember('in', REFERENCE_CLASS, 'In_' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Ip.In_', 
                [], [], 
                '''                in direction
                ''',
                'in_',
                'ietf-qos', False),
            _MetaInfoClassMember('out', REFERENCE_CLASS, 'Out' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Ip.Out', 
                [], [], 
                '''                out direction
                ''',
                'out',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ip',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Mpls.In_.Mpls_' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Mpls.In_.Mpls_',
            False, 
            [
            _MetaInfoClassMember('exp-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                exp-value
                ''',
                'exp_value',
                'ietf-qos', True),
            _MetaInfoClassMember('to-qos', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                to-qos
                ''',
                'to_qos',
                'ietf-qos', False),
            _MetaInfoClassMember('use-ethernet', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                use-ethernet
                ''',
                'use_ethernet',
                'ietf-qos', False),
            _MetaInfoClassMember('use-ip', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                use-ip
                ''',
                'use_ip',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'mpls',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Mpls.In_.MappingSchemaEnum' : _MetaInfoEnum('MappingSchemaEnum', 'ydk.models.ietf.ietf_qos',
        {
            '5P3D':'Y_5P3D',
            '6P2D':'Y_6P2D',
            '7P1D':'Y_7P1D',
            '8P0D':'Y_8P0D',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.ClassMaps.ClassMap.Mpls.In_' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Mpls.In_',
            False, 
            [
            _MetaInfoClassMember('mapping-schema', REFERENCE_ENUM_CLASS, 'MappingSchemaEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Mpls.In_.MappingSchemaEnum', 
                [], [], 
                '''                mapping-schema
                ''',
                'mapping_schema',
                'ietf-qos', False),
            _MetaInfoClassMember('mpls', REFERENCE_LIST, 'Mpls_' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Mpls.In_.Mpls_', 
                [], [], 
                '''                mpls list
                ''',
                'mpls',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'in',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Mpls.Out.Qos_' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Mpls.Out.Qos_',
            False, 
            [
            _MetaInfoClassMember('dscp-code', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                dscp-code
                ''',
                'dscp_code',
                'ietf-qos', True),
            _MetaInfoClassMember('to-mpls', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                to-mpls
                ''',
                'to_mpls',
                'ietf-qos', False),
            _MetaInfoClassMember('use-mpls', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                use-mpls
                ''',
                'use_mpls',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'qos',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Mpls.Out.MappingSchemaEnum' : _MetaInfoEnum('MappingSchemaEnum', 'ydk.models.ietf.ietf_qos',
        {
            '5P3D':'Y_5P3D',
            '6P2D':'Y_6P2D',
            '7P1D':'Y_7P1D',
            '8P0D':'Y_8P0D',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.ClassMaps.ClassMap.Mpls.Out' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Mpls.Out',
            False, 
            [
            _MetaInfoClassMember('mapping-schema', REFERENCE_ENUM_CLASS, 'MappingSchemaEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Mpls.Out.MappingSchemaEnum', 
                [], [], 
                '''                mapping-schema
                ''',
                'mapping_schema',
                'ietf-qos', False),
            _MetaInfoClassMember('qos', REFERENCE_LIST, 'Qos_' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Mpls.Out.Qos_', 
                [], [], 
                '''                qos list
                ''',
                'qos',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'out',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap.Mpls' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap.Mpls',
            False, 
            [
            _MetaInfoClassMember('in', REFERENCE_CLASS, 'In_' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Mpls.In_', 
                [], [], 
                '''                in direction
                ''',
                'in_',
                'ietf-qos', False),
            _MetaInfoClassMember('out', REFERENCE_CLASS, 'Out' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Mpls.Out', 
                [], [], 
                '''                out
                ''',
                'out',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'mpls',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps.ClassMap' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps.ClassMap',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                class-map-name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('atm', REFERENCE_CLASS, 'Atm' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Atm', 
                [], [], 
                '''                atm
                ''',
                'atm',
                'ietf-qos', False),
            _MetaInfoClassMember('ethernet', REFERENCE_CLASS, 'Ethernet' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Ethernet', 
                [], [], 
                '''                ethernet
                ''',
                'ethernet',
                'ietf-qos', False),
            _MetaInfoClassMember('ip', REFERENCE_CLASS, 'Ip' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Ip', 
                [], [], 
                '''                ip
                ''',
                'ip',
                'ietf-qos', False),
            _MetaInfoClassMember('mpls', REFERENCE_CLASS, 'Mpls' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap.Mpls', 
                [], [], 
                '''                mpls
                ''',
                'mpls',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class-map',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.ClassMaps' : {
        'meta_info' : _MetaInfoClass('Qos.ClassMaps',
            False, 
            [
            _MetaInfoClassMember('class-map', REFERENCE_LIST, 'ClassMap' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps.ClassMap', 
                [], [], 
                '''                class-map
                ''',
                'class_map',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class-maps',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue.Default' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue.Default',
            False, 
            [
            _MetaInfoClassMember('max-threshold', ATTRIBUTE, 'int' , None, None, 
                [('2', '10240')], [], 
                '''                max-threshold
                ''',
                'max_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('min-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10240')], [], 
                '''                min-threshold
                ''',
                'min_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('probability', ATTRIBUTE, 'int' , None, None, 
                [('1', '1023')], [], 
                '''                probability
                ''',
                'probability',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'default',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue.Profile1.DscpEnum' : _MetaInfoEnum('DscpEnum', 'ydk.models.ietf.ietf_qos',
        {
            'af11':'af11',
            'af12':'af12',
            'af13':'af13',
            'af21':'af21',
            'af22':'af22',
            'af23':'af23',
            'af31':'af31',
            'af32':'af32',
            'af33':'af33',
            'af41':'af41',
            'af42':'af42',
            'af43':'af43',
            'cs1':'cs1',
            'cs2':'cs2',
            'cs3':'cs3',
            'cs4':'cs4',
            'cs5':'cs5',
            'cs6':'cs6',
            'cs7':'cs7',
            'df':'df',
            'ef':'ef',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue.Profile1' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue.Profile1',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                dscp
                ''',
                'dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2.DscpEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2.DscpEnum', 
                        [], [], 
                        '''                        dscp
                        ''',
                        'dscp',
                        'ietf-qos', False, min_elements=1),
                    _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('1', '7'), ('9', 'None'), ('11', 'None'), ('13', 'None'), ('15', 'None'), ('17', 'None'), ('19', 'None'), ('21', 'None'), ('23', 'None'), ('25', 'None'), ('27', 'None'), ('29', 'None'), ('31', 'None'), ('33', 'None'), ('35', 'None'), ('37', 'None'), ('39', 'None'), ('41', '45'), ('47', 'None'), ('49', '55'), ('57', '63')], [], 
                        '''                        dscp
                        ''',
                        'dscp',
                        'ietf-qos', False, min_elements=1),
                ], min_elements=1),
            _MetaInfoClassMember('max-threshold', ATTRIBUTE, 'int' , None, None, 
                [('2', '10240')], [], 
                '''                max-threshold
                ''',
                'max_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('min-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10240')], [], 
                '''                min-threshold
                ''',
                'min_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('probability', ATTRIBUTE, 'int' , None, None, 
                [('1', '1023')], [], 
                '''                probability
                ''',
                'probability',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'profile-1',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue.Profile2.DscpEnum' : _MetaInfoEnum('DscpEnum', 'ydk.models.ietf.ietf_qos',
        {
            'af11':'af11',
            'af12':'af12',
            'af13':'af13',
            'af21':'af21',
            'af22':'af22',
            'af23':'af23',
            'af31':'af31',
            'af32':'af32',
            'af33':'af33',
            'af41':'af41',
            'af42':'af42',
            'af43':'af43',
            'cs1':'cs1',
            'cs2':'cs2',
            'cs3':'cs3',
            'cs4':'cs4',
            'cs5':'cs5',
            'cs6':'cs6',
            'cs7':'cs7',
            'df':'df',
            'ef':'ef',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue.Profile2' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue.Profile2',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                dscp
                ''',
                'dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2.DscpEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2.DscpEnum', 
                        [], [], 
                        '''                        dscp
                        ''',
                        'dscp',
                        'ietf-qos', False, min_elements=1),
                    _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('1', '7'), ('9', 'None'), ('11', 'None'), ('13', 'None'), ('15', 'None'), ('17', 'None'), ('19', 'None'), ('21', 'None'), ('23', 'None'), ('25', 'None'), ('27', 'None'), ('29', 'None'), ('31', 'None'), ('33', 'None'), ('35', 'None'), ('37', 'None'), ('39', 'None'), ('41', '45'), ('47', 'None'), ('49', '55'), ('57', '63')], [], 
                        '''                        dscp
                        ''',
                        'dscp',
                        'ietf-qos', False, min_elements=1),
                ], min_elements=1),
            _MetaInfoClassMember('max-threshold', ATTRIBUTE, 'int' , None, None, 
                [('2', '10240')], [], 
                '''                max-threshold
                ''',
                'max_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('min-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10240')], [], 
                '''                min-threshold
                ''',
                'min_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('probability', ATTRIBUTE, 'int' , None, None, 
                [('1', '1023')], [], 
                '''                probability
                ''',
                'probability',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'profile-2',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue',
            False, 
            [
            _MetaInfoClassMember('num', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                queue number
                ''',
                'num',
                'ietf-qos', True),
            _MetaInfoClassMember('default', REFERENCE_CLASS, 'Default' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue.Default', 
                [], [], 
                '''                default drop profile
                ''',
                'default',
                'ietf-qos', False),
            _MetaInfoClassMember('depth', ATTRIBUTE, 'int' , None, None, 
                [('1', '65536')], [], 
                '''                depth
                ''',
                'depth',
                'ietf-qos', False),
            _MetaInfoClassMember('exponential-weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '15')], [], 
                '''                exponential-weight
                ''',
                'exponential_weight',
                'ietf-qos', False),
            _MetaInfoClassMember('profile-1', REFERENCE_CLASS, 'Profile1' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue.Profile1', 
                [], [], 
                '''                drop profile-1
                ''',
                'profile_1',
                'ietf-qos', False),
            _MetaInfoClassMember('profile-2', REFERENCE_CLASS, 'Profile2' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue.Profile2', 
                [], [], 
                '''                drop profile-2
                ''',
                'profile_2',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'queue',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr',
            False, 
            [
            _MetaInfoClassMember('queue', REFERENCE_LIST, 'Queue' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue', 
                [], [], 
                '''                queue
                ''',
                'queue',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'mdrr',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue.Default' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue.Default',
            False, 
            [
            _MetaInfoClassMember('max-threshold', ATTRIBUTE, 'int' , None, None, 
                [('2', '10240')], [], 
                '''                max-threshold
                ''',
                'max_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('min-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10240')], [], 
                '''                min-threshold
                ''',
                'min_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('probability', ATTRIBUTE, 'int' , None, None, 
                [('1', '1023')], [], 
                '''                probability
                ''',
                'probability',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'default',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue.Profile1.DscpEnum' : _MetaInfoEnum('DscpEnum', 'ydk.models.ietf.ietf_qos',
        {
            'af11':'af11',
            'af12':'af12',
            'af13':'af13',
            'af21':'af21',
            'af22':'af22',
            'af23':'af23',
            'af31':'af31',
            'af32':'af32',
            'af33':'af33',
            'af41':'af41',
            'af42':'af42',
            'af43':'af43',
            'cs1':'cs1',
            'cs2':'cs2',
            'cs3':'cs3',
            'cs4':'cs4',
            'cs5':'cs5',
            'cs6':'cs6',
            'cs7':'cs7',
            'df':'df',
            'ef':'ef',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue.Profile1' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue.Profile1',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                dscp
                ''',
                'dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2.DscpEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2.DscpEnum', 
                        [], [], 
                        '''                        dscp
                        ''',
                        'dscp',
                        'ietf-qos', False, min_elements=1),
                    _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('1', '7'), ('9', 'None'), ('11', 'None'), ('13', 'None'), ('15', 'None'), ('17', 'None'), ('19', 'None'), ('21', 'None'), ('23', 'None'), ('25', 'None'), ('27', 'None'), ('29', 'None'), ('31', 'None'), ('33', 'None'), ('35', 'None'), ('37', 'None'), ('39', 'None'), ('41', '45'), ('47', 'None'), ('49', '55'), ('57', '63')], [], 
                        '''                        dscp
                        ''',
                        'dscp',
                        'ietf-qos', False, min_elements=1),
                ], min_elements=1),
            _MetaInfoClassMember('max-threshold', ATTRIBUTE, 'int' , None, None, 
                [('2', '10240')], [], 
                '''                max-threshold
                ''',
                'max_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('min-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10240')], [], 
                '''                min-threshold
                ''',
                'min_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('probability', ATTRIBUTE, 'int' , None, None, 
                [('1', '1023')], [], 
                '''                probability
                ''',
                'probability',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'profile-1',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue.Profile2.DscpEnum' : _MetaInfoEnum('DscpEnum', 'ydk.models.ietf.ietf_qos',
        {
            'af11':'af11',
            'af12':'af12',
            'af13':'af13',
            'af21':'af21',
            'af22':'af22',
            'af23':'af23',
            'af31':'af31',
            'af32':'af32',
            'af33':'af33',
            'af41':'af41',
            'af42':'af42',
            'af43':'af43',
            'cs1':'cs1',
            'cs2':'cs2',
            'cs3':'cs3',
            'cs4':'cs4',
            'cs5':'cs5',
            'cs6':'cs6',
            'cs7':'cs7',
            'df':'df',
            'ef':'ef',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue.Profile2' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue.Profile2',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                dscp
                ''',
                'dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2.DscpEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2.DscpEnum', 
                        [], [], 
                        '''                        dscp
                        ''',
                        'dscp',
                        'ietf-qos', False, min_elements=1),
                    _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('1', '7'), ('9', 'None'), ('11', 'None'), ('13', 'None'), ('15', 'None'), ('17', 'None'), ('19', 'None'), ('21', 'None'), ('23', 'None'), ('25', 'None'), ('27', 'None'), ('29', 'None'), ('31', 'None'), ('33', 'None'), ('35', 'None'), ('37', 'None'), ('39', 'None'), ('41', '45'), ('47', 'None'), ('49', '55'), ('57', '63')], [], 
                        '''                        dscp
                        ''',
                        'dscp',
                        'ietf-qos', False, min_elements=1),
                ], min_elements=1),
            _MetaInfoClassMember('max-threshold', ATTRIBUTE, 'int' , None, None, 
                [('2', '10240')], [], 
                '''                max-threshold
                ''',
                'max_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('min-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10240')], [], 
                '''                min-threshold
                ''',
                'min_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('probability', ATTRIBUTE, 'int' , None, None, 
                [('1', '1023')], [], 
                '''                probability
                ''',
                'probability',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'profile-2',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue',
            False, 
            [
            _MetaInfoClassMember('num', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                queue number
                ''',
                'num',
                'ietf-qos', True),
            _MetaInfoClassMember('default', REFERENCE_CLASS, 'Default' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue.Default', 
                [], [], 
                '''                default drop profile
                ''',
                'default',
                'ietf-qos', False),
            _MetaInfoClassMember('depth', ATTRIBUTE, 'int' , None, None, 
                [('1', '65536')], [], 
                '''                depth
                ''',
                'depth',
                'ietf-qos', False),
            _MetaInfoClassMember('profile-1', REFERENCE_CLASS, 'Profile1' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue.Profile1', 
                [], [], 
                '''                drop profile-1
                ''',
                'profile_1',
                'ietf-qos', False),
            _MetaInfoClassMember('profile-2', REFERENCE_CLASS, 'Profile2' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue.Profile2', 
                [], [], 
                '''                drop profile-2
                ''',
                'profile_2',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'queue',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1',
            False, 
            [
            _MetaInfoClassMember('queue', REFERENCE_LIST, 'Queue' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue', 
                [], [], 
                '''                queue
                ''',
                'queue',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'card-family-1',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue.Default' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue.Default',
            False, 
            [
            _MetaInfoClassMember('max-threshold', ATTRIBUTE, 'int' , None, None, 
                [('2', '10240')], [], 
                '''                max-threshold
                ''',
                'max_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('min-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10240')], [], 
                '''                min-threshold
                ''',
                'min_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('probability', ATTRIBUTE, 'int' , None, None, 
                [('1', '1023')], [], 
                '''                probability
                ''',
                'probability',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'default',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue.Profile1.DscpEnum' : _MetaInfoEnum('DscpEnum', 'ydk.models.ietf.ietf_qos',
        {
            'af11':'af11',
            'af12':'af12',
            'af13':'af13',
            'af21':'af21',
            'af22':'af22',
            'af23':'af23',
            'af31':'af31',
            'af32':'af32',
            'af33':'af33',
            'af41':'af41',
            'af42':'af42',
            'af43':'af43',
            'cs1':'cs1',
            'cs2':'cs2',
            'cs3':'cs3',
            'cs4':'cs4',
            'cs5':'cs5',
            'cs6':'cs6',
            'cs7':'cs7',
            'df':'df',
            'ef':'ef',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue.Profile1' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue.Profile1',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                dscp
                ''',
                'dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2.DscpEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2.DscpEnum', 
                        [], [], 
                        '''                        dscp
                        ''',
                        'dscp',
                        'ietf-qos', False, min_elements=1),
                    _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('1', '7'), ('9', 'None'), ('11', 'None'), ('13', 'None'), ('15', 'None'), ('17', 'None'), ('19', 'None'), ('21', 'None'), ('23', 'None'), ('25', 'None'), ('27', 'None'), ('29', 'None'), ('31', 'None'), ('33', 'None'), ('35', 'None'), ('37', 'None'), ('39', 'None'), ('41', '45'), ('47', 'None'), ('49', '55'), ('57', '63')], [], 
                        '''                        dscp
                        ''',
                        'dscp',
                        'ietf-qos', False, min_elements=1),
                ], min_elements=1),
            _MetaInfoClassMember('max-threshold', ATTRIBUTE, 'int' , None, None, 
                [('2', '10240')], [], 
                '''                max-threshold
                ''',
                'max_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('min-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10240')], [], 
                '''                min-threshold
                ''',
                'min_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('probability', ATTRIBUTE, 'int' , None, None, 
                [('1', '1023')], [], 
                '''                probability
                ''',
                'probability',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'profile-1',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue.Profile2.DscpEnum' : _MetaInfoEnum('DscpEnum', 'ydk.models.ietf.ietf_qos',
        {
            'af11':'af11',
            'af12':'af12',
            'af13':'af13',
            'af21':'af21',
            'af22':'af22',
            'af23':'af23',
            'af31':'af31',
            'af32':'af32',
            'af33':'af33',
            'af41':'af41',
            'af42':'af42',
            'af43':'af43',
            'cs1':'cs1',
            'cs2':'cs2',
            'cs3':'cs3',
            'cs4':'cs4',
            'cs5':'cs5',
            'cs6':'cs6',
            'cs7':'cs7',
            'df':'df',
            'ef':'ef',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue.Profile2' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue.Profile2',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                dscp
                ''',
                'dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2.DscpEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2.DscpEnum', 
                        [], [], 
                        '''                        dscp
                        ''',
                        'dscp',
                        'ietf-qos', False, min_elements=1),
                    _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('1', '7'), ('9', 'None'), ('11', 'None'), ('13', 'None'), ('15', 'None'), ('17', 'None'), ('19', 'None'), ('21', 'None'), ('23', 'None'), ('25', 'None'), ('27', 'None'), ('29', 'None'), ('31', 'None'), ('33', 'None'), ('35', 'None'), ('37', 'None'), ('39', 'None'), ('41', '45'), ('47', 'None'), ('49', '55'), ('57', '63')], [], 
                        '''                        dscp
                        ''',
                        'dscp',
                        'ietf-qos', False, min_elements=1),
                ], min_elements=1),
            _MetaInfoClassMember('max-threshold', ATTRIBUTE, 'int' , None, None, 
                [('2', '10240')], [], 
                '''                max-threshold
                ''',
                'max_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('min-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10240')], [], 
                '''                min-threshold
                ''',
                'min_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('probability', ATTRIBUTE, 'int' , None, None, 
                [('1', '1023')], [], 
                '''                probability
                ''',
                'probability',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'profile-2',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue',
            False, 
            [
            _MetaInfoClassMember('num', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                queue number
                ''',
                'num',
                'ietf-qos', True),
            _MetaInfoClassMember('default', REFERENCE_CLASS, 'Default' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue.Default', 
                [], [], 
                '''                default drop profile
                ''',
                'default',
                'ietf-qos', False),
            _MetaInfoClassMember('depth', ATTRIBUTE, 'int' , None, None, 
                [('1', '65536')], [], 
                '''                depth
                ''',
                'depth',
                'ietf-qos', False),
            _MetaInfoClassMember('exponential-weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '15')], [], 
                '''                exponential-weight
                ''',
                'exponential_weight',
                'ietf-qos', False),
            _MetaInfoClassMember('profile-1', REFERENCE_CLASS, 'Profile1' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue.Profile1', 
                [], [], 
                '''                drop profile-1
                ''',
                'profile_1',
                'ietf-qos', False),
            _MetaInfoClassMember('profile-2', REFERENCE_CLASS, 'Profile2' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue.Profile2', 
                [], [], 
                '''                drop profile-2
                ''',
                'profile_2',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'queue',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2',
            False, 
            [
            _MetaInfoClassMember('queue', REFERENCE_LIST, 'Queue' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue', 
                [], [], 
                '''                queue
                ''',
                'queue',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'card-family-2',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Default' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Default',
            False, 
            [
            _MetaInfoClassMember('max-threshold', ATTRIBUTE, 'int' , None, None, 
                [('2', '10240')], [], 
                '''                max-threshold
                ''',
                'max_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('min-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10240')], [], 
                '''                min-threshold
                ''',
                'min_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('probability', ATTRIBUTE, 'int' , None, None, 
                [('1', '1023')], [], 
                '''                probability
                ''',
                'probability',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'default',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile1.DscpEnum' : _MetaInfoEnum('DscpEnum', 'ydk.models.ietf.ietf_qos',
        {
            'af11':'af11',
            'af12':'af12',
            'af13':'af13',
            'af21':'af21',
            'af22':'af22',
            'af23':'af23',
            'af31':'af31',
            'af32':'af32',
            'af33':'af33',
            'af41':'af41',
            'af42':'af42',
            'af43':'af43',
            'cs1':'cs1',
            'cs2':'cs2',
            'cs3':'cs3',
            'cs4':'cs4',
            'cs5':'cs5',
            'cs6':'cs6',
            'cs7':'cs7',
            'df':'df',
            'ef':'ef',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile1' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile1',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                dscp
                ''',
                'dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2.DscpEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2.DscpEnum', 
                        [], [], 
                        '''                        dscp
                        ''',
                        'dscp',
                        'ietf-qos', False, min_elements=1),
                    _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('1', '7'), ('9', 'None'), ('11', 'None'), ('13', 'None'), ('15', 'None'), ('17', 'None'), ('19', 'None'), ('21', 'None'), ('23', 'None'), ('25', 'None'), ('27', 'None'), ('29', 'None'), ('31', 'None'), ('33', 'None'), ('35', 'None'), ('37', 'None'), ('39', 'None'), ('41', '45'), ('47', 'None'), ('49', '55'), ('57', '63')], [], 
                        '''                        dscp
                        ''',
                        'dscp',
                        'ietf-qos', False, min_elements=1),
                ], min_elements=1),
            _MetaInfoClassMember('max-threshold', ATTRIBUTE, 'int' , None, None, 
                [('2', '10240')], [], 
                '''                max-threshold
                ''',
                'max_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('min-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10240')], [], 
                '''                min-threshold
                ''',
                'min_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('probability', ATTRIBUTE, 'int' , None, None, 
                [('1', '1023')], [], 
                '''                probability
                ''',
                'probability',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'profile-1',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2.DscpEnum' : _MetaInfoEnum('DscpEnum', 'ydk.models.ietf.ietf_qos',
        {
            'af11':'af11',
            'af12':'af12',
            'af13':'af13',
            'af21':'af21',
            'af22':'af22',
            'af23':'af23',
            'af31':'af31',
            'af32':'af32',
            'af33':'af33',
            'af41':'af41',
            'af42':'af42',
            'af43':'af43',
            'cs1':'cs1',
            'cs2':'cs2',
            'cs3':'cs3',
            'cs4':'cs4',
            'cs5':'cs5',
            'cs6':'cs6',
            'cs7':'cs7',
            'df':'df',
            'ef':'ef',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                dscp
                ''',
                'dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2.DscpEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2.DscpEnum', 
                        [], [], 
                        '''                        dscp
                        ''',
                        'dscp',
                        'ietf-qos', False, min_elements=1),
                    _MetaInfoClassMember('dscp', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('1', '7'), ('9', 'None'), ('11', 'None'), ('13', 'None'), ('15', 'None'), ('17', 'None'), ('19', 'None'), ('21', 'None'), ('23', 'None'), ('25', 'None'), ('27', 'None'), ('29', 'None'), ('31', 'None'), ('33', 'None'), ('35', 'None'), ('37', 'None'), ('39', 'None'), ('41', '45'), ('47', 'None'), ('49', '55'), ('57', '63')], [], 
                        '''                        dscp
                        ''',
                        'dscp',
                        'ietf-qos', False, min_elements=1),
                ], min_elements=1),
            _MetaInfoClassMember('max-threshold', ATTRIBUTE, 'int' , None, None, 
                [('2', '10240')], [], 
                '''                max-threshold
                ''',
                'max_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('min-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10240')], [], 
                '''                min-threshold
                ''',
                'min_threshold',
                'ietf-qos', False),
            _MetaInfoClassMember('probability', ATTRIBUTE, 'int' , None, None, 
                [('1', '1023')], [], 
                '''                probability
                ''',
                'probability',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'profile-2',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue',
            False, 
            [
            _MetaInfoClassMember('num', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                queue number
                ''',
                'num',
                'ietf-qos', True),
            _MetaInfoClassMember('average-packet-size', ATTRIBUTE, 'int' , None, None, 
                [('128', '9600')], [], 
                '''                Packet size must be multiples of 128
                ''',
                'average_packet_size',
                'ietf-qos', False),
            _MetaInfoClassMember('default', REFERENCE_CLASS, 'Default' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Default', 
                [], [], 
                '''                default drop profile
                ''',
                'default',
                'ietf-qos', False),
            _MetaInfoClassMember('depth', ATTRIBUTE, 'int' , None, None, 
                [('1', '65536')], [], 
                '''                depth
                ''',
                'depth',
                'ietf-qos', False),
            _MetaInfoClassMember('exponential-weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '15')], [], 
                '''                exponential-weight
                ''',
                'exponential_weight',
                'ietf-qos', False),
            _MetaInfoClassMember('profile-1', REFERENCE_CLASS, 'Profile1' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile1', 
                [], [], 
                '''                drop profile-1
                ''',
                'profile_1',
                'ietf-qos', False),
            _MetaInfoClassMember('profile-2', REFERENCE_CLASS, 'Profile2' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2', 
                [], [], 
                '''                drop profile-2
                ''',
                'profile_2',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'queue',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3',
            False, 
            [
            _MetaInfoClassMember('queue', REFERENCE_LIST, 'Queue' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue', 
                [], [], 
                '''                queue
                ''',
                'queue',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'card-family-3',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq',
            False, 
            [
            _MetaInfoClassMember('card-family-1', REFERENCE_CLASS, 'CardFamily1' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1', 
                [], [], 
                '''                card-family-1
                ''',
                'card_family_1',
                'ietf-qos', False),
            _MetaInfoClassMember('card-family-2', REFERENCE_CLASS, 'CardFamily2' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2', 
                [], [], 
                '''                card-family-2
                ''',
                'card_family_2',
                'ietf-qos', False),
            _MetaInfoClassMember('card-family-3', REFERENCE_CLASS, 'CardFamily3' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3', 
                [], [], 
                '''                card-family-3
                ''',
                'card_family_3',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'pwfq',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                congestion-avoidance-map name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('mdrr', REFERENCE_CLASS, 'Mdrr' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr', 
                [], [], 
                '''                mdrr
                ''',
                'mdrr',
                'ietf-qos', False),
            _MetaInfoClassMember('pwfq', REFERENCE_CLASS, 'Pwfq' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq', 
                [], [], 
                '''                pwfq
                ''',
                'pwfq',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'congestion-avoidance-map',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.CongestionAvoidanceMaps' : {
        'meta_info' : _MetaInfoClass('Qos.CongestionAvoidanceMaps',
            False, 
            [
            _MetaInfoClassMember('congestion-avoidance-map', REFERENCE_LIST, 'CongestionAvoidanceMap' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap', 
                [], [], 
                '''                congestion-avoidance-map
                ''',
                'congestion_avoidance_map',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'congestion-avoidance-maps',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily1.EncapsAccessLine' : {
        'meta_info' : _MetaInfoClass('Qos.Profiles.Profile.Overhead.CardFamily.CardFamily1.EncapsAccessLine',
            False, 
            [
            _MetaInfoClassMember('ethernet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ethernet
                ''',
                'ethernet',
                'ietf-qos', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value
                ''',
                'value',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'encaps-access-line',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily1' : {
        'meta_info' : _MetaInfoClass('Qos.Profiles.Profile.Overhead.CardFamily.CardFamily1',
            False, 
            [
            _MetaInfoClassMember('encaps-access-line', REFERENCE_CLASS, 'EncapsAccessLine' , 'ydk.models.ietf.ietf_qos', 'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily1.EncapsAccessLine', 
                [], [], 
                '''                encaps-access-line
                ''',
                'encaps_access_line',
                'ietf-qos', False),
            _MetaInfoClassMember('reserved', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                reserved
                ''',
                'reserved',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'card-family-1',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2.EncapsAccessLine.Value.DataLink' : {
        'meta_info' : _MetaInfoClass('Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2.EncapsAccessLine.Value.DataLink',
            False, 
            [
            _MetaInfoClassMember('atm', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                atm
                ''',
                'atm',
                'ietf-qos', False),
            _MetaInfoClassMember('ethernet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ethernet
                ''',
                'ethernet',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'data-link',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2.EncapsAccessLine.Value' : {
        'meta_info' : _MetaInfoClass('Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2.EncapsAccessLine.Value',
            False, 
            [
            _MetaInfoClassMember('data-link', REFERENCE_CLASS, 'DataLink' , 'ydk.models.ietf.ietf_qos', 'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2.EncapsAccessLine.Value.DataLink', 
                [], [], 
                '''                data-link
                ''',
                'data_link',
                'ietf-qos', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value
                ''',
                'value',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'value',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2.EncapsAccessLine' : {
        'meta_info' : _MetaInfoClass('Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2.EncapsAccessLine',
            False, 
            [
            _MetaInfoClassMember('ether-aal5-llc', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ether-aal5-llc
                ''',
                'ether_aal5_llc',
                'ietf-qos', False),
            _MetaInfoClassMember('ether-aal5-llc-fcs', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ether-aal5-llc-fcs
                ''',
                'ether_aal5_llc_fcs',
                'ietf-qos', False),
            _MetaInfoClassMember('ether-aal5-null', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ether-aal5-null
                ''',
                'ether_aal5_null',
                'ietf-qos', False),
            _MetaInfoClassMember('ether-aal5-null-fcs', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ether-aal5-null-fcs
                ''',
                'ether_aal5_null_fcs',
                'ietf-qos', False),
            _MetaInfoClassMember('ethernet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ethernet
                ''',
                'ethernet',
                'ietf-qos', False),
            _MetaInfoClassMember('ipoa-llc', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ipoa-llc
                ''',
                'ipoa_llc',
                'ietf-qos', False),
            _MetaInfoClassMember('ipoa-null', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ipoa-null
                ''',
                'ipoa_null',
                'ietf-qos', False),
            _MetaInfoClassMember('pppoa-llc', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                pppoa-llc
                ''',
                'pppoa_llc',
                'ietf-qos', False),
            _MetaInfoClassMember('pppoa-null', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                pppoa-null
                ''',
                'pppoa_null',
                'ietf-qos', False),
            _MetaInfoClassMember('value', REFERENCE_CLASS, 'Value' , 'ydk.models.ietf.ietf_qos', 'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2.EncapsAccessLine.Value', 
                [], [], 
                '''                value
                ''',
                'value',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'encaps-access-line',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2' : {
        'meta_info' : _MetaInfoClass('Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2',
            False, 
            [
            _MetaInfoClassMember('encaps-access-line', REFERENCE_CLASS, 'EncapsAccessLine' , 'ydk.models.ietf.ietf_qos', 'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2.EncapsAccessLine', 
                [], [], 
                '''                encaps-access-line
                ''',
                'encaps_access_line',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-factor', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                rate-factor
                ''',
                'rate_factor',
                'ietf-qos', False),
            _MetaInfoClassMember('reserved', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                reserved
                ''',
                'reserved',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'card-family-2',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3.EncapsAccessLine.Value.DataLink' : {
        'meta_info' : _MetaInfoClass('Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3.EncapsAccessLine.Value.DataLink',
            False, 
            [
            _MetaInfoClassMember('atm', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                atm
                ''',
                'atm',
                'ietf-qos', False),
            _MetaInfoClassMember('ethernet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ethernet
                ''',
                'ethernet',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'data-link',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3.EncapsAccessLine.Value' : {
        'meta_info' : _MetaInfoClass('Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3.EncapsAccessLine.Value',
            False, 
            [
            _MetaInfoClassMember('data-link', REFERENCE_CLASS, 'DataLink' , 'ydk.models.ietf.ietf_qos', 'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3.EncapsAccessLine.Value.DataLink', 
                [], [], 
                '''                data-link
                ''',
                'data_link',
                'ietf-qos', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value
                ''',
                'value',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'value',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3.EncapsAccessLine' : {
        'meta_info' : _MetaInfoClass('Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3.EncapsAccessLine',
            False, 
            [
            _MetaInfoClassMember('ether-aal5-llc', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ether-aal5-llc
                ''',
                'ether_aal5_llc',
                'ietf-qos', False),
            _MetaInfoClassMember('ether-aal5-llc-fcs', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ether-aal5-llc-fcs
                ''',
                'ether_aal5_llc_fcs',
                'ietf-qos', False),
            _MetaInfoClassMember('ether-aal5-null', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ether-aal5-null
                ''',
                'ether_aal5_null',
                'ietf-qos', False),
            _MetaInfoClassMember('ether-aal5-null-fcs', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ether-aal5-null-fcs
                ''',
                'ether_aal5_null_fcs',
                'ietf-qos', False),
            _MetaInfoClassMember('ethernet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ethernet
                ''',
                'ethernet',
                'ietf-qos', False),
            _MetaInfoClassMember('ipoa-llc', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ipoa-llc
                ''',
                'ipoa_llc',
                'ietf-qos', False),
            _MetaInfoClassMember('ipoa-null', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ipoa-null
                ''',
                'ipoa_null',
                'ietf-qos', False),
            _MetaInfoClassMember('pppoa-llc', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                pppoa-llc
                ''',
                'pppoa_llc',
                'ietf-qos', False),
            _MetaInfoClassMember('pppoa-null', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                pppoa-null
                ''',
                'pppoa_null',
                'ietf-qos', False),
            _MetaInfoClassMember('value', REFERENCE_CLASS, 'Value' , 'ydk.models.ietf.ietf_qos', 'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3.EncapsAccessLine.Value', 
                [], [], 
                '''                value
                ''',
                'value',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'encaps-access-line',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3' : {
        'meta_info' : _MetaInfoClass('Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3',
            False, 
            [
            _MetaInfoClassMember('encaps-access-line', REFERENCE_CLASS, 'EncapsAccessLine' , 'ydk.models.ietf.ietf_qos', 'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3.EncapsAccessLine', 
                [], [], 
                '''                encaps-access-line
                ''',
                'encaps_access_line',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-factor', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                rate-factor
                ''',
                'rate_factor',
                'ietf-qos', False),
            _MetaInfoClassMember('reserved', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                reserved
                ''',
                'reserved',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'card-family-3',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Profiles.Profile.Overhead.CardFamily' : {
        'meta_info' : _MetaInfoClass('Qos.Profiles.Profile.Overhead.CardFamily',
            False, 
            [
            _MetaInfoClassMember('card-family-1', REFERENCE_CLASS, 'CardFamily1' , 'ydk.models.ietf.ietf_qos', 'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily1', 
                [], [], 
                '''                card-family-1
                ''',
                'card_family_1',
                'ietf-qos', False),
            _MetaInfoClassMember('card-family-2', REFERENCE_CLASS, 'CardFamily2' , 'ydk.models.ietf.ietf_qos', 'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2', 
                [], [], 
                '''                2
                ''',
                'card_family_2',
                'ietf-qos', False),
            _MetaInfoClassMember('card-family-3', REFERENCE_CLASS, 'CardFamily3' , 'ydk.models.ietf.ietf_qos', 'Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3', 
                [], [], 
                '''                3
                ''',
                'card_family_3',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'card-family',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Profiles.Profile.Overhead' : {
        'meta_info' : _MetaInfoClass('Qos.Profiles.Profile.Overhead',
            False, 
            [
            _MetaInfoClassMember('card-family', REFERENCE_CLASS, 'CardFamily' , 'ydk.models.ietf.ietf_qos', 'Qos.Profiles.Profile.Overhead.CardFamily', 
                [], [], 
                '''                card-family
                ''',
                'card_family',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'overhead',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Profiles.Profile.SlotPort' : {
        'meta_info' : _MetaInfoClass('Qos.Profiles.Profile.SlotPort',
            False, 
            [
            _MetaInfoClassMember('slot-port', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                slot-port
                ''',
                'slot_port',
                'ietf-qos', False),
            _MetaInfoClassMember('tm-resource', ATTRIBUTE, 'int' , None, None, 
                [('1', '4')], [], 
                '''                tm-resource
                ''',
                'tm_resource',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'slot-port',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Profiles.Profile' : {
        'meta_info' : _MetaInfoClass('Qos.Profiles.Profile',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                qos-profile name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('overhead', REFERENCE_CLASS, 'Overhead' , 'ydk.models.ietf.ietf_qos', 'Qos.Profiles.Profile.Overhead', 
                [], [], 
                '''                overhead
                ''',
                'overhead',
                'ietf-qos', False),
            _MetaInfoClassMember('resource', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                resource
                ''',
                'resource',
                'ietf-qos', False),
            _MetaInfoClassMember('slot-port', REFERENCE_CLASS, 'SlotPort' , 'ydk.models.ietf.ietf_qos', 'Qos.Profiles.Profile.SlotPort', 
                [], [], 
                '''                slot-port
                ''',
                'slot_port',
                'ietf-qos', False),
            _MetaInfoClassMember('tm-resource', ATTRIBUTE, 'int' , None, None, 
                [('1', '4')], [], 
                '''                tm-resource
                ''',
                'tm_resource',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'profile',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Profiles' : {
        'meta_info' : _MetaInfoClass('Qos.Profiles',
            False, 
            [
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile' , 'ydk.models.ietf.ietf_qos', 'Qos.Profiles.Profile', 
                [], [], 
                '''                profile
                ''',
                'profile',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'profiles',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.QueueMaps.QueueMap.NumQueues.Queue' : {
        'meta_info' : _MetaInfoClass('Qos.QueueMaps.QueueMap.NumQueues.Queue',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                queue
                ''',
                'id',
                'ietf-qos', True),
            _MetaInfoClassMember('priority', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '7')], [], 
                '''                priority
                ''',
                'priority',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'queue',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.QueueMaps.QueueMap.NumQueues' : {
        'meta_info' : _MetaInfoClass('Qos.QueueMaps.QueueMap.NumQueues',
            False, 
            [
            _MetaInfoClassMember('num', ATTRIBUTE, 'int' , None, None, 
                [('2', 'None'), ('4', 'None'), ('8', 'None')], [], 
                '''                num-queues
                ''',
                'num',
                'ietf-qos', True),
            _MetaInfoClassMember('queue', REFERENCE_LIST, 'Queue' , 'ydk.models.ietf.ietf_qos', 'Qos.QueueMaps.QueueMap.NumQueues.Queue', 
                [], [], 
                '''                queue
                ''',
                'queue',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'num-queues',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.QueueMaps.QueueMap' : {
        'meta_info' : _MetaInfoClass('Qos.QueueMaps.QueueMap',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                queue-map-name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('num-queues', REFERENCE_LIST, 'NumQueues' , 'ydk.models.ietf.ietf_qos', 'Qos.QueueMaps.QueueMap.NumQueues', 
                [], [], 
                '''                num-queues
                ''',
                'num_queues',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'queue-map',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.QueueMaps' : {
        'meta_info' : _MetaInfoClass('Qos.QueueMaps',
            False, 
            [
            _MetaInfoClassMember('queue-map', REFERENCE_LIST, 'QueueMap' , 'ydk.models.ietf.ietf_qos', 'Qos.QueueMaps.QueueMap', 
                [], [], 
                '''                queue-map
                ''',
                'queue_map',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'queue-maps',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'conform-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'exceed-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions',
            False, 
            [
            _MetaInfoClassMember('conform-handling', REFERENCE_CLASS, 'ConformHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling', 
                [], [], 
                '''                conform-handling
                ''',
                'conform_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('exceed-handling', REFERENCE_CLASS, 'ExceedHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling', 
                [], [], 
                '''                exceed-handling
                ''',
                'exceed_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'actions',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate',
            False, 
            [
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions', 
                [], [], 
                '''                actions
                ''',
                'actions',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', ATTRIBUTE, 'int' , None, None, 
                [('66', '100000000')], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                excess-burst
                ''',
                'excess_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('time-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-burst
                ''',
                'time_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('time-excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-excess-burst
                ''',
                'time_excess_burst',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'bit-rate',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage',
            False, 
            [
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                percentage
                ''',
                'percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'percentage',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', REFERENCE_CLASS, 'BitRate' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate', 
                [], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('parent-class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                parent-class
                ''',
                'parent_class',
                'ietf-qos', False),
            _MetaInfoClassMember('percentage', REFERENCE_CLASS, 'Percentage' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage', 
                [], [], 
                '''                percentage
                ''',
                'percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'packet-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 39)], [], 
                '''                name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('packet-handling', REFERENCE_CLASS, 'PacketHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling', 
                [], [], 
                '''                packet-handling
                ''',
                'packet_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_', 
                [], [], 
                '''                class
                ''',
                'class_',
                'ietf-qos', False, max_elements=8),
            ],
            'ietf-qos',
            'classes',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup',
            False, 
            [
            _MetaInfoClassMember('class-group-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                class-group-reference
                ''',
                'class_group_reference',
                'ietf-qos', False),
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes', 
                [], [], 
                '''                classes
                ''',
                'classes',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.IpAccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.IpAccessGroup',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                context-name
                ''',
                'context_name',
                'ietf-qos', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ip-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.Ipv6AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.Ipv6AccessGroup',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                context-name
                ''',
                'context_name',
                'ietf-qos', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ipv6-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.L2AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.L2AccessGroup',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'l2-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.Classes.Class_.PacketHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.Classes.Class_.PacketHandling',
            False, 
            [
            _MetaInfoClassMember('parent-class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                parent-class
                ''',
                'parent_class',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'packet-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('packet-handling', REFERENCE_CLASS, 'PacketHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.Classes.Class_.PacketHandling', 
                [], [], 
                '''                packet-handling
                ''',
                'packet_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.Classes' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.Classes.Class_', 
                [], [], 
                '''                class
                ''',
                'class_',
                'ietf-qos', False, max_elements=8),
            ],
            'ietf-qos',
            'classes',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup',
            False, 
            [
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.Classes', 
                [], [], 
                '''                classes
                ''',
                'classes',
                'ietf-qos', False),
            _MetaInfoClassMember('ip-access-group', REFERENCE_CLASS, 'IpAccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.IpAccessGroup', 
                [], [], 
                '''                Reference an IPv4 policy
                ''',
                'ip_access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('ipv6-access-group', REFERENCE_CLASS, 'Ipv6AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.Ipv6AccessGroup', 
                [], [], 
                '''                Reference an IPv6 policy
                ''',
                'ipv6_access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('l2-access-group', REFERENCE_CLASS, 'L2AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.L2AccessGroup', 
                [], [], 
                '''                Reference a layer-2 policy
                ''',
                'l2_access_group',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Policy_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Policy_',
            False, 
            [
            _MetaInfoClassMember('access-group', REFERENCE_CLASS, 'AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup', 
                [], [], 
                '''                access-group
                ''',
                'access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('class-group', REFERENCE_CLASS, 'ClassGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup', 
                [], [], 
                '''                Reference a previously defined class
                ''',
                'class_group',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'policy',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Rate.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Rate.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Rate.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Rate.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Rate.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Rate.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Rate.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions.ConformHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions.ConformHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions.ConformHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions.ConformHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'conform-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions.ExceedHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions.ExceedHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions.ExceedHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions.ExceedHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'exceed-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions.ViolateHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions.ViolateHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions.ViolateHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions.ViolateHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'violate-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions',
            False, 
            [
            _MetaInfoClassMember('conform-handling', REFERENCE_CLASS, 'ConformHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions.ConformHandling', 
                [], [], 
                '''                conform-handling
                ''',
                'conform_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('exceed-handling', REFERENCE_CLASS, 'ExceedHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions.ExceedHandling', 
                [], [], 
                '''                exceed-handling
                ''',
                'exceed_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('violate-handling', REFERENCE_CLASS, 'ViolateHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions.ViolateHandling', 
                [], [], 
                '''                violate-handling
                ''',
                'violate_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'actions',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.Rate' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1.Rate',
            False, 
            [
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions', 
                [], [], 
                '''                actions
                ''',
                'actions',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', ATTRIBUTE, 'int' , None, None, 
                [('66', '100000000')], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Rate.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                excess-burst
                ''',
                'excess_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Rate.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('informational', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                informational
                ''',
                'informational',
                'ietf-qos', False),
            _MetaInfoClassMember('time-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-burst
                ''',
                'time_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('time-excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-excess-burst
                ''',
                'time_excess_burst',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily1.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily1.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily1' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily1',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('policy', REFERENCE_CLASS, 'Policy_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Policy_', 
                [], [], 
                '''                policy
                ''',
                'policy',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', REFERENCE_CLASS, 'Rate' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1.Rate', 
                [], [], 
                '''                Specify rate limits inline
                ''',
                'rate',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-calculation-exclude-layer-2-overhead', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify that rate calculation excludes the size ofLayer 2 overhead for the layer 3 circuit on which a policy is applied
                ''',
                'rate_calculation_exclude_layer_2_overhead',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'card-family-1',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'conform-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'exceed-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions',
            False, 
            [
            _MetaInfoClassMember('conform-handling', REFERENCE_CLASS, 'ConformHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling', 
                [], [], 
                '''                conform-handling
                ''',
                'conform_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('exceed-handling', REFERENCE_CLASS, 'ExceedHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling', 
                [], [], 
                '''                exceed-handling
                ''',
                'exceed_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'actions',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate',
            False, 
            [
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions', 
                [], [], 
                '''                actions
                ''',
                'actions',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', ATTRIBUTE, 'int' , None, None, 
                [('5', '100000000')], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                excess-burst
                ''',
                'excess_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('time-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-burst
                ''',
                'time_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('time-excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-excess-burst
                ''',
                'time_excess_burst',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'bit-rate',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage',
            False, 
            [
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                percentage
                ''',
                'percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'percentage',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', REFERENCE_CLASS, 'BitRate' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate', 
                [], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('parent-class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                parent-class
                ''',
                'parent_class',
                'ietf-qos', False),
            _MetaInfoClassMember('percentage', REFERENCE_CLASS, 'Percentage' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage', 
                [], [], 
                '''                percentage
                ''',
                'percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'packet-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 39)], [], 
                '''                name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('packet-handling', REFERENCE_CLASS, 'PacketHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling', 
                [], [], 
                '''                packet-handling
                ''',
                'packet_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_', 
                [], [], 
                '''                class
                ''',
                'class_',
                'ietf-qos', False, max_elements=8),
            ],
            'ietf-qos',
            'classes',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup',
            False, 
            [
            _MetaInfoClassMember('class-group-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                class-group-reference
                ''',
                'class_group_reference',
                'ietf-qos', False),
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes', 
                [], [], 
                '''                classes
                ''',
                'classes',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.IpAccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.IpAccessGroup',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                context-name
                ''',
                'context_name',
                'ietf-qos', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ip-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.Ipv6AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.Ipv6AccessGroup',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                context-name
                ''',
                'context_name',
                'ietf-qos', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ipv6-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.L2AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.L2AccessGroup',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'l2-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.Classes.Class_.PacketHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.Classes.Class_.PacketHandling',
            False, 
            [
            _MetaInfoClassMember('parent-class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                parent-class
                ''',
                'parent_class',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'packet-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('packet-handling', REFERENCE_CLASS, 'PacketHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.Classes.Class_.PacketHandling', 
                [], [], 
                '''                packet-handling
                ''',
                'packet_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.Classes' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.Classes.Class_', 
                [], [], 
                '''                class
                ''',
                'class_',
                'ietf-qos', False, max_elements=8),
            ],
            'ietf-qos',
            'classes',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup',
            False, 
            [
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.Classes', 
                [], [], 
                '''                classes
                ''',
                'classes',
                'ietf-qos', False),
            _MetaInfoClassMember('ip-access-group', REFERENCE_CLASS, 'IpAccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.IpAccessGroup', 
                [], [], 
                '''                Reference an IPv4 policy
                ''',
                'ip_access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('ipv6-access-group', REFERENCE_CLASS, 'Ipv6AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.Ipv6AccessGroup', 
                [], [], 
                '''                Reference an IPv6 policy
                ''',
                'ipv6_access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('l2-access-group', REFERENCE_CLASS, 'L2AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.L2AccessGroup', 
                [], [], 
                '''                Reference a layer-2 policy
                ''',
                'l2_access_group',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Policy_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Policy_',
            False, 
            [
            _MetaInfoClassMember('access-group', REFERENCE_CLASS, 'AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup', 
                [], [], 
                '''                access-group
                ''',
                'access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('class-group', REFERENCE_CLASS, 'ClassGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup', 
                [], [], 
                '''                Reference a previously defined class
                ''',
                'class_group',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'policy',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Rate.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Rate.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Rate.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Rate.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Rate.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Rate.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Rate.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions.ConformHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions.ConformHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions.ConformHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions.ConformHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'conform-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions.ExceedHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions.ExceedHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions.ExceedHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions.ExceedHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'exceed-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions.ViolateHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions.ViolateHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions.ViolateHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions.ViolateHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'violate-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions',
            False, 
            [
            _MetaInfoClassMember('conform-handling', REFERENCE_CLASS, 'ConformHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions.ConformHandling', 
                [], [], 
                '''                conform-handling
                ''',
                'conform_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('exceed-handling', REFERENCE_CLASS, 'ExceedHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions.ExceedHandling', 
                [], [], 
                '''                exceed-handling
                ''',
                'exceed_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('violate-handling', REFERENCE_CLASS, 'ViolateHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions.ViolateHandling', 
                [], [], 
                '''                violate-handling
                ''',
                'violate_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'actions',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.Rate' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2.Rate',
            False, 
            [
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions', 
                [], [], 
                '''                actions
                ''',
                'actions',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', ATTRIBUTE, 'int' , None, None, 
                [('5', '100000000')], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Rate.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                excess-burst
                ''',
                'excess_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Rate.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('informational', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                informational
                ''',
                'informational',
                'ietf-qos', False),
            _MetaInfoClassMember('time-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-burst
                ''',
                'time_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('time-excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-excess-burst
                ''',
                'time_excess_burst',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily2.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily2.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily2' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily2',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('policy', REFERENCE_CLASS, 'Policy_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Policy_', 
                [], [], 
                '''                policy
                ''',
                'policy',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', REFERENCE_CLASS, 'Rate' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2.Rate', 
                [], [], 
                '''                Specify rate limits inline
                ''',
                'rate',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-calculation-exclude-layer-2-overhead', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify that rate calculation excludes the size ofLayer 2 overhead for the layer 3 circuit on which a policy is applied
                ''',
                'rate_calculation_exclude_layer_2_overhead',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'card-family-2',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'conform-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'exceed-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions',
            False, 
            [
            _MetaInfoClassMember('conform-handling', REFERENCE_CLASS, 'ConformHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling', 
                [], [], 
                '''                conform-handling
                ''',
                'conform_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('exceed-handling', REFERENCE_CLASS, 'ExceedHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling', 
                [], [], 
                '''                exceed-handling
                ''',
                'exceed_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'actions',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate',
            False, 
            [
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions', 
                [], [], 
                '''                actions
                ''',
                'actions',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', ATTRIBUTE, 'int' , None, None, 
                [('66', '100000000')], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                excess-burst
                ''',
                'excess_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('time-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-burst
                ''',
                'time_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('time-excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-excess-burst
                ''',
                'time_excess_burst',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'bit-rate',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage',
            False, 
            [
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                percentage
                ''',
                'percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'percentage',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', REFERENCE_CLASS, 'BitRate' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate', 
                [], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('parent-class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                parent-class
                ''',
                'parent_class',
                'ietf-qos', False),
            _MetaInfoClassMember('percentage', REFERENCE_CLASS, 'Percentage' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage', 
                [], [], 
                '''                percentage
                ''',
                'percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'packet-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 39)], [], 
                '''                name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('packet-handling', REFERENCE_CLASS, 'PacketHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling', 
                [], [], 
                '''                packet-handling
                ''',
                'packet_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_', 
                [], [], 
                '''                class
                ''',
                'class_',
                'ietf-qos', False, max_elements=8),
            ],
            'ietf-qos',
            'classes',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup',
            False, 
            [
            _MetaInfoClassMember('class-group-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                class-group-reference
                ''',
                'class_group_reference',
                'ietf-qos', False),
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes', 
                [], [], 
                '''                classes
                ''',
                'classes',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.IpAccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.IpAccessGroup',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                context-name
                ''',
                'context_name',
                'ietf-qos', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ip-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.Ipv6AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.Ipv6AccessGroup',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                context-name
                ''',
                'context_name',
                'ietf-qos', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ipv6-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.L2AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.L2AccessGroup',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'l2-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.Classes.Class_.PacketHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.Classes.Class_.PacketHandling',
            False, 
            [
            _MetaInfoClassMember('parent-class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                parent-class
                ''',
                'parent_class',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'packet-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('packet-handling', REFERENCE_CLASS, 'PacketHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.Classes.Class_.PacketHandling', 
                [], [], 
                '''                packet-handling
                ''',
                'packet_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.Classes' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.Classes.Class_', 
                [], [], 
                '''                class
                ''',
                'class_',
                'ietf-qos', False, max_elements=8),
            ],
            'ietf-qos',
            'classes',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup',
            False, 
            [
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.Classes', 
                [], [], 
                '''                classes
                ''',
                'classes',
                'ietf-qos', False),
            _MetaInfoClassMember('ip-access-group', REFERENCE_CLASS, 'IpAccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.IpAccessGroup', 
                [], [], 
                '''                Reference an IPv4 policy
                ''',
                'ip_access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('ipv6-access-group', REFERENCE_CLASS, 'Ipv6AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.Ipv6AccessGroup', 
                [], [], 
                '''                Reference an IPv6 policy
                ''',
                'ipv6_access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('l2-access-group', REFERENCE_CLASS, 'L2AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.L2AccessGroup', 
                [], [], 
                '''                Reference a layer-2 policy
                ''',
                'l2_access_group',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Policy_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Policy_',
            False, 
            [
            _MetaInfoClassMember('access-group', REFERENCE_CLASS, 'AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup', 
                [], [], 
                '''                access-group
                ''',
                'access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('class-group', REFERENCE_CLASS, 'ClassGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup', 
                [], [], 
                '''                Reference a previously defined class
                ''',
                'class_group',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'policy',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Rate.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Rate.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Rate.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Rate.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Rate.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Rate.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Rate.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions.ConformHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions.ConformHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions.ConformHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions.ConformHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'conform-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions.ExceedHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions.ExceedHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions.ExceedHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions.ExceedHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'exceed-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions.ViolateHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions.ViolateHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions.ViolateHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions.ViolateHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'violate-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions',
            False, 
            [
            _MetaInfoClassMember('conform-handling', REFERENCE_CLASS, 'ConformHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions.ConformHandling', 
                [], [], 
                '''                conform-handling
                ''',
                'conform_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('exceed-handling', REFERENCE_CLASS, 'ExceedHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions.ExceedHandling', 
                [], [], 
                '''                exceed-handling
                ''',
                'exceed_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('violate-handling', REFERENCE_CLASS, 'ViolateHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions.ViolateHandling', 
                [], [], 
                '''                violate-handling
                ''',
                'violate_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'actions',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.Rate' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3.Rate',
            False, 
            [
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions', 
                [], [], 
                '''                actions
                ''',
                'actions',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', ATTRIBUTE, 'int' , None, None, 
                [('66', '100000000')], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Rate.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                excess-burst
                ''',
                'excess_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Rate.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('informational', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                informational
                ''',
                'informational',
                'ietf-qos', False),
            _MetaInfoClassMember('time-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-burst
                ''',
                'time_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('time-excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-excess-burst
                ''',
                'time_excess_burst',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.CardFamily3.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily3.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.CardFamily3' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.CardFamily3',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('policy', REFERENCE_CLASS, 'Policy_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Policy_', 
                [], [], 
                '''                policy
                ''',
                'policy',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', REFERENCE_CLASS, 'Rate' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3.Rate', 
                [], [], 
                '''                Specify rate limits inline
                ''',
                'rate',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-calculation-exclude-layer-2-overhead', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify that rate calculation excludes the size ofLayer 2 overhead for the layer 3 circuit on which a policy is applied
                ''',
                'rate_calculation_exclude_layer_2_overhead',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'card-family-3',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'conform-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'exceed-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions',
            False, 
            [
            _MetaInfoClassMember('conform-handling', REFERENCE_CLASS, 'ConformHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling', 
                [], [], 
                '''                conform-handling
                ''',
                'conform_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('exceed-handling', REFERENCE_CLASS, 'ExceedHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling', 
                [], [], 
                '''                exceed-handling
                ''',
                'exceed_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'actions',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate',
            False, 
            [
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions', 
                [], [], 
                '''                actions
                ''',
                'actions',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', ATTRIBUTE, 'int' , None, None, 
                [('66', '100000000')], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                excess-burst
                ''',
                'excess_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('time-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-burst
                ''',
                'time_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('time-excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-excess-burst
                ''',
                'time_excess_burst',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'bit-rate',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage',
            False, 
            [
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                percentage
                ''',
                'percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'percentage',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', REFERENCE_CLASS, 'BitRate' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate', 
                [], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('parent-class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                parent-class
                ''',
                'parent_class',
                'ietf-qos', False),
            _MetaInfoClassMember('percentage', REFERENCE_CLASS, 'Percentage' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage', 
                [], [], 
                '''                percentage
                ''',
                'percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'packet-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 39)], [], 
                '''                name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('packet-handling', REFERENCE_CLASS, 'PacketHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling', 
                [], [], 
                '''                packet-handling
                ''',
                'packet_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_', 
                [], [], 
                '''                class
                ''',
                'class_',
                'ietf-qos', False, max_elements=8),
            ],
            'ietf-qos',
            'classes',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.ClassGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.ClassGroup',
            False, 
            [
            _MetaInfoClassMember('class-group-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                class-group-reference
                ''',
                'class_group_reference',
                'ietf-qos', False),
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes', 
                [], [], 
                '''                classes
                ''',
                'classes',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.AccessGroup.IpAccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.AccessGroup.IpAccessGroup',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                context-name
                ''',
                'context_name',
                'ietf-qos', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ip-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.AccessGroup.Ipv6AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.AccessGroup.Ipv6AccessGroup',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                context-name
                ''',
                'context_name',
                'ietf-qos', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ipv6-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.AccessGroup.L2AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.AccessGroup.L2AccessGroup',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'l2-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.AccessGroup.Classes.Class_.PacketHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.AccessGroup.Classes.Class_.PacketHandling',
            False, 
            [
            _MetaInfoClassMember('parent-class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                parent-class
                ''',
                'parent_class',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'packet-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.AccessGroup.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.AccessGroup.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('packet-handling', REFERENCE_CLASS, 'PacketHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.AccessGroup.Classes.Class_.PacketHandling', 
                [], [], 
                '''                packet-handling
                ''',
                'packet_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.AccessGroup.Classes' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.AccessGroup.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.AccessGroup.Classes.Class_', 
                [], [], 
                '''                class
                ''',
                'class_',
                'ietf-qos', False, max_elements=8),
            ],
            'ietf-qos',
            'classes',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_.AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_.AccessGroup',
            False, 
            [
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.AccessGroup.Classes', 
                [], [], 
                '''                classes
                ''',
                'classes',
                'ietf-qos', False),
            _MetaInfoClassMember('ip-access-group', REFERENCE_CLASS, 'IpAccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.AccessGroup.IpAccessGroup', 
                [], [], 
                '''                Reference an IPv4 policy
                ''',
                'ip_access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('ipv6-access-group', REFERENCE_CLASS, 'Ipv6AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.AccessGroup.Ipv6AccessGroup', 
                [], [], 
                '''                Reference an IPv6 policy
                ''',
                'ipv6_access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('l2-access-group', REFERENCE_CLASS, 'L2AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.AccessGroup.L2AccessGroup', 
                [], [], 
                '''                Reference a layer-2 policy
                ''',
                'l2_access_group',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Policy_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Policy_',
            False, 
            [
            _MetaInfoClassMember('access-group', REFERENCE_CLASS, 'AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.AccessGroup', 
                [], [], 
                '''                access-group
                ''',
                'access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('class-group', REFERENCE_CLASS, 'ClassGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_.ClassGroup', 
                [], [], 
                '''                Reference a previously defined class
                ''',
                'class_group',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'policy',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Rate.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Rate.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Rate.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Rate.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Rate.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Rate.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Rate.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Rate.Actions.ConformHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.Rate.Actions.ConformHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.Rate.Actions.ConformHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Rate.Actions.ConformHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'conform-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Rate.Actions.ExceedHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.Rate.Actions.ExceedHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.Rate.Actions.ExceedHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Rate.Actions.ExceedHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'exceed-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Rate.Actions.ViolateHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.Rate.Actions.ViolateHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.Rate.Actions.ViolateHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Rate.Actions.ViolateHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'violate-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Rate.Actions' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Rate.Actions',
            False, 
            [
            _MetaInfoClassMember('conform-handling', REFERENCE_CLASS, 'ConformHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Rate.Actions.ConformHandling', 
                [], [], 
                '''                conform-handling
                ''',
                'conform_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('exceed-handling', REFERENCE_CLASS, 'ExceedHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Rate.Actions.ExceedHandling', 
                [], [], 
                '''                exceed-handling
                ''',
                'exceed_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('violate-handling', REFERENCE_CLASS, 'ViolateHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Rate.Actions.ViolateHandling', 
                [], [], 
                '''                violate-handling
                ''',
                'violate_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'actions',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.Rate' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering.Rate',
            False, 
            [
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Rate.Actions', 
                [], [], 
                '''                actions
                ''',
                'actions',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', ATTRIBUTE, 'int' , None, None, 
                [('66', '100000000')], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Rate.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                excess-burst
                ''',
                'excess_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Rate.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('informational', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                informational
                ''',
                'informational',
                'ietf-qos', False),
            _MetaInfoClassMember('time-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-burst
                ''',
                'time_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('time-excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-excess-burst
                ''',
                'time_excess_burst',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Metering.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Metering' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Metering',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('card-family-1', REFERENCE_CLASS, 'CardFamily1' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily1', 
                [], [], 
                '''                card-family-1
                ''',
                'card_family_1',
                'ietf-qos', False),
            _MetaInfoClassMember('card-family-2', REFERENCE_CLASS, 'CardFamily2' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily2', 
                [], [], 
                '''                card-family-2
                ''',
                'card_family_2',
                'ietf-qos', False),
            _MetaInfoClassMember('card-family-3', REFERENCE_CLASS, 'CardFamily3' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.CardFamily3', 
                [], [], 
                '''                card-family-3
                ''',
                'card_family_3',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('policy', REFERENCE_CLASS, 'Policy_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Policy_', 
                [], [], 
                '''                policy
                ''',
                'policy',
                'ietf-qos', False),
            _MetaInfoClassMember('radius-guided', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                radius-guided
                ''',
                'radius_guided',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', REFERENCE_CLASS, 'Rate' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering.Rate', 
                [], [], 
                '''                Specify rate limits inline
                ''',
                'rate',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-calculation-exclude-layer-2-overhead', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify that rate calculation excludes the size ofLayer 2 overhead for the layer 3 circuit on which a policy is applied
                ''',
                'rate_calculation_exclude_layer_2_overhead',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'metering',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'conform-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'exceed-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions',
            False, 
            [
            _MetaInfoClassMember('conform-handling', REFERENCE_CLASS, 'ConformHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling', 
                [], [], 
                '''                conform-handling
                ''',
                'conform_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('exceed-handling', REFERENCE_CLASS, 'ExceedHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling', 
                [], [], 
                '''                exceed-handling
                ''',
                'exceed_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'actions',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate',
            False, 
            [
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions', 
                [], [], 
                '''                actions
                ''',
                'actions',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', ATTRIBUTE, 'int' , None, None, 
                [('66', '100000000')], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                excess-burst
                ''',
                'excess_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('time-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-burst
                ''',
                'time_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('time-excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-excess-burst
                ''',
                'time_excess_burst',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'bit-rate',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage',
            False, 
            [
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                percentage
                ''',
                'percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'percentage',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', REFERENCE_CLASS, 'BitRate' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate', 
                [], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('parent-class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                parent-class
                ''',
                'parent_class',
                'ietf-qos', False),
            _MetaInfoClassMember('percentage', REFERENCE_CLASS, 'Percentage' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage', 
                [], [], 
                '''                percentage
                ''',
                'percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'packet-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 39)], [], 
                '''                name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('packet-handling', REFERENCE_CLASS, 'PacketHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling', 
                [], [], 
                '''                packet-handling
                ''',
                'packet_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_', 
                [], [], 
                '''                class
                ''',
                'class_',
                'ietf-qos', False, max_elements=8),
            ],
            'ietf-qos',
            'classes',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup',
            False, 
            [
            _MetaInfoClassMember('class-group-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                class-group-reference
                ''',
                'class_group_reference',
                'ietf-qos', False),
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes', 
                [], [], 
                '''                classes
                ''',
                'classes',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.IpAccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.IpAccessGroup',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                context-name
                ''',
                'context_name',
                'ietf-qos', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ip-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.Ipv6AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.Ipv6AccessGroup',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                context-name
                ''',
                'context_name',
                'ietf-qos', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ipv6-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.L2AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.L2AccessGroup',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'l2-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.Classes.Class_.PacketHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.Classes.Class_.PacketHandling',
            False, 
            [
            _MetaInfoClassMember('parent-class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                parent-class
                ''',
                'parent_class',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'packet-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('packet-handling', REFERENCE_CLASS, 'PacketHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.Classes.Class_.PacketHandling', 
                [], [], 
                '''                packet-handling
                ''',
                'packet_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.Classes' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.Classes.Class_', 
                [], [], 
                '''                class
                ''',
                'class_',
                'ietf-qos', False, max_elements=8),
            ],
            'ietf-qos',
            'classes',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup',
            False, 
            [
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.Classes', 
                [], [], 
                '''                classes
                ''',
                'classes',
                'ietf-qos', False),
            _MetaInfoClassMember('ip-access-group', REFERENCE_CLASS, 'IpAccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.IpAccessGroup', 
                [], [], 
                '''                Reference an IPv4 policy
                ''',
                'ip_access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('ipv6-access-group', REFERENCE_CLASS, 'Ipv6AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.Ipv6AccessGroup', 
                [], [], 
                '''                Reference an IPv6 policy
                ''',
                'ipv6_access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('l2-access-group', REFERENCE_CLASS, 'L2AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.L2AccessGroup', 
                [], [], 
                '''                Reference a layer-2 policy
                ''',
                'l2_access_group',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Policy_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Policy_',
            False, 
            [
            _MetaInfoClassMember('access-group', REFERENCE_CLASS, 'AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup', 
                [], [], 
                '''                access-group
                ''',
                'access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('class-group', REFERENCE_CLASS, 'ClassGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup', 
                [], [], 
                '''                Reference a previously defined class
                ''',
                'class_group',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'policy',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Rate.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Rate.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Rate.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Rate.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Rate.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Rate.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Rate.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions.ConformHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions.ConformHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions.ConformHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions.ConformHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'conform-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions.ExceedHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions.ExceedHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions.ExceedHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions.ExceedHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'exceed-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions.ViolateHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions.ViolateHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions.ViolateHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions.ViolateHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'violate-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions',
            False, 
            [
            _MetaInfoClassMember('conform-handling', REFERENCE_CLASS, 'ConformHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions.ConformHandling', 
                [], [], 
                '''                conform-handling
                ''',
                'conform_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('exceed-handling', REFERENCE_CLASS, 'ExceedHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions.ExceedHandling', 
                [], [], 
                '''                exceed-handling
                ''',
                'exceed_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('violate-handling', REFERENCE_CLASS, 'ViolateHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions.ViolateHandling', 
                [], [], 
                '''                violate-handling
                ''',
                'violate_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'actions',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.Rate' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1.Rate',
            False, 
            [
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions', 
                [], [], 
                '''                actions
                ''',
                'actions',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', ATTRIBUTE, 'int' , None, None, 
                [('66', '100000000')], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Rate.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                excess-burst
                ''',
                'excess_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Rate.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('informational', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                informational
                ''',
                'informational',
                'ietf-qos', False),
            _MetaInfoClassMember('time-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-burst
                ''',
                'time_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('time-excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-excess-burst
                ''',
                'time_excess_burst',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily1.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily1.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily1' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily1',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('policy', REFERENCE_CLASS, 'Policy_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Policy_', 
                [], [], 
                '''                policy
                ''',
                'policy',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', REFERENCE_CLASS, 'Rate' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1.Rate', 
                [], [], 
                '''                Specify rate limits inline
                ''',
                'rate',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-calculation-exclude-layer-2-overhead', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify that rate calculation excludes the size ofLayer 2 overhead for the layer 3 circuit on which a policy is applied
                ''',
                'rate_calculation_exclude_layer_2_overhead',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'card-family-1',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'conform-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'exceed-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions',
            False, 
            [
            _MetaInfoClassMember('conform-handling', REFERENCE_CLASS, 'ConformHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling', 
                [], [], 
                '''                conform-handling
                ''',
                'conform_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('exceed-handling', REFERENCE_CLASS, 'ExceedHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling', 
                [], [], 
                '''                exceed-handling
                ''',
                'exceed_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'actions',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate',
            False, 
            [
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions', 
                [], [], 
                '''                actions
                ''',
                'actions',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', ATTRIBUTE, 'int' , None, None, 
                [('5', '100000000')], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                excess-burst
                ''',
                'excess_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('time-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-burst
                ''',
                'time_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('time-excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-excess-burst
                ''',
                'time_excess_burst',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'bit-rate',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage',
            False, 
            [
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                percentage
                ''',
                'percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'percentage',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', REFERENCE_CLASS, 'BitRate' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate', 
                [], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('parent-class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                parent-class
                ''',
                'parent_class',
                'ietf-qos', False),
            _MetaInfoClassMember('percentage', REFERENCE_CLASS, 'Percentage' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage', 
                [], [], 
                '''                percentage
                ''',
                'percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'packet-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 39)], [], 
                '''                name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('packet-handling', REFERENCE_CLASS, 'PacketHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling', 
                [], [], 
                '''                packet-handling
                ''',
                'packet_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_', 
                [], [], 
                '''                class
                ''',
                'class_',
                'ietf-qos', False, max_elements=8),
            ],
            'ietf-qos',
            'classes',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup',
            False, 
            [
            _MetaInfoClassMember('class-group-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                class-group-reference
                ''',
                'class_group_reference',
                'ietf-qos', False),
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes', 
                [], [], 
                '''                classes
                ''',
                'classes',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.IpAccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.IpAccessGroup',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                context-name
                ''',
                'context_name',
                'ietf-qos', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ip-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.Ipv6AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.Ipv6AccessGroup',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                context-name
                ''',
                'context_name',
                'ietf-qos', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ipv6-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.L2AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.L2AccessGroup',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'l2-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.Classes.Class_.PacketHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.Classes.Class_.PacketHandling',
            False, 
            [
            _MetaInfoClassMember('parent-class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                parent-class
                ''',
                'parent_class',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'packet-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('packet-handling', REFERENCE_CLASS, 'PacketHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.Classes.Class_.PacketHandling', 
                [], [], 
                '''                packet-handling
                ''',
                'packet_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.Classes' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.Classes.Class_', 
                [], [], 
                '''                class
                ''',
                'class_',
                'ietf-qos', False, max_elements=8),
            ],
            'ietf-qos',
            'classes',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup',
            False, 
            [
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.Classes', 
                [], [], 
                '''                classes
                ''',
                'classes',
                'ietf-qos', False),
            _MetaInfoClassMember('ip-access-group', REFERENCE_CLASS, 'IpAccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.IpAccessGroup', 
                [], [], 
                '''                Reference an IPv4 policy
                ''',
                'ip_access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('ipv6-access-group', REFERENCE_CLASS, 'Ipv6AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.Ipv6AccessGroup', 
                [], [], 
                '''                Reference an IPv6 policy
                ''',
                'ipv6_access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('l2-access-group', REFERENCE_CLASS, 'L2AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.L2AccessGroup', 
                [], [], 
                '''                Reference a layer-2 policy
                ''',
                'l2_access_group',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Policy_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Policy_',
            False, 
            [
            _MetaInfoClassMember('access-group', REFERENCE_CLASS, 'AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup', 
                [], [], 
                '''                access-group
                ''',
                'access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('class-group', REFERENCE_CLASS, 'ClassGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup', 
                [], [], 
                '''                Reference a previously defined class
                ''',
                'class_group',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'policy',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Rate.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Rate.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Rate.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Rate.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Rate.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Rate.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Rate.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions.ConformHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions.ConformHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions.ConformHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions.ConformHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'conform-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions.ExceedHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions.ExceedHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions.ExceedHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions.ExceedHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'exceed-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions.ViolateHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions.ViolateHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions.ViolateHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions.ViolateHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'violate-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions',
            False, 
            [
            _MetaInfoClassMember('conform-handling', REFERENCE_CLASS, 'ConformHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions.ConformHandling', 
                [], [], 
                '''                conform-handling
                ''',
                'conform_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('exceed-handling', REFERENCE_CLASS, 'ExceedHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions.ExceedHandling', 
                [], [], 
                '''                exceed-handling
                ''',
                'exceed_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('violate-handling', REFERENCE_CLASS, 'ViolateHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions.ViolateHandling', 
                [], [], 
                '''                violate-handling
                ''',
                'violate_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'actions',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.Rate' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2.Rate',
            False, 
            [
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions', 
                [], [], 
                '''                actions
                ''',
                'actions',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', ATTRIBUTE, 'int' , None, None, 
                [('5', '100000000')], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Rate.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                excess-burst
                ''',
                'excess_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Rate.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('informational', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                informational
                ''',
                'informational',
                'ietf-qos', False),
            _MetaInfoClassMember('time-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-burst
                ''',
                'time_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('time-excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-excess-burst
                ''',
                'time_excess_burst',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily2.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily2.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily2' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily2',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('policy', REFERENCE_CLASS, 'Policy_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Policy_', 
                [], [], 
                '''                policy
                ''',
                'policy',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', REFERENCE_CLASS, 'Rate' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2.Rate', 
                [], [], 
                '''                Specify rate limits inline
                ''',
                'rate',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-calculation-exclude-layer-2-overhead', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify that rate calculation excludes the size ofLayer 2 overhead for the layer 3 circuit on which a policy is applied
                ''',
                'rate_calculation_exclude_layer_2_overhead',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'card-family-2',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'conform-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'exceed-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions',
            False, 
            [
            _MetaInfoClassMember('conform-handling', REFERENCE_CLASS, 'ConformHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling', 
                [], [], 
                '''                conform-handling
                ''',
                'conform_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('exceed-handling', REFERENCE_CLASS, 'ExceedHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling', 
                [], [], 
                '''                exceed-handling
                ''',
                'exceed_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'actions',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate',
            False, 
            [
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions', 
                [], [], 
                '''                actions
                ''',
                'actions',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', ATTRIBUTE, 'int' , None, None, 
                [('66', '100000000')], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                excess-burst
                ''',
                'excess_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('time-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-burst
                ''',
                'time_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('time-excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-excess-burst
                ''',
                'time_excess_burst',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'bit-rate',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage',
            False, 
            [
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                percentage
                ''',
                'percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'percentage',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', REFERENCE_CLASS, 'BitRate' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate', 
                [], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('parent-class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                parent-class
                ''',
                'parent_class',
                'ietf-qos', False),
            _MetaInfoClassMember('percentage', REFERENCE_CLASS, 'Percentage' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage', 
                [], [], 
                '''                percentage
                ''',
                'percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'packet-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 39)], [], 
                '''                name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('packet-handling', REFERENCE_CLASS, 'PacketHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling', 
                [], [], 
                '''                packet-handling
                ''',
                'packet_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_', 
                [], [], 
                '''                class
                ''',
                'class_',
                'ietf-qos', False, max_elements=8),
            ],
            'ietf-qos',
            'classes',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup',
            False, 
            [
            _MetaInfoClassMember('class-group-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                class-group-reference
                ''',
                'class_group_reference',
                'ietf-qos', False),
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes', 
                [], [], 
                '''                classes
                ''',
                'classes',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.IpAccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.IpAccessGroup',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                context-name
                ''',
                'context_name',
                'ietf-qos', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ip-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.Ipv6AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.Ipv6AccessGroup',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                context-name
                ''',
                'context_name',
                'ietf-qos', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ipv6-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.L2AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.L2AccessGroup',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'l2-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.Classes.Class_.PacketHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.Classes.Class_.PacketHandling',
            False, 
            [
            _MetaInfoClassMember('parent-class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                parent-class
                ''',
                'parent_class',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'packet-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('packet-handling', REFERENCE_CLASS, 'PacketHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.Classes.Class_.PacketHandling', 
                [], [], 
                '''                packet-handling
                ''',
                'packet_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.Classes' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.Classes.Class_', 
                [], [], 
                '''                class
                ''',
                'class_',
                'ietf-qos', False, max_elements=8),
            ],
            'ietf-qos',
            'classes',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup',
            False, 
            [
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.Classes', 
                [], [], 
                '''                classes
                ''',
                'classes',
                'ietf-qos', False),
            _MetaInfoClassMember('ip-access-group', REFERENCE_CLASS, 'IpAccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.IpAccessGroup', 
                [], [], 
                '''                Reference an IPv4 policy
                ''',
                'ip_access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('ipv6-access-group', REFERENCE_CLASS, 'Ipv6AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.Ipv6AccessGroup', 
                [], [], 
                '''                Reference an IPv6 policy
                ''',
                'ipv6_access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('l2-access-group', REFERENCE_CLASS, 'L2AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.L2AccessGroup', 
                [], [], 
                '''                Reference a layer-2 policy
                ''',
                'l2_access_group',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Policy_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Policy_',
            False, 
            [
            _MetaInfoClassMember('access-group', REFERENCE_CLASS, 'AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup', 
                [], [], 
                '''                access-group
                ''',
                'access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('class-group', REFERENCE_CLASS, 'ClassGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup', 
                [], [], 
                '''                Reference a previously defined class
                ''',
                'class_group',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'policy',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Rate.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Rate.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Rate.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Rate.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Rate.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Rate.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Rate.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions.ConformHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions.ConformHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions.ConformHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions.ConformHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'conform-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions.ExceedHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions.ExceedHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions.ExceedHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions.ExceedHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'exceed-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions.ViolateHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions.ViolateHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions.ViolateHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions.ViolateHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'violate-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions',
            False, 
            [
            _MetaInfoClassMember('conform-handling', REFERENCE_CLASS, 'ConformHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions.ConformHandling', 
                [], [], 
                '''                conform-handling
                ''',
                'conform_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('exceed-handling', REFERENCE_CLASS, 'ExceedHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions.ExceedHandling', 
                [], [], 
                '''                exceed-handling
                ''',
                'exceed_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('violate-handling', REFERENCE_CLASS, 'ViolateHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions.ViolateHandling', 
                [], [], 
                '''                violate-handling
                ''',
                'violate_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'actions',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.Rate' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3.Rate',
            False, 
            [
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions', 
                [], [], 
                '''                actions
                ''',
                'actions',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', ATTRIBUTE, 'int' , None, None, 
                [('66', '100000000')], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Rate.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                excess-burst
                ''',
                'excess_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Rate.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('informational', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                informational
                ''',
                'informational',
                'ietf-qos', False),
            _MetaInfoClassMember('time-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-burst
                ''',
                'time_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('time-excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-excess-burst
                ''',
                'time_excess_burst',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.CardFamily3.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily3.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.CardFamily3' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.CardFamily3',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('policy', REFERENCE_CLASS, 'Policy_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Policy_', 
                [], [], 
                '''                policy
                ''',
                'policy',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', REFERENCE_CLASS, 'Rate' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3.Rate', 
                [], [], 
                '''                Specify rate limits inline
                ''',
                'rate',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-calculation-exclude-layer-2-overhead', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify that rate calculation excludes the size ofLayer 2 overhead for the layer 3 circuit on which a policy is applied
                ''',
                'rate_calculation_exclude_layer_2_overhead',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'card-family-3',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'conform-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'exceed-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions',
            False, 
            [
            _MetaInfoClassMember('conform-handling', REFERENCE_CLASS, 'ConformHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling', 
                [], [], 
                '''                conform-handling
                ''',
                'conform_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('exceed-handling', REFERENCE_CLASS, 'ExceedHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling', 
                [], [], 
                '''                exceed-handling
                ''',
                'exceed_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'actions',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate',
            False, 
            [
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions', 
                [], [], 
                '''                actions
                ''',
                'actions',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', ATTRIBUTE, 'int' , None, None, 
                [('66', '100000000')], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                excess-burst
                ''',
                'excess_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('time-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-burst
                ''',
                'time_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('time-excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-excess-burst
                ''',
                'time_excess_burst',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'bit-rate',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage',
            False, 
            [
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                percentage
                ''',
                'percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'percentage',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', REFERENCE_CLASS, 'BitRate' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate', 
                [], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('parent-class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                parent-class
                ''',
                'parent_class',
                'ietf-qos', False),
            _MetaInfoClassMember('percentage', REFERENCE_CLASS, 'Percentage' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage', 
                [], [], 
                '''                percentage
                ''',
                'percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'packet-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 39)], [], 
                '''                name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('packet-handling', REFERENCE_CLASS, 'PacketHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling', 
                [], [], 
                '''                packet-handling
                ''',
                'packet_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_', 
                [], [], 
                '''                class
                ''',
                'class_',
                'ietf-qos', False, max_elements=8),
            ],
            'ietf-qos',
            'classes',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.ClassGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.ClassGroup',
            False, 
            [
            _MetaInfoClassMember('class-group-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                class-group-reference
                ''',
                'class_group_reference',
                'ietf-qos', False),
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes', 
                [], [], 
                '''                classes
                ''',
                'classes',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.AccessGroup.IpAccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.AccessGroup.IpAccessGroup',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                context-name
                ''',
                'context_name',
                'ietf-qos', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ip-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.AccessGroup.Ipv6AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.AccessGroup.Ipv6AccessGroup',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                context-name
                ''',
                'context_name',
                'ietf-qos', False),
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'ipv6-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.AccessGroup.L2AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.AccessGroup.L2AccessGroup',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                policy-name
                ''',
                'policy_name',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'l2-access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.AccessGroup.Classes.Class_.PacketHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.AccessGroup.Classes.Class_.PacketHandling',
            False, 
            [
            _MetaInfoClassMember('parent-class', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                parent-class
                ''',
                'parent_class',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'packet-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.AccessGroup.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.AccessGroup.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('packet-handling', REFERENCE_CLASS, 'PacketHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.AccessGroup.Classes.Class_.PacketHandling', 
                [], [], 
                '''                packet-handling
                ''',
                'packet_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'class',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.AccessGroup.Classes' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.AccessGroup.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.AccessGroup.Classes.Class_', 
                [], [], 
                '''                class
                ''',
                'class_',
                'ietf-qos', False, max_elements=8),
            ],
            'ietf-qos',
            'classes',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_.AccessGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_.AccessGroup',
            False, 
            [
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.AccessGroup.Classes', 
                [], [], 
                '''                classes
                ''',
                'classes',
                'ietf-qos', False),
            _MetaInfoClassMember('ip-access-group', REFERENCE_CLASS, 'IpAccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.AccessGroup.IpAccessGroup', 
                [], [], 
                '''                Reference an IPv4 policy
                ''',
                'ip_access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('ipv6-access-group', REFERENCE_CLASS, 'Ipv6AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.AccessGroup.Ipv6AccessGroup', 
                [], [], 
                '''                Reference an IPv6 policy
                ''',
                'ipv6_access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('l2-access-group', REFERENCE_CLASS, 'L2AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.AccessGroup.L2AccessGroup', 
                [], [], 
                '''                Reference a layer-2 policy
                ''',
                'l2_access_group',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'access-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Policy_' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Policy_',
            False, 
            [
            _MetaInfoClassMember('access-group', REFERENCE_CLASS, 'AccessGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.AccessGroup', 
                [], [], 
                '''                access-group
                ''',
                'access_group',
                'ietf-qos', False),
            _MetaInfoClassMember('class-group', REFERENCE_CLASS, 'ClassGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_.ClassGroup', 
                [], [], 
                '''                Reference a previously defined class
                ''',
                'class_group',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'policy',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Rate.Counters.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Rate.Counters.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Rate.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Rate.Counters',
            False, 
            [
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Counters.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Rate.HierarchicalCounters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Rate.HierarchicalCounters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                dual-stack
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'hierarchical-counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Rate.Actions.ConformHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.Rate.Actions.ConformHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.Rate.Actions.ConformHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Rate.Actions.ConformHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'conform-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Rate.Actions.ExceedHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.Rate.Actions.ExceedHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.Rate.Actions.ExceedHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Rate.Actions.ExceedHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'exceed-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                drop-packet
                ''',
                'drop_packet',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('no-action', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                no-action
                ''',
                'no_action',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'violate-handling',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Rate.Actions' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Rate.Actions',
            False, 
            [
            _MetaInfoClassMember('conform-handling', REFERENCE_CLASS, 'ConformHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ConformHandling', 
                [], [], 
                '''                conform-handling
                ''',
                'conform_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('exceed-handling', REFERENCE_CLASS, 'ExceedHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ExceedHandling', 
                [], [], 
                '''                exceed-handling
                ''',
                'exceed_handling',
                'ietf-qos', False),
            _MetaInfoClassMember('violate-handling', REFERENCE_CLASS, 'ViolateHandling' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling', 
                [], [], 
                '''                violate-handling
                ''',
                'violate_handling',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'actions',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.Rate' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing.Rate',
            False, 
            [
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions', 
                [], [], 
                '''                actions
                ''',
                'actions',
                'ietf-qos', False),
            _MetaInfoClassMember('bit-rate', ATTRIBUTE, 'int' , None, None, 
                [('66', '100000000')], [], 
                '''                bit-rate
                ''',
                'bit_rate',
                'ietf-qos', False),
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '4250000000')], [], 
                '''                excess-burst
                ''',
                'excess_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('hierarchical-counters', REFERENCE_CLASS, 'HierarchicalCounters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.HierarchicalCounters', 
                [], [], 
                '''                hierarchical-counters
                ''',
                'hierarchical_counters',
                'ietf-qos', False),
            _MetaInfoClassMember('informational', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                informational
                ''',
                'informational',
                'ietf-qos', False),
            _MetaInfoClassMember('time-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-burst
                ''',
                'time_burst',
                'ietf-qos', False),
            _MetaInfoClassMember('time-excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '10000')], [], 
                '''                time-excess-burst
                ''',
                'time_excess_burst',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Policing.DropPrecedenceEnum' : _MetaInfoEnum('DropPrecedenceEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing.MarkPriorityEnum' : _MetaInfoEnum('MarkPriorityEnum', 'ydk.models.ietf.ietf_qos',
        {
            'ignore':'ignore',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Policing' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Policing',
            False, 
            [
            _MetaInfoClassMember('af-drop', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                af-drop
                ''',
                'af_drop',
                'ietf-qos', False),
            _MetaInfoClassMember('card-family-1', REFERENCE_CLASS, 'CardFamily1' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily1', 
                [], [], 
                '''                card-family-1
                ''',
                'card_family_1',
                'ietf-qos', False),
            _MetaInfoClassMember('card-family-2', REFERENCE_CLASS, 'CardFamily2' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily2', 
                [], [], 
                '''                card-family-2
                ''',
                'card_family_2',
                'ietf-qos', False),
            _MetaInfoClassMember('card-family-3', REFERENCE_CLASS, 'CardFamily3' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.CardFamily3', 
                [], [], 
                '''                card-family-3
                ''',
                'card_family_3',
                'ietf-qos', False),
            _MetaInfoClassMember('drop-precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                drop-precedence
                ''',
                'drop_precedence',
                'ietf-qos', False, [
                    _MetaInfoClassMember('drop-precedence', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                    _MetaInfoClassMember('drop-precedence', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling.DropPrecedenceEnum', 
                        [], [], 
                        '''                        drop-precedence
                        ''',
                        'drop_precedence',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-dscp
                ''',
                'mark_dscp',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-dscp', REFERENCE_ENUM_CLASS, 'DscpCodeAllValuesTypeEnum' , 'ydk.models.ietf.ietf_qos', 'DscpCodeAllValuesTypeEnum', 
                        [], [], 
                        '''                        mark-dscp
                        ''',
                        'mark_dscp',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('mark-precedence', ATTRIBUTE, 'int' , None, None, 
                [('1', '3')], [], 
                '''                mark-precedence
                ''',
                'mark_precedence',
                'ietf-qos', False),
            _MetaInfoClassMember('mark-priority', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                mark-priority
                ''',
                'mark_priority',
                'ietf-qos', False, [
                    _MetaInfoClassMember('mark-priority', ATTRIBUTE, 'int' , None, None, 
                        [('1', '7')], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                    _MetaInfoClassMember('mark-priority', REFERENCE_ENUM_CLASS, 'Qos.Policies.Policy.Policing.MarkPriorityEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.MarkPriorityEnum', 
                        [], [], 
                        '''                        mark-priority
                        ''',
                        'mark_priority',
                        'ietf-qos', False),
                ]),
            _MetaInfoClassMember('policy', REFERENCE_CLASS, 'Policy_' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Policy_', 
                [], [], 
                '''                policy
                ''',
                'policy',
                'ietf-qos', False),
            _MetaInfoClassMember('radius-guided', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                radius-guided
                ''',
                'radius_guided',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', REFERENCE_CLASS, 'Rate' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing.Rate', 
                [], [], 
                '''                Specify rate limits inline
                ''',
                'rate',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-calculation-exclude-layer-2-overhead', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify that rate calculation excludes the size ofLayer 2 overhead for the layer 3 circuit on which a policy is applied
                ''',
                'rate_calculation_exclude_layer_2_overhead',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'policing',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Mdrr.Queue' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Mdrr.Queue',
            False, 
            [
            _MetaInfoClassMember('num', ATTRIBUTE, 'int' , None, None, 
                [('0', '8')], [], 
                '''                num
                ''',
                'num',
                'ietf-qos', True),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int' , None, None, 
                [('5', '100')], [], 
                '''                weight
                ''',
                'weight',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'queue',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Mdrr.QosModeEnum' : _MetaInfoEnum('QosModeEnum', 'ydk.models.ietf.ietf_qos',
        {
            'priority':'priority',
            'strict':'strict',
            'wrr':'wrr',
        }, 'ietf-qos', _yang_ns._namespaces['ietf-qos']),
    'Qos.Policies.Policy.Mdrr' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Mdrr',
            False, 
            [
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '8000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('congestion-avoidance-map-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                congestion-avoidance-map-reference
                ''',
                'congestion_avoidance_map_reference',
                'ietf-qos', False),
            _MetaInfoClassMember('num-queues', ATTRIBUTE, 'int' , None, None, 
                [('1', 'None'), ('2', 'None'), ('4', 'None'), ('8', 'None')], [], 
                '''                num-queues
                ''',
                'num_queues',
                'ietf-qos', False),
            _MetaInfoClassMember('qos-mode', REFERENCE_ENUM_CLASS, 'QosModeEnum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Mdrr.QosModeEnum', 
                [], [], 
                '''                qos-mode
                ''',
                'qos_mode',
                'ietf-qos', False),
            _MetaInfoClassMember('queue', REFERENCE_LIST, 'Queue' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Mdrr.Queue', 
                [], [], 
                '''                queue
                ''',
                'queue',
                'ietf-qos', False),
            _MetaInfoClassMember('queue-map-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                queue-map-reference
                ''',
                'queue_map_reference',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('56', '10000000')], [], 
                '''                rate
                ''',
                'rate',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'mdrr',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily1.Queue' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily1.Queue',
            False, 
            [
            _MetaInfoClassMember('num', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                priority
                ''',
                'num',
                'ietf-qos', True),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                priority
                ''',
                'priority',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-maximum', ATTRIBUTE, 'int' , None, None, 
                [('4', '10000000')], [], 
                '''                rate-maximum
                ''',
                'rate_maximum',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-maximum-percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                rate-maximum-percentage
                ''',
                'rate_maximum_percentage',
                'ietf-qos', False),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '1023')], [], 
                '''                weight
                ''',
                'weight',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'queue',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily1.QueuePriorityGroup.RateAbsolute' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily1.QueuePriorityGroup.RateAbsolute',
            False, 
            [
            _MetaInfoClassMember('exceed', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                empty
                ''',
                'exceed',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('8', '100000000')], [], 
                '''                rate
                ''',
                'rate',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate-absolute',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily1.QueuePriorityGroup.RatePercentage' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily1.QueuePriorityGroup.RatePercentage',
            False, 
            [
            _MetaInfoClassMember('rate-percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                rate-percentage
                ''',
                'rate_percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate-percentage',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily1.QueuePriorityGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily1.QueuePriorityGroup',
            False, 
            [
            _MetaInfoClassMember('priority-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                priority-group
                ''',
                'priority_group',
                'ietf-qos', True),
            _MetaInfoClassMember('rate-absolute', REFERENCE_CLASS, 'RateAbsolute' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily1.QueuePriorityGroup.RateAbsolute', 
                [], [], 
                '''                rate-absolute
                ''',
                'rate_absolute',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-percentage', REFERENCE_CLASS, 'RatePercentage' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily1.QueuePriorityGroup.RatePercentage', 
                [], [], 
                '''                rate-percentage
                ''',
                'rate_percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'queue-priority-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily1.RateMinimum' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily1.RateMinimum',
            False, 
            [
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('64', '1875000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('8', '1000000')], [], 
                '''                rate-minimum
                ''',
                'rate',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate-minimum',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily1.RateMaximum' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily1.RateMaximum',
            False, 
            [
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('64', '1875000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('8', '10000000')], [], 
                '''                rate-maximum
                ''',
                'rate',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate-maximum',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily1' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily1',
            False, 
            [
            _MetaInfoClassMember('congestion-avoidance-map-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                congestion-avoidance-map-reference
                ''',
                'congestion_avoidance_map_reference',
                'ietf-qos', False),
            _MetaInfoClassMember('num-queues', ATTRIBUTE, 'int' , None, None, 
                [('1', 'None'), ('2', 'None'), ('4', 'None'), ('8', 'None')], [], 
                '''                num-queues
                ''',
                'num_queues',
                'ietf-qos', False),
            _MetaInfoClassMember('queue', REFERENCE_LIST, 'Queue' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily1.Queue', 
                [], [], 
                '''                queue
                ''',
                'queue',
                'ietf-qos', False),
            _MetaInfoClassMember('queue-map-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                queue-map-reference
                ''',
                'queue_map_reference',
                'ietf-qos', False),
            _MetaInfoClassMember('queue-priority-group', REFERENCE_LIST, 'QueuePriorityGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily1.QueuePriorityGroup', 
                [], [], 
                '''                queue-priority-group
                ''',
                'queue_priority_group',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-maximum', REFERENCE_CLASS, 'RateMaximum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily1.RateMaximum', 
                [], [], 
                '''                rate-maximum
                ''',
                'rate_maximum',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-minimum', REFERENCE_CLASS, 'RateMinimum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily1.RateMinimum', 
                [], [], 
                '''                rate-minimum
                ''',
                'rate_minimum',
                'ietf-qos', False),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '1023')], [], 
                '''                weight
                ''',
                'weight',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'card-family-1',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily2.Queue' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily2.Queue',
            False, 
            [
            _MetaInfoClassMember('num', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                priority
                ''',
                'num',
                'ietf-qos', True),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                priority
                ''',
                'priority',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-maximum', ATTRIBUTE, 'int' , None, None, 
                [('4', '10000000')], [], 
                '''                rate-maximum
                ''',
                'rate_maximum',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-maximum-percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                rate-maximum-percentage
                ''',
                'rate_maximum_percentage',
                'ietf-qos', False),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '1023')], [], 
                '''                weight
                ''',
                'weight',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'queue',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily2.QueuePriorityGroup.RateAbsolute' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily2.QueuePriorityGroup.RateAbsolute',
            False, 
            [
            _MetaInfoClassMember('exceed', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                exceed
                ''',
                'exceed',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('8', '10000000')], [], 
                '''                rate
                ''',
                'rate',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate-absolute',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily2.QueuePriorityGroup.RatePercentage' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily2.QueuePriorityGroup.RatePercentage',
            False, 
            [
            _MetaInfoClassMember('exceed', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                exceed
                ''',
                'exceed',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                rate-percentage
                ''',
                'rate_percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate-percentage',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily2.QueuePriorityGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily2.QueuePriorityGroup',
            False, 
            [
            _MetaInfoClassMember('priority-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                priority-group
                ''',
                'priority_group',
                'ietf-qos', True),
            _MetaInfoClassMember('rate-absolute', REFERENCE_CLASS, 'RateAbsolute' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily2.QueuePriorityGroup.RateAbsolute', 
                [], [], 
                '''                rate-absolute
                ''',
                'rate_absolute',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-percentage', REFERENCE_CLASS, 'RatePercentage' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily2.QueuePriorityGroup.RatePercentage', 
                [], [], 
                '''                rate-percentage
                ''',
                'rate_percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'queue-priority-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily2.RateMinimum' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily2.RateMinimum',
            False, 
            [
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('8', '1000000')], [], 
                '''                rate-minimum
                ''',
                'rate',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate-minimum',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily2.RateMaximum' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily2.RateMaximum',
            False, 
            [
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('64', '1000000')], [], 
                '''                rate-maximum
                ''',
                'rate',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate-maximum',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily2' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily2',
            False, 
            [
            _MetaInfoClassMember('congestion-avoidance-map-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                congestion-avoidance-map-reference
                ''',
                'congestion_avoidance_map_reference',
                'ietf-qos', False),
            _MetaInfoClassMember('num-queues', ATTRIBUTE, 'int' , None, None, 
                [('1', 'None'), ('2', 'None'), ('4', 'None'), ('8', 'None')], [], 
                '''                num-queues
                ''',
                'num_queues',
                'ietf-qos', False),
            _MetaInfoClassMember('queue', REFERENCE_LIST, 'Queue' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily2.Queue', 
                [], [], 
                '''                queue
                ''',
                'queue',
                'ietf-qos', False),
            _MetaInfoClassMember('queue-map-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                queue-map-reference
                ''',
                'queue_map_reference',
                'ietf-qos', False),
            _MetaInfoClassMember('queue-priority-group', REFERENCE_LIST, 'QueuePriorityGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily2.QueuePriorityGroup', 
                [], [], 
                '''                queue-priority-group
                ''',
                'queue_priority_group',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-maximum', REFERENCE_CLASS, 'RateMaximum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily2.RateMaximum', 
                [], [], 
                '''                rate-maximum
                ''',
                'rate_maximum',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-minimum', REFERENCE_CLASS, 'RateMinimum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily2.RateMinimum', 
                [], [], 
                '''                rate-minimum
                ''',
                'rate_minimum',
                'ietf-qos', False),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '4096')], [], 
                '''                weight
                ''',
                'weight',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'card-family-2',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily3.Queue' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily3.Queue',
            False, 
            [
            _MetaInfoClassMember('num', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                priority
                ''',
                'num',
                'ietf-qos', True),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                priority
                ''',
                'priority',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-maximum', ATTRIBUTE, 'int' , None, None, 
                [('4', '10000000')], [], 
                '''                rate-maximum
                ''',
                'rate_maximum',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-maximum-percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                rate-maximum-percentage
                ''',
                'rate_maximum_percentage',
                'ietf-qos', False),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '1023')], [], 
                '''                weight
                ''',
                'weight',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'queue',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup.RateAbsolute' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup.RateAbsolute',
            False, 
            [
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('8', '100000000')], [], 
                '''                rate
                ''',
                'rate',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate-absolute',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup.RateMinimum' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup.RateMinimum',
            False, 
            [
            _MetaInfoClassMember('rate-minimum', ATTRIBUTE, 'int' , None, None, 
                [('8', '100000000')], [], 
                '''                rate-minimum
                ''',
                'rate_minimum',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate-minimum',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup.RatePercentage' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup.RatePercentage',
            False, 
            [
            _MetaInfoClassMember('rate-percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                rate-percentage
                ''',
                'rate_percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate-percentage',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup.RateMinimumPercentage' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup.RateMinimumPercentage',
            False, 
            [
            _MetaInfoClassMember('rate-minimum-percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                rate-minimum-percentage
                ''',
                'rate_minimum_percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate-minimum-percentage',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup',
            False, 
            [
            _MetaInfoClassMember('priority-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                priority-group
                ''',
                'priority_group',
                'ietf-qos', True),
            _MetaInfoClassMember('rate-absolute', REFERENCE_CLASS, 'RateAbsolute' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup.RateAbsolute', 
                [], [], 
                '''                rate-absolute
                ''',
                'rate_absolute',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-minimum', REFERENCE_CLASS, 'RateMinimum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup.RateMinimum', 
                [], [], 
                '''                rate-minimum
                ''',
                'rate_minimum',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-minimum-percentage', REFERENCE_CLASS, 'RateMinimumPercentage' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup.RateMinimumPercentage', 
                [], [], 
                '''                rate-minimum-percentage
                ''',
                'rate_minimum_percentage',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-percentage', REFERENCE_CLASS, 'RatePercentage' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup.RatePercentage', 
                [], [], 
                '''                rate-percentage
                ''',
                'rate_percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'queue-priority-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily3.RateMinimum' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily3.RateMinimum',
            False, 
            [
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('64', '1875000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('8', '1000000')], [], 
                '''                rate-minimum
                ''',
                'rate',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate-minimum',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily3.RateMaximum.Counters' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily3.RateMaximum.Counters',
            False, 
            [
            _MetaInfoClassMember('dual-stack', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable dual-stack costing
                ''',
                'dual_stack',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'counters',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily3.RateMaximum' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily3.RateMaximum',
            False, 
            [
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily3.RateMaximum.Counters', 
                [], [], 
                '''                counters
                ''',
                'counters',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('8', '10000000')], [], 
                '''                rate-maximum
                ''',
                'rate',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate-maximum',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.CardFamily3' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.CardFamily3',
            False, 
            [
            _MetaInfoClassMember('congestion-avoidance-map-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                congestion-avoidance-map-reference
                ''',
                'congestion_avoidance_map_reference',
                'ietf-qos', False),
            _MetaInfoClassMember('num-queues', ATTRIBUTE, 'int' , None, None, 
                [('1', 'None'), ('2', 'None'), ('4', 'None'), ('8', 'None')], [], 
                '''                num-queues
                ''',
                'num_queues',
                'ietf-qos', False),
            _MetaInfoClassMember('queue', REFERENCE_LIST, 'Queue' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily3.Queue', 
                [], [], 
                '''                queue
                ''',
                'queue',
                'ietf-qos', False),
            _MetaInfoClassMember('queue-map-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                queue-map-reference
                ''',
                'queue_map_reference',
                'ietf-qos', False),
            _MetaInfoClassMember('queue-priority-group', REFERENCE_LIST, 'QueuePriorityGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup', 
                [], [], 
                '''                queue-priority-group
                ''',
                'queue_priority_group',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-maximum', REFERENCE_CLASS, 'RateMaximum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily3.RateMaximum', 
                [], [], 
                '''                rate-maximum
                ''',
                'rate_maximum',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-minimum', REFERENCE_CLASS, 'RateMinimum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily3.RateMinimum', 
                [], [], 
                '''                rate-minimum
                ''',
                'rate_minimum',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'card-family-3',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.Queue' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.Queue',
            False, 
            [
            _MetaInfoClassMember('num', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                priority
                ''',
                'num',
                'ietf-qos', True),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                priority
                ''',
                'priority',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-maximum', ATTRIBUTE, 'int' , None, None, 
                [('4', '10000000')], [], 
                '''                rate-maximum
                ''',
                'rate_maximum',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-maximum-percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                rate-maximum-percentage
                ''',
                'rate_maximum_percentage',
                'ietf-qos', False),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '1023')], [], 
                '''                weight
                ''',
                'weight',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'queue',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.QueuePriorityGroup.RateAbsolute' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.QueuePriorityGroup.RateAbsolute',
            False, 
            [
            _MetaInfoClassMember('exceed', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                exceed
                ''',
                'exceed',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('8', '100000000')], [], 
                '''                rate
                ''',
                'rate',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate-absolute',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.QueuePriorityGroup.RatePercentage' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.QueuePriorityGroup.RatePercentage',
            False, 
            [
            _MetaInfoClassMember('exceed', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                exceed
                ''',
                'exceed',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                rate-percentage
                ''',
                'rate_percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate-percentage',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.QueuePriorityGroup' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.QueuePriorityGroup',
            False, 
            [
            _MetaInfoClassMember('priority-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                priority-group
                ''',
                'priority_group',
                'ietf-qos', True),
            _MetaInfoClassMember('rate-absolute', REFERENCE_CLASS, 'RateAbsolute' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.QueuePriorityGroup.RateAbsolute', 
                [], [], 
                '''                rate-absolute
                ''',
                'rate_absolute',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-percentage', REFERENCE_CLASS, 'RatePercentage' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.QueuePriorityGroup.RatePercentage', 
                [], [], 
                '''                rate-percentage
                ''',
                'rate_percentage',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'queue-priority-group',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.RateMinimum' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.RateMinimum',
            False, 
            [
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('64', '1875000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('8', '1000000')], [], 
                '''                rate-minimum
                ''',
                'rate',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate-minimum',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq.RateMaximum' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq.RateMaximum',
            False, 
            [
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('64', '1875000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('8', '10000000')], [], 
                '''                rate-maximum
                ''',
                'rate',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'rate-maximum',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.Pwfq' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.Pwfq',
            False, 
            [
            _MetaInfoClassMember('card-family-1', REFERENCE_CLASS, 'CardFamily1' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily1', 
                [], [], 
                '''                card-family-1
                ''',
                'card_family_1',
                'ietf-qos', False),
            _MetaInfoClassMember('card-family-2', REFERENCE_CLASS, 'CardFamily2' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily2', 
                [], [], 
                '''                card-family-2
                ''',
                'card_family_2',
                'ietf-qos', False),
            _MetaInfoClassMember('card-family-3', REFERENCE_CLASS, 'CardFamily3' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.CardFamily3', 
                [], [], 
                '''                card-family-3
                ''',
                'card_family_3',
                'ietf-qos', False),
            _MetaInfoClassMember('congestion-avoidance-map-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                congestion-avoidance-map-reference
                ''',
                'congestion_avoidance_map_reference',
                'ietf-qos', False),
            _MetaInfoClassMember('num-queues', ATTRIBUTE, 'int' , None, None, 
                [('1', 'None'), ('2', 'None'), ('4', 'None'), ('8', 'None')], [], 
                '''                num-queues
                ''',
                'num_queues',
                'ietf-qos', False),
            _MetaInfoClassMember('queue', REFERENCE_LIST, 'Queue' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.Queue', 
                [], [], 
                '''                queue
                ''',
                'queue',
                'ietf-qos', False),
            _MetaInfoClassMember('queue-map-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                queue-map-reference
                ''',
                'queue_map_reference',
                'ietf-qos', False),
            _MetaInfoClassMember('queue-priority-group', REFERENCE_LIST, 'QueuePriorityGroup' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.QueuePriorityGroup', 
                [], [], 
                '''                queue-priority-group
                ''',
                'queue_priority_group',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-maximum', REFERENCE_CLASS, 'RateMaximum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.RateMaximum', 
                [], [], 
                '''                rate-maximum
                ''',
                'rate_maximum',
                'ietf-qos', False),
            _MetaInfoClassMember('rate-minimum', REFERENCE_CLASS, 'RateMinimum' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq.RateMinimum', 
                [], [], 
                '''                rate-minimum
                ''',
                'rate_minimum',
                'ietf-qos', False),
            _MetaInfoClassMember('weight', ATTRIBUTE, 'int' , None, None, 
                [('1', '1023')], [], 
                '''                weight
                ''',
                'weight',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'pwfq',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.ProtocolRateLimit.Arp' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.ProtocolRateLimit.Arp',
            False, 
            [
            _MetaInfoClassMember('burst', ATTRIBUTE, 'int' , None, None, 
                [('1', '25000000')], [], 
                '''                burst
                ''',
                'burst',
                'ietf-qos', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('1', '2500000')], [], 
                '''                rate
                ''',
                'rate',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'arp',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy.ProtocolRateLimit' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy.ProtocolRateLimit',
            False, 
            [
            _MetaInfoClassMember('arp', REFERENCE_CLASS, 'Arp' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.ProtocolRateLimit.Arp', 
                [], [], 
                '''                arp
                ''',
                'arp',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'protocol-rate-limit',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies.Policy' : {
        'meta_info' : _MetaInfoClass('Qos.Policies.Policy',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                name
                ''',
                'name',
                'ietf-qos', True),
            _MetaInfoClassMember('mdrr', REFERENCE_CLASS, 'Mdrr' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Mdrr', 
                [], [], 
                '''                mdrr policy
                ''',
                'mdrr',
                'ietf-qos', False),
            _MetaInfoClassMember('metering', REFERENCE_CLASS, 'Metering' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Metering', 
                [], [], 
                '''                metering policy
                ''',
                'metering',
                'ietf-qos', False),
            _MetaInfoClassMember('policing', REFERENCE_CLASS, 'Policing' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Policing', 
                [], [], 
                '''                policing policy
                ''',
                'policing',
                'ietf-qos', False),
            _MetaInfoClassMember('protocol-rate-limit', REFERENCE_CLASS, 'ProtocolRateLimit' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.ProtocolRateLimit', 
                [], [], 
                '''                protocol-rate-limit policy
                ''',
                'protocol_rate_limit',
                'ietf-qos', False),
            _MetaInfoClassMember('pwfq', REFERENCE_CLASS, 'Pwfq' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy.Pwfq', 
                [], [], 
                '''                pwfq policy
                ''',
                'pwfq',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'policy',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos.Policies' : {
        'meta_info' : _MetaInfoClass('Qos.Policies',
            False, 
            [
            _MetaInfoClassMember('policy', REFERENCE_LIST, 'Policy' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies.Policy', 
                [], [], 
                '''                policy
                ''',
                'policy',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'policies',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
    'Qos' : {
        'meta_info' : _MetaInfoClass('Qos',
            False, 
            [
            _MetaInfoClassMember('class-definitions', REFERENCE_CLASS, 'ClassDefinitions' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassDefinitions', 
                [], [], 
                '''                class-definition
                ''',
                'class_definitions',
                'ietf-qos', False),
            _MetaInfoClassMember('class-maps', REFERENCE_CLASS, 'ClassMaps' , 'ydk.models.ietf.ietf_qos', 'Qos.ClassMaps', 
                [], [], 
                '''                class-maps
                ''',
                'class_maps',
                'ietf-qos', False),
            _MetaInfoClassMember('congestion-avoidance-maps', REFERENCE_CLASS, 'CongestionAvoidanceMaps' , 'ydk.models.ietf.ietf_qos', 'Qos.CongestionAvoidanceMaps', 
                [], [], 
                '''                congestion-avoidance-maps
                ''',
                'congestion_avoidance_maps',
                'ietf-qos', False),
            _MetaInfoClassMember('policies', REFERENCE_CLASS, 'Policies' , 'ydk.models.ietf.ietf_qos', 'Qos.Policies', 
                [], [], 
                '''                policies
                ''',
                'policies',
                'ietf-qos', False),
            _MetaInfoClassMember('profiles', REFERENCE_CLASS, 'Profiles' , 'ydk.models.ietf.ietf_qos', 'Qos.Profiles', 
                [], [], 
                '''                profile
                ''',
                'profiles',
                'ietf-qos', False),
            _MetaInfoClassMember('queue-maps', REFERENCE_CLASS, 'QueueMaps' , 'ydk.models.ietf.ietf_qos', 'Qos.QueueMaps', 
                [], [], 
                '''                queue-maps
                ''',
                'queue_maps',
                'ietf-qos', False),
            ],
            'ietf-qos',
            'qos',
            _yang_ns._namespaces['ietf-qos'],
        'ydk.models.ietf.ietf_qos'
        ),
    },
}
_meta_table['Qos.ClassDefinitions.ClassDefinition.Qos_']['meta_info'].parent =_meta_table['Qos.ClassDefinitions.ClassDefinition']['meta_info']
_meta_table['Qos.ClassDefinitions.ClassDefinition']['meta_info'].parent =_meta_table['Qos.ClassDefinitions']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Atm.In_.Atm_']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap.Atm.In_']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Atm.Out.Qos_']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap.Atm.Out']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Atm.In_']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap.Atm']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Atm.Out']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap.Atm']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Ethernet.In_.Ethernet_']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap.Ethernet.In_']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Ethernet.Out.Qos_']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap.Ethernet.Out']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Ethernet.In_']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap.Ethernet']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Ethernet.Out']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap.Ethernet']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Ip.In_.Ip_']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap.Ip.In_']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Ip.Out.Qos_']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap.Ip.Out']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Ip.In_']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap.Ip']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Ip.Out']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap.Ip']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Mpls.In_.Mpls_']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap.Mpls.In_']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Mpls.Out.Qos_']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap.Mpls.Out']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Mpls.In_']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap.Mpls']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Mpls.Out']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap.Mpls']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Atm']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Ethernet']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Ip']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap.Mpls']['meta_info'].parent =_meta_table['Qos.ClassMaps.ClassMap']['meta_info']
_meta_table['Qos.ClassMaps.ClassMap']['meta_info'].parent =_meta_table['Qos.ClassMaps']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue.Default']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue.Profile1']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue.Profile2']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr.Queue']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue.Default']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue.Profile1']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue.Profile2']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1.Queue']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue.Default']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue.Profile1']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue.Profile2']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2.Queue']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Default']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile1']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue.Profile2']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3.Queue']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily1']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily2']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq.CardFamily3']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Mdrr']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap.Pwfq']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps.CongestionAvoidanceMap']['meta_info'].parent =_meta_table['Qos.CongestionAvoidanceMaps']['meta_info']
_meta_table['Qos.Profiles.Profile.Overhead.CardFamily.CardFamily1.EncapsAccessLine']['meta_info'].parent =_meta_table['Qos.Profiles.Profile.Overhead.CardFamily.CardFamily1']['meta_info']
_meta_table['Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2.EncapsAccessLine.Value.DataLink']['meta_info'].parent =_meta_table['Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2.EncapsAccessLine.Value']['meta_info']
_meta_table['Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2.EncapsAccessLine.Value']['meta_info'].parent =_meta_table['Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2.EncapsAccessLine']['meta_info']
_meta_table['Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2.EncapsAccessLine']['meta_info'].parent =_meta_table['Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2']['meta_info']
_meta_table['Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3.EncapsAccessLine.Value.DataLink']['meta_info'].parent =_meta_table['Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3.EncapsAccessLine.Value']['meta_info']
_meta_table['Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3.EncapsAccessLine.Value']['meta_info'].parent =_meta_table['Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3.EncapsAccessLine']['meta_info']
_meta_table['Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3.EncapsAccessLine']['meta_info'].parent =_meta_table['Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3']['meta_info']
_meta_table['Qos.Profiles.Profile.Overhead.CardFamily.CardFamily1']['meta_info'].parent =_meta_table['Qos.Profiles.Profile.Overhead.CardFamily']['meta_info']
_meta_table['Qos.Profiles.Profile.Overhead.CardFamily.CardFamily2']['meta_info'].parent =_meta_table['Qos.Profiles.Profile.Overhead.CardFamily']['meta_info']
_meta_table['Qos.Profiles.Profile.Overhead.CardFamily.CardFamily3']['meta_info'].parent =_meta_table['Qos.Profiles.Profile.Overhead.CardFamily']['meta_info']
_meta_table['Qos.Profiles.Profile.Overhead.CardFamily']['meta_info'].parent =_meta_table['Qos.Profiles.Profile.Overhead']['meta_info']
_meta_table['Qos.Profiles.Profile.Overhead']['meta_info'].parent =_meta_table['Qos.Profiles.Profile']['meta_info']
_meta_table['Qos.Profiles.Profile.SlotPort']['meta_info'].parent =_meta_table['Qos.Profiles.Profile']['meta_info']
_meta_table['Qos.Profiles.Profile']['meta_info'].parent =_meta_table['Qos.Profiles']['meta_info']
_meta_table['Qos.QueueMaps.QueueMap.NumQueues.Queue']['meta_info'].parent =_meta_table['Qos.QueueMaps.QueueMap.NumQueues']['meta_info']
_meta_table['Qos.QueueMaps.QueueMap.NumQueues']['meta_info'].parent =_meta_table['Qos.QueueMaps.QueueMap']['meta_info']
_meta_table['Qos.QueueMaps.QueueMap']['meta_info'].parent =_meta_table['Qos.QueueMaps']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes.Class_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup.Classes']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.Classes.Class_.PacketHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.Classes.Class_']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.Classes.Class_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.Classes']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.IpAccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.Ipv6AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.L2AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup.Classes']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.ClassGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_.AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Rate.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Rate.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions.ConformHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions.ExceedHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions.ViolateHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Rate.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Rate.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Rate.Actions']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Policy_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1.Rate']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily1']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes.Class_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup.Classes']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.Classes.Class_.PacketHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.Classes.Class_']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.Classes.Class_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.Classes']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.IpAccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.Ipv6AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.L2AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup.Classes']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.ClassGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_.AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Rate.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Rate.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions.ConformHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions.ExceedHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions.ViolateHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Rate.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Rate.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Rate.Actions']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Policy_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2.Rate']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily2']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes.Class_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup.Classes']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.Classes.Class_.PacketHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.Classes.Class_']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.Classes.Class_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.Classes']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.IpAccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.Ipv6AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.L2AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup.Classes']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.ClassGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_.AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Rate.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Rate.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions.ConformHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions.ExceedHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions.ViolateHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Rate.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Rate.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Rate.Actions']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Policy_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3.Rate']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.CardFamily3']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes.Class_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup.Classes']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.AccessGroup.Classes.Class_.PacketHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.AccessGroup.Classes.Class_']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.AccessGroup.Classes.Class_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.AccessGroup.Classes']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.AccessGroup.IpAccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.AccessGroup.Ipv6AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.AccessGroup.L2AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.AccessGroup.Classes']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.ClassGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_.AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Policy_']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Rate.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Rate.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Rate.Actions.ConformHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Rate.Actions.ExceedHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Rate.Actions.ViolateHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Rate.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Rate.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Rate.Actions']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily1']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily2']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.CardFamily3']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Policy_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering']['meta_info']
_meta_table['Qos.Policies.Policy.Metering.Rate']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Metering']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes.Class_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup.Classes']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.Classes.Class_.PacketHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.Classes.Class_']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.Classes.Class_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.Classes']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.IpAccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.Ipv6AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.L2AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup.Classes']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.ClassGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_.AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Rate.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Rate.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions.ConformHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions.ExceedHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions.ViolateHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Rate.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Rate.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Rate.Actions']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Policy_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1.Rate']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily1']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes.Class_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup.Classes']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.Classes.Class_.PacketHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.Classes.Class_']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.Classes.Class_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.Classes']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.IpAccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.Ipv6AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.L2AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup.Classes']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.ClassGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_.AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Rate.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Rate.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions.ConformHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions.ExceedHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions.ViolateHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Rate.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Rate.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Rate.Actions']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Policy_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2.Rate']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily2']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes.Class_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup.Classes']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.Classes.Class_.PacketHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.Classes.Class_']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.Classes.Class_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.Classes']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.IpAccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.Ipv6AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.L2AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup.Classes']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.ClassGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_.AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Rate.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Rate.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions.ConformHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions.ExceedHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions.ViolateHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Rate.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Rate.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Rate.Actions']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Policy_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3.Rate']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.CardFamily3']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ConformHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions.ExceedHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate.Actions']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.BitRate']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling.Percentage']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_.PacketHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes.Class_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup.Classes']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.AccessGroup.Classes.Class_.PacketHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.AccessGroup.Classes.Class_']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.AccessGroup.Classes.Class_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.AccessGroup.Classes']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.AccessGroup.IpAccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.AccessGroup.Ipv6AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.AccessGroup.L2AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.AccessGroup.Classes']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_.AccessGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.ClassGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_.AccessGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Policy_']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Rate.Counters.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Rate.Counters']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Rate.Actions.ConformHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Rate.Actions.ExceedHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Rate.Actions.ViolateHandling']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Rate.Actions']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Rate.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Rate.HierarchicalCounters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Rate.Actions']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing.Rate']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily1']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily2']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.CardFamily3']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Policy_']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing']['meta_info']
_meta_table['Qos.Policies.Policy.Policing.Rate']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Policing']['meta_info']
_meta_table['Qos.Policies.Policy.Mdrr.Queue']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Mdrr']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily1.QueuePriorityGroup.RateAbsolute']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily1.QueuePriorityGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily1.QueuePriorityGroup.RatePercentage']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily1.QueuePriorityGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily1.Queue']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily1']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily1.QueuePriorityGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily1']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily1.RateMinimum']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily1']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily1.RateMaximum']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily1']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily2.QueuePriorityGroup.RateAbsolute']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily2.QueuePriorityGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily2.QueuePriorityGroup.RatePercentage']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily2.QueuePriorityGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily2.Queue']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily2']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily2.QueuePriorityGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily2']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily2.RateMinimum']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily2']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily2.RateMaximum']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily2']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup.RateAbsolute']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup.RateMinimum']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup.RatePercentage']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup.RateMinimumPercentage']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3.RateMaximum.Counters']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3.RateMaximum']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3.Queue']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3.QueuePriorityGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3.RateMinimum']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3.RateMaximum']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.QueuePriorityGroup.RateAbsolute']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.QueuePriorityGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.QueuePriorityGroup.RatePercentage']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq.QueuePriorityGroup']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily1']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily2']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.CardFamily3']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.Queue']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.QueuePriorityGroup']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.RateMinimum']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq.RateMaximum']['meta_info'].parent =_meta_table['Qos.Policies.Policy.Pwfq']['meta_info']
_meta_table['Qos.Policies.Policy.ProtocolRateLimit.Arp']['meta_info'].parent =_meta_table['Qos.Policies.Policy.ProtocolRateLimit']['meta_info']
_meta_table['Qos.Policies.Policy.Metering']['meta_info'].parent =_meta_table['Qos.Policies.Policy']['meta_info']
_meta_table['Qos.Policies.Policy.Policing']['meta_info'].parent =_meta_table['Qos.Policies.Policy']['meta_info']
_meta_table['Qos.Policies.Policy.Mdrr']['meta_info'].parent =_meta_table['Qos.Policies.Policy']['meta_info']
_meta_table['Qos.Policies.Policy.Pwfq']['meta_info'].parent =_meta_table['Qos.Policies.Policy']['meta_info']
_meta_table['Qos.Policies.Policy.ProtocolRateLimit']['meta_info'].parent =_meta_table['Qos.Policies.Policy']['meta_info']
_meta_table['Qos.Policies.Policy']['meta_info'].parent =_meta_table['Qos.Policies']['meta_info']
_meta_table['Qos.ClassDefinitions']['meta_info'].parent =_meta_table['Qos']['meta_info']
_meta_table['Qos.ClassMaps']['meta_info'].parent =_meta_table['Qos']['meta_info']
_meta_table['Qos.CongestionAvoidanceMaps']['meta_info'].parent =_meta_table['Qos']['meta_info']
_meta_table['Qos.Profiles']['meta_info'].parent =_meta_table['Qos']['meta_info']
_meta_table['Qos.QueueMaps']['meta_info'].parent =_meta_table['Qos']['meta_info']
_meta_table['Qos.Policies']['meta_info'].parent =_meta_table['Qos']['meta_info']
