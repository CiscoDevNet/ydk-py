


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CvcInBandSignaling_Enum' : _MetaInfoEnum('CvcInBandSignaling_Enum', 'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB',
        {
            'cas':'CAS',
            'none':'NONE',
            'cept':'CEPT',
            'transparent':'TRANSPARENT',
            'gr303':'GR303',
        }, 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-COMMON-DIAL-CONTROL-MIB']),
    'CvcCoderTypeRate_Enum' : _MetaInfoEnum('CvcCoderTypeRate_Enum', 'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB',
        {
            'other':'OTHER',
            'fax2400':'FAX2400',
            'fax4800':'FAX4800',
            'fax7200':'FAX7200',
            'fax9600':'FAX9600',
            'fax14400':'FAX14400',
            'fax12000':'FAX12000',
            'g729r8000':'G729R8000',
            'g729Ar8000':'G729AR8000',
            'g726r16000':'G726R16000',
            'g726r24000':'G726R24000',
            'g726r32000':'G726R32000',
            'g711ulawr64000':'G711ULAWR64000',
            'g711Alawr64000':'G711ALAWR64000',
            'g728r16000':'G728R16000',
            'g723r6300':'G723R6300',
            'g723r5300':'G723R5300',
            'gsmr13200':'GSMR13200',
            'g729Br8000':'G729BR8000',
            'g729ABr8000':'G729ABR8000',
            'g723Ar6300':'G723AR6300',
            'g723Ar5300':'G723AR5300',
            'ietfg729r8000':'IETFG729R8000',
            'gsmeEr12200':'GSMEER12200',
            'clearChannel':'CLEARCHANNEL',
            'g726r40000':'G726R40000',
            'llcc':'LLCC',
            'gsmAmrNb':'GSMAMRNB',
            'g722':'G722',
            'iLBC':'ILBC',
            'iLBCr15200':'ILBCR15200',
            'iLBCr13330':'ILBCR13330',
            'g722r4800':'G722R4800',
            'g722r5600':'G722R5600',
            'g722r6400':'G722R6400',
            'iSAC':'ISAC',
            'aaclc':'AACLC',
            'aacld':'AACLD',
        }, 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-COMMON-DIAL-CONTROL-MIB']),
    'CvcVideoCoderRate_Enum' : _MetaInfoEnum('CvcVideoCoderRate_Enum', 'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB',
        {
            'none':'NONE',
            'h261':'H261',
            'h263':'H263',
            'h263plus':'H263PLUS',
            'h264':'H264',
        }, 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-COMMON-DIAL-CONTROL-MIB']),
    'CvcH320CallType_Enum' : _MetaInfoEnum('CvcH320CallType_Enum', 'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB',
        {
            'none':'NONE',
            'primary':'PRIMARY',
            'secondary':'SECONDARY',
        }, 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-COMMON-DIAL-CONTROL-MIB']),
    'CvcSpeechCoderRate_Enum' : _MetaInfoEnum('CvcSpeechCoderRate_Enum', 'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB',
        {
            'g729r8000':'G729R8000',
            'g729Ar8000':'G729AR8000',
            'g726r16000':'G726R16000',
            'g726r24000':'G726R24000',
            'g726r32000':'G726R32000',
            'g711ulawr64000':'G711ULAWR64000',
            'g711Alawr64000':'G711ALAWR64000',
            'g728r16000':'G728R16000',
            'g723r6300':'G723R6300',
            'g723r5300':'G723R5300',
            'gsmr13200':'GSMR13200',
            'g729Br8000':'G729BR8000',
            'g729ABr8000':'G729ABR8000',
            'g723Ar6300':'G723AR6300',
            'g723Ar5300':'G723AR5300',
            'g729IETFr8000':'G729IETFR8000',
            'gsmeEr12200':'GSMEER12200',
            'clearChannel':'CLEARCHANNEL',
            'g726r40000':'G726R40000',
            'llcc':'LLCC',
            'gsmAmrNb':'GSMAMRNB',
            'iLBC':'ILBC',
            'iLBCr15200':'ILBCR15200',
            'iLBCr13330':'ILBCR13330',
            'g722r4800':'G722R4800',
            'g722r5600':'G722R5600',
            'g722r6400':'G722R6400',
            'iSAC':'ISAC',
            'aaclc':'AACLC',
            'aacld':'AACLD',
        }, 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-COMMON-DIAL-CONTROL-MIB']),
    'CvcFaxTransmitRate_Enum' : _MetaInfoEnum('CvcFaxTransmitRate_Enum', 'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB',
        {
            'none':'NONE',
            'voiceRate':'VOICERATE',
            'fax2400':'FAX2400',
            'fax4800':'FAX4800',
            'fax7200':'FAX7200',
            'fax9600':'FAX9600',
            'fax14400':'FAX14400',
            'fax12000':'FAX12000',
        }, 'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-COMMON-DIAL-CONTROL-MIB']),
    'CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallActiveTable.CvCommonDcCallActiveEntry' : {
        'meta_info' : _MetaInfoClass('CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallActiveTable.CvCommonDcCallActiveEntry',
            False, 
            [
            _MetaInfoClassMember('callActiveIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'callactiveindex',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('callActiveSetupTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'callactivesetuptime',
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
                [(10, 255)], [], 
                '''                Specifies the payload size of the voice packet.
                ''',
                'cvcommondccallactivecodecbytes',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCommonDcCallActiveCoderTypeRate', REFERENCE_ENUM_CLASS, 'CvcCoderTypeRate_Enum' , 'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CvcCoderTypeRate_Enum', 
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
            _MetaInfoClassMember('cvCommonDcCallActiveInBandSignaling', REFERENCE_ENUM_CLASS, 'CvcInBandSignaling_Enum' , 'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CvcInBandSignaling_Enum', 
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
        'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB'
        ),
    },
    'CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallActiveTable' : {
        'meta_info' : _MetaInfoClass('CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallActiveTable',
            False, 
            [
            _MetaInfoClassMember('cvCommonDcCallActiveEntry', REFERENCE_LIST, 'CvCommonDcCallActiveEntry' , 'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallActiveTable.CvCommonDcCallActiveEntry', 
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
        'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB'
        ),
    },
    'CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallHistoryTable.CvCommonDcCallHistoryEntry' : {
        'meta_info' : _MetaInfoClass('CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallHistoryTable.CvCommonDcCallHistoryEntry',
            False, 
            [
            _MetaInfoClassMember('cCallHistoryIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
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
                [(10, 255)], [], 
                '''                Specifies the payload size of the voice packet.
                ''',
                'cvcommondccallhistorycodecbytes',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCommonDcCallHistoryCoderTypeRate', REFERENCE_ENUM_CLASS, 'CvcCoderTypeRate_Enum' , 'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CvcCoderTypeRate_Enum', 
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
            _MetaInfoClassMember('cvCommonDcCallHistoryInBandSignaling', REFERENCE_ENUM_CLASS, 'CvcInBandSignaling_Enum' , 'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CvcInBandSignaling_Enum', 
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
        'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB'
        ),
    },
    'CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallHistoryTable' : {
        'meta_info' : _MetaInfoClass('CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallHistoryTable',
            False, 
            [
            _MetaInfoClassMember('cvCommonDcCallHistoryEntry', REFERENCE_LIST, 'CvCommonDcCallHistoryEntry' , 'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallHistoryTable.CvCommonDcCallHistoryEntry', 
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
        'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB'
        ),
    },
    'CISCOVOICECOMMONDIALCONTROLMIB' : {
        'meta_info' : _MetaInfoClass('CISCOVOICECOMMONDIALCONTROLMIB',
            False, 
            [
            _MetaInfoClassMember('cvCommonDcCallActiveTable', REFERENCE_CLASS, 'CvCommonDcCallActiveTable' , 'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallActiveTable', 
                [], [], 
                '''                This table is a common extension to the call active
                table of IETF Dial Control MIB. It contains common call 
                leg information about a network call leg.
                ''',
                'cvcommondccallactivetable',
                'CISCO-VOICE-COMMON-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCommonDcCallHistoryTable', REFERENCE_CLASS, 'CvCommonDcCallHistoryTable' , 'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallHistoryTable', 
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
        'ydk.models.voice.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB'
        ),
    },
}
_meta_table['CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallActiveTable.CvCommonDcCallActiveEntry']['meta_info'].parent =_meta_table['CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallActiveTable']['meta_info']
_meta_table['CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallHistoryTable.CvCommonDcCallHistoryEntry']['meta_info'].parent =_meta_table['CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallHistoryTable']['meta_info']
_meta_table['CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallActiveTable']['meta_info'].parent =_meta_table['CISCOVOICECOMMONDIALCONTROLMIB']['meta_info']
_meta_table['CISCOVOICECOMMONDIALCONTROLMIB.CvCommonDcCallHistoryTable']['meta_info'].parent =_meta_table['CISCOVOICECOMMONDIALCONTROLMIB']['meta_info']
