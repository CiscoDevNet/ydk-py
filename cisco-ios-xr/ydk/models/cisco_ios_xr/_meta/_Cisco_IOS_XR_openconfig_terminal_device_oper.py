


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'LogicalProtocolEnum' : _MetaInfoEnum('LogicalProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper',
        {
            'proto-type-unknown':'proto_type_unknown',
            'proto-type-ethernet':'proto_type_ethernet',
            'proto-type-otn':'proto_type_otn',
        }, 'Cisco-IOS-XR-openconfig-terminal-device-oper', _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-oper']),
    'TribProtocolEnum' : _MetaInfoEnum('TribProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper',
        {
            'trib-proto-type-unknown':'trib_proto_type_unknown',
            'trib-proto-type1ge':'trib_proto_type1ge',
            'trib-proto-type-oc48':'trib_proto_type_oc48',
            'trib-proto-type-stm16':'trib_proto_type_stm16',
            'trib-proto-type10gelan':'trib_proto_type10gelan',
            'trib-proto-type10gewan':'trib_proto_type10gewan',
            'trib-proto-type-oc192':'trib_proto_type_oc192',
            'trib-proto-type-stm64':'trib_proto_type_stm64',
            'trib-proto-type-otu2':'trib_proto_type_otu2',
            'trib-proto-type-otu2e':'trib_proto_type_otu2e',
            'trib-proto-type-otu1e':'trib_proto_type_otu1e',
            'trib-proto-type-odu2':'trib_proto_type_odu2',
            'trib-proto-type-odu2e':'trib_proto_type_odu2e',
            'trib-proto-type40ge':'trib_proto_type40ge',
            'trib-proto-type-oc768':'trib_proto_type_oc768',
            'trib-proto-type-stm256':'trib_proto_type_stm256',
            'trib-proto-type-otu3':'trib_proto_type_otu3',
            'trib-proto-type-odu3':'trib_proto_type_odu3',
            'trib-proto-type100ge':'trib_proto_type100ge',
            'trib-proto-type100g-mlg':'trib_proto_type100g_mlg',
            'trib-proto-type-otu4':'trib_proto_type_otu4',
            'trib-proto-type-otu-cn':'trib_proto_type_otu_cn',
            'trib-proto-type-odu4':'trib_proto_type_odu4',
        }, 'Cisco-IOS-XR-openconfig-terminal-device-oper', _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-oper']),
    'TribRateClassEnum' : _MetaInfoEnum('TribRateClassEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper',
        {
            'trib-rate1g':'trib_rate1g',
            'trib-rate25g':'trib_rate25g',
            'trib-rate10g':'trib_rate10g',
            'trib-rate40g':'trib_rate40g',
            'trib-rate100g':'trib_rate100g',
            'trib-rate-unknown':'trib_rate_unknown',
        }, 'Cisco-IOS-XR-openconfig-terminal-device-oper', _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-oper']),
    'OpticalInterface.OpticalClientInterfaces.OpticalClientInterface.OpticalClientLogicalChannelAssignments.OpticalClientLogicalChannelAssignment' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OpticalClientInterfaces.OpticalClientInterface.OpticalClientLogicalChannelAssignments.OpticalClientLogicalChannelAssignment',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The index of the interface
                ''',
                'index',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', True),
            _MetaInfoClassMember('allocation', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Allocation
                ''',
                'allocation',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            _MetaInfoClassMember('is-logical-link', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IsLogicalLink
                ''',
                'is_logical_link',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            _MetaInfoClassMember('logical-channel', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LogicalChannel
                ''',
                'logical_channel',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            _MetaInfoClassMember('optical-channel', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                OpticalChannel
                ''',
                'optical_channel',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-oper',
            'optical-client-logical-channel-assignment',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper'
        ),
    },
    'OpticalInterface.OpticalClientInterfaces.OpticalClientInterface.OpticalClientLogicalChannelAssignments' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OpticalClientInterfaces.OpticalClientInterface.OpticalClientLogicalChannelAssignments',
            False, 
            [
            _MetaInfoClassMember('optical-client-logical-channel-assignment', REFERENCE_LIST, 'OpticalClientLogicalChannelAssignment' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper', 'OpticalInterface.OpticalClientInterfaces.OpticalClientInterface.OpticalClientLogicalChannelAssignments.OpticalClientLogicalChannelAssignment', 
                [], [], 
                '''                The operational attributes for a Underline
                Ether Interface
                ''',
                'optical_client_logical_channel_assignment',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-oper',
            'optical-client-logical-channel-assignments',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper'
        ),
    },
    'OpticalInterface.OpticalClientInterfaces.OpticalClientInterface' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OpticalClientInterfaces.OpticalClientInterface',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the client interface
                ''',
                'name',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', True),
            _MetaInfoClassMember('optical-client-logical-channel-assignments', REFERENCE_CLASS, 'OpticalClientLogicalChannelAssignments' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper', 'OpticalInterface.OpticalClientInterfaces.OpticalClientInterface.OpticalClientLogicalChannelAssignments', 
                [], [], 
                '''                The operational attributes for a Underline
                Ether Interface
                ''',
                'optical_client_logical_channel_assignments',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-oper',
            'optical-client-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper'
        ),
    },
    'OpticalInterface.OpticalClientInterfaces' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OpticalClientInterfaces',
            False, 
            [
            _MetaInfoClassMember('optical-client-interface', REFERENCE_LIST, 'OpticalClientInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper', 'OpticalInterface.OpticalClientInterfaces.OpticalClientInterface', 
                [], [], 
                '''                The operational attributes for Client Port
                ''',
                'optical_client_interface',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-oper',
            'optical-client-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper'
        ),
    },
    'OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Description
                ''',
                'description',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            _MetaInfoClassMember('vendor-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                VendorId
                ''',
                'vendor_id',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-oper',
            'operational-mode-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper'
        ),
    },
    'OpticalInterface.OperationalModes.OperationalMode' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OperationalModes.OperationalMode',
            False, 
            [
            _MetaInfoClassMember('mode-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Mode-id for supported mode on Device
                ''',
                'mode_id',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', True),
            _MetaInfoClassMember('operational-mode-attributes', REFERENCE_CLASS, 'OperationalModeAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper', 'OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes', 
                [], [], 
                '''                The operational attributes for mxp driver
                fec-mode
                ''',
                'operational_mode_attributes',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-oper',
            'operational-mode',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper'
        ),
    },
    'OpticalInterface.OperationalModes' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OperationalModes',
            False, 
            [
            _MetaInfoClassMember('operational-mode', REFERENCE_LIST, 'OperationalMode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper', 'OpticalInterface.OperationalModes.OperationalMode', 
                [], [], 
                '''                Mode supported on Device
                ''',
                'operational_mode',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-oper',
            'operational-modes',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper'
        ),
    },
    'OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr',
            False, 
            [
            _MetaInfoClassMember('protocol-type', REFERENCE_ENUM_CLASS, 'LogicalProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper', 'LogicalProtocolEnum', 
                [], [], 
                '''                ProtocolType
                ''',
                'protocol_type',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            _MetaInfoClassMember('trib-protocol', REFERENCE_ENUM_CLASS, 'TribProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper', 'TribProtocolEnum', 
                [], [], 
                '''                TribProtocol
                ''',
                'trib_protocol',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            _MetaInfoClassMember('trib-rate-class', REFERENCE_ENUM_CLASS, 'TribRateClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper', 'TribRateClassEnum', 
                [], [], 
                '''                TribRateClass
                ''',
                'trib_rate_class',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-oper',
            'optical-logical-interface-attr',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper'
        ),
    },
    'OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The index of the interface
                ''',
                'index',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', True),
            _MetaInfoClassMember('allocation', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Allocation
                ''',
                'allocation',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            _MetaInfoClassMember('is-logical-link', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IsLogicalLink
                ''',
                'is_logical_link',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            _MetaInfoClassMember('logical-channel', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LogicalChannel
                ''',
                'logical_channel',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            _MetaInfoClassMember('optical-channel', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                OpticalChannel
                ''',
                'optical_channel',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-oper',
            'optical-logical-interface-logical-channel-assignment',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper'
        ),
    },
    'OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments',
            False, 
            [
            _MetaInfoClassMember('optical-logical-interface-logical-channel-assignment', REFERENCE_LIST, 'OpticalLogicalInterfaceLogicalChannelAssignment' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper', 'OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment', 
                [], [], 
                '''                The operational attributes for a particular
                interface
                ''',
                'optical_logical_interface_logical_channel_assignment',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-oper',
            'optical-logical-interface-logical-channel-assignments',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper'
        ),
    },
    'OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The index of the logical-channel
                ''',
                'index',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', True),
            _MetaInfoClassMember('optical-logical-interface-attr', REFERENCE_CLASS, 'OpticalLogicalInterfaceAttr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper', 'OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr', 
                [], [], 
                '''                The operational attributes for a particular
                interface
                ''',
                'optical_logical_interface_attr',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            _MetaInfoClassMember('optical-logical-interface-logical-channel-assignments', REFERENCE_CLASS, 'OpticalLogicalInterfaceLogicalChannelAssignments' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper', 'OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments', 
                [], [], 
                '''                The operational attributes for a particular
                interface
                ''',
                'optical_logical_interface_logical_channel_assignments',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-oper',
            'optical-logical-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper'
        ),
    },
    'OpticalInterface.OpticalLogicalInterfaces' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OpticalLogicalInterfaces',
            False, 
            [
            _MetaInfoClassMember('optical-logical-interface', REFERENCE_LIST, 'OpticalLogicalInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper', 'OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface', 
                [], [], 
                '''                The operational attributes for a particular
                interface
                ''',
                'optical_logical_interface',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-oper',
            'optical-logical-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper'
        ),
    },
    'OpticalInterface' : {
        'meta_info' : _MetaInfoClass('OpticalInterface',
            False, 
            [
            _MetaInfoClassMember('operational-modes', REFERENCE_CLASS, 'OperationalModes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper', 'OpticalInterface.OperationalModes', 
                [], [], 
                '''                The Operational Mode Table
                ''',
                'operational_modes',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            _MetaInfoClassMember('optical-client-interfaces', REFERENCE_CLASS, 'OpticalClientInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper', 'OpticalInterface.OpticalClientInterfaces', 
                [], [], 
                '''                The operational attributes table for Client Port
                ''',
                'optical_client_interfaces',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            _MetaInfoClassMember('optical-logical-interfaces', REFERENCE_CLASS, 'OpticalLogicalInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper', 'OpticalInterface.OpticalLogicalInterfaces', 
                [], [], 
                '''                The operational attributes for a particular
                interface
                ''',
                'optical_logical_interfaces',
                'Cisco-IOS-XR-openconfig-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-openconfig-terminal-device-oper',
            'optical-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-openconfig-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_openconfig_terminal_device_oper'
        ),
    },
}
_meta_table['OpticalInterface.OpticalClientInterfaces.OpticalClientInterface.OpticalClientLogicalChannelAssignments.OpticalClientLogicalChannelAssignment']['meta_info'].parent =_meta_table['OpticalInterface.OpticalClientInterfaces.OpticalClientInterface.OpticalClientLogicalChannelAssignments']['meta_info']
_meta_table['OpticalInterface.OpticalClientInterfaces.OpticalClientInterface.OpticalClientLogicalChannelAssignments']['meta_info'].parent =_meta_table['OpticalInterface.OpticalClientInterfaces.OpticalClientInterface']['meta_info']
_meta_table['OpticalInterface.OpticalClientInterfaces.OpticalClientInterface']['meta_info'].parent =_meta_table['OpticalInterface.OpticalClientInterfaces']['meta_info']
_meta_table['OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes']['meta_info'].parent =_meta_table['OpticalInterface.OperationalModes.OperationalMode']['meta_info']
_meta_table['OpticalInterface.OperationalModes.OperationalMode']['meta_info'].parent =_meta_table['OpticalInterface.OperationalModes']['meta_info']
_meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment']['meta_info'].parent =_meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments']['meta_info']
_meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr']['meta_info'].parent =_meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface']['meta_info']
_meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments']['meta_info'].parent =_meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface']['meta_info']
_meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface']['meta_info'].parent =_meta_table['OpticalInterface.OpticalLogicalInterfaces']['meta_info']
_meta_table['OpticalInterface.OpticalClientInterfaces']['meta_info'].parent =_meta_table['OpticalInterface']['meta_info']
_meta_table['OpticalInterface.OperationalModes']['meta_info'].parent =_meta_table['OpticalInterface']['meta_info']
_meta_table['OpticalInterface.OpticalLogicalInterfaces']['meta_info'].parent =_meta_table['OpticalInterface']['meta_info']
