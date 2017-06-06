


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MacsecCtrlrCiphersuitEnum' : _MetaInfoEnum('MacsecCtrlrCiphersuitEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper',
        {
            'gcm-aes-256':'gcm_aes_256',
            'gcm-aes-128':'gcm_aes_128',
            'gcm-aes-xpn-256':'gcm_aes_xpn_256',
        }, 'Cisco-IOS-XR-macsec-ctrlr-oper', _yang_ns._namespaces['Cisco-IOS-XR-macsec-ctrlr-oper']),
    'MacsecCtrlrStateEnum' : _MetaInfoEnum('MacsecCtrlrStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper',
        {
            'macsec-ctrlr-state-up':'macsec_ctrlr_state_up',
            'macsec-ctrlr-state-down':'macsec_ctrlr_state_down',
            'macsec-ctrlr-state-admin-down':'macsec_ctrlr_state_admin_down',
        }, 'Cisco-IOS-XR-macsec-ctrlr-oper', _yang_ns._namespaces['Cisco-IOS-XR-macsec-ctrlr-oper']),
    'MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus.ActiveAssociation' : {
        'meta_info' : _MetaInfoClass('MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus.ActiveAssociation',
            False, 
            [
            _MetaInfoClassMember('association-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Association Number
                ''',
                'association_number',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('short-secure-channel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Short secure channel id
                ''',
                'short_secure_channel_id',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            ],
            'Cisco-IOS-XR-macsec-ctrlr-oper',
            'active-association',
            _yang_ns._namespaces['Cisco-IOS-XR-macsec-ctrlr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper'
        ),
    },
    'MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus' : {
        'meta_info' : _MetaInfoClass('MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus',
            False, 
            [
            _MetaInfoClassMember('active-association', REFERENCE_LIST, 'ActiveAssociation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper', 'MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus.ActiveAssociation', 
                [], [], 
                '''                Active Associations
                ''',
                'active_association',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('cipher-suite', REFERENCE_ENUM_CLASS, 'MacsecCtrlrCiphersuitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper', 'MacsecCtrlrCiphersuitEnum', 
                [], [], 
                '''                Cipher Suite
                ''',
                'cipher_suite',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('confidentiality-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Confidentiality offset
                ''',
                'confidentiality_offset',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('max-packet-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Max packet Number
                ''',
                'max_packet_number',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('protection-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Protection Enabled
                ''',
                'protection_enabled',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('recent-packet-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Recent Packet Number
                ''',
                'recent_packet_number',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('secure-channel-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Secure Channel Id
                ''',
                'secure_channel_id',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            ],
            'Cisco-IOS-XR-macsec-ctrlr-oper',
            'encrypt-sc-status',
            _yang_ns._namespaces['Cisco-IOS-XR-macsec-ctrlr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper'
        ),
    },
    'MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus.ActiveAssociation' : {
        'meta_info' : _MetaInfoClass('MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus.ActiveAssociation',
            False, 
            [
            _MetaInfoClassMember('association-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Association Number
                ''',
                'association_number',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('short-secure-channel-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Short secure channel id
                ''',
                'short_secure_channel_id',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            ],
            'Cisco-IOS-XR-macsec-ctrlr-oper',
            'active-association',
            _yang_ns._namespaces['Cisco-IOS-XR-macsec-ctrlr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper'
        ),
    },
    'MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus' : {
        'meta_info' : _MetaInfoClass('MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus',
            False, 
            [
            _MetaInfoClassMember('active-association', REFERENCE_LIST, 'ActiveAssociation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper', 'MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus.ActiveAssociation', 
                [], [], 
                '''                Active Associations
                ''',
                'active_association',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('cipher-suite', REFERENCE_ENUM_CLASS, 'MacsecCtrlrCiphersuitEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper', 'MacsecCtrlrCiphersuitEnum', 
                [], [], 
                '''                Cipher Suite
                ''',
                'cipher_suite',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('confidentiality-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Confidentiality offset
                ''',
                'confidentiality_offset',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('max-packet-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Max packet Number
                ''',
                'max_packet_number',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('protection-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Protection Enabled
                ''',
                'protection_enabled',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('recent-packet-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Recent Packet Number
                ''',
                'recent_packet_number',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('secure-channel-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Secure Channel Id
                ''',
                'secure_channel_id',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            ],
            'Cisco-IOS-XR-macsec-ctrlr-oper',
            'decrypt-sc-status',
            _yang_ns._namespaces['Cisco-IOS-XR-macsec-ctrlr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper'
        ),
    },
    'MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo' : {
        'meta_info' : _MetaInfoClass('MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo',
            False, 
            [
            _MetaInfoClassMember('decrypt-sc-status', REFERENCE_CLASS, 'DecryptScStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper', 'MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus', 
                [], [], 
                '''                Decrypt Secure Channel Status
                ''',
                'decrypt_sc_status',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('encrypt-sc-status', REFERENCE_CLASS, 'EncryptScStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper', 'MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus', 
                [], [], 
                '''                Encrypt Secure Channel Status
                ''',
                'encrypt_sc_status',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('must-secure', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Must Secure
                ''',
                'must_secure',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('replay-window-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Replay Window Size
                ''',
                'replay_window_size',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('secure-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Secure Mode
                ''',
                'secure_mode',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'MacsecCtrlrStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper', 'MacsecCtrlrStateEnum', 
                [], [], 
                '''                State
                ''',
                'state',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            ],
            'Cisco-IOS-XR-macsec-ctrlr-oper',
            'macsec-ctrlr-info',
            _yang_ns._namespaces['Cisco-IOS-XR-macsec-ctrlr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper'
        ),
    },
    'MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort' : {
        'meta_info' : _MetaInfoClass('MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Port name
                ''',
                'name',
                'Cisco-IOS-XR-macsec-ctrlr-oper', True),
            _MetaInfoClassMember('macsec-ctrlr-info', REFERENCE_CLASS, 'MacsecCtrlrInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper', 'MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo', 
                [], [], 
                '''                Macsec Controller operational data
                ''',
                'macsec_ctrlr_info',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            ],
            'Cisco-IOS-XR-macsec-ctrlr-oper',
            'macsec-ctrlr-port',
            _yang_ns._namespaces['Cisco-IOS-XR-macsec-ctrlr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper'
        ),
    },
    'MacsecCtrlrOper.MacsecCtrlrPorts' : {
        'meta_info' : _MetaInfoClass('MacsecCtrlrOper.MacsecCtrlrPorts',
            False, 
            [
            _MetaInfoClassMember('macsec-ctrlr-port', REFERENCE_LIST, 'MacsecCtrlrPort' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper', 'MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort', 
                [], [], 
                '''                Controller name
                ''',
                'macsec_ctrlr_port',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            ],
            'Cisco-IOS-XR-macsec-ctrlr-oper',
            'macsec-ctrlr-ports',
            _yang_ns._namespaces['Cisco-IOS-XR-macsec-ctrlr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper'
        ),
    },
    'MacsecCtrlrOper' : {
        'meta_info' : _MetaInfoClass('MacsecCtrlrOper',
            False, 
            [
            _MetaInfoClassMember('macsec-ctrlr-ports', REFERENCE_CLASS, 'MacsecCtrlrPorts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper', 'MacsecCtrlrOper.MacsecCtrlrPorts', 
                [], [], 
                '''                All Macsec Controller Port operational data
                ''',
                'macsec_ctrlr_ports',
                'Cisco-IOS-XR-macsec-ctrlr-oper', False),
            ],
            'Cisco-IOS-XR-macsec-ctrlr-oper',
            'macsec-ctrlr-oper',
            _yang_ns._namespaces['Cisco-IOS-XR-macsec-ctrlr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_macsec_ctrlr_oper'
        ),
    },
}
_meta_table['MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus.ActiveAssociation']['meta_info'].parent =_meta_table['MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus']['meta_info']
_meta_table['MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus.ActiveAssociation']['meta_info'].parent =_meta_table['MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus']['meta_info']
_meta_table['MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.EncryptScStatus']['meta_info'].parent =_meta_table['MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo']['meta_info']
_meta_table['MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo.DecryptScStatus']['meta_info'].parent =_meta_table['MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo']['meta_info']
_meta_table['MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort.MacsecCtrlrInfo']['meta_info'].parent =_meta_table['MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort']['meta_info']
_meta_table['MacsecCtrlrOper.MacsecCtrlrPorts.MacsecCtrlrPort']['meta_info'].parent =_meta_table['MacsecCtrlrOper.MacsecCtrlrPorts']['meta_info']
_meta_table['MacsecCtrlrOper.MacsecCtrlrPorts']['meta_info'].parent =_meta_table['MacsecCtrlrOper']['meta_info']
