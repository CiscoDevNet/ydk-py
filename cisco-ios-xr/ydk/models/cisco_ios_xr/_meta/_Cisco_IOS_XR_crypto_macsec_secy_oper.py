


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Macsec.Secy.Interfaces.Interface.Stats.IntfStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Secy.Interfaces.Interface.Stats.IntfStats',
            False, 
            [
            _MetaInfoClassMember('in-octets-decrypted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InOctetsDecrypted
                ''',
                'in_octets_decrypted',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('in-octets-validated', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InOctetsValidated
                ''',
                'in_octets_validated',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('in-pkts-bad-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InPktsBadTag
                ''',
                'in_pkts_bad_tag',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('in-pkts-no-sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InPktsNoSCI
                ''',
                'in_pkts_no_sci',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('in-pkts-no-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InPktsNoTag
                ''',
                'in_pkts_no_tag',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('in-pkts-overrun', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InPktsOverrun
                ''',
                'in_pkts_overrun',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('in-pkts-unknown-sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InPktsUnknownSCI
                ''',
                'in_pkts_unknown_sci',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('in-pkts-untagged', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InPktsUntagged
                ''',
                'in_pkts_untagged',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('out-octets-encrypted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                OutOctetsEncrypted
                ''',
                'out_octets_encrypted',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('out-octets-protected', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                OutOctetsProtected
                ''',
                'out_octets_protected',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('out-pkts-too-long', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                OutPktsTooLong
                ''',
                'out_pkts_too_long',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('out-pkts-untagged', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                OutPktsUntagged
                ''',
                'out_pkts_untagged',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-secy-oper',
            'intf-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-secy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper'
        ),
    },
    'Macsec.Secy.Interfaces.Interface.Stats.TxScStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Secy.Interfaces.Interface.Stats.TxScStats',
            False, 
            [
            _MetaInfoClassMember('out-octets-encrypted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                OutOctetsEncrypted
                ''',
                'out_octets_encrypted',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('out-octets-protected', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                OutOctetsProtected
                ''',
                'out_octets_protected',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('out-pkts-encrypted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                OutPktsEncrypted
                ''',
                'out_pkts_encrypted',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('out-pkts-protected', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                OutPktsProtected
                ''',
                'out_pkts_protected',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('out-pkts-too-long', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                OutPktsTooLong
                ''',
                'out_pkts_too_long',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('tx-sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Tx SCI
                ''',
                'tx_sci',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-secy-oper',
            'tx-sc-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-secy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper'
        ),
    },
    'Macsec.Secy.Interfaces.Interface.Stats.RxScStats' : {
        'meta_info' : _MetaInfoClass('Macsec.Secy.Interfaces.Interface.Stats.RxScStats',
            False, 
            [
            _MetaInfoClassMember('in-octets-decrypted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InOctetsDecrypted
                ''',
                'in_octets_decrypted',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('in-octets-validated', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InOctetsValidated
                ''',
                'in_octets_validated',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('in-pkts-delayed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InPktsDelayed
                ''',
                'in_pkts_delayed',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('in-pkts-invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InPktsInvalid
                ''',
                'in_pkts_invalid',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('in-pkts-late', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InPktsLate
                ''',
                'in_pkts_late',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('in-pkts-not-using-sa', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InPktsNotUsingSA
                ''',
                'in_pkts_not_using_sa',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('in-pkts-not-valid', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InPktsNotValid
                ''',
                'in_pkts_not_valid',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('in-pkts-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InPktsOK
                ''',
                'in_pkts_ok',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('in-pkts-unchecked', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InPktsUnchecked
                ''',
                'in_pkts_unchecked',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('in-pkts-untagged-hit', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InPktsUntaggedHit
                ''',
                'in_pkts_untagged_hit',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('in-pkts-unused-sa', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                InPktsUnusedSA
                ''',
                'in_pkts_unused_sa',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('rx-sci', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Rx SCI
                ''',
                'rx_sci',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-secy-oper',
            'rx-sc-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-secy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper'
        ),
    },
    'Macsec.Secy.Interfaces.Interface.Stats' : {
        'meta_info' : _MetaInfoClass('Macsec.Secy.Interfaces.Interface.Stats',
            False, 
            [
            _MetaInfoClassMember('intf-stats', REFERENCE_CLASS, 'IntfStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper', 'Macsec.Secy.Interfaces.Interface.Stats.IntfStats', 
                [], [], 
                '''                Interface stats
                ''',
                'intf_stats',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('rx-sc-stats', REFERENCE_LIST, 'RxScStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper', 'Macsec.Secy.Interfaces.Interface.Stats.RxScStats', 
                [], [], 
                '''                RX SC Stats List
                ''',
                'rx_sc_stats',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            _MetaInfoClassMember('tx-sc-stats', REFERENCE_CLASS, 'TxScStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper', 'Macsec.Secy.Interfaces.Interface.Stats.TxScStats', 
                [], [], 
                '''                Tx SC Stats
                ''',
                'tx_sc_stats',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-secy-oper',
            'stats',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-secy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper'
        ),
    },
    'Macsec.Secy.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Macsec.Secy.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'name',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', True),
            _MetaInfoClassMember('stats', REFERENCE_CLASS, 'Stats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper', 'Macsec.Secy.Interfaces.Interface.Stats', 
                [], [], 
                '''                MACsec Stats
                ''',
                'stats',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-secy-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-secy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper'
        ),
    },
    'Macsec.Secy.Interfaces' : {
        'meta_info' : _MetaInfoClass('Macsec.Secy.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper', 'Macsec.Secy.Interfaces.Interface', 
                [], [], 
                '''                MAC Security Data for the Interface
                ''',
                'interface',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-secy-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-secy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper'
        ),
    },
    'Macsec.Secy' : {
        'meta_info' : _MetaInfoClass('Macsec.Secy',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper', 'Macsec.Secy.Interfaces', 
                [], [], 
                '''                MAC Security Data
                ''',
                'interfaces',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-secy-oper',
            'secy',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-secy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper'
        ),
    },
    'Macsec' : {
        'meta_info' : _MetaInfoClass('Macsec',
            False, 
            [
            _MetaInfoClassMember('secy', REFERENCE_CLASS, 'Secy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper', 'Macsec.Secy', 
                [], [], 
                '''                MAC Security Entity
                ''',
                'secy',
                'Cisco-IOS-XR-crypto-macsec-secy-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-secy-oper',
            'macsec',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-secy-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_secy_oper'
        ),
    },
}
_meta_table['Macsec.Secy.Interfaces.Interface.Stats.IntfStats']['meta_info'].parent =_meta_table['Macsec.Secy.Interfaces.Interface.Stats']['meta_info']
_meta_table['Macsec.Secy.Interfaces.Interface.Stats.TxScStats']['meta_info'].parent =_meta_table['Macsec.Secy.Interfaces.Interface.Stats']['meta_info']
_meta_table['Macsec.Secy.Interfaces.Interface.Stats.RxScStats']['meta_info'].parent =_meta_table['Macsec.Secy.Interfaces.Interface.Stats']['meta_info']
_meta_table['Macsec.Secy.Interfaces.Interface.Stats']['meta_info'].parent =_meta_table['Macsec.Secy.Interfaces.Interface']['meta_info']
_meta_table['Macsec.Secy.Interfaces.Interface']['meta_info'].parent =_meta_table['Macsec.Secy.Interfaces']['meta_info']
_meta_table['Macsec.Secy.Interfaces']['meta_info'].parent =_meta_table['Macsec.Secy']['meta_info']
_meta_table['Macsec.Secy']['meta_info'].parent =_meta_table['Macsec']['meta_info']
