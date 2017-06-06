


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CvcallvolumestatsintvltypeEnum' : _MetaInfoEnum('CvcallvolumestatsintvltypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB',
        {
            'secondStats':'secondStats',
            'minuteStats':'minuteStats',
            'hourStats':'hourStats',
        }, 'CISCO-VOICE-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB']),
    'CvcallconnectiontypeEnum' : _MetaInfoEnum('CvcallconnectiontypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB',
        {
            'h323':'h323',
            'sip':'sip',
            'mgcp':'mgcp',
            'sccp':'sccp',
            'multicast':'multicast',
            'cacontrol':'cacontrol',
            'telephony':'telephony',
        }, 'CISCO-VOICE-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB']),
    'CvsessionprotocolEnum' : _MetaInfoEnum('CvsessionprotocolEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB',
        {
            'other':'other',
            'cisco':'cisco',
            'sdp':'sdp',
            'sip':'sip',
            'multicast':'multicast',
            'sccp':'sccp',
        }, 'CISCO-VOICE-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB']),
    'CvamrnbrtpencapEnum' : _MetaInfoEnum('CvamrnbrtpencapEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB',
        {
            'rfc3267':'rfc3267',
        }, 'CISCO-VOICE-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB']),
    'CvcallvolumewmintvltypeEnum' : _MetaInfoEnum('CvcallvolumewmintvltypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB',
        {
            'secondStats':'secondStats',
            'minuteStats':'minuteStats',
            'hourStats':'hourStats',
            'fromReloadStats':'fromReloadStats',
        }, 'CISCO-VOICE-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB']),
    'CvilbcframemodeEnum' : _MetaInfoEnum('CvilbcframemodeEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB',
        {
            'frameMode20':'frameMode20',
            'frameMode30':'frameMode30',
        }, 'CISCO-VOICE-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB']),
    'CiscoVoiceDialControlMib.Cvgeneralconfiguration' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvgeneralconfiguration',
            False, 
            [
            _MetaInfoClassMember('cvGeneralDSCPPolicyNotificationEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether cvdcPolicyViolationNotification
                traps should be generated for a RPH to DSCP mapping violation
                for SIP voice calls.
                
                If the value of this object is 'true',
                cvdcPolicyViolationNotification traps will be generated for SIP
                voice over IP peers when a RPH to DSCP violation condition is
                detected .  If the value of this object is 'false',
                cvdcPolicyViolationNotification traps will be generated only
                for calls for which the 
                cvVoIPPeerCfgDSCPPolicyNotificationEnable object of voice
                over IP peers having set to 'true'.
                ''',
                'cvgeneraldscppolicynotificationenable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvGeneralFallbackNotificationEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether cvdcFallbackNotification
                traps should be generated for fallback.
                If the value of this object is 'true',
                cvdcFallbackNotification traps will be generated
                for all voice over IP peers.
                ''',
                'cvgeneralfallbacknotificationenable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvGeneralMediaPolicyNotificationEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether cvdcPolicyViolationNotification
                traps should be generated for Media violation
                for SIP voice calls.
                
                If the value of this object is 'true',
                cvdcPolicyViolationNotification traps will be generated for SIP
                voice over IP peers when media violation condition is
                detected .  If the value of this object is 'false',
                cvdcPolicyViolationNotification traps will be generated only
                for calls for which the 
                cvVoIPPeerCfgMediaPolicyNotificationEnable object of voice
                over IP peers having set to 'true'.
                ''',
                'cvgeneralmediapolicynotificationenable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvGeneralPoorQoVNotificationEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether cvdcPoorQoVNotification (or
                the newer cvdcPoorQoVNotificationRev1) traps should be
                generated for a poor quality of voice calls.
                
                If the value of this object is 'true',
                cvdcPoorQoVNotification (or the newer
                cvdcPoorQoVNotificationRev1) traps will be generated
                for all voice over IP peers when a poor quality of voice
                call condition is detected after the voice gateway call
                disconnection.  If the value of this object is 'false',
                cvdcPoorQoVNotification (or the newer
                cvdcPoorQoVNotificationRev1) traps will be generated only
                for calls for which the
                cvVoIPPeerCfgPoorQoVNotificationEnable object of voice
                over IP peers having set to 'true'.
                ''',
                'cvgeneralpoorqovnotificationenable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvGeneralConfiguration',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvgatewaycallactive' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvgatewaycallactive',
            False, 
            [
            _MetaInfoClassMember('cvCallActiveDS0s', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The current number of DS0 interfaces used for the
                active calls.
                ''',
                'cvcallactiveds0s',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveDS0sHighNotifyEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specifies whether or not cvdcActiveDS0sHighNotification
                should be generated.
                
                'true' : Indicates that the cvdcActiveDS0sHighNotification
                         generation is enabled.
                
                'false': Indicates that cvdcActiveDS0sHighNotification
                         generation is disabled.
                ''',
                'cvcallactiveds0shighnotifyenable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveDS0sHighThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                A high threshold used to determine when to generate the
                cvdcActiveDS0sHighNotification. This object 
                represents the percentage of active DS0s in total number 
                of DS0s.
                ''',
                'cvcallactiveds0shighthreshold',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveDS0sLowNotifyEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specifies whether or not cvdcActiveDS0sLowNotification
                should be generated.
                
                'true' : Indicates that the cvdcActiveDS0sLowNotification
                         generation is enabled.
                
                'false': Indicates that cvdcActiveDS0sLowNotification
                         generation is disabled.
                ''',
                'cvcallactiveds0slownotifyenable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveDS0sLowThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                A low threshold used to determine when to generate the
                cvdcActiveDS0sLowNotification notification. This object 
                represents the percentage of active DS0s in total number 
                of DS0s.
                ''',
                'cvcallactiveds0slowthreshold',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvGatewayCallActive',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcallvolume' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcallvolume',
            False, 
            [
            _MetaInfoClassMember('cvCallVolConnMaxCallConnectionLicenese', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object represents the licensed call capacity
                for a voice gateway.  If the value is 0, no 
                licensing is done and the gateway can be 
                accomodate as many calls depending on its capability.
                ''',
                'cvcallvolconnmaxcallconnectionlicenese',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallVolConnTotalActiveConnections', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object represents the total number of
                active call legs in the voice gateway.
                ''',
                'cvcallvolconntotalactiveconnections',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallVolume',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcallratemonitor' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcallratemonitor',
            False, 
            [
            _MetaInfoClassMember('cvCallRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object represents the total number of
                calls handled by the gateway during the 
                monitored time.
                ''',
                'cvcallrate',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallRateHiWaterMark', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object represents the high water mark
                for the number of calls handled by the 
                gateway in an unit interval of 
                cvCallRateMonitorTime, from the time 
                the call-monitoring is enabled.
                ''',
                'cvcallratehiwatermark',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallRateMonitorEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object represents the state of call-monitoring.
                A value of 'true' indicates that call-monitoring 
                is enabled.  A value of 'false' indicates that 
                call-monitoring is disabled.
                ''',
                'cvcallratemonitorenable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallRateMonitorTime', ATTRIBUTE, 'int' , None, None, 
                [('1', '12')], [], 
                '''                This object represents the interval for
                which the gateway monitors the call-rate.
                ''',
                'cvcallratemonitortime',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallRateMonitor',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcallvolumestatshistory' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcallvolumestatshistory',
            False, 
            [
            _MetaInfoClassMember('cvCallDurationStatsThreshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                This Object specifies the thresold duration in seconds.
                cvCallDurationStatsTable will monitor all the calls below this 
                threshold.
                
                Decresing the value of the threshold will reset this table.
                ''',
                'cvcalldurationstatsthreshold',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallVolumeWMTableSize', ATTRIBUTE, 'int' , None, None, 
                [('3', '10')], [], 
                '''                This Object specifies the number of entries the watermark table
                will maintain.
                
                This value will decide the number of elements in
                cvCallRateWMTable,
                cvCallLegRateWMTable, cvActiveCallWMTable and
                cvSipMsgRateWMTable.
                ''',
                'cvcallvolumewmtablesize',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallVolumeStatsHistory',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvpeercfgtable.Cvpeercfgentry.CvpeercfgpeertypeEnum' : _MetaInfoEnum('CvpeercfgpeertypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB',
        {
            'voice':'voice',
            'data':'data',
        }, 'CISCO-VOICE-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB']),
    'CiscoVoiceDialControlMib.Cvpeercfgtable.Cvpeercfgentry.CvpeercfgtypeEnum' : _MetaInfoEnum('CvpeercfgtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB',
        {
            'voice':'voice',
            'voip':'voip',
            'mmail':'mmail',
            'voatm':'voatm',
            'vofr':'vofr',
        }, 'CISCO-VOICE-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB']),
    'CiscoVoiceDialControlMib.Cvpeercfgtable.Cvpeercfgentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvpeercfgtable.Cvpeercfgentry',
            False, 
            [
            _MetaInfoClassMember('cvPeerCfgIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                An arbitrary index that uniquely identifies a generic
                voice peer.
                ''',
                'cvpeercfgindex',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvCallVolPeerIncomingCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object represents the total number of
                active calls that has selected the dialpeer
                as an incoming dialpeer.
                ''',
                'cvcallvolpeerincomingcalls',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallVolPeerOutgoingCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object represents the total number of
                active calls that has selected the dialpeer
                as an outgoing dialpeer.
                ''',
                'cvcallvolpeeroutgoingcalls',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvPeerCfgIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The ifIndex of the peer associated ifEntry. The ifIndex
                appears after the associated ifEntry is created
                successfully.
                This ifIndex will be used to access the objects in the
                Voice over Telephony or Voice over IP peer specific table.
                In addition, the ifIndex is also used to access the
                associated peer configuration entry of the IETF Dial
                Control MIB. If the peer associated ifEntry had not been
                created, then this object has a value of zero.
                ''',
                'cvpeercfgifindex',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvPeerCfgPeerType', REFERENCE_ENUM_CLASS, 'CvpeercfgpeertypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvpeercfgtable.Cvpeercfgentry.CvpeercfgpeertypeEnum', 
                [], [], 
                '''                Specifies the type of a peer.
                voice - peer in voice type to be defined in a voice
                        gateway for voice calls. 
                data  - peer in data type to be defined in gateway
                        that supports universal ports for modem/data
                        calls and integrated ports for data calls.
                ''',
                'cvpeercfgpeertype',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvPeerCfgRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object is used to create a new row or modify or
                delete an existing row in this table.
                ''',
                'cvpeercfgrowstatus',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvPeerCfgType', REFERENCE_ENUM_CLASS, 'CvpeercfgtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvpeercfgtable.Cvpeercfgentry.CvpeercfgtypeEnum', 
                [], [], 
                '''                Specifies the type of voice related encapsulation.
                voice - voice encapsulation (voiceEncap ifType) on the
                        telephony network.
                voip  - VoIP encapsulation (voiceOverIp ifType) on the IP
                        network.
                mmail - Media Mail over IP encapsulation (mediaMailOverIp
                        ifType) on the IP network.
                voatm - VoATM encapsulation (voiceOverATM ifType) on the
                        ATM network.
                vofr  - VoFR encapsulation (voiceOverFR ifType) on the
                        Frame Relay network.
                ''',
                'cvpeercfgtype',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvPeerCfgEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvpeercfgtable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvpeercfgtable',
            False, 
            [
            _MetaInfoClassMember('cvPeerCfgEntry', REFERENCE_LIST, 'Cvpeercfgentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvpeercfgtable.Cvpeercfgentry', 
                [], [], 
                '''                A single voice generic Peer. The creation of this
                entry will create an associated ifEntry with an ifType
                that is associated with cvPeerCfgType, i.e., for
                'voiceEncap' encapsulation, an ifEntry will contain an
                ifType voiceEncap(103); for 'voiceOverIp' encapsulation,
                an ifEntry will contain an ifType voiceOverIp(104). The
                ifAdminStatus of the newly created ifEntry is set to 'up'
                and ifOperStatus is set to 'down'. In addition, an
                associated voiceEncap/voiceOverIp Peer configuration
                entry is created after the successful ifEntry creation.
                Then ifIndex of the newly created ifEntry must be used by
                the network manager to create a peer configuration entry
                of IETF Dial Control MIB (Refer to RFC 2128 section
                2.2.3.1 and the description of dialCtlPeerCfgEntry for the
                detailed information).
                In summary, the voice dial peer creation steps are as
                follows:
                [1] create this entry (voice/data generic peer entry).
                [2] read the cvPeerCfgIfIndex of this entry for the
                    ifIndex of newly created voice/data generic peer.
                [3] create the dialCtlPeerCfgEntry of RFC 2128 with the
                    indices of dialCtlPeerCfgId and the ifIndex of newly
                    created voice generic peer.
                
                For each VoIP peer, it uses IP address and UDP port with
                RTP protocol to transfer voice packet. Therefore, it does
                not have its lower layer interface. The
                dialCtlPeerCfgIfType object of IETF Dial Control MIB must
                set to 'other' and the dialCtlPeerCfgLowerIf must set to
                '0'.
                
                After the successful creation of peer configuration entry
                of IETF Dial Control MIB, the dial plan software in
                managed device will set the ifOperStatus of the newly
                created voiceEncap/voiceOverIp ifEntry to 'up' for
                enabling the peer function if the peer configuration is
                completed.
                When this entry is deleted, its associated ifEntry,
                voiceEncap/voiceOverIp specific peer entry and the peer
                entry of IETF Dial Control MIB are deleted.
                ''',
                'cvpeercfgentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvPeerCfgTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvvoicepeercfgtable.Cvvoicepeercfgentry.CvvoicepeercfgechocancellertestEnum' : _MetaInfoEnum('CvvoicepeercfgechocancellertestEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB',
        {
            'echoCancellerTestNone':'echoCancellerTestNone',
            'echoCancellerG168Test2A':'echoCancellerG168Test2A',
            'echoCancellerG168Test2B':'echoCancellerG168Test2B',
            'echoCancellerG168Test2Ca':'echoCancellerG168Test2Ca',
            'echoCancellerG168Test2Cb':'echoCancellerG168Test2Cb',
            'echoCancellerG168Test3A':'echoCancellerG168Test3A',
            'echoCancellerG168Test3B':'echoCancellerG168Test3B',
            'echoCancellerG168Test3C':'echoCancellerG168Test3C',
            'echoCancellerG168Test4':'echoCancellerG168Test4',
            'echoCancellerG168Test6':'echoCancellerG168Test6',
            'echoCancellerG168Test9':'echoCancellerG168Test9',
            'echoCancellerG168Test5':'echoCancellerG168Test5',
            'echoCancellerG168Test7':'echoCancellerG168Test7',
        }, 'CISCO-VOICE-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB']),
    'CiscoVoiceDialControlMib.Cvvoicepeercfgtable.Cvvoicepeercfgentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvvoicepeercfgtable.Cvvoicepeercfgentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvVoicePeerCfgCasGroup', ATTRIBUTE, 'int' , None, None, 
                [('-1', '30')], [], 
                '''                The object specifies the CAS group number of a CAS
                capable T1/E1  that is in the dialCtlPeerCfgLowerIf object
                of RFC2128.
                This object can be set to a valid CAS group number only if
                the dialCtlPeerCfgLowerIf contains a valid ifIndex for a
                CAS capable T1/E1. The object must set to -1 before the
                value of the  dialCtlPeerCfgLowerIf object of RFC2128 can
                be changed.
                ''',
                'cvvoicepeercfgcasgroup',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoicePeerCfgDialDigitsPrefix', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The object specifies the prefix of the dial digits for the
                peer. The dial digits prefix is sent to telephony
                interface before the real phone number when the system
                places the outgoing call to the voice encapsulation peer
                over telephony interface.
                ''',
                'cvvoicepeercfgdialdigitsprefix',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoicePeerCfgDIDCallEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The object enables/disables the DID call treatment for
                incoming DNIS digits.
                true  - treat the incoming DNIS digits as if the digits
                        are received from DID trunk.
                false - Disable DID call treatment for incoming DNIS
                        digits.
                ''',
                'cvvoicepeercfgdidcallenable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoicePeerCfgEchoCancellerTest', REFERENCE_ENUM_CLASS, 'CvvoicepeercfgechocancellertestEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvvoicepeercfgtable.Cvvoicepeercfgentry.CvvoicepeercfgechocancellertestEnum', 
                [], [], 
                '''                This object specifies which, if any, test to run in the
                echo canceller when a call from the network is connected.
                echoCancellerTestNone    - do not run a test.
                echoCancellerG168Test2A  - run ITU-T G.168 Test 2A.
                echoCancellerG168Test2B  - run ITU-T G.168 Test 2B.
                echoCancellerG168Test2Ca - run ITU-T G.168 Test 2C(a).
                echoCancellerG168Test2Cb - run ITU-T G.168 Test 2C(b).
                echoCancellerG168Test3A  - run ITU-T G.168 Test 3A.
                echoCancellerG168Test3B  - run ITU-T G.168 Test 3B.
                echoCancellerG168Test3C  - run ITU-T G.168 Test 3C.
                echoCancellerG168Test4   - run ITU-T G.168 Test 4.
                echoCancellerG168Test5   - run ITU-T G.168 Test 5.
                echoCancellerG168Test6   - run ITU-T G.168 Test 6.
                echoCancellerG168Test7   - run ITU-T G.168 Test 7.
                echoCancellerG168Test9   - run ITU-T G.168 Test 9.
                ''',
                'cvvoicepeercfgechocancellertest',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoicePeerCfgForwardDigits', ATTRIBUTE, 'int' , None, None, 
                [('-3', '32')], [], 
                '''                This object specifies the number of dialed digits to
                forward to the remote destination in the setup message.
                The object can take the value:
                    0-32 number of right justified digits to forward
                    -1 default
                    -2 forward extra digits i.e those over and above
                       those needed to match to the destination pattern
                    -3 forward all digits
                ''',
                'cvvoicepeercfgforwarddigits',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoicePeerCfgRegisterE164', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies that the E.164 number specified in
                the dialCtlPeerCfgOriginateAddress field of the associated
                dialCtlPeerCfgTable entry be registered as an extension 
                phone number of this gateway for H323 gatekeeper and/or 
                SIP registrar.
                ''',
                'cvvoicepeercfgregistere164',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoicePeerCfgSessionTarget', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The object specifies the session target of the peer.
                Session Targets definitions:
                The session target has the syntax used by the IETF service
                location protocol. The syntax is as follows:
                
                mapping-type:type-specific-syntax
                
                the mapping-type specifies a scheme for mapping the
                matching dial string to a session target.
                
                The valid Mapping type definitions for the peer are as
                follows:
                loopback - Syntax: loopback:where
                   'where' string is defined as follows:
                   compressed - loopback is performed on compressed voice
                                as close to the CODEC which processes the
                                data as possible.
                   uncompressed - loopback is performed on the PCM or
                                analog voice as close to the telephony
                                endpoint as possible.
                
                Local loopback case:
                uncompressed - the PCM voice coming into the DSP is simply
                    turned around and sent back out, allowing testing of
                    the transmit--> receive paths in the telephony
                    endpoint.
                compressed - the compressed voice coming out of the CODEC is
                    turned around on the DSP module and fed back into the
                    decompressor through the jitter buffer. In addition to
                    the telephony endpoint, this tests both the encode and
                    decode paths without involving data paths or packet
                    handling on the host router.
                
                Remote loopback case:
                compressed - RTP packets received from the network are
                    decapsulated and passed to the DSP board. Instead of
                    feeding these into the CODEC for decompression, they
                    are immediately sent back to the session application
                    as if they had originated locally and been compressed.
                uncompressed - In addition to the above, the voice samples
                    are sent all the way through the CODEC and then turned
                    around instead of being sent to the telephony
                    endpoint
                ''',
                'cvvoicepeercfgsessiontarget',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvVoicePeerCfgEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvvoicepeercfgtable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvvoicepeercfgtable',
            False, 
            [
            _MetaInfoClassMember('cvVoicePeerCfgEntry', REFERENCE_LIST, 'Cvvoicepeercfgentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvvoicepeercfgtable.Cvvoicepeercfgentry', 
                [], [], 
                '''                A single Voice specific Peer. One entry per voice
                encapsulation.
                The entry is created when its associated 'voiceEncap(103)'
                encapsulation ifEntry is created.
                This entry is deleted when its associated ifEntry is
                deleted.
                ''',
                'cvvoicepeercfgentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvVoicePeerCfgTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry.CvvoippeercfgcodingmodeEnum' : _MetaInfoEnum('CvvoippeercfgcodingmodeEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB',
        {
            'adaptive':'adaptive',
            'independent':'independent',
        }, 'CISCO-VOICE-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB']),
    'CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry.CvvoippeercfgframesizeEnum' : _MetaInfoEnum('CvvoippeercfgframesizeEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB',
        {
            'frameSize30':'frameSize30',
            'frameSize60':'frameSize60',
            'frameSize30fixed':'frameSize30fixed',
            'frameSize60fixed':'frameSize60fixed',
        }, 'CISCO-VOICE-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB']),
    'CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry.CvvoippeercfgmediasettingEnum' : _MetaInfoEnum('CvvoippeercfgmediasettingEnum', 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB',
        {
            'flowThrough':'flowThrough',
            'flowAround':'flowAround',
        }, 'CISCO-VOICE-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB']),
    'CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvVoIPPeerCfgBitRate', ATTRIBUTE, 'int' , None, None, 
                [('10000', '32000')], [], 
                '''                This object specifies the target bit rate. The object is
                instantiated only if cvVoIPPeerCfgCoderRate is 'iSAC'.
                ''',
                'cvvoippeercfgbitrate',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgBitRates', REFERENCE_BITS, 'Cvamrnbbitratemode' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'Cvamrnbbitratemode', 
                [], [], 
                '''                This object indicates modes of Bit rates. One or more
                upto four modes can be configured at the same time as
                bit rates can be changed dynamically for AMR-NB codec.
                This object is not instantiated when the object
                cvVoIPPeerCfgCoderRate is not equal to gsmAmrNb enum.
                ''',
                'cvvoippeercfgbitrates',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgCoderBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', 'None'), ('10', '240')], [], 
                '''                This object specifies the size of the voice payload sample
                to be produced by the coder specified in
                cvVoIPPeerCfgCoderRate.
                Each coder sample produces 10 bytes of voice payload. The
                specified value will be rounded down to the nearest valid
                size.
                
                A value of 0, specifies that the coder defined by
                cvVoIPPeerCfgCoderRate should produce its default payload
                size.
                ''',
                'cvvoippeercfgcoderbytes',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgCoderMode', REFERENCE_ENUM_CLASS, 'CvilbcframemodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CvilbcframemodeEnum', 
                [], [], 
                '''                This object indicates the iLBC codec mode to be used.
                The value of this object is valid only if 
                cvVoIPPeerCfgCoderRate is equal to 'iLBC'.
                ''',
                'cvvoippeercfgcodermode',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgCoderRate', REFERENCE_ENUM_CLASS, 'CvcspeechcoderrateEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CvcspeechcoderrateEnum', 
                [], [], 
                '''                This object specifies the most desirable codec of speech
                for the VoIP peer.
                ''',
                'cvvoippeercfgcoderrate',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgCodingMode', REFERENCE_ENUM_CLASS, 'CvvoippeercfgcodingmodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry.CvvoippeercfgcodingmodeEnum', 
                [], [], 
                '''                This object specifies the coding mode to be used. The object is
                instantiated only if cvVoIPPeerCfgCoderRate is 'iSAC'. Following
                coding modes are supported:
                adaptive    (1) - adaptive mode where iSAC performs bandwidth  
                                  estimation and adapts to the available channel
                
                                  bandwidth.
                independent (2) - independent mode in which no bandwidth
                estimation 
                                  is performed.
                ''',
                'cvvoippeercfgcodingmode',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgCRC', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the object has a value of true(1), frame CRC will be
                included in the payload and if the value is false(2),
                frame CRC will not be included in the payload.
                This object is applicable only when RTP frame type
                is octet aligned. This object is not instantiated when
                the object cvVoIPPeerCfgCoderRate is not equal to
                gsmAmrNb enum.
                ''',
                'cvvoippeercfgcrc',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgDesiredQoS', REFERENCE_ENUM_CLASS, 'QosserviceEnum' , 'ydk.models.cisco_ios_xe.INT_SERV_MIB', 'QosserviceEnum', 
                [], [], 
                '''                The object specifies the user requested Quality of Service
                for the call.
                ''',
                'cvvoippeercfgdesiredqos',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgDesiredQoSVideo', REFERENCE_ENUM_CLASS, 'QosserviceEnum' , 'ydk.models.cisco_ios_xe.INT_SERV_MIB', 'QosserviceEnum', 
                [], [], 
                '''                The object specifies the user requested Quality of Service
                for the video portion of the call.
                ''',
                'cvvoippeercfgdesiredqosvideo',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgDigitRelay', REFERENCE_BITS, 'Cvvoippeercfgdigitrelay' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry.Cvvoippeercfgdigitrelay', 
                [], [], 
                '''                This object specifies the methods to transmit dial digits
                (DTMF or MF digits) via IP network.
                rtpCisco       - Enable capability to transmit dial digits
                                 with Cisco proprietary RTP payload type.
                h245Signal     - Enable capability to transmit dtmf digits
                                 across the H.245 channel, via the signal
                                 field of the UserInputIndication message
                h245Alphanumeric - Enable capability to transmit dtmf
                                 digit across the H.245 channel, via the
                                 string or alphanumeric fields of the
                                 UserInputIndication message
                rtpNte         - Enable capability to transmit dial digits
                                 using Named Telephony Event per RFC 2833
                                 section 3.
                sipNotify      - Enable capability to transmit dtmf
                                 digits using unsolicited SIP NOTIFY
                                 messages. This mechanism is only available
                                 for SIP dialpeers.
                sipKpml        - Enable capability to transmit dtmf
                                 digits using KPML over SIP SUBSCRIBE
                                 and NOTIFY messages. This mechanism is
                                 only available for SIP dialpeers.
                
                
                Modifying the value of cvVoIPPeerCfgSessionProtocol
                can reset the digit-relay method associated bits value in
                this object if the modified session protocol does not
                support  these digit-relay methods.
                ''',
                'cvvoippeercfgdigitrelay',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgDSCPPolicyNotificationEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether cvdcPolicyViolationNotification
                traps should be generated for the call that is associated with
                this peer for RPH to DSCP mapping and policing feature.
                ''',
                'cvvoippeercfgdscppolicynotificationenable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgExpectFactor', ATTRIBUTE, 'int' , None, None, 
                [('0', '20')], [], 
                '''                This object specifies the user requested Expectation
                Factor of voice quality for the call via this peer.
                ''',
                'cvvoippeercfgexpectfactor',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgFaxBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', 'None'), ('10', '255')], [], 
                '''                This object specifies the payload size to be produced by
                the coder when it is generating fax data. A value of 0,
                specifies that the coder specified in
                cvVoIPCfgPeerCoderRate should produce its default fax
                payload size.
                ''',
                'cvvoippeercfgfaxbytes',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgFaxRate', REFERENCE_ENUM_CLASS, 'CvcfaxtransmitrateEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CvcfaxtransmitrateEnum', 
                [], [], 
                '''                This object specifies the default transmit rate of FAX
                the VoIP peer. If the value of this object is 'none',
                then the Fax relay feature is disabled; otherwise the Fax
                relay feature is enabled.
                ''',
                'cvvoippeercfgfaxrate',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgFrameSize', REFERENCE_ENUM_CLASS, 'CvvoippeercfgframesizeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry.CvvoippeercfgframesizeEnum', 
                [], [], 
                '''                This object specifies the frame size used. The object is
                instantiated only if cvVoIPPeerCfgCoderRate is 'iSAC'.
                The frame size can be 30 ms or 60 ms, and it can be fixed for
                all packets or vary depending on the configuration and bandwidth
                estimation. Thus it can have the following values:
                frameSize30      - initial frame size of 30 ms
                frameSize60      - initial frame size of 60 ms
                frameSize30fixed - fixed frame size 30 ms
                frameSize60fixed - fixed frame size 60 ms
                ''',
                'cvvoippeercfgframesize',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgIcpif', ATTRIBUTE, 'int' , None, None, 
                [('0', '55')], [], 
                '''                This object specifies the user requested Calculated
                Planning Impairment Factor (Icpif) for the call via this
                peer.
                ''',
                'cvvoippeercfgicpif',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgInBandSignaling', REFERENCE_ENUM_CLASS, 'CvcinbandsignalingEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CvcinbandsignalingEnum', 
                [], [], 
                '''                This object specifies the type of in-band signaling that
                will be used between the end points of the call. It is
                used by the router to determine how to interpret ABCD
                signaling bits sent as part of voice payload data.
                ''',
                'cvvoippeercfginbandsignaling',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgIPPrecedence', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                This object specifies the value to be stored in the IP
                Precedence field of voice packets, with values ranging
                from 0 (normal precedence) through 7 (network control),
                allowing the managed system to set the importance of each
                voice packet for delivering them to the destination peer.
                ''',
                'cvvoippeercfgipprecedence',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgMediaPolicyNotificationEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether cvdcPolicyViolationNotification
                traps should be generated for the call that is associated with
                this peer for Media policing feature..
                ''',
                'cvvoippeercfgmediapolicynotificationenable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgMediaSetting', REFERENCE_ENUM_CLASS, 'CvvoippeercfgmediasettingEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry.CvvoippeercfgmediasettingEnum', 
                [], [], 
                '''                This object specifies how the media is to be setup on
                an IP-IP Gateway. Two choices are valid: flow-through
                and flow-around. When in flow-through mode, which is the
                default setting, the IP-IP Gateway will terminate and 
                then re-originate the media stream. When flow-around
                is configured the Gateway will not be involved with the
                media, since it will flow-around the Gateway and will
                be established directly between the endpoints.
                ''',
                'cvvoippeercfgmediasetting',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgMinAcceptableQoS', REFERENCE_ENUM_CLASS, 'QosserviceEnum' , 'ydk.models.cisco_ios_xe.INT_SERV_MIB', 'QosserviceEnum', 
                [], [], 
                '''                The object specifies the minimally acceptable Quality of
                Service for the call.
                ''',
                'cvvoippeercfgminacceptableqos',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgMinAcceptableQoSVideo', REFERENCE_ENUM_CLASS, 'QosserviceEnum' , 'ydk.models.cisco_ios_xe.INT_SERV_MIB', 'QosserviceEnum', 
                [], [], 
                '''                The object specifies the minimally acceptable Quality of
                Service for the video portion of the call.
                ''',
                'cvvoippeercfgminacceptableqosvideo',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgOctetAligned', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the object has a value true(1) octet align operation
                is used, and if the value is false(2), bandwidth efficient
                operation is used. This object is not instantiated when
                the object cvVoIPPeerCfgCoderRate is not equal to
                gsmAmrNb enum.
                ''',
                'cvvoippeercfgoctetaligned',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgPoorQoVNotificationEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether cvdcPoorQoVNotification (or
                the newer cvdcPoorQoVNotificationRev1) traps should be
                generated for the call that is associated with this
                peer.
                ''',
                'cvvoippeercfgpoorqovnotificationenable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgRedirectip2ip', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies the Inbound VoIP calls that match
                an outbound VoIP dialpeer will be responded with a SIP 
                redirect(for inbound SIP) or H.450.3 call-forward(for 
                inbound H.323).
                ''',
                'cvvoippeercfgredirectip2ip',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgSessionProtocol', REFERENCE_ENUM_CLASS, 'CvsessionprotocolEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CvsessionprotocolEnum', 
                [], [], 
                '''                The object specifies the session protocol to be used
                for Internet call between local and remote router via
                IP backbone.
                ''',
                'cvvoippeercfgsessionprotocol',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgSessionTarget', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The object specifies the session target of the peer.
                Session Targets definitions:
                The session target has the syntax used by the IETF service
                location protocol. The syntax is as follows:
                
                mapping-type:type-specific-syntax
                
                the mapping-type specifies a scheme for mapping the
                matching dial string to a session target. The
                type-specific-syntax is exactly that, something that the
                particular mapping scheme can understand.
                For example,
                Session target           Meaning
                ipv4:171.68.13.55:1006   The session target is the IP
                                         version 4 address of 171.68.13.55
                                         and port 1006.
                dns:pots.cisco.com:1661  The session target is the IP host
                                         with dns name pots.cisco.com, and
                                         port 1661.
                ras                      The session target is the
                                         gatekeeper with RAS (Registration
                                         , Admission,  Status protocol).
                settlement               The session target is the
                                         settlement server.
                enum:1                   The session target is the enum 
                                         profile match table 1.
                
                The valid Mapping type definitions for the peer are as
                follows:
                ipv4       - Syntax: ipv4:w.x.y.z:port or  ipv4:w.x.y.z
                dns        - Syntax: dns:host.domain:port or
                                     dns:host.domain
                ras        - Syntax: ras
                settlement - Syntax: settlement
                enum       - Syntax: enum:
                
                loopback - Syntax: loopback:where
                   'where' string is defined as follows:
                   rtp - loopback is performed at the transport protocol
                         level.
                
                Local loopback case:
                rtp - the session application sets up an RTP stream to
                    itself (i.e. actually allocates a port pair and opens
                    the appropriate UDP sockets). It then does the full
                    RTP encapsulation, sends the packets to the loopback
                    IP address, receives the RTP packets, and hands the
                    compressed voice back to the CODEC. This tests the
                    entire local processing path, both transmit and
                    receive, in the router, as well as all of the above
                    paths.
                
                Remote loopback case:
                rtp: RTP packets received from the network are decapsulated and
                     immediately re-encapsulated in the outbound RTP
                     stream, using the same media clock (i.e. timestamp)
                     as the received packet. They are then sent back to
                     the remote source router as if the voice had
                     originated on a telephony port on the local router.
                ''',
                'cvvoippeercfgsessiontarget',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgTechPrefix', ATTRIBUTE, 'str' , None, None, 
                [(0, 128)], [], 
                '''                This object specifies the technology prefix of the peer,
                The technology prefix and the called party address
                are passed in Admission Request (ARQ) to gatekeeper
                for the called party address resolution during call setup.
                ''',
                'cvvoippeercfgtechprefix',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgUDPChecksumEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the outgoing voice related
                UDP packet contains a valid checksum value.
                true  - enable the checksum of outgoing voice UDP packets
                false - disable the checksum of outgoing voice UDP packets
                ''',
                'cvvoippeercfgudpchecksumenable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgVADEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether or not the VAD (Voice
                Activity Detection) voice data is continuously transmitted
                to IP backbone.
                ''',
                'cvvoippeercfgvadenable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvVoIPPeerCfgEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvvoippeercfgtable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvvoippeercfgtable',
            False, 
            [
            _MetaInfoClassMember('cvVoIPPeerCfgEntry', REFERENCE_LIST, 'Cvvoippeercfgentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry', 
                [], [], 
                '''                A single VoIP specific Peer. One entry per VoIP
                encapsulation.
                The entry is created when its associated 'voiceOverIp(104)'
                encapsulation ifEntry is created.
                This entry is deleted when its associated ifEntry is
                deleted.
                ''',
                'cvvoippeercfgentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvVoIPPeerCfgTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvpeercommoncfgtable.Cvpeercommoncfgentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvpeercommoncfgtable.Cvpeercommoncfgentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvPeerCommonCfgApplicationName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The object specifies the application to handle the incoming
                call after the peer is selected.
                If no application name is specified, then the default
                session application will take care of the incoming call.
                ''',
                'cvpeercommoncfgapplicationname',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvPeerCommonCfgDnisMappingName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The object specifies a Dialer Number Identification
                Service (DNIS) map name for the Voice specific peer
                entry specified in this row. A DNIS is a called party
                number and they can be grouped and identified by DNIS
                map.
                ''',
                'cvpeercommoncfgdnismappingname',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvPeerCommonCfgHuntStop', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether dialpeer hunting should stop
                when this peer is reached.
                ''',
                'cvpeercommoncfghuntstop',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvPeerCommonCfgIncomingDnisDigits', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The object specifies the prefix of the incoming Dialed
                Number Identification Service (DNIS) digits for the peer.
                The DNIS digits prefix is used to match with the incoming
                DNIS number for incoming call discrimination. If the
                digits in this object are matched with incoming DNIS
                number, the  associated dialCtlPeerCfgInfoType in RFC 2128
                will be used as a call discriminator for differentiating
                speech, data, fax, video or modem calls.
                ''',
                'cvpeercommoncfgincomingdnisdigits',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvPeerCommonCfgMaxConnections', ATTRIBUTE, 'int' , None, None, 
                [('-1', 'None'), ('1', '2147483647')], [], 
                '''                The object specifies the maximum allowed connection
                to/from the peer. A value of -1 disables the limit of
                maximum connections.
                ''',
                'cvpeercommoncfgmaxconnections',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvPeerCommonCfgPreference', ATTRIBUTE, 'int' , None, None, 
                [('0', '10')], [], 
                '''                This object specifies the selection preference of a peer
                when multiple peers are matched to the selection criteria.
                The value of 0 has the lowest preference for peer
                selection.
                ''',
                'cvpeercommoncfgpreference',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvPeerCommonCfgSourceCarrierId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The object specifies the Source Carrier Id for the peer.
                The Source Carrier Id is used to match with the Source
                Carrier Id of a call. If the Source Carrier Id in this
                object is matched with the Source Carrier Id of a call,
                then the associated peer will be used to handle the call. 
                Only alphanumeric characters, '-' and '_' are allowed in
                the string.
                ''',
                'cvpeercommoncfgsourcecarrierid',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvPeerCommonCfgSourceTrunkGrpLabel', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The object specifies the Source Trunk Group Label for the
                peer. The Source Trunk Group Label is used to match with
                the Source Trunk Group Label of a call. If the Source
                Trunk Group Label in this object is matched with the
                Source Trunk Group Label of a call, then the associated
                peer will be used to handle the call. 
                Only alphanumeric characters, '-' and '_' are allowed in
                the string.
                ''',
                'cvpeercommoncfgsourcetrunkgrplabel',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvPeerCommonCfgTargetCarrierId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The object specifies the Target Carrier Id for the peer.
                The Target Carrier Id is used to match with the Target
                Carrier Id of a call. If the Target Carrier Id in this
                object is matched with the Target Carrier Id of a call,
                then the associated peer will be used to handle the call.
                Only alphanumeric characters, '-' and '_' are allowed in
                the string.
                ''',
                'cvpeercommoncfgtargetcarrierid',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvPeerCommonCfgTargetTrunkGrpLabel', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The object specifies the Target Trunk Group Label for the
                peer. The Target Trunk Group Label is used to match with
                the Target Trunk Group Label of a call. If the Target
                Trunk Group Label in this object is matched with the
                Target Trunk Group Label of a call, then the associated
                peer will be used to handle the call.
                Only alphanumeric characters, '-' and '_' are allowed in
                the string.
                ''',
                'cvpeercommoncfgtargettrunkgrplabel',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvPeerCommonCfgEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvpeercommoncfgtable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvpeercommoncfgtable',
            False, 
            [
            _MetaInfoClassMember('cvPeerCommonCfgEntry', REFERENCE_LIST, 'Cvpeercommoncfgentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvpeercommoncfgtable.Cvpeercommoncfgentry', 
                [], [], 
                '''                A single Voice specific Peer. One entry per voice related
                encapsulation.
                The entry is created when a voice related encapsulation
                ifEntry is created.
                This entry is deleted when its associated ifEntry is
                deleted.
                ''',
                'cvpeercommoncfgentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvPeerCommonCfgTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcallactivetable.Cvcallactiveentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcallactivetable.Cvcallactiveentry',
            False, 
            [
            _MetaInfoClassMember('callActiveSetupTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'callactivesetuptime',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('callActiveIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'callactiveindex',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvCallActiveAccountCode', ATTRIBUTE, 'str' , None, None, 
                [(0, 50)], [], 
                '''                The object indicates the account code input to the call.
                It could be used for call screen or by down stream server
                for billing purpose.
                The value of empty string indicates no account code input.
                ''',
                'cvcallactiveaccountcode',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveACOMLevel', ATTRIBUTE, 'int' , None, None, 
                [('-1', '127')], [], 
                '''                The object contains the sum of Echo Return Loss (ERL),
                cancellation loss (Echo Return Loss Enhancement) and
                nonlinear processing loss for the call leg.
                The value -1 indicates the level can not be determined or
                level detection is disabled.
                ''',
                'cvcallactiveacomlevel',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveCallerIDBlock', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The object indicates whether or not the caller ID feature
                is blocked for this call.
                ''',
                'cvcallactivecalleridblock',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveCallId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object represents the call identifier
                for the active telephony leg of the call.
                ''',
                'cvcallactivecallid',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveCallingName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The calling party name of the call. If the name is
                not available, then it will have a length of zero.
                ''',
                'cvcallactivecallingname',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveCoderTypeRate', REFERENCE_ENUM_CLASS, 'CvccodertyperateEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CvccodertyperateEnum', 
                [], [], 
                '''                The negotiated coder rate. It specifies the transmit rate of
                voice/fax compression to its associated call leg for the
                call.
                ''',
                'cvcallactivecodertyperate',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveConnectionId', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                The global connection identifier for the
                active telephony leg of the call.
                ''',
                'cvcallactiveconnectionid',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveEcanReflectorLocation', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                The location in milliseconds of the largest amplitude
                reflector detected by the echo canceller for this call. 
                The value 0 indicates there is no reflector or the 
                information is not available.
                ''',
                'cvcallactiveecanreflectorlocation',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveERLLevel', ATTRIBUTE, 'int' , None, None, 
                [('-1', '45')], [], 
                '''                The object contains the current Echo Return Loss (ERL)
                level for the call leg.
                The value -1 indicates the level can not be determined or
                level detection is disabled.
                ''',
                'cvcallactiveerllevel',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveERLLevelRev1', ATTRIBUTE, 'int' , None, None, 
                [('-1', '200')], [], 
                '''                The object contains the current Echo Return Loss (ERL)
                level for the call leg.
                The value -1 indicates the level can not be determined or
                level detection is disabled.
                ''',
                'cvcallactiveerllevelrev1',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveFaxTxDuration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duration of fax transmitted from this peer to voice gateway
                for this call leg. The FAX Utilization Rate can be
                obtained by dividing this by cvCallActiveTXDuration
                object. This counter object will lock at the maximum
                value which is approximately two days.
                ''',
                'cvcallactivefaxtxduration',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveImgPageCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of FAX related image pages are received or
                transmitted via the peer for the call leg.
                ''',
                'cvcallactiveimgpagecount',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveInSignalLevel', ATTRIBUTE, 'int' , None, None, 
                [('-128', '8')], [], 
                '''                The object contains the active input signal level from
                telephony interface that is used by the call leg.
                ''',
                'cvcallactiveinsignallevel',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveNoiseLevel', ATTRIBUTE, 'int' , None, None, 
                [('-128', '8')], [], 
                '''                The object contains the active noise level for the call
                leg.
                ''',
                'cvcallactivenoiselevel',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveOutSignalLevel', ATTRIBUTE, 'int' , None, None, 
                [('-128', '8')], [], 
                '''                The object contains the active output signal level to
                telephony interface that is used by the call leg.
                ''',
                'cvcallactiveoutsignallevel',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveSessionTarget', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The object specifies the session target of the peer that
                is used for the call leg. This object is set with the
                information in the call associated
                cvVoicePeerCfgSessionTarget object when the call is
                connected.
                ''',
                'cvcallactivesessiontarget',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveTxDuration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duration of Transmit path open from this peer to the
                voice gateway for the call leg. This counter object will
                lock at the maximum value which is approximately two
                days.
                ''',
                'cvcallactivetxduration',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveVoiceTxDuration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duration of voice transmitted from this peer to voice
                gateway for this call leg. The Voice Utilization Rate can
                be obtained by dividing this by cvCallActiveTXDuration
                object. This counter object will lock at the maximum
                value which is approximately two days.
                ''',
                'cvcallactivevoicetxduration',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallActiveEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcallactivetable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcallactivetable',
            False, 
            [
            _MetaInfoClassMember('cvCallActiveEntry', REFERENCE_LIST, 'Cvcallactiveentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcallactivetable.Cvcallactiveentry', 
                [], [], 
                '''                The information regarding a single voice encapsulation
                call leg.
                The call leg entry is identified by using the same index
                objects that are used by Call Active table of IETF Dial
                Control MIB to identify the call.
                An entry of this table is created when its associated call
                active entry in the IETF Dial Control MIB is created and
                call active entry contains the call establishment to a
                voice over telephony network peer.
                The entry is deleted when its associated call active entry
                in the IETF Dial Control MIB is deleted.
                ''',
                'cvcallactiveentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallActiveTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvvoipcallactivetable.Cvvoipcallactiveentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvvoipcallactivetable.Cvvoipcallactiveentry',
            False, 
            [
            _MetaInfoClassMember('callActiveSetupTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'callactivesetuptime',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('callActiveIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'callactiveindex',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('ccVoIPCallActivePolicyName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object holds the policy name. It could be media
                policy, DSCP policy etc.
                ''',
                'ccvoipcallactivepolicyname',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveBitRates', REFERENCE_BITS, 'Cvamrnbbitratemode' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'Cvamrnbbitratemode', 
                [], [], 
                '''                This object indicates modes of Bit rates.
                This object is not instantiated when the object
                cvVoIPCallActiveCoderTypeRate is not equal to
                gsmAmrNb enum.
                ''',
                'cvvoipcallactivebitrates',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveCallId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object represents the call identifier
                for the active VoIP leg of the call.
                ''',
                'cvvoipcallactivecallid',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveCallReferenceId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The call reference ID associates the video call entry and voice
                call entry of the same endpoint.  An audio-only call may or may
                not have a valid call reference ID (i.e. value greater than
                zero), but in both cases, there will not be a video call entry
                associated with it.  
                
                For a video call, the video-specific information  is stored in a
                call entry in cVideoSessionActive of CISCO-VIDEO-SESSION-MIB, in
                which the call reference ID is also identified.
                ''',
                'cvvoipcallactivecallreferenceid',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveChannels', ATTRIBUTE, 'int' , None, None, 
                [('1', '6')], [], 
                '''                The object indicates the number of audio channels.
                Supported value is 1. This object is not instantiated
                when the object cvVoIPCallActiveCoderTypeRate is not equal
                to gsmAmrNb enum.
                ''',
                'cvvoipcallactivechannels',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveCoderMode', REFERENCE_ENUM_CLASS, 'CvilbcframemodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CvilbcframemodeEnum', 
                [], [], 
                '''                The object indicates the iLBC codec mode.
                The value of this object is valid only if 
                cvVoIPCallActiveCoderTypeRate is equal to 
                'iLBC'.
                ''',
                'cvvoipcallactivecodermode',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveCoderTypeRate', REFERENCE_ENUM_CLASS, 'CvccodertyperateEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CvccodertyperateEnum', 
                [], [], 
                '''                The negotiated coder rate. It specifies the transmit rate of
                voice/fax compression to its associated call leg for the
                call. This rate is different from the configuration rate
                because of rate negotiation during the call.
                ''',
                'cvvoipcallactivecodertyperate',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveConnectionId', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                The global connection identifier for
                the active VoIP leg of the call.
                ''',
                'cvvoipcallactiveconnectionid',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveCRC', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the object has a value of true(1), frame CRC will be
                included in the payload and if the value is false(2),
                frame CRC will not be included in the payload.
                This object is applicable only when RTP frame type
                is octet aligned. This object is not instantiated when
                the object cvVoIPCallActiveCoderTypeRate is not equal to
                gsmAmrNb enum.
                ''',
                'cvvoipcallactivecrc',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveEarlyPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of received voice packets that
                arrived too early to store in jitter buffer
                during the call.
                ''',
                'cvvoipcallactiveearlypackets',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveEncap', REFERENCE_ENUM_CLASS, 'CvamrnbrtpencapEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CvamrnbrtpencapEnum', 
                [], [], 
                '''                The object indicates the RTP encapsulation type.
                Supported RTP encapsulation type is RFC3267.
                This object is not instantiated when the object
                cvVoIPCallActiveCoderTypeRate is not equal to
                gsmAmrNb enum.
                ''',
                'cvvoipcallactiveencap',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveGapFillWithInterpolation', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duration of voice signal played out with signal synthesized
                from parameters or samples of data preceding and following
                in time due to voice data not received on time (or lost)
                from voice gateway for this call. This counter object
                will lock at the maximum value which is approximately two
                days.
                ''',
                'cvvoipcallactivegapfillwithinterpolation',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveGapFillWithPrediction', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duration of voice signal played out with signal synthesized
                from parameters or samples of data preceding in time due
                to voice data not received on time (or lost) from voice
                gateway for this call. An example of such playout is
                frame-erasure or frame-concealment strategies in G.729 and
                G.723.1 compression algorithms. This counter object will
                lock at the maximum value which is approximately two days.
                ''',
                'cvvoipcallactivegapfillwithprediction',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveGapFillWithRedundancy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duration of voice signal played out with signal synthesized
                from redundancy parameters available due to voice data not
                received on time (or lost) from voice gateway for this call.
                This counter object will lock at the maximum value which
                is approximately two days.
                ''',
                'cvvoipcallactivegapfillwithredundancy',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveGapFillWithSilence', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duration of voice signal replaced with signal played out
                during silence due to voice data not received on time
                (or lost) from voice gateway this call. This counter
                object will lock at the maximum value which is
                approximately two days.
                ''',
                'cvvoipcallactivegapfillwithsilence',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveHiWaterPlayoutDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The high water mark Voice Playout FIFO Delay during
                the voice call. This counter object will lock at the
                maximum value which is approximately two days.
                ''',
                'cvvoipcallactivehiwaterplayoutdelay',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveInterleaving', ATTRIBUTE, 'int' , None, None, 
                [('1', '50')], [], 
                '''                The object indicates the maximum number of frame-blocks
                allowed in an interleaving group. It indicates that
                frame-block level interleaving will be used for that
                session. If this object is not set, interleaving
                is not used. This object is applicable only when
                RTP frame type is octet aligned. This object is not
                instantiated when the object cvVoIPCallActiveCoderTypeRate
                is not equal to gsmAmrNb enum.
                ''',
                'cvvoipcallactiveinterleaving',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveLatePackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of received voice packets that
                arrived too late to playout with CODEC (Coder/Decoder)
                during the call.
                ''',
                'cvvoipcallactivelatepackets',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveLostPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of lost voice packets during the call.
                ''',
                'cvvoipcallactivelostpackets',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveLoWaterPlayoutDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The low water mark Voice Playout FIFO Delay during
                the voice call.
                ''',
                'cvvoipcallactivelowaterplayoutdelay',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveMaxPtime', ATTRIBUTE, 'int' , None, None, 
                [('20', '100')], [], 
                '''                The object indicates the maximum amount of media that
                can be encapsulated in a payload. Supported value is
                20 msec. This object is not instantiated when the
                object cvVoIPCallActiveCoderTypeRate is not equal to
                gsmAmrNb enum.
                ''',
                'cvvoipcallactivemaxptime',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveModeChgNeighbor', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the object has a value of true(1), mode changes will be
                made to only neighboring modes set to
                cvVoIPCallActiveBitRates object. If the value is false(2),
                mode changes will be allowed to any modes set to
                cvVoIPCallActiveBitRates object. This object is not
                instantiated when the object cvVoIPCallActiveCoderTypeRate
                is not equal to gsmAmrNb enum.
                ''',
                'cvvoipcallactivemodechgneighbor',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveModeChgPeriod', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                The object indicates the interval (N frame-blocks) at which
                codec mode changes are allowed. This object is not
                instantiated when the object cvVoIPCallActiveCoderTypeRate
                is not equal to gsmAmrNb enum.
                ''',
                'cvvoipcallactivemodechgperiod',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveOctetAligned', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the object has a value true(1) octet align operation
                is used, and if the value is false(2), bandwidth efficient
                operation is used. This object is not instantiated when
                the object cvVoIPCallActiveCoderTypeRate is not equal to
                gsmAmrNb enum.
                ''',
                'cvvoipcallactiveoctetaligned',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveOnTimeRvPlayout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duration of voice playout from data received on time for
                this call. This plus the durations for the GapFills in the
                following entries gives the Total Voice Playout Duration
                for Active Voice.
                This does not include duration for which no data was sent by the
                Transmit end as voice signal, e.g., silence suppression
                and fax signal. The On Time Playout Rate can be computed
                by dividing this entry by the Total Voice Playout Duration.
                This counter object will lock at the maximum value which
                is approximately two days.
                ''',
                'cvvoipcallactiveontimervplayout',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveProtocolCallId', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The protocol-specific call identifier for the VoIP call.
                ''',
                'cvvoipcallactiveprotocolcallid',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActivePtime', ATTRIBUTE, 'int' , None, None, 
                [('20', '100')], [], 
                '''                The object indicates the length of the time in milliseconds
                represented by the media of the packet. Supported value is
                20 milliseconds. This object is not instantiated when the
                object cvVoIPCallActiveCoderTypeRate is not equal to
                gsmAmrNb enum.
                ''',
                'cvvoipcallactiveptime',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveReceiveDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The average Playout FIFO Delay plus the decoder delay
                during the voice call.
                ''',
                'cvvoipcallactivereceivedelay',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveRemMediaIPAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Remote media end point IP address for the VoIP call.
                ''',
                'cvvoipcallactiveremmediaipaddr',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveRemMediaIPAddrT', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object specifies the type of address contained in
                the associated instance of
                cvVoIPCallActiveRemMediaIPAddr.
                ''',
                'cvvoipcallactiveremmediaipaddrt',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveRemMediaPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remote media end point listener port to which to transmit
                voice packets.
                ''',
                'cvvoipcallactiveremmediaport',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveRemoteIPAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote system IP address for the VoIP call.
                ''',
                'cvvoipcallactiveremoteipaddress',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveRemoteUDPPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remote system UDP listener port to which to transmit voice
                packets.
                ''',
                'cvvoipcallactiveremoteudpport',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveRemSigIPAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Remote signalling IP address for the VoIP call.
                ''',
                'cvvoipcallactiveremsigipaddr',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveRemSigIPAddrT', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object specifies the type of address contained in
                the associated instance of cvVoIPCallActiveRemSigIPAddr.
                ''',
                'cvvoipcallactiveremsigipaddrt',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveRemSigPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remote signalling listener port to which to transmit
                voice packets.
                ''',
                'cvvoipcallactiveremsigport',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveReversedDirectionPeerAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object store the reversed direction peer address  If the
                address is not available, then it will have a length of zero.
                
                If the call is ingress then it contains called number and if the
                call is egress then it contains calling number.
                ''',
                'cvvoipcallactivereverseddirectionpeeraddress',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveRobustSorting', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the object has a value of true(1), payload employs
                robust sorting and if the value is false(2), payload
                does not employ robust sorting. This object is applicable
                only when RTP frame type is octet aligned. This object
                is not instantiated when the object
                cvVoIPCallActiveCoderTypeRate is not equal to gsmAmrNb
                enum.
                ''',
                'cvvoipcallactiverobustsorting',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveRoundTripDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The voice packet round trip delay between local and
                the remote system on the IP backbone during the call.
                ''',
                'cvvoipcallactiveroundtripdelay',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveSelectedQoS', REFERENCE_ENUM_CLASS, 'QosserviceEnum' , 'ydk.models.cisco_ios_xe.INT_SERV_MIB', 'QosserviceEnum', 
                [], [], 
                '''                The selected RSVP QoS for the voice call.
                ''',
                'cvvoipcallactiveselectedqos',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveSessionId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the active session ID assigned by the
                call manager to identify call legs that belong to the same call
                session.
                ''',
                'cvvoipcallactivesessionid',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveSessionProtocol', REFERENCE_ENUM_CLASS, 'CvsessionprotocolEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CvsessionprotocolEnum', 
                [], [], 
                '''                The object specifies the session protocol to be used
                for Internet call between local and remote router via
                IP backbone.
                ''',
                'cvvoipcallactivesessionprotocol',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveSessionTarget', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The object specifies the session target of the peer that
                is used for the call. This object is set with the
                information in the call associated
                cvVoIPPeerCfgSessionTarget object when the voice over IP
                call is connected.
                ''',
                'cvvoipcallactivesessiontarget',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveSRTPEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The object indicates whether or not the SRTP (Secured RTP)
                was enabled for the voice call.
                ''',
                'cvvoipcallactivesrtpenable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveUsername', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                The textual identifier of the calling party (user) of the
                call. If the username is not available, then the value of
                this object will have a length of zero.
                ''',
                'cvvoipcallactiveusername',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveVADEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The object indicates whether or not the VAD (Voice Activity
                Detection) was enabled for the voice call.
                ''',
                'cvvoipcallactivevadenable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvVoIPCallActiveEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvvoipcallactivetable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvvoipcallactivetable',
            False, 
            [
            _MetaInfoClassMember('cvVoIPCallActiveEntry', REFERENCE_LIST, 'Cvvoipcallactiveentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvvoipcallactivetable.Cvvoipcallactiveentry', 
                [], [], 
                '''                The information regarding a single VoIP call leg.
                The call leg entry is identified by using the same index
                objects that are used by Call Active table of IETF Dial
                Control MIB to identify the call.
                An entry of this table is created when its associated call
                active entry in the IETF Dial Control MIB is created and
                the call active entry contains information for the call
                establishment to the peer on the IP backbone via a voice
                over  IP peer.
                The entry is deleted when its associated call active entry
                in the IETF Dial Control MIB is deleted.
                ''',
                'cvvoipcallactiveentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvVoIPCallActiveTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcallvolconntable.Cvcallvolconnentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcallvolconntable.Cvcallvolconnentry',
            False, 
            [
            _MetaInfoClassMember('cvCallVolConnIndex', REFERENCE_ENUM_CLASS, 'CvcallconnectiontypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CvcallconnectiontypeEnum', 
                [], [], 
                '''                This object represents index to the
                cvCallVolConnTable.
                ''',
                'cvcallvolconnindex',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvCallVolConnActiveConnection', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object represents the total number of
                active calls for a connection type 
                in the voice gateway.
                ''',
                'cvcallvolconnactiveconnection',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallVolConnEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcallvolconntable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcallvolconntable',
            False, 
            [
            _MetaInfoClassMember('cvCallVolConnEntry', REFERENCE_LIST, 'Cvcallvolconnentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcallvolconntable.Cvcallvolconnentry', 
                [], [], 
                '''                An entry in the cvCallVolConnTable indicates
                number of active calls for a call connection type
                in the voice gateway.
                ''',
                'cvcallvolconnentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallVolConnTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcallvoliftable.Cvcallvolifentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcallvoliftable.Cvcallvolifentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvCallVolMediaIncomingCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object represents the total number of
                inbound active media calls through this IP 
                interface.
                ''',
                'cvcallvolmediaincomingcalls',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallVolMediaOutgoingCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object represents the total number of
                outbound active media calls through the IP 
                interface.
                ''',
                'cvcallvolmediaoutgoingcalls',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallVolIfEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcallvoliftable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcallvoliftable',
            False, 
            [
            _MetaInfoClassMember('cvCallVolIfEntry', REFERENCE_LIST, 'Cvcallvolifentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcallvoliftable.Cvcallvolifentry', 
                [], [], 
                '''                Each entry represents a row in cvCallVolIfTable
                and corresponds to the information about an IP 
                interface in the voice gateway.
                ''',
                'cvcallvolifentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallVolIfTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcallhistorytable.Cvcallhistoryentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcallhistorytable.Cvcallhistoryentry',
            False, 
            [
            _MetaInfoClassMember('cCallHistoryIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'ccallhistoryindex',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvCallHistoryAccountCode', ATTRIBUTE, 'str' , None, None, 
                [(0, 50)], [], 
                '''                The object indicates the account code input to the call.
                It could be used by down stream billing server.
                The value of empty string indicates no account code input.
                ''',
                'cvcallhistoryaccountcode',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallHistoryACOMLevel', ATTRIBUTE, 'int' , None, None, 
                [('-1', '127')], [], 
                '''                The object contains the average ACOM level for the call
                leg. The value -1 indicates the level can not be
                determined or level detection is disabled.
                ''',
                'cvcallhistoryacomlevel',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallHistoryCallerIDBlock', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The object indicates whether or not the caller ID feature
                is blocked for this call.
                ''',
                'cvcallhistorycalleridblock',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallHistoryCallId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object represents the call identifier for the
                telephony leg, which was assigned to the call.
                ''',
                'cvcallhistorycallid',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallHistoryCallingName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The calling party name of the call. If the name is
                not available, then it will have a length of zero.
                ''',
                'cvcallhistorycallingname',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallHistoryCoderTypeRate', REFERENCE_ENUM_CLASS, 'CvccodertyperateEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CvccodertyperateEnum', 
                [], [], 
                '''                The negotiated coder rate. It specifies the transmit rate
                of voice/fax compression to its associated call leg for
                the call.
                ''',
                'cvcallhistorycodertyperate',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallHistoryConnectionId', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                The global connection identifier for the
                telephony leg, which was assigned to the call.
                ''',
                'cvcallhistoryconnectionid',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallHistoryFaxTxDuration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duration of fax transmitted from this peer to voice
                gateway for this call leg. The FAX Utilization Rate can be
                obtained by dividing this by cvCallHistoryTXDuration
                object. This counter object will lock at the maximum
                value which is approximately two days.
                ''',
                'cvcallhistoryfaxtxduration',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallHistoryImgPageCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of FAX related image pages are received or
                transmitted via the peer for the call leg.
                ''',
                'cvcallhistoryimgpagecount',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallHistoryNoiseLevel', ATTRIBUTE, 'int' , None, None, 
                [('-128', '8')], [], 
                '''                The object contains the average noise level for the call
                leg.
                ''',
                'cvcallhistorynoiselevel',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallHistorySessionTarget', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The object specifies the session target of the peer that
                is used for the call leg via telephony interface.
                ''',
                'cvcallhistorysessiontarget',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallHistoryTxDuration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duration of Transmit path open from this peer to the
                voice gateway for the call leg. This counter object will
                lock at the maximum value which is approximately two
                days.
                ''',
                'cvcallhistorytxduration',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallHistoryVoiceTxDuration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duration for this call leg. The Voice Utilization Rate
                can be obtained by dividing this by
                cvCallHistoryTXDuration object. This counter object will
                lock at the maximum value which is approximately two
                days.
                ''',
                'cvcallhistoryvoicetxduration',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallHistoryEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcallhistorytable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcallhistorytable',
            False, 
            [
            _MetaInfoClassMember('cvCallHistoryEntry', REFERENCE_LIST, 'Cvcallhistoryentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcallhistorytable.Cvcallhistoryentry', 
                [], [], 
                '''                The information regarding a single voice encapsulation
                call leg.
                The call leg entry is identified by using the same index
                objects that are used by Call Active table of IETF Dial
                Control MIB to identify the call.
                An entry of this table is created when its associated call
                history entry in the IETF Dial Control MIB is created and
                the call history entry contains the call establishment to
                a voice encapsulation peer.
                The entry is deleted when its associated call active entry
                in the IETF Dial Control MIB is deleted.
                ''',
                'cvcallhistoryentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallHistoryTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvvoipcallhistorytable.Cvvoipcallhistoryentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvvoipcallhistorytable.Cvvoipcallhistoryentry',
            False, 
            [
            _MetaInfoClassMember('cCallHistoryIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'ccallhistoryindex',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvVoIPCallHistoryBitRates', REFERENCE_BITS, 'Cvamrnbbitratemode' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'Cvamrnbbitratemode', 
                [], [], 
                '''                This object indicates modes of Bit rates.
                This object is not instantiated when the object
                cvVoIPCallHistoryCoderTypeRate is not equal to
                gsmAmrNb enum.
                ''',
                'cvvoipcallhistorybitrates',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryCallId', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object represents the call identifier for the
                VoIP leg, which was assigned to the call.
                ''',
                'cvvoipcallhistorycallid',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryCallReferenceId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The call reference ID associates the video call entry and voice
                call entry of the same endpoint.  An audio-only call may or may
                not have a valid call reference ID (i.e. value greater than
                zero), but in both cases, there will not be a video call entry
                associated with it. 
                
                For a video call, the video-specific information  is stored in a
                call entry in cVideoSessionActive of CISCO-VIDEO-SESSION-MIB, in
                which the call reference ID is also identified.
                ''',
                'cvvoipcallhistorycallreferenceid',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryChannels', ATTRIBUTE, 'int' , None, None, 
                [('1', '6')], [], 
                '''                The object indicates the number of audio channels.
                Supported value is 1. This object is not instantiated
                when the object cvVoIPCallHistoryCoderTypeRate is not equal
                to gsmAmrNb enum.
                ''',
                'cvvoipcallhistorychannels',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryCoderMode', REFERENCE_ENUM_CLASS, 'CvilbcframemodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CvilbcframemodeEnum', 
                [], [], 
                '''                The object indicates the iLBC mode.
                The value of this object is valid only if 
                cvVoIPCallHistoryCoderTypeRate is equal to 
                'iLBC'.
                ''',
                'cvvoipcallhistorycodermode',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryCoderTypeRate', REFERENCE_ENUM_CLASS, 'CvccodertyperateEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_COMMON_DIAL_CONTROL_MIB', 'CvccodertyperateEnum', 
                [], [], 
                '''                The negotiated coder rate. It specifies the transmit rate of
                voice/fax compression to its associated call leg for the
                call. This rate is different from the configuration rate
                because of rate negotiation during the call.
                ''',
                'cvvoipcallhistorycodertyperate',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryConnectionId', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                The global connection identifier for the
                VoIP leg, which was assigned to the call.
                ''',
                'cvvoipcallhistoryconnectionid',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryCRC', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the object has a value of true(1), frame CRC will be
                included in the payload and if the value is false(2),
                frame CRC will not be included in the payload.
                This object is applicable only when RTP frame type
                is octet aligned. This object is not instantiated when
                the object cvVoIPCallHistoryCoderTypeRate is not equal to
                gsmAmrNb enum.
                ''',
                'cvvoipcallhistorycrc',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryEarlyPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of received voice packets that are
                arrived too early to store in jitter buffer
                during the call.
                ''',
                'cvvoipcallhistoryearlypackets',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryEncap', REFERENCE_ENUM_CLASS, 'CvamrnbrtpencapEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CvamrnbrtpencapEnum', 
                [], [], 
                '''                The object indicates the RTP encapsulation type.
                Supported RTP encapsulation type is RFC3267.
                This object is not instantiated when the object
                cvVoIPCallHistoryCoderTypeRate is not equal to
                gsmAmrNb enum.
                ''',
                'cvvoipcallhistoryencap',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryFallbackDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The FallbackDelay is calculated as follows -
                Take the sum of the round trips for all the probes, 
                divide by the number of probes, 
                and divide by two to get the one-way delay.  
                Then add in jitter_in or jiter_out,
                which ever is higher.
                ''',
                'cvvoipcallhistoryfallbackdelay',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryFallbackIcpif', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The Calculated Planning Impairment Factor (Icpif) of the
                call  that is associated to this call leg.
                The value in this object is computed by the following
                equation.
                Icpif of the fallback probe =
                Itotal (total impairment value)  - configured fallback
                (Expectation Factor).
                A value of 0 implies that Icpif was not calculated and is
                meaningless for this attempt.
                ''',
                'cvvoipcallhistoryfallbackicpif',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryFallbackLoss', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                FallbackLoss is the percentage of loss packets based on
                the total packets sent.
                ''',
                'cvvoipcallhistoryfallbackloss',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryGapFillWithInterpolation', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duration of voice signal played out with signal synthesized
                from parameters or samples of data preceding and following
                in time due to voice data not received on time (or lost)
                from voice gateway for this call. This counter object
                will lock at the maximum value which is approximately two
                days.
                ''',
                'cvvoipcallhistorygapfillwithinterpolation',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryGapFillWithPrediction', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duration of voice signal played out with signal synthesized
                from parameters or samples of data preceding in time due to
                voice data not received on time (or lost) from voice gateway
                for this call. An example of such playout is frame-erasure
                or  frame-concealment strategies in G.729 and G.723.1
                compression algorithms. This counter object will lock at
                the maximum value which is approximately two days.
                ''',
                'cvvoipcallhistorygapfillwithprediction',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryGapFillWithRedundancy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duration of voice signal played out with signal synthesized
                from redundancy parameters available due to voice data not
                received on time (or lost) from voice gateway for this call.
                This counter object will lock at the maximum value which
                is approximately two days.
                ''',
                'cvvoipcallhistorygapfillwithredundancy',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryGapFillWithSilence', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duration of voice signal replaced with signal played out
                during silence due to voice data not received on time
                (or lost) from voice gateway this call. This counter
                object will lock at the maximum value which is
                approximately two days.
                ''',
                'cvvoipcallhistorygapfillwithsilence',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryHiWaterPlayoutDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The high water mark Voice Playout FIFO Delay during
                the voice call. This counter object will lock at the
                maximum value which is approximately two days.
                ''',
                'cvvoipcallhistoryhiwaterplayoutdelay',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryIcpif', ATTRIBUTE, 'int' , None, None, 
                [('-1', '55')], [], 
                '''                The Calculated Planning Impairment Factor (Icpif) of the
                call  that is associated to this call leg.
                The value in this object is computed by the following
                equation.
                Icpif of the call =
                Itotal (total impairment value) of the call - A
                (Expectation Factor) in the cvVoIPPeerCfgExpectFactor of
                the call leg associated peer.
                A value of -1 implies that Icpif was not calculated and is
                meaningless for this call.
                ''',
                'cvvoipcallhistoryicpif',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryInterleaving', ATTRIBUTE, 'int' , None, None, 
                [('1', '50')], [], 
                '''                The object indicates the maximum number of frame-blocks
                allowed in an interleaving group. It indicates that
                frame-block level interleaving will be used for that
                session. If this object is not set, interleaving
                is not used. This object is applicable only when
                RTP frame type is octet aligned. This object is not
                instantiated when the object cvVoIPCallHistoryCoderTypeRate
                is not equal to gsmAmrNb enum.
                ''',
                'cvvoipcallhistoryinterleaving',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryLatePackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of received voice packets that are
                arrived too late to playout with CODEC (Coder/Decoder)
                during the call.
                ''',
                'cvvoipcallhistorylatepackets',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryLostPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of lost voice packets during the call.
                ''',
                'cvvoipcallhistorylostpackets',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryLoWaterPlayoutDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The low water mark Voice Playout FIFO Delay during
                the voice call.
                ''',
                'cvvoipcallhistorylowaterplayoutdelay',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryMaxPtime', ATTRIBUTE, 'int' , None, None, 
                [('20', '100')], [], 
                '''                The object indicates the maximum amount of media that
                can be encapsulated in a payload. Supported value is
                20 msec. This object is not instantiated when the
                object cvVoIPCallHistoryCoderTypeRate is not equal to
                gsmAmrNb enum.
                ''',
                'cvvoipcallhistorymaxptime',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryModeChgNeighbor', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the object has a value of true(1), mode changes will be
                made to only neighboring modes set to
                cvVoIPCallHistoryBitRates object. If the value is false(2),
                mode changes will be allowed to any modes set to
                cvVoIPCallHistoryBitRates object. This object is not
                instantiated when the object cvVoIPCallHistoryCoderTypeRate
                is not equal to gsmAmrNb enum.
                ''',
                'cvvoipcallhistorymodechgneighbor',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryModeChgPeriod', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                The object indicates the interval (N frame-blocks) at which
                codec mode changes are allowed. This object is not
                instantiated when the object cvVoIPCallHistoryCoderTypeRate
                is not equal to gsmAmrNb enum.
                ''',
                'cvvoipcallhistorymodechgperiod',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryOctetAligned', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the object has a value true(1) octet align operation
                is used, and if the value is false(2), bandwidth efficient
                operation is used. This object is not instantiated when
                the object cvVoIPCallHistoryCoderTypeRate is not equal to
                gsmAmrNb enum.
                ''',
                'cvvoipcallhistoryoctetaligned',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryOnTimeRvPlayout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duration of voice playout from data received on time for
                this call. This plus the durations for the GapFills in the
                following entries gives the Total Voice Playout Duration
                for Active Voice.
                This does not include duration for which no data was sent by the
                Transmit end as voice signal, e.g., silence suppression
                and fax signal. The On Time Playout Rate can be computed
                by dividing this entry by the Total Voice Playout Duration.
                This counter object will lock at the maximum value which
                is approximately two days.
                ''',
                'cvvoipcallhistoryontimervplayout',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryProtocolCallId', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The protocol-specific call identifier for the VoIP call.
                ''',
                'cvvoipcallhistoryprotocolcallid',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryPtime', ATTRIBUTE, 'int' , None, None, 
                [('20', '100')], [], 
                '''                The object indicates the length of the time in milliseconds
                represented by the media of the packet. Supported value is
                20 milliseconds. This object is not instantiated when the
                object cvVoIPCallHistoryCoderTypeRate is not equal to
                gsmAmrNb enum.
                ''',
                'cvvoipcallhistoryptime',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryReceiveDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The average Playout FIFO Delay plus the decoder delay
                during the voice call.
                ''',
                'cvvoipcallhistoryreceivedelay',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryRemMediaIPAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Remote media end point IP address for the VoIP call.
                ''',
                'cvvoipcallhistoryremmediaipaddr',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryRemMediaIPAddrT', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object specifies the type of address contained in
                the associated instance of
                cvVoIPCallHistoryRemMediaIPAddr.
                ''',
                'cvvoipcallhistoryremmediaipaddrt',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryRemMediaPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remote media end point listener port to which to transmit
                voice packets.
                ''',
                'cvvoipcallhistoryremmediaport',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryRemoteIPAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote system IP address for the call.
                ''',
                'cvvoipcallhistoryremoteipaddress',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryRemoteUDPPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remote system UDP listener port to which to transmit voice
                packets for the call.
                ''',
                'cvvoipcallhistoryremoteudpport',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryRemSigIPAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Remote signalling IP address for the VoIP call.
                ''',
                'cvvoipcallhistoryremsigipaddr',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryRemSigIPAddrT', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object specifies the type of address contained in
                the associated instance of cvVoIPCallHistoryRemSigIPAddr.
                ''',
                'cvvoipcallhistoryremsigipaddrt',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryRemSigPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remote signalling listener port to which to transmit
                voice packets.
                ''',
                'cvvoipcallhistoryremsigport',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryRobustSorting', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the object has a value of true(1), payload employs
                robust sorting and if the value is false(2), payload
                does not employ robust sorting. This object is applicable
                only when RTP frame type is octet aligned. This object
                is not instantiated when the object
                cvVoIPCallHistoryCoderTypeRate is not equal to gsmAmrNb
                enum.
                ''',
                'cvvoipcallhistoryrobustsorting',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryRoundTripDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The voice packet round trip delay between local and
                the remote system on the IP backbone during the call.
                ''',
                'cvvoipcallhistoryroundtripdelay',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistorySelectedQoS', REFERENCE_ENUM_CLASS, 'QosserviceEnum' , 'ydk.models.cisco_ios_xe.INT_SERV_MIB', 'QosserviceEnum', 
                [], [], 
                '''                The selected RSVP QoS for the call.
                ''',
                'cvvoipcallhistoryselectedqos',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistorySessionId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the session ID assigned by the call
                manager to identify call legs that belong to the same call
                session.  This session ID (history) represents a completed call
                session, whereas the active session ID
                (cvVoIPCallActiveSessionId) represents an ongoing session.
                ''',
                'cvvoipcallhistorysessionid',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistorySessionProtocol', REFERENCE_ENUM_CLASS, 'CvsessionprotocolEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CvsessionprotocolEnum', 
                [], [], 
                '''                The object specifies the session protocol to be used
                for Internet call between local and remote router via
                IP backbone.
                ''',
                'cvvoipcallhistorysessionprotocol',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistorySessionTarget', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The object specifies the session target of the peer that
                is used for the Voice over IP call.
                ''',
                'cvvoipcallhistorysessiontarget',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistorySRTPEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The object indicates whether or not the SRTP (Secured RTP)
                was enabled for the voice call.
                ''',
                'cvvoipcallhistorysrtpenable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryUsername', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                The textual identifier of the calling party (user) of the
                call. If the username is not available, then the value of
                this object will have a length of zero.
                ''',
                'cvvoipcallhistoryusername',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryVADEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The object indicates whether or not the VAD (Voice Activity
                Detection) was enabled for the voice call.
                ''',
                'cvvoipcallhistoryvadenable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvVoIPCallHistoryEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvvoipcallhistorytable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvvoipcallhistorytable',
            False, 
            [
            _MetaInfoClassMember('cvVoIPCallHistoryEntry', REFERENCE_LIST, 'Cvvoipcallhistoryentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvvoipcallhistorytable.Cvvoipcallhistoryentry', 
                [], [], 
                '''                The information regarding a single VoIP call leg.
                The call leg entry is identified by using the same index
                objects that are used by Call Active table of IETF Dial
                Control MIB to identify the call.
                An entry of this table is created when its associated call
                history entry in the IETF Dial Control MIB is created and
                the call history entry contains information for the call
                establishment to the peer on the IP backbone via a voice
                over IP peer.
                The entry is deleted when its associated call history
                entry in the IETF Dial Control MIB is deleted.
                ''',
                'cvvoipcallhistoryentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvVoIPCallHistoryTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcallratestatstable.Cvcallratestatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcallratestatstable.Cvcallratestatsentry',
            False, 
            [
            _MetaInfoClassMember('cvCallRateStatsIntvlDurUnits', REFERENCE_ENUM_CLASS, 'CvcallvolumestatsintvltypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CvcallvolumestatsintvltypeEnum', 
                [], [], 
                '''                The Object indexes in Call Rate Table to select one among three
                interval-tables.
                
                The different types in this table are represented by 
                CvCallVolumeStatsIntvlType
                ''',
                'cvcallratestatsintvldurunits',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvCallRateStatsIntvlDur', ATTRIBUTE, 'int' , None, None, 
                [('1', '72')], [], 
                '''                This is an index that references to the different past periods
                in given in interval of call rate table.
                This range is 1-60 for Seconds and Minutes table 
                wherein 1-72 for hours table.
                ''',
                'cvcallratestatsintvldur',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvCallRateStatsAvgVal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the average calls per second
                that occured for the given period for the given interval.
                ''',
                'cvcallratestatsavgval',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallRateStatsMaxVal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the maximum calls per second
                that occured for the given period for the given interval.
                ''',
                'cvcallratestatsmaxval',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallRateStatsEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcallratestatstable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcallratestatstable',
            False, 
            [
            _MetaInfoClassMember('cvCallRateStatsEntry', REFERENCE_LIST, 'Cvcallratestatsentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcallratestatstable.Cvcallratestatsentry', 
                [], [], 
                '''                This is a conceptual-row in cvCallRateStatsTable
                This entry is created at the system initialization and is
                updated at every epoch based on CvCallVolumeStatsIntvlType
                ''',
                'cvcallratestatsentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallRateStatsTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcalllegratestatstable.Cvcalllegratestatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcalllegratestatstable.Cvcalllegratestatsentry',
            False, 
            [
            _MetaInfoClassMember('cvCallLegRateStatsIntvlDurUnits', REFERENCE_ENUM_CLASS, 'CvcallvolumestatsintvltypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CvcallvolumestatsintvltypeEnum', 
                [], [], 
                '''                The Object indexes in Call Leg Rate Table to select one among
                three
                interval-tables.
                
                The different types in this table are represented by 
                CvCallVolumeStatsIntvlType
                ''',
                'cvcalllegratestatsintvldurunits',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvCallLegRateStatsIntvlDur', ATTRIBUTE, 'int' , None, None, 
                [('1', '72')], [], 
                '''                This is an index that references to the different past periods
                in given in interval of call rate table.
                This range is 1-60 for Seconds and Minutes table 
                wherein 1-72 for hours table.
                ''',
                'cvcalllegratestatsintvldur',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvCallLegRateStatsAvgVal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the average call-legs per second
                that occured for the given period for the given interval.
                ''',
                'cvcalllegratestatsavgval',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallLegRateStatsMaxVal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the maximum call-legs per second
                that occured for the given period for the given interval.
                ''',
                'cvcalllegratestatsmaxval',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallLegRateStatsEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcalllegratestatstable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcalllegratestatstable',
            False, 
            [
            _MetaInfoClassMember('cvCallLegRateStatsEntry', REFERENCE_LIST, 'Cvcalllegratestatsentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcalllegratestatstable.Cvcalllegratestatsentry', 
                [], [], 
                '''                This is a conceptual-row in cvCallLegRateStatsTable
                This entry is created at the system initialization and is
                updated at every epoch based on CvCallVolumeStatsIntvlType
                ''',
                'cvcalllegratestatsentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallLegRateStatsTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvactivecallstatstable.Cvactivecallstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvactivecallstatstable.Cvactivecallstatsentry',
            False, 
            [
            _MetaInfoClassMember('cvActiveCallStatsIntvlDurUnits', REFERENCE_ENUM_CLASS, 'CvcallvolumestatsintvltypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CvcallvolumestatsintvltypeEnum', 
                [], [], 
                '''                The Object indexes in Active Call Rate Table (con-current calls
                table) to select one among three interval-tables.
                
                The different types in this table are represented by 
                CvCallVolumeStatsIntvlType
                ''',
                'cvactivecallstatsintvldurunits',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvActiveCallStatsIntvlDur', ATTRIBUTE, 'int' , None, None, 
                [('1', '72')], [], 
                '''                This is an index that references to the different past periods
                in given in interval of active call table.
                This range is 1-60 for Seconds and Minutes table 
                wherein 1-72 for hours table.
                ''',
                'cvactivecallstatsintvldur',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvActiveCallStatsAvgVal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the average number of active calls
                that occured for the given period for the given interval.
                ''',
                'cvactivecallstatsavgval',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvActiveCallStatsMaxVal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the maximum number of active call
                that occured for the given period for the given interval.
                ''',
                'cvactivecallstatsmaxval',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvActiveCallStatsEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvactivecallstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvactivecallstatstable',
            False, 
            [
            _MetaInfoClassMember('cvActiveCallStatsEntry', REFERENCE_LIST, 'Cvactivecallstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvactivecallstatstable.Cvactivecallstatsentry', 
                [], [], 
                '''                This is a conceptual-row in cvActiveCallStatsTable
                This entry is created at the system initialization and is
                updated at every epoch based on CvCallVolumeStatsIntvlType
                ''',
                'cvactivecallstatsentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvActiveCallStatsTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcalldurationstatstable.Cvcalldurationstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcalldurationstatstable.Cvcalldurationstatsentry',
            False, 
            [
            _MetaInfoClassMember('cvCallDurationStatsIntvlDurUnits', REFERENCE_ENUM_CLASS, 'CvcallvolumestatsintvltypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CvcallvolumestatsintvltypeEnum', 
                [], [], 
                '''                The Object indexes in Call Duration Table to select one among
                three interval-tables.
                
                The different types in this table are represented by 
                CvCallVolumeStatsIntvlType
                ''',
                'cvcalldurationstatsintvldurunits',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvCallDurationStatsIntvlDur', ATTRIBUTE, 'int' , None, None, 
                [('1', '72')], [], 
                '''                This is an index that references to the different past periods
                in given in interval of call Duration table.
                This range is 1-60 for Seconds and Minutes table 
                wherein 1-72 for hours table.
                ''',
                'cvcalldurationstatsintvldur',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvCallDurationStatsAvgVal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the average number of calls having a
                duration which is below the threshold for the given interval.
                ''',
                'cvcalldurationstatsavgval',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallDurationStatsMaxVal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the maximum number of calls having a
                duration which is below the threshold for the given interval.
                ''',
                'cvcalldurationstatsmaxval',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallDurationStatsEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcalldurationstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcalldurationstatstable',
            False, 
            [
            _MetaInfoClassMember('cvCallDurationStatsEntry', REFERENCE_LIST, 'Cvcalldurationstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcalldurationstatstable.Cvcalldurationstatsentry', 
                [], [], 
                '''                This is a conceptual-row in cvCallDurationStatsTable
                This entry is created at the system initialization and is
                updated at every epoch based on CvCallVolumeStatsIntvlType
                ''',
                'cvcalldurationstatsentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallDurationStatsTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvsipmsgratestatstable.Cvsipmsgratestatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvsipmsgratestatstable.Cvsipmsgratestatsentry',
            False, 
            [
            _MetaInfoClassMember('cvSipMsgRateStatsIntvlDurUnits', REFERENCE_ENUM_CLASS, 'CvcallvolumestatsintvltypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CvcallvolumestatsintvltypeEnum', 
                [], [], 
                '''                The Object indexes in SIP Message Rate Table to select one
                among three interval-tables.
                
                The different types in this table are represented by 
                CvCallVolumeStatsIntvlType
                ''',
                'cvsipmsgratestatsintvldurunits',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvSipMsgRateStatsIntvlDur', ATTRIBUTE, 'int' , None, None, 
                [('1', '72')], [], 
                '''                This is an index that references to the different past
                periods in given in interval of SIP message rate table.
                This range is 1-60 for Seconds and Minutes table 
                wherein 1-72 for hours table.
                ''',
                'cvsipmsgratestatsintvldur',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvSipMsgRateStatsAvgVal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the average SIP messages per second that
                is received for the given interval.
                ''',
                'cvsipmsgratestatsavgval',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvSipMsgRateStatsMaxVal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates the maximum SIP messages  per second that
                is received for the given interval.
                ''',
                'cvsipmsgratestatsmaxval',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvSipMsgRateStatsEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvsipmsgratestatstable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvsipmsgratestatstable',
            False, 
            [
            _MetaInfoClassMember('cvSipMsgRateStatsEntry', REFERENCE_LIST, 'Cvsipmsgratestatsentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvsipmsgratestatstable.Cvsipmsgratestatsentry', 
                [], [], 
                '''                This is a conceptual-row in cvSipMsgRateStatsTable
                This entry is created at the system initialization and is
                updated at every epoch based on CvCallVolumeStatsIntvlType
                ''',
                'cvsipmsgratestatsentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvSipMsgRateStatsTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcallratewmtable.Cvcallratewmentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcallratewmtable.Cvcallratewmentry',
            False, 
            [
            _MetaInfoClassMember('cvCallRateWMIntvlDurUnits', REFERENCE_ENUM_CLASS, 'CvcallvolumewmintvltypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CvcallvolumewmintvltypeEnum', 
                [], [], 
                '''                The Object indexes in call rate Water mark Table to select one
                among four interval-tables.
                
                The different types in this table are represented by 
                CvCallVolumeWMIntvlType
                ''',
                'cvcallratewmintvldurunits',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvCallRateWMIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                This is an index that references to different peaks in
                past period in call rate watermark table.
                
                The number of watermarks entries stored for each table are 
                based on cvCallVolumeWMTableSize
                ''',
                'cvcallratewmindex',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvCallRateWMts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates date and Time when the high watermark
                is achieved for calls per second for the given interval
                ''',
                'cvcallratewmts',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallRateWMValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates high watermark value achieved by the
                calls per second for the given interval
                ''',
                'cvcallratewmvalue',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallRateWMEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcallratewmtable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcallratewmtable',
            False, 
            [
            _MetaInfoClassMember('cvCallRateWMEntry', REFERENCE_LIST, 'Cvcallratewmentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcallratewmtable.Cvcallratewmentry', 
                [], [], 
                '''                This is a conceptual-row in cvCallRateWMTable
                This entry is created at the system initialization and is
                updated whenever 
                a) This entry is obsolete OR
                b) A new/higher entry is available.
                These entries are reinitialised/added/deleted  if
                cvCallVolumeWMTableSize is changed
                ''',
                'cvcallratewmentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallRateWMTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcalllegratewmtable.Cvcalllegratewmentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcalllegratewmtable.Cvcalllegratewmentry',
            False, 
            [
            _MetaInfoClassMember('cvCallLegRateWMIntvlDurUnits', REFERENCE_ENUM_CLASS, 'CvcallvolumewmintvltypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CvcallvolumewmintvltypeEnum', 
                [], [], 
                '''                The Object indexes in call leg rate Water mark Table to select
                one
                among four interval-tables.
                
                The different types in this table are represented by 
                CvCallVolumeWMIntvlType
                ''',
                'cvcalllegratewmintvldurunits',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvCallLegRateWMIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                This is an index that references to different peaks in
                past period in call leg rate watermark table.
                
                The number of watermarks entries stored for each table are 
                based on cvCallVolumeWMTableSize
                ''',
                'cvcalllegratewmindex',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvCallLegRateWMts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates date and time when the high watermark
                is achieved for call-legs per second for the given interval
                ''',
                'cvcalllegratewmts',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallLegRateWMValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates high watermark value achieved by the
                call legs per second for the given interval
                ''',
                'cvcalllegratewmvalue',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallLegRateWMEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvcalllegratewmtable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvcalllegratewmtable',
            False, 
            [
            _MetaInfoClassMember('cvCallLegRateWMEntry', REFERENCE_LIST, 'Cvcalllegratewmentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcalllegratewmtable.Cvcalllegratewmentry', 
                [], [], 
                '''                This is a conceptual-row in cvCallLegRateWMTable
                This entry is created at the system initialization and is
                updated whenever 
                a) This entry is obsolete OR
                b) A new/higher entry is available.
                These entries are reinitialised/added/deleted  if
                cvCallVolumeWMTableSize is changed
                ''',
                'cvcalllegratewmentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvCallLegRateWMTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvactivecallwmtable.Cvactivecallwmentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvactivecallwmtable.Cvactivecallwmentry',
            False, 
            [
            _MetaInfoClassMember('cvActiveCallWMIntvlDurUnits', REFERENCE_ENUM_CLASS, 'CvcallvolumewmintvltypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CvcallvolumewmintvltypeEnum', 
                [], [], 
                '''                The Object indexes in active call Water mark Table to select
                one among four interval-tables.
                
                The different types in this table are represented by 
                CvCallVolumeWMIntvlType
                ''',
                'cvactivecallwmintvldurunits',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvActiveCallWMIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                This is an index that references to different peaks in
                past period in acive call watermark table.
                
                The number of watermarks entries stored for each table are 
                based on cvCallVolumeWMTableSize
                ''',
                'cvactivecallwmindex',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvActiveCallWMts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates date and time when the high watermark
                is achieved for active calls for the given interval
                ''',
                'cvactivecallwmts',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvActiveCallWMValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates high watermark value achieved by the
                active calls for the given interval
                ''',
                'cvactivecallwmvalue',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvActiveCallWMEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvactivecallwmtable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvactivecallwmtable',
            False, 
            [
            _MetaInfoClassMember('cvActiveCallWMEntry', REFERENCE_LIST, 'Cvactivecallwmentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvactivecallwmtable.Cvactivecallwmentry', 
                [], [], 
                '''                This is a conceptual-row in cvActiveCallWMTable
                This entry is created at the system initialization and is
                updated whenever 
                a) This entry is obsolete OR
                b) A new/higher entry is available.
                These entries are reinitialised/added/deleted  if
                cvCallVolumeWMTableSize is changed
                ''',
                'cvactivecallwmentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvActiveCallWMTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvsipmsgratewmtable.Cvsipmsgratewmentry' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvsipmsgratewmtable.Cvsipmsgratewmentry',
            False, 
            [
            _MetaInfoClassMember('cvSipMsgRateWMIntvlDurUnits', REFERENCE_ENUM_CLASS, 'CvcallvolumewmintvltypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CvcallvolumewmintvltypeEnum', 
                [], [], 
                '''                The Object indexes in SIP Message rate Water mark Table to
                select one among four interval-tables.
                
                The different types in this table are represented by 
                CvCallVolumeWMIntvlType
                ''',
                'cvsipmsgratewmintvldurunits',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvSipMsgRateWMIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                This is an index that references to different peaks in
                past period in sip message rate watermark table.
                
                The number of watermarks entries stored for each table are 
                based on cvCallVolumeWMTableSize
                ''',
                'cvsipmsgratewmindex',
                'CISCO-VOICE-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cvSipMsgRateWMts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates date and time when the high watermark
                is achieved for SIP messages per second for the given interval
                ''',
                'cvsipmsgratewmts',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvSipMsgRateWMValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object indicates high watermark value achieved by the
                SIP messages per second for the given interval
                ''',
                'cvsipmsgratewmvalue',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvSipMsgRateWMEntry',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib.Cvsipmsgratewmtable' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib.Cvsipmsgratewmtable',
            False, 
            [
            _MetaInfoClassMember('cvSipMsgRateWMEntry', REFERENCE_LIST, 'Cvsipmsgratewmentry' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvsipmsgratewmtable.Cvsipmsgratewmentry', 
                [], [], 
                '''                This is a conceptual-row in cvSipMsgRateWMTable.
                This entry is created at the system initialization and is
                updated whenever 
                a) This entry is obsolete OR
                b) A new/higher entry is available.
                These entries are reinitialised/added/deleted if
                cvCallVolumeWMTableSize is changed
                ''',
                'cvsipmsgratewmentry',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'cvSipMsgRateWMTable',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoVoiceDialControlMib' : {
        'meta_info' : _MetaInfoClass('CiscoVoiceDialControlMib',
            False, 
            [
            _MetaInfoClassMember('cvActiveCallStatsTable', REFERENCE_CLASS, 'Cvactivecallstatstable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvactivecallstatstable', 
                [], [], 
                '''                This table represents the active voice calls in various
                interval lengths defined by the 
                CvCallVolumeStatsIntvlType object.
                
                Each interval may contain one or more entries to allow for
                detailed measurement to be collected.
                ''',
                'cvactivecallstatstable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvActiveCallWMTable', REFERENCE_CLASS, 'Cvactivecallwmtable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvactivecallwmtable', 
                [], [], 
                '''                This table represents high watermarks achieved
                by active calls in various interval length defined 
                by CvCallVolumeWMIntvlType. 
                
                Each interval may contain one or more entries to allow 
                for detailed measurement to be collected.
                ''',
                'cvactivecallwmtable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallActiveTable', REFERENCE_CLASS, 'Cvcallactivetable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcallactivetable', 
                [], [], 
                '''                This table is the voice extension to the call active table
                of IETF Dial Control MIB. It contains voice encapsulation
                call leg information that is derived from the statistics
                of lower layer telephony interface.
                ''',
                'cvcallactivetable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallDurationStatsTable', REFERENCE_CLASS, 'Cvcalldurationstatstable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcalldurationstatstable', 
                [], [], 
                '''                This table represents the number of calls below a specific
                duration in various interval length defined by 
                the CvCallVolumeStatsIntvlType object.  
                
                The specific duration is configurable value of 
                 cvCallDurationStatsThreshold object.
                
                Each interval may contain one or more entries to allow for 
                detailed measurement to be collected.
                ''',
                'cvcalldurationstatstable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallHistoryTable', REFERENCE_CLASS, 'Cvcallhistorytable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcallhistorytable', 
                [], [], 
                '''                This table is the voice extension to the call history table
                of IETF Dial Control MIB. It contains voice encapsulation
                call leg information such as voice packet statistics,
                coder usage and end to end bandwidth of the call leg.
                ''',
                'cvcallhistorytable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallLegRateStatsTable', REFERENCE_CLASS, 'Cvcalllegratestatstable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcalllegratestatstable', 
                [], [], 
                '''                cvCallLegRateStatsTable table represents voice call leg rate
                measurement in various interval lengths defined by 
                the CvCallVolumeStatsIntvlType object.
                Each interval may contain one or more entries to allow for
                detailed measurement to be collected.
                ''',
                'cvcalllegratestatstable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallLegRateWMTable', REFERENCE_CLASS, 'Cvcalllegratewmtable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcalllegratewmtable', 
                [], [], 
                '''                cvCallLegRateWMTable table represents high watermarks achieved
                by call-leg rate in various interval length defined 
                by CvCallVolumeWMIntvlType. 
                
                Each interval may contain one or more entries to allow for 
                detailed measurement to be collected
                ''',
                'cvcalllegratewmtable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallRateMonitor', REFERENCE_CLASS, 'Cvcallratemonitor' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcallratemonitor', 
                [], [], 
                '''                ''',
                'cvcallratemonitor',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallRateStatsTable', REFERENCE_CLASS, 'Cvcallratestatstable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcallratestatstable', 
                [], [], 
                '''                This table represents voice call rate measurement in various
                interval lengths defined by the 
                CvCallVolumeStatsIntvlType object.
                
                Each interval may contain one or more entries to allow for
                detailed measurement to be collected.
                ''',
                'cvcallratestatstable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallRateWMTable', REFERENCE_CLASS, 'Cvcallratewmtable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcallratewmtable', 
                [], [], 
                '''                This table represents high watermarks achieved
                by call rate in various interval length defined 
                by CvCallVolumeWMIntvlType. 
                
                Each interval may contain one or more entries to allow for 
                detailed measurement to be collected
                ''',
                'cvcallratewmtable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallVolConnTable', REFERENCE_CLASS, 'Cvcallvolconntable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcallvolconntable', 
                [], [], 
                '''                This table represents the number of active
                call connections for each call connection type
                in the voice gateway.
                ''',
                'cvcallvolconntable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallVolIfTable', REFERENCE_CLASS, 'Cvcallvoliftable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcallvoliftable', 
                [], [], 
                '''                This table represents the information about
                the usage of an IP interface in a voice
                gateway for voice media calls. This table
                has a sparse-dependent relationship with  
                ifTable. There exists an entry in this table, 
                for each of the  entries in ifTable where ifType 
                is one of 'ethernetCsmacd' and 'softwareLoopback'.
                ''',
                'cvcallvoliftable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallVolume', REFERENCE_CLASS, 'Cvcallvolume' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcallvolume', 
                [], [], 
                '''                ''',
                'cvcallvolume',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvCallVolumeStatsHistory', REFERENCE_CLASS, 'Cvcallvolumestatshistory' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvcallvolumestatshistory', 
                [], [], 
                '''                ''',
                'cvcallvolumestatshistory',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvGatewayCallActive', REFERENCE_CLASS, 'Cvgatewaycallactive' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvgatewaycallactive', 
                [], [], 
                '''                ''',
                'cvgatewaycallactive',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvGeneralConfiguration', REFERENCE_CLASS, 'Cvgeneralconfiguration' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvgeneralconfiguration', 
                [], [], 
                '''                ''',
                'cvgeneralconfiguration',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvPeerCfgTable', REFERENCE_CLASS, 'Cvpeercfgtable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvpeercfgtable', 
                [], [], 
                '''                The table contains the Voice Generic Peer information that
                is used to create an ifIndexed row with an appropriate
                ifType that is associated with the cvPeerCfgType and
                cvPeerCfgPeerType objects.
                ''',
                'cvpeercfgtable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvPeerCommonCfgTable', REFERENCE_CLASS, 'Cvpeercommoncfgtable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvpeercommoncfgtable', 
                [], [], 
                '''                The table contains the Voice specific peer common
                configuration information that is required to accept voice
                calls or to which it will place them or process the
                incoming calls.
                ''',
                'cvpeercommoncfgtable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvSipMsgRateStatsTable', REFERENCE_CLASS, 'Cvsipmsgratestatstable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvsipmsgratestatstable', 
                [], [], 
                '''                This table represents the SIP message rate measurement in
                various interval length defined by the 
                CvCallVolumeStatsIntvlType object.
                
                Each interval may contain one or more entries to allow for
                detailed measurement to be collected
                ''',
                'cvsipmsgratestatstable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvSipMsgRateWMTable', REFERENCE_CLASS, 'Cvsipmsgratewmtable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvsipmsgratewmtable', 
                [], [], 
                '''                This table represents of high watermarks achieved
                by SIP message rate in various interval length defined 
                by CvCallVolumeWMIntvlType. 
                
                Each interval may contain one or more entries to allow for
                detailed measurement to be collected
                ''',
                'cvsipmsgratewmtable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoicePeerCfgTable', REFERENCE_CLASS, 'Cvvoicepeercfgtable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvvoicepeercfgtable', 
                [], [], 
                '''                The table contains the Voice over Telephony peer specific
                information that is required to accept voice calls or to
                which it will place them or perform various loopback tests
                via interface.
                ''',
                'cvvoicepeercfgtable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallActiveTable', REFERENCE_CLASS, 'Cvvoipcallactivetable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvvoipcallactivetable', 
                [], [], 
                '''                This table is the VoIP extension to the call active table of
                IETF Dial Control MIB. It contains VoIP call leg
                information about specific VoIP call destination and the
                selected QoS for the call leg.
                ''',
                'cvvoipcallactivetable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPCallHistoryTable', REFERENCE_CLASS, 'Cvvoipcallhistorytable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvvoipcallhistorytable', 
                [], [], 
                '''                This table is the VoIP extension to the call history table
                of IETF Dial Control MIB. It contains VoIP call leg
                information about specific VoIP call destination and the
                selected QoS for the call leg.
                ''',
                'cvvoipcallhistorytable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cvVoIPPeerCfgTable', REFERENCE_CLASS, 'Cvvoippeercfgtable' , 'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB', 'CiscoVoiceDialControlMib.Cvvoippeercfgtable', 
                [], [], 
                '''                The table contains the Voice over IP (VoIP) peer specific
                information that is required to accept voice calls or to
                which it will place them via IP backbone with the
                specified session protocol in cvVoIPPeerCfgSessionProtocol.
                ''',
                'cvvoippeercfgtable',
                'CISCO-VOICE-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            'CISCO-VOICE-DIAL-CONTROL-MIB',
            _yang_ns._namespaces['CISCO-VOICE-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_VOICE_DIAL_CONTROL_MIB'
        ),
    },
}
_meta_table['CiscoVoiceDialControlMib.Cvpeercfgtable.Cvpeercfgentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvpeercfgtable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvvoicepeercfgtable.Cvvoicepeercfgentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvvoicepeercfgtable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvvoippeercfgtable.Cvvoippeercfgentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvvoippeercfgtable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvpeercommoncfgtable.Cvpeercommoncfgentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvpeercommoncfgtable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcallactivetable.Cvcallactiveentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvcallactivetable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvvoipcallactivetable.Cvvoipcallactiveentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvvoipcallactivetable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcallvolconntable.Cvcallvolconnentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvcallvolconntable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcallvoliftable.Cvcallvolifentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvcallvoliftable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcallhistorytable.Cvcallhistoryentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvcallhistorytable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvvoipcallhistorytable.Cvvoipcallhistoryentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvvoipcallhistorytable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcallratestatstable.Cvcallratestatsentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvcallratestatstable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcalllegratestatstable.Cvcalllegratestatsentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvcalllegratestatstable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvactivecallstatstable.Cvactivecallstatsentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvactivecallstatstable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcalldurationstatstable.Cvcalldurationstatsentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvcalldurationstatstable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvsipmsgratestatstable.Cvsipmsgratestatsentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvsipmsgratestatstable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcallratewmtable.Cvcallratewmentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvcallratewmtable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcalllegratewmtable.Cvcalllegratewmentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvcalllegratewmtable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvactivecallwmtable.Cvactivecallwmentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvactivecallwmtable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvsipmsgratewmtable.Cvsipmsgratewmentry']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib.Cvsipmsgratewmtable']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvgeneralconfiguration']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvgatewaycallactive']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcallvolume']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcallratemonitor']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcallvolumestatshistory']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvpeercfgtable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvvoicepeercfgtable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvvoippeercfgtable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvpeercommoncfgtable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcallactivetable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvvoipcallactivetable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcallvolconntable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcallvoliftable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcallhistorytable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvvoipcallhistorytable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcallratestatstable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcalllegratestatstable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvactivecallstatstable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcalldurationstatstable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvsipmsgratestatstable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcallratewmtable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvcalllegratewmtable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvactivecallwmtable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
_meta_table['CiscoVoiceDialControlMib.Cvsipmsgratewmtable']['meta_info'].parent =_meta_table['CiscoVoiceDialControlMib']['meta_info']
