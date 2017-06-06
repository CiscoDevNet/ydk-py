


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Config' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Config',
            False, 
            [
            _MetaInfoClassMember('duplex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                duplex
                ''',
                'duplex',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('loopback', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                loopback
                ''',
                'loopback',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('my-pause', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                myPause
                ''',
                'my_pause',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('pause', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                pauseEn
                ''',
                'pause',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('speed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                speed
                ''',
                'speed',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'config',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Phy' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Phy',
            False, 
            [
            _MetaInfoClassMember('reg', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                reg
                ''',
                'reg',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False, max_elements=32),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'phy',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Serdes' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Serdes',
            False, 
            [
            _MetaInfoClassMember('reg', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                reg
                ''',
                'reg',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False, max_elements=32),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'serdes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Mac' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Mac',
            False, 
            [
            _MetaInfoClassMember('reg', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                reg
                ''',
                'reg',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False, max_elements=32),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'mac',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Config', 
                [], [], 
                '''                Configuration Data
                ''',
                'config',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('mac', REFERENCE_CLASS, 'Mac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Mac', 
                [], [], 
                '''                MAC Registers
                ''',
                'mac',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('mac-valid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MAC data valid
                ''',
                'mac_valid',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('phy', REFERENCE_CLASS, 'Phy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Phy', 
                [], [], 
                '''                PHY Registers
                ''',
                'phy',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('phy-valid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PHY data valid
                ''',
                'phy_valid',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('port-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Port Number
                ''',
                'port_num',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('serdes', REFERENCE_CLASS, 'Serdes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Serdes', 
                [], [], 
                '''                SERDES Registers
                ''',
                'serdes',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('serdes-valid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SERDES data valid
                ''',
                'serdes_valid',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'port-status',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                port number
                ''',
                'number',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', True),
            _MetaInfoClassMember('port-status', REFERENCE_CLASS, 'PortStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus', 
                [], [], 
                '''                mlan port status info
                ''',
                'port_status',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'port-status-number',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.PortStatusNumbers' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.PortStatusNumbers',
            False, 
            [
            _MetaInfoClassMember('port-status-number', REFERENCE_LIST, 'PortStatusNumber' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber', 
                [], [], 
                '''                Number
                ''',
                'port_status_number',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'port-status-numbers',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg1' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg1',
            False, 
            [
            _MetaInfoClassMember('reg', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                reg
                ''',
                'reg',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False, max_elements=32),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'sw-reg-1',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg2' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg2',
            False, 
            [
            _MetaInfoClassMember('reg', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                reg
                ''',
                'reg',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False, max_elements=32),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'sw-reg-2',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwStatus' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwStatus',
            False, 
            [
            _MetaInfoClassMember('cpu-mac', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                cpu mac
                ''',
                'cpu_mac',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('cpu-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                cpu port
                ''',
                'cpu_port',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('initialized', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                initialized
                ''',
                'initialized',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('mac', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                mac
                ''',
                'mac',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                mtu
                ''',
                'mtu',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('ppu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ppu
                ''',
                'ppu',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('restarted', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                restarted
                ''',
                'restarted',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'sw-status',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus',
            False, 
            [
            _MetaInfoClassMember('rate-limit', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                CPU Interface Rate Limit
                ''',
                'rate_limit',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('sw-reg-1', REFERENCE_CLASS, 'SwReg1' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg1', 
                [], [], 
                '''                Switch Global Registers
                ''',
                'sw_reg_1',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('sw-reg-2', REFERENCE_CLASS, 'SwReg2' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg2', 
                [], [], 
                '''                Switch Global Registers
                ''',
                'sw_reg_2',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('sw-status', REFERENCE_CLASS, 'SwStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwStatus', 
                [], [], 
                '''                Switch Status Data
                ''',
                'sw_status',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'switch-status',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.SwitchStatusTable' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.SwitchStatusTable',
            False, 
            [
            _MetaInfoClassMember('switch-status', REFERENCE_CLASS, 'SwitchStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus', 
                [], [], 
                '''                mlan switch status info
                ''',
                'switch_status',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'switch-status-table',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters.MlanStats' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters.MlanStats',
            False, 
            [
            _MetaInfoClassMember('collisions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                collisions
                ''',
                'collisions',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('deferred', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                deferred
                ''',
                'deferred',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('excessive', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                excessive
                ''',
                'excessive',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('in-bad-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                inBadOctets
                ''',
                'in_bad_octets',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('in-bcast-pkt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                inBcastPkt
                ''',
                'in_bcast_pkt',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('in-discards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                inDiscards
                ''',
                'in_discards',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('in-fcs-err', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                inFcsErr
                ''',
                'in_fcs_err',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('in-filtered', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                inFiltered
                ''',
                'in_filtered',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('in-fragments', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                inFragments
                ''',
                'in_fragments',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('in-good-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                inGoodOctets
                ''',
                'in_good_octets',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('in-good-octets-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                inGoodOctets hi
                ''',
                'in_good_octets_hi',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('in-jabber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                inJabber
                ''',
                'in_jabber',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('in-mcast-pkt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                inMcastPkt
                ''',
                'in_mcast_pkt',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('in-oversize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                inOversize
                ''',
                'in_oversize',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('in-pause-pkt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                inPausePkt
                ''',
                'in_pause_pkt',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('in-rx-err', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                inRxErr
                ''',
                'in_rx_err',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('in-undersize-pkt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                inUndersizePkt
                ''',
                'in_undersize_pkt',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('in-unicast-pkt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                inUnicastPkt
                ''',
                'in_unicast_pkt',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('late', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                late
                ''',
                'late',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('multiple', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                multiple
                ''',
                'multiple',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('out-bcast-pkt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                outBcastPkt
                ''',
                'out_bcast_pkt',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('out-fcs-err', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                outFcsErr
                ''',
                'out_fcs_err',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('out-filtered', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                outFiltered
                ''',
                'out_filtered',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('out-mcast-pkt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                outMcastPkt
                ''',
                'out_mcast_pkt',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('out-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                outOctets
                ''',
                'out_octets',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('out-octets-hi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                outOctets hi
                ''',
                'out_octets_hi',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('out-pause-pkt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                outPausePkt
                ''',
                'out_pause_pkt',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('out-unicast-pkt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                outUnicastPkt
                ''',
                'out_unicast_pkt',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('rx-tx-1024-max-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                rx tx 1024 Max Octets
                ''',
                'rx_tx_1024_max_octets',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('rx-tx-128-255-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                rx tx 128 255 Octets
                ''',
                'rx_tx_128_255_octets',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('rx-tx-256-511-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                rx tx 256 511 Octets
                ''',
                'rx_tx_256_511_octets',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('rx-tx-512-1023-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                rx tx 512 1023 Octets
                ''',
                'rx_tx_512_1023_octets',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('rx-tx-64-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                rx tx 64 Octets
                ''',
                'rx_tx_64_octets',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('rx-tx-65-127-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                rx tx 65 127 Octets
                ''',
                'rx_tx_65_127_octets',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('single', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                single
                ''',
                'single',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'mlan-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters',
            False, 
            [
            _MetaInfoClassMember('mlan-stats', REFERENCE_CLASS, 'MlanStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters.MlanStats', 
                [], [], 
                '''                Switch Port Statistics
                ''',
                'mlan_stats',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('port-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Port Number
                ''',
                'port_num',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'port-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                port number
                ''',
                'number',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', True),
            _MetaInfoClassMember('port-counters', REFERENCE_CLASS, 'PortCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters', 
                [], [], 
                '''                mlan port counters info
                ''',
                'port_counters',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'port-counters-number',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.PortCountersNumbers' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.PortCountersNumbers',
            False, 
            [
            _MetaInfoClassMember('port-counters-number', REFERENCE_LIST, 'PortCountersNumber' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber', 
                [], [], 
                '''                Number
                ''',
                'port_counters_number',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'port-counters-numbers',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters.Atu' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters.Atu',
            False, 
            [
            _MetaInfoClassMember('db-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                dbNum
                ''',
                'db_num',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('dpv', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                dpv
                ''',
                'dpv',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('es', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                es
                ''',
                'es',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('macaddr', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                macaddr
                ''',
                'macaddr',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False, max_elements=3),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                priority
                ''',
                'priority',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('trunk', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                trunk
                ''',
                'trunk',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'atu',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters',
            False, 
            [
            _MetaInfoClassMember('atu', REFERENCE_CLASS, 'Atu' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters.Atu', 
                [], [], 
                '''                Switch ATU Data
                ''',
                'atu',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('entry-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index of ATU Entry
                ''',
                'entry_num',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'switch-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber',
            False, 
            [
            _MetaInfoClassMember('entry', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                entry number
                ''',
                'entry',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', True),
            _MetaInfoClassMember('switch-counters', REFERENCE_CLASS, 'SwitchCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters', 
                [], [], 
                '''                mlan switch counters info
                ''',
                'switch_counters',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'atu-entry-number',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node.AtuEntryNumbers' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node.AtuEntryNumbers',
            False, 
            [
            _MetaInfoClassMember('atu-entry-number', REFERENCE_LIST, 'AtuEntryNumber' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber', 
                [], [], 
                '''                Entry number
                ''',
                'atu_entry_number',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'atu-entry-numbers',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                node number
                ''',
                'node',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', True),
            _MetaInfoClassMember('atu-entry-numbers', REFERENCE_CLASS, 'AtuEntryNumbers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.AtuEntryNumbers', 
                [], [], 
                '''                Table of switch ATU
                ''',
                'atu_entry_numbers',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('port-counters-numbers', REFERENCE_CLASS, 'PortCountersNumbers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.PortCountersNumbers', 
                [], [], 
                '''                Table of port counters
                ''',
                'port_counters_numbers',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('port-status-numbers', REFERENCE_CLASS, 'PortStatusNumbers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.PortStatusNumbers', 
                [], [], 
                '''                Table of port status
                ''',
                'port_status_numbers',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            _MetaInfoClassMember('switch-status-table', REFERENCE_CLASS, 'SwitchStatusTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node.SwitchStatusTable', 
                [], [], 
                '''                Table of switch status
                ''',
                'switch_status_table',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan.Nodes' : {
        'meta_info' : _MetaInfoClass('Mlan.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes.Node', 
                [], [], 
                '''                Number
                ''',
                'node',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
    'Mlan' : {
        'meta_info' : _MetaInfoClass('Mlan',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper', 'Mlan.Nodes', 
                [], [], 
                '''                Table of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-asr9k-lc-ethctrl-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-ethctrl-oper',
            'mlan',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-ethctrl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_ethctrl_oper'
        ),
    },
}
_meta_table['Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Config']['meta_info'].parent =_meta_table['Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus']['meta_info']
_meta_table['Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Phy']['meta_info'].parent =_meta_table['Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus']['meta_info']
_meta_table['Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Serdes']['meta_info'].parent =_meta_table['Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus']['meta_info']
_meta_table['Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus.Mac']['meta_info'].parent =_meta_table['Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus']['meta_info']
_meta_table['Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber.PortStatus']['meta_info'].parent =_meta_table['Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber']['meta_info']
_meta_table['Mlan.Nodes.Node.PortStatusNumbers.PortStatusNumber']['meta_info'].parent =_meta_table['Mlan.Nodes.Node.PortStatusNumbers']['meta_info']
_meta_table['Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg1']['meta_info'].parent =_meta_table['Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus']['meta_info']
_meta_table['Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwReg2']['meta_info'].parent =_meta_table['Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus']['meta_info']
_meta_table['Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus.SwStatus']['meta_info'].parent =_meta_table['Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus']['meta_info']
_meta_table['Mlan.Nodes.Node.SwitchStatusTable.SwitchStatus']['meta_info'].parent =_meta_table['Mlan.Nodes.Node.SwitchStatusTable']['meta_info']
_meta_table['Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters.MlanStats']['meta_info'].parent =_meta_table['Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters']['meta_info']
_meta_table['Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber.PortCounters']['meta_info'].parent =_meta_table['Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber']['meta_info']
_meta_table['Mlan.Nodes.Node.PortCountersNumbers.PortCountersNumber']['meta_info'].parent =_meta_table['Mlan.Nodes.Node.PortCountersNumbers']['meta_info']
_meta_table['Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters.Atu']['meta_info'].parent =_meta_table['Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters']['meta_info']
_meta_table['Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber.SwitchCounters']['meta_info'].parent =_meta_table['Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber']['meta_info']
_meta_table['Mlan.Nodes.Node.AtuEntryNumbers.AtuEntryNumber']['meta_info'].parent =_meta_table['Mlan.Nodes.Node.AtuEntryNumbers']['meta_info']
_meta_table['Mlan.Nodes.Node.PortStatusNumbers']['meta_info'].parent =_meta_table['Mlan.Nodes.Node']['meta_info']
_meta_table['Mlan.Nodes.Node.SwitchStatusTable']['meta_info'].parent =_meta_table['Mlan.Nodes.Node']['meta_info']
_meta_table['Mlan.Nodes.Node.PortCountersNumbers']['meta_info'].parent =_meta_table['Mlan.Nodes.Node']['meta_info']
_meta_table['Mlan.Nodes.Node.AtuEntryNumbers']['meta_info'].parent =_meta_table['Mlan.Nodes.Node']['meta_info']
_meta_table['Mlan.Nodes.Node']['meta_info'].parent =_meta_table['Mlan.Nodes']['meta_info']
_meta_table['Mlan.Nodes']['meta_info'].parent =_meta_table['Mlan']['meta_info']
