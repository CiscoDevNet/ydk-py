


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AlAlarmSeverityEnum' : _MetaInfoEnum('AlAlarmSeverityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper',
        {
            'unknown':'unknown',
            'emergency':'emergency',
            'alert':'alert',
            'critical':'critical',
            'error':'error',
            'warning':'warning',
            'notice':'notice',
            'informational':'informational',
            'debugging':'debugging',
        }, 'Cisco-IOS-XR-infra-correlator-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper']),
    'AlAlarmBistateEnum' : _MetaInfoEnum('AlAlarmBistateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper',
        {
            'not-available':'not_available',
            'active':'active',
            'clear':'clear',
        }, 'Cisco-IOS-XR-infra-correlator-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper']),
    'AcRuleStateEnum' : _MetaInfoEnum('AcRuleStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper',
        {
            'rule-unapplied':'rule_unapplied',
            'rule-applied':'rule_applied',
            'rule-applied-all':'rule_applied_all',
        }, 'Cisco-IOS-XR-infra-correlator-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper']),
    'Suppression.RuleSummaries.RuleSummary' : {
        'meta_info' : _MetaInfoClass('Suppression.RuleSummaries.RuleSummary',
            False, 
            [
            _MetaInfoClassMember('rule-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Suppression Rule Name
                ''',
                'rule_name',
                'Cisco-IOS-XR-infra-correlator-oper', True),
            _MetaInfoClassMember('rule-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Suppress Rule Name
                ''',
                'rule_name_xr',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rule-state', REFERENCE_ENUM_CLASS, 'AcRuleStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'AcRuleStateEnum', 
                [], [], 
                '''                Applied state of the rule It could be not
                applied, applied or applied to all
                ''',
                'rule_state',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('suppressed-alarms-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of suppressed alarms associated with this
                rule
                ''',
                'suppressed_alarms_count',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'rule-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Suppression.RuleSummaries' : {
        'meta_info' : _MetaInfoClass('Suppression.RuleSummaries',
            False, 
            [
            _MetaInfoClassMember('rule-summary', REFERENCE_LIST, 'RuleSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Suppression.RuleSummaries.RuleSummary', 
                [], [], 
                '''                One of the suppression rules
                ''',
                'rule_summary',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'rule-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Suppression.RuleDetails.RuleDetail.RuleSummary' : {
        'meta_info' : _MetaInfoClass('Suppression.RuleDetails.RuleDetail.RuleSummary',
            False, 
            [
            _MetaInfoClassMember('rule-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Suppress Rule Name
                ''',
                'rule_name_xr',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rule-state', REFERENCE_ENUM_CLASS, 'AcRuleStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'AcRuleStateEnum', 
                [], [], 
                '''                Applied state of the rule It could be not
                applied, applied or applied to all
                ''',
                'rule_state',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('suppressed-alarms-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of suppressed alarms associated with this
                rule
                ''',
                'suppressed_alarms_count',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'rule-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Suppression.RuleDetails.RuleDetail.Codes' : {
        'meta_info' : _MetaInfoClass('Suppression.RuleDetails.RuleDetail.Codes',
            False, 
            [
            _MetaInfoClassMember('category', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Category of messages to which this alarm belongs
                ''',
                'category',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('code', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Alarm code which further qualifies the alarm
                within a message group
                ''',
                'code',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Group of messages to which this alarm belongs
                ''',
                'group',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'codes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Suppression.RuleDetails.RuleDetail' : {
        'meta_info' : _MetaInfoClass('Suppression.RuleDetails.RuleDetail',
            False, 
            [
            _MetaInfoClassMember('rule-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Suppression Rule Name
                ''',
                'rule_name',
                'Cisco-IOS-XR-infra-correlator-oper', True),
            _MetaInfoClassMember('alarm-severity', REFERENCE_ENUM_CLASS, 'AlAlarmSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'AlAlarmSeverityEnum', 
                [], [], 
                '''                Severity level to suppress
                ''',
                'alarm_severity',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('all-alarms', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Match any alarm
                ''',
                'all_alarms',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('apply-source', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Sources (R/S/M) to which the rule is applied
                ''',
                'apply_source',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('codes', REFERENCE_LIST, 'Codes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Suppression.RuleDetails.RuleDetail.Codes', 
                [], [], 
                '''                Message codes defining the rule.
                ''',
                'codes',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rule-summary', REFERENCE_CLASS, 'RuleSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Suppression.RuleDetails.RuleDetail.RuleSummary', 
                [], [], 
                '''                Rule summary, name, etc
                ''',
                'rule_summary',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'rule-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Suppression.RuleDetails' : {
        'meta_info' : _MetaInfoClass('Suppression.RuleDetails',
            False, 
            [
            _MetaInfoClassMember('rule-detail', REFERENCE_LIST, 'RuleDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Suppression.RuleDetails.RuleDetail', 
                [], [], 
                '''                Details of one of the suppression rules
                ''',
                'rule_detail',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'rule-details',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Suppression' : {
        'meta_info' : _MetaInfoClass('Suppression',
            False, 
            [
            _MetaInfoClassMember('rule-details', REFERENCE_CLASS, 'RuleDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Suppression.RuleDetails', 
                [], [], 
                '''                Table that contains the database of suppression
                rule details
                ''',
                'rule_details',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rule-summaries', REFERENCE_CLASS, 'RuleSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Suppression.RuleSummaries', 
                [], [], 
                '''                Table that contains the database of suppression
                rule summary
                ''',
                'rule_summaries',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'suppression',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator.Rules.Rule.Codes' : {
        'meta_info' : _MetaInfoClass('Correlator.Rules.Rule.Codes',
            False, 
            [
            _MetaInfoClassMember('category', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Category of messages to which this alarm belongs
                ''',
                'category',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('code', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Alarm code which further qualifies the alarm
                within a message group
                ''',
                'code',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Group of messages to which this alarm belongs
                ''',
                'group',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'codes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator.Rules.Rule' : {
        'meta_info' : _MetaInfoClass('Correlator.Rules.Rule',
            False, 
            [
            _MetaInfoClassMember('rule-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Correlation Rule Name
                ''',
                'rule_name',
                'Cisco-IOS-XR-infra-correlator-oper', True),
            _MetaInfoClassMember('apply-context', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Contexts (Interfaces) to which the rule is
                applied
                ''',
                'apply_context',
                'Cisco-IOS-XR-infra-correlator-oper', False, max_elements=32),
            _MetaInfoClassMember('apply-location', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Locations (R/S/M) to which the rule is  applied
                ''',
                'apply_location',
                'Cisco-IOS-XR-infra-correlator-oper', False, max_elements=32),
            _MetaInfoClassMember('codes', REFERENCE_LIST, 'Codes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Correlator.Rules.Rule.Codes', 
                [], [], 
                '''                Message codes defining the rule.
                ''',
                'codes',
                'Cisco-IOS-XR-infra-correlator-oper', False, max_elements=10),
            _MetaInfoClassMember('rule-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlation Rule Name
                ''',
                'rule_name_xr',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rule-state', REFERENCE_ENUM_CLASS, 'AcRuleStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'AcRuleStateEnum', 
                [], [], 
                '''                Applied state of the rule It could be not
                applied, applied or applied to all
                ''',
                'rule_state',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time window (in ms) for which root/all messages
                are kept in correlater before sending them to
                the logger
                ''',
                'timeout',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'rule',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator.Rules' : {
        'meta_info' : _MetaInfoClass('Correlator.Rules',
            False, 
            [
            _MetaInfoClassMember('rule', REFERENCE_LIST, 'Rule' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Correlator.Rules.Rule', 
                [], [], 
                '''                One of the correlation rules
                ''',
                'rule',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'rules',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator.BufferStatus' : {
        'meta_info' : _MetaInfoClass('Correlator.BufferStatus',
            False, 
            [
            _MetaInfoClassMember('configured-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured buffer size
                ''',
                'configured_size',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('current-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current buffer usage
                ''',
                'current_size',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'buffer-status',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator.Alarms.Alarm.AlarmInfo' : {
        'meta_info' : _MetaInfoClass('Correlator.Alarms.Alarm.AlarmInfo',
            False, 
            [
            _MetaInfoClassMember('additional-text', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Full text of the Alarm
                ''',
                'additional_text',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('category', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Category of the alarm
                ''',
                'category',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('code', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Alarm code which further qualifies the alarm
                within a message group
                ''',
                'code',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('correlation-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Correlation Identifier
                ''',
                'correlation_id',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Group of messages to which this alarm belongs to
                ''',
                'group',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('is-admin', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates the event id admin-level
                ''',
                'is_admin',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('severity', REFERENCE_ENUM_CLASS, 'AlAlarmSeverityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'AlAlarmSeverityEnum', 
                [], [], 
                '''                Severity of the alarm
                ''',
                'severity',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('source-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Identifier(Location).Indicates the node
                in which the alarm was generated
                ''',
                'source_id',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'AlAlarmBistateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'AlAlarmBistateEnum', 
                [], [], 
                '''                State of the alarm (bistate alarms only)
                ''',
                'state',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time when the alarm was generated. It is
                expressed in number of milliseconds since 00:00
                :00 UTC, January 1, 1970
                ''',
                'timestamp',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'alarm-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator.Alarms.Alarm' : {
        'meta_info' : _MetaInfoClass('Correlator.Alarms.Alarm',
            False, 
            [
            _MetaInfoClassMember('alarm-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Alarm ID
                ''',
                'alarm_id',
                'Cisco-IOS-XR-infra-correlator-oper', True),
            _MetaInfoClassMember('alarm-info', REFERENCE_CLASS, 'AlarmInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Correlator.Alarms.Alarm.AlarmInfo', 
                [], [], 
                '''                Correlated alarm information
                ''',
                'alarm_info',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('context', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Context string  for the alarm
                ''',
                'context',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rule-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlation rule name
                ''',
                'rule_name',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'alarm',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator.Alarms' : {
        'meta_info' : _MetaInfoClass('Correlator.Alarms',
            False, 
            [
            _MetaInfoClassMember('alarm', REFERENCE_LIST, 'Alarm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Correlator.Alarms.Alarm', 
                [], [], 
                '''                One of the correlated alarms
                ''',
                'alarm',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'alarms',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator.RuleSetSummaries.RuleSetSummary' : {
        'meta_info' : _MetaInfoClass('Correlator.RuleSetSummaries.RuleSetSummary',
            False, 
            [
            _MetaInfoClassMember('rule-set-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Ruleset Name
                ''',
                'rule_set_name',
                'Cisco-IOS-XR-infra-correlator-oper', True),
            _MetaInfoClassMember('rule-set-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ruleset Name
                ''',
                'rule_set_name_xr',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'rule-set-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator.RuleSetSummaries' : {
        'meta_info' : _MetaInfoClass('Correlator.RuleSetSummaries',
            False, 
            [
            _MetaInfoClassMember('rule-set-summary', REFERENCE_LIST, 'RuleSetSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Correlator.RuleSetSummaries.RuleSetSummary', 
                [], [], 
                '''                Summary of one of the correlation rulesets
                ''',
                'rule_set_summary',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'rule-set-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator.RuleSetDetails.RuleSetDetail.Rules' : {
        'meta_info' : _MetaInfoClass('Correlator.RuleSetDetails.RuleSetDetail.Rules',
            False, 
            [
            _MetaInfoClassMember('buffered-alarms-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of buffered alarms correlated to this
                rule
                ''',
                'buffered_alarms_count',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rule-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlation Rule Name
                ''',
                'rule_name_xr',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rule-state', REFERENCE_ENUM_CLASS, 'AcRuleStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'AcRuleStateEnum', 
                [], [], 
                '''                Applied state of the rule It could be not
                applied, applied or applied to all
                ''',
                'rule_state',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('stateful', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the rule is stateful
                ''',
                'stateful',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'rules',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator.RuleSetDetails.RuleSetDetail' : {
        'meta_info' : _MetaInfoClass('Correlator.RuleSetDetails.RuleSetDetail',
            False, 
            [
            _MetaInfoClassMember('rule-set-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Ruleset Name
                ''',
                'rule_set_name',
                'Cisco-IOS-XR-infra-correlator-oper', True),
            _MetaInfoClassMember('rule-set-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ruleset Name
                ''',
                'rule_set_name_xr',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rules', REFERENCE_LIST, 'Rules' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Correlator.RuleSetDetails.RuleSetDetail.Rules', 
                [], [], 
                '''                Rules contained in a ruleset
                ''',
                'rules',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'rule-set-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator.RuleSetDetails' : {
        'meta_info' : _MetaInfoClass('Correlator.RuleSetDetails',
            False, 
            [
            _MetaInfoClassMember('rule-set-detail', REFERENCE_LIST, 'RuleSetDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Correlator.RuleSetDetails.RuleSetDetail', 
                [], [], 
                '''                Detail of one of the correlation rulesets
                ''',
                'rule_set_detail',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'rule-set-details',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator.RuleDetails.RuleDetail.RuleSummary' : {
        'meta_info' : _MetaInfoClass('Correlator.RuleDetails.RuleDetail.RuleSummary',
            False, 
            [
            _MetaInfoClassMember('buffered-alarms-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of buffered alarms correlated to this
                rule
                ''',
                'buffered_alarms_count',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rule-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlation Rule Name
                ''',
                'rule_name_xr',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rule-state', REFERENCE_ENUM_CLASS, 'AcRuleStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'AcRuleStateEnum', 
                [], [], 
                '''                Applied state of the rule It could be not
                applied, applied or applied to all
                ''',
                'rule_state',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('stateful', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the rule is stateful
                ''',
                'stateful',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'rule-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator.RuleDetails.RuleDetail.Codes' : {
        'meta_info' : _MetaInfoClass('Correlator.RuleDetails.RuleDetail.Codes',
            False, 
            [
            _MetaInfoClassMember('category', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Category of messages to which this alarm belongs
                ''',
                'category',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('code', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Alarm code which further qualifies the alarm
                within a message group
                ''',
                'code',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Group of messages to which this alarm belongs
                ''',
                'group',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'codes',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator.RuleDetails.RuleDetail' : {
        'meta_info' : _MetaInfoClass('Correlator.RuleDetails.RuleDetail',
            False, 
            [
            _MetaInfoClassMember('rule-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Correlation Rule Name
                ''',
                'rule_name',
                'Cisco-IOS-XR-infra-correlator-oper', True),
            _MetaInfoClassMember('apply-context', REFERENCE_LEAFLIST, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Contexts (Interfaces) to which the rule is
                applied
                ''',
                'apply_context',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('apply-location', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Locations (R/S/M) to which the rule is applied
                ''',
                'apply_location',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('codes', REFERENCE_LIST, 'Codes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Correlator.RuleDetails.RuleDetail.Codes', 
                [], [], 
                '''                Message codes defining the rule.
                ''',
                'codes',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('context-correlation', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether context correlation is enabled
                ''',
                'context_correlation',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('internal', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if the rule is internal
                ''',
                'internal',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('reissue-non-bistate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether to reissue non-bistate alarms
                ''',
                'reissue_non_bistate',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('reparent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Reparent
                ''',
                'reparent',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('root-cause-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Timeout before root cause alarm
                ''',
                'root_cause_timeout',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rule-summary', REFERENCE_CLASS, 'RuleSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Correlator.RuleDetails.RuleDetail.RuleSummary', 
                [], [], 
                '''                Rule summary, name, etc
                ''',
                'rule_summary',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time window (in ms) for which root/all messages
                are kept in correlater before sending them to
                the logger
                ''',
                'timeout',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'rule-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator.RuleDetails' : {
        'meta_info' : _MetaInfoClass('Correlator.RuleDetails',
            False, 
            [
            _MetaInfoClassMember('rule-detail', REFERENCE_LIST, 'RuleDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Correlator.RuleDetails.RuleDetail', 
                [], [], 
                '''                Details of one of the correlation rules
                ''',
                'rule_detail',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'rule-details',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator.RuleSummaries.RuleSummary' : {
        'meta_info' : _MetaInfoClass('Correlator.RuleSummaries.RuleSummary',
            False, 
            [
            _MetaInfoClassMember('rule-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Correlation Rule Name
                ''',
                'rule_name',
                'Cisco-IOS-XR-infra-correlator-oper', True),
            _MetaInfoClassMember('buffered-alarms-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of buffered alarms correlated to this
                rule
                ''',
                'buffered_alarms_count',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rule-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlation Rule Name
                ''',
                'rule_name_xr',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rule-state', REFERENCE_ENUM_CLASS, 'AcRuleStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'AcRuleStateEnum', 
                [], [], 
                '''                Applied state of the rule It could be not
                applied, applied or applied to all
                ''',
                'rule_state',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('stateful', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the rule is stateful
                ''',
                'stateful',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'rule-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator.RuleSummaries' : {
        'meta_info' : _MetaInfoClass('Correlator.RuleSummaries',
            False, 
            [
            _MetaInfoClassMember('rule-summary', REFERENCE_LIST, 'RuleSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Correlator.RuleSummaries.RuleSummary', 
                [], [], 
                '''                One of the correlation rules
                ''',
                'rule_summary',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'rule-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
    'Correlator' : {
        'meta_info' : _MetaInfoClass('Correlator',
            False, 
            [
            _MetaInfoClassMember('alarms', REFERENCE_CLASS, 'Alarms' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Correlator.Alarms', 
                [], [], 
                '''                Correlated alarms Table
                ''',
                'alarms',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('buffer-status', REFERENCE_CLASS, 'BufferStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Correlator.BufferStatus', 
                [], [], 
                '''                Describes buffer utilization and parameters
                configured
                ''',
                'buffer_status',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rule-details', REFERENCE_CLASS, 'RuleDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Correlator.RuleDetails', 
                [], [], 
                '''                Table that contains the database of correlation
                rule details
                ''',
                'rule_details',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rule-set-details', REFERENCE_CLASS, 'RuleSetDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Correlator.RuleSetDetails', 
                [], [], 
                '''                Table that contains the ruleset detail info
                ''',
                'rule_set_details',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rule-set-summaries', REFERENCE_CLASS, 'RuleSetSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Correlator.RuleSetSummaries', 
                [], [], 
                '''                Table that contains the ruleset summary info
                ''',
                'rule_set_summaries',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rule-summaries', REFERENCE_CLASS, 'RuleSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Correlator.RuleSummaries', 
                [], [], 
                '''                Table that contains the database of correlation
                rule summary
                ''',
                'rule_summaries',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            _MetaInfoClassMember('rules', REFERENCE_CLASS, 'Rules' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper', 'Correlator.Rules', 
                [], [], 
                '''                Table that contains the database of correlation
                rules
                ''',
                'rules',
                'Cisco-IOS-XR-infra-correlator-oper', False),
            ],
            'Cisco-IOS-XR-infra-correlator-oper',
            'correlator',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-correlator-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_correlator_oper'
        ),
    },
}
_meta_table['Suppression.RuleSummaries.RuleSummary']['meta_info'].parent =_meta_table['Suppression.RuleSummaries']['meta_info']
_meta_table['Suppression.RuleDetails.RuleDetail.RuleSummary']['meta_info'].parent =_meta_table['Suppression.RuleDetails.RuleDetail']['meta_info']
_meta_table['Suppression.RuleDetails.RuleDetail.Codes']['meta_info'].parent =_meta_table['Suppression.RuleDetails.RuleDetail']['meta_info']
_meta_table['Suppression.RuleDetails.RuleDetail']['meta_info'].parent =_meta_table['Suppression.RuleDetails']['meta_info']
_meta_table['Suppression.RuleSummaries']['meta_info'].parent =_meta_table['Suppression']['meta_info']
_meta_table['Suppression.RuleDetails']['meta_info'].parent =_meta_table['Suppression']['meta_info']
_meta_table['Correlator.Rules.Rule.Codes']['meta_info'].parent =_meta_table['Correlator.Rules.Rule']['meta_info']
_meta_table['Correlator.Rules.Rule']['meta_info'].parent =_meta_table['Correlator.Rules']['meta_info']
_meta_table['Correlator.Alarms.Alarm.AlarmInfo']['meta_info'].parent =_meta_table['Correlator.Alarms.Alarm']['meta_info']
_meta_table['Correlator.Alarms.Alarm']['meta_info'].parent =_meta_table['Correlator.Alarms']['meta_info']
_meta_table['Correlator.RuleSetSummaries.RuleSetSummary']['meta_info'].parent =_meta_table['Correlator.RuleSetSummaries']['meta_info']
_meta_table['Correlator.RuleSetDetails.RuleSetDetail.Rules']['meta_info'].parent =_meta_table['Correlator.RuleSetDetails.RuleSetDetail']['meta_info']
_meta_table['Correlator.RuleSetDetails.RuleSetDetail']['meta_info'].parent =_meta_table['Correlator.RuleSetDetails']['meta_info']
_meta_table['Correlator.RuleDetails.RuleDetail.RuleSummary']['meta_info'].parent =_meta_table['Correlator.RuleDetails.RuleDetail']['meta_info']
_meta_table['Correlator.RuleDetails.RuleDetail.Codes']['meta_info'].parent =_meta_table['Correlator.RuleDetails.RuleDetail']['meta_info']
_meta_table['Correlator.RuleDetails.RuleDetail']['meta_info'].parent =_meta_table['Correlator.RuleDetails']['meta_info']
_meta_table['Correlator.RuleSummaries.RuleSummary']['meta_info'].parent =_meta_table['Correlator.RuleSummaries']['meta_info']
_meta_table['Correlator.Rules']['meta_info'].parent =_meta_table['Correlator']['meta_info']
_meta_table['Correlator.BufferStatus']['meta_info'].parent =_meta_table['Correlator']['meta_info']
_meta_table['Correlator.Alarms']['meta_info'].parent =_meta_table['Correlator']['meta_info']
_meta_table['Correlator.RuleSetSummaries']['meta_info'].parent =_meta_table['Correlator']['meta_info']
_meta_table['Correlator.RuleSetDetails']['meta_info'].parent =_meta_table['Correlator']['meta_info']
_meta_table['Correlator.RuleDetails']['meta_info'].parent =_meta_table['Correlator']['meta_info']
_meta_table['Correlator.RuleSummaries']['meta_info'].parent =_meta_table['Correlator']['meta_info']
