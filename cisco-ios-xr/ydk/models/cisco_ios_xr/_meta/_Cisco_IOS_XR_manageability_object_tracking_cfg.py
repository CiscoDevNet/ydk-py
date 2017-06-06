


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'ObjectTrackings.ObjectTracking.TypeInterface' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeInterface',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'type-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues.ThresholdUpValue' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues.ThresholdUpValue',
            False, 
            [
            _MetaInfoClassMember('up', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Up value
                ''',
                'up',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', True),
            _MetaInfoClassMember('threshold-down', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold limit at which track is set to Down
                state
                ''',
                'threshold_down',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'threshold-up-value',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues',
            False, 
            [
            _MetaInfoClassMember('threshold-up-value', REFERENCE_LIST, 'ThresholdUpValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues.ThresholdUpValue', 
                [], [], 
                '''                Threshold limit at which track is set to UP
                state
                ''',
                'threshold_up_value',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'threshold-up-values',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits',
            False, 
            [
            _MetaInfoClassMember('threshold-up-values', REFERENCE_CLASS, 'ThresholdUpValues' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues', 
                [], [], 
                '''                Threshold limit at which track is set to UP
                state
                ''',
                'threshold_up_values',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'threshold-limits',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight',
            False, 
            [
            _MetaInfoClassMember('threshold-limits', REFERENCE_CLASS, 'ThresholdLimits' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits', 
                [], [], 
                '''                Threshold Limits
                ''',
                'threshold_limits',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'threshold-weight',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject.Object' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject.Object',
            False, 
            [
            _MetaInfoClassMember('object', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Object name
                ''',
                'object',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', True),
            _MetaInfoClassMember('object-weight', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Weight of object
                ''',
                'object_weight',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'object',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LIST, 'Object' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject.Object', 
                [], [], 
                '''                Track name object
                ''',
                'object',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'threshold-percentage-object',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues.ThresholdUpValue' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues.ThresholdUpValue',
            False, 
            [
            _MetaInfoClassMember('up', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Up value
                ''',
                'up',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', True),
            _MetaInfoClassMember('threshold-down', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold limit at which track is set to Down
                state
                ''',
                'threshold_down',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'threshold-up-value',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues',
            False, 
            [
            _MetaInfoClassMember('threshold-up-value', REFERENCE_LIST, 'ThresholdUpValue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues.ThresholdUpValue', 
                [], [], 
                '''                Threshold limit at which track is set to UP
                state
                ''',
                'threshold_up_value',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'threshold-up-values',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits',
            False, 
            [
            _MetaInfoClassMember('threshold-up-values', REFERENCE_CLASS, 'ThresholdUpValues' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues', 
                [], [], 
                '''                Threshold limit at which track is set to UP
                state
                ''',
                'threshold_up_values',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'threshold-limits',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage',
            False, 
            [
            _MetaInfoClassMember('threshold-limits', REFERENCE_CLASS, 'ThresholdLimits' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits', 
                [], [], 
                '''                Threshold Limits
                ''',
                'threshold_limits',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'threshold-percentage',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject.Object' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject.Object',
            False, 
            [
            _MetaInfoClassMember('object', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Object name
                ''',
                'object',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', True),
            _MetaInfoClassMember('object-weight', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Weight of object
                ''',
                'object_weight',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'object',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LIST, 'Object' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject.Object', 
                [], [], 
                '''                Track name object
                ''',
                'object',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'threshold-weight-object',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeList' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeList',
            False, 
            [
            _MetaInfoClassMember('threshold-percentage', REFERENCE_CLASS, 'ThresholdPercentage' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage', 
                [], [], 
                '''                Track type threshold percentage
                ''',
                'threshold_percentage',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            _MetaInfoClassMember('threshold-percentage-object', REFERENCE_CLASS, 'ThresholdPercentageObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject', 
                [], [], 
                '''                Track type threshold percentage
                ''',
                'threshold_percentage_object',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            _MetaInfoClassMember('threshold-weight', REFERENCE_CLASS, 'ThresholdWeight' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight', 
                [], [], 
                '''                Track type threshold weight
                ''',
                'threshold_weight',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            _MetaInfoClassMember('threshold-weight-object', REFERENCE_CLASS, 'ThresholdWeightObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject', 
                [], [], 
                '''                Track type threshold weight
                ''',
                'threshold_weight_object',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'type-list',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeRoute.IpAddress' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeRoute.IpAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            _MetaInfoClassMember('mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Mask
                ''',
                'mask',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'ip-address',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeRoute' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeRoute',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_CLASS, 'IpAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeRoute.IpAddress', 
                [], [], 
                '''                set track IPv4 address
                ''',
                'ip_address',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF tag - use 'default' for the DEFAULT vrf
                ''',
                'vrf',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'type-route',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects.OrObject' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects.OrObject',
            False, 
            [
            _MetaInfoClassMember('object', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Object name
                ''',
                'object',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', True),
            _MetaInfoClassMember('object-sign', REFERENCE_ENUM_CLASS, 'ObjectTrackingBooleanSignEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_datatypes', 'ObjectTrackingBooleanSignEnum', 
                [], [], 
                '''                Tracked Object sign (with or without not)
                ''',
                'object_sign',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'or-object',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects',
            False, 
            [
            _MetaInfoClassMember('or-object', REFERENCE_LIST, 'OrObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects.OrObject', 
                [], [], 
                '''                Track name - maximum 32 characters
                ''',
                'or_object',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'or-objects',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects.AndObject' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects.AndObject',
            False, 
            [
            _MetaInfoClassMember('object-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Object name
                ''',
                'object_name',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', True),
            _MetaInfoClassMember('object-sign', REFERENCE_ENUM_CLASS, 'ObjectTrackingBooleanSignEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_datatypes', 'ObjectTrackingBooleanSignEnum', 
                [], [], 
                '''                Tracked Object sign (with or without not)
                ''',
                'object_sign',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'and-object',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects',
            False, 
            [
            _MetaInfoClassMember('and-object', REFERENCE_LIST, 'AndObject' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects.AndObject', 
                [], [], 
                '''                Track name - maximum 32 characters
                ''',
                'and_object',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'and-objects',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking.TypeBooleanList' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking.TypeBooleanList',
            False, 
            [
            _MetaInfoClassMember('and-objects', REFERENCE_CLASS, 'AndObjects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects', 
                [], [], 
                '''                Track type boolean and list
                ''',
                'and_objects',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            _MetaInfoClassMember('or-objects', REFERENCE_CLASS, 'OrObjects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects', 
                [], [], 
                '''                Track type boolean or list
                ''',
                'or_objects',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'type-boolean-list',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings.ObjectTracking' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings.ObjectTracking',
            False, 
            [
            _MetaInfoClassMember('track-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Track name
                ''',
                'track_name',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', True),
            _MetaInfoClassMember('delay-down', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Track delay down time
                ''',
                'delay_down',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            _MetaInfoClassMember('delay-up', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Delay up in seconds
                ''',
                'delay_up',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable the Track
                ''',
                'enable',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            _MetaInfoClassMember('type-boolean-list', REFERENCE_CLASS, 'TypeBooleanList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeBooleanList', 
                [], [], 
                '''                Track type boolean list
                ''',
                'type_boolean_list',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            _MetaInfoClassMember('type-boolean-list-and-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable track type boolean list and
                ''',
                'type_boolean_list_and_enable',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            _MetaInfoClassMember('type-boolean-list-or-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable track type boolean list or
                ''',
                'type_boolean_list_or_enable',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            _MetaInfoClassMember('type-interface', REFERENCE_CLASS, 'TypeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeInterface', 
                [], [], 
                '''                Track type line-protocol
                ''',
                'type_interface',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            _MetaInfoClassMember('type-interface-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable track type Interface
                ''',
                'type_interface_enable',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            _MetaInfoClassMember('type-list', REFERENCE_CLASS, 'TypeList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeList', 
                [], [], 
                '''                Track type boolean list
                ''',
                'type_list',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            _MetaInfoClassMember('type-route', REFERENCE_CLASS, 'TypeRoute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking.TypeRoute', 
                [], [], 
                '''                Track type route ipv4
                ''',
                'type_route',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            _MetaInfoClassMember('type-route-enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable track type Route
                ''',
                'type_route_enable',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'object-tracking',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
    'ObjectTrackings' : {
        'meta_info' : _MetaInfoClass('ObjectTrackings',
            False, 
            [
            _MetaInfoClassMember('object-tracking', REFERENCE_LIST, 'ObjectTracking' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg', 'ObjectTrackings.ObjectTracking', 
                [], [], 
                '''                Track name - maximum 32 characters
                ''',
                'object_tracking',
                'Cisco-IOS-XR-manageability-object-tracking-cfg', False),
            ],
            'Cisco-IOS-XR-manageability-object-tracking-cfg',
            'object-trackings',
            _yang_ns._namespaces['Cisco-IOS-XR-manageability-object-tracking-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_manageability_object_tracking_cfg'
        ),
    },
}
_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues.ThresholdUpValue']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits.ThresholdUpValues']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight.ThresholdLimits']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject.Object']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues.ThresholdUpValue']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits.ThresholdUpValues']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage.ThresholdLimits']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject.Object']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdWeight']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking.TypeList']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentageObject']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking.TypeList']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdPercentage']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking.TypeList']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeList.ThresholdWeightObject']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking.TypeList']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeRoute.IpAddress']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking.TypeRoute']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects.OrObject']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects.AndObject']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeBooleanList.OrObjects']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking.TypeBooleanList']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeBooleanList.AndObjects']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking.TypeBooleanList']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeInterface']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeList']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeRoute']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking.TypeBooleanList']['meta_info'].parent =_meta_table['ObjectTrackings.ObjectTracking']['meta_info']
_meta_table['ObjectTrackings.ObjectTracking']['meta_info'].parent =_meta_table['ObjectTrackings']['meta_info']
