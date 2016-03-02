


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'OpticsFormFactor_Enum' : _MetaInfoEnum('OpticsFormFactor_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper',
        {
            'not-set':'NOT_SET',
            'invalid':'INVALID',
            'cpak':'CPAK',
            'cxp':'CXP',
            'sfp-plus':'SFP_PLUS',
            'qsfp':'QSFP',
            'qsfp-plus':'QSFP_PLUS',
            'qsfp28':'QSFP28',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsControllerState_Enum' : _MetaInfoEnum('OpticsControllerState_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper',
        {
            'optics-state-up':'OPTICS_STATE_UP',
            'optics-state-down':'OPTICS_STATE_DOWN',
            'optics-state-admin-down':'OPTICS_STATE_ADMIN_DOWN',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsLaserState_Enum' : _MetaInfoEnum('OpticsLaserState_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper',
        {
            'on':'ON',
            'off':'OFF',
            'unknown':'UNKNOWN',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsPhy_Enum' : _MetaInfoEnum('OpticsPhy_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper',
        {
            'not-set':'NOT_SET',
            'invalid':'INVALID',
            'long-reach-four-lanes':'LONG_REACH_FOUR_LANES',
            'short-reach-ten-lanes':'SHORT_REACH_TEN_LANES',
            'short-reach-one-lane':'SHORT_REACH_ONE_LANE',
            'long-reach-one-lane':'LONG_REACH_ONE_LANE',
            'short-reach-four-lanes':'SHORT_REACH_FOUR_LANES',
            'copper-four-lanes':'COPPER_FOUR_LANES',
            'active-optical-cable':'ACTIVE_OPTICAL_CABLE',
            'fourty-gig-e-long-reach-four-lanes':'FOURTY_GIG_E_LONG_REACH_FOUR_LANES',
            'fourty-gig-e-short-reach-four-lanes':'FOURTY_GIG_E_SHORT_REACH_FOUR_LANES',
            'cwdm-four-lanes':'CWDM_FOUR_LANES',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsTas_Enum' : _MetaInfoEnum('OpticsTas_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper',
        {
            'tas-ui-oos':'TAS_UI_OOS',
            'tas-ui-main':'TAS_UI_MAIN',
            'tas-ui-is':'TAS_UI_IS',
            'tas-ui-ains':'TAS_UI_AINS',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'Optics_Enum' : _MetaInfoEnum('Optics_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper',
        {
            'optics-unknown':'OPTICS_UNKNOWN',
            'optics-grey':'OPTICS_GREY',
            'optics-dwdm':'OPTICS_DWDM',
            'optics-cwdm':'OPTICS_CWDM',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsLedState_Enum' : _MetaInfoEnum('OpticsLedState_Enum', 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper',
        {
            'off':'OFF',
            'green-on':'GREEN_ON',
            'green-flashing':'GREEN_FLASHING',
            'yellow-on':'YELLOW_ON',
            'yellow-flashing':'YELLOW_FLASHING',
            'red-on':'RED_ON',
            'red-flashing':'RED_FLASHING',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap.DwdmCarrierMapInfo' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap.DwdmCarrierMapInfo',
            False, 
            [
            _MetaInfoClassMember('frequency', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Frequency
                ''',
                'frequency',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('g694-chan-num', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                G694 channel number
                ''',
                'g694_chan_num',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('itu-chan-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ITU channel number
                ''',
                'itu_chan_num',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('wavelength', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Wavelength
                ''',
                'wavelength',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'dwdm-carrier-map-info',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap',
            False, 
            [
            _MetaInfoClassMember('dwdm-carrier-band', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                DWDM carrier band
                ''',
                'dwdm_carrier_band',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('dwdm-carrier-map-info', REFERENCE_LIST, 'DwdmCarrierMapInfo' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap.DwdmCarrierMapInfo', 
                [], [], 
                '''                DWDM carrier mapping info
                ''',
                'dwdm_carrier_map_info',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('dwdm-carrier-max', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Highest DWDM carrier supported
                ''',
                'dwdm_carrier_max',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('dwdm-carrier-min', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Lowest DWDM carrier supported
                ''',
                'dwdm_carrier_min',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'optics-dwdm-carrrier-channel-map',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData',
            False, 
            [
            _MetaInfoClassMember('lane-index', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The index number of the lane
                ''',
                'lane_index',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-bias-current-milli-amps', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Laser Bias Current in units of 0.01mA
                ''',
                'laser_bias_current_milli_amps',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-bias-current-percent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Laser Bias Current in units of 0.01%
                ''',
                'laser_bias_current_percent',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('receive-power', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Transponder receive power in the unit of 0.01dBm
                ''',
                'receive_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('transmit-power', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Transmit power in the unit of 0.01dBm
                ''',
                'transmit_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'lane-data',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo',
            False, 
            [
            _MetaInfoClassMember('network-srlg', REFERENCE_LEAFLIST, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Network Srlg
                ''',
                'network_srlg',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'network-srlg-info',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'hidgd',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'high-lbc',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'high-rx1-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'high-rx2-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'high-rx3-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'high-rx4-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'high-rx-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'high-tx1-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1lbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1lbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'high-tx1lbc',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'high-tx2-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2lbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2lbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'high-tx2lbc',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'high-tx3-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3lbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3lbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'high-tx3lbc',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'high-tx4-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4lbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4lbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'high-tx4lbc',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'high-tx-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'imp-removal',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'low-rx1-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'low-rx2-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'low-rx3-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'low-rx4-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'low-rx-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'low-tx1-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1lbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1lbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'low-tx1lbc',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'low-tx2-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2lbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2lbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'low-tx2lbc',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'low-tx3-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3lbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3lbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'low-tx3lbc',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'low-tx4-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4lbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4lbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'low-tx4lbc',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'low-tx-power',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'mea',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'oorcd',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'osnr',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'rx-lol',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'rx-los',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'tx-fault',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'tx-lol',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'tx-los',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Alarm counter
                ''',
                'counter',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is defect detected?
                ''',
                'is_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'wvlool',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo',
            False, 
            [
            _MetaInfoClassMember('hidgd', REFERENCE_CLASS, 'Hidgd' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd', 
                [], [], 
                '''                HI DGD
                ''',
                'hidgd',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-lbc', REFERENCE_CLASS, 'HighLbc' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc', 
                [], [], 
                '''                High laser bias current
                ''',
                'high_lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-rx1-power', REFERENCE_CLASS, 'HighRx1Power' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power', 
                [], [], 
                '''                High Rx1 Power
                ''',
                'high_rx1_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-rx2-power', REFERENCE_CLASS, 'HighRx2Power' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power', 
                [], [], 
                '''                High Rx2 Power
                ''',
                'high_rx2_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-rx3-power', REFERENCE_CLASS, 'HighRx3Power' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power', 
                [], [], 
                '''                High Rx3 Power
                ''',
                'high_rx3_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-rx4-power', REFERENCE_CLASS, 'HighRx4Power' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power', 
                [], [], 
                '''                High Rx4 Power
                ''',
                'high_rx4_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-rx-power', REFERENCE_CLASS, 'HighRxPower' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower', 
                [], [], 
                '''                High Rx Power
                ''',
                'high_rx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx1-power', REFERENCE_CLASS, 'HighTx1Power' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power', 
                [], [], 
                '''                High Tx1 Power
                ''',
                'high_tx1_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx1lbc', REFERENCE_CLASS, 'HighTx1lbc' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1lbc', 
                [], [], 
                '''                High Tx1 laser bias current
                ''',
                'high_tx1lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx2-power', REFERENCE_CLASS, 'HighTx2Power' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power', 
                [], [], 
                '''                High Tx2 Power
                ''',
                'high_tx2_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx2lbc', REFERENCE_CLASS, 'HighTx2lbc' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2lbc', 
                [], [], 
                '''                High Tx2 laser bias current
                ''',
                'high_tx2lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx3-power', REFERENCE_CLASS, 'HighTx3Power' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power', 
                [], [], 
                '''                High Tx3 Power
                ''',
                'high_tx3_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx3lbc', REFERENCE_CLASS, 'HighTx3lbc' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3lbc', 
                [], [], 
                '''                High Tx3 laser bias current
                ''',
                'high_tx3lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx4-power', REFERENCE_CLASS, 'HighTx4Power' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power', 
                [], [], 
                '''                High Tx4 Power
                ''',
                'high_tx4_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx4lbc', REFERENCE_CLASS, 'HighTx4lbc' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4lbc', 
                [], [], 
                '''                High Tx4 laser bias current
                ''',
                'high_tx4lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx-power', REFERENCE_CLASS, 'HighTxPower' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower', 
                [], [], 
                '''                High Tx Power
                ''',
                'high_tx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('imp-removal', REFERENCE_CLASS, 'ImpRemoval' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval', 
                [], [], 
                '''                IMPROPER REM
                ''',
                'imp_removal',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-rx1-power', REFERENCE_CLASS, 'LowRx1Power' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power', 
                [], [], 
                '''                Low Rx1 Power
                ''',
                'low_rx1_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-rx2-power', REFERENCE_CLASS, 'LowRx2Power' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power', 
                [], [], 
                '''                Low Rx2 Power
                ''',
                'low_rx2_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-rx3-power', REFERENCE_CLASS, 'LowRx3Power' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power', 
                [], [], 
                '''                Low Rx3 Power
                ''',
                'low_rx3_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-rx4-power', REFERENCE_CLASS, 'LowRx4Power' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power', 
                [], [], 
                '''                Low Rx4 Power
                ''',
                'low_rx4_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-rx-power', REFERENCE_CLASS, 'LowRxPower' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower', 
                [], [], 
                '''                Low Rx Power
                ''',
                'low_rx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx1-power', REFERENCE_CLASS, 'LowTx1Power' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power', 
                [], [], 
                '''                Low Tx1 Power
                ''',
                'low_tx1_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx1lbc', REFERENCE_CLASS, 'LowTx1lbc' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1lbc', 
                [], [], 
                '''                Low Tx1 laser bias current
                ''',
                'low_tx1lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx2-power', REFERENCE_CLASS, 'LowTx2Power' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power', 
                [], [], 
                '''                Low Tx2 Power
                ''',
                'low_tx2_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx2lbc', REFERENCE_CLASS, 'LowTx2lbc' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2lbc', 
                [], [], 
                '''                Low Tx2 laser bias current
                ''',
                'low_tx2lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx3-power', REFERENCE_CLASS, 'LowTx3Power' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power', 
                [], [], 
                '''                Low Tx3 Power
                ''',
                'low_tx3_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx3lbc', REFERENCE_CLASS, 'LowTx3lbc' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3lbc', 
                [], [], 
                '''                Low Tx3 laser bias current
                ''',
                'low_tx3lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx4-power', REFERENCE_CLASS, 'LowTx4Power' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power', 
                [], [], 
                '''                Low Tx4 Power
                ''',
                'low_tx4_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx4lbc', REFERENCE_CLASS, 'LowTx4lbc' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4lbc', 
                [], [], 
                '''                Low Tx4 laser bias current
                ''',
                'low_tx4lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx-power', REFERENCE_CLASS, 'LowTxPower' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower', 
                [], [], 
                '''                Low Tx Power
                ''',
                'low_tx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('mea', REFERENCE_CLASS, 'Mea' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea', 
                [], [], 
                '''                MEA
                ''',
                'mea',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('oorcd', REFERENCE_CLASS, 'Oorcd' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd', 
                [], [], 
                '''                OOR CD
                ''',
                'oorcd',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('osnr', REFERENCE_CLASS, 'Osnr' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr', 
                [], [], 
                '''                OSNR
                ''',
                'osnr',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('rx-lol', REFERENCE_CLASS, 'RxLol' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol', 
                [], [], 
                '''                RX LOL
                ''',
                'rx_lol',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('rx-los', REFERENCE_CLASS, 'RxLos' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos', 
                [], [], 
                '''                RX LOS
                ''',
                'rx_los',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tx-fault', REFERENCE_CLASS, 'TxFault' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault', 
                [], [], 
                '''                TX Fault
                ''',
                'tx_fault',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tx-lol', REFERENCE_CLASS, 'TxLol' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol', 
                [], [], 
                '''                TX LOL
                ''',
                'tx_lol',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tx-los', REFERENCE_CLASS, 'TxLos' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos', 
                [], [], 
                '''                TX LOS
                ''',
                'tx_los',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('wvlool', REFERENCE_CLASS, 'Wvlool' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool', 
                [], [], 
                '''                WVL OOL
                ''',
                'wvlool',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'optics-alarm-info',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo',
            False, 
            [
            _MetaInfoClassMember('cd', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Chromatic Dispersion ps/nm
                ''',
                'cd',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('cd-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Chromatic Dispersion high threshold ps/nm
                ''',
                'cd_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('cd-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Chromatic Dispersion low threshold ps/nm
                ''',
                'cd_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('cd-max', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Chromatic Dispersion Max ps/nm
                ''',
                'cd_max',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('cd-min', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Chromatic Dispersion Min ps/nm
                ''',
                'cd_min',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('cfg-tx-power', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Configured Tx power value
                ''',
                'cfg_tx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('controller-state', REFERENCE_ENUM_CLASS, 'OpticsControllerState_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsControllerState_Enum', 
                [], [], 
                '''                Optics controller state: Up, Down or
                Administratively Down
                ''',
                'controller_state',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('dgd-high-threshold', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                DGD high threshold in 0.1 ps
                ''',
                'dgd_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('differential-group-delay', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Differential Group Delay ps
                ''',
                'differential_group_delay',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('display-volt-temp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Display Volt/Temp ?
                ''',
                'display_volt_temp',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('dwdm-carrier-band', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                DWDM Carrier Band information
                ''',
                'dwdm_carrier_band',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('dwdm-carrier-channel', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Current ITU DWDM Carrier channel number
                ''',
                'dwdm_carrier_channel',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('dwdm-carrier-frequency', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                DWDM Carrier frequency read from hw in the unit
                0.01THz
                ''',
                'dwdm_carrier_frequency',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('dwdm-carrier-wavelength', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Wavelength of color optics 0.001nm
                ''',
                'dwdm_carrier_wavelength',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('form-factor', REFERENCE_ENUM_CLASS, 'OpticsFormFactor_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsFormFactor_Enum', 
                [], [], 
                '''                Optics form factor
                ''',
                'form_factor',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('grey-wavelength', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Wavelength of grey optics 0.01nm
                ''',
                'grey_wavelength',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('lane-data', REFERENCE_LIST, 'LaneData' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData', 
                [], [], 
                '''                Lane information
                ''',
                'lane_data',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-state', REFERENCE_ENUM_CLASS, 'OpticsLaserState_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsLaserState_Enum', 
                [], [], 
                '''                Showing laser state.Either ON or OFF or unknown
                ''',
                'laser_state',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('lbc-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                LBC High threshold value
                ''',
                'lbc_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('led-state', REFERENCE_ENUM_CLASS, 'OpticsLedState_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsLedState_Enum', 
                [], [], 
                '''                Showing Current Colour of led state
                ''',
                'led_state',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('network-srlg-info', REFERENCE_CLASS, 'NetworkSrlgInfo' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo', 
                [], [], 
                '''                Network SRLG information
                ''',
                'network_srlg_info',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('optical-signal-to-noise-ratio', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Optical Signal to Noise Ratio dB
                ''',
                'optical_signal_to_noise_ratio',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('optics-alarm-info', REFERENCE_CLASS, 'OpticsAlarmInfo' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo', 
                [], [], 
                '''                Optics Alarm Information
                ''',
                'optics_alarm_info',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('optics-module', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Optics module name
                ''',
                'optics_module',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('optics-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Optics Present?
                ''',
                'optics_present',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('optics-type', REFERENCE_ENUM_CLASS, 'Optics_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'Optics_Enum', 
                [], [], 
                '''                Optics type name
                ''',
                'optics_type',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('osnr-low-threshold', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSNR low threshold in 0.01 dB
                ''',
                'osnr_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('phase-noise', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Phase Noise dB
                ''',
                'phase_noise',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('phy-type', REFERENCE_ENUM_CLASS, 'OpticsPhy_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsPhy_Enum', 
                [], [], 
                '''                Optics physical type
                ''',
                'phy_type',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pm-enable', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                PmEable or Disable
                ''',
                'pm_enable',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('polarization-change-rate', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Polarization Change Rate rad/s
                ''',
                'polarization_change_rate',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('polarization-dependent-loss', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Polarization Dependent Loss dB
                ''',
                'polarization_dependent_loss',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('polarization-mode-dispersion', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Polarization Mode Dispersion 0.1ps
                ''',
                'polarization_mode_dispersion',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('rx-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Rx High threshold value
                ''',
                'rx_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('rx-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Rx Low threshold value
                ''',
                'rx_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('second-order-polarization-mode-dispersion', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Second Order Polarization Mode Dispersion 0
                .1ps^2
                ''',
                'second_order_polarization_mode_dispersion',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('temp-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Temp High threshold value
                ''',
                'temp_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('temp-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Temp Low threshold value
                ''',
                'temp_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('transport-admin-state', REFERENCE_ENUM_CLASS, 'OpticsTas_Enum' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsTas_Enum', 
                [], [], 
                '''                Transport Admin State
                ''',
                'transport_admin_state',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tx-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Tx High threshold value
                ''',
                'tx_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tx-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Tx Low threshold value
                ''',
                'tx_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('vendor-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Vendor Information
                ''',
                'vendor_info',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('volt-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Volt High threshold value
                ''',
                'volt_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('volt-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Volt Low threshold value
                ''',
                'volt_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'optics-info',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Port name
                ''',
                'name',
                'Cisco-IOS-XR-controller-optics-oper', True),
            _MetaInfoClassMember('optics-dwdm-carrrier-channel-map', REFERENCE_CLASS, 'OpticsDwdmCarrrierChannelMap' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap', 
                [], [], 
                '''                Optics operational data
                ''',
                'optics_dwdm_carrrier_channel_map',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('optics-info', REFERENCE_CLASS, 'OpticsInfo' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo', 
                [], [], 
                '''                Optics operational data
                ''',
                'optics_info',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'optics-port',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts',
            False, 
            [
            _MetaInfoClassMember('optics-port', REFERENCE_LIST, 'OpticsPort' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort', 
                [], [], 
                '''                Optics operational data
                ''',
                'optics_port',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'optics-ports',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper' : {
        'meta_info' : _MetaInfoClass('OpticsOper',
            False, 
            [
            _MetaInfoClassMember('optics-ports', REFERENCE_CLASS, 'OpticsPorts' , 'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts', 
                [], [], 
                '''                All Optics Port operational data
                ''',
                'optics_ports',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'optics-oper',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.controller.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
}
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap.DwdmCarrierMapInfo']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1lbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2lbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3lbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4lbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1lbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2lbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3lbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4lbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts']['meta_info']
_meta_table['OpticsOper.OpticsPorts']['meta_info'].parent =_meta_table['OpticsOper']['meta_info']
