


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'LogicalProtocolEnum' : _MetaInfoEnum('LogicalProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper',
        {
            'proto-type-unknown':'proto_type_unknown',
            'proto-type-ethernet':'proto_type_ethernet',
            'proto-type-otn':'proto_type_otn',
        }, 'Cisco-IOS-XR-terminal-device-oper', _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper']),
    'TribProtocolEnum' : _MetaInfoEnum('TribProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper',
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
        }, 'Cisco-IOS-XR-terminal-device-oper', _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper']),
    'TribRateClassEnum' : _MetaInfoEnum('TribRateClassEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper',
        {
            'trib-rate-unknown':'trib_rate_unknown',
            'trib-rate1g':'trib_rate1g',
            'trib-rate25g':'trib_rate25g',
            'trib-rate10g':'trib_rate10g',
            'trib-rate40g':'trib_rate40g',
            'trib-rate100g':'trib_rate100g',
        }, 'Cisco-IOS-XR-terminal-device-oper', _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper']),
    'OpticalInterface.ConfigStatus.PartialConfig' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.ConfigStatus.PartialConfig',
            False, 
            [
            _MetaInfoClassMember('partial-config', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PartialConfig
                ''',
                'partial_config',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'partial-config',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
        ),
    },
    'OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr',
            False, 
            [
            _MetaInfoClassMember('err-str', ATTRIBUTE, 'str' , None, None, 
                [(0, 1024)], [], 
                '''                ErrStr
                ''',
                'err_str',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('err-timestamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                ErrTimestamp
                ''',
                'err_timestamp',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('past-config', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                PastConfig
                ''',
                'past_config',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('past-timestamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                PastTimestamp
                ''',
                'past_timestamp',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('present-config', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                PresentConfig
                ''',
                'present_config',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('present-timestamp', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                PresentTimestamp
                ''',
                'present_timestamp',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('prov-status', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                ProvStatus
                ''',
                'prov_status',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('slice', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Slice
                ''',
                'slice',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'slice-status-attr',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
        ),
    },
    'OpticalInterface.ConfigStatus.SliceTables.SliceTable' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.ConfigStatus.SliceTables.SliceTable',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The index of slice
                ''',
                'index',
                'Cisco-IOS-XR-terminal-device-oper', True),
            _MetaInfoClassMember('slice-status-attr', REFERENCE_CLASS, 'SliceStatusAttr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr', 
                [], [], 
                '''                The bag containing slice config status
                ''',
                'slice_status_attr',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'slice-table',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
        ),
    },
    'OpticalInterface.ConfigStatus.SliceTables' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.ConfigStatus.SliceTables',
            False, 
            [
            _MetaInfoClassMember('slice-table', REFERENCE_LIST, 'SliceTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.ConfigStatus.SliceTables.SliceTable', 
                [], [], 
                '''                The table contains list of slices present
                ''',
                'slice_table',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'slice-tables',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
        ),
    },
    'OpticalInterface.ConfigStatus' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.ConfigStatus',
            False, 
            [
            _MetaInfoClassMember('partial-config', REFERENCE_CLASS, 'PartialConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.ConfigStatus.PartialConfig', 
                [], [], 
                '''                The bag containing partial config status
                ''',
                'partial_config',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('slice-tables', REFERENCE_CLASS, 'SliceTables' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.ConfigStatus.SliceTables', 
                [], [], 
                '''                The container containing slice status
                information
                ''',
                'slice_tables',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'config-status',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
        ),
    },
    'OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr',
            False, 
            [
            _MetaInfoClassMember('frequency', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Frequency
                ''',
                'frequency',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index
                ''',
                'index',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('line-port', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                LinePort
                ''',
                'line_port',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Name
                ''',
                'name',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('oper-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OperMode
                ''',
                'oper_mode',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('power', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Power
                ''',
                'power',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'optical-channel-interface-attr',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
        ),
    },
    'OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface',
            False, 
            [
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The name of the optical-channel
                ''',
                'location',
                'Cisco-IOS-XR-terminal-device-oper', True),
            _MetaInfoClassMember('optical-channel-interface-attr', REFERENCE_CLASS, 'OpticalChannelInterfaceAttr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr', 
                [], [], 
                '''                The operational attributes for an optical
                channel
                ''',
                'optical_channel_interface_attr',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'optical-channel-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
        ),
    },
    'OpticalInterface.OpticalChannelInterfaces' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OpticalChannelInterfaces',
            False, 
            [
            _MetaInfoClassMember('optical-channel-interface', REFERENCE_LIST, 'OpticalChannelInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface', 
                [], [], 
                '''                The operational attributes for an optical
                channel
                ''',
                'optical_channel_interface',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'optical-channel-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
        ),
    },
    'OpticalInterface.Graph.AdjListPath' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.Graph.AdjListPath',
            False, 
            [
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Path
                ''',
                'path',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'adj-list-path',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
        ),
    },
    'OpticalInterface.Graph.GraphStructurePath' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.Graph.GraphStructurePath',
            False, 
            [
            _MetaInfoClassMember('path', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                Path
                ''',
                'path',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'graph-structure-path',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
        ),
    },
    'OpticalInterface.Graph' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.Graph',
            False, 
            [
            _MetaInfoClassMember('adj-list-path', REFERENCE_CLASS, 'AdjListPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.Graph.AdjListPath', 
                [], [], 
                '''                The path containg file which has adjacency list
                stored
                ''',
                'adj_list_path',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('graph-structure-path', REFERENCE_CLASS, 'GraphStructurePath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.Graph.GraphStructurePath', 
                [], [], 
                '''                The path containg file which has graph
                structure stored
                ''',
                'graph_structure_path',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'graph',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
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
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('vendor-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                VendorId
                ''',
                'vendor_id',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'operational-mode-attributes',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
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
                'Cisco-IOS-XR-terminal-device-oper', True),
            _MetaInfoClassMember('operational-mode-attributes', REFERENCE_CLASS, 'OperationalModeAttributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes', 
                [], [], 
                '''                The operational attributes for mxp driver
                fec-mode
                ''',
                'operational_mode_attributes',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'operational-mode',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
        ),
    },
    'OpticalInterface.OperationalModes' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OperationalModes',
            False, 
            [
            _MetaInfoClassMember('operational-mode', REFERENCE_LIST, 'OperationalMode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.OperationalModes.OperationalMode', 
                [], [], 
                '''                Mode supported on Device
                ''',
                'operational_mode',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'operational-modes',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
        ),
    },
    'OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr',
            False, 
            [
            _MetaInfoClassMember('admin-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AdminState
                ''',
                'admin_state',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('ingress-client-port', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                IngressClientPort
                ''',
                'ingress_client_port',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('ingress-physical-channel', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IngressPhysicalChannel
                ''',
                'ingress_physical_channel',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('logical-channel-ifname', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                LogicalChannelIfname
                ''',
                'logical_channel_ifname',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('logical-channel-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LogicalChannelIndex
                ''',
                'logical_channel_index',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('loopback-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LoopbackMode
                ''',
                'loopback_mode',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('protocol-type', REFERENCE_ENUM_CLASS, 'LogicalProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'LogicalProtocolEnum', 
                [], [], 
                '''                ProtocolType
                ''',
                'protocol_type',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('trib-protocol', REFERENCE_ENUM_CLASS, 'TribProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'TribProtocolEnum', 
                [], [], 
                '''                TribProtocol
                ''',
                'trib_protocol',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('trib-rate-class', REFERENCE_ENUM_CLASS, 'TribRateClassEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'TribRateClassEnum', 
                [], [], 
                '''                TribRateClass
                ''',
                'trib_rate_class',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('tti-expected', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                TtiExpected
                ''',
                'tti_expected',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('tti-transmit', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                TtiTransmit
                ''',
                'tti_transmit',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Type
                ''',
                'type',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'optical-logical-interface-attr',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
        ),
    },
    'OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr',
            False, 
            [
            _MetaInfoClassMember('allocation', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Allocation
                ''',
                'allocation',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('assignment-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AssignmentType
                ''',
                'assignment_type',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index
                ''',
                'index',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('is-logical-link', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IsLogicalLink
                ''',
                'is_logical_link',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('logical-channel', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LogicalChannel
                ''',
                'logical_channel',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                Name
                ''',
                'name',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('optical-channel', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                OpticalChannel
                ''',
                'optical_channel',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'optical-logical-interface-logical-channel-assignment-attr',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
        ),
    },
    'OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The index of the logical-channel
                ''',
                'index',
                'Cisco-IOS-XR-terminal-device-oper', True),
            _MetaInfoClassMember('optical-logical-interface-logical-channel-assignment-attr', REFERENCE_CLASS, 'OpticalLogicalInterfaceLogicalChannelAssignmentAttr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr', 
                [], [], 
                '''                The operational attributes for a logical
                channel assignment
                ''',
                'optical_logical_interface_logical_channel_assignment_attr',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'optical-logical-interface-logical-channel-assignment',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
        ),
    },
    'OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments',
            False, 
            [
            _MetaInfoClassMember('optical-logical-interface-logical-channel-assignment', REFERENCE_LIST, 'OpticalLogicalInterfaceLogicalChannelAssignment' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment', 
                [], [], 
                '''                The operational attributes for a logical
                channel assignment
                ''',
                'optical_logical_interface_logical_channel_assignment',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'optical-logical-interface-logical-channel-assignments',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
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
                'Cisco-IOS-XR-terminal-device-oper', True),
            _MetaInfoClassMember('optical-logical-interface-attr', REFERENCE_CLASS, 'OpticalLogicalInterfaceAttr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr', 
                [], [], 
                '''                The operational attributes for a particular
                logical channel
                ''',
                'optical_logical_interface_attr',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('optical-logical-interface-logical-channel-assignments', REFERENCE_CLASS, 'OpticalLogicalInterfaceLogicalChannelAssignments' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments', 
                [], [], 
                '''                The operational attributes for a particular
                interface
                ''',
                'optical_logical_interface_logical_channel_assignments',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'optical-logical-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
        ),
    },
    'OpticalInterface.OpticalLogicalInterfaces' : {
        'meta_info' : _MetaInfoClass('OpticalInterface.OpticalLogicalInterfaces',
            False, 
            [
            _MetaInfoClassMember('optical-logical-interface', REFERENCE_LIST, 'OpticalLogicalInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface', 
                [], [], 
                '''                The operational attributes for a logical
                channel
                ''',
                'optical_logical_interface',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'optical-logical-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
        ),
    },
    'OpticalInterface' : {
        'meta_info' : _MetaInfoClass('OpticalInterface',
            False, 
            [
            _MetaInfoClassMember('config-status', REFERENCE_CLASS, 'ConfigStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.ConfigStatus', 
                [], [], 
                '''                Table containing status information
                ''',
                'config_status',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('graph', REFERENCE_CLASS, 'Graph' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.Graph', 
                [], [], 
                '''                Table containing Graph Structure and related
                info
                ''',
                'graph',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('operational-modes', REFERENCE_CLASS, 'OperationalModes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.OperationalModes', 
                [], [], 
                '''                The Operational Mode Table
                ''',
                'operational_modes',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('optical-channel-interfaces', REFERENCE_CLASS, 'OpticalChannelInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.OpticalChannelInterfaces', 
                [], [], 
                '''                The operational attributes for a particular
                optical channel
                ''',
                'optical_channel_interfaces',
                'Cisco-IOS-XR-terminal-device-oper', False),
            _MetaInfoClassMember('optical-logical-interfaces', REFERENCE_CLASS, 'OpticalLogicalInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper', 'OpticalInterface.OpticalLogicalInterfaces', 
                [], [], 
                '''                The operational attributes for a logical channel
                ''',
                'optical_logical_interfaces',
                'Cisco-IOS-XR-terminal-device-oper', False),
            ],
            'Cisco-IOS-XR-terminal-device-oper',
            'optical-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-terminal-device-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_terminal_device_oper'
        ),
    },
}
_meta_table['OpticalInterface.ConfigStatus.SliceTables.SliceTable.SliceStatusAttr']['meta_info'].parent =_meta_table['OpticalInterface.ConfigStatus.SliceTables.SliceTable']['meta_info']
_meta_table['OpticalInterface.ConfigStatus.SliceTables.SliceTable']['meta_info'].parent =_meta_table['OpticalInterface.ConfigStatus.SliceTables']['meta_info']
_meta_table['OpticalInterface.ConfigStatus.PartialConfig']['meta_info'].parent =_meta_table['OpticalInterface.ConfigStatus']['meta_info']
_meta_table['OpticalInterface.ConfigStatus.SliceTables']['meta_info'].parent =_meta_table['OpticalInterface.ConfigStatus']['meta_info']
_meta_table['OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface.OpticalChannelInterfaceAttr']['meta_info'].parent =_meta_table['OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface']['meta_info']
_meta_table['OpticalInterface.OpticalChannelInterfaces.OpticalChannelInterface']['meta_info'].parent =_meta_table['OpticalInterface.OpticalChannelInterfaces']['meta_info']
_meta_table['OpticalInterface.Graph.AdjListPath']['meta_info'].parent =_meta_table['OpticalInterface.Graph']['meta_info']
_meta_table['OpticalInterface.Graph.GraphStructurePath']['meta_info'].parent =_meta_table['OpticalInterface.Graph']['meta_info']
_meta_table['OpticalInterface.OperationalModes.OperationalMode.OperationalModeAttributes']['meta_info'].parent =_meta_table['OpticalInterface.OperationalModes.OperationalMode']['meta_info']
_meta_table['OpticalInterface.OperationalModes.OperationalMode']['meta_info'].parent =_meta_table['OpticalInterface.OperationalModes']['meta_info']
_meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment.OpticalLogicalInterfaceLogicalChannelAssignmentAttr']['meta_info'].parent =_meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment']['meta_info']
_meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments.OpticalLogicalInterfaceLogicalChannelAssignment']['meta_info'].parent =_meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments']['meta_info']
_meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceAttr']['meta_info'].parent =_meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface']['meta_info']
_meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface.OpticalLogicalInterfaceLogicalChannelAssignments']['meta_info'].parent =_meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface']['meta_info']
_meta_table['OpticalInterface.OpticalLogicalInterfaces.OpticalLogicalInterface']['meta_info'].parent =_meta_table['OpticalInterface.OpticalLogicalInterfaces']['meta_info']
_meta_table['OpticalInterface.ConfigStatus']['meta_info'].parent =_meta_table['OpticalInterface']['meta_info']
_meta_table['OpticalInterface.OpticalChannelInterfaces']['meta_info'].parent =_meta_table['OpticalInterface']['meta_info']
_meta_table['OpticalInterface.Graph']['meta_info'].parent =_meta_table['OpticalInterface']['meta_info']
_meta_table['OpticalInterface.OperationalModes']['meta_info'].parent =_meta_table['OpticalInterface']['meta_info']
_meta_table['OpticalInterface.OpticalLogicalInterfaces']['meta_info'].parent =_meta_table['OpticalInterface']['meta_info']
