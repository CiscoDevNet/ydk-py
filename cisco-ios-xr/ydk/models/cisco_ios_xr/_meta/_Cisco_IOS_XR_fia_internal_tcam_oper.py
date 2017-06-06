


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank.BankDb' : {
        'meta_info' : _MetaInfoClass('Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank.BankDb',
            False, 
            [
            _MetaInfoClassMember('db-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                db id
                ''',
                'db_id',
                'Cisco-IOS-XR-fia-internal-tcam-oper', False),
            _MetaInfoClassMember('db-inuse-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                db inuse entries
                ''',
                'db_inuse_entries',
                'Cisco-IOS-XR-fia-internal-tcam-oper', False),
            _MetaInfoClassMember('db-prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                db prefix
                ''',
                'db_prefix',
                'Cisco-IOS-XR-fia-internal-tcam-oper', False),
            ],
            'Cisco-IOS-XR-fia-internal-tcam-oper',
            'bank-db',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-internal-tcam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper'
        ),
    },
    'Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank' : {
        'meta_info' : _MetaInfoClass('Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank',
            False, 
            [
            _MetaInfoClassMember('bank-db', REFERENCE_LIST, 'BankDb' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper', 'Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank.BankDb', 
                [], [], 
                '''                bank db
                ''',
                'bank_db',
                'Cisco-IOS-XR-fia-internal-tcam-oper', False),
            _MetaInfoClassMember('bank-free-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                bank free entries
                ''',
                'bank_free_entries',
                'Cisco-IOS-XR-fia-internal-tcam-oper', False),
            _MetaInfoClassMember('bank-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                bank id
                ''',
                'bank_id',
                'Cisco-IOS-XR-fia-internal-tcam-oper', False),
            _MetaInfoClassMember('bank-inuse-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                bank inuse entries
                ''',
                'bank_inuse_entries',
                'Cisco-IOS-XR-fia-internal-tcam-oper', False),
            _MetaInfoClassMember('bank-key-size', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                bank key size
                ''',
                'bank_key_size',
                'Cisco-IOS-XR-fia-internal-tcam-oper', False),
            _MetaInfoClassMember('nof-dbs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                nof dbs
                ''',
                'nof_dbs',
                'Cisco-IOS-XR-fia-internal-tcam-oper', False),
            _MetaInfoClassMember('owner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                owner
                ''',
                'owner',
                'Cisco-IOS-XR-fia-internal-tcam-oper', False),
            ],
            'Cisco-IOS-XR-fia-internal-tcam-oper',
            'tcam-bank',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-internal-tcam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper'
        ),
    },
    'Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam' : {
        'meta_info' : _MetaInfoClass('Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam',
            False, 
            [
            _MetaInfoClassMember('npu-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                npu id
                ''',
                'npu_id',
                'Cisco-IOS-XR-fia-internal-tcam-oper', False),
            _MetaInfoClassMember('tcam-bank', REFERENCE_LIST, 'TcamBank' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper', 'Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank', 
                [], [], 
                '''                tcam bank
                ''',
                'tcam_bank',
                'Cisco-IOS-XR-fia-internal-tcam-oper', False),
            ],
            'Cisco-IOS-XR-fia-internal-tcam-oper',
            'npu-tcam',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-internal-tcam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper'
        ),
    },
    'Controller.Dpa.Nodes.Node.InternalTcamResources' : {
        'meta_info' : _MetaInfoClass('Controller.Dpa.Nodes.Node.InternalTcamResources',
            False, 
            [
            _MetaInfoClassMember('npu-tcam', REFERENCE_LIST, 'NpuTcam' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper', 'Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam', 
                [], [], 
                '''                npu tcam
                ''',
                'npu_tcam',
                'Cisco-IOS-XR-fia-internal-tcam-oper', False),
            ],
            'Cisco-IOS-XR-fia-internal-tcam-oper',
            'internal-tcam-resources',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-internal-tcam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper'
        ),
    },
    'Controller.Dpa.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Controller.Dpa.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_name',
                'Cisco-IOS-XR-fia-internal-tcam-oper', True),
            _MetaInfoClassMember('internal-tcam-resources', REFERENCE_CLASS, 'InternalTcamResources' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper', 'Controller.Dpa.Nodes.Node.InternalTcamResources', 
                [], [], 
                '''                Internal TCAM Resource Information
                ''',
                'internal_tcam_resources',
                'Cisco-IOS-XR-fia-internal-tcam-oper', False),
            ],
            'Cisco-IOS-XR-fia-internal-tcam-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-internal-tcam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper'
        ),
    },
    'Controller.Dpa.Nodes' : {
        'meta_info' : _MetaInfoClass('Controller.Dpa.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper', 'Controller.Dpa.Nodes.Node', 
                [], [], 
                '''                DPA operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-fia-internal-tcam-oper', False),
            ],
            'Cisco-IOS-XR-fia-internal-tcam-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-internal-tcam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper'
        ),
    },
    'Controller.Dpa' : {
        'meta_info' : _MetaInfoClass('Controller.Dpa',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper', 'Controller.Dpa.Nodes', 
                [], [], 
                '''                DPA data for available nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-fia-internal-tcam-oper', False),
            ],
            'Cisco-IOS-XR-fia-internal-tcam-oper',
            'dpa',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-internal-tcam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper'
        ),
    },
    'Controller' : {
        'meta_info' : _MetaInfoClass('Controller',
            False, 
            [
            _MetaInfoClassMember('dpa', REFERENCE_CLASS, 'Dpa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper', 'Controller.Dpa', 
                [], [], 
                '''                Controller DPA operational data
                ''',
                'dpa',
                'Cisco-IOS-XR-fia-internal-tcam-oper', False),
            ],
            'Cisco-IOS-XR-fia-internal-tcam-oper',
            'controller',
            _yang_ns._namespaces['Cisco-IOS-XR-fia-internal-tcam-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fia_internal_tcam_oper'
        ),
    },
}
_meta_table['Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank.BankDb']['meta_info'].parent =_meta_table['Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank']['meta_info']
_meta_table['Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam.TcamBank']['meta_info'].parent =_meta_table['Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam']['meta_info']
_meta_table['Controller.Dpa.Nodes.Node.InternalTcamResources.NpuTcam']['meta_info'].parent =_meta_table['Controller.Dpa.Nodes.Node.InternalTcamResources']['meta_info']
_meta_table['Controller.Dpa.Nodes.Node.InternalTcamResources']['meta_info'].parent =_meta_table['Controller.Dpa.Nodes.Node']['meta_info']
_meta_table['Controller.Dpa.Nodes.Node']['meta_info'].parent =_meta_table['Controller.Dpa.Nodes']['meta_info']
_meta_table['Controller.Dpa.Nodes']['meta_info'].parent =_meta_table['Controller.Dpa']['meta_info']
_meta_table['Controller.Dpa']['meta_info'].parent =_meta_table['Controller']['meta_info']
