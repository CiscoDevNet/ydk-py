


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'G709PrbsIntervalEnum' : _MetaInfoEnum('G709PrbsIntervalEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper',
        {
            'current-interval':'current_interval',
            'previous-interval':'previous_interval',
            'previous-interval2':'previous_interval2',
            'previous-interval3':'previous_interval3',
            'previous-interval4':'previous_interval4',
            'previous-interval5':'previous_interval5',
            'previous-interval6':'previous_interval6',
            'previous-interval7':'previous_interval7',
            'previous-interval8':'previous_interval8',
            'previous-interval9':'previous_interval9',
            'previous-interval10':'previous_interval10',
            'previous-interval11':'previous_interval11',
            'previous-interval12':'previous_interval12',
            'previous-interval13':'previous_interval13',
            'previous-interval14':'previous_interval14',
            'previous-interval15':'previous_interval15',
            'previous-interval16':'previous_interval16',
            'previous-interval17':'previous_interval17',
            'previous-interval18':'previous_interval18',
            'previous-interval19':'previous_interval19',
            'previous-interval20':'previous_interval20',
            'previous-interval21':'previous_interval21',
            'previous-interval22':'previous_interval22',
            'previous-interval23':'previous_interval23',
            'previous-interval24':'previous_interval24',
            'previous-interval25':'previous_interval25',
            'previous-interval26':'previous_interval26',
            'previous-interval27':'previous_interval27',
            'previous-interval28':'previous_interval28',
            'previous-interval29':'previous_interval29',
            'previous-interval30':'previous_interval30',
            'previous-interval31':'previous_interval31',
            'previous-interval32':'previous_interval32',
        }, 'Cisco-IOS-XR-dwdm-ui-oper', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper']),
    'G709PrbsModeEnum' : _MetaInfoEnum('G709PrbsModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper',
        {
            'mode-source':'mode_source',
            'mode-sink':'mode_sink',
            'mode-source-sink':'mode_source_sink',
            'mode-invalid':'mode_invalid',
        }, 'Cisco-IOS-XR-dwdm-ui-oper', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper']),
    'DwdmtasStateEnum' : _MetaInfoEnum('DwdmtasStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper',
        {
            'tas-oos':'tas_oos',
            'tas-is':'tas_is',
            'tas-oos-mt':'tas_oos_mt',
            'tas-is-cfg':'tas_is_cfg',
        }, 'Cisco-IOS-XR-dwdm-ui-oper', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper']),
    'G709PpfsmModeEnum' : _MetaInfoEnum('G709PpfsmModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper',
        {
            'pp-disable':'pp_disable',
            'pp-default-mode':'pp_default_mode',
            'pp-graceful-mode':'pp_graceful_mode',
        }, 'Cisco-IOS-XR-dwdm-ui-oper', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper']),
    'DwdmControllerStateEnum' : _MetaInfoEnum('DwdmControllerStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper',
        {
            'dwdm-ui-state-up':'dwdm_ui_state_up',
            'dwdm-ui-state-down':'dwdm_ui_state_down',
            'dwdm-ui-state-admin-down':'dwdm_ui_state_admin_down',
        }, 'Cisco-IOS-XR-dwdm-ui-oper', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper']),
    'G709PrbsPatternEnum' : _MetaInfoEnum('G709PrbsPatternEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper',
        {
            'pattern-none':'pattern_none',
            'pattern-null':'pattern_null',
            'pattern-pn11':'pattern_pn11',
            'pattern-pn23':'pattern_pn23',
            'pattern-pn31':'pattern_pn31',
        }, 'Cisco-IOS-XR-dwdm-ui-oper', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper']),
    'G709ApsByteEnum' : _MetaInfoEnum('G709ApsByteEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper',
        {
            'pp-no-protect':'pp_no_protect',
            'pp-no-request':'pp_no_request',
            'pp-regen-degrade':'pp_regen_degrade',
            'pp-sig-degrade':'pp_sig_degrade',
            'pp-remote-main':'pp_remote_main',
            'pp-aps-unknown':'pp_aps_unknown',
        }, 'Cisco-IOS-XR-dwdm-ui-oper', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper']),
    'G709EfecModeEnum' : _MetaInfoEnum('G709EfecModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper',
        {
            'g975-none':'g975_none',
            'g975-1-i4':'g975_1_i4',
            'g975-1-i7':'g975_1_i7',
        }, 'Cisco-IOS-XR-dwdm-ui-oper', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper']),
    'DwdmWaveChannelOwnerEnum' : _MetaInfoEnum('DwdmWaveChannelOwnerEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper',
        {
            'default':'default',
            'configuration':'configuration',
            'gmpls':'gmpls',
        }, 'Cisco-IOS-XR-dwdm-ui-oper', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper']),
    'G709PpintfStateEnum' : _MetaInfoEnum('G709PpintfStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper',
        {
            'pp-intf-up':'pp_intf_up',
            'pp-intf-failing':'pp_intf_failing',
            'pp-intf-down':'pp_intf_down',
        }, 'Cisco-IOS-XR-dwdm-ui-oper', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper']),
    'G709PpfsmStateEnum' : _MetaInfoEnum('G709PpfsmStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper',
        {
            'in-active':'in_active',
            'disabled':'disabled',
            'normal-state':'normal_state',
            'local-failing':'local_failing',
            'remote-failing':'remote_failing',
            'main-t-failing':'main_t_failing',
            'regen-failing':'regen_failing',
            'local-failed':'local_failed',
            'remote-failed':'remote_failed',
            'main-t-failed':'main_t_failed',
            'regen-failed':'regen_failed',
        }, 'Cisco-IOS-XR-dwdm-ui-oper', _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper']),
    'Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics.PrbsEntry' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics.PrbsEntry',
            False, 
            [
            _MetaInfoClassMember('bit-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bit Error Count
                ''',
                'bit_error_count',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('configured-pattern', REFERENCE_ENUM_CLASS, 'G709PrbsPatternEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709PrbsPatternEnum', 
                [], [], 
                '''                Configured pattern of PRBS test
                ''',
                'configured_pattern',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('found-at', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Pattern first found at timestamp
                ''',
                'found_at',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('found-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Count of pattern found in interval
                ''',
                'found_count',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('interval-index', REFERENCE_ENUM_CLASS, 'G709PrbsIntervalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709PrbsIntervalEnum', 
                [], [], 
                '''                Index of bucket, current and previous
                ''',
                'interval_index',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('lost-at', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Pattern first lost at timestamp
                ''',
                'lost_at',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('lost-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Count of pattern lost in interval
                ''',
                'lost_count',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('received-pattern', REFERENCE_ENUM_CLASS, 'G709PrbsPatternEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709PrbsPatternEnum', 
                [], [], 
                '''                Received Pattern of PRBS Test
                ''',
                'received_pattern',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('start-at', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Interval start timestamp
                ''',
                'start_at',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('stop-at', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Interval stop timestamp
                ''',
                'stop_at',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'prbs-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics',
            False, 
            [
            _MetaInfoClassMember('is-prbs-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                'True' if PRBS is enabled 'False' otherwise
                ''',
                'is_prbs_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('prbs-config-mode', REFERENCE_ENUM_CLASS, 'G709PrbsModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709PrbsModeEnum', 
                [], [], 
                '''                Configured mode of PRBS test
                ''',
                'prbs_config_mode',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('prbs-entry', REFERENCE_LIST, 'PrbsEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics.PrbsEntry', 
                [], [], 
                '''                History consists of 15-minute/24-hour intervals
                ''',
                'prbs_entry',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'twenty-four-hours-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket',
            False, 
            [
            _MetaInfoClassMember('twenty-four-hours-statistics', REFERENCE_CLASS, 'TwentyFourHoursStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics', 
                [], [], 
                '''                Port 24-hour PRBS statistics data
                ''',
                'twenty_four_hours_statistics',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'twenty-four-hours-bucket',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics.PrbsEntry' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics.PrbsEntry',
            False, 
            [
            _MetaInfoClassMember('bit-error-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bit Error Count
                ''',
                'bit_error_count',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('configured-pattern', REFERENCE_ENUM_CLASS, 'G709PrbsPatternEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709PrbsPatternEnum', 
                [], [], 
                '''                Configured pattern of PRBS test
                ''',
                'configured_pattern',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('found-at', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Pattern first found at timestamp
                ''',
                'found_at',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('found-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Count of pattern found in interval
                ''',
                'found_count',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('interval-index', REFERENCE_ENUM_CLASS, 'G709PrbsIntervalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709PrbsIntervalEnum', 
                [], [], 
                '''                Index of bucket, current and previous
                ''',
                'interval_index',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('lost-at', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Pattern first lost at timestamp
                ''',
                'lost_at',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('lost-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Count of pattern lost in interval
                ''',
                'lost_count',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('received-pattern', REFERENCE_ENUM_CLASS, 'G709PrbsPatternEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709PrbsPatternEnum', 
                [], [], 
                '''                Received Pattern of PRBS Test
                ''',
                'received_pattern',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('start-at', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Interval start timestamp
                ''',
                'start_at',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('stop-at', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Interval stop timestamp
                ''',
                'stop_at',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'prbs-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics',
            False, 
            [
            _MetaInfoClassMember('is-prbs-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                'True' if PRBS is enabled 'False' otherwise
                ''',
                'is_prbs_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('prbs-config-mode', REFERENCE_ENUM_CLASS, 'G709PrbsModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709PrbsModeEnum', 
                [], [], 
                '''                Configured mode of PRBS test
                ''',
                'prbs_config_mode',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('prbs-entry', REFERENCE_LIST, 'PrbsEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics.PrbsEntry', 
                [], [], 
                '''                History consists of 15-minute/24-hour intervals
                ''',
                'prbs_entry',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'fifteen-minutes-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Prbs.FifteenMinutesBucket' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Prbs.FifteenMinutesBucket',
            False, 
            [
            _MetaInfoClassMember('fifteen-minutes-statistics', REFERENCE_CLASS, 'FifteenMinutesStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics', 
                [], [], 
                '''                Port 15-minute PRBS statistics data
                ''',
                'fifteen_minutes_statistics',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'fifteen-minutes-bucket',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Prbs' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Prbs',
            False, 
            [
            _MetaInfoClassMember('fifteen-minutes-bucket', REFERENCE_CLASS, 'FifteenMinutesBucket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Prbs.FifteenMinutesBucket', 
                [], [], 
                '''                Port 15-minute PRBS statistics table
                ''',
                'fifteen_minutes_bucket',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('twenty-four-hours-bucket', REFERENCE_CLASS, 'TwentyFourHoursBucket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket', 
                [], [], 
                '''                Port 24-hour PRBS statistics table
                ''',
                'twenty_four_hours_bucket',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'prbs',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Optics.WaveInfo' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Optics.WaveInfo',
            False, 
            [
            _MetaInfoClassMember('wave-band', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Wavelength band
                ''',
                'wave_band',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('wave-channel-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Highest ITU wavelength channel number supported
                ''',
                'wave_channel_max',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('wave-channel-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lowest ITU wavelength channel number supported
                ''',
                'wave_channel_min',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'wave-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Optics' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Optics',
            False, 
            [
            _MetaInfoClassMember('wave-info', REFERENCE_CLASS, 'WaveInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Optics.WaveInfo', 
                [], [], 
                '''                DWDM port wavelength information data
                ''',
                'wave_info',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'optics',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.FecMismatch' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.FecMismatch',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'fec-mismatch',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.EcTca' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.EcTca',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Error counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Error threshold power
                ''',
                'threshold',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'ec-tca',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.UcTca' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.UcTca',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Error counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Error threshold power
                ''',
                'threshold',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'uc-tca',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'los',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'lof',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'lom',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'oof',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'oom',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'ais',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'iae',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'bdi',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'tim',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'eoc',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Error counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Error threshold power
                ''',
                'threshold',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'sf-ber',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Error counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Error threshold power
                ''',
                'threshold',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'sd-ber',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Error counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Error threshold power
                ''',
                'threshold',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'prefec-sf-ber',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Error counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Error threshold power
                ''',
                'threshold',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'prefec-sd-ber',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Error counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Error threshold power
                ''',
                'threshold',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'bbe-tca',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Error counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Error threshold power
                ''',
                'threshold',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'es-tca',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bbe' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bbe',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Performance Monitoring counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'bbe',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Es' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Es',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Performance Monitoring counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'es',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ses' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ses',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Performance Monitoring counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'ses',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Uas' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Uas',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Performance Monitoring counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'uas',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Fc' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Fc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Performance Monitoring counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'fc',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bber' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bber',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Performance Monitoring counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'bber',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Esr' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Esr',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Performance Monitoring counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'esr',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Sesr' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Sesr',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Performance Monitoring counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'sesr',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti',
            False, 
            [
            _MetaInfoClassMember('exp-dapi-range', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                 Expected DAPI Range String
                ''',
                'exp_dapi_range',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('exp-oper-spec-range', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                 Expected Operator Specific Field Range String
                ''',
                'exp_oper_spec_range',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('exp-sapi-range', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                 Expected SAPI Range String
                ''',
                'exp_sapi_range',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('expected-dapi', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Expected DAPI[1-15] Field
                ''',
                'expected_dapi',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('expected-dapi0', ATTRIBUTE, 'str' , None, None, 
                [(0, 5)], [], 
                '''                Expected DAPI[0] Field
                ''',
                'expected_dapi0',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('expected-oper-spec', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Expected Operator Specific Field
                ''',
                'expected_oper_spec',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('expected-sapi', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Expected SAPI[1-15] Field
                ''',
                'expected_sapi',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('expected-sapi0', ATTRIBUTE, 'str' , None, None, 
                [(0, 5)], [], 
                '''                Expected SAPI[0] Field
                ''',
                'expected_sapi0',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('expected-string-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of String
                ''',
                'expected_string_type',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('expected-tti', ATTRIBUTE, 'str' , None, None, 
                [(0, 129)], [], 
                '''                Expected TTI String
                ''',
                'expected_tti',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-dapi', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Rx DAPI[1-15] Field
                ''',
                'rx_dapi',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-dapi0', ATTRIBUTE, 'str' , None, None, 
                [(0, 5)], [], 
                '''                Rx DAPI[0] Field
                ''',
                'rx_dapi0',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-dapi-range', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                 Rx DAPI Range String
                ''',
                'rx_dapi_range',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-oper-spec', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Rx Operator Specific Field
                ''',
                'rx_oper_spec',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-oper-spec-range', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                 Rx Operator Specific Field Range String
                ''',
                'rx_oper_spec_range',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-sapi', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Rx SAPI[1-15] Field
                ''',
                'rx_sapi',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-sapi0', ATTRIBUTE, 'str' , None, None, 
                [(0, 5)], [], 
                '''                Rx SAPI[0] Field
                ''',
                'rx_sapi0',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-sapi-range', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                 Rx SAPI Range String
                ''',
                'rx_sapi_range',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-string-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of String
                ''',
                'rx_string_type',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-tti', ATTRIBUTE, 'str' , None, None, 
                [(0, 129)], [], 
                '''                Rx TTI String 
                ''',
                'rx_tti',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-dapi', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Tx DAPI[1-15] Field
                ''',
                'tx_dapi',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-dapi0', ATTRIBUTE, 'str' , None, None, 
                [(0, 5)], [], 
                '''                Tx DAPI[0] Field
                ''',
                'tx_dapi0',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-dapi-range', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                 Tx DAPI Range String
                ''',
                'tx_dapi_range',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-oper-spec', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Tx Operator Specific Field
                ''',
                'tx_oper_spec',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-oper-spec-range', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                 Tx Operator Specific Field Range String
                ''',
                'tx_oper_spec_range',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-sapi', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Tx SAPI[1-15] Field
                ''',
                'tx_sapi',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-sapi0', ATTRIBUTE, 'str' , None, None, 
                [(0, 5)], [], 
                '''                Tx SAPI[0] Field
                ''',
                'tx_sapi0',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-sapi-range', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                 Tx SAPI Range String
                ''',
                'tx_sapi_range',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-string-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of String
                ''',
                'tx_string_type',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-tti', ATTRIBUTE, 'str' , None, None, 
                [(0, 129)], [], 
                '''                Tx TTI String 
                ''',
                'tx_tti',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'tti',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OtuInfo' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OtuInfo',
            False, 
            [
            _MetaInfoClassMember('ais', REFERENCE_CLASS, 'Ais' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais', 
                [], [], 
                '''                Alarm Indication Signal information
                ''',
                'ais',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('bbe', REFERENCE_CLASS, 'Bbe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bbe', 
                [], [], 
                '''                Backgound Block Error information
                ''',
                'bbe',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('bbe-tca', REFERENCE_CLASS, 'BbeTca' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca', 
                [], [], 
                '''                 Backgound Block Error TCA information
                ''',
                'bbe_tca',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('bber', REFERENCE_CLASS, 'Bber' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bber', 
                [], [], 
                '''                Backgound Block Error Rate information
                ''',
                'bber',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('bdi', REFERENCE_CLASS, 'Bdi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi', 
                [], [], 
                '''                Backward Defect Indication information
                ''',
                'bdi',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('bei', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Backward Error Indication counter
                ''',
                'bei',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('bip', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bit Interleave Parity(BIP) counter
                ''',
                'bip',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('eoc', REFERENCE_CLASS, 'Eoc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc', 
                [], [], 
                '''                GCC End of Channel information
                ''',
                'eoc',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('es', REFERENCE_CLASS, 'Es' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Es', 
                [], [], 
                '''                Errored Seconds information 
                ''',
                'es',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('es-tca', REFERENCE_CLASS, 'EsTca' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca', 
                [], [], 
                '''                Errored Seconds TCA information
                ''',
                'es_tca',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('esr', REFERENCE_CLASS, 'Esr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Esr', 
                [], [], 
                '''                Errored Seconds Rate information
                ''',
                'esr',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('fc', REFERENCE_CLASS, 'Fc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Fc', 
                [], [], 
                '''                Failure Count information
                ''',
                'fc',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('iae', REFERENCE_CLASS, 'Iae' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae', 
                [], [], 
                '''                Incoming Alignment Error information
                ''',
                'iae',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('lof', REFERENCE_CLASS, 'Lof' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof', 
                [], [], 
                '''                Loss of Frame information
                ''',
                'lof',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('lom', REFERENCE_CLASS, 'Lom' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom', 
                [], [], 
                '''                Loss of MultiFrame information
                ''',
                'lom',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('los', REFERENCE_CLASS, 'Los' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los', 
                [], [], 
                '''                Loss of Signal information
                ''',
                'los',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('oof', REFERENCE_CLASS, 'Oof' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof', 
                [], [], 
                '''                Out of Frame information
                ''',
                'oof',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('oom', REFERENCE_CLASS, 'Oom' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom', 
                [], [], 
                '''                Out of MultiFrame information
                ''',
                'oom',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('prefec-sd-ber', REFERENCE_CLASS, 'PrefecSdBer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer', 
                [], [], 
                '''                Prefec Signal Degrade BER information
                ''',
                'prefec_sd_ber',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('prefec-sf-ber', REFERENCE_CLASS, 'PrefecSfBer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer', 
                [], [], 
                '''                Prefec Signal Fail BER information
                ''',
                'prefec_sf_ber',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('sd-ber', REFERENCE_CLASS, 'SdBer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer', 
                [], [], 
                '''                Signal Degrade BER information
                ''',
                'sd_ber',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('ses', REFERENCE_CLASS, 'Ses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ses', 
                [], [], 
                '''                Severly Errored Seconds information
                ''',
                'ses',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('sesr', REFERENCE_CLASS, 'Sesr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Sesr', 
                [], [], 
                '''                Severly Errored Seconds Rate information
                ''',
                'sesr',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('sf-ber', REFERENCE_CLASS, 'SfBer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer', 
                [], [], 
                '''                Signal Fail  BER information
                ''',
                'sf_ber',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tim', REFERENCE_CLASS, 'Tim' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim', 
                [], [], 
                '''                Trace Identifier Mismatch information
                ''',
                'tim',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tti', REFERENCE_CLASS, 'Tti' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti', 
                [], [], 
                '''                Trail Trace Identifier information
                ''',
                'tti',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('uas', REFERENCE_CLASS, 'Uas' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo.Uas', 
                [], [], 
                '''                Unavailability Seconds information
                ''',
                'uas',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'otu-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'oci',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'ais',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'lck',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'bdi',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'eoc',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'ptim',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'tim',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Error counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Error threshold power
                ''',
                'threshold',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'sf-ber',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Error counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Error threshold power
                ''',
                'threshold',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'sd-ber',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Error counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Error threshold power
                ''',
                'threshold',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'bbe-tca',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Error counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-asserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect delared?
                ''',
                'is_asserted',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reporting-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is reporting enabled?
                ''',
                'reporting_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Error threshold power
                ''',
                'threshold',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'es-tca',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.Bbe' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.Bbe',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Performance Monitoring counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'bbe',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.Es' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.Es',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Performance Monitoring counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'es',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.Ses' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.Ses',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Performance Monitoring counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'ses',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.Uas' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.Uas',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Performance Monitoring counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'uas',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.Fc' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.Fc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Performance Monitoring counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'fc',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.Bber' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.Bber',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Performance Monitoring counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'bber',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.Esr' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.Esr',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Performance Monitoring counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'esr',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.Sesr' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.Sesr',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Performance Monitoring counter
                ''',
                'counter',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'sesr',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti',
            False, 
            [
            _MetaInfoClassMember('exp-dapi-range', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                 Expected DAPI Range String
                ''',
                'exp_dapi_range',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('exp-oper-spec-range', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                 Expected Operator Specific Field Range String
                ''',
                'exp_oper_spec_range',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('exp-sapi-range', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                 Expected SAPI Range String
                ''',
                'exp_sapi_range',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('expected-dapi', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Expected DAPI[1-15] Field
                ''',
                'expected_dapi',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('expected-dapi0', ATTRIBUTE, 'str' , None, None, 
                [(0, 5)], [], 
                '''                Expected DAPI[0] Field
                ''',
                'expected_dapi0',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('expected-oper-spec', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Expected Operator Specific Field
                ''',
                'expected_oper_spec',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('expected-sapi', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Expected SAPI[1-15] Field
                ''',
                'expected_sapi',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('expected-sapi0', ATTRIBUTE, 'str' , None, None, 
                [(0, 5)], [], 
                '''                Expected SAPI[0] Field
                ''',
                'expected_sapi0',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('expected-string-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of String
                ''',
                'expected_string_type',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('expected-tti', ATTRIBUTE, 'str' , None, None, 
                [(0, 129)], [], 
                '''                Expected TTI String
                ''',
                'expected_tti',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-dapi', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Rx DAPI[1-15] Field
                ''',
                'rx_dapi',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-dapi0', ATTRIBUTE, 'str' , None, None, 
                [(0, 5)], [], 
                '''                Rx DAPI[0] Field
                ''',
                'rx_dapi0',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-dapi-range', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                 Rx DAPI Range String
                ''',
                'rx_dapi_range',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-oper-spec', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Rx Operator Specific Field
                ''',
                'rx_oper_spec',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-oper-spec-range', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                 Rx Operator Specific Field Range String
                ''',
                'rx_oper_spec_range',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-sapi', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Rx SAPI[1-15] Field
                ''',
                'rx_sapi',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-sapi0', ATTRIBUTE, 'str' , None, None, 
                [(0, 5)], [], 
                '''                Rx SAPI[0] Field
                ''',
                'rx_sapi0',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-sapi-range', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                 Rx SAPI Range String
                ''',
                'rx_sapi_range',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-string-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of String
                ''',
                'rx_string_type',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-tti', ATTRIBUTE, 'str' , None, None, 
                [(0, 129)], [], 
                '''                Rx TTI String 
                ''',
                'rx_tti',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-dapi', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Tx DAPI[1-15] Field
                ''',
                'tx_dapi',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-dapi0', ATTRIBUTE, 'str' , None, None, 
                [(0, 5)], [], 
                '''                Tx DAPI[0] Field
                ''',
                'tx_dapi0',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-dapi-range', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                 Tx DAPI Range String
                ''',
                'tx_dapi_range',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-oper-spec', ATTRIBUTE, 'str' , None, None, 
                [(0, 33)], [], 
                '''                Tx Operator Specific Field
                ''',
                'tx_oper_spec',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-oper-spec-range', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                 Tx Operator Specific Field Range String
                ''',
                'tx_oper_spec_range',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-sapi', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                Tx SAPI[1-15] Field
                ''',
                'tx_sapi',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-sapi0', ATTRIBUTE, 'str' , None, None, 
                [(0, 5)], [], 
                '''                Tx SAPI[0] Field
                ''',
                'tx_sapi0',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-sapi-range', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                 Tx SAPI Range String
                ''',
                'tx_sapi_range',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-string-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of String
                ''',
                'tx_string_type',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-tti', ATTRIBUTE, 'str' , None, None, 
                [(0, 129)], [], 
                '''                Tx TTI String 
                ''',
                'tx_tti',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'tti',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info.OduInfo' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info.OduInfo',
            False, 
            [
            _MetaInfoClassMember('ais', REFERENCE_CLASS, 'Ais' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais', 
                [], [], 
                '''                Alarm Indication Signal information
                ''',
                'ais',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('bbe', REFERENCE_CLASS, 'Bbe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.Bbe', 
                [], [], 
                '''                Background Block Error information
                ''',
                'bbe',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('bbe-tca', REFERENCE_CLASS, 'BbeTca' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca', 
                [], [], 
                '''                Background Block Error TCA information
                ''',
                'bbe_tca',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('bber', REFERENCE_CLASS, 'Bber' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.Bber', 
                [], [], 
                '''                Background Block Error Rate count information
                ''',
                'bber',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('bdi', REFERENCE_CLASS, 'Bdi' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi', 
                [], [], 
                '''                Backward Defect Indication information
                ''',
                'bdi',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('bei', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Backward Error Indication counter
                ''',
                'bei',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('bip', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Bit Interleave Parity(BIP) counter
                ''',
                'bip',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('eoc', REFERENCE_CLASS, 'Eoc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc', 
                [], [], 
                '''                GCC End of Channel information
                ''',
                'eoc',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('es', REFERENCE_CLASS, 'Es' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.Es', 
                [], [], 
                '''                Errored Seconds information
                ''',
                'es',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('es-tca', REFERENCE_CLASS, 'EsTca' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca', 
                [], [], 
                '''                Errored Seconds TCA information
                ''',
                'es_tca',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('esr', REFERENCE_CLASS, 'Esr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.Esr', 
                [], [], 
                '''                Errored Seconds Rate information
                ''',
                'esr',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('fc', REFERENCE_CLASS, 'Fc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.Fc', 
                [], [], 
                '''                Failure count information
                ''',
                'fc',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('lck', REFERENCE_CLASS, 'Lck' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck', 
                [], [], 
                '''                Upstream Connection Locked information
                ''',
                'lck',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('oci', REFERENCE_CLASS, 'Oci' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci', 
                [], [], 
                '''                Open Connection Indiction information
                ''',
                'oci',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('ptim', REFERENCE_CLASS, 'Ptim' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim', 
                [], [], 
                '''                Payload Type Identifier Mismatch information
                ''',
                'ptim',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('sd-ber', REFERENCE_CLASS, 'SdBer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer', 
                [], [], 
                '''                Signal Degrade BER information
                ''',
                'sd_ber',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('ses', REFERENCE_CLASS, 'Ses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.Ses', 
                [], [], 
                '''                Severly Errored Seconds information
                ''',
                'ses',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('sesr', REFERENCE_CLASS, 'Sesr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.Sesr', 
                [], [], 
                '''                Severly Errored Seconds Rate information
                ''',
                'sesr',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('sf-ber', REFERENCE_CLASS, 'SfBer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer', 
                [], [], 
                '''                Signal Fail  BER information
                ''',
                'sf_ber',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tim', REFERENCE_CLASS, 'Tim' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim', 
                [], [], 
                '''                Trace Identifier Mismatch information
                ''',
                'tim',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tti', REFERENCE_CLASS, 'Tti' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti', 
                [], [], 
                '''                Trail Trace Identifier information
                ''',
                'tti',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('uas', REFERENCE_CLASS, 'Uas' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo.Uas', 
                [], [], 
                '''                Unavailability Seconds information
                ''',
                'uas',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'odu-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.G709Info' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.G709Info',
            False, 
            [
            _MetaInfoClassMember('ec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Corrected bit error counter 
                ''',
                'ec',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('ec-accum', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                FEC Corrected bit error accumulated counter
                ''',
                'ec_accum',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('ec-tca', REFERENCE_CLASS, 'EcTca' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.EcTca', 
                [], [], 
                '''                FEC Corrected bits TCA information
                ''',
                'ec_tca',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('efec-mode', REFERENCE_ENUM_CLASS, 'G709EfecModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709EfecModeEnum', 
                [], [], 
                '''                EFEC information
                ''',
                'efec_mode',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('fe-cstr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                FEC BER String 
                ''',
                'fe_cstr',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('fec-ber', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                pre fec ber calculated
                ''',
                'fec_ber',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('fec-ber-man', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                pre fec ber calculated
                ''',
                'fec_ber_man',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('fec-mismatch', REFERENCE_CLASS, 'FecMismatch' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.FecMismatch', 
                [], [], 
                '''                FEC mismatch alarm
                ''',
                'fec_mismatch',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('fec-mode', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FEC information
                ''',
                'fec_mode',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('g709-prbs-mode', REFERENCE_ENUM_CLASS, 'G709PrbsModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709PrbsModeEnum', 
                [], [], 
                '''                Configured mode of PRBS Test
                ''',
                'g709_prbs_mode',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('g709-prbs-pattern', REFERENCE_ENUM_CLASS, 'G709PrbsPatternEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709PrbsPatternEnum', 
                [], [], 
                '''                Pattern of PRBS Test
                ''',
                'g709_prbs_pattern',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-fec-mode-default', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                 Is Operating FEC Mode Default
                ''',
                'is_fec_mode_default',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-g709-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                 Is G709 framing enabled
                ''',
                'is_g709_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-prbs-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                'true' if Prbs is enabled 'false' otherwise
                ''',
                'is_prbs_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('loopback-mode', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Loopback information
                ''',
                'loopback_mode',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('network-conn-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Network connection ID
                ''',
                'network_conn_id',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('network-port-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 65)], [], 
                '''                Network port ID
                ''',
                'network_port_id',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('odu-info', REFERENCE_CLASS, 'OduInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OduInfo', 
                [], [], 
                '''                ODU layer Information
                ''',
                'odu_info',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('otu-info', REFERENCE_CLASS, 'OtuInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.OtuInfo', 
                [], [], 
                '''                OTU layer information
                ''',
                'otu_info',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('prbs-time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time stamp for prbs configuration
                ''',
                'prbs_time_stamp',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('q', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                q value calculated
                ''',
                'q',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('q-margin', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                q margin calculated
                ''',
                'q_margin',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('qmargin-str', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                QMargin String
                ''',
                'qmargin_str',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('qstr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Q String 
                ''',
                'qstr',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('remote-fec-mode', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Remote FEC information
                ''',
                'remote_fec_mode',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('uc', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                FEC Uncorrected words counter
                ''',
                'uc',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('uc-tca', REFERENCE_CLASS, 'UcTca' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info.UcTca', 
                [], [], 
                '''                FEC uncorrected words TCA information
                ''',
                'uc_tca',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'g709-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.OpticsInfo' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.OpticsInfo',
            False, 
            [
            _MetaInfoClassMember('chromatic-dispersion', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Current chromatic dispersion
                ''',
                'chromatic_dispersion',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('clock-source', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Actual transmit clock source
                ''',
                'clock_source',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('configured-wave-channel', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Wavelength channel set from configuration
                ''',
                'configured_wave_channel',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('default-wave-channel', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Wavelength channel default from hardware
                ''',
                'default_wave_channel',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('differential-group-delay', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Current differential group Delay
                ''',
                'differential_group_delay',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('gmpls-set-wave-channel', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Wavelength channel set by GMPLS
                ''',
                'gmpls_set_wave_channel',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('input-power-fail', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Receive power failure(above/belowe a threshold)
                count
                ''',
                'input_power_fail',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-rx-los-threshold-supported', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if  Rx LOS thresold configurable
                ''',
                'is_rx_los_threshold_supported',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-wave-frequency-progressive-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if Progressive Frequency is supported by hw
                ''',
                'is_wave_frequency_progressive_valid',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-wave-frequency-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if hw supported wavelength frequency
                readback
                ''',
                'is_wave_frequency_valid',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('laser-bias-current-avg', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Laser bias current average value in the interval
                time
                ''',
                'laser_bias_current_avg',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('laser-bias-current-max', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Laser bias current maxinum value in the interval
                time
                ''',
                'laser_bias_current_max',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('laser-bias-current-min', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Laser bias current minimum value in the interval
                time
                ''',
                'laser_bias_current_min',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('laser-current-bias', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Laser current bias value
                ''',
                'laser_current_bias',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('laser-current-bias-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                 Laser Current Bias threshold value
                ''',
                'laser_current_bias_threshold',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('optics-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Optics type name
                ''',
                'optics_type',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('output-power-fail', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Transmit power failure(above/belowe a threshold)
                count
                ''',
                'output_power_fail',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('phase-noise', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current Phase Noise
                ''',
                'phase_noise',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('polarization-change-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current Polarization change rate
                ''',
                'polarization_change_rate',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('polarization-dependent-loss', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Current Polarization Dependent loss
                ''',
                'polarization_dependent_loss',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('polarization-mode-dispersion', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Current polarization mode dispersion
                ''',
                'polarization_mode_dispersion',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('receive-power', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Transponder receive power
                ''',
                'receive_power',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('receive-power-avg', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Recieve power average value in the interval time
                ''',
                'receive_power_avg',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('receive-power-max', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Receive power maximum value in the interval time
                ''',
                'receive_power_max',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('receive-power-min', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Recieve power mininum value in the interval time
                ''',
                'receive_power_min',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-los-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Rx LOS threshold value
                ''',
                'rx_los_threshold',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('signal-to-noise-ratio', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Current optical signal to noise ratio
                ''',
                'signal_to_noise_ratio',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('transmit-power', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Transmit power in the unit of 0.01dbm
                ''',
                'transmit_power',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('transmit-power-avg', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Transmit optical average value in the interval
                time
                ''',
                'transmit_power_avg',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('transmit-power-max', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Transmit power maximum value in the interval
                time
                ''',
                'transmit_power_max',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('transmit-power-min', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Transmit  power mininum value in the interval
                time
                ''',
                'transmit_power_min',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('transmit-power-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Transmit power threshold value
                ''',
                'transmit_power_threshold',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('wave-band', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Wavelength band information
                ''',
                'wave_band',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('wave-channel', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current ITU wavelength channel number
                ''',
                'wave_channel',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('wave-channel-owner', REFERENCE_ENUM_CLASS, 'DwdmWaveChannelOwnerEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'DwdmWaveChannelOwnerEnum', 
                [], [], 
                '''                Owner of current wavelength
                ''',
                'wave_channel_owner',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('wave-frequency', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 wavelenght frequency read from hw in the uint 0
                .01nm
                ''',
                'wave_frequency',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('wave-frequency-progressive-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Wave Frequency Information for Progressive
                Frequencies
                ''',
                'wave_frequency_progressive_string',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('wavelength-progressive', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Wavelength Information for Progressive
                Frequencies
                ''',
                'wavelength_progressive',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('wavelength-progressive-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Wavelength Information for Progressive
                Frequencies
                ''',
                'wavelength_progressive_string',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'optics-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.TdcInfo' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.TdcInfo',
            False, 
            [
            _MetaInfoClassMember('dispersion-offset', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                TDC Dispersion Offset
                ''',
                'dispersion_offset',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('is-reroute-control-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE for ENABLED else DISABLED
                ''',
                'is_reroute_control_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('major-alarm', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE for Alarm condition else FALSE
                ''',
                'major_alarm',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('operation-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE for MANUAL else AUTO
                ''',
                'operation_mode',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('reroute-ber', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Reroute BER
                ''',
                'reroute_ber',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tdc-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if TDC Aquiring else Locked
                ''',
                'tdc_status',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tdc-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE for Valid else Invalid
                ''',
                'tdc_valid',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'tdc-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.NetworkSrlgInfo' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.NetworkSrlgInfo',
            False, 
            [
            _MetaInfoClassMember('network-srlg', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Network Srlg
                ''',
                'network_srlg',
                'Cisco-IOS-XR-dwdm-ui-oper', False, max_elements=102),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'network-srlg-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.Proactive' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.Proactive',
            False, 
            [
            _MetaInfoClassMember('alarm-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                AlarmState
                ''',
                'alarm_state',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('default-rvrt-thresh-coeff', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Default Revert threshold coefficient
                ''',
                'default_rvrt_thresh_coeff',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('default-rvrt-thresh-power', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Default Revert threshold power
                ''',
                'default_rvrt_thresh_power',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('default-trig-thresh-coeff', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Default Trigger threshold coefficient
                ''',
                'default_trig_thresh_coeff',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('default-trig-thresh-power', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Default Trigger threshold power
                ''',
                'default_trig_thresh_power',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('interface-trigger', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Proactive Interface Triffer
                ''',
                'interface_trigger',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('prefec-thresh-crossed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Prefec Trigger Thresh Crossed
                ''',
                'prefec_thresh_crossed',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('proactive-feature', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Feature Support
                ''',
                'proactive_feature',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('proactive-fsm-if-state', REFERENCE_ENUM_CLASS, 'G709PpintfStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709PpintfStateEnum', 
                [], [], 
                '''                Proactive FSM IF State
                ''',
                'proactive_fsm_if_state',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('proactive-fsm-state', REFERENCE_ENUM_CLASS, 'G709PpfsmStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709PpfsmStateEnum', 
                [], [], 
                '''                Proactive FSM State
                ''',
                'proactive_fsm_state',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('proactive-mode', REFERENCE_ENUM_CLASS, 'G709PpfsmModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709PpfsmModeEnum', 
                [], [], 
                '''                Proactive Mode
                ''',
                'proactive_mode',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('protection-trigger', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Protection Trigger State
                ''',
                'protection_trigger',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('revert-window', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Revert Integration Window
                ''',
                'revert_window',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rvrt-ec-cnt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Revert EC Cnt
                ''',
                'rvrt_ec_cnt',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rvrt-samples', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Required Revert Samples
                ''',
                'rvrt_samples',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rvrt-thresh-coeff', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Revert threshold coefficient
                ''',
                'rvrt_thresh_coeff',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rvrt-thresh-power', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Revert threshold power
                ''',
                'rvrt_thresh_power',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-aps', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Received APS byte
                ''',
                'rx_aps',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('rx-aps-descr', REFERENCE_ENUM_CLASS, 'G709ApsByteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709ApsByteEnum', 
                [], [], 
                '''                Rx APS Description
                ''',
                'rx_aps_descr',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tas-state', REFERENCE_ENUM_CLASS, 'DwdmtasStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'DwdmtasStateEnum', 
                [], [], 
                '''                TAS State
                ''',
                'tas_state',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('trig-ec-cnt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Trigger EC Cnt
                ''',
                'trig_ec_cnt',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('trig-samples', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Required Trigger Samples
                ''',
                'trig_samples',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('trig-thresh-coeff', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Trigger threshold coefficient
                ''',
                'trig_thresh_coeff',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('trig-thresh-power', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Trigger threshold power
                ''',
                'trig_thresh_power',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('trigger-window', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Trigger Integration window
                ''',
                'trigger_window',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-aps', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Transmitted APS Byte
                ''',
                'tx_aps',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tx-aps-descr', REFERENCE_ENUM_CLASS, 'G709ApsByteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'G709ApsByteEnum', 
                [], [], 
                '''                Tx APS Description
                ''',
                'tx_aps_descr',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'proactive',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info.SignalLog' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info.SignalLog',
            False, 
            [
            _MetaInfoClassMember('is-log-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                'true' if signal log is enabled 'false'
                otherwise
                ''',
                'is_log_enabled',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('log-filename', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Log file name 
                ''',
                'log_filename',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'signal-log',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port.Info' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port.Info',
            False, 
            [
            _MetaInfoClassMember('controller-state', REFERENCE_ENUM_CLASS, 'DwdmControllerStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'DwdmControllerStateEnum', 
                [], [], 
                '''                DWDM controller state: Up, Down or
                Administratively Down
                ''',
                'controller_state',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('g709-info', REFERENCE_CLASS, 'G709Info' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.G709Info', 
                [], [], 
                '''                G709 operational information
                ''',
                'g709_info',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('network-srlg-info', REFERENCE_CLASS, 'NetworkSrlgInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.NetworkSrlgInfo', 
                [], [], 
                '''                Network SRLG information
                ''',
                'network_srlg_info',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('optics-info', REFERENCE_CLASS, 'OpticsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.OpticsInfo', 
                [], [], 
                '''                Optics operational information
                ''',
                'optics_info',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('proactive', REFERENCE_CLASS, 'Proactive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.Proactive', 
                [], [], 
                '''                Proactive protection information
                ''',
                'proactive',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('signal-log', REFERENCE_CLASS, 'SignalLog' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.SignalLog', 
                [], [], 
                '''                Signal log information
                ''',
                'signal_log',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('slice-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                DWDM port slice state Up/Down
                ''',
                'slice_state',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('tdc-info', REFERENCE_CLASS, 'TdcInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info.TdcInfo', 
                [], [], 
                '''                TDC operational information
                ''',
                'tdc_info',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('transport-admin-state', REFERENCE_ENUM_CLASS, 'DwdmtasStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'DwdmtasStateEnum', 
                [], [], 
                '''                DWDM controller TAS state: IS, OOS, OOS-MT or
                IS-CFG
                ''',
                'transport_admin_state',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'info',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports.Port' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports.Port',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Port name
                ''',
                'name',
                'Cisco-IOS-XR-dwdm-ui-oper', True),
            _MetaInfoClassMember('info', REFERENCE_CLASS, 'Info' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Info', 
                [], [], 
                '''                DWDM port operational data
                ''',
                'info',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('optics', REFERENCE_CLASS, 'Optics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Optics', 
                [], [], 
                '''                DWDM Port optics operational data
                ''',
                'optics',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            _MetaInfoClassMember('prbs', REFERENCE_CLASS, 'Prbs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port.Prbs', 
                [], [], 
                '''                DWDM Port PRBS related data
                ''',
                'prbs',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'port',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm.Ports' : {
        'meta_info' : _MetaInfoClass('Dwdm.Ports',
            False, 
            [
            _MetaInfoClassMember('port', REFERENCE_LIST, 'Port' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports.Port', 
                [], [], 
                '''                DWDM Port operational data
                ''',
                'port',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'ports',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Dwdm' : {
        'meta_info' : _MetaInfoClass('Dwdm',
            False, 
            [
            _MetaInfoClassMember('ports', REFERENCE_CLASS, 'Ports' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Dwdm.Ports', 
                [], [], 
                '''                All DWDM Port operational data
                ''',
                'ports',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'dwdm',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info' : {
        'meta_info' : _MetaInfoClass('Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info',
            False, 
            [
            _MetaInfoClassMember('vtxp-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is VTXP attribute enabled
                ''',
                'vtxp_enable',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'info',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Vtxp.DwdmVtxp.PortVtxps.PortVtxp' : {
        'meta_info' : _MetaInfoClass('Vtxp.DwdmVtxp.PortVtxps.PortVtxp',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Port name
                ''',
                'name',
                'Cisco-IOS-XR-dwdm-ui-oper', True),
            _MetaInfoClassMember('info', REFERENCE_CLASS, 'Info' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info', 
                [], [], 
                '''                DWDM port operational data
                ''',
                'info',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'port-vtxp',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Vtxp.DwdmVtxp.PortVtxps' : {
        'meta_info' : _MetaInfoClass('Vtxp.DwdmVtxp.PortVtxps',
            False, 
            [
            _MetaInfoClassMember('port-vtxp', REFERENCE_LIST, 'PortVtxp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Vtxp.DwdmVtxp.PortVtxps.PortVtxp', 
                [], [], 
                '''                DWDM Port operational data
                ''',
                'port_vtxp',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'port-vtxps',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Vtxp.DwdmVtxp' : {
        'meta_info' : _MetaInfoClass('Vtxp.DwdmVtxp',
            False, 
            [
            _MetaInfoClassMember('port-vtxps', REFERENCE_CLASS, 'PortVtxps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Vtxp.DwdmVtxp.PortVtxps', 
                [], [], 
                '''                All DWDM Port operational data
                ''',
                'port_vtxps',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'dwdm-vtxp',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
    'Vtxp' : {
        'meta_info' : _MetaInfoClass('Vtxp',
            False, 
            [
            _MetaInfoClassMember('dwdm-vtxp', REFERENCE_CLASS, 'DwdmVtxp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper', 'Vtxp.DwdmVtxp', 
                [], [], 
                '''                DWDM operational data
                ''',
                'dwdm_vtxp',
                'Cisco-IOS-XR-dwdm-ui-oper', False),
            ],
            'Cisco-IOS-XR-dwdm-ui-oper',
            'vtxp',
            _yang_ns._namespaces['Cisco-IOS-XR-dwdm-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_dwdm_ui_oper'
        ),
    },
}
_meta_table['Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics.PrbsEntry']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics']['meta_info']
_meta_table['Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket.TwentyFourHoursStatistics']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket']['meta_info']
_meta_table['Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics.PrbsEntry']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics']['meta_info']
_meta_table['Dwdm.Ports.Port.Prbs.FifteenMinutesBucket.FifteenMinutesStatistics']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Prbs.FifteenMinutesBucket']['meta_info']
_meta_table['Dwdm.Ports.Port.Prbs.TwentyFourHoursBucket']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Prbs']['meta_info']
_meta_table['Dwdm.Ports.Port.Prbs.FifteenMinutesBucket']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Prbs']['meta_info']
_meta_table['Dwdm.Ports.Port.Optics.WaveInfo']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Optics']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Los']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lof']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Lom']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oof']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Oom']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ais']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Iae']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bdi']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tim']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Eoc']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.SfBer']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.SdBer']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSfBer']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.PrefecSdBer']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.BbeTca']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.EsTca']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bbe']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Es']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Ses']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Uas']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Fc']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Bber']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Esr']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Sesr']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo.Tti']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Oci']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Ais']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Lck']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Bdi']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Eoc']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Ptim']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Tim']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.SfBer']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.SdBer']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.BbeTca']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.EsTca']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Bbe']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Es']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Ses']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Uas']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Fc']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Bber']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Esr']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Sesr']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo.Tti']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.FecMismatch']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.EcTca']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.UcTca']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OtuInfo']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info.OduInfo']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info.G709Info']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.G709Info']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.OpticsInfo']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.TdcInfo']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.NetworkSrlgInfo']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.Proactive']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info']['meta_info']
_meta_table['Dwdm.Ports.Port.Info.SignalLog']['meta_info'].parent =_meta_table['Dwdm.Ports.Port.Info']['meta_info']
_meta_table['Dwdm.Ports.Port.Prbs']['meta_info'].parent =_meta_table['Dwdm.Ports.Port']['meta_info']
_meta_table['Dwdm.Ports.Port.Optics']['meta_info'].parent =_meta_table['Dwdm.Ports.Port']['meta_info']
_meta_table['Dwdm.Ports.Port.Info']['meta_info'].parent =_meta_table['Dwdm.Ports.Port']['meta_info']
_meta_table['Dwdm.Ports.Port']['meta_info'].parent =_meta_table['Dwdm.Ports']['meta_info']
_meta_table['Dwdm.Ports']['meta_info'].parent =_meta_table['Dwdm']['meta_info']
_meta_table['Vtxp.DwdmVtxp.PortVtxps.PortVtxp.Info']['meta_info'].parent =_meta_table['Vtxp.DwdmVtxp.PortVtxps.PortVtxp']['meta_info']
_meta_table['Vtxp.DwdmVtxp.PortVtxps.PortVtxp']['meta_info'].parent =_meta_table['Vtxp.DwdmVtxp.PortVtxps']['meta_info']
_meta_table['Vtxp.DwdmVtxp.PortVtxps']['meta_info'].parent =_meta_table['Vtxp.DwdmVtxp']['meta_info']
_meta_table['Vtxp.DwdmVtxp']['meta_info'].parent =_meta_table['Vtxp']['meta_info']
