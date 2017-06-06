


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-pfilter-oper', True),
            _MetaInfoClassMember('acl-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                acl information
                ''',
                'acl_info',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'interface-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos',
            False, 
            [
            _MetaInfoClassMember('interface-info', REFERENCE_LIST, 'InterfaceInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo', 
                [], [], 
                '''                Operational data for pfilter in bag
                ''',
                'interface_info',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'interface-infos',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable',
            False, 
            [
            _MetaInfoClassMember('interface-infos', REFERENCE_CLASS, 'InterfaceInfos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos', 
                [], [], 
                '''                Operational data for pfilter
                ''',
                'interface_infos',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'acl-info-table',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv6' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv6',
            False, 
            [
            _MetaInfoClassMember('acl-info-table', REFERENCE_CLASS, 'AclInfoTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable', 
                [], [], 
                '''                Operational data for pfilter
                ''',
                'acl_info_table',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-pfilter-oper', True),
            _MetaInfoClassMember('acl-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                acl information
                ''',
                'acl_info',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'interface-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos',
            False, 
            [
            _MetaInfoClassMember('interface-info', REFERENCE_LIST, 'InterfaceInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo', 
                [], [], 
                '''                Operational data for pfilter in bag
                ''',
                'interface_info',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'interface-infos',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable',
            False, 
            [
            _MetaInfoClassMember('interface-infos', REFERENCE_CLASS, 'InterfaceInfos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos', 
                [], [], 
                '''                Operational data for pfilter
                ''',
                'interface_infos',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'acl-info-table',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv4' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv4',
            False, 
            [
            _MetaInfoClassMember('acl-info-table', REFERENCE_CLASS, 'AclInfoTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable', 
                [], [], 
                '''                Operational data for pfilter
                ''',
                'acl_info_table',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa.Nodes.Node.Process' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv4', 
                [], [], 
                '''                Operational data for pfilter
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv6', 
                [], [], 
                '''                Operational data for pfilter
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'process',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node
                ''',
                'node_name',
                'Cisco-IOS-XR-ip-pfilter-oper', True),
            _MetaInfoClassMember('process', REFERENCE_CLASS, 'Process' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process', 
                [], [], 
                '''                Operational data for pfilter
                ''',
                'process',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa.Nodes' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node', 
                [], [], 
                '''                PfilterMa operational data for a particular
                node
                ''',
                'node',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa' : {
        'meta_info' : _MetaInfoClass('PfilterMa',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes', 
                [], [], 
                '''                Node-specific operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'pfilter-ma',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
}
_meta_table['PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos.InterfaceInfo']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable.InterfaceInfos']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv6.AclInfoTable']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process.Ipv6']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos.InterfaceInfo']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable.InterfaceInfos']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv4.AclInfoTable']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process.Ipv4']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv6']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv4']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node']['meta_info']
_meta_table['PfilterMa.Nodes.Node']['meta_info'].parent =_meta_table['PfilterMa.Nodes']['meta_info']
_meta_table['PfilterMa.Nodes']['meta_info'].parent =_meta_table['PfilterMa']['meta_info']
