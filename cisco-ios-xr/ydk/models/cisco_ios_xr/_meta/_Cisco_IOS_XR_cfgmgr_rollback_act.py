


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'RollBackConfigurationLastRpc.Input' : {
        'meta_info' : _MetaInfoClass('RollBackConfigurationLastRpc.Input',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Number of commits to rollback
                ''',
                'count',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            _MetaInfoClassMember('force', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override commit blocks
                ''',
                'force',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            _MetaInfoClassMember('best-effort', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Rollback via best-effort operation
                ''',
                'best_effort',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            _MetaInfoClassMember('label', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Assign a label to this rollback
                ''',
                'label',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            _MetaInfoClassMember('comment', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Assign a comment to this rollback
                ''',
                'comment',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            ],
            'Cisco-IOS-XR-cfgmgr-rollback-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-cfgmgr-rollback-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act'
        ),
    },
    'RollBackConfigurationLastRpc' : {
        'meta_info' : _MetaInfoClass('RollBackConfigurationLastRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act', 'RollBackConfigurationLastRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            ],
            'Cisco-IOS-XR-cfgmgr-rollback-act',
            'roll-back-configuration-last',
            _yang_ns._namespaces['Cisco-IOS-XR-cfgmgr-rollback-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act'
        ),
    },
    'RollBackConfigurationToRpc.Input' : {
        'meta_info' : _MetaInfoClass('RollBackConfigurationToRpc.Input',
            False, 
            [
            _MetaInfoClassMember('commit-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Commit ID
                ''',
                'commit_id',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            _MetaInfoClassMember('force', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override commit blocks
                ''',
                'force',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            _MetaInfoClassMember('best-effort', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Rollback via best-effort operation
                ''',
                'best_effort',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            _MetaInfoClassMember('label', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Assign a label to this rollback
                ''',
                'label',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            _MetaInfoClassMember('comment', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Assign a comment to this rollback
                ''',
                'comment',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            ],
            'Cisco-IOS-XR-cfgmgr-rollback-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-cfgmgr-rollback-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act'
        ),
    },
    'RollBackConfigurationToRpc' : {
        'meta_info' : _MetaInfoClass('RollBackConfigurationToRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act', 'RollBackConfigurationToRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            ],
            'Cisco-IOS-XR-cfgmgr-rollback-act',
            'roll-back-configuration-to',
            _yang_ns._namespaces['Cisco-IOS-XR-cfgmgr-rollback-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act'
        ),
    },
    'RollBackConfigurationToExcludeRpc.Input' : {
        'meta_info' : _MetaInfoClass('RollBackConfigurationToExcludeRpc.Input',
            False, 
            [
            _MetaInfoClassMember('commit-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Commit ID
                ''',
                'commit_id',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            _MetaInfoClassMember('force', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override commit blocks
                ''',
                'force',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            _MetaInfoClassMember('best-effort', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Rollback via best-effort operation
                ''',
                'best_effort',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            _MetaInfoClassMember('label', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Assign a label to this rollback
                ''',
                'label',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            _MetaInfoClassMember('comment', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Assign a comment to this rollback
                ''',
                'comment',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            ],
            'Cisco-IOS-XR-cfgmgr-rollback-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-cfgmgr-rollback-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act'
        ),
    },
    'RollBackConfigurationToExcludeRpc' : {
        'meta_info' : _MetaInfoClass('RollBackConfigurationToExcludeRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act', 'RollBackConfigurationToExcludeRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            ],
            'Cisco-IOS-XR-cfgmgr-rollback-act',
            'roll-back-configuration-to-exclude',
            _yang_ns._namespaces['Cisco-IOS-XR-cfgmgr-rollback-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act'
        ),
    },
    'RollBackConfigurationRpc.Input' : {
        'meta_info' : _MetaInfoClass('RollBackConfigurationRpc.Input',
            False, 
            [
            _MetaInfoClassMember('commit-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Commit ID
                ''',
                'commit_id',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            _MetaInfoClassMember('force', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Override commit blocks
                ''',
                'force',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            _MetaInfoClassMember('best-effort', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Rollback via best-effort operation
                ''',
                'best_effort',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            _MetaInfoClassMember('label', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Assign a label to this rollback
                ''',
                'label',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            _MetaInfoClassMember('comment', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Assign a comment to this rollback
                ''',
                'comment',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            ],
            'Cisco-IOS-XR-cfgmgr-rollback-act',
            'input',
            _yang_ns._namespaces['Cisco-IOS-XR-cfgmgr-rollback-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act'
        ),
    },
    'RollBackConfigurationRpc' : {
        'meta_info' : _MetaInfoClass('RollBackConfigurationRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act', 'RollBackConfigurationRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'Cisco-IOS-XR-cfgmgr-rollback-act', False),
            ],
            'Cisco-IOS-XR-cfgmgr-rollback-act',
            'roll-back-configuration',
            _yang_ns._namespaces['Cisco-IOS-XR-cfgmgr-rollback-act'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_cfgmgr_rollback_act'
        ),
    },
}
_meta_table['RollBackConfigurationLastRpc.Input']['meta_info'].parent =_meta_table['RollBackConfigurationLastRpc']['meta_info']
_meta_table['RollBackConfigurationToRpc.Input']['meta_info'].parent =_meta_table['RollBackConfigurationToRpc']['meta_info']
_meta_table['RollBackConfigurationToExcludeRpc.Input']['meta_info'].parent =_meta_table['RollBackConfigurationToExcludeRpc']['meta_info']
_meta_table['RollBackConfigurationRpc.Input']['meta_info'].parent =_meta_table['RollBackConfigurationRpc']['meta_info']
