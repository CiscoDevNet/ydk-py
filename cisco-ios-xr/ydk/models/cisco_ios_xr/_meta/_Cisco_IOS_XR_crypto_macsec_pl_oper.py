


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.TxSaStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.TxSaStats',
            False, 
            [
            _MetaInfoClassMember('out-octets-encrypted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Octets Encrypted
                ''',
                'out_octets_encrypted',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-octets-protected', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Octets Protected
                ''',
                'out_octets_protected',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkts-encrypted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Pkts Encrypted
                ''',
                'out_pkts_encrypted',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkts-protected', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Pkts Protected
                ''',
                'out_pkts_protected',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'tx-sa-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.RxSaStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.RxSaStats',
            False, 
            [
            _MetaInfoClassMember('in-octets-decrypted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Octets Decrypted
                ''',
                'in_octets_decrypted',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-octets-validated', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Octets Validated
                ''',
                'in_octets_validated',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-delayed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Delayed
                ''',
                'in_pkts_delayed',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Invalid
                ''',
                'in_pkts_invalid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-late', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Late
                ''',
                'in_pkts_late',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-not-using-sa', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Not Using SA
                ''',
                'in_pkts_not_using_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-not-valid', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Not Valid
                ''',
                'in_pkts_not_valid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts OK
                ''',
                'in_pkts_ok',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-unchecked', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Unchecked
                ''',
                'in_pkts_unchecked',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-unused-sa', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Unused SA
                ''',
                'in_pkts_unused_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'rx-sa-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.TxInterfaceMacsecStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.TxInterfaceMacsecStats',
            False, 
            [
            _MetaInfoClassMember('out-pkt-too-long', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Pkts Too Long
                ''',
                'out_pkt_too_long',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkt-uncontrolled', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Pkts Uncontrolled
                ''',
                'out_pkt_uncontrolled',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkt-untagged', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Pkts Untagged
                ''',
                'out_pkt_untagged',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'tx-interface-macsec-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.RxInterfaceMacsecStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.RxInterfaceMacsecStats',
            False, 
            [
            _MetaInfoClassMember('in-pkt-bad-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Bad tag
                ''',
                'in_pkt_bad_tag',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-no-sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts No Sci
                ''',
                'in_pkt_no_sci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-notag', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Notag
                ''',
                'in_pkt_notag',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-overrun', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Over Run
                ''',
                'in_pkt_overrun',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-tagged', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Tagged
                ''',
                'in_pkt_tagged',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-uncontrolled', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Uncontrolled
                ''',
                'in_pkt_uncontrolled',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-unknown-sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Unknown Sci
                ''',
                'in_pkt_unknown_sci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-untagged', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Untagged
                ''',
                'in_pkt_untagged',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'rx-interface-macsec-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats',
            False, 
            [
            _MetaInfoClassMember('rx-interface-macsec-stats', REFERENCE_CLASS, 'RxInterfaceMacsecStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.RxInterfaceMacsecStats', 
                [], [], 
                '''                Rx interface Macsec Stats
                ''',
                'rx_interface_macsec_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('rx-sa-stats', REFERENCE_CLASS, 'RxSaStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.RxSaStats', 
                [], [], 
                '''                Rx SA Stats
                ''',
                'rx_sa_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tx-interface-macsec-stats', REFERENCE_CLASS, 'TxInterfaceMacsecStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.TxInterfaceMacsecStats', 
                [], [], 
                '''                Tx interface Macsec Stats
                ''',
                'tx_interface_macsec_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tx-sa-stats', REFERENCE_CLASS, 'TxSaStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.TxSaStats', 
                [], [], 
                '''                Tx SA Stats
                ''',
                'tx_sa_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'msfpga-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwStatistics',
            False, 
            [
            _MetaInfoClassMember('hw-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Hardware Type
                ''',
                'hw_type',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('msfpga-stats', REFERENCE_CLASS, 'MsfpgaStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats', 
                [], [], 
                '''                MSFPGA Stats
                ''',
                'msfpga_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'hw-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa.TxSa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa.TxSa',
            False, 
            [
            _MetaInfoClassMember('action', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Action
                ''',
                'action',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('an', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Association Number
                ''',
                'an',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('c-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Conf offset
                ''',
                'c_offset',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('crypto-algo', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Crypto Algorithm
                ''',
                'crypto_algo',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-use', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                In Use
                ''',
                'in_use',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-egress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                rx_tx direction
                ''',
                'is_egress',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('key-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Key Length
                ''',
                'key_len',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('next-pn', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Next Packet Number
                ''',
                'next_pn',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('q-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Q bit
                ''',
                'q_bit',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('qq-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                QQ bit
                ''',
                'qq_bit',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                SA Index
                ''',
                'sa_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                SCI
                ''',
                'sci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SA Validity
                ''',
                'valid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('xpn', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                XPN EN
                ''',
                'xpn',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'tx-sa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa.RxSa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa.RxSa',
            False, 
            [
            _MetaInfoClassMember('action', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Action
                ''',
                'action',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('an', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Association Number
                ''',
                'an',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('c-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Conf offset
                ''',
                'c_offset',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('crypto-algo', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Crypto Algorithm
                ''',
                'crypto_algo',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-use', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                In Use
                ''',
                'in_use',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-egress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                rx_tx direction
                ''',
                'is_egress',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('key-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Key Length
                ''',
                'key_len',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('next-pn', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Next Packet Number
                ''',
                'next_pn',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('q-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Q bit
                ''',
                'q_bit',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('qq-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                QQ bit
                ''',
                'qq_bit',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                SA Index
                ''',
                'sa_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                SCI
                ''',
                'sci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SA Validity
                ''',
                'valid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('xpn', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                XPN EN
                ''',
                'xpn',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'rx-sa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa',
            False, 
            [
            _MetaInfoClassMember('rx-sa', REFERENCE_CLASS, 'RxSa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa.RxSa', 
                [], [], 
                '''                Rx SA Details
                ''',
                'rx_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tx-sa', REFERENCE_CLASS, 'TxSa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa.TxSa', 
                [], [], 
                '''                Tx SA Details
                ''',
                'tx_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'msfpga-sa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa',
            False, 
            [
            _MetaInfoClassMember('sa-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                SA ID
                ''',
                'sa_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', True),
            _MetaInfoClassMember('hw-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Hardware Type
                ''',
                'hw_type',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('msfpga-sa', REFERENCE_CLASS, 'MsfpgaSa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa', 
                [], [], 
                '''                MSFPGA SA Information
                ''',
                'msfpga_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'sw-sa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwSas' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwSas',
            False, 
            [
            _MetaInfoClassMember('sw-sa', REFERENCE_LIST, 'SwSa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa', 
                [], [], 
                '''                Software Security Association
                ''',
                'sw_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'sw-sas',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa.TxSa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa.TxSa',
            False, 
            [
            _MetaInfoClassMember('action', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Action
                ''',
                'action',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('an', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Association Number
                ''',
                'an',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('c-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Conf offset
                ''',
                'c_offset',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('crypto-algo', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Crypto Algorithm
                ''',
                'crypto_algo',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-use', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                In Use
                ''',
                'in_use',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-egress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                rx_tx direction
                ''',
                'is_egress',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('key-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Key Length
                ''',
                'key_len',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('next-pn', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Next Packet Number
                ''',
                'next_pn',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('q-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Q bit
                ''',
                'q_bit',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('qq-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                QQ bit
                ''',
                'qq_bit',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                SA Index
                ''',
                'sa_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                SCI
                ''',
                'sci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SA Validity
                ''',
                'valid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('xpn', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                XPN EN
                ''',
                'xpn',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'tx-sa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa.RxSa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa.RxSa',
            False, 
            [
            _MetaInfoClassMember('action', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Action
                ''',
                'action',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('an', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Association Number
                ''',
                'an',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('c-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Conf offset
                ''',
                'c_offset',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('crypto-algo', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Crypto Algorithm
                ''',
                'crypto_algo',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-use', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                In Use
                ''',
                'in_use',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-egress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                rx_tx direction
                ''',
                'is_egress',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('key-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Key Length
                ''',
                'key_len',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('next-pn', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Next Packet Number
                ''',
                'next_pn',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('q-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Q bit
                ''',
                'q_bit',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('qq-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                QQ bit
                ''',
                'qq_bit',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                SA Index
                ''',
                'sa_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                SCI
                ''',
                'sci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SA Validity
                ''',
                'valid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('xpn', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                XPN EN
                ''',
                'xpn',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'rx-sa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa',
            False, 
            [
            _MetaInfoClassMember('rx-sa', REFERENCE_CLASS, 'RxSa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa.RxSa', 
                [], [], 
                '''                Rx SA Details
                ''',
                'rx_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tx-sa', REFERENCE_CLASS, 'TxSa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa.TxSa', 
                [], [], 
                '''                Tx SA Details
                ''',
                'tx_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'msfpga-sa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa',
            False, 
            [
            _MetaInfoClassMember('sa-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                SA ID
                ''',
                'sa_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', True),
            _MetaInfoClassMember('hw-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Hardware Type
                ''',
                'hw_type',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('msfpga-sa', REFERENCE_CLASS, 'MsfpgaSa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa', 
                [], [], 
                '''                MSFPGA SA Information
                ''',
                'msfpga_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'hw-sa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwSas' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwSas',
            False, 
            [
            _MetaInfoClassMember('hw-sa', REFERENCE_LIST, 'HwSa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa', 
                [], [], 
                '''                Hardware Security Association
                ''',
                'hw_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'hw-sas',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow.TxFlow' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow.TxFlow',
            False, 
            [
            _MetaInfoClassMember('action', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Action
                ''',
                'action',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('ctrl-check', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ctrl Pkt ChkEn
                ''',
                'ctrl_check',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('dmac-inuse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If MAC DA in Use
                ''',
                'dmac_inuse',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('ethertype', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Ether Type
                ''',
                'ethertype',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('flow-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Flow Index
                ''',
                'flow_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-use', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                In Use
                ''',
                'in_use',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Inner VLAN ID
                ''',
                'inner_vlan',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-tpid', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Inner Vlan TPID
                ''',
                'inner_vlan_tpid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Inner Vlan UserPri
                ''',
                'inner_vlan_up',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-ctrl-pkt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Control Pkt
                ''',
                'is_ctrl_pkt',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-egress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                rx_tx direction
                ''',
                'is_egress',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('macda', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                MAC DA
                ''',
                'macda',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('macsa', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                MAC SA
                ''',
                'macsa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-bad-tag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Match Bad Tag
                ''',
                'match_bad_tag',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-kay-tag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MatchKaYTag
                ''',
                'match_kay_tag',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-pri', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Match Priority
                ''',
                'match_pri',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-tagged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MatchTagged
                ''',
                'match_tagged',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-untagged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MatchUntagged
                ''',
                'match_untagged',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Outer VLAN ID
                ''',
                'outer_vlan',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-tpid', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Outer Vlan TPID
                ''',
                'outer_vlan_tpid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Outer Vlan UserPri
                ''',
                'outer_vlan_up',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sai', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SAI
                ''',
                'sai',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                SCI
                ''',
                'sci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sci-inuse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If SCI in use
                ''',
                'sci_inuse',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('smac-inuse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If MAC SA in Use
                ''',
                'smac_inuse',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('source-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Source Port
                ''',
                'source_port',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('source-port-chk', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Source Port ChkEn
                ''',
                'source_port_chk',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI E
                ''',
                'tci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-an', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI AN
                ''',
                'tci_an',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-an-chk', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TciAnChkEn
                ''',
                'tci_an_chk',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-c', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI C
                ''',
                'tci_c',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-chk', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TciChkEn
                ''',
                'tci_chk',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-e-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI ES
                ''',
                'tci_e_xr',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-sc', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI SC
                ''',
                'tci_sc',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-scb', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI SCB
                ''',
                'tci_scb',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-v', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI V
                ''',
                'tci_v',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flow Validity
                ''',
                'valid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'tx-flow',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow.RxFlow' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow.RxFlow',
            False, 
            [
            _MetaInfoClassMember('action', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Action
                ''',
                'action',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('ctrl-check', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ctrl Pkt ChkEn
                ''',
                'ctrl_check',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('dmac-inuse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If MAC DA in Use
                ''',
                'dmac_inuse',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('ethertype', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Ether Type
                ''',
                'ethertype',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('flow-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Flow Index
                ''',
                'flow_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-use', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                In Use
                ''',
                'in_use',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Inner VLAN ID
                ''',
                'inner_vlan',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-tpid', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Inner Vlan TPID
                ''',
                'inner_vlan_tpid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Inner Vlan UserPri
                ''',
                'inner_vlan_up',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-ctrl-pkt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Control Pkt
                ''',
                'is_ctrl_pkt',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-egress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                rx_tx direction
                ''',
                'is_egress',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('macda', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                MAC DA
                ''',
                'macda',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('macsa', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                MAC SA
                ''',
                'macsa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-bad-tag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Match Bad Tag
                ''',
                'match_bad_tag',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-kay-tag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MatchKaYTag
                ''',
                'match_kay_tag',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-pri', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Match Priority
                ''',
                'match_pri',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-tagged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MatchTagged
                ''',
                'match_tagged',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-untagged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MatchUntagged
                ''',
                'match_untagged',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Outer VLAN ID
                ''',
                'outer_vlan',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-tpid', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Outer Vlan TPID
                ''',
                'outer_vlan_tpid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Outer Vlan UserPri
                ''',
                'outer_vlan_up',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sai', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SAI
                ''',
                'sai',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                SCI
                ''',
                'sci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sci-inuse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If SCI in use
                ''',
                'sci_inuse',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('smac-inuse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If MAC SA in Use
                ''',
                'smac_inuse',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('source-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Source Port
                ''',
                'source_port',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('source-port-chk', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Source Port ChkEn
                ''',
                'source_port_chk',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI E
                ''',
                'tci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-an', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI AN
                ''',
                'tci_an',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-an-chk', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TciAnChkEn
                ''',
                'tci_an_chk',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-c', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI C
                ''',
                'tci_c',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-chk', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TciChkEn
                ''',
                'tci_chk',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-e-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI ES
                ''',
                'tci_e_xr',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-sc', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI SC
                ''',
                'tci_sc',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-scb', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI SCB
                ''',
                'tci_scb',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-v', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI V
                ''',
                'tci_v',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flow Validity
                ''',
                'valid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'rx-flow',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow',
            False, 
            [
            _MetaInfoClassMember('rx-flow', REFERENCE_CLASS, 'RxFlow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow.RxFlow', 
                [], [], 
                '''                Rx Flow Details
                ''',
                'rx_flow',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tx-flow', REFERENCE_CLASS, 'TxFlow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow.TxFlow', 
                [], [], 
                '''                Tx Flow Details
                ''',
                'tx_flow',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'msfpga-flow',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow',
            False, 
            [
            _MetaInfoClassMember('flow-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FLOW ID
                ''',
                'flow_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', True),
            _MetaInfoClassMember('hw-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Hardware Type
                ''',
                'hw_type',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('msfpga-flow', REFERENCE_CLASS, 'MsfpgaFlow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow', 
                [], [], 
                '''                MSFPGA Flow Information
                ''',
                'msfpga_flow',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'hw-flow',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwFlowS' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwFlowS',
            False, 
            [
            _MetaInfoClassMember('hw-flow', REFERENCE_LIST, 'HwFlow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow', 
                [], [], 
                '''                Hardware Flow
                ''',
                'hw_flow',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'hw-flow-s',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow.TxFlow' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow.TxFlow',
            False, 
            [
            _MetaInfoClassMember('action', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Action
                ''',
                'action',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('ctrl-check', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ctrl Pkt ChkEn
                ''',
                'ctrl_check',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('dmac-inuse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If MAC DA in Use
                ''',
                'dmac_inuse',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('ethertype', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Ether Type
                ''',
                'ethertype',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('flow-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Flow Index
                ''',
                'flow_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-use', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                In Use
                ''',
                'in_use',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Inner VLAN ID
                ''',
                'inner_vlan',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-tpid', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Inner Vlan TPID
                ''',
                'inner_vlan_tpid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Inner Vlan UserPri
                ''',
                'inner_vlan_up',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-ctrl-pkt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Control Pkt
                ''',
                'is_ctrl_pkt',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-egress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                rx_tx direction
                ''',
                'is_egress',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('macda', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                MAC DA
                ''',
                'macda',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('macsa', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                MAC SA
                ''',
                'macsa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-bad-tag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Match Bad Tag
                ''',
                'match_bad_tag',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-kay-tag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MatchKaYTag
                ''',
                'match_kay_tag',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-pri', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Match Priority
                ''',
                'match_pri',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-tagged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MatchTagged
                ''',
                'match_tagged',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-untagged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MatchUntagged
                ''',
                'match_untagged',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Outer VLAN ID
                ''',
                'outer_vlan',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-tpid', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Outer Vlan TPID
                ''',
                'outer_vlan_tpid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Outer Vlan UserPri
                ''',
                'outer_vlan_up',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sai', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SAI
                ''',
                'sai',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                SCI
                ''',
                'sci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sci-inuse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If SCI in use
                ''',
                'sci_inuse',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('smac-inuse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If MAC SA in Use
                ''',
                'smac_inuse',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('source-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Source Port
                ''',
                'source_port',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('source-port-chk', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Source Port ChkEn
                ''',
                'source_port_chk',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI E
                ''',
                'tci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-an', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI AN
                ''',
                'tci_an',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-an-chk', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TciAnChkEn
                ''',
                'tci_an_chk',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-c', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI C
                ''',
                'tci_c',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-chk', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TciChkEn
                ''',
                'tci_chk',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-e-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI ES
                ''',
                'tci_e_xr',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-sc', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI SC
                ''',
                'tci_sc',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-scb', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI SCB
                ''',
                'tci_scb',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-v', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI V
                ''',
                'tci_v',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flow Validity
                ''',
                'valid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'tx-flow',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow.RxFlow' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow.RxFlow',
            False, 
            [
            _MetaInfoClassMember('action', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Action
                ''',
                'action',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('ctrl-check', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ctrl Pkt ChkEn
                ''',
                'ctrl_check',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('dmac-inuse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If MAC DA in Use
                ''',
                'dmac_inuse',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('ethertype', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Ether Type
                ''',
                'ethertype',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('flow-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Flow Index
                ''',
                'flow_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-use', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                In Use
                ''',
                'in_use',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Inner VLAN ID
                ''',
                'inner_vlan',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-tpid', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Inner Vlan TPID
                ''',
                'inner_vlan_tpid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Inner Vlan UserPri
                ''',
                'inner_vlan_up',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-ctrl-pkt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Control Pkt
                ''',
                'is_ctrl_pkt',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-egress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                rx_tx direction
                ''',
                'is_egress',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('macda', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                MAC DA
                ''',
                'macda',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('macsa', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                MAC SA
                ''',
                'macsa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-bad-tag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Match Bad Tag
                ''',
                'match_bad_tag',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-kay-tag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MatchKaYTag
                ''',
                'match_kay_tag',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-pri', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Match Priority
                ''',
                'match_pri',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-tagged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MatchTagged
                ''',
                'match_tagged',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-untagged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MatchUntagged
                ''',
                'match_untagged',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Outer VLAN ID
                ''',
                'outer_vlan',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-tpid', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Outer Vlan TPID
                ''',
                'outer_vlan_tpid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-up', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Outer Vlan UserPri
                ''',
                'outer_vlan_up',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sai', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SAI
                ''',
                'sai',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                SCI
                ''',
                'sci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sci-inuse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If SCI in use
                ''',
                'sci_inuse',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('smac-inuse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If MAC SA in Use
                ''',
                'smac_inuse',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('source-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Source Port
                ''',
                'source_port',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('source-port-chk', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Source Port ChkEn
                ''',
                'source_port_chk',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI E
                ''',
                'tci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-an', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI AN
                ''',
                'tci_an',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-an-chk', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TciAnChkEn
                ''',
                'tci_an_chk',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-c', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI C
                ''',
                'tci_c',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-chk', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TciChkEn
                ''',
                'tci_chk',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-e-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI ES
                ''',
                'tci_e_xr',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-sc', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI SC
                ''',
                'tci_sc',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-scb', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI SCB
                ''',
                'tci_scb',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-v', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                TCI V
                ''',
                'tci_v',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flow Validity
                ''',
                'valid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'rx-flow',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow',
            False, 
            [
            _MetaInfoClassMember('rx-flow', REFERENCE_CLASS, 'RxFlow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow.RxFlow', 
                [], [], 
                '''                Rx Flow Details
                ''',
                'rx_flow',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tx-flow', REFERENCE_CLASS, 'TxFlow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow.TxFlow', 
                [], [], 
                '''                Tx Flow Details
                ''',
                'tx_flow',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'msfpga-flow',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow',
            False, 
            [
            _MetaInfoClassMember('flow-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                FLOW ID
                ''',
                'flow_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', True),
            _MetaInfoClassMember('hw-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Hardware Type
                ''',
                'hw_type',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('msfpga-flow', REFERENCE_CLASS, 'MsfpgaFlow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow', 
                [], [], 
                '''                MSFPGA Flow Information
                ''',
                'msfpga_flow',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'sw-flow',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwFlowS' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwFlowS',
            False, 
            [
            _MetaInfoClassMember('sw-flow', REFERENCE_LIST, 'SwFlow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow', 
                [], [], 
                '''                Software Flow
                ''',
                'sw_flow',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'sw-flow-s',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.TxSaStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.TxSaStats',
            False, 
            [
            _MetaInfoClassMember('out-octets-encrypted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Octets Encrypted
                ''',
                'out_octets_encrypted',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-octets-protected', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Octets Protected
                ''',
                'out_octets_protected',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkts-encrypted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Pkts Encrypted
                ''',
                'out_pkts_encrypted',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkts-protected', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Pkts Protected
                ''',
                'out_pkts_protected',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'tx-sa-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.RxSaStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.RxSaStats',
            False, 
            [
            _MetaInfoClassMember('in-octets-decrypted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Octets Decrypted
                ''',
                'in_octets_decrypted',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-octets-validated', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Octets Validated
                ''',
                'in_octets_validated',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-delayed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Delayed
                ''',
                'in_pkts_delayed',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Invalid
                ''',
                'in_pkts_invalid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-late', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Late
                ''',
                'in_pkts_late',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-not-using-sa', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Not Using SA
                ''',
                'in_pkts_not_using_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-not-valid', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Not Valid
                ''',
                'in_pkts_not_valid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts OK
                ''',
                'in_pkts_ok',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-unchecked', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Unchecked
                ''',
                'in_pkts_unchecked',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-unused-sa', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Unused SA
                ''',
                'in_pkts_unused_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'rx-sa-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.TxInterfaceMacsecStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.TxInterfaceMacsecStats',
            False, 
            [
            _MetaInfoClassMember('out-pkt-too-long', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Pkts Too Long
                ''',
                'out_pkt_too_long',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkt-uncontrolled', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Pkts Uncontrolled
                ''',
                'out_pkt_uncontrolled',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkt-untagged', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Pkts Untagged
                ''',
                'out_pkt_untagged',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'tx-interface-macsec-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.RxInterfaceMacsecStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.RxInterfaceMacsecStats',
            False, 
            [
            _MetaInfoClassMember('in-pkt-bad-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Bad tag
                ''',
                'in_pkt_bad_tag',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-no-sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts No Sci
                ''',
                'in_pkt_no_sci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-notag', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Notag
                ''',
                'in_pkt_notag',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-overrun', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Over Run
                ''',
                'in_pkt_overrun',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-tagged', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Tagged
                ''',
                'in_pkt_tagged',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-uncontrolled', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Uncontrolled
                ''',
                'in_pkt_uncontrolled',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-unknown-sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Unknown Sci
                ''',
                'in_pkt_unknown_sci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-untagged', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Untagged
                ''',
                'in_pkt_untagged',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'rx-interface-macsec-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats',
            False, 
            [
            _MetaInfoClassMember('rx-interface-macsec-stats', REFERENCE_CLASS, 'RxInterfaceMacsecStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.RxInterfaceMacsecStats', 
                [], [], 
                '''                Rx interface Macsec Stats
                ''',
                'rx_interface_macsec_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('rx-sa-stats', REFERENCE_CLASS, 'RxSaStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.RxSaStats', 
                [], [], 
                '''                Rx SA Stats
                ''',
                'rx_sa_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tx-interface-macsec-stats', REFERENCE_CLASS, 'TxInterfaceMacsecStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.TxInterfaceMacsecStats', 
                [], [], 
                '''                Tx interface Macsec Stats
                ''',
                'tx_interface_macsec_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tx-sa-stats', REFERENCE_CLASS, 'TxSaStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.TxSaStats', 
                [], [], 
                '''                Tx SA Stats
                ''',
                'tx_sa_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'msfpga-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwStatistics',
            False, 
            [
            _MetaInfoClassMember('hw-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Hardware Type
                ''',
                'hw_type',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('msfpga-stats', REFERENCE_CLASS, 'MsfpgaStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats', 
                [], [], 
                '''                MSFPGA Stats
                ''',
                'msfpga_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'sw-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Value
                ''',
                'name',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', True),
            _MetaInfoClassMember('hw-flow-s', REFERENCE_CLASS, 'HwFlowS' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwFlowS', 
                [], [], 
                '''                Table of Hardware Flows
                ''',
                'hw_flow_s',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('hw-sas', REFERENCE_CLASS, 'HwSas' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwSas', 
                [], [], 
                '''                Table of Hardware SAs
                ''',
                'hw_sas',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('hw-statistics', REFERENCE_CLASS, 'HwStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics', 
                [], [], 
                '''                The Hardware Statistics
                ''',
                'hw_statistics',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sw-flow-s', REFERENCE_CLASS, 'SwFlowS' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwFlowS', 
                [], [], 
                '''                Table of sofware Flows
                ''',
                'sw_flow_s',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sw-sas', REFERENCE_CLASS, 'SwSas' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwSas', 
                [], [], 
                '''                Table of Software SAs
                ''',
                'sw_sas',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sw-statistics', REFERENCE_CLASS, 'SwStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics', 
                [], [], 
                '''                The Software Statistics
                ''',
                'sw_statistics',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface', 
                [], [], 
                '''                Interface Where Macsec is configured
                ''',
                'interface',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node
                ''',
                'node_name',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', True),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces', 
                [], [], 
                '''                Table of Interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node', 
                [], [], 
                '''                Node where macsec interfaces exist
                ''',
                'node',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec' : {
        'meta_info' : _MetaInfoClass('Macsec',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes', 
                [], [], 
                '''                NodeTable for all the nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'macsec',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
}
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.TxSaStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.RxSaStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.TxInterfaceMacsecStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats.RxInterfaceMacsecStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa.TxSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa.RxSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa.TxSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa.RxSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow.TxFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow.RxFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow.TxFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow.RxFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.TxSaStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.RxSaStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.TxInterfaceMacsecStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.RxInterfaceMacsecStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['Macsec.Nodes.Node']['meta_info']
_meta_table['Macsec.Nodes.Node']['meta_info'].parent =_meta_table['Macsec.Nodes']['meta_info']
_meta_table['Macsec.Nodes']['meta_info'].parent =_meta_table['Macsec']['meta_info']
