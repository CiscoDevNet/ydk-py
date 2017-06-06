


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoDialControlMib.Cpeerglobalconfiguration.CpeersearchtypeEnum' : _MetaInfoEnum('CpeersearchtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB',
        {
            'none':'none',
            'datavoice':'datavoice',
            'voicedata':'voicedata',
        }, 'CISCO-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-DIAL-CONTROL-MIB']),
    'CiscoDialControlMib.Cpeerglobalconfiguration' : {
        'meta_info' : _MetaInfoClass('CiscoDialControlMib.Cpeerglobalconfiguration',
            False, 
            [
            _MetaInfoClassMember('cPeerSearchType', REFERENCE_ENUM_CLASS, 'CpeersearchtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB', 'CiscoDialControlMib.Cpeerglobalconfiguration.CpeersearchtypeEnum', 
                [], [], 
                '''                Specifies the peer search preference based on the
                type of peers in an universal/integrated port
                platform.
                
                none      - both voice and data peers are searched
                           in same preference.
                datavoice - search data peers first. If no data peers
                           are found, the voice peers are searched.
                voicedata - search voice peers first. If no voice peers
                           are found, the data peers are searched.
                ''',
                'cpeersearchtype',
                'CISCO-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-DIAL-CONTROL-MIB',
            'cPeerGlobalConfiguration',
            _yang_ns._namespaces['CISCO-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.CcallhistorycalloriginEnum' : _MetaInfoEnum('CcallhistorycalloriginEnum', 'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB',
        {
            'originate':'originate',
            'answer':'answer',
            'callback':'callback',
        }, 'CISCO-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-DIAL-CONTROL-MIB']),
    'CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.CcallhistoryinfotypeEnum' : _MetaInfoEnum('CcallhistoryinfotypeEnum', 'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB',
        {
            'other':'other',
            'speech':'speech',
            'unrestrictedDigital':'unrestrictedDigital',
            'unrestrictedDigital56':'unrestrictedDigital56',
            'restrictedDigital':'restrictedDigital',
            'audio31':'audio31',
            'audio7':'audio7',
            'video':'video',
            'packetSwitched':'packetSwitched',
            'fax':'fax',
        }, 'CISCO-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-DIAL-CONTROL-MIB']),
    'CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.CcallhistoryreleasesourceEnum' : _MetaInfoEnum('CcallhistoryreleasesourceEnum', 'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB',
        {
            'callingPartyInPstn':'callingPartyInPstn',
            'callingPartyInVoip':'callingPartyInVoip',
            'calledPartyInPstn':'calledPartyInPstn',
            'calledPartyInVoip':'calledPartyInVoip',
            'internalRelease':'internalRelease',
            'internalCallControlApp':'internalCallControlApp',
            'consoleCommand':'consoleCommand',
            'externalRadiusServer':'externalRadiusServer',
            'externalNmsApp':'externalNmsApp',
            'externalCallControlAgent':'externalCallControlAgent',
        }, 'CISCO-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-DIAL-CONTROL-MIB']),
    'CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.CcallhistoryreleasesrcEnum' : _MetaInfoEnum('CcallhistoryreleasesrcEnum', 'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB',
        {
            'callingPartyInPstn':'callingPartyInPstn',
            'callingPartyInVoip':'callingPartyInVoip',
            'calledPartyInPstn':'calledPartyInPstn',
            'calledPartyInVoip':'calledPartyInVoip',
            'internalReleaseInPotsLeg':'internalReleaseInPotsLeg',
            'internalReleaseInVoipLeg':'internalReleaseInVoipLeg',
            'internalCallControlApp':'internalCallControlApp',
            'internalReleaseInVoipAAA':'internalReleaseInVoipAAA',
            'consoleCommand':'consoleCommand',
            'externalRadiusServer':'externalRadiusServer',
            'externalNmsApp':'externalNmsApp',
            'externalCallControlAgent':'externalCallControlAgent',
            'gatekeeper':'gatekeeper',
            'externalGKTMPServer':'externalGKTMPServer',
        }, 'CISCO-DIAL-CONTROL-MIB', _yang_ns._namespaces['CISCO-DIAL-CONTROL-MIB']),
    'CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry' : {
        'meta_info' : _MetaInfoClass('CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry',
            False, 
            [
            _MetaInfoClassMember('cCallHistoryIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                A monotonically increasing integer for the sole purpose of
                indexing call disconnection events.  When it reaches the 
                maximum value, an extremely unlikely event, the agent wraps 
                the value back to 1 and may flush existing entries.
                ''',
                'ccallhistoryindex',
                'CISCO-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cCallHistoryCallOrigin', REFERENCE_ENUM_CLASS, 'CcallhistorycalloriginEnum' , 'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB', 'CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.CcallhistorycalloriginEnum', 
                [], [], 
                '''                The call origin.
                ''',
                'ccallhistorycallorigin',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistoryChargedUnits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of charged units for this connection.
                For incoming calls or if charging information is
                not supplied by the switch, the value of this object
                will be zero.
                ''',
                'ccallhistorychargedunits',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistoryConnectTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the call was connected.
                ''',
                'ccallhistoryconnecttime',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistoryDisconnectCause', ATTRIBUTE, 'str' , None, None, 
                [(0, 4)], [], 
                '''                The encoded network cause value associated with this call.
                
                The value of this object will depend on the interface type
                as well as on the protocol and protocol version being
                used on this interface. Some references for possible cause
                values are given below.
                ''',
                'ccallhistorydisconnectcause',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistoryDisconnectText', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ASCII text describing the reason for call termination.
                
                This object exists because it would be impossible for
                a management station to store all possible cause values
                for all types of interfaces. It should be used only if
                a management station is unable to decode the value of
                dialCtlPeerStatsLastDisconnectCause.
                ''',
                'ccallhistorydisconnecttext',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistoryDisconnectTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the call was disconnected.
                ''',
                'ccallhistorydisconnecttime',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistoryInfoType', REFERENCE_ENUM_CLASS, 'CcallhistoryinfotypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB', 'CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.CcallhistoryinfotypeEnum', 
                [], [], 
                '''                The information type for this call.
                ''',
                'ccallhistoryinfotype',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistoryLogicalIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This is the ifIndex value of the logical interface through
                which this call was made. For ISDN media, this would be
                the ifIndex of the B channel which was used for this call.
                If the ifIndex value is unknown, the value of this object 
                will be zero. For an IP call, the value will be zero.
                ''',
                'ccallhistorylogicalifindex',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistoryPeerAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The number this call was connected to. If the number is
                not available, then it will have a length of zero.
                ''',
                'ccallhistorypeeraddress',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistoryPeerId', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This is the Id value of the peer table entry
                to which this call was made. If a peer table entry
                for this call does not exist, the value of this object
                will be zero.
                ''',
                'ccallhistorypeerid',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistoryPeerIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This is the ifIndex value of the peer table entry
                to which this call was made. If a peer table entry
                for this call does not exist, the value of this object
                will be zero.
                ''',
                'ccallhistorypeerifindex',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistoryPeerSubAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The subaddress this call was connected to. If the subaddress
                is undefined or not available, this will be a zero length
                string.
                ''',
                'ccallhistorypeersubaddress',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistoryReceiveBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of bytes which were received while this
                call was active.
                ''',
                'ccallhistoryreceivebytes',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistoryReceivePackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets which were received while this
                call was active.
                ''',
                'ccallhistoryreceivepackets',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistoryReleaseSource', REFERENCE_ENUM_CLASS, 'CcallhistoryreleasesourceEnum' , 'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB', 'CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.CcallhistoryreleasesourceEnum', 
                [], [], 
                '''                Originator of the call release.
                ''',
                'ccallhistoryreleasesource',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistoryReleaseSrc', REFERENCE_ENUM_CLASS, 'CcallhistoryreleasesrcEnum' , 'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB', 'CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry.CcallhistoryreleasesrcEnum', 
                [], [], 
                '''                Originator of the call release. Indicates the source of 
                the call release as follows : 
                1) callingPartyInPstn : Calling party in PSTN.
                2) callingPartyInVoip : Calling party in VoIP.
                3) calledPartyInPstn : Called party in PSTN.
                4) calledPartyInVoip : Called party in VoIP.
                5) internalReleaseInPotsLeg : Due to an internal error 
                   in Telephony call leg.
                6) internalReleaseInVoipLeg : Due to an internal error
                   in VoIP call leg.
                7) internalCallControlApp : Due to an internal error
                   in Session Application or Tcl or VXML script originated
                   release. 
                8) internalReleaseInVoipAAA : Due to an internal error
                   in VoIP AAA module.
                9) consoleCommand : Due to CLI or MML.
                10) externalRadiusServer : Call failed during authorization
                    , authentication or due to receipt of POD from the 
                    RADIUS server.
                11) externalNmsApp : Due to SNMP request to clear 
                    the call.
                12) externalCallControlAgent : External Call Control Agent
                    initiated clear.
                13) gatekeeper : Gatekeeper initiated clear due to receipt
                    of Admission Reject, Disengage Request message.
                14) externalGKTMPServer : External GKTMP server initiated
                    clear due to receipt of Admission Reject message from
                    the gatekeeper, triggered by RESPONSE.ARJ message from
                    the GKTMP server.
                ''',
                'ccallhistoryreleasesrc',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistorySetupTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the call setup was started.
                This will be useful for an NMS to sort the call history
                entry with call setup time. Also, this object
                can be useful in finding large delays between the time the
                call was started and the time the call was connected.
                For ISDN media, this will be the time when the setup
                message was received from or sent to the network.
                The value of this object is the same as callActiveSetupTime
                in the callActiveTable
                ''',
                'ccallhistorysetuptime',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistoryTransmitBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of bytes which were transmitted while this
                call was active.
                ''',
                'ccallhistorytransmitbytes',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistoryTransmitPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets which were transmitted while this
                call was active.
                ''',
                'ccallhistorytransmitpackets',
                'CISCO-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-DIAL-CONTROL-MIB',
            'cCallHistoryEntry',
            _yang_ns._namespaces['CISCO-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoDialControlMib.Ccallhistorytable' : {
        'meta_info' : _MetaInfoClass('CiscoDialControlMib.Ccallhistorytable',
            False, 
            [
            _MetaInfoClassMember('cCallHistoryEntry', REFERENCE_LIST, 'Ccallhistoryentry' , 'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB', 'CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry', 
                [], [], 
                '''                The information regarding a single Connection.
                ''',
                'ccallhistoryentry',
                'CISCO-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-DIAL-CONTROL-MIB',
            'cCallHistoryTable',
            _yang_ns._namespaces['CISCO-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoDialControlMib.Ccallhistoryiectable.Ccallhistoryiecentry' : {
        'meta_info' : _MetaInfoClass('CiscoDialControlMib.Ccallhistoryiectable.Ccallhistoryiecentry',
            False, 
            [
            _MetaInfoClassMember('cCallHistoryIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'ccallhistoryindex',
                'CISCO-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cCallHistoryIecIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '1024')], [], 
                '''                This object is used to index one or more IECs in the
                context of a single call.  In most cases there will
                only be one IEC when a call fails.  However, it is
                possible for the software processing the call to 
                generate multiple IECs before the call ultimately fails.
                In that scenario, there will be multiple entries in
                this table related to a single call (cCallHistoryIndex)
                and this object will serve to uniquely identify each IEC.
                ''',
                'ccallhistoryiecindex',
                'CISCO-DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('cCallHistoryIec', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object reflects the Internal Error Code.
                The format is a string of dotted decimal numbers
                composed of the following components:
                
                Version.Entity.Category.Subsystem.Errorcode.Diagnostic
                
                Each component is defined as follows:
                Version     : The version of IEC software.
                Entity      : The network entity that originated
                              the error.
                Category    : The category of the error (eg, software
                              error, hardware resource unavailable, ...)
                Subsystem   : The subsystem in which the error occurred.
                Errorcode   : A subsytem-specific error code.
                Diagnostic  : An implementation-specific diagnostic code.
                ''',
                'ccallhistoryiec',
                'CISCO-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-DIAL-CONTROL-MIB',
            'cCallHistoryIecEntry',
            _yang_ns._namespaces['CISCO-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoDialControlMib.Ccallhistoryiectable' : {
        'meta_info' : _MetaInfoClass('CiscoDialControlMib.Ccallhistoryiectable',
            False, 
            [
            _MetaInfoClassMember('cCallHistoryIecEntry', REFERENCE_LIST, 'Ccallhistoryiecentry' , 'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB', 'CiscoDialControlMib.Ccallhistoryiectable.Ccallhistoryiecentry', 
                [], [], 
                '''                The IEC information regarding a single call.
                ''',
                'ccallhistoryiecentry',
                'CISCO-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-DIAL-CONTROL-MIB',
            'cCallHistoryIecTable',
            _yang_ns._namespaces['CISCO-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB'
        ),
    },
    'CiscoDialControlMib' : {
        'meta_info' : _MetaInfoClass('CiscoDialControlMib',
            False, 
            [
            _MetaInfoClassMember('cCallHistoryIecTable', REFERENCE_CLASS, 'Ccallhistoryiectable' , 'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB', 'CiscoDialControlMib.Ccallhistoryiectable', 
                [], [], 
                '''                This table contains information about Internal Error
                Code(s) (IEC) which caused the call to fail.
                ''',
                'ccallhistoryiectable',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cCallHistoryTable', REFERENCE_CLASS, 'Ccallhistorytable' , 'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB', 'CiscoDialControlMib.Ccallhistorytable', 
                [], [], 
                '''                A table containing information about specific
                calls to a specific destination.
                ''',
                'ccallhistorytable',
                'CISCO-DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('cPeerGlobalConfiguration', REFERENCE_CLASS, 'Cpeerglobalconfiguration' , 'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB', 'CiscoDialControlMib.Cpeerglobalconfiguration', 
                [], [], 
                '''                ''',
                'cpeerglobalconfiguration',
                'CISCO-DIAL-CONTROL-MIB', False),
            ],
            'CISCO-DIAL-CONTROL-MIB',
            'CISCO-DIAL-CONTROL-MIB',
            _yang_ns._namespaces['CISCO-DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DIAL_CONTROL_MIB'
        ),
    },
}
_meta_table['CiscoDialControlMib.Ccallhistorytable.Ccallhistoryentry']['meta_info'].parent =_meta_table['CiscoDialControlMib.Ccallhistorytable']['meta_info']
_meta_table['CiscoDialControlMib.Ccallhistoryiectable.Ccallhistoryiecentry']['meta_info'].parent =_meta_table['CiscoDialControlMib.Ccallhistoryiectable']['meta_info']
_meta_table['CiscoDialControlMib.Cpeerglobalconfiguration']['meta_info'].parent =_meta_table['CiscoDialControlMib']['meta_info']
_meta_table['CiscoDialControlMib.Ccallhistorytable']['meta_info'].parent =_meta_table['CiscoDialControlMib']['meta_info']
_meta_table['CiscoDialControlMib.Ccallhistoryiectable']['meta_info'].parent =_meta_table['CiscoDialControlMib']['meta_info']
