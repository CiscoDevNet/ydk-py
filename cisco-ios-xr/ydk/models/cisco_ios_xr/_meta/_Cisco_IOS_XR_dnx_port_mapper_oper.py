


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Oor.Nodes.Node.InterfaceNpuResources.InterfaceNpuResource.Member.DpaTable' : {
        'meta_info' : _MetaInfoClass('Oor.Nodes.Node.InterfaceNpuResources.InterfaceNpuResource.Member.DpaTable',
            False, 
            [
            _MetaInfoClassMember('in-use', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                In-use entries of NPU resource DB for this
                logical table
                ''',
                'in_use',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('in-use-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                In-use entries of NPU resource DB for this
                logical table
                ''',
                'in_use_percent',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Logical (DPA) table name
                ''',
                'name',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            ],
            'Cisco-IOS-XR-dnx-port-mapper-oper',
            'dpa-table',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-port-mapper-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper'
        ),
    },
    'Oor.Nodes.Node.InterfaceNpuResources.InterfaceNpuResource.Member' : {
        'meta_info' : _MetaInfoClass('Oor.Nodes.Node.InterfaceNpuResources.InterfaceNpuResource.Member',
            False, 
            [
            _MetaInfoClassMember('dpa-table', REFERENCE_LIST, 'DpaTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper', 'Oor.Nodes.Node.InterfaceNpuResources.InterfaceNpuResource.Member.DpaTable', 
                [], [], 
                '''                Logical (DPA) tables information
                ''',
                'dpa_table',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the member interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Rack/Slot/Instance of the interface
                ''',
                'location',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('npu-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Npu Id of the interface
                ''',
                'npu_id',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('number-of-dpa-tables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of logical tables using this NPU resource
                ''',
                'number_of_dpa_tables',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('total-in-use', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total In-use entries of NPU resource DB
                ''',
                'total_in_use',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('total-in-use-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total In-use percentage of NPU resource DB
                ''',
                'total_in_use_percent',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            ],
            'Cisco-IOS-XR-dnx-port-mapper-oper',
            'member',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-port-mapper-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper'
        ),
    },
    'Oor.Nodes.Node.InterfaceNpuResources.InterfaceNpuResource' : {
        'meta_info' : _MetaInfoClass('Oor.Nodes.Node.InterfaceNpuResources.InterfaceNpuResource',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-dnx-port-mapper-oper', True),
            _MetaInfoClassMember('interface-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Current OOR state of the interface/bundle
                ''',
                'interface_state',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('max-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max entries in NPU for this HW resource
                ''',
                'max_entries',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('member', REFERENCE_LIST, 'Member' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper', 'Oor.Nodes.Node.InterfaceNpuResources.InterfaceNpuResource.Member', 
                [], [], 
                '''                Interface/Bundle member HW/NPU resources
                ''',
                'member',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                HW/NPU resource name
                ''',
                'name',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('number-of-members', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of bundle members. for non-bundles this
                will be 1
                ''',
                'number_of_members',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('red-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Red threshold
                ''',
                'red_threshold',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('red-threshold-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Red threshold percentage
                ''',
                'red_threshold_percent',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Timestamp of last OOR change
                ''',
                'time_stamp',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('yellow-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Yellow threshold
                ''',
                'yellow_threshold',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('yellow-threshold-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Yellow threshold percentage
                ''',
                'yellow_threshold_percent',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            ],
            'Cisco-IOS-XR-dnx-port-mapper-oper',
            'interface-npu-resource',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-port-mapper-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper'
        ),
    },
    'Oor.Nodes.Node.InterfaceNpuResources' : {
        'meta_info' : _MetaInfoClass('Oor.Nodes.Node.InterfaceNpuResources',
            False, 
            [
            _MetaInfoClassMember('interface-npu-resource', REFERENCE_LIST, 'InterfaceNpuResource' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper', 'Oor.Nodes.Node.InterfaceNpuResources.InterfaceNpuResource', 
                [], [], 
                '''                OOR information with NPU resources for an
                interface
                ''',
                'interface_npu_resource',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            ],
            'Cisco-IOS-XR-dnx-port-mapper-oper',
            'interface-npu-resources',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-port-mapper-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper'
        ),
    },
    'Oor.Nodes.Node.BundleInterfaceDetails.BundleInterfaceDetail.Member' : {
        'meta_info' : _MetaInfoClass('Oor.Nodes.Node.BundleInterfaceDetails.BundleInterfaceDetail.Member',
            False, 
            [
            _MetaInfoClassMember('hardware-resource', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Type of harware resoruce
                ''',
                'hardware_resource',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('interface-status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The current state of the interface
                ''',
                'interface_status',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('npu-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Npuid of the interface
                ''',
                'npu_id',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Timestamp
                ''',
                'time_stamp',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            ],
            'Cisco-IOS-XR-dnx-port-mapper-oper',
            'member',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-port-mapper-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper'
        ),
    },
    'Oor.Nodes.Node.BundleInterfaceDetails.BundleInterfaceDetail' : {
        'meta_info' : _MetaInfoClass('Oor.Nodes.Node.BundleInterfaceDetails.BundleInterfaceDetail',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Interface Name
                ''',
                'interface',
                'Cisco-IOS-XR-dnx-port-mapper-oper', True),
            _MetaInfoClassMember('interface-state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Current state of the interface
                ''',
                'interface_state',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('member', REFERENCE_LIST, 'Member' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper', 'Oor.Nodes.Node.BundleInterfaceDetails.BundleInterfaceDetail.Member', 
                [], [], 
                '''                Member details
                ''',
                'member',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False, max_elements=64),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Timestamp
                ''',
                'time_stamp',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            ],
            'Cisco-IOS-XR-dnx-port-mapper-oper',
            'bundle-interface-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-port-mapper-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper'
        ),
    },
    'Oor.Nodes.Node.BundleInterfaceDetails' : {
        'meta_info' : _MetaInfoClass('Oor.Nodes.Node.BundleInterfaceDetails',
            False, 
            [
            _MetaInfoClassMember('bundle-interface-detail', REFERENCE_LIST, 'BundleInterfaceDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper', 'Oor.Nodes.Node.BundleInterfaceDetails.BundleInterfaceDetail', 
                [], [], 
                '''                OOR Data for particular Bundle interface
                ''',
                'bundle_interface_detail',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            ],
            'Cisco-IOS-XR-dnx-port-mapper-oper',
            'bundle-interface-details',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-port-mapper-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper'
        ),
    },
    'Oor.Nodes.Node.InterfaceDetails.InterfaceDetail' : {
        'meta_info' : _MetaInfoClass('Oor.Nodes.Node.InterfaceDetails.InterfaceDetail',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Interface Name
                ''',
                'interface',
                'Cisco-IOS-XR-dnx-port-mapper-oper', True),
            _MetaInfoClassMember('hardware-resource', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Type of harware resoruce
                ''',
                'hardware_resource',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('interface-status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The current state of the interface
                ''',
                'interface_status',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('npu-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Npuid of the interface
                ''',
                'npu_id',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('time-stamp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Timestamp
                ''',
                'time_stamp',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            ],
            'Cisco-IOS-XR-dnx-port-mapper-oper',
            'interface-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-port-mapper-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper'
        ),
    },
    'Oor.Nodes.Node.InterfaceDetails' : {
        'meta_info' : _MetaInfoClass('Oor.Nodes.Node.InterfaceDetails',
            False, 
            [
            _MetaInfoClassMember('interface-detail', REFERENCE_LIST, 'InterfaceDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper', 'Oor.Nodes.Node.InterfaceDetails.InterfaceDetail', 
                [], [], 
                '''                OOR Data for particular interface
                ''',
                'interface_detail',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            ],
            'Cisco-IOS-XR-dnx-port-mapper-oper',
            'interface-details',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-port-mapper-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper'
        ),
    },
    'Oor.Nodes.Node.InterfaceSummaryDatas.InterfaceSummaryData' : {
        'meta_info' : _MetaInfoClass('Oor.Nodes.Node.InterfaceSummaryDatas.InterfaceSummaryData',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Interface Number
                ''',
                'interface',
                'Cisco-IOS-XR-dnx-port-mapper-oper', True),
            _MetaInfoClassMember('hardware-resource', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Type of harware resoruce
                ''',
                'hardware_resource',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('interface-status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The current state of the interface
                ''',
                'interface_status',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            ],
            'Cisco-IOS-XR-dnx-port-mapper-oper',
            'interface-summary-data',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-port-mapper-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper'
        ),
    },
    'Oor.Nodes.Node.InterfaceSummaryDatas' : {
        'meta_info' : _MetaInfoClass('Oor.Nodes.Node.InterfaceSummaryDatas',
            False, 
            [
            _MetaInfoClassMember('interface-summary-data', REFERENCE_LIST, 'InterfaceSummaryData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper', 'Oor.Nodes.Node.InterfaceSummaryDatas.InterfaceSummaryData', 
                [], [], 
                '''                OOR Data for particular interface
                ''',
                'interface_summary_data',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            ],
            'Cisco-IOS-XR-dnx-port-mapper-oper',
            'interface-summary-datas',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-port-mapper-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper'
        ),
    },
    'Oor.Nodes.Node.OorSummary' : {
        'meta_info' : _MetaInfoClass('Oor.Nodes.Node.OorSummary',
            False, 
            [
            _MetaInfoClassMember('green', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                interfaces in green state
                ''',
                'green',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('red', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                interfaces in red state
                ''',
                'red',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('yel-low', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                interfaces in yellow state
                ''',
                'yel_low',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            ],
            'Cisco-IOS-XR-dnx-port-mapper-oper',
            'oor-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-port-mapper-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper'
        ),
    },
    'Oor.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Oor.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_name',
                'Cisco-IOS-XR-dnx-port-mapper-oper', True),
            _MetaInfoClassMember('bundle-interface-details', REFERENCE_CLASS, 'BundleInterfaceDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper', 'Oor.Nodes.Node.BundleInterfaceDetails', 
                [], [], 
                '''                OOR Bundle Interface Detail
                ''',
                'bundle_interface_details',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('interface-details', REFERENCE_CLASS, 'InterfaceDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper', 'Oor.Nodes.Node.InterfaceDetails', 
                [], [], 
                '''                OOR Interface Detail
                ''',
                'interface_details',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('interface-npu-resources', REFERENCE_CLASS, 'InterfaceNpuResources' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper', 'Oor.Nodes.Node.InterfaceNpuResources', 
                [], [], 
                '''                OOR information with NPU resources
                ''',
                'interface_npu_resources',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('interface-summary-datas', REFERENCE_CLASS, 'InterfaceSummaryDatas' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper', 'Oor.Nodes.Node.InterfaceSummaryDatas', 
                [], [], 
                '''                OOR Per Interface Summary
                ''',
                'interface_summary_datas',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            _MetaInfoClassMember('oor-summary', REFERENCE_CLASS, 'OorSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper', 'Oor.Nodes.Node.OorSummary', 
                [], [], 
                '''                OOR Summary
                ''',
                'oor_summary',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            ],
            'Cisco-IOS-XR-dnx-port-mapper-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-port-mapper-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper'
        ),
    },
    'Oor.Nodes' : {
        'meta_info' : _MetaInfoClass('Oor.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper', 'Oor.Nodes.Node', 
                [], [], 
                '''                DPA operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            ],
            'Cisco-IOS-XR-dnx-port-mapper-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-port-mapper-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper'
        ),
    },
    'Oor' : {
        'meta_info' : _MetaInfoClass('Oor',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper', 'Oor.Nodes', 
                [], [], 
                '''                OOR data for available nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-dnx-port-mapper-oper', False),
            ],
            'Cisco-IOS-XR-dnx-port-mapper-oper',
            'oor',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-port-mapper-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dnx_port_mapper_oper'
        ),
    },
}
_meta_table['Oor.Nodes.Node.InterfaceNpuResources.InterfaceNpuResource.Member.DpaTable']['meta_info'].parent =_meta_table['Oor.Nodes.Node.InterfaceNpuResources.InterfaceNpuResource.Member']['meta_info']
_meta_table['Oor.Nodes.Node.InterfaceNpuResources.InterfaceNpuResource.Member']['meta_info'].parent =_meta_table['Oor.Nodes.Node.InterfaceNpuResources.InterfaceNpuResource']['meta_info']
_meta_table['Oor.Nodes.Node.InterfaceNpuResources.InterfaceNpuResource']['meta_info'].parent =_meta_table['Oor.Nodes.Node.InterfaceNpuResources']['meta_info']
_meta_table['Oor.Nodes.Node.BundleInterfaceDetails.BundleInterfaceDetail.Member']['meta_info'].parent =_meta_table['Oor.Nodes.Node.BundleInterfaceDetails.BundleInterfaceDetail']['meta_info']
_meta_table['Oor.Nodes.Node.BundleInterfaceDetails.BundleInterfaceDetail']['meta_info'].parent =_meta_table['Oor.Nodes.Node.BundleInterfaceDetails']['meta_info']
_meta_table['Oor.Nodes.Node.InterfaceDetails.InterfaceDetail']['meta_info'].parent =_meta_table['Oor.Nodes.Node.InterfaceDetails']['meta_info']
_meta_table['Oor.Nodes.Node.InterfaceSummaryDatas.InterfaceSummaryData']['meta_info'].parent =_meta_table['Oor.Nodes.Node.InterfaceSummaryDatas']['meta_info']
_meta_table['Oor.Nodes.Node.InterfaceNpuResources']['meta_info'].parent =_meta_table['Oor.Nodes.Node']['meta_info']
_meta_table['Oor.Nodes.Node.BundleInterfaceDetails']['meta_info'].parent =_meta_table['Oor.Nodes.Node']['meta_info']
_meta_table['Oor.Nodes.Node.InterfaceDetails']['meta_info'].parent =_meta_table['Oor.Nodes.Node']['meta_info']
_meta_table['Oor.Nodes.Node.InterfaceSummaryDatas']['meta_info'].parent =_meta_table['Oor.Nodes.Node']['meta_info']
_meta_table['Oor.Nodes.Node.OorSummary']['meta_info'].parent =_meta_table['Oor.Nodes.Node']['meta_info']
_meta_table['Oor.Nodes.Node']['meta_info'].parent =_meta_table['Oor.Nodes']['meta_info']
_meta_table['Oor.Nodes']['meta_info'].parent =_meta_table['Oor']['meta_info']
