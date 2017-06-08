


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'MinRateIdentity' : {
        'meta_info' : _MetaInfoClass('MinRateIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'min-rate',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterReferenceIdentity' : {
        'meta_info' : _MetaInfoClass('MeterReferenceIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'meter-reference',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MaxRateIdentity' : {
        'meta_info' : _MetaInfoClass('MaxRateIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'max-rate',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'ChildPolicyIdentity' : {
        'meta_info' : _MetaInfoClass('ChildPolicyIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'child-policy',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterInlineIdentity' : {
        'meta_info' : _MetaInfoClass('MeterInlineIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'meter-inline',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'RateUnitTypeIdentity' : {
        'meta_info' : _MetaInfoClass('RateUnitTypeIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'rate-unit-type',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'DscpMarkingIdentity' : {
        'meta_info' : _MetaInfoClass('DscpMarkingIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'dscp-marking',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'DropTypeIdentity' : {
        'meta_info' : _MetaInfoClass('DropTypeIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'drop-type',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterActionTypeIdentity' : {
        'meta_info' : _MetaInfoClass('MeterActionTypeIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'meter-action-type',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'SchedularIdentity' : {
        'meta_info' : _MetaInfoClass('SchedularIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'schedular',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'CountIdentity' : {
        'meta_info' : _MetaInfoClass('CountIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'count',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTypeIdentity' : {
        'meta_info' : _MetaInfoClass('MeterTypeIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'meter-type',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'QueueIdentity' : {
        'meta_info' : _MetaInfoClass('QueueIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'queue',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'DiscardIdentity' : {
        'meta_info' : _MetaInfoClass('DiscardIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'discard',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.OneRateTwoColorMeter.ConformAction.MeterActionParams' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.OneRateTwoColorMeter.ConformAction.MeterActionParams',
            False, 
            [
            _MetaInfoClassMember('meter-action-type', REFERENCE_IDENTITY_CLASS, 'MeterActionTypeIdentity' , 'ydk.models.ietf.ietf_qos_action', 'MeterActionTypeIdentity', 
                [], [], 
                '''                meter action type
                ''',
                'meter_action_type',
                'ietf-qos-action', True),
            ],
            'ietf-qos-action',
            'meter-action-params',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.OneRateTwoColorMeter.ConformAction' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.OneRateTwoColorMeter.ConformAction',
            False, 
            [
            _MetaInfoClassMember('meter-action-params', REFERENCE_LIST, 'MeterActionParams' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.OneRateTwoColorMeter.ConformAction.MeterActionParams', 
                [], [], 
                '''                Configuration of basic-meter & associated actions
                ''',
                'meter_action_params',
                'ietf-qos-action', False),
            ],
            'ietf-qos-action',
            'conform-action',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.OneRateTwoColorMeter.ExceedAction.MeterActionParams' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.OneRateTwoColorMeter.ExceedAction.MeterActionParams',
            False, 
            [
            _MetaInfoClassMember('meter-action-type', REFERENCE_IDENTITY_CLASS, 'MeterActionTypeIdentity' , 'ydk.models.ietf.ietf_qos_action', 'MeterActionTypeIdentity', 
                [], [], 
                '''                meter action type
                ''',
                'meter_action_type',
                'ietf-qos-action', True),
            ],
            'ietf-qos-action',
            'meter-action-params',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.OneRateTwoColorMeter.ExceedAction' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.OneRateTwoColorMeter.ExceedAction',
            False, 
            [
            _MetaInfoClassMember('meter-action-params', REFERENCE_LIST, 'MeterActionParams' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.OneRateTwoColorMeter.ExceedAction.MeterActionParams', 
                [], [], 
                '''                Configuration of basic-meter & associated actions
                ''',
                'meter_action_params',
                'ietf-qos-action', False),
            ],
            'ietf-qos-action',
            'exceed-action',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.OneRateTwoColorMeter' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.OneRateTwoColorMeter',
            False, 
            [
            _MetaInfoClassMember('conform-action', REFERENCE_CLASS, 'ConformAction' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.OneRateTwoColorMeter.ConformAction', 
                [], [], 
                '''                conform action
                ''',
                'conform_action',
                'ietf-qos-action', False),
            _MetaInfoClassMember('exceed-action', REFERENCE_CLASS, 'ExceedAction' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.OneRateTwoColorMeter.ExceedAction', 
                [], [], 
                '''                exceed action
                ''',
                'exceed_action',
                'ietf-qos-action', False),
            _MetaInfoClassMember('meter-burst', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                burst size
                ''',
                'meter_burst',
                'ietf-qos-action', False),
            _MetaInfoClassMember('meter-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                meter rate
                ''',
                'meter_rate',
                'ietf-qos-action', False),
            ],
            'ietf-qos-action',
            'one-rate-two-color-meter',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.OneRateTriColorMeter.ConformAction.MeterActionParams' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.OneRateTriColorMeter.ConformAction.MeterActionParams',
            False, 
            [
            _MetaInfoClassMember('meter-action-type', REFERENCE_IDENTITY_CLASS, 'MeterActionTypeIdentity' , 'ydk.models.ietf.ietf_qos_action', 'MeterActionTypeIdentity', 
                [], [], 
                '''                meter action type
                ''',
                'meter_action_type',
                'ietf-qos-action', True),
            ],
            'ietf-qos-action',
            'meter-action-params',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.OneRateTriColorMeter.ConformAction' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.OneRateTriColorMeter.ConformAction',
            False, 
            [
            _MetaInfoClassMember('meter-action-params', REFERENCE_LIST, 'MeterActionParams' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.OneRateTriColorMeter.ConformAction.MeterActionParams', 
                [], [], 
                '''                Configuration of basic-meter & associated actions
                ''',
                'meter_action_params',
                'ietf-qos-action', False),
            ],
            'ietf-qos-action',
            'conform-action',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.OneRateTriColorMeter.ExceedAction.MeterActionParams' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.OneRateTriColorMeter.ExceedAction.MeterActionParams',
            False, 
            [
            _MetaInfoClassMember('meter-action-type', REFERENCE_IDENTITY_CLASS, 'MeterActionTypeIdentity' , 'ydk.models.ietf.ietf_qos_action', 'MeterActionTypeIdentity', 
                [], [], 
                '''                meter action type
                ''',
                'meter_action_type',
                'ietf-qos-action', True),
            ],
            'ietf-qos-action',
            'meter-action-params',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.OneRateTriColorMeter.ExceedAction' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.OneRateTriColorMeter.ExceedAction',
            False, 
            [
            _MetaInfoClassMember('meter-action-params', REFERENCE_LIST, 'MeterActionParams' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.OneRateTriColorMeter.ExceedAction.MeterActionParams', 
                [], [], 
                '''                Configuration of basic-meter & associated actions
                ''',
                'meter_action_params',
                'ietf-qos-action', False),
            ],
            'ietf-qos-action',
            'exceed-action',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.OneRateTriColorMeter.ViolateAction.MeterActionParams' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.OneRateTriColorMeter.ViolateAction.MeterActionParams',
            False, 
            [
            _MetaInfoClassMember('meter-action-type', REFERENCE_IDENTITY_CLASS, 'MeterActionTypeIdentity' , 'ydk.models.ietf.ietf_qos_action', 'MeterActionTypeIdentity', 
                [], [], 
                '''                meter action type
                ''',
                'meter_action_type',
                'ietf-qos-action', True),
            ],
            'ietf-qos-action',
            'meter-action-params',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.OneRateTriColorMeter.ViolateAction' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.OneRateTriColorMeter.ViolateAction',
            False, 
            [
            _MetaInfoClassMember('meter-action-params', REFERENCE_LIST, 'MeterActionParams' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.OneRateTriColorMeter.ViolateAction.MeterActionParams', 
                [], [], 
                '''                Configuration of basic-meter & associated actions
                ''',
                'meter_action_params',
                'ietf-qos-action', False),
            ],
            'ietf-qos-action',
            'violate-action',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.OneRateTriColorMeter' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.OneRateTriColorMeter',
            False, 
            [
            _MetaInfoClassMember('committed-burst', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                commited burst size
                ''',
                'committed_burst',
                'ietf-qos-action', False),
            _MetaInfoClassMember('committed-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                meter rate
                ''',
                'committed_rate',
                'ietf-qos-action', False),
            _MetaInfoClassMember('conform-action', REFERENCE_CLASS, 'ConformAction' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.OneRateTriColorMeter.ConformAction', 
                [], [], 
                '''                conform, or green action
                ''',
                'conform_action',
                'ietf-qos-action', False),
            _MetaInfoClassMember('exceed-action', REFERENCE_CLASS, 'ExceedAction' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.OneRateTriColorMeter.ExceedAction', 
                [], [], 
                '''                exceed, or yellow action
                ''',
                'exceed_action',
                'ietf-qos-action', False),
            _MetaInfoClassMember('excess-burst', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                excess burst size
                ''',
                'excess_burst',
                'ietf-qos-action', False),
            _MetaInfoClassMember('violate-action', REFERENCE_CLASS, 'ViolateAction' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.OneRateTriColorMeter.ViolateAction', 
                [], [], 
                '''                violate, or red action
                ''',
                'violate_action',
                'ietf-qos-action', False),
            ],
            'ietf-qos-action',
            'one-rate-tri-color-meter',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.TwoRateTriColorMeter.ConformAction.MeterActionParams' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.TwoRateTriColorMeter.ConformAction.MeterActionParams',
            False, 
            [
            _MetaInfoClassMember('meter-action-type', REFERENCE_IDENTITY_CLASS, 'MeterActionTypeIdentity' , 'ydk.models.ietf.ietf_qos_action', 'MeterActionTypeIdentity', 
                [], [], 
                '''                meter action type
                ''',
                'meter_action_type',
                'ietf-qos-action', True),
            ],
            'ietf-qos-action',
            'meter-action-params',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.TwoRateTriColorMeter.ConformAction' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.TwoRateTriColorMeter.ConformAction',
            False, 
            [
            _MetaInfoClassMember('meter-action-params', REFERENCE_LIST, 'MeterActionParams' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.TwoRateTriColorMeter.ConformAction.MeterActionParams', 
                [], [], 
                '''                Configuration of basic-meter & associated actions
                ''',
                'meter_action_params',
                'ietf-qos-action', False),
            ],
            'ietf-qos-action',
            'conform-action',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.TwoRateTriColorMeter.ExceedAction.MeterActionParams' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.TwoRateTriColorMeter.ExceedAction.MeterActionParams',
            False, 
            [
            _MetaInfoClassMember('meter-action-type', REFERENCE_IDENTITY_CLASS, 'MeterActionTypeIdentity' , 'ydk.models.ietf.ietf_qos_action', 'MeterActionTypeIdentity', 
                [], [], 
                '''                meter action type
                ''',
                'meter_action_type',
                'ietf-qos-action', True),
            ],
            'ietf-qos-action',
            'meter-action-params',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.TwoRateTriColorMeter.ExceedAction' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.TwoRateTriColorMeter.ExceedAction',
            False, 
            [
            _MetaInfoClassMember('meter-action-params', REFERENCE_LIST, 'MeterActionParams' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.TwoRateTriColorMeter.ExceedAction.MeterActionParams', 
                [], [], 
                '''                Configuration of basic-meter & associated actions
                ''',
                'meter_action_params',
                'ietf-qos-action', False),
            ],
            'ietf-qos-action',
            'exceed-action',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.TwoRateTriColorMeter.ViolateAction.MeterActionParams' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.TwoRateTriColorMeter.ViolateAction.MeterActionParams',
            False, 
            [
            _MetaInfoClassMember('meter-action-type', REFERENCE_IDENTITY_CLASS, 'MeterActionTypeIdentity' , 'ydk.models.ietf.ietf_qos_action', 'MeterActionTypeIdentity', 
                [], [], 
                '''                meter action type
                ''',
                'meter_action_type',
                'ietf-qos-action', True),
            ],
            'ietf-qos-action',
            'meter-action-params',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.TwoRateTriColorMeter.ViolateAction' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.TwoRateTriColorMeter.ViolateAction',
            False, 
            [
            _MetaInfoClassMember('meter-action-params', REFERENCE_LIST, 'MeterActionParams' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.TwoRateTriColorMeter.ViolateAction.MeterActionParams', 
                [], [], 
                '''                Configuration of basic-meter & associated actions
                ''',
                'meter_action_params',
                'ietf-qos-action', False),
            ],
            'ietf-qos-action',
            'violate-action',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry.TwoRateTriColorMeter' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry.TwoRateTriColorMeter',
            False, 
            [
            _MetaInfoClassMember('committed-burst', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                commited burst size
                ''',
                'committed_burst',
                'ietf-qos-action', False),
            _MetaInfoClassMember('committed-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                meter rate
                ''',
                'committed_rate',
                'ietf-qos-action', False),
            _MetaInfoClassMember('conform-action', REFERENCE_CLASS, 'ConformAction' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.TwoRateTriColorMeter.ConformAction', 
                [], [], 
                '''                conform, or green action
                ''',
                'conform_action',
                'ietf-qos-action', False),
            _MetaInfoClassMember('exceed-action', REFERENCE_CLASS, 'ExceedAction' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.TwoRateTriColorMeter.ExceedAction', 
                [], [], 
                '''                exceed, or yellow action
                ''',
                'exceed_action',
                'ietf-qos-action', False),
            _MetaInfoClassMember('peak-burst', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                commited burst size
                ''',
                'peak_burst',
                'ietf-qos-action', False),
            _MetaInfoClassMember('peak-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                meter rate
                ''',
                'peak_rate',
                'ietf-qos-action', False),
            _MetaInfoClassMember('violate-action', REFERENCE_CLASS, 'ViolateAction' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.TwoRateTriColorMeter.ViolateAction', 
                [], [], 
                '''                exceed, or red action
                ''',
                'violate_action',
                'ietf-qos-action', False),
            ],
            'ietf-qos-action',
            'two-rate-tri-color-meter',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate.MeterEntry' : {
        'meta_info' : _MetaInfoClass('MeterTemplate.MeterEntry',
            False, 
            [
            _MetaInfoClassMember('meter-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                meter identifier
                ''',
                'meter_name',
                'ietf-qos-action', True),
            _MetaInfoClassMember('one-rate-tri-color-meter', REFERENCE_CLASS, 'OneRateTriColorMeter' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.OneRateTriColorMeter', 
                [], [], 
                '''                single rate three color meter
                ''',
                'one_rate_tri_color_meter',
                'ietf-qos-action', False),
            _MetaInfoClassMember('one-rate-two-color-meter', REFERENCE_CLASS, 'OneRateTwoColorMeter' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.OneRateTwoColorMeter', 
                [], [], 
                '''                single rate two color marker meter
                ''',
                'one_rate_two_color_meter',
                'ietf-qos-action', False),
            _MetaInfoClassMember('two-rate-tri-color-meter', REFERENCE_CLASS, 'TwoRateTriColorMeter' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry.TwoRateTriColorMeter', 
                [], [], 
                '''                two rate three color meter
                ''',
                'two_rate_tri_color_meter',
                'ietf-qos-action', False),
            ],
            'ietf-qos-action',
            'meter-entry',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterTemplate' : {
        'meta_info' : _MetaInfoClass('MeterTemplate',
            False, 
            [
            _MetaInfoClassMember('meter-entry', REFERENCE_LIST, 'MeterEntry' , 'ydk.models.ietf.ietf_qos_action', 'MeterTemplate.MeterEntry', 
                [], [], 
                '''                meter entry template
                ''',
                'meter_entry',
                'ietf-qos-action', False),
            ],
            'ietf-qos-action',
            'meter-template',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'KiloBitsPerSecondIdentity' : {
        'meta_info' : _MetaInfoClass('KiloBitsPerSecondIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'kilo-bits-per-second',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'TailDropIdentity' : {
        'meta_info' : _MetaInfoClass('TailDropIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'tail-drop',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterActionMarkDscpIdentity' : {
        'meta_info' : _MetaInfoClass('MeterActionMarkDscpIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'meter-action-mark-dscp',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'OneRateTwoColorMeterTypeIdentity' : {
        'meta_info' : _MetaInfoClass('OneRateTwoColorMeterTypeIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'one-rate-two-color-meter-type',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'GigaBitsPerSecondIdentity' : {
        'meta_info' : _MetaInfoClass('GigaBitsPerSecondIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'giga-bits-per-second',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MeterActionDropIdentity' : {
        'meta_info' : _MetaInfoClass('MeterActionDropIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'meter-action-drop',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'PercentIdentity' : {
        'meta_info' : _MetaInfoClass('PercentIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'percent',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'TwoRateTriColorMeterTypeIdentity' : {
        'meta_info' : _MetaInfoClass('TwoRateTriColorMeterTypeIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'two-rate-tri-color-meter-type',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'BitsPerSecondIdentity' : {
        'meta_info' : _MetaInfoClass('BitsPerSecondIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'bits-per-second',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'OneRateTriColorMeterTypeIdentity' : {
        'meta_info' : _MetaInfoClass('OneRateTriColorMeterTypeIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'one-rate-tri-color-meter-type',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'MegaBitsPerSecondIdentity' : {
        'meta_info' : _MetaInfoClass('MegaBitsPerSecondIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'mega-bits-per-second',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
    'RandomDetectIdentity' : {
        'meta_info' : _MetaInfoClass('RandomDetectIdentity',
            False, 
            [
            ],
            'ietf-qos-action',
            'random-detect',
            _yang_ns._namespaces['ietf-qos-action'],
        'ydk.models.ietf.ietf_qos_action'
        ),
    },
}
_meta_table['MeterTemplate.MeterEntry.OneRateTwoColorMeter.ConformAction.MeterActionParams']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry.OneRateTwoColorMeter.ConformAction']['meta_info']
_meta_table['MeterTemplate.MeterEntry.OneRateTwoColorMeter.ExceedAction.MeterActionParams']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry.OneRateTwoColorMeter.ExceedAction']['meta_info']
_meta_table['MeterTemplate.MeterEntry.OneRateTwoColorMeter.ConformAction']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry.OneRateTwoColorMeter']['meta_info']
_meta_table['MeterTemplate.MeterEntry.OneRateTwoColorMeter.ExceedAction']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry.OneRateTwoColorMeter']['meta_info']
_meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter.ConformAction.MeterActionParams']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter.ConformAction']['meta_info']
_meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter.ExceedAction.MeterActionParams']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter.ExceedAction']['meta_info']
_meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter.ViolateAction.MeterActionParams']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter.ViolateAction']['meta_info']
_meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter.ConformAction']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter']['meta_info']
_meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter.ExceedAction']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter']['meta_info']
_meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter.ViolateAction']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter']['meta_info']
_meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter.ConformAction.MeterActionParams']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter.ConformAction']['meta_info']
_meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter.ExceedAction.MeterActionParams']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter.ExceedAction']['meta_info']
_meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter.ViolateAction.MeterActionParams']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter.ViolateAction']['meta_info']
_meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter.ConformAction']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter']['meta_info']
_meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter.ExceedAction']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter']['meta_info']
_meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter.ViolateAction']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter']['meta_info']
_meta_table['MeterTemplate.MeterEntry.OneRateTwoColorMeter']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry']['meta_info']
_meta_table['MeterTemplate.MeterEntry.OneRateTriColorMeter']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry']['meta_info']
_meta_table['MeterTemplate.MeterEntry.TwoRateTriColorMeter']['meta_info'].parent =_meta_table['MeterTemplate.MeterEntry']['meta_info']
_meta_table['MeterTemplate.MeterEntry']['meta_info'].parent =_meta_table['MeterTemplate']['meta_info']
