


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SonetApplicationCodeEnum' : _MetaInfoEnum('SonetApplicationCodeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper',
        {
            'optics-sonet-not-set':'optics_sonet_not_set',
            'optics-vsr2000-3r2':'optics_vsr2000_3r2',
            'optics-vsr2000-3r3':'optics_vsr2000_3r3',
            'optics-vsr2000-3r5':'optics_vsr2000_3r5',
            'optics-sonet-undefined':'optics_sonet_undefined',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsAmplifierControlModeEnum' : _MetaInfoEnum('OpticsAmplifierControlModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper',
        {
            'automatic':'automatic',
            'manual':'manual',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsAmplifierSafetyControlModeEnum' : _MetaInfoEnum('OpticsAmplifierSafetyControlModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper',
        {
            'optics-amplifier-safety-mode-auto':'optics_amplifier_safety_mode_auto',
            'optics-amplifier-safety-mode-disabled':'optics_amplifier_safety_mode_disabled',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'EthernetPmdEnum' : _MetaInfoEnum('EthernetPmdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper',
        {
            'optics-eth-not-set':'optics_eth_not_set',
            'optics-eth-10gbase-lrm':'optics_eth_10gbase_lrm',
            'optics-eth-10gbase-lr':'optics_eth_10gbase_lr',
            'optics-eth-10gbase-zr':'optics_eth_10gbase_zr',
            'optics-eth-10gbase-er':'optics_eth_10gbase_er',
            'optics-eth-10gbase-sr':'optics_eth_10gbase_sr',
            'optics-eth-10gbase':'optics_eth_10gbase',
            'optics-eth-40gbase-cr4':'optics_eth_40gbase_cr4',
            'optics-eth-40gbase-sr4':'optics_eth_40gbase_sr4',
            'optics-eth-40gbase-lr4':'optics_eth_40gbase_lr4',
            'optics-eth-40gbase-er4':'optics_eth_40gbase_er4',
            'optics-eth-40gbase-psm4':'optics_eth_40gbase_psm4',
            'optics-eth-40gbase-csr4':'optics_eth_40gbase_csr4',
            'optics-eth-40gbase-sr-bd':'optics_eth_40gbase_sr_bd',
            'optics-eth-40g-aoc':'optics_eth_40g_aoc',
            'optics-eth-4x10gbase-lr':'optics_eth_4x10gbase_lr',
            'optics-eth-4x10gbase-sr':'optics_eth_4x10gbase_sr',
            'optics-eth-100g-aoc':'optics_eth_100g_aoc',
            'optics-eth-100g-acc':'optics_eth_100g_acc',
            'optics-eth-100gbase-sr10':'optics_eth_100gbase_sr10',
            'optics-eth-100gbase-sr4':'optics_eth_100gbase_sr4',
            'optics-eth-100gbase-lr4':'optics_eth_100gbase_lr4',
            'optics-eth-100gbase-er4':'optics_eth_100gbase_er4',
            'optics-eth-100gbase-cwdm4':'optics_eth_100gbase_cwdm4',
            'optics-eth-100gbase-clr4':'optics_eth_100gbase_clr4',
            'optics-eth-100gbase-psm4':'optics_eth_100gbase_psm4',
            'optics-eth-100gbase-cr4':'optics_eth_100gbase_cr4',
            'optics-eth-100gbase-al':'optics_eth_100gbase_al',
            'optics-eth-100gbase-pl':'optics_eth_100gbase_pl',
            'optics-eth-undefined':'optics_eth_undefined',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsPhyEnum' : _MetaInfoEnum('OpticsPhyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper',
        {
            'not-set':'not_set',
            'invalid':'invalid',
            'long-reach-four-lanes':'long_reach_four_lanes',
            'short-reach-ten-lanes':'short_reach_ten_lanes',
            'short-reach-one-lane':'short_reach_one_lane',
            'long-reach-one-lane':'long_reach_one_lane',
            'short-reach-four-lanes':'short_reach_four_lanes',
            'copper-four-lanes':'copper_four_lanes',
            'active-optical-cable':'active_optical_cable',
            'fourty-gig-e-long-reach-four-lanes':'fourty_gig_e_long_reach_four_lanes',
            'fourty-gig-e-short-reach-four-lanes':'fourty_gig_e_short_reach_four_lanes',
            'cwdm-four-lanes':'cwdm_four_lanes',
            'extended-reach-four-lanes':'extended_reach_four_lanes',
            'psm-four-lanes':'psm_four_lanes',
            'active-copper-cable':'active_copper_cable',
            'fourty-gig-e-extended-reach-four-lanes':'fourty_gig_e_extended_reach_four_lanes',
            'four-x-ten-gig-e-short-reach-one-lane':'four_x_ten_gig_e_short_reach_one_lane',
            'fourty-gig-epsm-four-lanes':'fourty_gig_epsm_four_lanes',
            'fourty-gig-e-copper-four-lanes':'fourty_gig_e_copper_four_lanes',
            'long-reach-mm-one-lane':'long_reach_mm_one_lane',
            'copper-short-reach':'copper_short_reach',
            'short-reach-srbd':'short_reach_srbd',
            'copper-one-lane':'copper_one_lane',
            'four-x-ten-gig-e-long-reach-one-lane':'four_x_ten_gig_e_long_reach_one_lane',
            'fourty-gig-eaoc-four-lanes':'fourty_gig_eaoc_four_lanes',
            'extended-one-lane':'extended_one_lane',
            'zr-one-lane':'zr_one_lane',
            'dwdm-one-lane':'dwdm_one_lane',
            'sx-one-lane':'sx_one_lane',
            'lx-one-lane':'lx_one_lane',
            'ex-one-lane':'ex_one_lane',
            'zx-one-lane':'zx_one_lane',
            'ba-set-one-lane':'ba_set_one_lane',
            'aoc-one-lane':'aoc_one_lane',
            'active-copper-one-lane':'active_copper_one_lane',
            'fourty-gig-eacu-four-lanes':'fourty_gig_eacu_four_lanes',
            'four-x-ten-gig-eacu-one-lanes':'four_x_ten_gig_eacu_one_lanes',
            'four-x-ten-gig-ecu-one-lanes':'four_x_ten_gig_ecu_one_lanes',
            'four-x-ten-gig-eaoc-one-lanes':'four_x_ten_gig_eaoc_one_lanes',
            'twenty-five-gig-short-reach-one-lane':'twenty_five_gig_short_reach_one_lane',
            'twenty-five-gig-long-reach-one-lane':'twenty_five_gig_long_reach_one_lane',
            'twenty-five-gig-extended-reach-one-lane':'twenty_five_gig_extended_reach_one_lane',
            'twenty-five-gig-copper-one-lane':'twenty_five_gig_copper_one_lane',
            'twenty-five-gig-active-optical-one-lane':'twenty_five_gig_active_optical_one_lane',
            'hundred-gig-edwdm-two':'hundred_gig_edwdm_two',
            'fourty-gig-plr4-four-lanes':'fourty_gig_plr4_four_lanes',
            'fourty-gig-esr4-four-lanes':'fourty_gig_esr4_four_lanes',
            'smsr-four-lanes':'smsr_four_lanes',
            'trunk-port-cfp2':'trunk_port_cfp2',
            'short-reach1-lane':'short_reach1_lane',
            'inmd-reach1lane':'inmd_reach1lane',
            'long-reach1-lane':'long_reach1_lane',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsAmplifierGainRangeEnum' : _MetaInfoEnum('OpticsAmplifierGainRangeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper',
        {
            'optics-amplifier-gain-range-normal':'optics_amplifier_gain_range_normal',
            'optics-amplifier-gain-range-ext-end-ed':'optics_amplifier_gain_range_ext_end_ed',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsTasEnum' : _MetaInfoEnum('OpticsTasEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper',
        {
            'tas-ui-oos':'tas_ui_oos',
            'tas-ui-main':'tas_ui_main',
            'tas-ui-is':'tas_ui_is',
            'tas-ui-ains':'tas_ui_ains',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OtnApplicationCodeEnum' : _MetaInfoEnum('OtnApplicationCodeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper',
        {
            'optics-not-set':'optics_not_set',
            'optics-p1l1-2d1':'optics_p1l1_2d1',
            'optics-p1s1-2d2':'optics_p1s1_2d2',
            'optics-p1l1-2d2':'optics_p1l1_2d2',
            'optics-undefined':'optics_undefined',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsPortEnum' : _MetaInfoEnum('OpticsPortEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper',
        {
            'com':'com',
            'line':'line',
            'osc':'osc',
            'com-check':'com_check',
            'work':'work',
            'prot':'prot',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'FiberConnectorEnum' : _MetaInfoEnum('FiberConnectorEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper',
        {
            'optics-connect-or-not-set':'optics_connect_or_not_set',
            'optics-sc-connect-or':'optics_sc_connect_or',
            'optics-lc-connect-or':'optics_lc_connect_or',
            'optics-mpo-connect-or':'optics_mpo_connect_or',
            'optics-undefined-connect-or':'optics_undefined_connect_or',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsControllerStateEnum' : _MetaInfoEnum('OpticsControllerStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper',
        {
            'optics-state-up':'optics_state_up',
            'optics-state-down':'optics_state_down',
            'optics-state-admin-down':'optics_state_admin_down',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsFecEnum' : _MetaInfoEnum('OpticsFecEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper',
        {
            'fec-none':'fec_none',
            'fec-hg15':'fec_hg15',
            'fec-hg25':'fec_hg25',
            'fec-hg15-de':'fec_hg15_de',
            'fec-hg25-de':'fec_hg25_de',
            'fec-enabled':'fec_enabled',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsPortStatusEnum' : _MetaInfoEnum('OpticsPortStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper',
        {
            'active':'active',
            'standby':'standby',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsWaveBandEnum' : _MetaInfoEnum('OpticsWaveBandEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper',
        {
            'c-band':'c_band',
            'l-band':'l_band',
            'c-band-odd':'c_band_odd',
            'c-band-even':'c_band_even',
            'invalid-band':'invalid_band',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsLedStateEnum' : _MetaInfoEnum('OpticsLedStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper',
        {
            'off':'off',
            'green-on':'green_on',
            'green-flashing':'green_flashing',
            'yellow-on':'yellow_on',
            'yellow-flashing':'yellow_flashing',
            'red-on':'red_on',
            'red-flashing':'red_flashing',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsFormFactorEnum' : _MetaInfoEnum('OpticsFormFactorEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper',
        {
            'not-set':'not_set',
            'invalid':'invalid',
            'cpak':'cpak',
            'cxp':'cxp',
            'sfp-plus':'sfp_plus',
            'qsfp':'qsfp',
            'qsfp-plus':'qsfp_plus',
            'qsfp28':'qsfp28',
            'sfp':'sfp',
            'cfp':'cfp',
            'cfp2':'cfp2',
            'cfp4':'cfp4',
            'xfp':'xfp',
            'x2':'x2',
            'non-pluggable':'non_pluggable',
            'other':'other',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsLaserStateEnum' : _MetaInfoEnum('OpticsLaserStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper',
        {
            'on':'on',
            'off':'off',
            'unknown':'unknown',
            'apr':'apr',
        }, 'Cisco-IOS-XR-controller-optics-oper', _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper']),
    'OpticsEnum' : _MetaInfoEnum('OpticsEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper',
        {
            'optics-unknown':'optics_unknown',
            'optics-grey':'optics_grey',
            'optics-dwdm':'optics_dwdm',
            'optics-cwdm':'optics_cwdm',
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
                [('-2147483648', '2147483647')], [], 
                '''                G694 channel number
                ''',
                'g694_chan_num',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('itu-chan-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap',
            False, 
            [
            _MetaInfoClassMember('dwdm-carrier-band', REFERENCE_ENUM_CLASS, 'OpticsWaveBandEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsWaveBandEnum', 
                [], [], 
                '''                DWDM carrier band
                ''',
                'dwdm_carrier_band',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('dwdm-carrier-map-info', REFERENCE_LIST, 'DwdmCarrierMapInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap.DwdmCarrierMapInfo', 
                [], [], 
                '''                DWDM carrier mapping info
                ''',
                'dwdm_carrier_map_info',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('dwdm-carrier-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Highest DWDM carrier supported
                ''',
                'dwdm_carrier_max',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('dwdm-carrier-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Lowest DWDM carrier supported
                ''',
                'dwdm_carrier_min',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'optics-dwdm-carrrier-channel-map',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray',
            False, 
            [
            _MetaInfoClassMember('network-srlg', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Network Srlg
                ''',
                'network_srlg',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('set-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Array to maintain set number
                ''',
                'set_number',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'network-srlg-array',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo',
            False, 
            [
            _MetaInfoClassMember('network-srlg-array', REFERENCE_LIST, 'NetworkSrlgArray' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray', 
                [], [], 
                '''                Network Srlg Array
                ''',
                'network_srlg_array',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'network-srlg-info',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Lbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Lbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Lbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Lbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Lbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Lbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Lbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Lbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Lbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Lbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Lbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Lbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Lbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Lbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Lbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Lbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
            'rx-loc',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
            'amp-gain-deg-low',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
            'amp-gain-deg-high',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo',
            False, 
            [
            _MetaInfoClassMember('amp-gain-deg-high', REFERENCE_CLASS, 'AmpGainDegHigh' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh', 
                [], [], 
                '''                Ampli Gain Deg High
                ''',
                'amp_gain_deg_high',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('amp-gain-deg-low', REFERENCE_CLASS, 'AmpGainDegLow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow', 
                [], [], 
                '''                Ampli Gain Deg Low
                ''',
                'amp_gain_deg_low',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('hidgd', REFERENCE_CLASS, 'Hidgd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd', 
                [], [], 
                '''                HI DGD
                ''',
                'hidgd',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-lbc', REFERENCE_CLASS, 'HighLbc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc', 
                [], [], 
                '''                High laser bias current in units of percentage
                ''',
                'high_lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-rx1-power', REFERENCE_CLASS, 'HighRx1Power' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power', 
                [], [], 
                '''                High Rx1 Power in uints of 0.1 dBm
                ''',
                'high_rx1_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-rx2-power', REFERENCE_CLASS, 'HighRx2Power' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power', 
                [], [], 
                '''                High Rx2 Power in uints of 0.1 dBm
                ''',
                'high_rx2_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-rx3-power', REFERENCE_CLASS, 'HighRx3Power' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power', 
                [], [], 
                '''                High Rx3 Power in uints of 0.1 dBm
                ''',
                'high_rx3_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-rx4-power', REFERENCE_CLASS, 'HighRx4Power' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power', 
                [], [], 
                '''                High Rx4 Power in uints of 0.1 dBm
                ''',
                'high_rx4_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-rx-power', REFERENCE_CLASS, 'HighRxPower' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower', 
                [], [], 
                '''                High Rx Power in uints of 0.1 dBm
                ''',
                'high_rx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx1-power', REFERENCE_CLASS, 'HighTx1Power' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power', 
                [], [], 
                '''                High Tx1 Power in uints of 0.1 dBm
                ''',
                'high_tx1_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx1lbc', REFERENCE_CLASS, 'HighTx1Lbc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Lbc', 
                [], [], 
                '''                High Tx1 laser bias current in units of
                percentage
                ''',
                'high_tx1lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx2-power', REFERENCE_CLASS, 'HighTx2Power' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power', 
                [], [], 
                '''                High Tx2 Power in uints of 0.1 dBm
                ''',
                'high_tx2_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx2lbc', REFERENCE_CLASS, 'HighTx2Lbc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Lbc', 
                [], [], 
                '''                High Tx2 laser bias current in units of
                percentage
                ''',
                'high_tx2lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx3-power', REFERENCE_CLASS, 'HighTx3Power' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power', 
                [], [], 
                '''                High Tx3 Power in uints of 0.1 dBm
                ''',
                'high_tx3_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx3lbc', REFERENCE_CLASS, 'HighTx3Lbc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Lbc', 
                [], [], 
                '''                High Tx3 laser bias current in units of
                percentage
                ''',
                'high_tx3lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx4-power', REFERENCE_CLASS, 'HighTx4Power' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power', 
                [], [], 
                '''                High Tx4 Power in uints of 0.1 dBm
                ''',
                'high_tx4_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx4lbc', REFERENCE_CLASS, 'HighTx4Lbc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Lbc', 
                [], [], 
                '''                High Tx4 laser bias current in units of
                percentage
                ''',
                'high_tx4lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx-power', REFERENCE_CLASS, 'HighTxPower' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower', 
                [], [], 
                '''                High Tx Power in uints of 0.1 dBm
                ''',
                'high_tx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('imp-removal', REFERENCE_CLASS, 'ImpRemoval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval', 
                [], [], 
                '''                IMPROPER REM
                ''',
                'imp_removal',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-rx1-power', REFERENCE_CLASS, 'LowRx1Power' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power', 
                [], [], 
                '''                Low Rx1 Power in uints of 0.1 dBm
                ''',
                'low_rx1_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-rx2-power', REFERENCE_CLASS, 'LowRx2Power' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power', 
                [], [], 
                '''                Low Rx2 Power in uints of 0.1 dBm
                ''',
                'low_rx2_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-rx3-power', REFERENCE_CLASS, 'LowRx3Power' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power', 
                [], [], 
                '''                Low Rx3 Power in uints of 0.1 dBm
                ''',
                'low_rx3_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-rx4-power', REFERENCE_CLASS, 'LowRx4Power' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power', 
                [], [], 
                '''                Low Rx4 Power in uints of 0.1 dBm
                ''',
                'low_rx4_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-rx-power', REFERENCE_CLASS, 'LowRxPower' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower', 
                [], [], 
                '''                Low Rx Power in uints of 0.1 dBm
                ''',
                'low_rx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx1-power', REFERENCE_CLASS, 'LowTx1Power' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power', 
                [], [], 
                '''                Low Tx1 Power in uints of 0.1 dBm
                ''',
                'low_tx1_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx1lbc', REFERENCE_CLASS, 'LowTx1Lbc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Lbc', 
                [], [], 
                '''                Low Tx1 laser bias current in units of
                percentage
                ''',
                'low_tx1lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx2-power', REFERENCE_CLASS, 'LowTx2Power' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power', 
                [], [], 
                '''                Low Tx2 Power in uints of 0.1 dBm
                ''',
                'low_tx2_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx2lbc', REFERENCE_CLASS, 'LowTx2Lbc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Lbc', 
                [], [], 
                '''                Low Tx2 laser bias current in units of
                percentage
                ''',
                'low_tx2lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx3-power', REFERENCE_CLASS, 'LowTx3Power' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power', 
                [], [], 
                '''                Low Tx3 Power in uints of 0.1 dBm
                ''',
                'low_tx3_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx3lbc', REFERENCE_CLASS, 'LowTx3Lbc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Lbc', 
                [], [], 
                '''                Low Tx3 laser bias current in units of
                percentage
                ''',
                'low_tx3lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx4-power', REFERENCE_CLASS, 'LowTx4Power' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power', 
                [], [], 
                '''                Low Tx4 Power in uints of 0.1 dBm
                ''',
                'low_tx4_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx4lbc', REFERENCE_CLASS, 'LowTx4Lbc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Lbc', 
                [], [], 
                '''                Low Tx4 laser bias current in units of
                percentage
                ''',
                'low_tx4lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx-power', REFERENCE_CLASS, 'LowTxPower' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower', 
                [], [], 
                '''                Low Tx Power in uints of 0.1 dBm
                ''',
                'low_tx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('mea', REFERENCE_CLASS, 'Mea' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea', 
                [], [], 
                '''                MEA
                ''',
                'mea',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('oorcd', REFERENCE_CLASS, 'Oorcd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd', 
                [], [], 
                '''                OOR CD
                ''',
                'oorcd',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('osnr', REFERENCE_CLASS, 'Osnr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr', 
                [], [], 
                '''                OSNR
                ''',
                'osnr',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('rx-loc', REFERENCE_CLASS, 'RxLoc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc', 
                [], [], 
                '''                Rx LOC
                ''',
                'rx_loc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('rx-lol', REFERENCE_CLASS, 'RxLol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol', 
                [], [], 
                '''                RX LOL
                ''',
                'rx_lol',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('rx-los', REFERENCE_CLASS, 'RxLos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos', 
                [], [], 
                '''                RX LOS
                ''',
                'rx_los',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tx-fault', REFERENCE_CLASS, 'TxFault' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault', 
                [], [], 
                '''                TX Fault
                ''',
                'tx_fault',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tx-lol', REFERENCE_CLASS, 'TxLol' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol', 
                [], [], 
                '''                TX LOL
                ''',
                'tx_lol',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tx-los', REFERENCE_CLASS, 'TxLos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos', 
                [], [], 
                '''                TX LOS
                ''',
                'tx_los',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('wvlool', REFERENCE_CLASS, 'Wvlool' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool', 
                [], [], 
                '''                WVL OOL
                ''',
                'wvlool',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'optics-alarm-info',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
            'rx-los-p',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
            'rx-loc',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
            'amp-gain-deg-low',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
            'amp-gain-deg-high',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
            'auto-laser-shut',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
            'auto-power-red',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
            'auto-ampli-ctrl-disabled',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
            'auto-ampli-ctrl-config-mismatch',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
            'switch-to-protect',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo',
            False, 
            [
            _MetaInfoClassMember('amp-gain-deg-high', REFERENCE_CLASS, 'AmpGainDegHigh' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh', 
                [], [], 
                '''                Ampli Gain Deg High
                ''',
                'amp_gain_deg_high',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('amp-gain-deg-low', REFERENCE_CLASS, 'AmpGainDegLow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow', 
                [], [], 
                '''                Ampli Gain Deg Low
                ''',
                'amp_gain_deg_low',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('auto-ampli-ctrl-config-mismatch', REFERENCE_CLASS, 'AutoAmpliCtrlConfigMismatch' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch', 
                [], [], 
                '''                Auto Ampli Ctrl Config Mismatch
                ''',
                'auto_ampli_ctrl_config_mismatch',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('auto-ampli-ctrl-disabled', REFERENCE_CLASS, 'AutoAmpliCtrlDisabled' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled', 
                [], [], 
                '''                Auto Ampli Ctrl Disabled
                ''',
                'auto_ampli_ctrl_disabled',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('auto-laser-shut', REFERENCE_CLASS, 'AutoLaserShut' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut', 
                [], [], 
                '''                Auto Laser Shut
                ''',
                'auto_laser_shut',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('auto-power-red', REFERENCE_CLASS, 'AutoPowerRed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed', 
                [], [], 
                '''                Auto Power Red
                ''',
                'auto_power_red',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-rx-power', REFERENCE_CLASS, 'LowRxPower' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower', 
                [], [], 
                '''                Low Rx Power in uints of 0.1 dBm
                ''',
                'low_rx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx-power', REFERENCE_CLASS, 'LowTxPower' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower', 
                [], [], 
                '''                Low Tx Power in uints of 0.1 dBm
                ''',
                'low_tx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('rx-loc', REFERENCE_CLASS, 'RxLoc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc', 
                [], [], 
                '''                Rx LOC
                ''',
                'rx_loc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('rx-los-p', REFERENCE_CLASS, 'RxLosP' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP', 
                [], [], 
                '''                Rx LOS_P
                ''',
                'rx_los_p',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('switch-to-protect', REFERENCE_CLASS, 'SwitchToProtect' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect', 
                [], [], 
                '''                Switch To Protect
                ''',
                'switch_to_protect',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'ots-alarm-info',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo',
            False, 
            [
            _MetaInfoClassMember('connector-type', REFERENCE_ENUM_CLASS, 'FiberConnectorEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'FiberConnectorEnum', 
                [], [], 
                '''                Connector type
                ''',
                'connector_type',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('date', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Date in Transceiver
                ''',
                'date',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('ethernet-compliance-code', REFERENCE_ENUM_CLASS, 'EthernetPmdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'EthernetPmdEnum', 
                [], [], 
                '''                Ethernet Compliance Code
                ''',
                'ethernet_compliance_code',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('internal-temperature', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Internal Temperature in C
                ''',
                'internal_temperature',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('optics-serial-no', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Transceiver serial number
                ''',
                'optics_serial_no',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('optics-vendor-part', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Transceiver vendors part number
                ''',
                'optics_vendor_part',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('optics-vendor-rev', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Transceiver vendors revision number
                ''',
                'optics_vendor_rev',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('otn-application-code', REFERENCE_ENUM_CLASS, 'OtnApplicationCodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OtnApplicationCodeEnum', 
                [], [], 
                '''                Otn Application Code
                ''',
                'otn_application_code',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('sonet-application-code', REFERENCE_ENUM_CLASS, 'SonetApplicationCodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'SonetApplicationCodeEnum', 
                [], [], 
                '''                Sonet Application Code
                ''',
                'sonet_application_code',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('vendor-info', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Vendor Information
                ''',
                'vendor_info',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'transceiver-info',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal',
            False, 
            [
            _MetaInfoClassMember('isi-correction-lane1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Inter symbol Interference correction on Lane 1
                ''',
                'isi_correction_lane1',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('isi-correction-lane2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Inter symbol Interference correction on Lane 2
                ''',
                'isi_correction_lane2',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-diff-frequency-lane1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Difference between target and actual center
                frequency on Lane 1
                ''',
                'laser_diff_frequency_lane1',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-diff-frequency-lane2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Difference between target and actual center
                frequency on Lane 2
                ''',
                'laser_diff_frequency_lane2',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-diff-temperature-lane1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Difference between target and actual temperature
                on Lane 1
                ''',
                'laser_diff_temperature_lane1',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-diff-temperature-lane2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Difference between target and actual temperature
                on Lane 2
                ''',
                'laser_diff_temperature_lane2',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pam-rate-lane1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                PAM Histogram parameter on Lane 1
                ''',
                'pam_rate_lane1',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pam-rate-lane2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                PAM Histogram parameter on Lane 2
                ''',
                'pam_rate_lane2',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Pre FEC BER since last counter reset
                ''',
                'pre_fec_ber',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-accumulated', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Pre FEC BER value prior accumulation period,
                line ingress
                ''',
                'pre_fec_ber_accumulated',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-instantaneous', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Pre FEC BER value instantaneous line ingress
                ''',
                'pre_fec_ber_instantaneous',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-latched-max', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Latched maximum Pre FEC BER value since last
                read, line ingress
                ''',
                'pre_fec_ber_latched_max',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-latched-min', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Latched minimum Pre FEC BER value since last
                read, line ingress
                ''',
                'pre_fec_ber_latched_min',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('snr-lane1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Signal to Noise Ratio on Lane 1
                ''',
                'snr_lane1',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('snr-lane2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Signal to Noise Ratio on Lane 2
                ''',
                'snr_lane2',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tec-current-lane1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Current flowing to the TEC of a cooled laser on
                Lane 1
                ''',
                'tec_current_lane1',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tec-current-lane2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Current flowing to the TEC of a cooled laser on
                Lane 2
                ''',
                'tec_current_lane2',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Uncorrected BER since last counter reset
                ''',
                'uncorrected_ber',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-accumulated', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Uncorrected BER value prior accumulation period,
                line ingress
                ''',
                'uncorrected_ber_accumulated',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-instantaneous', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Uncorrected BER value instantaneous line line
                ingress
                ''',
                'uncorrected_ber_instantaneous',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-latched-max', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Latched maximum Uncorrected BER value since last
                read, line ingress
                ''',
                'uncorrected_ber_latched_max',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-latched-min', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Latched minimum Uncorrected BER value since last
                read, line ingress
                ''',
                'uncorrected_ber_latched_min',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'ext-param-val',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal',
            False, 
            [
            _MetaInfoClassMember('isi-correction-alarm-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold alarm for ISI Correction
                ''',
                'isi_correction_alarm_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('isi-correction-alarm-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold alarm for ISI Correction
                ''',
                'isi_correction_alarm_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('isi-correction-warn-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold warning for ISI Correction
                ''',
                'isi_correction_warn_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('isi-correction-warn-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold warning for ISI Correction
                ''',
                'isi_correction_warn_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-diff-frequency-alarm-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High Threshold Alarm for Differential Laser
                Frequency
                ''',
                'laser_diff_frequency_alarm_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-diff-frequency-alarm-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low Threshold Alarm for Differential Laser
                Frequency
                ''',
                'laser_diff_frequency_alarm_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-diff-frequency-warn-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High Threshold Warning for Differential Laser
                Frequency
                ''',
                'laser_diff_frequency_warn_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-diff-frequency-warn-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low Threshold Warning for Differential Laser
                Frequency
                ''',
                'laser_diff_frequency_warn_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-diff-temperature-alarm-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High Threshold Alarm for Differential Laser
                Temperature
                ''',
                'laser_diff_temperature_alarm_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-diff-temperature-alarm-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low Threshold Alarm for Differential Laser
                Temperature
                ''',
                'laser_diff_temperature_alarm_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-diff-temperature-warn-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High Threshold Warning for Differential Laser
                Temperature
                ''',
                'laser_diff_temperature_warn_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-diff-temperature-warn-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low Threshold Warning for Differential Laser
                Temperature
                ''',
                'laser_diff_temperature_warn_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pam-rate-alarm-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold alarm for PAM Rate
                ''',
                'pam_rate_alarm_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pam-rate-alarm-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold alarm for PAM Rate
                ''',
                'pam_rate_alarm_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pam-rate-warn-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold warning for PAM Rate
                ''',
                'pam_rate_warn_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pam-rate-warn-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold warning for PAM Rate
                ''',
                'pam_rate_warn_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-accumulated-alarm-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold alarm for Accumulated Pre FEC BER
                ''',
                'pre_fec_ber_accumulated_alarm_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-accumulated-alarm-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold alarm for Accumulated Pre FEC BER
                ''',
                'pre_fec_ber_accumulated_alarm_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-accumulated-warn-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold warning for Accumulated Pre FEC
                BER
                ''',
                'pre_fec_ber_accumulated_warn_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-accumulated-warn-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold warning for Accumulated Pre FEC
                BER
                ''',
                'pre_fec_ber_accumulated_warn_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-alarm-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold alarm for Pre FEC BER
                ''',
                'pre_fec_ber_alarm_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-alarm-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold alarm for Pre FEC BER
                ''',
                'pre_fec_ber_alarm_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-instantaneous-alarm-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold alarm for Instantaneous Pre FEC
                BER
                ''',
                'pre_fec_ber_instantaneous_alarm_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-instantaneous-alarm-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold alarm for Instantaneous Pre FEC
                BER
                ''',
                'pre_fec_ber_instantaneous_alarm_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-instantaneous-warn-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold warning for Instantaneous Pre FEC
                BER
                ''',
                'pre_fec_ber_instantaneous_warn_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-instantaneous-warn-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold warning for Instantaneous Pre FEC
                BER
                ''',
                'pre_fec_ber_instantaneous_warn_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-latched-max-alarm-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold alarm for Latched Max Pre FEC BER
                ''',
                'pre_fec_ber_latched_max_alarm_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-latched-max-alarm-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold alarm for Latched Max Pre FEC BER
                ''',
                'pre_fec_ber_latched_max_alarm_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-latched-max-warn-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold warning for Latched Max Pre FEC
                BER
                ''',
                'pre_fec_ber_latched_max_warn_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-latched-max-warn-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold warning for Latched Max Pre FEC
                BER
                ''',
                'pre_fec_ber_latched_max_warn_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-latched-min-alarm-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold alarm for Latched Min Pre FEC BER
                ''',
                'pre_fec_ber_latched_min_alarm_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-latched-min-alarm-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold alarm for Latched Min Pre FEC BER
                ''',
                'pre_fec_ber_latched_min_alarm_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-latched-min-warn-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold warning for Latched Min Pre FEC
                BER
                ''',
                'pre_fec_ber_latched_min_warn_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-latched-min-warn-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold warning for Latched Min Pre FEC
                BER
                ''',
                'pre_fec_ber_latched_min_warn_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-warn-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold warning for Pre FEC BER
                ''',
                'pre_fec_ber_warn_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pre-fec-ber-warn-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold warning for Pre FEC BER
                ''',
                'pre_fec_ber_warn_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('snr-alarm-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold alarm for SNR
                ''',
                'snr_alarm_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('snr-alarm-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold alarm for SNR
                ''',
                'snr_alarm_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('snr-warn-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold warning for SNR
                ''',
                'snr_warn_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('snr-warn-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold warning for SNR
                ''',
                'snr_warn_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tec-current-alarm-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold alarm for TEC Current
                ''',
                'tec_current_alarm_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tec-current-alarm-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold alarm for TEC Current
                ''',
                'tec_current_alarm_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tec-current-warn-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold warning for TEC Current
                ''',
                'tec_current_warn_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tec-current-warn-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold warning for TEC Current
                ''',
                'tec_current_warn_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-accumulated-alarm-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold alarm for Accumulated Uncorrected
                BER
                ''',
                'uncorrected_ber_accumulated_alarm_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-accumulated-alarm-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold alarm for Accumulated Uncorrected
                BER
                ''',
                'uncorrected_ber_accumulated_alarm_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-accumulated-warn-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold warning for Accumulated
                Uncorrected BER
                ''',
                'uncorrected_ber_accumulated_warn_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-accumulated-warn-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold warning for Accumulated
                Uncorrected BER
                ''',
                'uncorrected_ber_accumulated_warn_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-alarm-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold alarm for Uncorrected BER
                ''',
                'uncorrected_ber_alarm_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-alarm-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold alarm for Uncorrected BER
                ''',
                'uncorrected_ber_alarm_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-instantaneous-alarm-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold alarm for Instantaneous
                Uncorrected BER
                ''',
                'uncorrected_ber_instantaneous_alarm_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-instantaneous-alarm-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold alarm for Instantaneous
                Uncorrected BER
                ''',
                'uncorrected_ber_instantaneous_alarm_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-instantaneous-warn-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold warning for Instantaneous
                Uncorrected BER
                ''',
                'uncorrected_ber_instantaneous_warn_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-instantaneous-warn-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold warning for Instantaneous
                Uncorrected BER
                ''',
                'uncorrected_ber_instantaneous_warn_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-latched-max-alarm-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold alarm for Latched_Max Uncorrected
                BER
                ''',
                'uncorrected_ber_latched_max_alarm_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-latched-max-alarm-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold alarm for Latched_Max Uncorrected
                BER
                ''',
                'uncorrected_ber_latched_max_alarm_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-latched-max-warn-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold warning Latched_Max for
                Uncorrected BER
                ''',
                'uncorrected_ber_latched_max_warn_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-latched-max-warn-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold warning Latched_Max for
                Uncorrected BER
                ''',
                'uncorrected_ber_latched_max_warn_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-latched-min-alarm-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold alarm for  Latched Min
                Uncorrected BER
                ''',
                'uncorrected_ber_latched_min_alarm_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-latched-min-alarm-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold alarm for  Latched Min Uncorrected
                BER
                ''',
                'uncorrected_ber_latched_min_alarm_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-latched-min-warn-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold warning for  Latched Min
                Uncorrected BER
                ''',
                'uncorrected_ber_latched_min_warn_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-latched-min-warn-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold alarm for Latched Min Uncorrected
                BER
                ''',
                'uncorrected_ber_latched_min_warn_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-warn-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                High threshold warning for Uncorrected BER
                ''',
                'uncorrected_ber_warn_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('uncorrected-ber-warn-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Low threshold warning for Uncorrected BER
                ''',
                'uncorrected_ber_warn_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'ext-param-threshold-val',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo',
            False, 
            [
            _MetaInfoClassMember('high-lbc', REFERENCE_CLASS, 'HighLbc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc', 
                [], [], 
                '''                High laser bias current
                ''',
                'high_lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-rx-power', REFERENCE_CLASS, 'HighRxPower' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower', 
                [], [], 
                '''                High Rx Power
                ''',
                'high_rx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx-power', REFERENCE_CLASS, 'HighTxPower' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower', 
                [], [], 
                '''                High Tx Power
                ''',
                'high_tx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-rx-power', REFERENCE_CLASS, 'LowRxPower' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower', 
                [], [], 
                '''                Low Rx Power
                ''',
                'low_rx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx-power', REFERENCE_CLASS, 'LowTxPower' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower', 
                [], [], 
                '''                Low Tx Power
                ''',
                'low_tx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'lane-alarm-info',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData',
            False, 
            [
            _MetaInfoClassMember('lane-alarm-info', REFERENCE_CLASS, 'LaneAlarmInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo', 
                [], [], 
                '''                Lane Alarm Information
                ''',
                'lane_alarm_info',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('lane-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The index number of the lane
                ''',
                'lane_index',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-bias-current-milli-amps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Laser Bias Current in units of 0.01mA
                ''',
                'laser_bias_current_milli_amps',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-bias-current-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Laser Bias Current in units of 0.01 percentage
                ''',
                'laser_bias_current_percent',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('output-frequency', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Output frequency read from hw in the unit 0
                .01THz
                ''',
                'output_frequency',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('receive-power', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Transponder receive power in the unit of 0.01dBm
                ''',
                'receive_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('receive-signal-power', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Transponder receive signal power in the unit of
                0.01dBm
                ''',
                'receive_signal_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('transmit-power', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Transmit power in the unit of 0.01dBm
                ''',
                'transmit_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('transmit-signal-power', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Transmit Signal power in the unit of 0.01dBm
                ''',
                'transmit_signal_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'lane-data',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsInfo',
            False, 
            [
            _MetaInfoClassMember('alarm-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Are there any alarms ?
                ''',
                'alarm_detected',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('ampli-channel-power-config-val', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ampli channel power config val
                ''',
                'ampli_channel_power_config_val',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('ampli-control-mode-config-val', REFERENCE_ENUM_CLASS, 'OpticsAmplifierControlModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsAmplifierControlModeEnum', 
                [], [], 
                '''                ampli control mode config val
                ''',
                'ampli_control_mode_config_val',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('ampli-gain', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Ampli Gain in the unit of 0.01dBm
                ''',
                'ampli_gain',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('ampli-gain-config-val', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ampli gain config val
                ''',
                'ampli_gain_config_val',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('ampli-gain-range-config-val', REFERENCE_ENUM_CLASS, 'OpticsAmplifierGainRangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsAmplifierGainRangeEnum', 
                [], [], 
                '''                ampli gain range config val
                ''',
                'ampli_gain_range_config_val',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('ampli-gain-thr-deg-high-config-val', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ampli gain thr deg high config val
                ''',
                'ampli_gain_thr_deg_high_config_val',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('ampli-gain-thr-deg-low-config-val', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ampli gain thr deg low config val
                ''',
                'ampli_gain_thr_deg_low_config_val',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('ampli-tilt', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Ampli Tilt in the unit of 0.01dBm
                ''',
                'ampli_tilt',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('ampli-tilt-config-val', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                ampli tilt config val
                ''',
                'ampli_tilt_config_val',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('cd', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Chromatic Dispersion ps/nm
                ''',
                'cd',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('cd-configurable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                CD Configurable is supported or not
                ''',
                'cd_configurable',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('cd-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Chromatic Dispersion high threshold ps/nm
                ''',
                'cd_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('cd-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Chromatic Dispersion low threshold ps/nm
                ''',
                'cd_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('cd-max', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Chromatic Dispersion Max ps/nm
                ''',
                'cd_max',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('cd-min', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Chromatic Dispersion Min ps/nm
                ''',
                'cd_min',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('cfg-tx-power', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Configured Tx power value in 0.01 dB
                ''',
                'cfg_tx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('cfg-tx-power-configurable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TX Power Configuration is supported or not
                ''',
                'cfg_tx_power_configurable',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('channel-power-max-delta-config-val', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                channel power max delta config val
                ''',
                'channel_power_max_delta_config_val',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('controller-state', REFERENCE_ENUM_CLASS, 'OpticsControllerStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsControllerStateEnum', 
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
            _MetaInfoClassMember('dwdm-carrier-band', REFERENCE_ENUM_CLASS, 'OpticsWaveBandEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsWaveBandEnum', 
                [], [], 
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
            _MetaInfoClassMember('ext-param-threshold-val', REFERENCE_CLASS, 'ExtParamThresholdVal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal', 
                [], [], 
                '''                Extended optics parameters threshold values
                ''',
                'ext_param_threshold_val',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('ext-param-val', REFERENCE_CLASS, 'ExtParamVal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal', 
                [], [], 
                '''                Extended optics parameters
                ''',
                'ext_param_val',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('form-factor', REFERENCE_ENUM_CLASS, 'OpticsFormFactorEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsFormFactorEnum', 
                [], [], 
                '''                Optics form factor
                ''',
                'form_factor',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('grey-wavelength', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Wavelength of grey optics 0.01nm
                ''',
                'grey_wavelength',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-bo-configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is BO configured ?
                ''',
                'is_bo_configured',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('is-ext-param-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Are the Extended Parameters Valid ?
                ''',
                'is_ext_param_valid',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('lane-data', REFERENCE_LIST, 'LaneData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData', 
                [], [], 
                '''                Lane information
                ''',
                'lane_data',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-state', REFERENCE_ENUM_CLASS, 'OpticsLaserStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsLaserStateEnum', 
                [], [], 
                '''                Showing laser state.Either ON or OFF or unknown
                ''',
                'laser_state',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('lbc-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                LBC High threshold value in units of percentage
                ''',
                'lbc_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('lbc-th-high-default', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                LBC high threshold default value in unit of 0
                .001mA
                ''',
                'lbc_th_high_default',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('lbc-th-high-warning-default', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                LBC high Warning threshold default value in unit
                of 0.001mA
                ''',
                'lbc_th_high_warning_default',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('lbc-th-low-default', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                LBC low threshold default value in units of 0
                .001mA
                ''',
                'lbc_th_low_default',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('lbc-th-low-warning-default', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                LBC low warning threshold default value in units
                of 0.001mA
                ''',
                'lbc_th_low_warning_default',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('led-state', REFERENCE_ENUM_CLASS, 'OpticsLedStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsLedStateEnum', 
                [], [], 
                '''                Showing Current Colour of led state
                ''',
                'led_state',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('network-srlg-info', REFERENCE_CLASS, 'NetworkSrlgInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo', 
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
            _MetaInfoClassMember('optics-alarm-info', REFERENCE_CLASS, 'OpticsAlarmInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo', 
                [], [], 
                '''                Optics Alarm Information
                ''',
                'optics_alarm_info',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('optics-fec', REFERENCE_ENUM_CLASS, 'OpticsFecEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsFecEnum', 
                [], [], 
                '''                Optics FEC
                ''',
                'optics_fec',
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
            _MetaInfoClassMember('optics-type', REFERENCE_ENUM_CLASS, 'OpticsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsEnum', 
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
            _MetaInfoClassMember('osri-config-val', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                osri config val
                ''',
                'osri_config_val',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('ots-alarm-info', REFERENCE_CLASS, 'OtsAlarmInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo', 
                [], [], 
                '''                Ots Alarm Information
                ''',
                'ots_alarm_info',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('phase-noise', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Phase Noise dB
                ''',
                'phase_noise',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('phy-type', REFERENCE_ENUM_CLASS, 'OpticsPhyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsPhyEnum', 
                [], [], 
                '''                Optics physical type
                ''',
                'phy_type',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('pm-enable', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
            _MetaInfoClassMember('port-status', REFERENCE_ENUM_CLASS, 'OpticsPortStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsPortStatusEnum', 
                [], [], 
                '''                Showing port status
                ''',
                'port_status',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('port-type', REFERENCE_ENUM_CLASS, 'OpticsPortEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsPortEnum', 
                [], [], 
                '''                Showing port type
                ''',
                'port_type',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('rx-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Rx High threshold value in units of 0.1dBm
                ''',
                'rx_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('rx-high-warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Rx High Warning threshold value in units of 0
                .1dBm
                ''',
                'rx_high_warning_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('rx-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Rx Low threshold value in units of 0.1dBm
                ''',
                'rx_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('rx-low-warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Rx Low Warning threshold value in units of 0
                .1dBm
                ''',
                'rx_low_warning_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('rx-power', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Receive Power in 0.01 dB
                ''',
                'rx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('rx-power-th-configurable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                rx power th configurable
                ''',
                'rx_power_th_configurable',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('rx-voa-attenuation', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Rx Voa Attenuation in the unit of 0.01dBm
                ''',
                'rx_voa_attenuation',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('rx-voa-attenuation-config-val', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                rx voa attenuation config val
                ''',
                'rx_voa_attenuation_config_val',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('safety-control-mode-config-val', REFERENCE_ENUM_CLASS, 'OpticsAmplifierSafetyControlModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsAmplifierSafetyControlModeEnum', 
                [], [], 
                '''                safety control mode config val
                ''',
                'safety_control_mode_config_val',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('second-order-polarization-mode-dispersion', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Second Order Polarization Mode Dispersion 0
                .1ps^2
                ''',
                'second_order_polarization_mode_dispersion',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('temp-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Temp High threshold value in the units of 0.01 C
                ''',
                'temp_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('temp-high-warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Temp High warning threshold value in the units
                of 0.01 C
                ''',
                'temp_high_warning_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('temp-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Temp Low threshold value in the units 0.01 C
                ''',
                'temp_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('temp-low-warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Temp Low warning threshold value in the units 0
                .01 C
                ''',
                'temp_low_warning_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('temperature', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Temperature value
                ''',
                'temperature',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('total-rx-power', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Total Receive Power for Multi-Lane Optics in dBm
                ''',
                'total_rx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('total-tx-power', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Total Transmit Power for Multi-Lane Optics in
                dBm
                ''',
                'total_tx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('transceiver-info', REFERENCE_CLASS, 'TransceiverInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo', 
                [], [], 
                '''                Transceiver Vendor Details
                ''',
                'transceiver_info',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('transport-admin-state', REFERENCE_ENUM_CLASS, 'OpticsTasEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsTasEnum', 
                [], [], 
                '''                Transport Admin State
                ''',
                'transport_admin_state',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tx-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Tx High threshold value in units of 0.1dBm
                ''',
                'tx_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tx-high-warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Tx High Warning threshold value in units of 0
                .1dBm
                ''',
                'tx_high_warning_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tx-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Tx Low threshold value in units of 0.1dBm
                ''',
                'tx_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tx-low-warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Tx Low Warning threshold value in units of 0
                .1dBm
                ''',
                'tx_low_warning_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tx-power', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Transmit Power in 0.01 dB
                ''',
                'tx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tx-power-th-configurable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                tx power th configurable
                ''',
                'tx_power_th_configurable',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tx-voa-attenuation', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Tx Voa Attenuation in the unit of 0.01dBm
                ''',
                'tx_voa_attenuation',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('tx-voa-attenuation-config-val', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                tx voa attenuation config val
                ''',
                'tx_voa_attenuation_config_val',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('volt-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Volt High threshold value
                ''',
                'volt_high_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('volt-high-warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Volt High warning threshold value
                ''',
                'volt_high_warning_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('volt-low-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Volt Low threshold value
                ''',
                'volt_low_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('volt-low-warning-threshold', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Volt Low warning threshold value
                ''',
                'volt_low_warning_threshold',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('voltage', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Voltage value
                ''',
                'voltage',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'optics-info',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc',
            False, 
            [
            _MetaInfoClassMember('counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
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
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo',
            False, 
            [
            _MetaInfoClassMember('high-lbc', REFERENCE_CLASS, 'HighLbc' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc', 
                [], [], 
                '''                High laser bias current
                ''',
                'high_lbc',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-rx-power', REFERENCE_CLASS, 'HighRxPower' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower', 
                [], [], 
                '''                High Rx Power
                ''',
                'high_rx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('high-tx-power', REFERENCE_CLASS, 'HighTxPower' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower', 
                [], [], 
                '''                High Tx Power
                ''',
                'high_tx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-rx-power', REFERENCE_CLASS, 'LowRxPower' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower', 
                [], [], 
                '''                Low Rx Power
                ''',
                'low_rx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('low-tx-power', REFERENCE_CLASS, 'LowTxPower' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower', 
                [], [], 
                '''                Low Tx Power
                ''',
                'low_tx_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'lane-alarm-info',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Lane Index
                ''',
                'number',
                'Cisco-IOS-XR-controller-optics-oper', True),
            _MetaInfoClassMember('lane-alarm-info', REFERENCE_CLASS, 'LaneAlarmInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo', 
                [], [], 
                '''                Lane Alarm Information
                ''',
                'lane_alarm_info',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('lane-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The index number of the lane
                ''',
                'lane_index',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-bias-current-milli-amps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Laser Bias Current in units of 0.01mA
                ''',
                'laser_bias_current_milli_amps',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('laser-bias-current-percent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Laser Bias Current in units of 0.01 percentage
                ''',
                'laser_bias_current_percent',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('output-frequency', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Output frequency read from hw in the unit 0
                .01THz
                ''',
                'output_frequency',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('receive-power', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Transponder receive power in the unit of 0.01dBm
                ''',
                'receive_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('receive-signal-power', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Transponder receive signal power in the unit of
                0.01dBm
                ''',
                'receive_signal_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('transmit-power', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Transmit power in the unit of 0.01dBm
                ''',
                'transmit_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('transmit-signal-power', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Transmit Signal power in the unit of 0.01dBm
                ''',
                'transmit_signal_power',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'optics-lane',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsLanes' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsLanes',
            False, 
            [
            _MetaInfoClassMember('optics-lane', REFERENCE_LIST, 'OpticsLane' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane', 
                [], [], 
                '''                Lane Information
                ''',
                'optics_lane',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'optics-lanes',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray',
            False, 
            [
            _MetaInfoClassMember('network-srlg', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Network Srlg
                ''',
                'network_srlg',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('set-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Array to maintain set number
                ''',
                'set_number',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'network-srlg-array',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo',
            False, 
            [
            _MetaInfoClassMember('network-srlg-array', REFERENCE_LIST, 'NetworkSrlgArray' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray', 
                [], [], 
                '''                Network Srlg Array
                ''',
                'network_srlg_array',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'network-srlg-info',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo',
            False, 
            [
            _MetaInfoClassMember('controller-state', REFERENCE_ENUM_CLASS, 'OpticsControllerStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsControllerStateEnum', 
                [], [], 
                '''                Optics controller state: Up, Down or
                Administratively Down
                ''',
                'controller_state',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('network-srlg-info', REFERENCE_CLASS, 'NetworkSrlgInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo', 
                [], [], 
                '''                Network SRLG information
                ''',
                'network_srlg_info',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('transport-admin-state', REFERENCE_ENUM_CLASS, 'OpticsTasEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsTasEnum', 
                [], [], 
                '''                Transport Admin State
                ''',
                'transport_admin_state',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'optics-db-info',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts.OpticsPort' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts.OpticsPort',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Port name
                ''',
                'name',
                'Cisco-IOS-XR-controller-optics-oper', True),
            _MetaInfoClassMember('optics-db-info', REFERENCE_CLASS, 'OpticsDbInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo', 
                [], [], 
                '''                Optics operational data
                ''',
                'optics_db_info',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('optics-dwdm-carrrier-channel-map', REFERENCE_CLASS, 'OpticsDwdmCarrrierChannelMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap', 
                [], [], 
                '''                Optics operational data
                ''',
                'optics_dwdm_carrrier_channel_map',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('optics-info', REFERENCE_CLASS, 'OpticsInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsInfo', 
                [], [], 
                '''                Optics operational data
                ''',
                'optics_info',
                'Cisco-IOS-XR-controller-optics-oper', False),
            _MetaInfoClassMember('optics-lanes', REFERENCE_CLASS, 'OpticsLanes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort.OpticsLanes', 
                [], [], 
                '''                All Optics Port operational data
                ''',
                'optics_lanes',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'optics-port',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper.OpticsPorts' : {
        'meta_info' : _MetaInfoClass('OpticsOper.OpticsPorts',
            False, 
            [
            _MetaInfoClassMember('optics-port', REFERENCE_LIST, 'OpticsPort' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts.OpticsPort', 
                [], [], 
                '''                Optics operational data
                ''',
                'optics_port',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'optics-ports',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
    'OpticsOper' : {
        'meta_info' : _MetaInfoClass('OpticsOper',
            False, 
            [
            _MetaInfoClassMember('optics-ports', REFERENCE_CLASS, 'OpticsPorts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper', 'OpticsOper.OpticsPorts', 
                [], [], 
                '''                All Optics Port operational data
                ''',
                'optics_ports',
                'Cisco-IOS-XR-controller-optics-oper', False),
            ],
            'Cisco-IOS-XR-controller-optics-oper',
            'optics-oper',
            _yang_ns._namespaces['Cisco-IOS-XR-controller-optics-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_controller_optics_oper'
        ),
    },
}
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap.DwdmCarrierMapInfo']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo.NetworkSrlgArray']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRxPower']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRxPower']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTxPower']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTxPower']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighLbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx1Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx2Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx3Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighRx4Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx1Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx2Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx3Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowRx4Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Power']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx1Lbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx2Lbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx3Lbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.HighTx4Lbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx1Lbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx2Lbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx3Lbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.LowTx4Lbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLos']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLos']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLol']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxLol']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.TxFault']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Hidgd']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Oorcd']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Osnr']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Wvlool']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.Mea']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.ImpRemoval']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.RxLoc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegLow']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo.AmpGainDegHigh']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowTxPower']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.LowRxPower']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLosP']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.RxLoc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegLow']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AmpGainDegHigh']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoLaserShut']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoPowerRed']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlDisabled']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.AutoAmpliCtrlConfigMismatch']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo.SwitchToProtect']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighRxPower']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowRxPower']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighTxPower']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.LowTxPower']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo.HighLbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData.LaneAlarmInfo']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.NetworkSrlgInfo']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OpticsAlarmInfo']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.OtsAlarmInfo']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.TransceiverInfo']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamVal']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.ExtParamThresholdVal']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo.LaneData']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighRxPower']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowRxPower']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighTxPower']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.LowTxPower']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo.HighLbc']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane.LaneAlarmInfo']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes.OpticsLane']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo.NetworkSrlgArray']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo.NetworkSrlgInfo']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDwdmCarrrierChannelMap']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsInfo']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsLanes']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort.OpticsDbInfo']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts.OpticsPort']['meta_info']
_meta_table['OpticsOper.OpticsPorts.OpticsPort']['meta_info'].parent =_meta_table['OpticsOper.OpticsPorts']['meta_info']
_meta_table['OpticsOper.OpticsPorts']['meta_info'].parent =_meta_table['OpticsOper']['meta_info']
