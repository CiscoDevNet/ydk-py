


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
    'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecTxStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecTxStats',
            False, 
            [
            _MetaInfoClassMember('current-an', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Current Tx AN
                ''',
                'current_an',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-encrypted-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Current Tx SA Encrypted Packets
                ''',
                'sa_encrypted_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-encrypted-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Octets Encrypted
                ''',
                'sc_encrypted_octets',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-encrypted-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx packets Encrypted
                ''',
                'sc_encrypted_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-overrun-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Overrun Packets
                ''',
                'sc_overrun_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-toolong-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Pkts Too Long
                ''',
                'sc_toolong_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-untagged-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Untagged Packets
                ''',
                'sc_untagged_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'macsec-tx-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecRxStats.RxSaStat' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecRxStats.RxSaStat',
            False, 
            [
            _MetaInfoClassMember('an', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Current Rx AN
                ''',
                'an',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-invalid-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Invalid Pkts for current AN
                ''',
                'sa_invalid_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-not-using-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts not using SA for Current AN
                ''',
                'sa_not_using_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-not-valid-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Not Valid Pkts for Current AN
                ''',
                'sa_not_valid_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-ok-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Ok Pkts for Current AN
                ''',
                'sa_ok_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-unused-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Unused Pkts for Current AN
                ''',
                'sa_unused_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'rx-sa-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecRxStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecRxStats',
            False, 
            [
            _MetaInfoClassMember('rx-sa-stat', REFERENCE_LIST, 'RxSaStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecRxStats.RxSaStat', 
                [], [], 
                '''                Rx SA Level Stats
                ''',
                'rx_sa_stat',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-bad-tag-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Bad Tag Packets
                ''',
                'sc_bad_tag_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-decrypted-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Octets Decrypted
                ''',
                'sc_decrypted_octets',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-delayed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Delayed Pkts
                ''',
                'sc_delayed_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-invalid-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Invalid
                ''',
                'sc_invalid_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-late-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Late Pkts
                ''',
                'sc_late_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-no-sci-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx No SCI Pkts
                ''',
                'sc_no_sci_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-no-tag-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx No Tag Packets
                ''',
                'sc_no_tag_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-not-using-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Not Using SA
                ''',
                'sc_not_using_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-not-valid-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Not Valid Pkts
                ''',
                'sc_not_valid_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-ok-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Ok
                ''',
                'sc_ok_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-overrun-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Overrun Pkts
                ''',
                'sc_overrun_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-unchecked-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Unchecked Pkts
                ''',
                'sc_unchecked_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-unknown-sci-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Unknown SCI Pkts
                ''',
                'sc_unknown_sci_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-untagged-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Untagged Packets
                ''',
                'sc_untagged_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-unused-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Unused SA
                ''',
                'sc_unused_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'macsec-rx-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats',
            False, 
            [
            _MetaInfoClassMember('macsec-rx-stats', REFERENCE_CLASS, 'MacsecRxStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecRxStats', 
                [], [], 
                '''                Rx SC and SA Level Stats
                ''',
                'macsec_rx_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('macsec-tx-stats', REFERENCE_CLASS, 'MacsecTxStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecTxStats', 
                [], [], 
                '''                Tx SC and SA Level Stats
                ''',
                'macsec_tx_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'xlfpga-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.TxSaStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.TxSaStats',
            False, 
            [
            _MetaInfoClassMember('out-octets-encrypted-protected1', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                octets1 encrypted/protected ?
                ''',
                'out_octets_encrypted_protected1',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-octets-encrypted-protected2', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                octets2 encrypted/protected ?
                ''',
                'out_octets_encrypted_protected2',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkts-encrypted-protected', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packets encrypted/protected
                ''',
                'out_pkts_encrypted_protected',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkts-sa-not-in-use', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packets coming on SA that is expired or
                otherwise not-in-use
                ''',
                'out_pkts_sa_not_in_use',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkts-too-long', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packets exceeding egress MTU
                ''',
                'out_pkts_too_long',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'tx-sa-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.RxSaStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.RxSaStats',
            False, 
            [
            _MetaInfoClassMember('in-octets-decrypted-validated1', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                octets1 decrypted/validated
                ''',
                'in_octets_decrypted_validated1',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-octets-decrypted-validated2', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                octets2 decrypted/validated
                ''',
                'in_octets_decrypted_validated2',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-octets-validated', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                octets validated
                ''',
                'in_octets_validated',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-delayed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PN of packet outside replay window &
                validateFrames !strict
                ''',
                'in_pkts_delayed',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packet not valid & validateFrames !strict
                ''',
                'in_pkts_invalid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-late', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PN of packet outside replay window &
                validateFrames strict
                ''',
                'in_pkts_late',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-not-using-sa', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packet assigned to SA not in use &
                validateFrames strict
                ''',
                'in_pkts_not_using_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-not-valid', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packet not valid & validateFrames strict
                ''',
                'in_pkts_not_valid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packets with no error
                ''',
                'in_pkts_ok',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-sa-not-in-use', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packets coming on SA that is
                ''',
                'in_pkts_sa_not_in_use',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-unchecked', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                frame not valid & validateFrames disabled
                ''',
                'in_pkts_unchecked',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-unused-sa', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packet assigned to SA not in use &
                validateFrames !strict
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
    'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.TxInterfaceMacsecStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.TxInterfaceMacsecStats',
            False, 
            [
            _MetaInfoClassMember('out-bcast-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Broadcast pkts tx on controlled port
                ''',
                'out_bcast_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-bcast-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Broadcast pkts tx on uncontrolled port
                ''',
                'out_bcast_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-drop-pkts-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets dropped due to overflow in
                classification pipeline
                ''',
                'out_drop_pkts_class',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-drop-pkts-data', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets dropped due to overflow in  processing
                pipeline
                ''',
                'out_drop_pkts_data',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-mcast-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Multicast pkts tx on controlled port
                ''',
                'out_mcast_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-mcast-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Multicast pkts tx on uncontrolled port
                ''',
                'out_mcast_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-octets-common', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Octets tx on common port
                ''',
                'out_octets_common',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-octets-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Octets tx on controlled port
                ''',
                'out_octets_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-octets-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Octets tx on uncontrolled port
                ''',
                'out_octets_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkt-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                egress packet that is classified as control
                packet
                ''',
                'out_pkt_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkts-untagged', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                egress packet to go out untagged when
                protectFrames not set
                ''',
                'out_pkts_untagged',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-rx-drop-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Data pkts dropped due to overrun
                ''',
                'out_rx_drop_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-rx-drop-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Control pkts dropped due to overrun
                ''',
                'out_rx_drop_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-rx-err-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Data pkts error-terminated due to overrun
                ''',
                'out_rx_err_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-rx-err-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Control pkts error-terminated due to overrun
                ''',
                'out_rx_err_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-ucast-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unicast pkts tx on controlled port
                ''',
                'out_ucast_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-ucast-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unicast pkts tx on uncontrolled port
                ''',
                'out_ucast_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('transform-error-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                counter to count internal errors in the MACSec
                core
                ''',
                'transform_error_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'tx-interface-macsec-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.RxInterfaceMacsecStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.RxInterfaceMacsecStats',
            False, 
            [
            _MetaInfoClassMember('in-bcast-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Broadcast pkts rx on controlled port
                ''',
                'in_bcast_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-bcast-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Broadcast pkts rx on uncontrolled port
                ''',
                'in_bcast_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-drop-pkts-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets dropped due to overflow in
                classification pipeline
                ''',
                'in_drop_pkts_class',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-drop-pkts-data', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets dropped due to overflow in processing
                pipeline
                ''',
                'in_drop_pkts_data',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-mcast-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Multicast pkts rx on controlled port
                ''',
                'in_mcast_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-mcast-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Multicast pkts rx on uncontrolled port
                ''',
                'in_mcast_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-octets-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Octets rx on controlled port
                ''',
                'in_octets_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-octets-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Octets rx on uncontrolled port
                ''',
                'in_octets_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-bad-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ingress frames received with an invalid MACSec
                tag or ICV                                      
                added with next one gives InPktsSCIMiss
                ''',
                'in_pkt_bad_tag',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ingress packet that is classified as control
                packet
                ''',
                'in_pkt_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-no-sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                correctly tagged ingress frames for which no
                valid SC found & \;                             
                validateFrames is strict
                ''',
                'in_pkt_no_sci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-no-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ingress packet untagged & validateFrames is
                strict
                ''',
                'in_pkt_no_tag',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-tagged-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ingress packets that are control or KaY packets
                ''',
                'in_pkts_tagged_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-unknown-sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                correctly tagged ingress frames for which no
                valid SC found &                                
                validateFrames is !strict
                ''',
                'in_pkts_unknown_sci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-untagged', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ingress packet untagged & validateFrames is 
                !strict
                ''',
                'in_pkts_untagged',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-rx-drop-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Data pkts dropped due to overrun
                ''',
                'in_rx_drop_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-rx-drop-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Control pkts dropped due to overrun
                ''',
                'in_rx_drop_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-rx-error-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Data pkts error-terminated due to overrun
                ''',
                'in_rx_error_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-rx-error-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Control pkts error-terminated due to overrun
                ''',
                'in_rx_error_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-ucast-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unicast pkts rx on controlled port
                ''',
                'in_ucast_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-ucast-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unicast pkts rx on uncontrolled port
                ''',
                'in_ucast_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('transform-error-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                counter to count internal errors in the MACSec
                core
                ''',
                'transform_error_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'rx-interface-macsec-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats',
            False, 
            [
            _MetaInfoClassMember('rx-interface-macsec-stats', REFERENCE_CLASS, 'RxInterfaceMacsecStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.RxInterfaceMacsecStats', 
                [], [], 
                '''                Rx interface Macsec Stats
                ''',
                'rx_interface_macsec_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('rx-sa-stats', REFERENCE_CLASS, 'RxSaStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.RxSaStats', 
                [], [], 
                '''                Rx SA Stats
                ''',
                'rx_sa_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tx-interface-macsec-stats', REFERENCE_CLASS, 'TxInterfaceMacsecStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.TxInterfaceMacsecStats', 
                [], [], 
                '''                Tx interface Macsec Stats
                ''',
                'tx_interface_macsec_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tx-sa-stats', REFERENCE_CLASS, 'TxSaStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.TxSaStats', 
                [], [], 
                '''                Tx SA Stats
                ''',
                'tx_sa_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'es200-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwStatistics',
            False, 
            [
            _MetaInfoClassMember('es200-stats', REFERENCE_CLASS, 'Es200Stats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats', 
                [], [], 
                '''                ES200 Stats
                ''',
                'es200_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
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
            _MetaInfoClassMember('xlfpga-stats', REFERENCE_CLASS, 'XlfpgaStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats', 
                [], [], 
                '''                XLFPGA Stats
                ''',
                'xlfpga_stats',
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
    'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa.TxSa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa.TxSa',
            False, 
            [
            _MetaInfoClassMember('an', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Association Number
                ''',
                'an',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('cipher-suite', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cipher Suite Used
                ''',
                'cipher_suite',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('confidentiality-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Confidentiality Offset
                ''',
                'confidentiality_offset',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('crc-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CRC Value
                ''',
                'crc_value',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('current-packet-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Current Packet Number
                ''',
                'current_packet_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('fcs-err-cfg', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                FCS Error Config
                ''',
                'fcs_err_cfg',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('initial-packet-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Initial Packet Number
                ''',
                'initial_packet_number',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('max-packet-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Max Packet Number
                ''',
                'max_packet_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('protection-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Protection Enabled
                ''',
                'protection_enable',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sectag-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sec Tag Length(bytes) 
                ''',
                'sectag_length',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('secure-channel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Secure Channel ID
                ''',
                'secure_channel_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('secure-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Secure Mode - Must/Should
                ''',
                'secure_mode',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('ssci', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Short Secure Channel ID
                ''',
                'ssci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'tx-sa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa.RxSa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa.RxSa',
            False, 
            [
            _MetaInfoClassMember('an', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Association Number
                ''',
                'an',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('auth-err-cfg', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Auth  Error Config
                ''',
                'auth_err_cfg',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('cipher-suite', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cipher Suite Used
                ''',
                'cipher_suite',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('confidentiality-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Confidentiality Offset
                ''',
                'confidentiality_offset',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('crc-value', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CRC Value
                ''',
                'crc_value',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False, max_elements=4),
            _MetaInfoClassMember('current-packet-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Current Packet Number
                ''',
                'current_packet_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('fcs-err-cfg', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FCS Error Config
                ''',
                'fcs_err_cfg',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('lowest-acceptable-packet-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Lowest Acceptable Packet Number
                ''',
                'lowest_acceptable_packet_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('max-packet-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Max Packet Number
                ''',
                'max_packet_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('next-expected-packet-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Next expected Packet Number
                ''',
                'next_expected_packet_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('num-an-in-use', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Num of AN's in Use
                ''',
                'num_an_in_use',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkt-tagged-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Tagged Pkts Detected
                ''',
                'pkt_tagged_detected',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkt-tagged-validated', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Tagged Pkts Validated
                ''',
                'pkt_tagged_validated',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkt-untagged-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Untagged Pkts Detected
                ''',
                'pkt_untagged_detected',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('protection-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Protection Enabled
                ''',
                'protection_enable',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('recent-an', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Recent Association Num
                ''',
                'recent_an',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('replay-protect-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Replay Protect Mode
                ''',
                'replay_protect_mode',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('replay-window', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Replay Window 
                ''',
                'replay_window',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('secure-channel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Secure Channel ID
                ''',
                'secure_channel_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('secure-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Secure Mode - Must/Should
                ''',
                'secure_mode',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('ssci', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Short Secure Channel ID
                ''',
                'ssci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False, max_elements=4),
            _MetaInfoClassMember('validation-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Validation Mode
                ''',
                'validation_mode',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'rx-sa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa',
            False, 
            [
            _MetaInfoClassMember('rx-sa', REFERENCE_CLASS, 'RxSa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa.RxSa', 
                [], [], 
                '''                Rx SA Details
                ''',
                'rx_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tx-sa', REFERENCE_CLASS, 'TxSa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa.TxSa', 
                [], [], 
                '''                Tx SA Details
                ''',
                'tx_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'xlfpga-sa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.TxSa.XformParams' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.TxSa.XformParams',
            False, 
            [
            _MetaInfoClassMember('aes-key-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AES Key length
                ''',
                'aes_key_len',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('assoc-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Association Number for egress
                ''',
                'assoc_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('bgen-auth-key', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to generate the authKey, so authKey in this
                struct not used                                 
                APM_FALSE to use provided authKey
                ''',
                'bgen_auth_key',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('crypt-algo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cryptographic algo used
                ''',
                'crypt_algo',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-egress-tr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                APM_TRUE if this is Egress Transform record,
                APM_FALSE otherwise
                ''',
                'is_egress_tr',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-seq-num64-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if Seq Num is 64-bit, FALSE if it is 32-bit
                ''',
                'is_seq_num64_bit',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('replay-win-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                range of pkt nos considered valid
                ''',
                'replay_win_size',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'xform-params',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.TxSa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.TxSa',
            False, 
            [
            _MetaInfoClassMember('is-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is structure valid
                ''',
                'is_valid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-octets-encrypted-protected1', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                octets1 encrypted/protected
                ''',
                'out_octets_encrypted_protected1',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-octets-encrypted-protected2', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                octets2 encrypted/protected
                ''',
                'out_octets_encrypted_protected2',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkts-encrypted-protected', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                packets encrypted/protected
                ''',
                'out_pkts_encrypted_protected',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkts-sa-not-in-use', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                packets coming on SA that is
                ''',
                'out_pkts_sa_not_in_use',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkts-too-long', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                packets exceeding egress MTU
                ''',
                'out_pkts_too_long',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                SA Index
                ''',
                'sa_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SC Number
                ''',
                'sc_no',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('xform-params', REFERENCE_CLASS, 'XformParams' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.TxSa.XformParams', 
                [], [], 
                '''                 Xform Params
                ''',
                'xform_params',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'tx-sa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.RxSa.XformParams' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.RxSa.XformParams',
            False, 
            [
            _MetaInfoClassMember('aes-key-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AES Key length
                ''',
                'aes_key_len',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('assoc-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Association Number for egress
                ''',
                'assoc_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('bgen-auth-key', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to generate the authKey, so authKey in this
                struct not used                                 
                APM_FALSE to use provided authKey
                ''',
                'bgen_auth_key',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('crypt-algo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cryptographic algo used
                ''',
                'crypt_algo',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-egress-tr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                APM_TRUE if this is Egress Transform record,
                APM_FALSE otherwise
                ''',
                'is_egress_tr',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-seq-num64-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if Seq Num is 64-bit, FALSE if it is 32-bit
                ''',
                'is_seq_num64_bit',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('replay-win-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                range of pkt nos considered valid
                ''',
                'replay_win_size',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'xform-params',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.RxSa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.RxSa',
            False, 
            [
            _MetaInfoClassMember('in-octets-decrypted-validated1', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                octets1 decrypted/validated
                ''',
                'in_octets_decrypted_validated1',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-octets-decrypted-validated2', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                octets2 decrypted/validated
                ''',
                'in_octets_decrypted_validated2',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-octets-validated', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                octets validated
                ''',
                'in_octets_validated',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-delayed', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PN of packet outside replay window &
                validateFrames !strict
                ''',
                'in_pkts_delayed',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                packet not valid & validateFrames !strict
                ''',
                'in_pkts_invalid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-late', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PN of packet outside replay window &
                validateFrames strict
                ''',
                'in_pkts_late',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-not-using-sa', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                packet assigned to SA not in use &
                validateFrames strict
                ''',
                'in_pkts_not_using_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-not-valid', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                packet not valid & validateFrames strict
                ''',
                'in_pkts_not_valid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                packets with no error
                ''',
                'in_pkts_ok',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-unchecked', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                frame not valid & validateFrames disabled
                ''',
                'in_pkts_unchecked',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-unused-sa', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                packet assigned to SA not in use& validateFrames
                !strict
                ''',
                'in_pkts_unused_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is structure valid
                ''',
                'is_valid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                SA Index
                ''',
                'sa_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SC Number
                ''',
                'sc_no',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('xform-params', REFERENCE_CLASS, 'XformParams' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.RxSa.XformParams', 
                [], [], 
                '''                 Xform Params
                ''',
                'xform_params',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'rx-sa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa',
            False, 
            [
            _MetaInfoClassMember('rx-sa', REFERENCE_CLASS, 'RxSa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.RxSa', 
                [], [], 
                '''                Rx SA Details
                ''',
                'rx_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tx-sa', REFERENCE_CLASS, 'TxSa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.TxSa', 
                [], [], 
                '''                Tx SA Details
                ''',
                'tx_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'es200-sa',
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
            _MetaInfoClassMember('es200-sa', REFERENCE_CLASS, 'Es200Sa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa', 
                [], [], 
                '''                ES200 SA Information
                ''',
                'es200_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
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
            _MetaInfoClassMember('xlfpga-sa', REFERENCE_CLASS, 'XlfpgaSa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa', 
                [], [], 
                '''                XLFPGA SA Information
                ''',
                'xlfpga_sa',
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
    'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa.TxSa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa.TxSa',
            False, 
            [
            _MetaInfoClassMember('an', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Association Number
                ''',
                'an',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('cipher-suite', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cipher Suite Used
                ''',
                'cipher_suite',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('confidentiality-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Confidentiality Offset
                ''',
                'confidentiality_offset',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('crc-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CRC Value
                ''',
                'crc_value',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('current-packet-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Current Packet Number
                ''',
                'current_packet_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('fcs-err-cfg', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                FCS Error Config
                ''',
                'fcs_err_cfg',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('initial-packet-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Initial Packet Number
                ''',
                'initial_packet_number',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('max-packet-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Max Packet Number
                ''',
                'max_packet_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('protection-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Protection Enabled
                ''',
                'protection_enable',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sectag-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sec Tag Length(bytes) 
                ''',
                'sectag_length',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('secure-channel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Secure Channel ID
                ''',
                'secure_channel_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('secure-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Secure Mode - Must/Should
                ''',
                'secure_mode',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('ssci', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Short Secure Channel ID
                ''',
                'ssci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'tx-sa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa.RxSa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa.RxSa',
            False, 
            [
            _MetaInfoClassMember('an', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Association Number
                ''',
                'an',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('auth-err-cfg', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Auth  Error Config
                ''',
                'auth_err_cfg',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('cipher-suite', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cipher Suite Used
                ''',
                'cipher_suite',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('confidentiality-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Confidentiality Offset
                ''',
                'confidentiality_offset',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('crc-value', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CRC Value
                ''',
                'crc_value',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False, max_elements=4),
            _MetaInfoClassMember('current-packet-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Current Packet Number
                ''',
                'current_packet_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('fcs-err-cfg', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FCS Error Config
                ''',
                'fcs_err_cfg',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('lowest-acceptable-packet-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Lowest Acceptable Packet Number
                ''',
                'lowest_acceptable_packet_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('max-packet-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Max Packet Number
                ''',
                'max_packet_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('next-expected-packet-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Next expected Packet Number
                ''',
                'next_expected_packet_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('num-an-in-use', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Num of AN's in Use
                ''',
                'num_an_in_use',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkt-tagged-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Tagged Pkts Detected
                ''',
                'pkt_tagged_detected',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkt-tagged-validated', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Tagged Pkts Validated
                ''',
                'pkt_tagged_validated',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkt-untagged-detected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Untagged Pkts Detected
                ''',
                'pkt_untagged_detected',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('protection-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Protection Enabled
                ''',
                'protection_enable',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('recent-an', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Recent Association Num
                ''',
                'recent_an',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('replay-protect-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Replay Protect Mode
                ''',
                'replay_protect_mode',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('replay-window', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Replay Window 
                ''',
                'replay_window',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('secure-channel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Secure Channel ID
                ''',
                'secure_channel_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('secure-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Secure Mode - Must/Should
                ''',
                'secure_mode',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('ssci', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Short Secure Channel ID
                ''',
                'ssci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False, max_elements=4),
            _MetaInfoClassMember('validation-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Validation Mode
                ''',
                'validation_mode',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'rx-sa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa',
            False, 
            [
            _MetaInfoClassMember('rx-sa', REFERENCE_CLASS, 'RxSa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa.RxSa', 
                [], [], 
                '''                Rx SA Details
                ''',
                'rx_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tx-sa', REFERENCE_CLASS, 'TxSa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa.TxSa', 
                [], [], 
                '''                Tx SA Details
                ''',
                'tx_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'xlfpga-sa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.TxSa.XformParams' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.TxSa.XformParams',
            False, 
            [
            _MetaInfoClassMember('aes-key-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AES Key length
                ''',
                'aes_key_len',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('assoc-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Association Number for egress
                ''',
                'assoc_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('bgen-auth-key', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to generate the authKey, so authKey in this
                struct not used                                 
                APM_FALSE to use provided authKey
                ''',
                'bgen_auth_key',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('crypt-algo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cryptographic algo used
                ''',
                'crypt_algo',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-egress-tr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                APM_TRUE if this is Egress Transform record,
                APM_FALSE otherwise
                ''',
                'is_egress_tr',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-seq-num64-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if Seq Num is 64-bit, FALSE if it is 32-bit
                ''',
                'is_seq_num64_bit',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('replay-win-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                range of pkt nos considered valid
                ''',
                'replay_win_size',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'xform-params',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.TxSa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.TxSa',
            False, 
            [
            _MetaInfoClassMember('is-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is structure valid
                ''',
                'is_valid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-octets-encrypted-protected1', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                octets1 encrypted/protected
                ''',
                'out_octets_encrypted_protected1',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-octets-encrypted-protected2', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                octets2 encrypted/protected
                ''',
                'out_octets_encrypted_protected2',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkts-encrypted-protected', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                packets encrypted/protected
                ''',
                'out_pkts_encrypted_protected',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkts-sa-not-in-use', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                packets coming on SA that is
                ''',
                'out_pkts_sa_not_in_use',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkts-too-long', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                packets exceeding egress MTU
                ''',
                'out_pkts_too_long',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                SA Index
                ''',
                'sa_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SC Number
                ''',
                'sc_no',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('xform-params', REFERENCE_CLASS, 'XformParams' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.TxSa.XformParams', 
                [], [], 
                '''                 Xform Params
                ''',
                'xform_params',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'tx-sa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.RxSa.XformParams' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.RxSa.XformParams',
            False, 
            [
            _MetaInfoClassMember('aes-key-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AES Key length
                ''',
                'aes_key_len',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('assoc-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Association Number for egress
                ''',
                'assoc_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('bgen-auth-key', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to generate the authKey, so authKey in this
                struct not used                                 
                APM_FALSE to use provided authKey
                ''',
                'bgen_auth_key',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('crypt-algo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cryptographic algo used
                ''',
                'crypt_algo',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-egress-tr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                APM_TRUE if this is Egress Transform record,
                APM_FALSE otherwise
                ''',
                'is_egress_tr',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-seq-num64-bit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if Seq Num is 64-bit, FALSE if it is 32-bit
                ''',
                'is_seq_num64_bit',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('replay-win-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                range of pkt nos considered valid
                ''',
                'replay_win_size',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'xform-params',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.RxSa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.RxSa',
            False, 
            [
            _MetaInfoClassMember('in-octets-decrypted-validated1', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                octets1 decrypted/validated
                ''',
                'in_octets_decrypted_validated1',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-octets-decrypted-validated2', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                octets2 decrypted/validated
                ''',
                'in_octets_decrypted_validated2',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-octets-validated', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                octets validated
                ''',
                'in_octets_validated',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-delayed', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PN of packet outside replay window &
                validateFrames !strict
                ''',
                'in_pkts_delayed',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                packet not valid & validateFrames !strict
                ''',
                'in_pkts_invalid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-late', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PN of packet outside replay window &
                validateFrames strict
                ''',
                'in_pkts_late',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-not-using-sa', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                packet assigned to SA not in use &
                validateFrames strict
                ''',
                'in_pkts_not_using_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-not-valid', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                packet not valid & validateFrames strict
                ''',
                'in_pkts_not_valid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                packets with no error
                ''',
                'in_pkts_ok',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-unchecked', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                frame not valid & validateFrames disabled
                ''',
                'in_pkts_unchecked',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-unused-sa', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                packet assigned to SA not in use& validateFrames
                !strict
                ''',
                'in_pkts_unused_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is structure valid
                ''',
                'is_valid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                SA Index
                ''',
                'sa_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SC Number
                ''',
                'sc_no',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('xform-params', REFERENCE_CLASS, 'XformParams' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.RxSa.XformParams', 
                [], [], 
                '''                 Xform Params
                ''',
                'xform_params',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'rx-sa',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa',
            False, 
            [
            _MetaInfoClassMember('rx-sa', REFERENCE_CLASS, 'RxSa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.RxSa', 
                [], [], 
                '''                Rx SA Details
                ''',
                'rx_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tx-sa', REFERENCE_CLASS, 'TxSa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.TxSa', 
                [], [], 
                '''                Tx SA Details
                ''',
                'tx_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'es200-sa',
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
            _MetaInfoClassMember('es200-sa', REFERENCE_CLASS, 'Es200Sa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa', 
                [], [], 
                '''                ES200 SA Information
                ''',
                'es200_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
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
            _MetaInfoClassMember('xlfpga-sa', REFERENCE_CLASS, 'XlfpgaSa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa', 
                [], [], 
                '''                XLFPGA SA Information
                ''',
                'xlfpga_sa',
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
    'Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow.TxFlow' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow.TxFlow',
            False, 
            [
            _MetaInfoClassMember('drop', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Drop the packet
                ''',
                'drop',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('ethertype', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Parsed EtherType to match could be 0 if
                Ethertype should'nt                             
                be matched can be 0x88E5 for MACSec tag
                ''',
                'ethertype',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('flow-miss', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts matching none of flow entries
                ''',
                'flow_miss',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('flow-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flow Number
                ''',
                'flow_no',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('force-ctrl', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Force the pkt as control pkt irrepective        
                of the results of control packet detector
                ''',
                'force_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-dei', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Dei to match for innner Vlan tag
                ''',
                'inner_vlan_dei',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN ID for inner tag used when two             
                VLAN Tags should be matched
                ''',
                'inner_vlan_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-user-pri', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 VLAN User priority for inner tag use           
                when matching two VLAN tags
                ''',
                'inner_vlan_user_pri',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-flow-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Flow Enabled
                ''',
                'is_flow_enabled',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('macda', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                MAC DA
                ''',
                'macda',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mask-da', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                DA mask
                ''',
                'mask_da',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mask-ethertype', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Parsed EtherType mask
                ''',
                'mask_ethertype',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mask-plain-bits', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Plain Bits mask
                ''',
                'mask_plain_bits',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                priority for match 0-15(highest) 
                ''',
                'match_priority',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls1-bos', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 botton of stack 
                ''',
                'mpls1_bos',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls1-exp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 exp 
                ''',
                'mpls1_exp',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls1-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 label 
                ''',
                'mpls1_label',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls2-bos', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 botton of stack 
                ''',
                'mpls2_bos',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls2-exp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 exp 
                ''',
                'mpls2_exp',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls2-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 label 
                ''',
                'mpls2_label',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('multi-flow-match', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts matching multiple flow entries
                ''',
                'multi_flow_match',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-dei', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Dei to match for outer Vlan tag
                ''',
                'outer_vlan_dei',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                 VLAN ID for outer tag use this when            
                only one tag should be matched
                ''',
                'outer_vlan_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-user-pri', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                VLAN User Priority for outer tag  use           
                this when only one tag should be matched
                ''',
                'outer_vlan_user_pri',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('parser-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts dropped by header parser as invalid
                ''',
                'parser_dropped',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pbb-bvid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Backbone Vlan id 
                ''',
                'pbb_bvid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pbb-dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 dei 
                ''',
                'pbb_dei',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pbb-pcp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 pcp 
                ''',
                'pbb_pcp',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pbb-sid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Service Instance id 
                ''',
                'pbb_sid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkt-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of packet. See ethMscCfyEPktType_e
                ''',
                'pkt_type',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Control pkts forwarded
                ''',
                'pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkts-data', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Data pkts forwarded
                ''',
                'pkts_data',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkts-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts dropped by classifier
                ''',
                'pkts_dropped',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkts-err-in', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts received with an error indication
                ''',
                'pkts_err_in',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('plain-bits', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Plain bits to compare. Max values:              
                untagged pkt - 40 bits after EthType            
                1 VLAN tag - 24 bits after parsed EthType       
                2 VLAN tags- 8 bits after  parsed EthType       
                1 MPLS tag - 32 bits after 1st tag              
                2 MPLS tags- 8 bits following after 2nd         
                or atmost 5th MPLS tag                          
                PBB - 16 bits after C-SA                        
                PBB with VLAN tag - 16 bits of VLAN tag 
                ''',
                'plain_bits',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('plain-bits-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No. of bits used in plainBits
                ''',
                'plain_bits_size',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('psci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                 SCI to be matched value required for           
                ingress only, pass NULL for egress
                ''',
                'psci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tag-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of MPLS or VLAN tags See ethMscCfyETagNum_e 
                ''',
                'tag_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'e' in TCI to match (1bit )
                ''',
                'tci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-c', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'c' in TCI to match (1bit) 
                ''',
                'tci_c',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-chk', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TCI bits will be checked only when this         
                bit is enabled. All the values of TCI bits      
                are mandatory when TCI check is used
                ''',
                'tci_chk',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-e-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'es' in TCI to match (1bit) 
                ''',
                'tci_e_xr',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-sc', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'sc' in TCI to match (1bit) 
                ''',
                'tci_sc',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-scb', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'scb' in TCI to match (1bit) 
                ''',
                'tci_scb',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-v', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'v' in TCI to match (1bit) 
                ''',
                'tci_v',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('vlan-dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 dei 
                ''',
                'vlan_dei',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                 vlan id 
                ''',
                'vlan_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('vlan-pcp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 pcp 
                ''',
                'vlan_pcp',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'tx-flow',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow.RxFlow' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow.RxFlow',
            False, 
            [
            _MetaInfoClassMember('drop', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Drop the packet
                ''',
                'drop',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('ethertype', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Parsed EtherType to match could be 0 if
                Ethertype should'nt                             
                be matched can be 0x88E5 for MACSec tag
                ''',
                'ethertype',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('flow-miss', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts matching none of flow entries
                ''',
                'flow_miss',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('flow-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flow Number
                ''',
                'flow_no',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('force-ctrl', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Force the pkt as control pkt irrepective        
                of the results of control packet detector
                ''',
                'force_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-dei', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Dei to match for innner Vlan tag
                ''',
                'inner_vlan_dei',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN ID for inner tag used when two             
                VLAN Tags should be matched
                ''',
                'inner_vlan_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-user-pri', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 VLAN User priority for inner tag use           
                when matching two VLAN tags
                ''',
                'inner_vlan_user_pri',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-flow-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Flow Enabled
                ''',
                'is_flow_enabled',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('macda', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                MAC DA
                ''',
                'macda',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mask-da', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                DA mask
                ''',
                'mask_da',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mask-ethertype', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Parsed EtherType mask
                ''',
                'mask_ethertype',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mask-plain-bits', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Plain Bits mask
                ''',
                'mask_plain_bits',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                priority for match 0-15(highest) 
                ''',
                'match_priority',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls1-bos', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 botton of stack 
                ''',
                'mpls1_bos',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls1-exp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 exp 
                ''',
                'mpls1_exp',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls1-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 label 
                ''',
                'mpls1_label',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls2-bos', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 botton of stack 
                ''',
                'mpls2_bos',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls2-exp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 exp 
                ''',
                'mpls2_exp',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls2-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 label 
                ''',
                'mpls2_label',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('multi-flow-match', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts matching multiple flow entries
                ''',
                'multi_flow_match',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-dei', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Dei to match for outer Vlan tag
                ''',
                'outer_vlan_dei',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                 VLAN ID for outer tag use this when            
                only one tag should be matched
                ''',
                'outer_vlan_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-user-pri', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                VLAN User Priority for outer tag  use           
                this when only one tag should be matched
                ''',
                'outer_vlan_user_pri',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('parser-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts dropped by header parser as invalid
                ''',
                'parser_dropped',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pbb-bvid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Backbone Vlan id 
                ''',
                'pbb_bvid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pbb-dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 dei 
                ''',
                'pbb_dei',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pbb-pcp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 pcp 
                ''',
                'pbb_pcp',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pbb-sid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Service Instance id 
                ''',
                'pbb_sid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkt-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of packet. See ethMscCfyEPktType_e
                ''',
                'pkt_type',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Control pkts forwarded
                ''',
                'pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkts-data', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Data pkts forwarded
                ''',
                'pkts_data',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkts-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts dropped by classifier
                ''',
                'pkts_dropped',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkts-err-in', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts received with an error indication
                ''',
                'pkts_err_in',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('plain-bits', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Plain bits to compare. Max values:              
                untagged pkt - 40 bits after EthType            
                1 VLAN tag - 24 bits after parsed EthType       
                2 VLAN tags- 8 bits after  parsed EthType       
                1 MPLS tag - 32 bits after 1st tag              
                2 MPLS tags- 8 bits following after 2nd         
                or atmost 5th MPLS tag                          
                PBB - 16 bits after C-SA                        
                PBB with VLAN tag - 16 bits of VLAN tag 
                ''',
                'plain_bits',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('plain-bits-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No. of bits used in plainBits
                ''',
                'plain_bits_size',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('psci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                 SCI to be matched value required for           
                ingress only, pass NULL for egress
                ''',
                'psci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tag-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of MPLS or VLAN tags See ethMscCfyETagNum_e 
                ''',
                'tag_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'e' in TCI to match (1bit )
                ''',
                'tci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-c', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'c' in TCI to match (1bit) 
                ''',
                'tci_c',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-chk', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TCI bits will be checked only when this         
                bit is enabled. All the values of TCI bits      
                are mandatory when TCI check is used
                ''',
                'tci_chk',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-e-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'es' in TCI to match (1bit) 
                ''',
                'tci_e_xr',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-sc', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'sc' in TCI to match (1bit) 
                ''',
                'tci_sc',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-scb', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'scb' in TCI to match (1bit) 
                ''',
                'tci_scb',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-v', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'v' in TCI to match (1bit) 
                ''',
                'tci_v',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('vlan-dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 dei 
                ''',
                'vlan_dei',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                 vlan id 
                ''',
                'vlan_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('vlan-pcp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 pcp 
                ''',
                'vlan_pcp',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'rx-flow',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow',
            False, 
            [
            _MetaInfoClassMember('rx-flow', REFERENCE_CLASS, 'RxFlow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow.RxFlow', 
                [], [], 
                '''                Rx Flow Details
                ''',
                'rx_flow',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tx-flow', REFERENCE_CLASS, 'TxFlow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow.TxFlow', 
                [], [], 
                '''                Tx Flow Details
                ''',
                'tx_flow',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'es200-flow',
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
            _MetaInfoClassMember('es200-flow', REFERENCE_CLASS, 'Es200Flow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow', 
                [], [], 
                '''                ES200 Flow Information
                ''',
                'es200_flow',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
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
    'Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow.TxFlow' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow.TxFlow',
            False, 
            [
            _MetaInfoClassMember('drop', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Drop the packet
                ''',
                'drop',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('ethertype', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Parsed EtherType to match could be 0 if
                Ethertype should'nt                             
                be matched can be 0x88E5 for MACSec tag
                ''',
                'ethertype',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('flow-miss', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts matching none of flow entries
                ''',
                'flow_miss',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('flow-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flow Number
                ''',
                'flow_no',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('force-ctrl', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Force the pkt as control pkt irrepective        
                of the results of control packet detector
                ''',
                'force_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-dei', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Dei to match for innner Vlan tag
                ''',
                'inner_vlan_dei',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN ID for inner tag used when two             
                VLAN Tags should be matched
                ''',
                'inner_vlan_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-user-pri', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 VLAN User priority for inner tag use           
                when matching two VLAN tags
                ''',
                'inner_vlan_user_pri',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-flow-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Flow Enabled
                ''',
                'is_flow_enabled',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('macda', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                MAC DA
                ''',
                'macda',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mask-da', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                DA mask
                ''',
                'mask_da',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mask-ethertype', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Parsed EtherType mask
                ''',
                'mask_ethertype',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mask-plain-bits', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Plain Bits mask
                ''',
                'mask_plain_bits',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                priority for match 0-15(highest) 
                ''',
                'match_priority',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls1-bos', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 botton of stack 
                ''',
                'mpls1_bos',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls1-exp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 exp 
                ''',
                'mpls1_exp',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls1-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 label 
                ''',
                'mpls1_label',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls2-bos', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 botton of stack 
                ''',
                'mpls2_bos',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls2-exp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 exp 
                ''',
                'mpls2_exp',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls2-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 label 
                ''',
                'mpls2_label',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('multi-flow-match', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts matching multiple flow entries
                ''',
                'multi_flow_match',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-dei', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Dei to match for outer Vlan tag
                ''',
                'outer_vlan_dei',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                 VLAN ID for outer tag use this when            
                only one tag should be matched
                ''',
                'outer_vlan_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-user-pri', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                VLAN User Priority for outer tag  use           
                this when only one tag should be matched
                ''',
                'outer_vlan_user_pri',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('parser-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts dropped by header parser as invalid
                ''',
                'parser_dropped',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pbb-bvid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Backbone Vlan id 
                ''',
                'pbb_bvid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pbb-dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 dei 
                ''',
                'pbb_dei',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pbb-pcp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 pcp 
                ''',
                'pbb_pcp',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pbb-sid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Service Instance id 
                ''',
                'pbb_sid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkt-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of packet. See ethMscCfyEPktType_e
                ''',
                'pkt_type',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Control pkts forwarded
                ''',
                'pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkts-data', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Data pkts forwarded
                ''',
                'pkts_data',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkts-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts dropped by classifier
                ''',
                'pkts_dropped',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkts-err-in', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts received with an error indication
                ''',
                'pkts_err_in',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('plain-bits', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Plain bits to compare. Max values:              
                untagged pkt - 40 bits after EthType            
                1 VLAN tag - 24 bits after parsed EthType       
                2 VLAN tags- 8 bits after  parsed EthType       
                1 MPLS tag - 32 bits after 1st tag              
                2 MPLS tags- 8 bits following after 2nd         
                or atmost 5th MPLS tag                          
                PBB - 16 bits after C-SA                        
                PBB with VLAN tag - 16 bits of VLAN tag 
                ''',
                'plain_bits',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('plain-bits-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No. of bits used in plainBits
                ''',
                'plain_bits_size',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('psci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                 SCI to be matched value required for           
                ingress only, pass NULL for egress
                ''',
                'psci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tag-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of MPLS or VLAN tags See ethMscCfyETagNum_e 
                ''',
                'tag_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'e' in TCI to match (1bit )
                ''',
                'tci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-c', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'c' in TCI to match (1bit) 
                ''',
                'tci_c',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-chk', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TCI bits will be checked only when this         
                bit is enabled. All the values of TCI bits      
                are mandatory when TCI check is used
                ''',
                'tci_chk',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-e-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'es' in TCI to match (1bit) 
                ''',
                'tci_e_xr',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-sc', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'sc' in TCI to match (1bit) 
                ''',
                'tci_sc',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-scb', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'scb' in TCI to match (1bit) 
                ''',
                'tci_scb',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-v', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'v' in TCI to match (1bit) 
                ''',
                'tci_v',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('vlan-dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 dei 
                ''',
                'vlan_dei',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                 vlan id 
                ''',
                'vlan_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('vlan-pcp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 pcp 
                ''',
                'vlan_pcp',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'tx-flow',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow.RxFlow' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow.RxFlow',
            False, 
            [
            _MetaInfoClassMember('drop', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Drop the packet
                ''',
                'drop',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('ethertype', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Parsed EtherType to match could be 0 if
                Ethertype should'nt                             
                be matched can be 0x88E5 for MACSec tag
                ''',
                'ethertype',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('flow-miss', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts matching none of flow entries
                ''',
                'flow_miss',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('flow-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Flow Number
                ''',
                'flow_no',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('force-ctrl', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Force the pkt as control pkt irrepective        
                of the results of control packet detector
                ''',
                'force_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-dei', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Dei to match for innner Vlan tag
                ''',
                'inner_vlan_dei',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN ID for inner tag used when two             
                VLAN Tags should be matched
                ''',
                'inner_vlan_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('inner-vlan-user-pri', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 VLAN User priority for inner tag use           
                when matching two VLAN tags
                ''',
                'inner_vlan_user_pri',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('is-flow-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Flow Enabled
                ''',
                'is_flow_enabled',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('macda', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '255')], [], 
                '''                MAC DA
                ''',
                'macda',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mask-da', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                DA mask
                ''',
                'mask_da',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mask-ethertype', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Parsed EtherType mask
                ''',
                'mask_ethertype',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mask-plain-bits', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Plain Bits mask
                ''',
                'mask_plain_bits',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('match-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                priority for match 0-15(highest) 
                ''',
                'match_priority',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls1-bos', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 botton of stack 
                ''',
                'mpls1_bos',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls1-exp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 exp 
                ''',
                'mpls1_exp',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls1-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 label 
                ''',
                'mpls1_label',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls2-bos', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 botton of stack 
                ''',
                'mpls2_bos',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls2-exp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 exp 
                ''',
                'mpls2_exp',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('mpls2-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 label 
                ''',
                'mpls2_label',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('multi-flow-match', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts matching multiple flow entries
                ''',
                'multi_flow_match',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-dei', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Dei to match for outer Vlan tag
                ''',
                'outer_vlan_dei',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                 VLAN ID for outer tag use this when            
                only one tag should be matched
                ''',
                'outer_vlan_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('outer-vlan-user-pri', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                VLAN User Priority for outer tag  use           
                this when only one tag should be matched
                ''',
                'outer_vlan_user_pri',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('parser-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts dropped by header parser as invalid
                ''',
                'parser_dropped',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pbb-bvid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Backbone Vlan id 
                ''',
                'pbb_bvid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pbb-dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 dei 
                ''',
                'pbb_dei',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pbb-pcp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 pcp 
                ''',
                'pbb_pcp',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pbb-sid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Service Instance id 
                ''',
                'pbb_sid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkt-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Type of packet. See ethMscCfyEPktType_e
                ''',
                'pkt_type',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Control pkts forwarded
                ''',
                'pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkts-data', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Data pkts forwarded
                ''',
                'pkts_data',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkts-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts dropped by classifier
                ''',
                'pkts_dropped',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('pkts-err-in', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Pkts received with an error indication
                ''',
                'pkts_err_in',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('plain-bits', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Plain bits to compare. Max values:              
                untagged pkt - 40 bits after EthType            
                1 VLAN tag - 24 bits after parsed EthType       
                2 VLAN tags- 8 bits after  parsed EthType       
                1 MPLS tag - 32 bits after 1st tag              
                2 MPLS tags- 8 bits following after 2nd         
                or atmost 5th MPLS tag                          
                PBB - 16 bits after C-SA                        
                PBB with VLAN tag - 16 bits of VLAN tag 
                ''',
                'plain_bits',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('plain-bits-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                No. of bits used in plainBits
                ''',
                'plain_bits_size',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('psci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                 SCI to be matched value required for           
                ingress only, pass NULL for egress
                ''',
                'psci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tag-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of MPLS or VLAN tags See ethMscCfyETagNum_e 
                ''',
                'tag_num',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'e' in TCI to match (1bit )
                ''',
                'tci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-c', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'c' in TCI to match (1bit) 
                ''',
                'tci_c',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-chk', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TCI bits will be checked only when this         
                bit is enabled. All the values of TCI bits      
                are mandatory when TCI check is used
                ''',
                'tci_chk',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-e-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'es' in TCI to match (1bit) 
                ''',
                'tci_e_xr',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-sc', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'sc' in TCI to match (1bit) 
                ''',
                'tci_sc',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-scb', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'scb' in TCI to match (1bit) 
                ''',
                'tci_scb',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tci-v', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                value of 'v' in TCI to match (1bit) 
                ''',
                'tci_v',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('vlan-dei', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 dei 
                ''',
                'vlan_dei',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                 vlan id 
                ''',
                'vlan_id',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('vlan-pcp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                 pcp 
                ''',
                'vlan_pcp',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'rx-flow',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow',
            False, 
            [
            _MetaInfoClassMember('rx-flow', REFERENCE_CLASS, 'RxFlow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow.RxFlow', 
                [], [], 
                '''                Rx Flow Details
                ''',
                'rx_flow',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tx-flow', REFERENCE_CLASS, 'TxFlow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow.TxFlow', 
                [], [], 
                '''                Tx Flow Details
                ''',
                'tx_flow',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'es200-flow',
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
            _MetaInfoClassMember('es200-flow', REFERENCE_CLASS, 'Es200Flow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow', 
                [], [], 
                '''                ES200 Flow Information
                ''',
                'es200_flow',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
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
    'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecTxStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecTxStats',
            False, 
            [
            _MetaInfoClassMember('current-an', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Current Tx AN
                ''',
                'current_an',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-encrypted-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Current Tx SA Encrypted Packets
                ''',
                'sa_encrypted_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-encrypted-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Octets Encrypted
                ''',
                'sc_encrypted_octets',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-encrypted-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx packets Encrypted
                ''',
                'sc_encrypted_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-overrun-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Overrun Packets
                ''',
                'sc_overrun_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-toolong-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Pkts Too Long
                ''',
                'sc_toolong_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-untagged-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx Untagged Packets
                ''',
                'sc_untagged_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'macsec-tx-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecRxStats.RxSaStat' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecRxStats.RxSaStat',
            False, 
            [
            _MetaInfoClassMember('an', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Current Rx AN
                ''',
                'an',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-invalid-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Invalid Pkts for current AN
                ''',
                'sa_invalid_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-not-using-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts not using SA for Current AN
                ''',
                'sa_not_using_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-not-valid-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Not Valid Pkts for Current AN
                ''',
                'sa_not_valid_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-ok-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Ok Pkts for Current AN
                ''',
                'sa_ok_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sa-unused-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Unused Pkts for Current AN
                ''',
                'sa_unused_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'rx-sa-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecRxStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecRxStats',
            False, 
            [
            _MetaInfoClassMember('rx-sa-stat', REFERENCE_LIST, 'RxSaStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecRxStats.RxSaStat', 
                [], [], 
                '''                Rx SA Level Stats
                ''',
                'rx_sa_stat',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-bad-tag-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Bad Tag Packets
                ''',
                'sc_bad_tag_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-decrypted-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Octets Decrypted
                ''',
                'sc_decrypted_octets',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-delayed-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Delayed Pkts
                ''',
                'sc_delayed_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-invalid-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Invalid
                ''',
                'sc_invalid_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-late-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Late Pkts
                ''',
                'sc_late_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-no-sci-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx No SCI Pkts
                ''',
                'sc_no_sci_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-no-tag-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx No Tag Packets
                ''',
                'sc_no_tag_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-not-using-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Not Using SA
                ''',
                'sc_not_using_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-not-valid-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Not Valid Pkts
                ''',
                'sc_not_valid_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-ok-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Ok
                ''',
                'sc_ok_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-overrun-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Overrun Pkts
                ''',
                'sc_overrun_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-unchecked-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Unchecked Pkts
                ''',
                'sc_unchecked_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-unknown-sci-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Unknown SCI Pkts
                ''',
                'sc_unknown_sci_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-untagged-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Untagged Packets
                ''',
                'sc_untagged_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('sc-unused-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx Pkts Unused SA
                ''',
                'sc_unused_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'macsec-rx-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats',
            False, 
            [
            _MetaInfoClassMember('macsec-rx-stats', REFERENCE_CLASS, 'MacsecRxStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecRxStats', 
                [], [], 
                '''                Rx SC and SA Level Stats
                ''',
                'macsec_rx_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('macsec-tx-stats', REFERENCE_CLASS, 'MacsecTxStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecTxStats', 
                [], [], 
                '''                Tx SC and SA Level Stats
                ''',
                'macsec_tx_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'xlfpga-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.TxSaStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.TxSaStats',
            False, 
            [
            _MetaInfoClassMember('out-octets-encrypted-protected1', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                octets1 encrypted/protected ?
                ''',
                'out_octets_encrypted_protected1',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-octets-encrypted-protected2', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                octets2 encrypted/protected ?
                ''',
                'out_octets_encrypted_protected2',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkts-encrypted-protected', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packets encrypted/protected
                ''',
                'out_pkts_encrypted_protected',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkts-sa-not-in-use', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packets coming on SA that is expired or
                otherwise not-in-use
                ''',
                'out_pkts_sa_not_in_use',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkts-too-long', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packets exceeding egress MTU
                ''',
                'out_pkts_too_long',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'tx-sa-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.RxSaStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.RxSaStats',
            False, 
            [
            _MetaInfoClassMember('in-octets-decrypted-validated1', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                octets1 decrypted/validated
                ''',
                'in_octets_decrypted_validated1',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-octets-decrypted-validated2', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                octets2 decrypted/validated
                ''',
                'in_octets_decrypted_validated2',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-octets-validated', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                octets validated
                ''',
                'in_octets_validated',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-delayed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PN of packet outside replay window &
                validateFrames !strict
                ''',
                'in_pkts_delayed',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packet not valid & validateFrames !strict
                ''',
                'in_pkts_invalid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-late', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                PN of packet outside replay window &
                validateFrames strict
                ''',
                'in_pkts_late',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-not-using-sa', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packet assigned to SA not in use &
                validateFrames strict
                ''',
                'in_pkts_not_using_sa',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-not-valid', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packet not valid & validateFrames strict
                ''',
                'in_pkts_not_valid',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packets with no error
                ''',
                'in_pkts_ok',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-sa-not-in-use', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packets coming on SA that is
                ''',
                'in_pkts_sa_not_in_use',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-unchecked', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                frame not valid & validateFrames disabled
                ''',
                'in_pkts_unchecked',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-unused-sa', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packet assigned to SA not in use &
                validateFrames !strict
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
    'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.TxInterfaceMacsecStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.TxInterfaceMacsecStats',
            False, 
            [
            _MetaInfoClassMember('out-bcast-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Broadcast pkts tx on controlled port
                ''',
                'out_bcast_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-bcast-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Broadcast pkts tx on uncontrolled port
                ''',
                'out_bcast_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-drop-pkts-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets dropped due to overflow in
                classification pipeline
                ''',
                'out_drop_pkts_class',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-drop-pkts-data', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets dropped due to overflow in  processing
                pipeline
                ''',
                'out_drop_pkts_data',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-mcast-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Multicast pkts tx on controlled port
                ''',
                'out_mcast_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-mcast-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Multicast pkts tx on uncontrolled port
                ''',
                'out_mcast_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-octets-common', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Octets tx on common port
                ''',
                'out_octets_common',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-octets-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Octets tx on controlled port
                ''',
                'out_octets_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-octets-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Octets tx on uncontrolled port
                ''',
                'out_octets_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkt-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                egress packet that is classified as control
                packet
                ''',
                'out_pkt_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-pkts-untagged', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                egress packet to go out untagged when
                protectFrames not set
                ''',
                'out_pkts_untagged',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-rx-drop-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Data pkts dropped due to overrun
                ''',
                'out_rx_drop_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-rx-drop-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Control pkts dropped due to overrun
                ''',
                'out_rx_drop_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-rx-err-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Data pkts error-terminated due to overrun
                ''',
                'out_rx_err_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-rx-err-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Control pkts error-terminated due to overrun
                ''',
                'out_rx_err_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-ucast-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unicast pkts tx on controlled port
                ''',
                'out_ucast_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('out-ucast-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unicast pkts tx on uncontrolled port
                ''',
                'out_ucast_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('transform-error-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                counter to count internal errors in the MACSec
                core
                ''',
                'transform_error_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'tx-interface-macsec-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.RxInterfaceMacsecStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.RxInterfaceMacsecStats',
            False, 
            [
            _MetaInfoClassMember('in-bcast-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Broadcast pkts rx on controlled port
                ''',
                'in_bcast_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-bcast-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Broadcast pkts rx on uncontrolled port
                ''',
                'in_bcast_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-drop-pkts-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets dropped due to overflow in
                classification pipeline
                ''',
                'in_drop_pkts_class',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-drop-pkts-data', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Packets dropped due to overflow in processing
                pipeline
                ''',
                'in_drop_pkts_data',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-mcast-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Multicast pkts rx on controlled port
                ''',
                'in_mcast_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-mcast-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Multicast pkts rx on uncontrolled port
                ''',
                'in_mcast_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-octets-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Octets rx on controlled port
                ''',
                'in_octets_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-octets-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Octets rx on uncontrolled port
                ''',
                'in_octets_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-bad-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ingress frames received with an invalid MACSec
                tag or ICV                                      
                added with next one gives InPktsSCIMiss
                ''',
                'in_pkt_bad_tag',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ingress packet that is classified as control
                packet
                ''',
                'in_pkt_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-no-sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                correctly tagged ingress frames for which no
                valid SC found & \;                             
                validateFrames is strict
                ''',
                'in_pkt_no_sci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkt-no-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ingress packet untagged & validateFrames is
                strict
                ''',
                'in_pkt_no_tag',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-tagged-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ingress packets that are control or KaY packets
                ''',
                'in_pkts_tagged_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-unknown-sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                correctly tagged ingress frames for which no
                valid SC found &                                
                validateFrames is !strict
                ''',
                'in_pkts_unknown_sci',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-pkts-untagged', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ingress packet untagged & validateFrames is 
                !strict
                ''',
                'in_pkts_untagged',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-rx-drop-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Data pkts dropped due to overrun
                ''',
                'in_rx_drop_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-rx-drop-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Control pkts dropped due to overrun
                ''',
                'in_rx_drop_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-rx-error-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Data pkts error-terminated due to overrun
                ''',
                'in_rx_error_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-rx-error-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Control pkts error-terminated due to overrun
                ''',
                'in_rx_error_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-ucast-pkts-ctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unicast pkts rx on controlled port
                ''',
                'in_ucast_pkts_ctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('in-ucast-pkts-unctrl', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Unicast pkts rx on uncontrolled port
                ''',
                'in_ucast_pkts_unctrl',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('transform-error-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                counter to count internal errors in the MACSec
                core
                ''',
                'transform_error_pkts',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'rx-interface-macsec-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats',
            False, 
            [
            _MetaInfoClassMember('rx-interface-macsec-stats', REFERENCE_CLASS, 'RxInterfaceMacsecStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.RxInterfaceMacsecStats', 
                [], [], 
                '''                Rx interface Macsec Stats
                ''',
                'rx_interface_macsec_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('rx-sa-stats', REFERENCE_CLASS, 'RxSaStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.RxSaStats', 
                [], [], 
                '''                Rx SA Stats
                ''',
                'rx_sa_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tx-interface-macsec-stats', REFERENCE_CLASS, 'TxInterfaceMacsecStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.TxInterfaceMacsecStats', 
                [], [], 
                '''                Tx interface Macsec Stats
                ''',
                'tx_interface_macsec_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            _MetaInfoClassMember('tx-sa-stats', REFERENCE_CLASS, 'TxSaStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.TxSaStats', 
                [], [], 
                '''                Tx SA Stats
                ''',
                'tx_sa_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-pl-oper',
            'es200-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-pl-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper'
        ),
    },
    'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics' : {
        'meta_info' : _MetaInfoClass('Macsec.Nodes.Node.Interfaces.Interface.SwStatistics',
            False, 
            [
            _MetaInfoClassMember('es200-stats', REFERENCE_CLASS, 'Es200Stats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats', 
                [], [], 
                '''                ES200 Stats
                ''',
                'es200_stats',
                'Cisco-IOS-XR-crypto-macsec-pl-oper', False),
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
            _MetaInfoClassMember('xlfpga-stats', REFERENCE_CLASS, 'XlfpgaStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_pl_oper', 'Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats', 
                [], [], 
                '''                XLFPGA Stats
                ''',
                'xlfpga_stats',
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
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecRxStats.RxSaStat']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecRxStats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecTxStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats.MacsecRxStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.TxSaStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.RxSaStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.TxInterfaceMacsecStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats.RxInterfaceMacsecStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.MsfpgaStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.XlfpgaStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics.Es200Stats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwStatistics']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa.TxSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa.RxSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa.TxSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa.RxSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.TxSa.XformParams']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.TxSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.RxSa.XformParams']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.RxSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.TxSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa.RxSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.MsfpgaSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.XlfpgaSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa.Es200Sa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas.SwSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwSas']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa.TxSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa.RxSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa.TxSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa.RxSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.TxSa.XformParams']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.TxSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.RxSa.XformParams']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.RxSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.TxSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa.RxSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.MsfpgaSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.XlfpgaSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa.Es200Sa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas.HwSa']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwSas']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow.TxFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow.RxFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow.TxFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow.RxFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.MsfpgaFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow.Es200Flow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS.HwFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.HwFlowS']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow.TxFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow.RxFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow.TxFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow.RxFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.MsfpgaFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow.Es200Flow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS.SwFlow']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwFlowS']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.TxSaStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.RxSaStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.TxInterfaceMacsecStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats.RxInterfaceMacsecStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecRxStats.RxSaStat']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecRxStats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecTxStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats.MacsecRxStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.TxSaStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.RxSaStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.TxInterfaceMacsecStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats.RxInterfaceMacsecStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.MsfpgaStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.XlfpgaStats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics']['meta_info']
_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics.Es200Stats']['meta_info'].parent =_meta_table['Macsec.Nodes.Node.Interfaces.Interface.SwStatistics']['meta_info']
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
