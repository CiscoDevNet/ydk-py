


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'DialControlMib.Dialctlconfiguration.DialctlacceptmodeEnum' : _MetaInfoEnum('DialctlacceptmodeEnum', 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB',
        {
            'acceptNone':'acceptNone',
            'acceptAll':'acceptAll',
            'acceptKnown':'acceptKnown',
        }, 'DIAL-CONTROL-MIB', _yang_ns._namespaces['DIAL-CONTROL-MIB']),
    'DialControlMib.Dialctlconfiguration.DialctltrapenableEnum' : _MetaInfoEnum('DialctltrapenableEnum', 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'DIAL-CONTROL-MIB', _yang_ns._namespaces['DIAL-CONTROL-MIB']),
    'DialControlMib.Dialctlconfiguration' : {
        'meta_info' : _MetaInfoClass('DialControlMib.Dialctlconfiguration',
            False, 
            [
            _MetaInfoClassMember('dialCtlAcceptMode', REFERENCE_ENUM_CLASS, 'DialctlacceptmodeEnum' , 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB', 'DialControlMib.Dialctlconfiguration.DialctlacceptmodeEnum', 
                [], [], 
                '''                The security level for acceptance of incoming calls.
                acceptNone(1)  - incoming calls will not be accepted
                acceptAll(2)   - incoming calls will be accepted,
                                 even if there is no matching entry
                                 in the dialCtlPeerCfgTable
                acceptKnown(3) - incoming calls will be accepted only
                                 if there is a matching entry in the
                                 dialCtlPeerCfgTable
                ''',
                'dialctlacceptmode',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlTrapEnable', REFERENCE_ENUM_CLASS, 'DialctltrapenableEnum' , 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB', 'DialControlMib.Dialctlconfiguration.DialctltrapenableEnum', 
                [], [], 
                '''                This object indicates whether dialCtlPeerCallInformation
                and dialCtlPeerCallSetup traps should be generated for
                all peers. If the value of this object is enabled(1),
                traps will be generated for all peers. If the value
                of this object is disabled(2), traps will be generated
                only for peers having dialCtlPeerCfgTrapEnable set
                to enabled(1).
                ''',
                'dialctltrapenable',
                'DIAL-CONTROL-MIB', False),
            ],
            'DIAL-CONTROL-MIB',
            'dialCtlConfiguration',
            _yang_ns._namespaces['DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB'
        ),
    },
    'DialControlMib.Callhistory' : {
        'meta_info' : _MetaInfoClass('DialControlMib.Callhistory',
            False, 
            [
            _MetaInfoClassMember('callHistoryRetainTimer', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The minimum amount of time that an callHistoryEntry
                will be maintained before being deleted. A value of
                0 will prevent any history from being retained in the
                callHistoryTable, but will neither prevent callCompletion
                traps being generated nor affect other tables.
                ''',
                'callhistoryretaintimer',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callHistoryTableMaxLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The upper limit on the number of entries that the
                callHistoryTable may contain.  A value of 0
                will prevent any history from being retained. When
                this table is full, the oldest entry will be deleted
                and the new one will be created.
                ''',
                'callhistorytablemaxlength',
                'DIAL-CONTROL-MIB', False),
            ],
            'DIAL-CONTROL-MIB',
            'callHistory',
            _yang_ns._namespaces['DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB'
        ),
    },
    'DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry.DialctlpeercfginfotypeEnum' : _MetaInfoEnum('DialctlpeercfginfotypeEnum', 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB',
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
        }, 'DIAL-CONTROL-MIB', _yang_ns._namespaces['DIAL-CONTROL-MIB']),
    'DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry.DialctlpeercfgpermissionEnum' : _MetaInfoEnum('DialctlpeercfgpermissionEnum', 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB',
        {
            'originate':'originate',
            'answer':'answer',
            'both':'both',
            'callback':'callback',
            'none':'none',
        }, 'DIAL-CONTROL-MIB', _yang_ns._namespaces['DIAL-CONTROL-MIB']),
    'DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry.DialctlpeercfgtrapenableEnum' : _MetaInfoEnum('DialctlpeercfgtrapenableEnum', 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'DIAL-CONTROL-MIB', _yang_ns._namespaces['DIAL-CONTROL-MIB']),
    'DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry' : {
        'meta_info' : _MetaInfoClass('DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry',
            False, 
            [
            _MetaInfoClassMember('dialCtlPeerCfgId', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This object identifies a single peer. There may
                be several entries in this table for one peer,
                defining different ways of reaching this peer.
                Thus, there may be several entries in this table
                with the same value of dialCtlPeerCfgId.
                Multiple entries for one peer may be used to support
                multilink as well as backup lines.
                A single peer will be identified by a unique value
                of this object. Several entries for one peer MUST
                have the same value of dialCtlPeerCfgId, but different
                ifEntries and thus different values of ifIndex.
                ''',
                'dialctlpeercfgid',
                'DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('dialCtlPeerCfgAnswerAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Calling Party Number information element, as for example
                passed in an ISDN SETUP message by a PBX or switch,
                for incoming calls.
                This address can be used to identify the peer.
                If this address is either unknown or identical
                to dialCtlPeerCfgOriginateAddress, this object will be
                a zero length string.
                ''',
                'dialctlpeercfgansweraddress',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerCfgCallRetries', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The number of calls to a non-responding address
                that may be made. A retry count of zero means
                there is no bound. The intent is to bound
                the number of successive calls to an address
                which is inaccessible, or which refuses those calls.
                
                Some countries regulate the number of call retries
                to a given peer that can be made.
                ''',
                'dialctlpeercfgcallretries',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerCfgCarrierDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The call timeout time in seconds. The default value
                of zero means that the call timeout as specified for
                the media in question will apply.
                ''',
                'dialctlpeercfgcarrierdelay',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerCfgClosedUserGroup', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Closed User Group at which the peer will be called.
                If the Closed User Group is undefined for the given media
                or unused, this is a zero length string.
                ''',
                'dialctlpeercfgclosedusergroup',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerCfgFailureDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The time in seconds after which call attempts are
                to be placed again after a peer has been noticed
                to be unreachable, i.e. after dialCtlPeerCfgCallRetries
                unsuccessful call attempts.
                A value of zero means that a peer will not be called
                again after dialCtlPeerCfgCallRetries unsuccessful call
                attempts.
                ''',
                'dialctlpeercfgfailuredelay',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerCfgIfType', REFERENCE_ENUM_CLASS, 'IanaiftypeEnum' , 'ydk.models.cisco_ios_xe.IANAifType_MIB', 'IanaiftypeEnum', 
                [], [], 
                '''                The interface type to be used for calling this peer.
                In case of ISDN, the value of isdn(63) is to be used.
                ''',
                'dialctlpeercfgiftype',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerCfgInactivityTimer', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The connection will be automatically disconnected
                if no longer carrying useful data for a time
                period, in seconds, specified in this object.
                Useful data in this context refers to forwarding
                packets, including routing information; it
                excludes the encapsulator maintenance frames.
                A value of zero means the connection will not be
                automatically taken down due to inactivity,
                which implies that it is a dedicated circuit.
                ''',
                'dialctlpeercfginactivitytimer',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerCfgInfoType', REFERENCE_ENUM_CLASS, 'DialctlpeercfginfotypeEnum' , 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB', 'DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry.DialctlpeercfginfotypeEnum', 
                [], [], 
                '''                The Information Transfer Capability to be used when
                calling this peer.
                
                speech(2) refers to a non-data connection, whereas
                audio31(6) and audio7(7) refer to data mode
                connections.
                ''',
                'dialctlpeercfginfotype',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerCfgLowerIf', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                ifIndex value of an interface the peer will have to be
                called on. For example, on an ISDN interface, this can be
                the ifIndex value of a D channel or the ifIndex value of a
                B channel, whatever is appropriate for a given peer.
                As an example, for Basic Rate leased lines it will be
                necessary to specify a B channel ifIndex, while for
                
                
                
                
                semi-permanent connections the D channel ifIndex has
                to be specified.
                If the interface can be dynamically assigned, this object
                has a value of zero.
                ''',
                'dialctlpeercfglowerif',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerCfgMaxDuration', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Maximum call duration in seconds. Zero means 'unlimited'.
                ''',
                'dialctlpeercfgmaxduration',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerCfgMinDuration', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Minimum duration of a call in seconds, starting from the
                time the call is connected until the call is disconnected.
                This is to accomplish the fact that in most countries
                charging applies to units of time, which should be matched
                as closely as possible.
                ''',
                'dialctlpeercfgminduration',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerCfgOriginateAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Call Address at which the peer will be called.
                Think of this as the set of characters following 'ATDT '
                or the 'phone number' included in a D channel call request.
                
                The structure of this information will be switch type
                specific. If there is no address information required
                for reaching the peer, i.e., for leased lines,
                this object will be a zero length string.
                ''',
                'dialctlpeercfgoriginateaddress',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerCfgPermission', REFERENCE_ENUM_CLASS, 'DialctlpeercfgpermissionEnum' , 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB', 'DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry.DialctlpeercfgpermissionEnum', 
                [], [], 
                '''                Applicable permissions. callback(4) either rejects the
                call and then calls back, or uses the 'Reverse charging'
                information element if it is available.
                Note that callback(4) is supposed to control charging, not
                security, and applies to callback prior to accepting a
                call. Callback for security reasons can be handled using
                PPP callback.
                ''',
                'dialctlpeercfgpermission',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerCfgRetryDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The time in seconds between call retries if a peer
                cannot be reached.
                A value of zero means that call retries may be done
                without any delay.
                ''',
                'dialctlpeercfgretrydelay',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerCfgSpeed', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The desired information transfer speed in bits/second
                when calling this peer.
                The detailed media specific information, e.g. information
                type and information transfer rate for ISDN circuits,
                has to be extracted from this object.
                If the transfer speed to be used is unknown or the default
                speed for this type of interfaces, the value of this object
                may be zero.
                ''',
                'dialctlpeercfgspeed',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerCfgStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                Status of one row in this table.
                ''',
                'dialctlpeercfgstatus',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerCfgSubAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Subaddress at which the peer will be called.
                If the subaddress is undefined for the given media or
                unused, this is a zero length string.
                ''',
                'dialctlpeercfgsubaddress',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerCfgTrapEnable', REFERENCE_ENUM_CLASS, 'DialctlpeercfgtrapenableEnum' , 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB', 'DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry.DialctlpeercfgtrapenableEnum', 
                [], [], 
                '''                This object indicates whether dialCtlPeerCallInformation
                and dialCtlPeerCallSetup traps should be generated for
                this peer.
                ''',
                'dialctlpeercfgtrapenable',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerStatsAcceptCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of calls from this peer accepted since system
                startup.
                ''',
                'dialctlpeerstatsacceptcalls',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerStatsChargedUnits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of charging units applying to this
                peer since system startup.
                Only the charging units applying to the local interface,
                i.e. for originated calls or for calls with 'Reverse
                charging' being active, will be counted here.
                ''',
                'dialctlpeerstatschargedunits',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerStatsConnectTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Accumulated connect time to the peer since system startup.
                This is the total connect time, i.e. the connect time
                for outgoing calls plus the time for incoming calls.
                ''',
                'dialctlpeerstatsconnecttime',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerStatsFailCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of failed call attempts to this peer since system
                startup.
                ''',
                'dialctlpeerstatsfailcalls',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerStatsLastDisconnectCause', ATTRIBUTE, 'str' , None, None, 
                [(0, 4)], [], 
                '''                The encoded network cause value associated with the last
                call.
                This object will be updated whenever a call is started
                or cleared.
                The value of this object will depend on the interface type
                as well as on the protocol and protocol version being
                used on this interface. Some references for possible cause
                values are given below.
                ''',
                'dialctlpeerstatslastdisconnectcause',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerStatsLastDisconnectText', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ASCII text describing the reason for the last call
                termination.
                
                This object exists because it would be impossible for
                a management station to store all possible cause values
                for all types of interfaces. It should be used only if
                a management station is unable to decode the value of
                dialCtlPeerStatsLastDisconnectCause.
                
                This object will be updated whenever a call is started
                or cleared.
                ''',
                'dialctlpeerstatslastdisconnecttext',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerStatsLastSetupTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the last call to this peer
                was started.
                For ISDN media, this will be the time when the setup
                message was received from or sent to the network.
                This object will be updated whenever a call is started
                or cleared.
                ''',
                'dialctlpeerstatslastsetuptime',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerStatsRefuseCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of calls from this peer refused since system
                startup.
                ''',
                'dialctlpeerstatsrefusecalls',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerStatsSuccessCalls', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of completed calls to this peer.
                ''',
                'dialctlpeerstatssuccesscalls',
                'DIAL-CONTROL-MIB', False),
            ],
            'DIAL-CONTROL-MIB',
            'dialCtlPeerCfgEntry',
            _yang_ns._namespaces['DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB'
        ),
    },
    'DialControlMib.Dialctlpeercfgtable' : {
        'meta_info' : _MetaInfoClass('DialControlMib.Dialctlpeercfgtable',
            False, 
            [
            _MetaInfoClassMember('dialCtlPeerCfgEntry', REFERENCE_LIST, 'Dialctlpeercfgentry' , 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB', 'DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry', 
                [], [], 
                '''                Configuration data for a single Peer. This entry is
                effectively permanent, and contains information
                to identify the peer, how to connect to the peer,
                how to identify the peer and its permissions.
                The value of dialCtlPeerCfgOriginateAddress must be
                specified before a new row in this table can become
                active(1). Any writeable parameters in an existing entry
                can be modified while the entry is active. The modification
                will take effect when the peer in question will be
                called the next time.
                An entry in this table can only be created if the
                associated ifEntry already exists.
                ''',
                'dialctlpeercfgentry',
                'DIAL-CONTROL-MIB', False),
            ],
            'DIAL-CONTROL-MIB',
            'dialCtlPeerCfgTable',
            _yang_ns._namespaces['DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB'
        ),
    },
    'DialControlMib.Callactivetable.Callactiveentry.CallactivecalloriginEnum' : _MetaInfoEnum('CallactivecalloriginEnum', 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB',
        {
            'originate':'originate',
            'answer':'answer',
            'callback':'callback',
        }, 'DIAL-CONTROL-MIB', _yang_ns._namespaces['DIAL-CONTROL-MIB']),
    'DialControlMib.Callactivetable.Callactiveentry.CallactivecallstateEnum' : _MetaInfoEnum('CallactivecallstateEnum', 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB',
        {
            'unknown':'unknown',
            'connecting':'connecting',
            'connected':'connected',
            'active':'active',
        }, 'DIAL-CONTROL-MIB', _yang_ns._namespaces['DIAL-CONTROL-MIB']),
    'DialControlMib.Callactivetable.Callactiveentry.CallactiveinfotypeEnum' : _MetaInfoEnum('CallactiveinfotypeEnum', 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB',
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
        }, 'DIAL-CONTROL-MIB', _yang_ns._namespaces['DIAL-CONTROL-MIB']),
    'DialControlMib.Callactivetable.Callactiveentry' : {
        'meta_info' : _MetaInfoClass('DialControlMib.Callactivetable.Callactiveentry',
            False, 
            [
            _MetaInfoClassMember('callActiveSetupTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the call associated to this
                entry was started. This will be useful for an NMS to
                retrieve all calls after a specific time. Also, this object
                can be useful in finding large delays between the time the
                call was started and the time the call was connected.
                For ISDN media, this will be the time when the setup
                message was received from or sent to the network.
                ''',
                'callactivesetuptime',
                'DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('callActiveIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                Small index variable to distinguish calls that start in
                the same hundredth of a second.
                ''',
                'callactiveindex',
                'DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('callActiveCallOrigin', REFERENCE_ENUM_CLASS, 'CallactivecalloriginEnum' , 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB', 'DialControlMib.Callactivetable.Callactiveentry.CallactivecalloriginEnum', 
                [], [], 
                '''                The call origin.
                ''',
                'callactivecallorigin',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callActiveCallState', REFERENCE_ENUM_CLASS, 'CallactivecallstateEnum' , 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB', 'DialControlMib.Callactivetable.Callactiveentry.CallactivecallstateEnum', 
                [], [], 
                '''                The current call state.
                unknown(1)     - The call state is unknown.
                connecting(2)  - A connection attempt (outgoing call)
                                 is being made.
                connected(3)   - An incoming call is in the process
                                 of validation.
                active(4)      - The call is active.
                ''',
                'callactivecallstate',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callActiveChargedUnits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of charged units for this connection.
                For incoming calls or if charging information is
                not supplied by the switch, the value of this object
                will be zero.
                ''',
                'callactivechargedunits',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callActiveConnectTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the call was connected.
                If the call is not connected, this object will have a
                value of zero.
                ''',
                'callactiveconnecttime',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callActiveInfoType', REFERENCE_ENUM_CLASS, 'CallactiveinfotypeEnum' , 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB', 'DialControlMib.Callactivetable.Callactiveentry.CallactiveinfotypeEnum', 
                [], [], 
                '''                The information type for this call.
                ''',
                'callactiveinfotype',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callActiveLogicalIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This is the ifIndex value of the logical interface through
                which this call was made. For ISDN media, this would be
                the ifIndex of the B channel which was used for this call.
                If the ifIndex value is unknown, the value of this object
                will be zero.
                ''',
                'callactivelogicalifindex',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callActivePeerAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The number this call is connected to. If the number is
                not available, then it will have a length of zero.
                ''',
                'callactivepeeraddress',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callActivePeerId', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This is the Id value of the peer table entry
                to which this call was made. If a peer table entry
                for this call does not exist or is unknown, the value
                of this object will be zero.
                ''',
                'callactivepeerid',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callActivePeerIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This is the ifIndex value of the peer table entry
                to which this call was made. If a peer table entry
                for this call does not exist or is unknown, the value
                of this object will be zero.
                ''',
                'callactivepeerifindex',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callActivePeerSubAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The subaddress this call is connected to. If the subaddress
                is undefined or not available, this will be a zero length
                string.
                ''',
                'callactivepeersubaddress',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callActiveReceiveBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of bytes which were received for this call.
                ''',
                'callactivereceivebytes',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callActiveReceivePackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets which were received for this
                call.
                ''',
                'callactivereceivepackets',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callActiveTransmitBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of bytes which were transmitted for this
                call.
                ''',
                'callactivetransmitbytes',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callActiveTransmitPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets which were transmitted for this
                call.
                ''',
                'callactivetransmitpackets',
                'DIAL-CONTROL-MIB', False),
            ],
            'DIAL-CONTROL-MIB',
            'callActiveEntry',
            _yang_ns._namespaces['DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB'
        ),
    },
    'DialControlMib.Callactivetable' : {
        'meta_info' : _MetaInfoClass('DialControlMib.Callactivetable',
            False, 
            [
            _MetaInfoClassMember('callActiveEntry', REFERENCE_LIST, 'Callactiveentry' , 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB', 'DialControlMib.Callactivetable.Callactiveentry', 
                [], [], 
                '''                The information regarding a single active Connection.
                An entry in this table will be created when a call is
                started. An entry in this table will be deleted when
                an active call clears.
                ''',
                'callactiveentry',
                'DIAL-CONTROL-MIB', False),
            ],
            'DIAL-CONTROL-MIB',
            'callActiveTable',
            _yang_ns._namespaces['DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB'
        ),
    },
    'DialControlMib.Callhistorytable.Callhistoryentry.CallhistorycalloriginEnum' : _MetaInfoEnum('CallhistorycalloriginEnum', 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB',
        {
            'originate':'originate',
            'answer':'answer',
            'callback':'callback',
        }, 'DIAL-CONTROL-MIB', _yang_ns._namespaces['DIAL-CONTROL-MIB']),
    'DialControlMib.Callhistorytable.Callhistoryentry.CallhistoryinfotypeEnum' : _MetaInfoEnum('CallhistoryinfotypeEnum', 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB',
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
        }, 'DIAL-CONTROL-MIB', _yang_ns._namespaces['DIAL-CONTROL-MIB']),
    'DialControlMib.Callhistorytable.Callhistoryentry' : {
        'meta_info' : _MetaInfoClass('DialControlMib.Callhistorytable.Callhistoryentry',
            False, 
            [
            _MetaInfoClassMember('callActiveSetupTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'callactivesetuptime',
                'DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('callActiveIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'callactiveindex',
                'DIAL-CONTROL-MIB', True),
            _MetaInfoClassMember('callHistoryCallOrigin', REFERENCE_ENUM_CLASS, 'CallhistorycalloriginEnum' , 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB', 'DialControlMib.Callhistorytable.Callhistoryentry.CallhistorycalloriginEnum', 
                [], [], 
                '''                The call origin.
                ''',
                'callhistorycallorigin',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callHistoryChargedUnits', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of charged units for this connection.
                For incoming calls or if charging information is
                not supplied by the switch, the value of this object
                will be zero.
                ''',
                'callhistorychargedunits',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callHistoryConnectTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the call was connected.
                ''',
                'callhistoryconnecttime',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callHistoryDisconnectCause', ATTRIBUTE, 'str' , None, None, 
                [(0, 4)], [], 
                '''                The encoded network cause value associated with this call.
                
                The value of this object will depend on the interface type
                as well as on the protocol and protocol version being
                used on this interface. Some references for possible cause
                values are given below.
                ''',
                'callhistorydisconnectcause',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callHistoryDisconnectText', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ASCII text describing the reason for call termination.
                
                This object exists because it would be impossible for
                a management station to store all possible cause values
                for all types of interfaces. It should be used only if
                a management station is unable to decode the value of
                dialCtlPeerStatsLastDisconnectCause.
                ''',
                'callhistorydisconnecttext',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callHistoryDisconnectTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the call was disconnected.
                ''',
                'callhistorydisconnecttime',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callHistoryInfoType', REFERENCE_ENUM_CLASS, 'CallhistoryinfotypeEnum' , 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB', 'DialControlMib.Callhistorytable.Callhistoryentry.CallhistoryinfotypeEnum', 
                [], [], 
                '''                The information type for this call.
                ''',
                'callhistoryinfotype',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callHistoryLogicalIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This is the ifIndex value of the logical interface through
                which this call was made. For ISDN media, this would be
                the ifIndex of the B channel which was used for this call.
                ''',
                'callhistorylogicalifindex',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callHistoryPeerAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The number this call was connected to. If the number is
                not available, then it will have a length of zero.
                ''',
                'callhistorypeeraddress',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callHistoryPeerId', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This is the Id value of the peer table entry
                to which this call was made. If a peer table entry
                for this call does not exist, the value of this object
                will be zero.
                ''',
                'callhistorypeerid',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callHistoryPeerIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This is the ifIndex value of the peer table entry
                to which this call was made. If a peer table entry
                for this call does not exist, the value of this object
                will be zero.
                ''',
                'callhistorypeerifindex',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callHistoryPeerSubAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The subaddress this call was connected to. If the subaddress
                is undefined or not available, this will be a zero length
                string.
                ''',
                'callhistorypeersubaddress',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callHistoryReceiveBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of bytes which were received while this
                call was active.
                ''',
                'callhistoryreceivebytes',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callHistoryReceivePackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets which were received while this
                call was active.
                ''',
                'callhistoryreceivepackets',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callHistoryTransmitBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of bytes which were transmitted while this
                call was active.
                ''',
                'callhistorytransmitbytes',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callHistoryTransmitPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets which were transmitted while this
                call was active.
                ''',
                'callhistorytransmitpackets',
                'DIAL-CONTROL-MIB', False),
            ],
            'DIAL-CONTROL-MIB',
            'callHistoryEntry',
            _yang_ns._namespaces['DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB'
        ),
    },
    'DialControlMib.Callhistorytable' : {
        'meta_info' : _MetaInfoClass('DialControlMib.Callhistorytable',
            False, 
            [
            _MetaInfoClassMember('callHistoryEntry', REFERENCE_LIST, 'Callhistoryentry' , 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB', 'DialControlMib.Callhistorytable.Callhistoryentry', 
                [], [], 
                '''                The information regarding a single Connection.
                ''',
                'callhistoryentry',
                'DIAL-CONTROL-MIB', False),
            ],
            'DIAL-CONTROL-MIB',
            'callHistoryTable',
            _yang_ns._namespaces['DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB'
        ),
    },
    'DialControlMib' : {
        'meta_info' : _MetaInfoClass('DialControlMib',
            False, 
            [
            _MetaInfoClassMember('callActiveTable', REFERENCE_CLASS, 'Callactivetable' , 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB', 'DialControlMib.Callactivetable', 
                [], [], 
                '''                A table containing information about active
                calls to a specific destination.
                ''',
                'callactivetable',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callHistory', REFERENCE_CLASS, 'Callhistory' , 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB', 'DialControlMib.Callhistory', 
                [], [], 
                '''                ''',
                'callhistory',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('callHistoryTable', REFERENCE_CLASS, 'Callhistorytable' , 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB', 'DialControlMib.Callhistorytable', 
                [], [], 
                '''                A table containing information about specific
                calls to a specific destination.
                ''',
                'callhistorytable',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlConfiguration', REFERENCE_CLASS, 'Dialctlconfiguration' , 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB', 'DialControlMib.Dialctlconfiguration', 
                [], [], 
                '''                ''',
                'dialctlconfiguration',
                'DIAL-CONTROL-MIB', False),
            _MetaInfoClassMember('dialCtlPeerCfgTable', REFERENCE_CLASS, 'Dialctlpeercfgtable' , 'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB', 'DialControlMib.Dialctlpeercfgtable', 
                [], [], 
                '''                The list of peers from which the managed device
                will accept calls or to which it will place them.
                ''',
                'dialctlpeercfgtable',
                'DIAL-CONTROL-MIB', False),
            ],
            'DIAL-CONTROL-MIB',
            'DIAL-CONTROL-MIB',
            _yang_ns._namespaces['DIAL-CONTROL-MIB'],
        'ydk.models.cisco_ios_xe.DIAL_CONTROL_MIB'
        ),
    },
}
_meta_table['DialControlMib.Dialctlpeercfgtable.Dialctlpeercfgentry']['meta_info'].parent =_meta_table['DialControlMib.Dialctlpeercfgtable']['meta_info']
_meta_table['DialControlMib.Callactivetable.Callactiveentry']['meta_info'].parent =_meta_table['DialControlMib.Callactivetable']['meta_info']
_meta_table['DialControlMib.Callhistorytable.Callhistoryentry']['meta_info'].parent =_meta_table['DialControlMib.Callhistorytable']['meta_info']
_meta_table['DialControlMib.Dialctlconfiguration']['meta_info'].parent =_meta_table['DialControlMib']['meta_info']
_meta_table['DialControlMib.Callhistory']['meta_info'].parent =_meta_table['DialControlMib']['meta_info']
_meta_table['DialControlMib.Dialctlpeercfgtable']['meta_info'].parent =_meta_table['DialControlMib']['meta_info']
_meta_table['DialControlMib.Callactivetable']['meta_info'].parent =_meta_table['DialControlMib']['meta_info']
_meta_table['DialControlMib.Callhistorytable']['meta_info'].parent =_meta_table['DialControlMib']['meta_info']
