


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'WanphyAlarmRepStatusEnum' : _MetaInfoEnum('WanphyAlarmRepStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-wanphy-ui-oper', _yang_ns._namespaces['Cisco-IOS-XR-wanphy-ui-oper']),
    'WanphyModeInfoEnum' : _MetaInfoEnum('WanphyModeInfoEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper',
        {
            'lan':'lan',
            'wan':'wan',
        }, 'Cisco-IOS-XR-wanphy-ui-oper', _yang_ns._namespaces['Cisco-IOS-XR-wanphy-ui-oper']),
    'Wanphy.Controllers.Controller.Info' : {
        'meta_info' : _MetaInfoClass('Wanphy.Controllers.Controller.Info',
            False, 
            [
            _MetaInfoClassMember('admin-mode', REFERENCE_ENUM_CLASS, 'WanphyModeInfoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper', 'WanphyModeInfoEnum', 
                [], [], 
                '''                Configuration Mode
                ''',
                'admin_mode',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('line-ais', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Line AIS
                ''',
                'line_ais',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('line-bip', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Line BIP(B2) 
                ''',
                'line_bip',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('line-febe', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Line FEBE
                ''',
                'line_febe',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('line-rdi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Line RDI
                ''',
                'line_rdi',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('operational-mode', REFERENCE_ENUM_CLASS, 'WanphyModeInfoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper', 'WanphyModeInfoEnum', 
                [], [], 
                '''                Operational Mode
                ''',
                'operational_mode',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('path-ais', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path AIS
                ''',
                'path_ais',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('path-bip', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Path BIP(B3)
                ''',
                'path_bip',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('path-febe', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Path FEBE
                ''',
                'path_febe',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('path-lop', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path LOP
                ''',
                'path_lop',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('path-newptr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path NEWPTR
                ''',
                'path_newptr',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('path-nse', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path NSE
                ''',
                'path_nse',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('path-pse', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path PSE
                ''',
                'path_pse',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('path-rdi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path RDI
                ''',
                'path_rdi',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('port-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Port State
                ''',
                'port_state',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('register-j1-rx0', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Register J1-Rx0
                ''',
                'register_j1_rx0',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('register-j1-rx1', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Register J1-Rx1
                ''',
                'register_j1_rx1',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('register-j1-rx2', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Register J1-Rx2
                ''',
                'register_j1_rx2',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('register-j1-rx3', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Register J1-Rx3
                ''',
                'register_j1_rx3',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('register-j1-rx4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Register J1-Rx4
                ''',
                'register_j1_rx4',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('register-j1-rx5', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Register J1-Rx5
                ''',
                'register_j1_rx5',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('register-j1-rx6', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Register J1-Rx6
                ''',
                'register_j1_rx6',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('register-j1-rx7', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Register J1-Rx7
                ''',
                'register_j1_rx7',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('register-l-bip', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Register L_BIP
                ''',
                'register_l_bip',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('register-l-fe-bip', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Register L_FE_BIP
                ''',
                'register_l_fe_bip',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('register-p-bec', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Register P_BEC
                ''',
                'register_p_bec',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('register-p-febe', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Register P_FEBE
                ''',
                'register_p_febe',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('register-s-bip', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Register S_BIP
                ''',
                'register_s_bip',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('remote-ip', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote IP Address
                ''',
                'remote_ip',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('sd-ber-report', REFERENCE_ENUM_CLASS, 'WanphyAlarmRepStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper', 'WanphyAlarmRepStatusEnum', 
                [], [], 
                '''                SD_BER Report
                ''',
                'sd_ber_report',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('sd-ber-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BER thresholds: SD. Value 'd' in 10e-%d
                ''',
                'sd_ber_threshold',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('section-bip', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Section BIP(B1)
                ''',
                'section_bip',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('section-lof', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Section LOF
                ''',
                'section_lof',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('section-los', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Section LOS
                ''',
                'section_los',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('sf-ber-report', REFERENCE_ENUM_CLASS, 'WanphyAlarmRepStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper', 'WanphyAlarmRepStatusEnum', 
                [], [], 
                '''                SF_BER Report
                ''',
                'sf_ber_report',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('sf-ber-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BER thresholds: SF. Value 'd' in 10e-%d
                ''',
                'sf_ber_threshold',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('wanphy-poll-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                wanphy poll timer
                ''',
                'wanphy_poll_timer',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('wis-alarms-feaisp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                WIS Alarms FEAISP
                ''',
                'wis_alarms_feaisp',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('wis-alarms-felcdp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                WIS Alarms FELCDP
                ''',
                'wis_alarms_felcdp',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('wis-alarms-lfebip', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                WIS Alarms LFEBIP
                ''',
                'wis_alarms_lfebip',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('wis-alarms-pbec', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                WIS Alarms PBEC
                ''',
                'wis_alarms_pbec',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('wis-alarms-plcd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                WIS Alarms PLCD
                ''',
                'wis_alarms_plcd',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('wis-alarms-plmp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                WIS Alarms PLMP
                ''',
                'wis_alarms_plmp',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('wis-alarms-ser', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                WIS Alarms SER
                ''',
                'wis_alarms_ser',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            _MetaInfoClassMember('wis-alarms-wlos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                WIS Alarms WLOS
                ''',
                'wis_alarms_wlos',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            ],
            'Cisco-IOS-XR-wanphy-ui-oper',
            'info',
            _yang_ns._namespaces['Cisco-IOS-XR-wanphy-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper'
        ),
    },
    'Wanphy.Controllers.Controller' : {
        'meta_info' : _MetaInfoClass('Wanphy.Controllers.Controller',
            False, 
            [
            _MetaInfoClassMember('controller-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Controller name
                ''',
                'controller_name',
                'Cisco-IOS-XR-wanphy-ui-oper', True),
            _MetaInfoClassMember('info', REFERENCE_CLASS, 'Info' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper', 'Wanphy.Controllers.Controller.Info', 
                [], [], 
                '''                WANPHY controller operational data
                ''',
                'info',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            ],
            'Cisco-IOS-XR-wanphy-ui-oper',
            'controller',
            _yang_ns._namespaces['Cisco-IOS-XR-wanphy-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper'
        ),
    },
    'Wanphy.Controllers' : {
        'meta_info' : _MetaInfoClass('Wanphy.Controllers',
            False, 
            [
            _MetaInfoClassMember('controller', REFERENCE_LIST, 'Controller' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper', 'Wanphy.Controllers.Controller', 
                [], [], 
                '''                WANPHY controller operational data
                ''',
                'controller',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            ],
            'Cisco-IOS-XR-wanphy-ui-oper',
            'controllers',
            _yang_ns._namespaces['Cisco-IOS-XR-wanphy-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper'
        ),
    },
    'Wanphy' : {
        'meta_info' : _MetaInfoClass('Wanphy',
            False, 
            [
            _MetaInfoClassMember('controllers', REFERENCE_CLASS, 'Controllers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper', 'Wanphy.Controllers', 
                [], [], 
                '''                All WANPHY controller operational data
                ''',
                'controllers',
                'Cisco-IOS-XR-wanphy-ui-oper', False),
            ],
            'Cisco-IOS-XR-wanphy-ui-oper',
            'wanphy',
            _yang_ns._namespaces['Cisco-IOS-XR-wanphy-ui-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_wanphy_ui_oper'
        ),
    },
}
_meta_table['Wanphy.Controllers.Controller.Info']['meta_info'].parent =_meta_table['Wanphy.Controllers.Controller']['meta_info']
_meta_table['Wanphy.Controllers.Controller']['meta_info'].parent =_meta_table['Wanphy.Controllers']['meta_info']
_meta_table['Wanphy.Controllers']['meta_info'].parent =_meta_table['Wanphy']['meta_info']
