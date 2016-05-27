


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'PfilterMa.Nodes.Node.Process.Ipv6.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv6.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-pfilter-oper', True),
            _MetaInfoClassMember('acl-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface ACL Details
                ''',
                'acl_information',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv6.Interfaces' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv6.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv6.Interfaces.Interface', 
                [], [], 
                '''                Operational data for pfilter
                ''',
                'interface',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv6' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv6',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv6.Interfaces', 
                [], [], 
                '''                Operational data for pfilter
                ''',
                'interfaces',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv4.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv4.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ip-pfilter-oper', True),
            _MetaInfoClassMember('acl-information', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface ACL Details
                ''',
                'acl_information',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv4.Interfaces' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv4.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv4.Interfaces.Interface', 
                [], [], 
                '''                Operational data for pfilter
                ''',
                'interface',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa.Nodes.Node.Process.Ipv4' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process.Ipv4',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv4.Interfaces', 
                [], [], 
                '''                Operational data for pfilter
                ''',
                'interfaces',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa.Nodes.Node.Process' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node.Process',
            False, 
            [
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv6', 
                [], [], 
                '''                Operational data for pfilter
                ''',
                'ipv6',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process.Ipv4', 
                [], [], 
                '''                Operational data for pfilter
                ''',
                'ipv4',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'process',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node
                ''',
                'node_name',
                'Cisco-IOS-XR-ip-pfilter-oper', True),
            _MetaInfoClassMember('process', REFERENCE_CLASS, 'Process' , 'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node.Process', 
                [], [], 
                '''                Operational data for pfilter
                ''',
                'process',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa.Nodes' : {
        'meta_info' : _MetaInfoClass('PfilterMa.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes.Node', 
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
        'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
    'PfilterMa' : {
        'meta_info' : _MetaInfoClass('PfilterMa',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper', 'PfilterMa.Nodes', 
                [], [], 
                '''                Node-specific operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-ip-pfilter-oper', False),
            ],
            'Cisco-IOS-XR-ip-pfilter-oper',
            'pfilter-ma',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-pfilter-oper'],
        'ydk.models.ip.Cisco_IOS_XR_ip_pfilter_oper'
        ),
    },
}
_meta_table['PfilterMa.Nodes.Node.Process.Ipv6.Interfaces.Interface']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process.Ipv6.Interfaces']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv6.Interfaces']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process.Ipv6']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv4.Interfaces.Interface']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process.Ipv4.Interfaces']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv4.Interfaces']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process.Ipv4']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv6']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process.Ipv4']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node.Process']['meta_info']
_meta_table['PfilterMa.Nodes.Node.Process']['meta_info'].parent =_meta_table['PfilterMa.Nodes.Node']['meta_info']
_meta_table['PfilterMa.Nodes.Node']['meta_info'].parent =_meta_table['PfilterMa.Nodes']['meta_info']
_meta_table['PfilterMa.Nodes']['meta_info'].parent =_meta_table['PfilterMa']['meta_info']
