


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed',
            False, 
            [
            _MetaInfoClassMember('threshold-evaluation', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates the result of the most recent
                evaluation of the thresholD
                ''',
                'threshold_evaluation',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('threshold-notification-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether or not a notification should
                result, in case of threshold violation
                ''',
                'threshold_notification_enabled',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('threshold-relation', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates relation between sensor value and
                threshold
                ''',
                'threshold_relation',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('threshold-severity', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates minor, major, critical severities
                ''',
                'threshold_severity',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('threshold-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Value of the configured threshold
                ''',
                'threshold_value',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'value-detailed',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper'
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Threshold type
                ''',
                'type',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', True),
            _MetaInfoClassMember('trap', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold trap enable flag
                true-ENABLE, false-DISABLE
                ''',
                'trap',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('value-brief', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Threshold value for the sensor
                ''',
                'value_brief',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('value-detailed', REFERENCE_CLASS, 'ValueDetailed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed', 
                [], [], 
                '''                Detailed sensor threshold
                information
                ''',
                'value_detailed',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper'
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds',
            False, 
            [
            _MetaInfoClassMember('threshold', REFERENCE_LIST, 'Threshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold', 
                [], [], 
                '''                Types of thresholds
                ''',
                'threshold',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'thresholds',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper'
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed',
            False, 
            [
            _MetaInfoClassMember('age-time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Age of the sensor value; set to the current time
                if directly access the value from sensor
                ''',
                'age_time_stamp',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('alarm-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates threshold violation
                ''',
                'alarm_type',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('data-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sensor data type enums
                ''',
                'data_type',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('device-description', ATTRIBUTE, 'str' , None, None, 
                [(0, 50)], [], 
                '''                Device Name
                ''',
                'device_description',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Identifier for this device
                ''',
                'device_id',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('field-validity-bitmap', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sensor valid bitmap
                ''',
                'field_validity_bitmap',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('precision', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sensor precision range
                ''',
                'precision',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('scale', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sensor scale enums
                ''',
                'scale',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sensor operation state enums
                ''',
                'status',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('units', ATTRIBUTE, 'str' , None, None, 
                [(0, 50)], [], 
                '''                Units of variable being read
                ''',
                'units',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('update-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sensor value update rate;set to 0 if sensor
                value is updated and evaluated immediately
                ''',
                'update_rate',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current reading of sensor
                ''',
                'value',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'value-detailed',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper'
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Sensor name
                ''',
                'name',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', True),
            _MetaInfoClassMember('thresholds', REFERENCE_CLASS, 'Thresholds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds', 
                [], [], 
                '''                The threshold information
                ''',
                'thresholds',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('value-brief', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The sensor value
                ''',
                'value_brief',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('value-detailed', REFERENCE_CLASS, 'ValueDetailed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed', 
                [], [], 
                '''                Detailed sensor information including
                the sensor value
                ''',
                'value_detailed',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'sensor-name',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper'
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames',
            False, 
            [
            _MetaInfoClassMember('sensor-name', REFERENCE_LIST, 'SensorName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName', 
                [], [], 
                '''                Name of sensor
                ''',
                'sensor_name',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'sensor-names',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper'
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Sensor type
                ''',
                'type',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', True),
            _MetaInfoClassMember('sensor-names', REFERENCE_CLASS, 'SensorNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames', 
                [], [], 
                '''                Table of sensors
                ''',
                'sensor_names',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'sensor-type',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper'
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes',
            False, 
            [
            _MetaInfoClassMember('sensor-type', REFERENCE_LIST, 'SensorType' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType', 
                [], [], 
                '''                Type of sensor
                ''',
                'sensor_type',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'sensor-types',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper'
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag',
            False, 
            [
            _MetaInfoClassMember('power-accuracy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accuracy of the Power Value
                ''',
                'power_accuracy',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('power-admin-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Admin Status of the Unit
                ''',
                'power_admin_state',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('power-current-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current Type of the Unit
                ''',
                'power_current_type',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('power-max-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Max Power Value of the Unit
                ''',
                'power_max_value',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('power-measure-caliber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Measure Caliber
                ''',
                'power_measure_caliber',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('power-oper-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Oper Status of the Unit
                ''',
                'power_oper_state',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('power-origin', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Power Origin of the Unit
                ''',
                'power_origin',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('power-state-enter-reason', ATTRIBUTE, 'str' , None, None, 
                [(0, 50)], [], 
                '''                Enter Reason for the State
                ''',
                'power_state_enter_reason',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('power-unit-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unit Multiplier of Power
                ''',
                'power_unit_multiplier',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('power-value', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Current Power Value of the Unit
                ''',
                'power_value',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'power-bag',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper'
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power',
            False, 
            [
            _MetaInfoClassMember('power-bag', REFERENCE_CLASS, 'PowerBag' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag', 
                [], [], 
                '''                Detailed power bag information
                ''',
                'power_bag',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'power',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper'
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module',
            False, 
            [
            _MetaInfoClassMember('module', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Module name
                ''',
                'module',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', True),
            _MetaInfoClassMember('power', REFERENCE_CLASS, 'Power' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power', 
                [], [], 
                '''                Module Power Draw
                ''',
                'power',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            _MetaInfoClassMember('sensor-types', REFERENCE_CLASS, 'SensorTypes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes', 
                [], [], 
                '''                Table of sensor types
                ''',
                'sensor_types',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'module',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper'
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules',
            False, 
            [
            _MetaInfoClassMember('module', REFERENCE_LIST, 'Module' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module', 
                [], [], 
                '''                Name
                ''',
                'module',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'modules',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper'
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots.Slot' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots.Slot',
            False, 
            [
            _MetaInfoClassMember('slot', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Slot name
                ''',
                'slot',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', True),
            _MetaInfoClassMember('modules', REFERENCE_CLASS, 'Modules' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules', 
                [], [], 
                '''                Table of modules
                ''',
                'modules',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'slot',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper'
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack.Slots' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack.Slots',
            False, 
            [
            _MetaInfoClassMember('slot', REFERENCE_LIST, 'Slot' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots.Slot', 
                [], [], 
                '''                Name
                ''',
                'slot',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'slots',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper'
        ),
    },
    'EnvironmentalMonitoring.Racks.Rack' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks.Rack',
            False, 
            [
            _MetaInfoClassMember('rack', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Rack number
                ''',
                'rack',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', True),
            _MetaInfoClassMember('slots', REFERENCE_CLASS, 'Slots' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack.Slots', 
                [], [], 
                '''                Table of slots
                ''',
                'slots',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'rack',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper'
        ),
    },
    'EnvironmentalMonitoring.Racks' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring.Racks',
            False, 
            [
            _MetaInfoClassMember('rack', REFERENCE_LIST, 'Rack' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks.Rack', 
                [], [], 
                '''                Number
                ''',
                'rack',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'racks',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper'
        ),
    },
    'EnvironmentalMonitoring' : {
        'meta_info' : _MetaInfoClass('EnvironmentalMonitoring',
            False, 
            [
            _MetaInfoClassMember('racks', REFERENCE_CLASS, 'Racks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper', 'EnvironmentalMonitoring.Racks', 
                [], [], 
                '''                Table of racks
                ''',
                'racks',
                'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-sc-envmon-admin-oper',
            'environmental-monitoring',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-sc-envmon-admin-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_sc_envmon_admin_oper'
        ),
    },
}
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold.ValueDetailed']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds.Threshold']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.Thresholds']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName.ValueDetailed']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames.SensorName']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType.SensorNames']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes.SensorType']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power.PowerBag']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.SensorTypes']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module.Power']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules.Module']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot.Modules']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots.Slot']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack.Slots']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks.Rack']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks.Rack']['meta_info'].parent =_meta_table['EnvironmentalMonitoring.Racks']['meta_info']
_meta_table['EnvironmentalMonitoring.Racks']['meta_info'].parent =_meta_table['EnvironmentalMonitoring']['meta_info']
