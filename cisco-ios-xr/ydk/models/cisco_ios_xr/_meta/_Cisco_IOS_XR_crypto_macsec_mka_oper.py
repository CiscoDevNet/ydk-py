


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Macsec.Mka.Interfaces.Interface.Session.SessionSummary.OuterTag' : {
        'meta_info' : _MetaInfoClass('Macsec.Mka.Interfaces.Interface.Session.SessionSummary.OuterTag',
            False, 
            [
            _MetaInfoClassMember('cfi', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                cfi
                ''',
                'cfi',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('etype', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                etype
                ''',
                'etype',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                priority
                ''',
                'priority',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                vlan id
                ''',
                'vlan_id',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-mka-oper',
            'outer-tag',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper'
        ),
    },
    'Macsec.Mka.Interfaces.Interface.Session.SessionSummary.InnerTag' : {
        'meta_info' : _MetaInfoClass('Macsec.Mka.Interfaces.Interface.Session.SessionSummary.InnerTag',
            False, 
            [
            _MetaInfoClassMember('cfi', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                cfi
                ''',
                'cfi',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('etype', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                etype
                ''',
                'etype',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                priority
                ''',
                'priority',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                vlan id
                ''',
                'vlan_id',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-mka-oper',
            'inner-tag',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper'
        ),
    },
    'Macsec.Mka.Interfaces.Interface.Session.SessionSummary' : {
        'meta_info' : _MetaInfoClass('Macsec.Mka.Interfaces.Interface.Session.SessionSummary',
            False, 
            [
            _MetaInfoClassMember('algo-agility', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Alogorithm Agility
                ''',
                'algo_agility',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('capability', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MACSec Capability
                ''',
                'capability',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('cipher-str', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Cipher String
                ''',
                'cipher_str',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('confidentiality-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Confidentiality Offset
                ''',
                'confidentiality_offset',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('delay-protection', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Delay Protect
                ''',
                'delay_protection',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('include-icv-indicator', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                IncludeICVIndicator
                ''',
                'include_icv_indicator',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('inherited-policy', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Inherited Policy
                ''',
                'inherited_policy',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('inner-tag', REFERENCE_CLASS, 'InnerTag' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper', 'Macsec.Mka.Interfaces.Interface.Session.SessionSummary.InnerTag', 
                [], [], 
                '''                VLAN Inner TAG
                ''',
                'inner_tag',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                macsec configured interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('mac-sec-desired', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MACSec Desired
                ''',
                'mac_sec_desired',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('my-mac', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                My MAC
                ''',
                'my_mac',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('outer-tag', REFERENCE_CLASS, 'OuterTag' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper', 'Macsec.Mka.Interfaces.Interface.Session.SessionSummary.OuterTag', 
                [], [], 
                '''                VLAN Outer TAG
                ''',
                'outer_tag',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Policy Name
                ''',
                'policy',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Key Server Priority
                ''',
                'priority',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('replay-protect', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Replay Protect
                ''',
                'replay_protect',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('window-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Replay Window Size
                ''',
                'window_size',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-mka-oper',
            'session-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper'
        ),
    },
    'Macsec.Mka.Interfaces.Interface.Session.Vp' : {
        'meta_info' : _MetaInfoClass('Macsec.Mka.Interfaces.Interface.Session.Vp',
            False, 
            [
            _MetaInfoClassMember('cipher-suite', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SAK Cipher Suite
                ''',
                'cipher_suite',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('latest-an', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Latest SAK AN
                ''',
                'latest_an',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('latest-ki', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Latest SAK KI
                ''',
                'latest_ki',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('latest-kn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Latest SAK KN
                ''',
                'latest_kn',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('latest-rx', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Latest Rx status
                ''',
                'latest_rx',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('latest-tx', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Latest Tx status
                ''',
                'latest_tx',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('my-sci', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Local SCI(MAC)
                ''',
                'my_sci',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('old-an', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Old SAK AN
                ''',
                'old_an',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('old-ki', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Old SAK KI
                ''',
                'old_ki',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('old-kn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Old SAK KN
                ''',
                'old_kn',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('old-rx', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Old Rx status
                ''',
                'old_rx',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('old-tx', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Old Tx status
                ''',
                'old_tx',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('retire-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SAK Retire time
                ''',
                'retire_time',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('ssci', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SSCI of the Local TxSC
                ''',
                'ssci',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('time-to-sak-rekey', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Next SAK Rekey time in Sec
                ''',
                'time_to_sak_rekey',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('virtual-port-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Virtual Port ID
                ''',
                'virtual_port_id',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('wait-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SAK Transmit Wait Time
                ''',
                'wait_time',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-mka-oper',
            'vp',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper'
        ),
    },
    'Macsec.Mka.Interfaces.Interface.Session.Ca.LivePeer' : {
        'meta_info' : _MetaInfoClass('Macsec.Mka.Interfaces.Interface.Session.Ca.LivePeer',
            False, 
            [
            _MetaInfoClassMember('mi', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Member ID
                ''',
                'mi',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('mn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message Number
                ''',
                'mn',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                KS Priority
                ''',
                'priority',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('sci', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Rx SCI
                ''',
                'sci',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('ssci', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peer SSCI
                ''',
                'ssci',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-mka-oper',
            'live-peer',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper'
        ),
    },
    'Macsec.Mka.Interfaces.Interface.Session.Ca.PotentialPeer' : {
        'meta_info' : _MetaInfoClass('Macsec.Mka.Interfaces.Interface.Session.Ca.PotentialPeer',
            False, 
            [
            _MetaInfoClassMember('mi', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Member ID
                ''',
                'mi',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('mn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message Number
                ''',
                'mn',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                KS Priority
                ''',
                'priority',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('sci', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Rx SCI
                ''',
                'sci',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('ssci', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peer SSCI
                ''',
                'ssci',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-mka-oper',
            'potential-peer',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper'
        ),
    },
    'Macsec.Mka.Interfaces.Interface.Session.Ca.DormantPeer' : {
        'meta_info' : _MetaInfoClass('Macsec.Mka.Interfaces.Interface.Session.Ca.DormantPeer',
            False, 
            [
            _MetaInfoClassMember('mi', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Member ID
                ''',
                'mi',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('mn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message Number
                ''',
                'mn',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                KS Priority
                ''',
                'priority',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('sci', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Rx SCI
                ''',
                'sci',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('ssci', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Peer SSCI
                ''',
                'ssci',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-mka-oper',
            'dormant-peer',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper'
        ),
    },
    'Macsec.Mka.Interfaces.Interface.Session.Ca' : {
        'meta_info' : _MetaInfoClass('Macsec.Mka.Interfaces.Interface.Session.Ca',
            False, 
            [
            _MetaInfoClassMember('authentication-mode', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                CA Authentication Mode
                :PRIMARY-PSK/FALLBACK-PSK/EAP
                ''',
                'authentication_mode',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('authenticator', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                authenticator
                ''',
                'authenticator',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('ckn', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                CKN
                ''',
                'ckn',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('dormant-peer', REFERENCE_LIST, 'DormantPeer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper', 'Macsec.Mka.Interfaces.Interface.Session.Ca.DormantPeer', 
                [], [], 
                '''                Dormant Peer List
                ''',
                'dormant_peer',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('first-ca', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is First CA
                ''',
                'first_ca',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('is-key-server', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Key Server
                ''',
                'is_key_server',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('key-chain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Key Chain name
                ''',
                'key_chain',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('live-peer', REFERENCE_LIST, 'LivePeer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper', 'Macsec.Mka.Interfaces.Interface.Session.Ca.LivePeer', 
                [], [], 
                '''                Live Peer List
                ''',
                'live_peer',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('my-mi', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Member Identifier
                ''',
                'my_mi',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('my-mn', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Message Number
                ''',
                'my_mn',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('num-live-peers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Live Peers
                ''',
                'num_live_peers',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('num-live-peers-responded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Live Peers responded
                ''',
                'num_live_peers_responded',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('peer-sci', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Peer SCI(MAC)
                ''',
                'peer_sci',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('potential-peer', REFERENCE_LIST, 'PotentialPeer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper', 'Macsec.Mka.Interfaces.Interface.Session.Ca.PotentialPeer', 
                [], [], 
                '''                Potential Peer List
                ''',
                'potential_peer',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session Status [Secured/Not Secured]
                ''',
                'status',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('status-description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Status Description
                ''',
                'status_description',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-mka-oper',
            'ca',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper'
        ),
    },
    'Macsec.Mka.Interfaces.Interface.Session' : {
        'meta_info' : _MetaInfoClass('Macsec.Mka.Interfaces.Interface.Session',
            False, 
            [
            _MetaInfoClassMember('ca', REFERENCE_LIST, 'Ca' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper', 'Macsec.Mka.Interfaces.Interface.Session.Ca', 
                [], [], 
                '''                CA List for a Session
                ''',
                'ca',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('session-summary', REFERENCE_CLASS, 'SessionSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper', 'Macsec.Mka.Interfaces.Interface.Session.SessionSummary', 
                [], [], 
                '''                Session summary
                ''',
                'session_summary',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            _MetaInfoClassMember('vp', REFERENCE_CLASS, 'Vp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper', 'Macsec.Mka.Interfaces.Interface.Session.Vp', 
                [], [], 
                '''                Virtual Pointer Info
                ''',
                'vp',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-mka-oper',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper'
        ),
    },
    'Macsec.Mka.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Macsec.Mka.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'name',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', True),
            _MetaInfoClassMember('session', REFERENCE_CLASS, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper', 'Macsec.Mka.Interfaces.Interface.Session', 
                [], [], 
                '''                MKA Session Data
                ''',
                'session',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-mka-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper'
        ),
    },
    'Macsec.Mka.Interfaces' : {
        'meta_info' : _MetaInfoClass('Macsec.Mka.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper', 'Macsec.Mka.Interfaces.Interface', 
                [], [], 
                '''                MKA Data for the Interface
                ''',
                'interface',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-mka-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper'
        ),
    },
    'Macsec.Mka' : {
        'meta_info' : _MetaInfoClass('Macsec.Mka',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper', 'Macsec.Mka.Interfaces', 
                [], [], 
                '''                MKA Data
                ''',
                'interfaces',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-mka-oper',
            'mka',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper'
        ),
    },
    'Macsec' : {
        'meta_info' : _MetaInfoClass('Macsec',
            False, 
            [
            _MetaInfoClassMember('mka', REFERENCE_CLASS, 'Mka' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper', 'Macsec.Mka', 
                [], [], 
                '''                MKA Data
                ''',
                'mka',
                'Cisco-IOS-XR-crypto-macsec-mka-oper', False),
            ],
            'Cisco-IOS-XR-crypto-macsec-mka-oper',
            'macsec',
            _yang_ns._namespaces['Cisco-IOS-XR-crypto-macsec-mka-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_crypto_macsec_mka_oper'
        ),
    },
}
_meta_table['Macsec.Mka.Interfaces.Interface.Session.SessionSummary.OuterTag']['meta_info'].parent =_meta_table['Macsec.Mka.Interfaces.Interface.Session.SessionSummary']['meta_info']
_meta_table['Macsec.Mka.Interfaces.Interface.Session.SessionSummary.InnerTag']['meta_info'].parent =_meta_table['Macsec.Mka.Interfaces.Interface.Session.SessionSummary']['meta_info']
_meta_table['Macsec.Mka.Interfaces.Interface.Session.Ca.LivePeer']['meta_info'].parent =_meta_table['Macsec.Mka.Interfaces.Interface.Session.Ca']['meta_info']
_meta_table['Macsec.Mka.Interfaces.Interface.Session.Ca.PotentialPeer']['meta_info'].parent =_meta_table['Macsec.Mka.Interfaces.Interface.Session.Ca']['meta_info']
_meta_table['Macsec.Mka.Interfaces.Interface.Session.Ca.DormantPeer']['meta_info'].parent =_meta_table['Macsec.Mka.Interfaces.Interface.Session.Ca']['meta_info']
_meta_table['Macsec.Mka.Interfaces.Interface.Session.SessionSummary']['meta_info'].parent =_meta_table['Macsec.Mka.Interfaces.Interface.Session']['meta_info']
_meta_table['Macsec.Mka.Interfaces.Interface.Session.Vp']['meta_info'].parent =_meta_table['Macsec.Mka.Interfaces.Interface.Session']['meta_info']
_meta_table['Macsec.Mka.Interfaces.Interface.Session.Ca']['meta_info'].parent =_meta_table['Macsec.Mka.Interfaces.Interface.Session']['meta_info']
_meta_table['Macsec.Mka.Interfaces.Interface.Session']['meta_info'].parent =_meta_table['Macsec.Mka.Interfaces.Interface']['meta_info']
_meta_table['Macsec.Mka.Interfaces.Interface']['meta_info'].parent =_meta_table['Macsec.Mka.Interfaces']['meta_info']
_meta_table['Macsec.Mka.Interfaces']['meta_info'].parent =_meta_table['Macsec.Mka']['meta_info']
_meta_table['Macsec.Mka']['meta_info'].parent =_meta_table['Macsec']['meta_info']
