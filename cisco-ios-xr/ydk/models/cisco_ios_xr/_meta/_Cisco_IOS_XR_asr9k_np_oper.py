


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad',
            False, 
            [
            _MetaInfoClassMember('avg-guar-rfd-usage', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average of garanteed RFD usage
                ''',
                'avg_guar_rfd_usage',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('avg-rfd-usage', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Average RFD Usage
                ''',
                'avg_rfd_usage',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('flow-ctr-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flow control counters
                ''',
                'flow_ctr_counter',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inerface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('peak-guar-rfd-usage', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peak of garanteed RFD usage
                ''',
                'peak_guar_rfd_usage',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('peak-rfd-usage', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peak RFD Usage
                ''',
                'peak_rfd_usage',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'np-chn-load',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad',
            False, 
            [
            _MetaInfoClassMember('np-chn-load', REFERENCE_LIST, 'NpChnLoad' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad', 
                [], [], 
                '''                Array of NP Channel load counters
                ''',
                'np_chn_load',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'chn-load',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib',
            False, 
            [
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'total_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-used-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of used vmr entries
                ''',
                'total_used_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-ifib',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos',
            False, 
            [
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'total_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-used-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of used vmr entries
                ''',
                'total_used_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-qos',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl',
            False, 
            [
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'total_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-used-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of used vmr entries
                ''',
                'total_used_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-acl',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon',
            False, 
            [
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'total_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-used-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of used vmr entries
                ''',
                'total_used_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-afmon',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi',
            False, 
            [
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'total_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-used-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of used vmr entries
                ''',
                'total_used_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-li',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr',
            False, 
            [
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'total_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-used-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of used vmr entries
                ''',
                'total_used_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-pbr',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry',
            False, 
            [
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'total_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-used-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of used vmr entries
                ''',
                'total_used_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'application-edpl-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2',
            False, 
            [
            _MetaInfoClassMember('app-id-acl', REFERENCE_CLASS, 'AppIdAcl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl', 
                [], [], 
                '''                app acl entry
                ''',
                'app_id_acl',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-afmon', REFERENCE_CLASS, 'AppIdAfmon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon', 
                [], [], 
                '''                app afmon entry
                ''',
                'app_id_afmon',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-ifib', REFERENCE_CLASS, 'AppIdIfib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib', 
                [], [], 
                '''                app IFIB entry
                ''',
                'app_id_ifib',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-li', REFERENCE_CLASS, 'AppIdLi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi', 
                [], [], 
                '''                app LI entry
                ''',
                'app_id_li',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-pbr', REFERENCE_CLASS, 'AppIdPbr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr', 
                [], [], 
                '''                app PBR entry
                ''',
                'app_id_pbr',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-qos', REFERENCE_CLASS, 'AppIdQos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos', 
                [], [], 
                '''                app qos entry
                ''',
                'app_id_qos',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('application-edpl-entry', REFERENCE_CLASS, 'ApplicationEdplEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry', 
                [], [], 
                '''                app EDPL entry
                ''',
                'application_edpl_entry',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('free-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                free entries
                ''',
                'free_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('max-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max entries
                ''',
                'max_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'tcam-lt-ods2',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib',
            False, 
            [
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'total_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-used-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of used vmr entries
                ''',
                'total_used_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-ifib',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos',
            False, 
            [
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'total_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-used-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of used vmr entries
                ''',
                'total_used_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-qos',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl',
            False, 
            [
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'total_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-used-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of used vmr entries
                ''',
                'total_used_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-acl',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon',
            False, 
            [
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'total_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-used-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of used vmr entries
                ''',
                'total_used_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-afmon',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi',
            False, 
            [
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'total_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-used-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of used vmr entries
                ''',
                'total_used_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-li',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr',
            False, 
            [
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'total_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-used-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of used vmr entries
                ''',
                'total_used_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-pbr',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry',
            False, 
            [
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'total_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('total-used-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                number of used vmr entries
                ''',
                'total_used_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'application-edpl-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8',
            False, 
            [
            _MetaInfoClassMember('app-id-acl', REFERENCE_CLASS, 'AppIdAcl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl', 
                [], [], 
                '''                app acl entry
                ''',
                'app_id_acl',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-afmon', REFERENCE_CLASS, 'AppIdAfmon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon', 
                [], [], 
                '''                app afmon entry
                ''',
                'app_id_afmon',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-ifib', REFERENCE_CLASS, 'AppIdIfib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib', 
                [], [], 
                '''                app IFIB entry
                ''',
                'app_id_ifib',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-li', REFERENCE_CLASS, 'AppIdLi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi', 
                [], [], 
                '''                app LI entry
                ''',
                'app_id_li',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-pbr', REFERENCE_CLASS, 'AppIdPbr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr', 
                [], [], 
                '''                app PBR entry
                ''',
                'app_id_pbr',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-qos', REFERENCE_CLASS, 'AppIdQos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos', 
                [], [], 
                '''                app qos entry
                ''',
                'app_id_qos',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('application-edpl-entry', REFERENCE_CLASS, 'ApplicationEdplEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry', 
                [], [], 
                '''                app EDPL entry
                ''',
                'application_edpl_entry',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('free-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                free entries
                ''',
                'free_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('max-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max entries
                ''',
                'max_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'tcam-lt-ods8',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2',
            False, 
            [
            _MetaInfoClassMember('free-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Free Entries
                ''',
                'free_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('partition-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PartitionID
                ''',
                'partition_id',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('valid-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Valid Entries
                ''',
                'valid_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'tcam-lt-l2',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo',
            False, 
            [
            _MetaInfoClassMember('tcam-lt-l2', REFERENCE_LIST, 'TcamLtL2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2', 
                [], [], 
                '''                Array of TCAM LT L2 partition summaries
                ''',
                'tcam_lt_l2',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('tcam-lt-ods2', REFERENCE_CLASS, 'TcamLtOds2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2', 
                [], [], 
                '''                TCAM LT ODS 2 summary
                ''',
                'tcam_lt_ods2',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('tcam-lt-ods8', REFERENCE_CLASS, 'TcamLtOds8' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8', 
                [], [], 
                '''                TCAM LT_ODS 8 summary
                ''',
                'tcam_lt_ods8',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'internal-tcam-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon',
            False, 
            [
            _MetaInfoClassMember('allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('free-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Free entries in the table
                ''',
                'free_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'acl-common',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib',
            False, 
            [
            _MetaInfoClassMember('num-active-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_active_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-ifib',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos',
            False, 
            [
            _MetaInfoClassMember('num-active-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_active_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-qos',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl',
            False, 
            [
            _MetaInfoClassMember('num-active-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_active_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-acl',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon',
            False, 
            [
            _MetaInfoClassMember('num-active-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_active_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-afmon',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi',
            False, 
            [
            _MetaInfoClassMember('num-active-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_active_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-li',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr',
            False, 
            [
            _MetaInfoClassMember('num-active-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_active_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-pbr',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl',
            False, 
            [
            _MetaInfoClassMember('num-active-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_active_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-edpl',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2',
            False, 
            [
            _MetaInfoClassMember('acl-common', REFERENCE_CLASS, 'AclCommon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon', 
                [], [], 
                '''                ACL common region
                ''',
                'acl_common',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-acl', REFERENCE_CLASS, 'AppIdAcl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl', 
                [], [], 
                '''                app acl entry
                ''',
                'app_id_acl',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-afmon', REFERENCE_CLASS, 'AppIdAfmon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon', 
                [], [], 
                '''                app afmon entry
                ''',
                'app_id_afmon',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-edpl', REFERENCE_CLASS, 'AppIdEdpl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl', 
                [], [], 
                '''                app EDPL entry
                ''',
                'app_id_edpl',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-ifib', REFERENCE_CLASS, 'AppIdIfib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib', 
                [], [], 
                '''                app IFIB entry
                ''',
                'app_id_ifib',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-li', REFERENCE_CLASS, 'AppIdLi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi', 
                [], [], 
                '''                app LI entry
                ''',
                'app_id_li',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-pbr', REFERENCE_CLASS, 'AppIdPbr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr', 
                [], [], 
                '''                app PBR entry
                ''',
                'app_id_pbr',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-qos', REFERENCE_CLASS, 'AppIdQos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos', 
                [], [], 
                '''                app qos entry
                ''',
                'app_id_qos',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('free-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Free entries in the table
                ''',
                'free_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('reserved-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'reserved_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'tcam-lt-ods2',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon',
            False, 
            [
            _MetaInfoClassMember('allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('free-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Free entries in the table
                ''',
                'free_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'acl-common',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib',
            False, 
            [
            _MetaInfoClassMember('num-active-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_active_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-ifib',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos',
            False, 
            [
            _MetaInfoClassMember('num-active-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_active_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-qos',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl',
            False, 
            [
            _MetaInfoClassMember('num-active-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_active_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-acl',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon',
            False, 
            [
            _MetaInfoClassMember('num-active-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_active_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-afmon',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi',
            False, 
            [
            _MetaInfoClassMember('num-active-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_active_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-li',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr',
            False, 
            [
            _MetaInfoClassMember('num-active-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_active_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-pbr',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl',
            False, 
            [
            _MetaInfoClassMember('num-active-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_active_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-allocated-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'num_allocated_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('num-vmr-ids', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Vmr IDs
                ''',
                'num_vmr_ids',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'app-id-edpl',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8',
            False, 
            [
            _MetaInfoClassMember('acl-common', REFERENCE_CLASS, 'AclCommon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon', 
                [], [], 
                '''                ACL common region
                ''',
                'acl_common',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-acl', REFERENCE_CLASS, 'AppIdAcl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl', 
                [], [], 
                '''                app acl entry
                ''',
                'app_id_acl',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-afmon', REFERENCE_CLASS, 'AppIdAfmon' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon', 
                [], [], 
                '''                app afmon entry
                ''',
                'app_id_afmon',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-edpl', REFERENCE_CLASS, 'AppIdEdpl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl', 
                [], [], 
                '''                app EDPL entry
                ''',
                'app_id_edpl',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-ifib', REFERENCE_CLASS, 'AppIdIfib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib', 
                [], [], 
                '''                app IFIB entry
                ''',
                'app_id_ifib',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-li', REFERENCE_CLASS, 'AppIdLi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi', 
                [], [], 
                '''                app LI entry
                ''',
                'app_id_li',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-pbr', REFERENCE_CLASS, 'AppIdPbr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr', 
                [], [], 
                '''                app PBR entry
                ''',
                'app_id_pbr',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('app-id-qos', REFERENCE_CLASS, 'AppIdQos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos', 
                [], [], 
                '''                app qos entry
                ''',
                'app_id_qos',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('free-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Free entries in the table
                ''',
                'free_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('reserved-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of active vmr entries
                ''',
                'reserved_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'tcam-lt-ods8',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2',
            False, 
            [
            _MetaInfoClassMember('free-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Free Entries
                ''',
                'free_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('partition-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PartitionID
                ''',
                'partition_id',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Priority
                ''',
                'priority',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('valid-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Valid Entries
                ''',
                'valid_entries',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'tcam-lt-l2',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo',
            False, 
            [
            _MetaInfoClassMember('tcam-lt-l2', REFERENCE_LIST, 'TcamLtL2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2', 
                [], [], 
                '''                Array of TCAM L2 partition summaries
                ''',
                'tcam_lt_l2',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('tcam-lt-ods2', REFERENCE_CLASS, 'TcamLtOds2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2', 
                [], [], 
                '''                TCAM ODS2 partition summary
                ''',
                'tcam_lt_ods2',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('tcam-lt-ods8', REFERENCE_CLASS, 'TcamLtOds8' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8', 
                [], [], 
                '''                TCAM ODS8 partition summary
                ''',
                'tcam_lt_ods8',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'tcam-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary',
            False, 
            [
            _MetaInfoClassMember('internal-tcam-info', REFERENCE_CLASS, 'InternalTcamInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo', 
                [], [], 
                '''                Internal tcam summary info
                ''',
                'internal_tcam_info',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('tcam-info', REFERENCE_CLASS, 'TcamInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo', 
                [], [], 
                '''                External tcam summary info
                ''',
                'tcam_info',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'tcam-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter',
            False, 
            [
            _MetaInfoClassMember('counter-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Counter Index
                ''',
                'counter_index',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('counter-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Counter name
                ''',
                'counter_name',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('counter-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Counter TypeDROP: Drop counterPUNT: Punt
                counterFWD:  Forward or generic counterUNKNOWN:
                Counter type unknown
                ''',
                'counter_type',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('counter-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The accurate value of the counter
                ''',
                'counter_value',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Rate in Packets Per Second
                ''',
                'rate',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'np-counter',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.Counters' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.Counters',
            False, 
            [
            _MetaInfoClassMember('np-counter', REFERENCE_LIST, 'NpCounter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter', 
                [], [], 
                '''                Array of NP Counters
                ''',
                'np_counter',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'counters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop',
            False, 
            [
            _MetaInfoClassMember('counter-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The Value of the counter
                ''',
                'counter_value',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'np-fast-drop',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop',
            False, 
            [
            _MetaInfoClassMember('np-fast-drop', REFERENCE_LIST, 'NpFastDrop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop', 
                [], [], 
                '''                Array of NP Fast Drop Counters
                ''',
                'np_fast_drop',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'fast-drop',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps.Np' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps.Np',
            False, 
            [
            _MetaInfoClassMember('np-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(np0)|(np1)|(np2)|(np3)|(np4)|(np5)|(np6)|(np7)'], 
                '''                NP name
                ''',
                'np_name',
                'Cisco-IOS-XR-asr9k-np-oper', True),
            _MetaInfoClassMember('chn-load', REFERENCE_CLASS, 'ChnLoad' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad', 
                [], [], 
                '''                prm channel load info
                ''',
                'chn_load',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('counters', REFERENCE_CLASS, 'Counters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.Counters', 
                [], [], 
                '''                prm counters info
                ''',
                'counters',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('fast-drop', REFERENCE_CLASS, 'FastDrop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop', 
                [], [], 
                '''                prm fast drop counters info
                ''',
                'fast_drop',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            _MetaInfoClassMember('tcam-summary', REFERENCE_CLASS, 'TcamSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary', 
                [], [], 
                '''                prm tcam summary info
                ''',
                'tcam_summary',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'np',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node.Nps' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node.Nps',
            False, 
            [
            _MetaInfoClassMember('np', REFERENCE_LIST, 'Np' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps.Np', 
                [], [], 
                '''                np0 to np7
                ''',
                'np',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'nps',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                node number
                ''',
                'node_name',
                'Cisco-IOS-XR-asr9k-np-oper', True),
            _MetaInfoClassMember('nps', REFERENCE_CLASS, 'Nps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node.Nps', 
                [], [], 
                '''                List of all NP
                ''',
                'nps',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp.Nodes' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes.Node', 
                [], [], 
                '''                Number
                ''',
                'node',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
    'HardwareModuleNp' : {
        'meta_info' : _MetaInfoClass('HardwareModuleNp',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper', 'HardwareModuleNp.Nodes', 
                [], [], 
                '''                Table of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-asr9k-np-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-np-oper',
            'hardware-module-np',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-np-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_np_oper'
        ),
    },
}
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad.NpChnLoad']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdIfib']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdQos']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAcl']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdAfmon']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdLi']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.AppIdPbr']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2.ApplicationEdplEntry']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdIfib']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdQos']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAcl']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdAfmon']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdLi']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.AppIdPbr']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8.ApplicationEdplEntry']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds2']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtOds8']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo.TcamLtL2']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AclCommon']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdIfib']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdQos']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAcl']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdAfmon']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdLi']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdPbr']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2.AppIdEdpl']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AclCommon']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdIfib']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdQos']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAcl']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdAfmon']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdLi']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdPbr']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8.AppIdEdpl']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds2']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtOds8']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo.TcamLtL2']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.InternalTcamInfo']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary.TcamInfo']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.Counters.NpCounter']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.Counters']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop.NpFastDrop']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.ChnLoad']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.TcamSummary']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.Counters']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np.FastDrop']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps.Np']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node.Nps']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node.Nps']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes.Node']['meta_info']
_meta_table['HardwareModuleNp.Nodes.Node']['meta_info'].parent =_meta_table['HardwareModuleNp.Nodes']['meta_info']
_meta_table['HardwareModuleNp.Nodes']['meta_info'].parent =_meta_table['HardwareModuleNp']['meta_info']
