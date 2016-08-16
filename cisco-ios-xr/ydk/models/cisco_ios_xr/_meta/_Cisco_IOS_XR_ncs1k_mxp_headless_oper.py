


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'HeadlessFuncData.OtnPortNames.OtnPortName.OtnStatistics' : {
        'meta_info' : _MetaInfoClass('HeadlessFuncData.OtnPortNames.OtnPortName.OtnStatistics',
            False, 
            [
            _MetaInfoClassMember('fec-ec', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                FecEc
                ''',
                'fec_ec',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('fec-uc', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                FecUc
                ''',
                'fec_uc',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('sm-bei', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                SmBei
                ''',
                'sm_bei',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('sm-bip', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                SmBip
                ''',
                'sm_bip',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-headless-oper',
            'otn-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-headless-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper'
        ),
    },
    'HeadlessFuncData.OtnPortNames.OtnPortName' : {
        'meta_info' : _MetaInfoClass('HeadlessFuncData.OtnPortNames.OtnPortName',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Port name
                ''',
                'name',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', True),
            _MetaInfoClassMember('headless-end-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Headless End Time
                ''',
                'headless_end_time',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('headless-start-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Headless Start Time
                ''',
                'headless_start_time',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('otn-statistics', REFERENCE_CLASS, 'OtnStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper', 'HeadlessFuncData.OtnPortNames.OtnPortName.OtnStatistics', 
                [], [], 
                '''                OTN statistics
                ''',
                'otn_statistics',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('started-stateful', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Started Stateful
                ''',
                'started_stateful',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-headless-oper',
            'otn-port-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-headless-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper'
        ),
    },
    'HeadlessFuncData.OtnPortNames' : {
        'meta_info' : _MetaInfoClass('HeadlessFuncData.OtnPortNames',
            False, 
            [
            _MetaInfoClassMember('otn-port-name', REFERENCE_LIST, 'OtnPortName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper', 'HeadlessFuncData.OtnPortNames.OtnPortName', 
                [], [], 
                '''                port Name
                ''',
                'otn_port_name',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-headless-oper',
            'otn-port-names',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-headless-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper'
        ),
    },
    'HeadlessFuncData.EthernetPortNames.EthernetPortName.EtherStatistics' : {
        'meta_info' : _MetaInfoClass('HeadlessFuncData.EthernetPortNames.EthernetPortName.EtherStatistics',
            False, 
            [
            _MetaInfoClassMember('rx-bytes-good', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RxBytesGood
                ''',
                'rx_bytes_good',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('rx-error-jabbers', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RxErrorJabbers
                ''',
                'rx_error_jabbers',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('rx-packets', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RxPackets
                ''',
                'rx_packets',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('rx-pkts1024-to1518-bytes', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RxPkts1024To1518Bytes
                ''',
                'rx_pkts1024_to1518_bytes',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('rx-pkts128to255-bytes', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RxPkts128to255Bytes
                ''',
                'rx_pkts128to255_bytes',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('rx-pkts256-to511-bytes', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RxPkts256To511Bytes
                ''',
                'rx_pkts256_to511_bytes',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('rx-pkts512-to1023-bytes', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RxPkts512To1023Bytes
                ''',
                'rx_pkts512_to1023_bytes',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('rx-pkts64-bytes', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RxPkts64Bytes
                ''',
                'rx_pkts64_bytes',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('rx-pkts65-to127-bytes', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RxPkts65To127Bytes
                ''',
                'rx_pkts65_to127_bytes',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('rx-pkts-bad-fcs', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RxPktsBadFcs
                ''',
                'rx_pkts_bad_fcs',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('rx-pkts-broadcast', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RxPktsBroadcast
                ''',
                'rx_pkts_broadcast',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('rx-pkts-good', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RxPktsGood
                ''',
                'rx_pkts_good',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('rx-pkts-multicast', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RxPktsMulticast
                ''',
                'rx_pkts_multicast',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('rx-pkts-over-sized', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RxPktsOverSized
                ''',
                'rx_pkts_over_sized',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('rx-pkts-under-sized', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RxPktsUnderSized
                ''',
                'rx_pkts_under_sized',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('rx-pkts-unicast', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RxPktsUnicast
                ''',
                'rx_pkts_unicast',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('rx-recv-fragments', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RxRecvFragments
                ''',
                'rx_recv_fragments',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('rx-total-bytes', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RxTotalBytes
                ''',
                'rx_total_bytes',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('tx-bytes-good', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                TxBytesGood
                ''',
                'tx_bytes_good',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('tx-pkts-good', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                TxPktsGood
                ''',
                'tx_pkts_good',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('tx-total-bytes', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                TxTotalBytes
                ''',
                'tx_total_bytes',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-headless-oper',
            'ether-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-headless-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper'
        ),
    },
    'HeadlessFuncData.EthernetPortNames.EthernetPortName' : {
        'meta_info' : _MetaInfoClass('HeadlessFuncData.EthernetPortNames.EthernetPortName',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Port name
                ''',
                'name',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', True),
            _MetaInfoClassMember('ether-statistics', REFERENCE_CLASS, 'EtherStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper', 'HeadlessFuncData.EthernetPortNames.EthernetPortName.EtherStatistics', 
                [], [], 
                '''                Ether Statistics
                ''',
                'ether_statistics',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('headless-end-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Headless End Time
                ''',
                'headless_end_time',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('headless-start-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Headless Start Time
                ''',
                'headless_start_time',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('started-stateful', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Started Stateful
                ''',
                'started_stateful',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-headless-oper',
            'ethernet-port-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-headless-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper'
        ),
    },
    'HeadlessFuncData.EthernetPortNames' : {
        'meta_info' : _MetaInfoClass('HeadlessFuncData.EthernetPortNames',
            False, 
            [
            _MetaInfoClassMember('ethernet-port-name', REFERENCE_LIST, 'EthernetPortName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper', 'HeadlessFuncData.EthernetPortNames.EthernetPortName', 
                [], [], 
                '''                Port Name
                ''',
                'ethernet_port_name',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-headless-oper',
            'ethernet-port-names',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-headless-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper'
        ),
    },
    'HeadlessFuncData' : {
        'meta_info' : _MetaInfoClass('HeadlessFuncData',
            False, 
            [
            _MetaInfoClassMember('ethernet-port-names', REFERENCE_CLASS, 'EthernetPortNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper', 'HeadlessFuncData.EthernetPortNames', 
                [], [], 
                '''                Ethernet Statistics collected during last
                headless operation
                ''',
                'ethernet_port_names',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            _MetaInfoClassMember('otn-port-names', REFERENCE_CLASS, 'OtnPortNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper', 'HeadlessFuncData.OtnPortNames', 
                [], [], 
                '''                OTN Statistics collected during last headless
                operation
                ''',
                'otn_port_names',
                'Cisco-IOS-XR-ncs1k-mxp-headless-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-mxp-headless-oper',
            'headless-func-data',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-mxp-headless-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_mxp_headless_oper'
        ),
    },
}
_meta_table['HeadlessFuncData.OtnPortNames.OtnPortName.OtnStatistics']['meta_info'].parent =_meta_table['HeadlessFuncData.OtnPortNames.OtnPortName']['meta_info']
_meta_table['HeadlessFuncData.OtnPortNames.OtnPortName']['meta_info'].parent =_meta_table['HeadlessFuncData.OtnPortNames']['meta_info']
_meta_table['HeadlessFuncData.EthernetPortNames.EthernetPortName.EtherStatistics']['meta_info'].parent =_meta_table['HeadlessFuncData.EthernetPortNames.EthernetPortName']['meta_info']
_meta_table['HeadlessFuncData.EthernetPortNames.EthernetPortName']['meta_info'].parent =_meta_table['HeadlessFuncData.EthernetPortNames']['meta_info']
_meta_table['HeadlessFuncData.OtnPortNames']['meta_info'].parent =_meta_table['HeadlessFuncData']['meta_info']
_meta_table['HeadlessFuncData.EthernetPortNames']['meta_info'].parent =_meta_table['HeadlessFuncData']['meta_info']
