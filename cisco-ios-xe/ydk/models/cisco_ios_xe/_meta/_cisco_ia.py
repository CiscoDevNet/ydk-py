


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiaSyncTypeEnum' : _MetaInfoEnum('CiaSyncTypeEnum', 'ydk.models.cisco_ios_xe.cisco_ia',
        {
            'disabled':'disabled',
            'without-defaults':'without_defaults',
            'include-defaults':'include_defaults',
        }, 'cisco-ia', _yang_ns._namespaces['cisco-ia']),
    'CiaLogLevelEnum' : _MetaInfoEnum('CiaLogLevelEnum', 'ydk.models.cisco_ios_xe.cisco_ia',
        {
            'none':'none',
            'error':'error',
            'warning':'warning',
            'information':'information',
            'debug':'debug',
        }, 'cisco-ia', _yang_ns._namespaces['cisco-ia']),
    'SyslogSeverityEnum' : _MetaInfoEnum('SyslogSeverityEnum', 'ydk.models.cisco_ios_xe.cisco_ia',
        {
            'none':'none',
            'emergency':'emergency',
            'alert':'alert',
            'critical':'critical',
            'error':'error',
            'warning':'warning',
            'notice':'notice',
            'info':'info',
            'debug':'debug',
        }, 'cisco-ia', _yang_ns._namespaces['cisco-ia']),
    'OnepLogLevelEnum' : _MetaInfoEnum('OnepLogLevelEnum', 'ydk.models.cisco_ios_xe.cisco_ia',
        {
            'none':'none',
            'fatal':'fatal',
            'error':'error',
            'warning':'warning',
            'information':'information',
            'debug':'debug',
            'trace':'trace',
        }, 'cisco-ia', _yang_ns._namespaces['cisco-ia']),
    'SyncFromRpc.Input' : {
        'meta_info' : _MetaInfoClass('SyncFromRpc.Input',
            False, 
            [
            _MetaInfoClassMember('sync-defaults', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Sends the output of 
                "show running all" line
                by line to Confd.
                ''',
                'sync_defaults',
                'cisco-ia', False),
            ],
            'cisco-ia',
            'input',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_ia'
        ),
    },
    'SyncFromRpc.Output' : {
        'meta_info' : _MetaInfoClass('SyncFromRpc.Output',
            False, 
            [
            _MetaInfoClassMember('result', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Output returned by the network element
                ''',
                'result',
                'cisco-ia', False),
            ],
            'cisco-ia',
            'output',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_ia'
        ),
    },
    'SyncFromRpc' : {
        'meta_info' : _MetaInfoClass('SyncFromRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xe.cisco_ia', 'SyncFromRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'cisco-ia', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xe.cisco_ia', 'SyncFromRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'cisco-ia', False),
            ],
            'cisco-ia',
            'sync-from',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_ia'
        ),
    },
    'SaveConfigRpc.Output' : {
        'meta_info' : _MetaInfoClass('SaveConfigRpc.Output',
            False, 
            [
            _MetaInfoClassMember('result', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Output returned by the network element
                ''',
                'result',
                'cisco-ia', False),
            ],
            'cisco-ia',
            'output',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_ia'
        ),
    },
    'SaveConfigRpc' : {
        'meta_info' : _MetaInfoClass('SaveConfigRpc',
            False, 
            [
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xe.cisco_ia', 'SaveConfigRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'cisco-ia', False),
            ],
            'cisco-ia',
            'save-config',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_ia'
        ),
    },
    'CheckpointRpc.Output' : {
        'meta_info' : _MetaInfoClass('CheckpointRpc.Output',
            False, 
            [
            _MetaInfoClassMember('result', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Output returned by the network element
                ''',
                'result',
                'cisco-ia', False),
            ],
            'cisco-ia',
            'output',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_ia'
        ),
    },
    'CheckpointRpc' : {
        'meta_info' : _MetaInfoClass('CheckpointRpc',
            False, 
            [
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xe.cisco_ia', 'CheckpointRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'cisco-ia', False),
            ],
            'cisco-ia',
            'checkpoint',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_ia'
        ),
    },
    'RevertRpc.Input' : {
        'meta_info' : _MetaInfoClass('RevertRpc.Input',
            False, 
            [
            _MetaInfoClassMember('now', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                To cancel the timed rollback and 
                trigger the rollback immediately
                ''',
                'now',
                'cisco-ia', False),
            _MetaInfoClassMember('timer', ATTRIBUTE, 'int' , None, None, 
                [('1', '120')], [], 
                '''                Reset parameters for the timed rollback
                ''',
                'timer',
                'cisco-ia', False),
            _MetaInfoClassMember('idle', ATTRIBUTE, 'int' , None, None, 
                [('1', '120')], [], 
                '''                Maximum allowable time period of no activity
                before reverting to the saved configuration.
                ''',
                'idle',
                'cisco-ia', False),
            ],
            'cisco-ia',
            'input',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_ia'
        ),
    },
    'RevertRpc.Output' : {
        'meta_info' : _MetaInfoClass('RevertRpc.Output',
            False, 
            [
            _MetaInfoClassMember('result', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Output returned by the network element
                ''',
                'result',
                'cisco-ia', False),
            ],
            'cisco-ia',
            'output',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_ia'
        ),
    },
    'RevertRpc' : {
        'meta_info' : _MetaInfoClass('RevertRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xe.cisco_ia', 'RevertRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'cisco-ia', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xe.cisco_ia', 'RevertRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'cisco-ia', False),
            ],
            'cisco-ia',
            'revert',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_ia'
        ),
    },
    'RollbackRpc.Input' : {
        'meta_info' : _MetaInfoClass('RollbackRpc.Input',
            False, 
            [
            _MetaInfoClassMember('target-url', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Cisco IOS XE configuration file that is to 
                replace the current running configuration
                ''',
                'target_url',
                'cisco-ia', False),
            _MetaInfoClassMember('verbose', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Display a list of the command lines applied by 
                the Cisco IOS XE software parser during each pass 
                of the configuration replace operation. The total 
                number of passes performed is also displayed.
                ''',
                'verbose',
                'cisco-ia', False),
            _MetaInfoClassMember('nolock', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disables the locking of the running 
                configuration file that prevents other users
                from changing the running configuration 
                during a configuration replace operation.
                ''',
                'nolock',
                'cisco-ia', False),
            _MetaInfoClassMember('revert-on-error', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Reverts to the original configuration upon
                error.
                ''',
                'revert_on_error',
                'cisco-ia', False),
            _MetaInfoClassMember('revert-timer', ATTRIBUTE, 'int' , None, None, 
                [('1', '120')], [], 
                '''                Reverts to the original configuration if 
                specified time elapses.
                ''',
                'revert_timer',
                'cisco-ia', False),
            ],
            'cisco-ia',
            'input',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_ia'
        ),
    },
    'RollbackRpc.Output' : {
        'meta_info' : _MetaInfoClass('RollbackRpc.Output',
            False, 
            [
            _MetaInfoClassMember('result', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Output returned by the network element
                ''',
                'result',
                'cisco-ia', False),
            ],
            'cisco-ia',
            'output',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_ia'
        ),
    },
    'RollbackRpc' : {
        'meta_info' : _MetaInfoClass('RollbackRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xe.cisco_ia', 'RollbackRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'cisco-ia', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xe.cisco_ia', 'RollbackRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'cisco-ia', False),
            ],
            'cisco-ia',
            'rollback',
            _yang_ns._namespaces['cisco-ia'],
        'ydk.models.cisco_ios_xe.cisco_ia'
        ),
    },
}
_meta_table['SyncFromRpc.Input']['meta_info'].parent =_meta_table['SyncFromRpc']['meta_info']
_meta_table['SyncFromRpc.Output']['meta_info'].parent =_meta_table['SyncFromRpc']['meta_info']
_meta_table['SaveConfigRpc.Output']['meta_info'].parent =_meta_table['SaveConfigRpc']['meta_info']
_meta_table['CheckpointRpc.Output']['meta_info'].parent =_meta_table['CheckpointRpc']['meta_info']
_meta_table['RevertRpc.Input']['meta_info'].parent =_meta_table['RevertRpc']['meta_info']
_meta_table['RevertRpc.Output']['meta_info'].parent =_meta_table['RevertRpc']['meta_info']
_meta_table['RollbackRpc.Input']['meta_info'].parent =_meta_table['RollbackRpc']['meta_info']
_meta_table['RollbackRpc.Output']['meta_info'].parent =_meta_table['RollbackRpc']['meta_info']
