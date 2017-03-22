


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'HwModuleSliceStatusEnum' : _MetaInfoEnum('HwModuleSliceStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper',
        {
            'not-provisioned':'not_provisioned',
            'provisioning-in-progress':'provisioning_in_progress',
            'provisioned':'provisioned',
            'provisioning-failed':'provisioning_failed',
            'provisioning-scheduled':'provisioning_scheduled',
            'reprovisioning-aborted':'reprovisioning_aborted',
        }, 'Cisco-IOS-XR-ncs1k-mxp-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-oper']),
    'HwModule.SliceIds.SliceId.SliceInfo.ClientPort.TrunkPort' : {
        'meta_info' : _MetaInfoClass('HwModule.SliceIds.SliceId.SliceInfo.ClientPort.TrunkPort',
            False, 
            [
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IfIndex
                ''',
                'if_index',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('percentage', ATTRIBUTE, 'str' , None, None, 
                [(0, 8)], [], 
                '''                Percentage
                ''',
                'percentage',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('trunk-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                TrunkName
                ''',
                'trunk_name',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-oper',
            'trunk-port',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper'
        ),
    },
    'HwModule.SliceIds.SliceId.SliceInfo.ClientPort' : {
        'meta_info' : _MetaInfoClass('HwModule.SliceIds.SliceId.SliceInfo.ClientPort',
            False, 
            [
            _MetaInfoClassMember('client-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                ClientName
                ''',
                'client_name',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IfIndex
                ''',
                'if_index',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('trunk-port', REFERENCE_LIST, 'TrunkPort' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper', 'HwModule.SliceIds.SliceId.SliceInfo.ClientPort.TrunkPort', 
                [], [], 
                '''                trunk port
                ''',
                'trunk_port',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-oper',
            'client-port',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper'
        ),
    },
    'HwModule.SliceIds.SliceId.SliceInfo' : {
        'meta_info' : _MetaInfoClass('HwModule.SliceIds.SliceId.SliceInfo',
            False, 
            [
            _MetaInfoClassMember('client-port', REFERENCE_LIST, 'ClientPort' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper', 'HwModule.SliceIds.SliceId.SliceInfo.ClientPort', 
                [], [], 
                '''                client port
                ''',
                'client_port',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('client-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ClientRate
                ''',
                'client_rate',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('dp-fpga-fw-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 10)], [], 
                '''                DpFpgaFwType
                ''',
                'dp_fpga_fw_type',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('dp-fpga-fw-ver', ATTRIBUTE, 'str' , None, None, 
                [(0, 10)], [], 
                '''                DpFpgaFwVer
                ''',
                'dp_fpga_fw_ver',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('encryption-supported', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                EncryptionSupported
                ''',
                'encryption_supported',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('hardware-status', REFERENCE_ENUM_CLASS, 'HwModuleSliceStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper', 'HwModuleSliceStatusEnum', 
                [], [], 
                '''                HardwareStatus
                ''',
                'hardware_status',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('lldp-drop-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LldpDropStatus
                ''',
                'lldp_drop_status',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('need-upg', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                NeedUpg
                ''',
                'need_upg',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('slice-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SliceId
                ''',
                'slice_id',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('trunk-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TrunkRate
                ''',
                'trunk_rate',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-oper',
            'slice-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper'
        ),
    },
    'HwModule.SliceIds.SliceId' : {
        'meta_info' : _MetaInfoClass('HwModule.SliceIds.SliceId',
            False, 
            [
            _MetaInfoClassMember('slice-num', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Details associated with a particular slice
                number
                ''',
                'slice_num',
                'Cisco-IOS-XR-ncs1k-mxp-oper', True),
            _MetaInfoClassMember('slice-info', REFERENCE_LIST, 'SliceInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper', 'HwModule.SliceIds.SliceId.SliceInfo', 
                [], [], 
                '''                slice info
                ''',
                'slice_info',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-oper',
            'slice-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper'
        ),
    },
    'HwModule.SliceIds' : {
        'meta_info' : _MetaInfoClass('HwModule.SliceIds',
            False, 
            [
            _MetaInfoClassMember('slice-id', REFERENCE_LIST, 'SliceId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper', 'HwModule.SliceIds.SliceId', 
                [], [], 
                '''                Per slice num data
                ''',
                'slice_id',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-oper',
            'slice-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper'
        ),
    },
    'HwModule.SliceAll.SliceInfo.ClientPort.TrunkPort' : {
        'meta_info' : _MetaInfoClass('HwModule.SliceAll.SliceInfo.ClientPort.TrunkPort',
            False, 
            [
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IfIndex
                ''',
                'if_index',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('percentage', ATTRIBUTE, 'str' , None, None, 
                [(0, 8)], [], 
                '''                Percentage
                ''',
                'percentage',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('trunk-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                TrunkName
                ''',
                'trunk_name',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-oper',
            'trunk-port',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper'
        ),
    },
    'HwModule.SliceAll.SliceInfo.ClientPort' : {
        'meta_info' : _MetaInfoClass('HwModule.SliceAll.SliceInfo.ClientPort',
            False, 
            [
            _MetaInfoClassMember('client-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                ClientName
                ''',
                'client_name',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IfIndex
                ''',
                'if_index',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('trunk-port', REFERENCE_LIST, 'TrunkPort' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper', 'HwModule.SliceAll.SliceInfo.ClientPort.TrunkPort', 
                [], [], 
                '''                trunk port
                ''',
                'trunk_port',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-oper',
            'client-port',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper'
        ),
    },
    'HwModule.SliceAll.SliceInfo' : {
        'meta_info' : _MetaInfoClass('HwModule.SliceAll.SliceInfo',
            False, 
            [
            _MetaInfoClassMember('client-port', REFERENCE_LIST, 'ClientPort' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper', 'HwModule.SliceAll.SliceInfo.ClientPort', 
                [], [], 
                '''                client port
                ''',
                'client_port',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('client-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ClientRate
                ''',
                'client_rate',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('dp-fpga-fw-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 10)], [], 
                '''                DpFpgaFwType
                ''',
                'dp_fpga_fw_type',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('dp-fpga-fw-ver', ATTRIBUTE, 'str' , None, None, 
                [(0, 10)], [], 
                '''                DpFpgaFwVer
                ''',
                'dp_fpga_fw_ver',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('encryption-supported', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                EncryptionSupported
                ''',
                'encryption_supported',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('hardware-status', REFERENCE_ENUM_CLASS, 'HwModuleSliceStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper', 'HwModuleSliceStatusEnum', 
                [], [], 
                '''                HardwareStatus
                ''',
                'hardware_status',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('lldp-drop-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LldpDropStatus
                ''',
                'lldp_drop_status',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('need-upg', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                NeedUpg
                ''',
                'need_upg',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('slice-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SliceId
                ''',
                'slice_id',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('trunk-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TrunkRate
                ''',
                'trunk_rate',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-oper',
            'slice-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper'
        ),
    },
    'HwModule.SliceAll' : {
        'meta_info' : _MetaInfoClass('HwModule.SliceAll',
            False, 
            [
            _MetaInfoClassMember('slice-info', REFERENCE_LIST, 'SliceInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper', 'HwModule.SliceAll.SliceInfo', 
                [], [], 
                '''                slice info
                ''',
                'slice_info',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-oper',
            'slice-all',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper'
        ),
    },
    'HwModule' : {
        'meta_info' : _MetaInfoClass('HwModule',
            False, 
            [
            _MetaInfoClassMember('slice-all', REFERENCE_CLASS, 'SliceAll' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper', 'HwModule.SliceAll', 
                [], [], 
                '''                Information for all slices
                ''',
                'slice_all',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            _MetaInfoClassMember('slice-ids', REFERENCE_CLASS, 'SliceIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper', 'HwModule.SliceIds', 
                [], [], 
                '''                Slice information
                ''',
                'slice_ids',
                'Cisco-IOS-XR-ncs1k-mxp-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-oper',
            'hw-module',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_oper'
        ),
    },
}
_meta_table['HwModule.SliceIds.SliceId.SliceInfo.ClientPort.TrunkPort']['meta_info'].parent =_meta_table['HwModule.SliceIds.SliceId.SliceInfo.ClientPort']['meta_info']
_meta_table['HwModule.SliceIds.SliceId.SliceInfo.ClientPort']['meta_info'].parent =_meta_table['HwModule.SliceIds.SliceId.SliceInfo']['meta_info']
_meta_table['HwModule.SliceIds.SliceId.SliceInfo']['meta_info'].parent =_meta_table['HwModule.SliceIds.SliceId']['meta_info']
_meta_table['HwModule.SliceIds.SliceId']['meta_info'].parent =_meta_table['HwModule.SliceIds']['meta_info']
_meta_table['HwModule.SliceAll.SliceInfo.ClientPort.TrunkPort']['meta_info'].parent =_meta_table['HwModule.SliceAll.SliceInfo.ClientPort']['meta_info']
_meta_table['HwModule.SliceAll.SliceInfo.ClientPort']['meta_info'].parent =_meta_table['HwModule.SliceAll.SliceInfo']['meta_info']
_meta_table['HwModule.SliceAll.SliceInfo']['meta_info'].parent =_meta_table['HwModule.SliceAll']['meta_info']
_meta_table['HwModule.SliceIds']['meta_info'].parent =_meta_table['HwModule']['meta_info']
_meta_table['HwModule.SliceAll']['meta_info'].parent =_meta_table['HwModule']['meta_info']
