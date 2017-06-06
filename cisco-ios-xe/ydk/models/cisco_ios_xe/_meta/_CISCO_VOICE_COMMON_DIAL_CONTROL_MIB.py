


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CvccodertyperateEnum' : _MetaInfoEnum('CvccodertyperateEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB',
        {
            'other':'other',
            'fax2400':'fax2400',
            'fax4800':'fax4800',
            'fax7200':'fax7200',
            'fax9600':'fax9600',
            'fax14400':'fax14400',
            'fax12000':'fax12000',
            'g729r8000':'g729r8000',
            'g729Ar8000':'g729Ar8000',
            'g726r16000':'g726r16000',
            'g726r24000':'g726r24000',
            'g726r32000':'g726r32000',
            'g711ulawr64000':'g711ulawr64000',
            'g711Alawr64000':'g711Alawr64000',
            'g728r16000':'g728r16000',
            'g723r6300':'g723r6300',
            'g723r5300':'g723r5300',
            'gsmr13200':'gsmr13200',
            'g729Br8000':'g729Br8000',
            'g729ABr8000':'g729ABr8000',
            'g723Ar6300':'g723Ar6300',
            'g723Ar5300':'g723Ar5300',
            'ietfg729r8000':'ietfg729r8000',
            'gsmeEr12200':'gsmeEr12200',
            'clearChannel':'clearChannel',
            'g726r40000':'g726r40000',
            'llcc':'llcc',
            'gsmAmrNb':'gsmAmrNb',
            'g722':'g722',
            'iLBC':'iLBC',
            'iLBCr15200':'iLBCr15200',
            'iLBCr13330':'iLBCr13330',
            'g722r4800':'g722r4800',
            'g722r5600':'g722r5600',
            'g722r6400':'g722r6400',
            'iSAC':'iSAC',
            'aaclc':'aaclc',
            'aacld':'aacld',
        }, 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-COMMON-DIAL-CONTROL-MIB']),
    'CvcinbandsignalingEnum' : _MetaInfoEnum('CvcinbandsignalingEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB',
        {
            'cas':'cas',
            'none':'none',
            'cept':'cept',
            'transparent':'transparent',
            'gr303':'gr303',
        }, 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-COMMON-DIAL-CONTROL-MIB']),
    'CvcfaxtransmitrateEnum' : _MetaInfoEnum('CvcfaxtransmitrateEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB',
        {
            'none':'none',
            'voiceRate':'voiceRate',
            'fax2400':'fax2400',
            'fax4800':'fax4800',
            'fax7200':'fax7200',
            'fax9600':'fax9600',
            'fax14400':'fax14400',
            'fax12000':'fax12000',
        }, 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-COMMON-DIAL-CONTROL-MIB']),
    'CvcspeechcoderrateEnum' : _MetaInfoEnum('CvcspeechcoderrateEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB',
        {
            'g729r8000':'g729r8000',
            'g729Ar8000':'g729Ar8000',
            'g726r16000':'g726r16000',
            'g726r24000':'g726r24000',
            'g726r32000':'g726r32000',
            'g711ulawr64000':'g711ulawr64000',
            'g711Alawr64000':'g711Alawr64000',
            'g728r16000':'g728r16000',
            'g723r6300':'g723r6300',
            'g723r5300':'g723r5300',
            'gsmr13200':'gsmr13200',
            'g729Br8000':'g729Br8000',
            'g729ABr8000':'g729ABr8000',
            'g723Ar6300':'g723Ar6300',
            'g723Ar5300':'g723Ar5300',
            'g729IETFr8000':'g729IETFr8000',
            'gsmeEr12200':'gsmeEr12200',
            'clearChannel':'clearChannel',
            'g726r40000':'g726r40000',
            'llcc':'llcc',
            'gsmAmrNb':'gsmAmrNb',
            'iLBC':'iLBC',
            'iLBCr15200':'iLBCr15200',
            'iLBCr13330':'iLBCr13330',
            'g722r4800':'g722r4800',
            'g722r5600':'g722r5600',
            'g722r6400':'g722r6400',
            'iSAC':'iSAC',
            'aaclc':'aaclc',
            'aacld':'aacld',
        }, 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-COMMON-DIAL-CONTROL-MIB']),
    'Cvch320CalltypeEnum' : _MetaInfoEnum('Cvch320CalltypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB',
        {
            'none':'none',
            'primary':'primary',
            'secondary':'secondary',
        }, 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-COMMON-DIAL-CONTROL-MIB']),
    'CvcvideocoderrateEnum' : _MetaInfoEnum('CvcvideocoderrateEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB',
        {
            'none':'none',
            'h261':'h261',
            'h263':'h263',
            'h263plus':'h263plus',
            'h264':'h264',
        }, 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-COMMON-DIAL-CONTROL-MIB']),
    'CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable.Cvcommondccallactiveentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable.Cvcommondccallactiveentry',
            False, 
            [
            _MetaInfoClassMember('callActiveSetupTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'callactivesetuptime',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('callActiveIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'callactiveindex',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvCommonDcCallActiveCallerIDBlock', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The object indicates whether or not the caller ID feature
                is blocked for this voice call.
                ''',
                'cvcommondccallactivecalleridblock',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCommonDcCallActiveCallingName', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The calling party name this call is connected to. If the
                name is not available, then it will have a length of zero.
                ''',
                'cvcommondccallactivecallingname',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCommonDcCallActiveCodecBytes', ATTRIBUTE, 'int' , None, None, 
                [('10', '255')], [], 
                '''                Specifies the payload size of the voice packet.
                ''',
                'cvcommondccallactivecodecbytes',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCommonDcCallActiveCoderTypeRate', REFERENCE_ENUM_CLASS, 'CvccodertyperateEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CvccodertyperateEnum', 
                [], [], 
                '''                The negotiated coder rate. It specifies the transmit
                rate of voice/fax compression to its associated call leg 
                for the call.
                This rate is different from the configuration rate 
                because of rate negotiation during the call.
                ''',
                'cvcommondccallactivecodertyperate',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCommonDcCallActiveConnectionId', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                The global call identifier for the network call.
                ''',
                'cvcommondccallactiveconnectionid',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCommonDcCallActiveInBandSignaling', REFERENCE_ENUM_CLASS, 'CvcinbandsignalingEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CvcinbandsignalingEnum', 
                [], [], 
                '''                Specifies the type of in-band signaling being used on
                the call.  This object is instantiated only for 
                Connection Trunk calls.
                ''',
                'cvcommondccallactiveinbandsignaling',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCommonDcCallActiveVADEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The object indicates whether or not the VAD (Voice
                Activity Detection) is enabled for the voice call.
                ''',
                'cvcommondccallactivevadenable',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB',
            'cvCommonDcCallActiveEntry',
            _yang_ns._namespaces['CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable',
            False, 
            [
            _MetaInfoClassMember('cvCommonDcCallActiveEntry', REFERENCE_LIST, 'Cvcommondccallactiveentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable.Cvcommondccallactiveentry', 
                [], [], 
                '''                The common information regarding a single network call
                leg. The call leg entry is identified by using the same 
                index objects that are used by Call Active table of IETF 
                Dial Control MIB to identify the call.
                An entry of this table is created when its associated 
                call active entry in the IETF Dial Control MIB is created
                and the call active entry contains information for the 
                call establishment to a network dialpeer.             
                The entry is deleted when its associated call active entry 
                in the IETF Dial Control MIB is deleted.
                ''',
                'cvcommondccallactiveentry',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB',
            'cvCommonDcCallActiveTable',
            _yang_ns._namespaces['CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable.Cvcommondccallhistoryentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable.Cvcommondccallhistoryentry',
            False, 
            [
            _MetaInfoClassMember('cCallHistoryIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'ccallhistoryindex',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvCommonDcCallHistoryCallerIDBlock', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The object indicates whether or not the caller ID
                feature is blocked for this voice call.
                ''',
                'cvcommondccallhistorycalleridblock',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCommonDcCallHistoryCallingName', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The calling party name this call is connected to. If
                the name is not available, then it will have a length 
                of zero.
                ''',
                'cvcommondccallhistorycallingname',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCommonDcCallHistoryCodecBytes', ATTRIBUTE, 'int' , None, None, 
                [('10', '255')], [], 
                '''                Specifies the payload size of the voice packet.
                ''',
                'cvcommondccallhistorycodecbytes',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCommonDcCallHistoryCoderTypeRate', REFERENCE_ENUM_CLASS, 'CvccodertyperateEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CvccodertyperateEnum', 
                [], [], 
                '''                The negotiated coder rate. It specifies the transmit rate
                of voice/fax compression to its associated call leg for 
                the call.
                This rate is different from the configuration rate 
                because of rate negotiation during the call.
                ''',
                'cvcommondccallhistorycodertyperate',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCommonDcCallHistoryConnectionId', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                The global call identifier for the gateway call.
                ''',
                'cvcommondccallhistoryconnectionid',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCommonDcCallHistoryInBandSignaling', REFERENCE_ENUM_CLASS, 'CvcinbandsignalingEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CvcinbandsignalingEnum', 
                [], [], 
                '''                Specifies the type of in-band signaling used on the
                call.  This object is instantiated only for 
                Connection Trunk calls.
                ''',
                'cvcommondccallhistoryinbandsignaling',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCommonDcCallHistoryVADEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The object indicates whether or not the VAD (Voice
                Activity Detection) was enabled for the voice call.
                ''',
                'cvcommondccallhistoryvadenable',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB',
            'cvCommonDcCallHistoryEntry',
            _yang_ns._namespaces['CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable',
            False, 
            [
            _MetaInfoClassMember('cvCommonDcCallHistoryEntry', REFERENCE_LIST, 'Cvcommondccallhistoryentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable.Cvcommondccallhistoryentry', 
                [], [], 
                '''                The common information regarding a single network call
                leg. The call leg entry is identified by using the same 
                index objects that are used by Call Active table of IETF 
                Dial Control MIB to identify the call.
                An entry of this table is created when its associated 
                call history entry in the IETF Dial Control MIB is 
                created and the call history entry contains information 
                for the call establishment to a network dialpeer.
                The entry is deleted when its associated call history 
                entry in the IETF Dial Control MIB is deleted.
                ''',
                'cvcommondccallhistoryentry',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB',
            'cvCommonDcCallHistoryTable',
            _yang_ns._namespaces['CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceCommonDialControlMib' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceCommonDialControlMib',
            False, 
            [
            _MetaInfoClassMember('cvCommonDcCallActiveTable', REFERENCE_CLASS, 'Cvcommondccallactivetable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable', 
                [], [], 
                '''                This table is a common extension to the call active
                table of IETF Dial Control MIB. It contains common call 
                leg information about a network call leg.
                ''',
                'cvcommondccallactivetable',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCommonDcCallHistoryTable', REFERENCE_CLASS, 'Cvcommondccallhistorytable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable', 
                [], [], 
                '''                This table is the Common extension to the call history
                table of IETF Dial Control MIB. It contains Common call 
                leg information about a network call leg.
                ''',
                'cvcommondccallhistorytable',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB',
            'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB',
            _yang_ns._namespaces['CISCO-VOICE-COMMON-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB'
        ),
    },
}
_meta_table['CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable.Cvcommondccallactiveentry']['meta_info'].parent =_meta_table['CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable']['meta_info']
_meta_table['CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable.Cvcommondccallhistoryentry']['meta_info'].parent =_meta_table['CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable']['meta_info']
_meta_table['CiscoVoiceCommonDialControlMib.Cvcommondccallactivetable']['meta_info'].parent =_meta_table['CiscoVoiceCommonDialControlMib']['meta_info']
_meta_table['CiscoVoiceCommonDialControlMib.Cvcommondccallhistorytable']['meta_info'].parent =_meta_table['CiscoVoiceCommonDialControlMib']['meta_info']
