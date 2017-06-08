


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'PwRtpFlagEnum' : _MetaInfoEnum('PwRtpFlagEnum', 'ydk.models.ietf.ietf_pw',
        {
            'UNUSE':'UNUSE',
            'USE':'USE',
            'UNKNOWN':'UNKNOWN',
        }, 'ietf-pw', _yang_ns._namespaces['ietf-pw']),
    'PwTypeEnum' : _MetaInfoEnum('PwTypeEnum', 'ydk.models.ietf.ietf_pw',
        {
            'unknown':'unknown',
            'dlciOld':'dlciOld',
            'atmSdu':'atmSdu',
            'atmCell':'atmCell',
            'vlan':'vlan',
            'ethernet':'ethernet',
            'hdlc':'hdlc',
            'ppp':'ppp',
            'sdhCESoM':'sdhCESoM',
            'atmVCCn':'atmVCCn',
            'atmVPCn':'atmVPCn',
            'ipL2':'ipL2',
            'atmVCC1':'atmVCC1',
            'atmVPC1':'atmVPC1',
            'atmPDU':'atmPDU',
            'frPort':'frPort',
            'sdhCEoP':'sdhCEoP',
            'saTopE1':'saTopE1',
            'saTopT1':'saTopT1',
            'saTopE3':'saTopE3',
            'saTopT3':'saTopT3',
            'ceSoPSNB':'ceSoPSNB',
            'tdmAAL1':'tdmAAL1',
            'ceSoPSNC':'ceSoPSNC',
            'tdmAAL2':'tdmAAL2',
            'dlciNew':'dlciNew',
        }, 'ietf-pw', _yang_ns._namespaces['ietf-pw']),
    'PwTimestampModeEnum' : _MetaInfoEnum('PwTimestampModeEnum', 'ydk.models.ietf.ietf_pw',
        {
            'Absolute':'Absolute',
            'Differential':'Differential',
            'UNKNOWN':'UNKNOWN',
        }, 'ietf-pw', _yang_ns._namespaces['ietf-pw']),
    'CvTypeEnum' : _MetaInfoEnum('CvTypeEnum', 'ydk.models.ietf.ietf_pw',
        {
            'ICMP-ping':'ICMP_ping',
            'LSP-ping':'LSP_ping',
            'BFD-basic-ip':'BFD_basic_ip',
            'BFD-basic-raw':'BFD_basic_raw',
            'BFD-signalling-ip':'BFD_signalling_ip',
            'BFD-signalling-raw':'BFD_signalling_raw',
        }, 'ietf-pw', _yang_ns._namespaces['ietf-pw']),
    'CwCapableTypeEnum' : _MetaInfoEnum('CwCapableTypeEnum', 'ydk.models.ietf.ietf_pw',
        {
            'non-preferred':'non_preferred',
            'preferred':'preferred',
        }, 'ietf-pw', _yang_ns._namespaces['ietf-pw']),
    'CcTypeEnum' : _MetaInfoEnum('CcTypeEnum', 'ydk.models.ietf.ietf_pw',
        {
            'pw-ach':'pw_ach',
            'alert-label':'alert_label',
            'ttl':'ttl',
        }, 'ietf-pw', _yang_ns._namespaces['ietf-pw']),
    'Pwe3.SsPw.SsPw_.Tunnel' : {
        'meta_info' : _MetaInfoClass('Pwe3.SsPw.SsPw_.Tunnel',
            False, 
            [
            _MetaInfoClassMember('tunnel-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                tunnel identifier
                ''',
                'tunnel_id',
                'ietf-pw', True),
            ],
            'ietf-pw',
            'tunnel',
            _yang_ns._namespaces['ietf-pw'],
        'ydk.models.ietf.ietf_pw'
        ),
    },
    'Pwe3.SsPw.SsPw_.Interfaces.Interface.VccvParameter' : {
        'meta_info' : _MetaInfoClass('Pwe3.SsPw.SsPw_.Interfaces.Interface.VccvParameter',
            False, 
            [
            _MetaInfoClassMember('cc', REFERENCE_ENUM_CLASS, 'CcTypeEnum' , 'ydk.models.ietf.ietf_pw', 'CcTypeEnum', 
                [], [], 
                '''                Control Channel Types
                ''',
                'cc',
                'ietf-pw', False),
            _MetaInfoClassMember('cv', REFERENCE_ENUM_CLASS, 'CvTypeEnum' , 'ydk.models.ietf.ietf_pw', 'CvTypeEnum', 
                [], [], 
                '''                Connectivity Verification Types
                ''',
                'cv',
                'ietf-pw', False),
            ],
            'ietf-pw',
            'vccv-parameter',
            _yang_ns._namespaces['ietf-pw'],
        'ydk.models.ietf.ietf_pw'
        ),
    },
    'Pwe3.SsPw.SsPw_.Interfaces.Interface.TdmOptions' : {
        'meta_info' : _MetaInfoClass('Pwe3.SsPw.SsPw_.Interfaces.Interface.TdmOptions',
            False, 
            [
            _MetaInfoClassMember('cas', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The local cas of the PW
                ''',
                'cas',
                'ietf-pw', False),
            _MetaInfoClassMember('frequency', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The local frequency of timestamping clock
                ''',
                'frequency',
                'ietf-pw', False),
            _MetaInfoClassMember('payload-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The local payload type in the RTP header expected by the PW endpoint distributing this FEC
                ''',
                'payload_type',
                'ietf-pw', False),
            _MetaInfoClassMember('rtp', REFERENCE_ENUM_CLASS, 'PwRtpFlagEnum' , 'ydk.models.ietf.ietf_pw', 'PwRtpFlagEnum', 
                [], [], 
                '''                The local rtp header usage
                ''',
                'rtp',
                'ietf-pw', False),
            _MetaInfoClassMember('sp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The local sp of the PW
                ''',
                'sp',
                'ietf-pw', False),
            _MetaInfoClassMember('ssrc', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The local value of the Synchronization source ID
                ''',
                'ssrc',
                'ietf-pw', False),
            _MetaInfoClassMember('timestamp-mode', REFERENCE_ENUM_CLASS, 'PwTimestampModeEnum' , 'ydk.models.ietf.ietf_pw', 'PwTimestampModeEnum', 
                [], [], 
                '''                The local timestamp mode
                ''',
                'timestamp_mode',
                'ietf-pw', False),
            ],
            'ietf-pw',
            'tdm-options',
            _yang_ns._namespaces['ietf-pw'],
        'ydk.models.ietf.ietf_pw'
        ),
    },
    'Pwe3.SsPw.SsPw_.Interfaces.Interface.CepOption' : {
        'meta_info' : _MetaInfoClass('Pwe3.SsPw.SsPw_.Interfaces.Interface.CepOption',
            False, 
            [
            _MetaInfoClassMember('ais', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The local ais of CEP Options parameter of the PW
                ''',
                'ais',
                'ietf-pw', False),
            _MetaInfoClassMember('async-e3', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The local async-e3 of CEP Options parameter of the PW
                ''',
                'async_e3',
                'ietf-pw', False),
            _MetaInfoClassMember('async-t3', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The local async-t3 of CEP Options parameter of the PW
                ''',
                'async_t3',
                'ietf-pw', False),
            _MetaInfoClassMember('cep-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The local cep type of CEP Options parameter of the PW
                ''',
                'cep_type',
                'ietf-pw', False),
            _MetaInfoClassMember('ebm', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The local ebm of CEP Options parameter of the PW
                ''',
                'ebm',
                'ietf-pw', False),
            _MetaInfoClassMember('rtp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The local rtp of CEP Options parameter of the PW
                ''',
                'rtp',
                'ietf-pw', False),
            _MetaInfoClassMember('une', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The local une of CEP Options parameter of the PW
                ''',
                'une',
                'ietf-pw', False),
            ],
            'ietf-pw',
            'cep-option',
            _yang_ns._namespaces['ietf-pw'],
        'ydk.models.ietf.ietf_pw'
        ),
    },
    'Pwe3.SsPw.SsPw_.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Pwe3.SsPw.SsPw_.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interfaces used for pw
                ''',
                'name',
                'ietf-pw', True),
            _MetaInfoClassMember('bit-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The local bit rate of the PW
                ''',
                'bit_rate',
                'ietf-pw', False),
            _MetaInfoClassMember('cells-per-packet', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The local TDMoIP AAL1 cells per packet of the PW
                ''',
                'cells_per_packet',
                'ietf-pw', False),
            _MetaInfoClassMember('cep-option', REFERENCE_CLASS, 'CepOption' , 'ydk.models.ietf.ietf_pw', 'Pwe3.SsPw.SsPw_.Interfaces.Interface.CepOption', 
                [], [], 
                '''                The CEP Options parameter of the PW
                ''',
                'cep_option',
                'ietf-pw', False),
            _MetaInfoClassMember('fcs-retention-indicator', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The negotiated fcs retention indicator of the PW
                ''',
                'fcs_retention_indicator',
                'ietf-pw', False),
            _MetaInfoClassMember('fr-dlci-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The local fr dlci length of the PW
                ''',
                'fr_dlci_len',
                'ietf-pw', False),
            _MetaInfoClassMember('frag-indicator', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The local fragmentation indicator of the PW
                ''',
                'frag_indicator',
                'ietf-pw', False),
            _MetaInfoClassMember('interface-description', ATTRIBUTE, 'str' , None, None, 
                [(0, 81)], [], 
                '''                The local interface description of the PW
                ''',
                'interface_description',
                'ietf-pw', False),
            _MetaInfoClassMember('max-atm-cells', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The local max atm cells of the PW
                ''',
                'max_atm_cells',
                'ietf-pw', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pseudowire mtu
                ''',
                'mtu',
                'ietf-pw', False),
            _MetaInfoClassMember('payload-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The local payload bytes of the PW
                ''',
                'payload_bytes',
                'ietf-pw', False),
            _MetaInfoClassMember('requested-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The local requested VLAN ID of the PW
                ''',
                'requested_vlan_id',
                'ietf-pw', False),
            _MetaInfoClassMember('tdm-options', REFERENCE_CLASS, 'TdmOptions' , 'ydk.models.ietf.ietf_pw', 'Pwe3.SsPw.SsPw_.Interfaces.Interface.TdmOptions', 
                [], [], 
                '''                The TDM Options parameter of the PW
                ''',
                'tdm_options',
                'ietf-pw', False),
            _MetaInfoClassMember('vccv-parameter', REFERENCE_CLASS, 'VccvParameter' , 'ydk.models.ietf.ietf_pw', 'Pwe3.SsPw.SsPw_.Interfaces.Interface.VccvParameter', 
                [], [], 
                '''                vccv-parameter
                ''',
                'vccv_parameter',
                'ietf-pw', False),
            ],
            'ietf-pw',
            'interface',
            _yang_ns._namespaces['ietf-pw'],
        'ydk.models.ietf.ietf_pw'
        ),
    },
    'Pwe3.SsPw.SsPw_.Interfaces' : {
        'meta_info' : _MetaInfoClass('Pwe3.SsPw.SsPw_.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.ietf.ietf_pw', 'Pwe3.SsPw.SsPw_.Interfaces.Interface', 
                [], [], 
                '''                interface list
                ''',
                'interface',
                'ietf-pw', False),
            ],
            'ietf-pw',
            'interfaces',
            _yang_ns._namespaces['ietf-pw'],
        'ydk.models.ietf.ietf_pw'
        ),
    },
    'Pwe3.SsPw.SsPw_' : {
        'meta_info' : _MetaInfoClass('Pwe3.SsPw.SsPw_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ss-pseudowire name
                ''',
                'name',
                'ietf-pw', True),
            _MetaInfoClassMember('agi', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Attachment Group Identifier
                ''',
                'agi',
                'ietf-pw', False),
            _MetaInfoClassMember('autodiscovery-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                enable the auto-discovery
                ''',
                'autodiscovery_enable',
                'ietf-pw', False),
            _MetaInfoClassMember('cw-capable', REFERENCE_ENUM_CLASS, 'CwCapableTypeEnum' , 'ydk.models.ietf.ietf_pw', 'CwCapableTypeEnum', 
                [], [], 
                '''                control-word negotiation preference
                ''',
                'cw_capable',
                'ietf-pw', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.ietf.ietf_pw', 'Pwe3.SsPw.SsPw_.Interfaces', 
                [], [], 
                '''                Interfaces
                ''',
                'interfaces',
                'ietf-pw', False),
            _MetaInfoClassMember('leaf-type', REFERENCE_ENUM_CLASS, 'PwTypeEnum' , 'ydk.models.ietf.ietf_pw', 'PwTypeEnum', 
                [], [], 
                '''                pseudo-wire type
                ''',
                'leaf_type',
                'ietf-pw', False),
            _MetaInfoClassMember('peer-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                peer IP address
                ''',
                'peer_ip',
                'ietf-pw', False, [
                    _MetaInfoClassMember('peer-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        peer IP address
                        ''',
                        'peer_ip',
                        'ietf-pw', False),
                    _MetaInfoClassMember('peer-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        peer IP address
                        ''',
                        'peer_ip',
                        'ietf-pw', False),
                ]),
            _MetaInfoClassMember('pw-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pseudowire id
                ''',
                'pw_id',
                'ietf-pw', False),
            _MetaInfoClassMember('receive-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                receive label
                ''',
                'receive_label',
                'ietf-pw', False),
            _MetaInfoClassMember('source-AII', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Source Attachment individual identifier
                ''',
                'source_aii',
                'ietf-pw', False),
            _MetaInfoClassMember('static-pw-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pseudowire id
                ''',
                'static_pw_id',
                'ietf-pw', False),
            _MetaInfoClassMember('target-AII', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Target Attachment individual identifier
                ''',
                'target_aii',
                'ietf-pw', False),
            _MetaInfoClassMember('transmit-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                transmit lable
                ''',
                'transmit_label',
                'ietf-pw', False),
            _MetaInfoClassMember('tunnel', REFERENCE_LIST, 'Tunnel' , 'ydk.models.ietf.ietf_pw', 'Pwe3.SsPw.SsPw_.Tunnel', 
                [], [], 
                '''                tunnel list
                ''',
                'tunnel',
                'ietf-pw', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'PwTypeEnum' , 'ydk.models.ietf.ietf_pw', 'PwTypeEnum', 
                [], [], 
                '''                pseudo-wire type
                ''',
                'type',
                'ietf-pw', False),
            ],
            'ietf-pw',
            'ss-pw',
            _yang_ns._namespaces['ietf-pw'],
        'ydk.models.ietf.ietf_pw'
        ),
    },
    'Pwe3.SsPw' : {
        'meta_info' : _MetaInfoClass('Pwe3.SsPw',
            False, 
            [
            _MetaInfoClassMember('ss-pw', REFERENCE_LIST, 'SsPw_' , 'ydk.models.ietf.ietf_pw', 'Pwe3.SsPw.SsPw_', 
                [], [], 
                '''                ss-pw list
                ''',
                'ss_pw',
                'ietf-pw', False),
            ],
            'ietf-pw',
            'ss-pw',
            _yang_ns._namespaces['ietf-pw'],
        'ydk.models.ietf.ietf_pw'
        ),
    },
    'Pwe3.MsPw.MsPw_.PwSegmentA' : {
        'meta_info' : _MetaInfoClass('Pwe3.MsPw.MsPw_.PwSegmentA',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                pseudowire segment a name
                ''',
                'name',
                'ietf-pw', True),
            ],
            'ietf-pw',
            'pw-segment-a',
            _yang_ns._namespaces['ietf-pw'],
        'ydk.models.ietf.ietf_pw'
        ),
    },
    'Pwe3.MsPw.MsPw_.PwSegmentZ' : {
        'meta_info' : _MetaInfoClass('Pwe3.MsPw.MsPw_.PwSegmentZ',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                pseudowire segment z name
                ''',
                'name',
                'ietf-pw', True),
            ],
            'ietf-pw',
            'pw-segment-z',
            _yang_ns._namespaces['ietf-pw'],
        'ydk.models.ietf.ietf_pw'
        ),
    },
    'Pwe3.MsPw.MsPw_' : {
        'meta_info' : _MetaInfoClass('Pwe3.MsPw.MsPw_',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ms-pseudowire name
                ''',
                'name',
                'ietf-pw', True),
            _MetaInfoClassMember('pw-segment-a', REFERENCE_LIST, 'PwSegmentA' , 'ydk.models.ietf.ietf_pw', 'Pwe3.MsPw.MsPw_.PwSegmentA', 
                [], [], 
                '''                pw segment-a list
                ''',
                'pw_segment_a',
                'ietf-pw', False),
            _MetaInfoClassMember('pw-segment-z', REFERENCE_LIST, 'PwSegmentZ' , 'ydk.models.ietf.ietf_pw', 'Pwe3.MsPw.MsPw_.PwSegmentZ', 
                [], [], 
                '''                pw segment-z list
                ''',
                'pw_segment_z',
                'ietf-pw', False),
            ],
            'ietf-pw',
            'ms-pw',
            _yang_ns._namespaces['ietf-pw'],
        'ydk.models.ietf.ietf_pw'
        ),
    },
    'Pwe3.MsPw' : {
        'meta_info' : _MetaInfoClass('Pwe3.MsPw',
            False, 
            [
            _MetaInfoClassMember('ms-pw', REFERENCE_LIST, 'MsPw_' , 'ydk.models.ietf.ietf_pw', 'Pwe3.MsPw.MsPw_', 
                [], [], 
                '''                ms-pw list
                ''',
                'ms_pw',
                'ietf-pw', False),
            ],
            'ietf-pw',
            'ms-pw',
            _yang_ns._namespaces['ietf-pw'],
        'ydk.models.ietf.ietf_pw'
        ),
    },
    'Pwe3' : {
        'meta_info' : _MetaInfoClass('Pwe3',
            False, 
            [
            _MetaInfoClassMember('ms-pw', REFERENCE_CLASS, 'MsPw' , 'ydk.models.ietf.ietf_pw', 'Pwe3.MsPw', 
                [], [], 
                '''                configure ms-pw
                ''',
                'ms_pw',
                'ietf-pw', False),
            _MetaInfoClassMember('ss-pw', REFERENCE_CLASS, 'SsPw' , 'ydk.models.ietf.ietf_pw', 'Pwe3.SsPw', 
                [], [], 
                '''                configure ss-pw
                ''',
                'ss_pw',
                'ietf-pw', False),
            ],
            'ietf-pw',
            'pwe3',
            _yang_ns._namespaces['ietf-pw'],
        'ydk.models.ietf.ietf_pw'
        ),
    },
}
_meta_table['Pwe3.SsPw.SsPw_.Interfaces.Interface.VccvParameter']['meta_info'].parent =_meta_table['Pwe3.SsPw.SsPw_.Interfaces.Interface']['meta_info']
_meta_table['Pwe3.SsPw.SsPw_.Interfaces.Interface.TdmOptions']['meta_info'].parent =_meta_table['Pwe3.SsPw.SsPw_.Interfaces.Interface']['meta_info']
_meta_table['Pwe3.SsPw.SsPw_.Interfaces.Interface.CepOption']['meta_info'].parent =_meta_table['Pwe3.SsPw.SsPw_.Interfaces.Interface']['meta_info']
_meta_table['Pwe3.SsPw.SsPw_.Interfaces.Interface']['meta_info'].parent =_meta_table['Pwe3.SsPw.SsPw_.Interfaces']['meta_info']
_meta_table['Pwe3.SsPw.SsPw_.Tunnel']['meta_info'].parent =_meta_table['Pwe3.SsPw.SsPw_']['meta_info']
_meta_table['Pwe3.SsPw.SsPw_.Interfaces']['meta_info'].parent =_meta_table['Pwe3.SsPw.SsPw_']['meta_info']
_meta_table['Pwe3.SsPw.SsPw_']['meta_info'].parent =_meta_table['Pwe3.SsPw']['meta_info']
_meta_table['Pwe3.MsPw.MsPw_.PwSegmentA']['meta_info'].parent =_meta_table['Pwe3.MsPw.MsPw_']['meta_info']
_meta_table['Pwe3.MsPw.MsPw_.PwSegmentZ']['meta_info'].parent =_meta_table['Pwe3.MsPw.MsPw_']['meta_info']
_meta_table['Pwe3.MsPw.MsPw_']['meta_info'].parent =_meta_table['Pwe3.MsPw']['meta_info']
_meta_table['Pwe3.SsPw']['meta_info'].parent =_meta_table['Pwe3']['meta_info']
_meta_table['Pwe3.MsPw']['meta_info'].parent =_meta_table['Pwe3']['meta_info']
