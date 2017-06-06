


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'HistRecordEnum' : _MetaInfoEnum('HistRecordEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper',
        {
            'cfghist-bag-record-all':'cfghist_bag_record_all',
            'cfghist-bag-record-alarm':'cfghist_bag_record_alarm',
            'cfghist-bag-record-cfs-check':'cfghist_bag_record_cfs_check',
            'cfghist-bag-record-commit':'cfghist_bag_record_commit',
            'cfghist-bag-record-oir':'cfghist_bag_record_oir',
            'cfghist-bag-record-shutdown':'cfghist_bag_record_shutdown',
            'cfghist-bag-record-startup':'cfghist_bag_record_startup',
            'cfghist-bag-record-backup':'cfghist_bag_record_backup',
            'cfghist-bag-record-rebase':'cfghist_bag_record_rebase',
            'cfghist-bag-record-last':'cfghist_bag_record_last',
        }, 'Cisco-IOS-XR-config-cfgmgr-exec-oper', _yang_ns._namespaces['Cisco-IOS-XR-config-cfgmgr-exec-oper']),
    'CfgHistGl.RecordType.Record.Info.AlarmInfo' : {
        'meta_info' : _MetaInfoClass('CfgHistGl.RecordType.Record.Info.AlarmInfo',
            False, 
            [
            _MetaInfoClassMember('state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('where', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Where
                ''',
                'where',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            ],
            'Cisco-IOS-XR-config-cfgmgr-exec-oper',
            'alarm-info',
            _yang_ns._namespaces['Cisco-IOS-XR-config-cfgmgr-exec-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper'
        ),
    },
    'CfgHistGl.RecordType.Record.Info.CfscheckInfo' : {
        'meta_info' : _MetaInfoClass('CfgHistGl.RecordType.Record.Info.CfscheckInfo',
            False, 
            [
            _MetaInfoClassMember('line', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Line
                ''',
                'line',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('user-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                UserId
                ''',
                'user_id',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            ],
            'Cisco-IOS-XR-config-cfgmgr-exec-oper',
            'cfscheck-info',
            _yang_ns._namespaces['Cisco-IOS-XR-config-cfgmgr-exec-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper'
        ),
    },
    'CfgHistGl.RecordType.Record.Info.CommitInfo' : {
        'meta_info' : _MetaInfoClass('CfgHistGl.RecordType.Record.Info.CommitInfo',
            False, 
            [
            _MetaInfoClassMember('client-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Client name
                ''',
                'client_name',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('comment', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Comment
                ''',
                'comment',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('commit-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                CommitId
                ''',
                'commit_id',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('label', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Label
                ''',
                'label',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('line', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Line
                ''',
                'line',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('user-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                UserId
                ''',
                'user_id',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            ],
            'Cisco-IOS-XR-config-cfgmgr-exec-oper',
            'commit-info',
            _yang_ns._namespaces['Cisco-IOS-XR-config-cfgmgr-exec-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper'
        ),
    },
    'CfgHistGl.RecordType.Record.Info.OirInfo' : {
        'meta_info' : _MetaInfoClass('CfgHistGl.RecordType.Record.Info.OirInfo',
            False, 
            [
            _MetaInfoClassMember('config-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Config Name
                ''',
                'config_name',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('config-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Config Type
                ''',
                'config_type',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('operation', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Operation
                ''',
                'operation',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            ],
            'Cisco-IOS-XR-config-cfgmgr-exec-oper',
            'oir-info',
            _yang_ns._namespaces['Cisco-IOS-XR-config-cfgmgr-exec-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper'
        ),
    },
    'CfgHistGl.RecordType.Record.Info.ShutdownInfo' : {
        'meta_info' : _MetaInfoClass('CfgHistGl.RecordType.Record.Info.ShutdownInfo',
            False, 
            [
            _MetaInfoClassMember('comment', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Comment
                ''',
                'comment',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            ],
            'Cisco-IOS-XR-config-cfgmgr-exec-oper',
            'shutdown-info',
            _yang_ns._namespaces['Cisco-IOS-XR-config-cfgmgr-exec-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper'
        ),
    },
    'CfgHistGl.RecordType.Record.Info.StartupInfo' : {
        'meta_info' : _MetaInfoClass('CfgHistGl.RecordType.Record.Info.StartupInfo',
            False, 
            [
            _MetaInfoClassMember('boot-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Boot Path
                ''',
                'boot_path',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('how-booted', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                How Booted
                ''',
                'how_booted',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            ],
            'Cisco-IOS-XR-config-cfgmgr-exec-oper',
            'startup-info',
            _yang_ns._namespaces['Cisco-IOS-XR-config-cfgmgr-exec-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper'
        ),
    },
    'CfgHistGl.RecordType.Record.Info.BackupInfo' : {
        'meta_info' : _MetaInfoClass('CfgHistGl.RecordType.Record.Info.BackupInfo',
            False, 
            [
            _MetaInfoClassMember('comment', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Comment
                ''',
                'comment',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            ],
            'Cisco-IOS-XR-config-cfgmgr-exec-oper',
            'backup-info',
            _yang_ns._namespaces['Cisco-IOS-XR-config-cfgmgr-exec-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper'
        ),
    },
    'CfgHistGl.RecordType.Record.Info' : {
        'meta_info' : _MetaInfoClass('CfgHistGl.RecordType.Record.Info',
            False, 
            [
            _MetaInfoClassMember('a', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                B
                ''',
                'a',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('alarm-info', REFERENCE_CLASS, 'AlarmInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper', 'CfgHistGl.RecordType.Record.Info.AlarmInfo', 
                [], [], 
                '''                alarm info
                ''',
                'alarm_info',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('backup-info', REFERENCE_CLASS, 'BackupInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper', 'CfgHistGl.RecordType.Record.Info.BackupInfo', 
                [], [], 
                '''                backup info
                ''',
                'backup_info',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('cfscheck-info', REFERENCE_CLASS, 'CfscheckInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper', 'CfgHistGl.RecordType.Record.Info.CfscheckInfo', 
                [], [], 
                '''                cfscheck info
                ''',
                'cfscheck_info',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('commit-info', REFERENCE_CLASS, 'CommitInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper', 'CfgHistGl.RecordType.Record.Info.CommitInfo', 
                [], [], 
                '''                commit info
                ''',
                'commit_info',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('oir-info', REFERENCE_CLASS, 'OirInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper', 'CfgHistGl.RecordType.Record.Info.OirInfo', 
                [], [], 
                '''                oir info
                ''',
                'oir_info',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('shutdown-info', REFERENCE_CLASS, 'ShutdownInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper', 'CfgHistGl.RecordType.Record.Info.ShutdownInfo', 
                [], [], 
                '''                shutdown info
                ''',
                'shutdown_info',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('startup-info', REFERENCE_CLASS, 'StartupInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper', 'CfgHistGl.RecordType.Record.Info.StartupInfo', 
                [], [], 
                '''                startup info
                ''',
                'startup_info',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'HistRecordEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper', 'HistRecordEnum', 
                [], [], 
                '''                type
                ''',
                'type',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            ],
            'Cisco-IOS-XR-config-cfgmgr-exec-oper',
            'info',
            _yang_ns._namespaces['Cisco-IOS-XR-config-cfgmgr-exec-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper'
        ),
    },
    'CfgHistGl.RecordType.Record' : {
        'meta_info' : _MetaInfoClass('CfgHistGl.RecordType.Record',
            False, 
            [
            _MetaInfoClassMember('record', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Record
                ''',
                'record',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', True),
            _MetaInfoClassMember('info', REFERENCE_CLASS, 'Info' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper', 'CfgHistGl.RecordType.Record.Info', 
                [], [], 
                '''                Content of the history
                ''',
                'info',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('record-type', REFERENCE_ENUM_CLASS, 'HistRecordEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper', 'HistRecordEnum', 
                [], [], 
                '''                Record type
                ''',
                'record_type',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            _MetaInfoClassMember('timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time stamp for the history
                ''',
                'timestamp',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            ],
            'Cisco-IOS-XR-config-cfgmgr-exec-oper',
            'record',
            _yang_ns._namespaces['Cisco-IOS-XR-config-cfgmgr-exec-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper'
        ),
    },
    'CfgHistGl.RecordType' : {
        'meta_info' : _MetaInfoClass('CfgHistGl.RecordType',
            False, 
            [
            _MetaInfoClassMember('record-type', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Record type
                ''',
                'record_type',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', True),
            _MetaInfoClassMember('record', REFERENCE_LIST, 'Record' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper', 'CfgHistGl.RecordType.Record', 
                [], [], 
                '''                History summary information for a specific type
                of history
                ''',
                'record',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            ],
            'Cisco-IOS-XR-config-cfgmgr-exec-oper',
            'record-type',
            _yang_ns._namespaces['Cisco-IOS-XR-config-cfgmgr-exec-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper'
        ),
    },
    'CfgHistGl' : {
        'meta_info' : _MetaInfoClass('CfgHistGl',
            False, 
            [
            _MetaInfoClassMember('record-type', REFERENCE_LIST, 'RecordType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper', 'CfgHistGl.RecordType', 
                [], [], 
                '''                History summary information for a specific type
                of history
                ''',
                'record_type',
                'Cisco-IOS-XR-config-cfgmgr-exec-oper', False),
            ],
            'Cisco-IOS-XR-config-cfgmgr-exec-oper',
            'cfg-hist-gl',
            _yang_ns._namespaces['Cisco-IOS-XR-config-cfgmgr-exec-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_config_cfgmgr_exec_oper'
        ),
    },
}
_meta_table['CfgHistGl.RecordType.Record.Info.AlarmInfo']['meta_info'].parent =_meta_table['CfgHistGl.RecordType.Record.Info']['meta_info']
_meta_table['CfgHistGl.RecordType.Record.Info.CfscheckInfo']['meta_info'].parent =_meta_table['CfgHistGl.RecordType.Record.Info']['meta_info']
_meta_table['CfgHistGl.RecordType.Record.Info.CommitInfo']['meta_info'].parent =_meta_table['CfgHistGl.RecordType.Record.Info']['meta_info']
_meta_table['CfgHistGl.RecordType.Record.Info.OirInfo']['meta_info'].parent =_meta_table['CfgHistGl.RecordType.Record.Info']['meta_info']
_meta_table['CfgHistGl.RecordType.Record.Info.ShutdownInfo']['meta_info'].parent =_meta_table['CfgHistGl.RecordType.Record.Info']['meta_info']
_meta_table['CfgHistGl.RecordType.Record.Info.StartupInfo']['meta_info'].parent =_meta_table['CfgHistGl.RecordType.Record.Info']['meta_info']
_meta_table['CfgHistGl.RecordType.Record.Info.BackupInfo']['meta_info'].parent =_meta_table['CfgHistGl.RecordType.Record.Info']['meta_info']
_meta_table['CfgHistGl.RecordType.Record.Info']['meta_info'].parent =_meta_table['CfgHistGl.RecordType.Record']['meta_info']
_meta_table['CfgHistGl.RecordType.Record']['meta_info'].parent =_meta_table['CfgHistGl.RecordType']['meta_info']
_meta_table['CfgHistGl.RecordType']['meta_info'].parent =_meta_table['CfgHistGl']['meta_info']
