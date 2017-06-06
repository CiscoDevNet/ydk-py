


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ncs1KCipherSuitEnum' : _MetaInfoEnum('Ncs1KCipherSuitEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper',
        {
            'gcm-aes-256':'gcm_aes_256',
            'gcm-aes-128':'gcm_aes_128',
            'gcm-aes-xpn-256':'gcm_aes_xpn_256',
        }, 'Cisco-IOS-XR-ncs1k-macsec-ea-oper', _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-macsec-ea-oper']),
    'Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus.ActiveAssociation' : {
        'meta_info' : _MetaInfoClass('Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus.ActiveAssociation',
            False, 
            [
            _MetaInfoClassMember('association-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Assocition Number
                ''',
                'association_number',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('device-association-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Devive Association Number
                ''',
                'device_association_number',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('key-crc', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                32bit CRC of Programmed Key
                ''',
                'key_crc',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('programmed-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                Key Programmed Time
                ''',
                'programmed_time',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('short-secure-channel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Short Secure Channel Id
                ''',
                'short_secure_channel_id',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('xpn-salt', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                XPN Salt
                ''',
                'xpn_salt',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-macsec-ea-oper',
            'active-association',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-macsec-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper'
        ),
    },
    'Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus' : {
        'meta_info' : _MetaInfoClass('Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus',
            False, 
            [
            _MetaInfoClassMember('active-association', REFERENCE_LIST, 'ActiveAssociation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper', 'Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus.ActiveAssociation', 
                [], [], 
                '''                Active Associations
                ''',
                'active_association',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('cipher-suite', REFERENCE_ENUM_CLASS, 'Ncs1KCipherSuitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper', 'Ncs1KCipherSuitEnum', 
                [], [], 
                '''                Cipher Suite
                ''',
                'cipher_suite',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('confidentiality-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Confidentiality offset
                ''',
                'confidentiality_offset',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('initial-packet-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Initial Packet Number
                ''',
                'initial_packet_number',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('max-packet-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Maximum Packet Number
                ''',
                'max_packet_number',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('protection-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Protection Enabled
                ''',
                'protection_enabled',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('recent-packet-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Recent Packet Number
                ''',
                'recent_packet_number',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('secure-channel-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                Secure Channel Id
                ''',
                'secure_channel_id',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('secure-tag-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Secure Tag Length
                ''',
                'secure_tag_length',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-macsec-ea-oper',
            'encrypt-sc-status',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-macsec-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper'
        ),
    },
    'Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus.ActiveAssociation' : {
        'meta_info' : _MetaInfoClass('Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus.ActiveAssociation',
            False, 
            [
            _MetaInfoClassMember('association-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Assocition Number
                ''',
                'association_number',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('device-association-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Devive Association Number
                ''',
                'device_association_number',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('key-crc', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                32bit CRC of Programmed Key
                ''',
                'key_crc',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('programmed-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 30)], [], 
                '''                Key Programmed Time
                ''',
                'programmed_time',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('short-secure-channel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Short Secure Channel Id
                ''',
                'short_secure_channel_id',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('xpn-salt', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                XPN Salt
                ''',
                'xpn_salt',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-macsec-ea-oper',
            'active-association',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-macsec-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper'
        ),
    },
    'Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus' : {
        'meta_info' : _MetaInfoClass('Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus',
            False, 
            [
            _MetaInfoClassMember('active-association', REFERENCE_LIST, 'ActiveAssociation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper', 'Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus.ActiveAssociation', 
                [], [], 
                '''                Active Associations
                ''',
                'active_association',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('cipher-suite', REFERENCE_ENUM_CLASS, 'Ncs1KCipherSuitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper', 'Ncs1KCipherSuitEnum', 
                [], [], 
                '''                Cipher Suite
                ''',
                'cipher_suite',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('confidentiality-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Confidentiality offset
                ''',
                'confidentiality_offset',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('initial-packet-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Initial Packet Number
                ''',
                'initial_packet_number',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('max-packet-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Maximum Packet Number
                ''',
                'max_packet_number',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('protection-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Protection Enabled
                ''',
                'protection_enabled',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('recent-packet-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Recent Packet Number
                ''',
                'recent_packet_number',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('secure-channel-id', ATTRIBUTE, 'str' , None, None, 
                [(0, 20)], [], 
                '''                Secure Channel Id
                ''',
                'secure_channel_id',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('secure-tag-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Secure Tag Length
                ''',
                'secure_tag_length',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-macsec-ea-oper',
            'decrypt-sc-status',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-macsec-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper'
        ),
    },
    'Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo' : {
        'meta_info' : _MetaInfoClass('Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo',
            False, 
            [
            _MetaInfoClassMember('decrypt-sc-status', REFERENCE_CLASS, 'DecryptScStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper', 'Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus', 
                [], [], 
                '''                Decrypt Secure Channel Status
                ''',
                'decrypt_sc_status',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('encrypt-sc-status', REFERENCE_CLASS, 'EncryptScStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper', 'Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus', 
                [], [], 
                '''                Encrypt Secure Channel Status
                ''',
                'encrypt_sc_status',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('must-secure', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Must Secure
                ''',
                'must_secure',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('replay-window-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Replay Window Size
                ''',
                'replay_window_size',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            _MetaInfoClassMember('secure-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Secure Mode
                ''',
                'secure_mode',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-macsec-ea-oper',
            'ncs1k-status-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-macsec-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper'
        ),
    },
    'Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName' : {
        'meta_info' : _MetaInfoClass('Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Port name
                ''',
                'name',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', True),
            _MetaInfoClassMember('ncs1k-status-info', REFERENCE_CLASS, 'Ncs1KStatusInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper', 'Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo', 
                [], [], 
                '''                controller data
                ''',
                'ncs1k_status_info',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-macsec-ea-oper',
            'ncs1k-macsec-ctrlr-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-macsec-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper'
        ),
    },
    'Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames' : {
        'meta_info' : _MetaInfoClass('Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames',
            False, 
            [
            _MetaInfoClassMember('ncs1k-macsec-ctrlr-name', REFERENCE_LIST, 'Ncs1KMacsecCtrlrName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper', 'Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName', 
                [], [], 
                '''                Interface name
                ''',
                'ncs1k_macsec_ctrlr_name',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-macsec-ea-oper',
            'ncs1k-macsec-ctrlr-names',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-macsec-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper'
        ),
    },
    'Ncs1KMacsecOper' : {
        'meta_info' : _MetaInfoClass('Ncs1KMacsecOper',
            False, 
            [
            _MetaInfoClassMember('ncs1k-macsec-ctrlr-names', REFERENCE_CLASS, 'Ncs1KMacsecCtrlrNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper', 'Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames', 
                [], [], 
                '''                All Macsec operational data
                ''',
                'ncs1k_macsec_ctrlr_names',
                'Cisco-IOS-XR-ncs1k-macsec-ea-oper', False),
            ],
            'Cisco-IOS-XR-ncs1k-macsec-ea-oper',
            'ncs1k-macsec-oper',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs1k-macsec-ea-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs1k_macsec_ea_oper'
        ),
    },
}
_meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus.ActiveAssociation']['meta_info'].parent =_meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus']['meta_info']
_meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus.ActiveAssociation']['meta_info'].parent =_meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus']['meta_info']
_meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.EncryptScStatus']['meta_info'].parent =_meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo']['meta_info']
_meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo.DecryptScStatus']['meta_info'].parent =_meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo']['meta_info']
_meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName.Ncs1KStatusInfo']['meta_info'].parent =_meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName']['meta_info']
_meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames.Ncs1KMacsecCtrlrName']['meta_info'].parent =_meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames']['meta_info']
_meta_table['Ncs1KMacsecOper.Ncs1KMacsecCtrlrNames']['meta_info'].parent =_meta_table['Ncs1KMacsecOper']['meta_info']
