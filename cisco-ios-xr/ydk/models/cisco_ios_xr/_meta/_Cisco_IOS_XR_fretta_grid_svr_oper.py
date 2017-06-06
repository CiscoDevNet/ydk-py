


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Grid.Nodes.Node.ClientXr.Client.ClientData' : {
        'meta_info' : _MetaInfoClass('Grid.Nodes.Node.ClientXr.Client.ClientData',
            False, 
            [
            _MetaInfoClassMember('res-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Resource ID
                ''',
                'res_id',
                'Cisco-IOS-XR-fretta-grid-svr-oper', False),
            ],
            'Cisco-IOS-XR-fretta-grid-svr-oper',
            'client-data',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-grid-svr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper'
        ),
    },
    'Grid.Nodes.Node.ClientXr.Client' : {
        'meta_info' : _MetaInfoClass('Grid.Nodes.Node.ClientXr.Client',
            False, 
            [
            _MetaInfoClassMember('client-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Client name
                ''',
                'client_name',
                'Cisco-IOS-XR-fretta-grid-svr-oper', True),
            _MetaInfoClassMember('client-data', REFERENCE_LIST, 'ClientData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper', 'Grid.Nodes.Node.ClientXr.Client.ClientData', 
                [], [], 
                '''                Client information
                ''',
                'client_data',
                'Cisco-IOS-XR-fretta-grid-svr-oper', False),
            ],
            'Cisco-IOS-XR-fretta-grid-svr-oper',
            'client',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-grid-svr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper'
        ),
    },
    'Grid.Nodes.Node.ClientXr' : {
        'meta_info' : _MetaInfoClass('Grid.Nodes.Node.ClientXr',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_LIST, 'Client' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper', 'Grid.Nodes.Node.ClientXr.Client', 
                [], [], 
                '''                GRID Client Database
                ''',
                'client',
                'Cisco-IOS-XR-fretta-grid-svr-oper', False),
            ],
            'Cisco-IOS-XR-fretta-grid-svr-oper',
            'client-xr',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-grid-svr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper'
        ),
    },
    'Grid.Nodes.Node.Clients.Client.ClientData' : {
        'meta_info' : _MetaInfoClass('Grid.Nodes.Node.Clients.Client.ClientData',
            False, 
            [
            _MetaInfoClassMember('res-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Resource ID
                ''',
                'res_id',
                'Cisco-IOS-XR-fretta-grid-svr-oper', False),
            ],
            'Cisco-IOS-XR-fretta-grid-svr-oper',
            'client-data',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-grid-svr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper'
        ),
    },
    'Grid.Nodes.Node.Clients.Client' : {
        'meta_info' : _MetaInfoClass('Grid.Nodes.Node.Clients.Client',
            False, 
            [
            _MetaInfoClassMember('client-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Client name
                ''',
                'client_name',
                'Cisco-IOS-XR-fretta-grid-svr-oper', True),
            _MetaInfoClassMember('client-data', REFERENCE_LIST, 'ClientData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper', 'Grid.Nodes.Node.Clients.Client.ClientData', 
                [], [], 
                '''                Client information
                ''',
                'client_data',
                'Cisco-IOS-XR-fretta-grid-svr-oper', False),
            ],
            'Cisco-IOS-XR-fretta-grid-svr-oper',
            'client',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-grid-svr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper'
        ),
    },
    'Grid.Nodes.Node.Clients' : {
        'meta_info' : _MetaInfoClass('Grid.Nodes.Node.Clients',
            False, 
            [
            _MetaInfoClassMember('client', REFERENCE_LIST, 'Client' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper', 'Grid.Nodes.Node.Clients.Client', 
                [], [], 
                '''                GRID Client Consistency Check
                ''',
                'client',
                'Cisco-IOS-XR-fretta-grid-svr-oper', False),
            ],
            'Cisco-IOS-XR-fretta-grid-svr-oper',
            'clients',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-grid-svr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper'
        ),
    },
    'Grid.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Grid.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_name',
                'Cisco-IOS-XR-fretta-grid-svr-oper', True),
            _MetaInfoClassMember('client-xr', REFERENCE_CLASS, 'ClientXr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper', 'Grid.Nodes.Node.ClientXr', 
                [], [], 
                '''                GRID Client Table
                ''',
                'client_xr',
                'Cisco-IOS-XR-fretta-grid-svr-oper', False),
            _MetaInfoClassMember('clients', REFERENCE_CLASS, 'Clients' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper', 'Grid.Nodes.Node.Clients', 
                [], [], 
                '''                GRID Client Consistency Check
                ''',
                'clients',
                'Cisco-IOS-XR-fretta-grid-svr-oper', False),
            ],
            'Cisco-IOS-XR-fretta-grid-svr-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-grid-svr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper'
        ),
    },
    'Grid.Nodes' : {
        'meta_info' : _MetaInfoClass('Grid.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper', 'Grid.Nodes.Node', 
                [], [], 
                '''                Operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-fretta-grid-svr-oper', False),
            ],
            'Cisco-IOS-XR-fretta-grid-svr-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-grid-svr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper'
        ),
    },
    'Grid' : {
        'meta_info' : _MetaInfoClass('Grid',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper', 'Grid.Nodes', 
                [], [], 
                '''                Table of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-fretta-grid-svr-oper', False),
            ],
            'Cisco-IOS-XR-fretta-grid-svr-oper',
            'grid',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-grid-svr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_grid_svr_oper'
        ),
    },
}
_meta_table['Grid.Nodes.Node.ClientXr.Client.ClientData']['meta_info'].parent =_meta_table['Grid.Nodes.Node.ClientXr.Client']['meta_info']
_meta_table['Grid.Nodes.Node.ClientXr.Client']['meta_info'].parent =_meta_table['Grid.Nodes.Node.ClientXr']['meta_info']
_meta_table['Grid.Nodes.Node.Clients.Client.ClientData']['meta_info'].parent =_meta_table['Grid.Nodes.Node.Clients.Client']['meta_info']
_meta_table['Grid.Nodes.Node.Clients.Client']['meta_info'].parent =_meta_table['Grid.Nodes.Node.Clients']['meta_info']
_meta_table['Grid.Nodes.Node.ClientXr']['meta_info'].parent =_meta_table['Grid.Nodes.Node']['meta_info']
_meta_table['Grid.Nodes.Node.Clients']['meta_info'].parent =_meta_table['Grid.Nodes.Node']['meta_info']
_meta_table['Grid.Nodes.Node']['meta_info'].parent =_meta_table['Grid.Nodes']['meta_info']
_meta_table['Grid.Nodes']['meta_info'].parent =_meta_table['Grid']['meta_info']
