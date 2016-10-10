


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
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
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
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
_meta_table['Oor.Nodes.Node.BundleInterfaceDetails.BundleInterfaceDetail.Member']['meta_info'].parent =_meta_table['Oor.Nodes.Node.BundleInterfaceDetails.BundleInterfaceDetail']['meta_info']
_meta_table['Oor.Nodes.Node.BundleInterfaceDetails.BundleInterfaceDetail']['meta_info'].parent =_meta_table['Oor.Nodes.Node.BundleInterfaceDetails']['meta_info']
_meta_table['Oor.Nodes.Node.InterfaceDetails.InterfaceDetail']['meta_info'].parent =_meta_table['Oor.Nodes.Node.InterfaceDetails']['meta_info']
_meta_table['Oor.Nodes.Node.InterfaceSummaryDatas.InterfaceSummaryData']['meta_info'].parent =_meta_table['Oor.Nodes.Node.InterfaceSummaryDatas']['meta_info']
_meta_table['Oor.Nodes.Node.BundleInterfaceDetails']['meta_info'].parent =_meta_table['Oor.Nodes.Node']['meta_info']
_meta_table['Oor.Nodes.Node.InterfaceDetails']['meta_info'].parent =_meta_table['Oor.Nodes.Node']['meta_info']
_meta_table['Oor.Nodes.Node.InterfaceSummaryDatas']['meta_info'].parent =_meta_table['Oor.Nodes.Node']['meta_info']
_meta_table['Oor.Nodes.Node.OorSummary']['meta_info'].parent =_meta_table['Oor.Nodes.Node']['meta_info']
_meta_table['Oor.Nodes.Node']['meta_info'].parent =_meta_table['Oor.Nodes']['meta_info']
_meta_table['Oor.Nodes']['meta_info'].parent =_meta_table['Oor']['meta_info']
