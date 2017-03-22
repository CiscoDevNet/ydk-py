


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Grpc.Statistics' : {
        'meta_info' : _MetaInfoClass('Grpc.Statistics',
            False, 
            [
            _MetaInfoClassMember('address-family', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AddressFamily
                ''',
                'address_family',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-cli-config-req-recv', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterCliConfigReqRecv
                ''',
                'ct_cli_config_req_recv',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-cli-config-res-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterCliConfigResSent
                ''',
                'ct_cli_config_res_sent',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-commit-replace-req-recv', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterCommitReplaceReq
                ''',
                'ct_commit_replace_req_recv',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-commit-replace-res-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterCommitReplaceRes
                ''',
                'ct_commit_replace_res_sent',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-delete-config-req-recv', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterDeleteConfigReq
                ''',
                'ct_delete_config_req_recv',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-delete-config-res-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterDeleteConfigRes
                ''',
                'ct_delete_config_res_sent',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-get-config-req-recv', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterGetConfigReqRecv
                ''',
                'ct_get_config_req_recv',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-get-config-res-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterGetConfigResSent
                ''',
                'ct_get_config_res_sent',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-get-current-session', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CounterGetCurrentSession
                ''',
                'ct_get_current_session',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-get-oper-req-recv', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterGetOperReqRecv
                ''',
                'ct_get_oper_req_recv',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-get-oper-res-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterGetOperResSent
                ''',
                'ct_get_oper_res_sent',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-merge-config-req-recv', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterMergeConfigReq
                ''',
                'ct_merge_config_req_recv',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-merge-config-res-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterMergeConfigRes
                ''',
                'ct_merge_config_res_sent',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-replace-config-req-recv', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterReplaceConfigReq
                ''',
                'ct_replace_config_req_recv',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-replace-config-res-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterReplaceConfigSent
                ''',
                'ct_replace_config_res_sent',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-show-cmd-txt-req-recv', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterShowCmdTxtReqRecv
                ''',
                'ct_show_cmd_txt_req_recv',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-show-cmd-txt-res-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterShowCmdTxtResSent
                ''',
                'ct_show_cmd_txt_res_sent',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('listening-port', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ListeningPort
                ''',
                'listening_port',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('max-req-per-user', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MaxReqPerUser
                ''',
                'max_req_per_user',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('max-req-total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MaxReqTotal
                ''',
                'max_req_total',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('tls', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                GRPCTLS
                ''',
                'tls',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('transport', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                GRPCTransport
                ''',
                'transport',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('trustpoint', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                GRPCTrustpoint
                ''',
                'trustpoint',
                'Cisco-IOS-XR-man-ems-oper', False),
            ],
            'Cisco-IOS-XR-man-ems-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-man-ems-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_oper'
        ),
    },
    'Grpc.Status' : {
        'meta_info' : _MetaInfoClass('Grpc.Status',
            False, 
            [
            _MetaInfoClassMember('address-family', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                AddressFamily
                ''',
                'address_family',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-cli-config-req-recv', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterCliConfigReqRecv
                ''',
                'ct_cli_config_req_recv',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-cli-config-res-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterCliConfigResSent
                ''',
                'ct_cli_config_res_sent',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-commit-replace-req-recv', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterCommitReplaceReq
                ''',
                'ct_commit_replace_req_recv',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-commit-replace-res-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterCommitReplaceRes
                ''',
                'ct_commit_replace_res_sent',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-delete-config-req-recv', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterDeleteConfigReq
                ''',
                'ct_delete_config_req_recv',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-delete-config-res-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterDeleteConfigRes
                ''',
                'ct_delete_config_res_sent',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-get-config-req-recv', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterGetConfigReqRecv
                ''',
                'ct_get_config_req_recv',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-get-config-res-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterGetConfigResSent
                ''',
                'ct_get_config_res_sent',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-get-current-session', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CounterGetCurrentSession
                ''',
                'ct_get_current_session',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-get-oper-req-recv', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterGetOperReqRecv
                ''',
                'ct_get_oper_req_recv',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-get-oper-res-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterGetOperResSent
                ''',
                'ct_get_oper_res_sent',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-merge-config-req-recv', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterMergeConfigReq
                ''',
                'ct_merge_config_req_recv',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-merge-config-res-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterMergeConfigRes
                ''',
                'ct_merge_config_res_sent',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-replace-config-req-recv', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterReplaceConfigReq
                ''',
                'ct_replace_config_req_recv',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-replace-config-res-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterReplaceConfigSent
                ''',
                'ct_replace_config_res_sent',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-show-cmd-txt-req-recv', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterShowCmdTxtReqRecv
                ''',
                'ct_show_cmd_txt_req_recv',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('ct-show-cmd-txt-res-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                CounterShowCmdTxtResSent
                ''',
                'ct_show_cmd_txt_res_sent',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('listening-port', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ListeningPort
                ''',
                'listening_port',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('max-req-per-user', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MaxReqPerUser
                ''',
                'max_req_per_user',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('max-req-total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MaxReqTotal
                ''',
                'max_req_total',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('tls', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                GRPCTLS
                ''',
                'tls',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('transport', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                GRPCTransport
                ''',
                'transport',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('trustpoint', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                GRPCTrustpoint
                ''',
                'trustpoint',
                'Cisco-IOS-XR-man-ems-oper', False),
            ],
            'Cisco-IOS-XR-man-ems-oper',
            'status',
            _yang_ns._namespaces['Cisco-IOS-XR-man-ems-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_oper'
        ),
    },
    'Grpc' : {
        'meta_info' : _MetaInfoClass('Grpc',
            False, 
            [
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_oper', 'Grpc.Statistics', 
                [], [], 
                '''                Grpc Statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-man-ems-oper', False),
            _MetaInfoClassMember('status', REFERENCE_CLASS, 'Status' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_oper', 'Grpc.Status', 
                [], [], 
                '''                Grpc Status
                ''',
                'status',
                'Cisco-IOS-XR-man-ems-oper', False),
            ],
            'Cisco-IOS-XR-man-ems-oper',
            'grpc',
            _yang_ns._namespaces['Cisco-IOS-XR-man-ems-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_man_ems_oper'
        ),
    },
}
_meta_table['Grpc.Statistics']['meta_info'].parent =_meta_table['Grpc']['meta_info']
_meta_table['Grpc.Status']['meta_info'].parent =_meta_table['Grpc']['meta_info']
