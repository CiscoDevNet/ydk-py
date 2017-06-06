


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'FrameRelayDteMib.Framerelaytrapcontrol.FrtrapstateEnum' : _MetaInfoEnum('FrtrapstateEnum', 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'FRAME-RELAY-DTE-MIB', _yang_ns._namespaces['FRAME-RELAY-DTE-MIB']),
    'FrameRelayDteMib.Framerelaytrapcontrol' : {
        'meta_info' : _MetaInfoClass('FrameRelayDteMib.Framerelaytrapcontrol',
            False, 
            [
            _MetaInfoClassMember('frTrapMaxRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600000')], [], 
                '''                This variable indicates the number of milliseconds
                that must elapse between trap emissions.  If events
                occur more rapidly, the impementation may simply fail
                to trap, or may queue traps until an appropriate time.
                ''',
                'frtrapmaxrate',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frTrapState', REFERENCE_ENUM_CLASS, 'FrtrapstateEnum' , 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FrameRelayDteMib.Framerelaytrapcontrol.FrtrapstateEnum', 
                [], [], 
                '''                This variable indicates whether the system produces
                the frDLCIStatusChange trap.
                ''',
                'frtrapstate',
                'FRAME-RELAY-DTE-MIB', False),
            ],
            'FRAME-RELAY-DTE-MIB',
            'frameRelayTrapControl',
            _yang_ns._namespaces['FRAME-RELAY-DTE-MIB'],
        'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB'
        ),
    },
    'FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmiaddressEnum' : _MetaInfoEnum('FrdlcmiaddressEnum', 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB',
        {
            'q921':'q921',
            'q922March90':'q922March90',
            'q922November90':'q922November90',
            'q922':'q922',
        }, 'FRAME-RELAY-DTE-MIB', _yang_ns._namespaces['FRAME-RELAY-DTE-MIB']),
    'FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmiaddresslenEnum' : _MetaInfoEnum('FrdlcmiaddresslenEnum', 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB',
        {
            'twoOctets':'twoOctets',
            'threeOctets':'threeOctets',
            'fourOctets':'fourOctets',
        }, 'FRAME-RELAY-DTE-MIB', _yang_ns._namespaces['FRAME-RELAY-DTE-MIB']),
    'FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmimulticastEnum' : _MetaInfoEnum('FrdlcmimulticastEnum', 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB',
        {
            'nonBroadcast':'nonBroadcast',
            'broadcast':'broadcast',
        }, 'FRAME-RELAY-DTE-MIB', _yang_ns._namespaces['FRAME-RELAY-DTE-MIB']),
    'FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmistateEnum' : _MetaInfoEnum('FrdlcmistateEnum', 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB',
        {
            'noLmiConfigured':'noLmiConfigured',
            'lmiRev1':'lmiRev1',
            'ansiT1617D':'ansiT1617D',
            'ansiT1617B':'ansiT1617B',
            'itut933A':'itut933A',
            'ansiT1617D1994':'ansiT1617D1994',
        }, 'FRAME-RELAY-DTE-MIB', _yang_ns._namespaces['FRAME-RELAY-DTE-MIB']),
    'FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmistatusEnum' : _MetaInfoEnum('FrdlcmistatusEnum', 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB',
        {
            'running':'running',
            'fault':'fault',
            'initializing':'initializing',
        }, 'FRAME-RELAY-DTE-MIB', _yang_ns._namespaces['FRAME-RELAY-DTE-MIB']),
    'FrameRelayDteMib.Frdlcmitable.Frdlcmientry' : {
        'meta_info' : _MetaInfoClass('FrameRelayDteMib.Frdlcmitable.Frdlcmientry',
            False, 
            [
            _MetaInfoClassMember('frDlcmiIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The ifIndex value of the corresponding ifEntry.
                ''',
                'frdlcmiifindex',
                'FRAME-RELAY-DTE-MIB', True),
            _MetaInfoClassMember('frDlcmiAddress', REFERENCE_ENUM_CLASS, 'FrdlcmiaddressEnum' , 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmiaddressEnum', 
                [], [], 
                '''                This variable states which address format is in use on
                the Frame Relay interface.
                ''',
                'frdlcmiaddress',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frDlcmiAddressLen', REFERENCE_ENUM_CLASS, 'FrdlcmiaddresslenEnum' , 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmiaddresslenEnum', 
                [], [], 
                '''                This variable states the address length in octets.  In
                the case of Q922 format, the length indicates the
                entire length of the address including the control
                portion.
                ''',
                'frdlcmiaddresslen',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frDlcmiErrorThreshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                This is the maximum number of unanswered Status
                Enquiries the equipment shall accept before declaring
                the interface down.
                ''',
                'frdlcmierrorthreshold',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frDlcmiFullEnquiryInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Number of status enquiry intervals that pass before
                issuance of a full status enquiry message.
                ''',
                'frdlcmifullenquiryinterval',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frDlcmiMaxSupportedVCs', ATTRIBUTE, 'int' , None, None, 
                [('0', '8388607')], [], 
                '''                The maximum number of Virtual Circuits allowed for
                this interface.  Usually dictated by the Frame Relay
                network.
                
                In response to a SET, if a value less than zero or
                higher than the agent's maximal capability is
                configured, the agent should respond badValue
                ''',
                'frdlcmimaxsupportedvcs',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frDlcmiMonitoredEvents', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                This is the number of status polling intervals over
                which the error threshold is counted.  For example, if
                within 'MonitoredEvents' number of events the station
                receives 'ErrorThreshold' number of errors, the
                interface is marked as down.
                ''',
                'frdlcmimonitoredevents',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frDlcmiMulticast', REFERENCE_ENUM_CLASS, 'FrdlcmimulticastEnum' , 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmimulticastEnum', 
                [], [], 
                '''                This indicates whether the Frame Relay interface is
                using a multicast service.
                ''',
                'frdlcmimulticast',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frDlcmiPollingInterval', ATTRIBUTE, 'int' , None, None, 
                [('5', '30')], [], 
                '''                This is the number of seconds between successive
                status enquiry messages.
                ''',
                'frdlcmipollinginterval',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frDlcmiRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                SNMP Version 2 Row Status Variable.  Writable objects
                in the table may be written in any RowStatus state.
                ''',
                'frdlcmirowstatus',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frDlcmiState', REFERENCE_ENUM_CLASS, 'FrdlcmistateEnum' , 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmistateEnum', 
                [], [], 
                '''                This variable states which Data Link Connection
                Management scheme is active (and by implication, what
                DLCI it uses) on the Frame Relay interface.
                ''',
                'frdlcmistate',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frDlcmiStatus', REFERENCE_ENUM_CLASS, 'FrdlcmistatusEnum' , 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FrameRelayDteMib.Frdlcmitable.Frdlcmientry.FrdlcmistatusEnum', 
                [], [], 
                '''                This indicates the status of the Frame Relay interface
                as determined by the performance of the dlcmi.  If no
                dlcmi is running, the Frame Relay interface will stay
                in the running state indefinitely.
                ''',
                'frdlcmistatus',
                'FRAME-RELAY-DTE-MIB', False),
            ],
            'FRAME-RELAY-DTE-MIB',
            'frDlcmiEntry',
            _yang_ns._namespaces['FRAME-RELAY-DTE-MIB'],
        'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB'
        ),
    },
    'FrameRelayDteMib.Frdlcmitable' : {
        'meta_info' : _MetaInfoClass('FrameRelayDteMib.Frdlcmitable',
            False, 
            [
            _MetaInfoClassMember('frDlcmiEntry', REFERENCE_LIST, 'Frdlcmientry' , 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FrameRelayDteMib.Frdlcmitable.Frdlcmientry', 
                [], [], 
                '''                The Parameters for a particular Data Link Connection
                Management Interface.
                ''',
                'frdlcmientry',
                'FRAME-RELAY-DTE-MIB', False),
            ],
            'FRAME-RELAY-DTE-MIB',
            'frDlcmiTable',
            _yang_ns._namespaces['FRAME-RELAY-DTE-MIB'],
        'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB'
        ),
    },
    'FrameRelayDteMib.Frcircuittable.Frcircuitentry.FrcircuitmulticastEnum' : _MetaInfoEnum('FrcircuitmulticastEnum', 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB',
        {
            'unicast':'unicast',
            'oneWay':'oneWay',
            'twoWay':'twoWay',
            'nWay':'nWay',
        }, 'FRAME-RELAY-DTE-MIB', _yang_ns._namespaces['FRAME-RELAY-DTE-MIB']),
    'FrameRelayDteMib.Frcircuittable.Frcircuitentry.FrcircuitstateEnum' : _MetaInfoEnum('FrcircuitstateEnum', 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB',
        {
            'invalid':'invalid',
            'active':'active',
            'inactive':'inactive',
        }, 'FRAME-RELAY-DTE-MIB', _yang_ns._namespaces['FRAME-RELAY-DTE-MIB']),
    'FrameRelayDteMib.Frcircuittable.Frcircuitentry.FrcircuittypeEnum' : _MetaInfoEnum('FrcircuittypeEnum', 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB',
        {
            'static':'static',
            'dynamic':'dynamic',
        }, 'FRAME-RELAY-DTE-MIB', _yang_ns._namespaces['FRAME-RELAY-DTE-MIB']),
    'FrameRelayDteMib.Frcircuittable.Frcircuitentry' : {
        'meta_info' : _MetaInfoClass('FrameRelayDteMib.Frcircuittable.Frcircuitentry',
            False, 
            [
            _MetaInfoClassMember('frCircuitIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The ifIndex Value of the ifEntry this virtual circuit
                is layered onto.
                ''',
                'frcircuitifindex',
                'FRAME-RELAY-DTE-MIB', True),
            _MetaInfoClassMember('frCircuitDlci', ATTRIBUTE, 'int' , None, None, 
                [('0', '8388607')], [], 
                '''                The Data Link Connection Identifier for this virtual
                circuit.
                ''',
                'frcircuitdlci',
                'FRAME-RELAY-DTE-MIB', True),
            _MetaInfoClassMember('frCircuitCommittedBurst', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This variable indicates the maximum amount of data, in
                bits, that the network agrees to transfer under normal
                conditions, during the measurement interval.
                ''',
                'frcircuitcommittedburst',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitCreationTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the virtual circuit was
                created, whether by the Data Link Connection Management
                Interface or by a SetRequest.
                ''',
                'frcircuitcreationtime',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitDiscards', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of inbound frames dropped because of format
                errors, or because the VC is inactive.
                ''',
                'frcircuitdiscards',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitExcessBurst', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This variable indicates the maximum amount of
                uncommitted data bits that the network will attempt to
                deliver over the measurement interval.
                
                By default, if not configured when creating the entry,
                the Excess Information Burst Size is set to the value
                of ifSpeed.
                ''',
                'frcircuitexcessburst',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitLastTimeChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when last there was a change in
                the virtual circuit state
                ''',
                'frcircuitlasttimechange',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitLogicalIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                Normally the same value as frDlcmiIfIndex, but
                different when an implementation associates a virtual
                ifEntry with a DLC or set of DLCs in order to associate
                higher layer objects such as the ipAddrEntry with a
                subset of the virtual circuits on a Frame Relay
                interface. The type of such ifEntries is defined by the
                higher layer object; for example, if PPP/Frame Relay is
                implemented, the ifType of this ifEntry would be PPP.
                If it is not so defined, as would be the case with an
                ipAddrEntry, it should be of type Other.
                ''',
                'frcircuitlogicalifindex',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitMulticast', REFERENCE_ENUM_CLASS, 'FrcircuitmulticastEnum' , 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FrameRelayDteMib.Frcircuittable.Frcircuitentry.FrcircuitmulticastEnum', 
                [], [], 
                '''                This indicates whether this VC is used as a unicast VC
                (i.e. not multicast) or the type of multicast service
                subscribed to
                ''',
                'frcircuitmulticast',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitReceivedBECNs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of frames received from the network indicating
                backward congestion since the virtual circuit was
                created.  This occurs when the remote DTE sets the BECN
                flag, or when a switch in the network receives the
                frame from a trunk whose transmission queue is
                congested.
                ''',
                'frcircuitreceivedbecns',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitReceivedDEs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of frames received from the network indicating
                that they were eligible for discard since the virtual
                circuit was created.  This occurs when the remote DTE
                sets the DE flag, or when in remote DTE's switch
                detects that the frame was received as Excess Burst
                data.
                ''',
                'frcircuitreceiveddes',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitReceivedFECNs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of frames received from the network indicating
                forward congestion since the virtual circuit was
                created.  This occurs when the remote DTE sets the FECN
                flag, or when a switch in the network enqueues the
                frame to a trunk whose transmission queue is
                congested.
                ''',
                'frcircuitreceivedfecns',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitReceivedFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of frames received over this virtual circuit
                since it was created.
                ''',
                'frcircuitreceivedframes',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitReceivedOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of octets received over this virtual circuit
                since it was created.  Octets counted include the full
                frame relay header, but do not include the flag
                characters or the CRC.
                ''',
                'frcircuitreceivedoctets',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object is used to create a new row or modify or
                destroy an existing row in the manner described in the
                definition of the RowStatus textual convention.
                Writable objects in the table may be written in any
                RowStatus state.
                ''',
                'frcircuitrowstatus',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitSentDEs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of frames sent to the network indicating that
                they were eligible for discard since the virtual
                circuit was created.   This occurs when the local DTE
                sets the DE flag, indicating that during Network
                congestion situations those frames should be discarded
                in preference of other frames sent without the DE bit
                set.
                ''',
                'frcircuitsentdes',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitSentFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of frames sent from this virtual circuit
                since it was created.
                ''',
                'frcircuitsentframes',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitSentOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of octets sent from this virtual circuit
                since it was created.  Octets counted are the full
                frame relay header and the payload, but do not include
                the flag characters or CRC.
                ''',
                'frcircuitsentoctets',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitState', REFERENCE_ENUM_CLASS, 'FrcircuitstateEnum' , 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FrameRelayDteMib.Frcircuittable.Frcircuitentry.FrcircuitstateEnum', 
                [], [], 
                '''                Indicates whether the particular virtual circuit is
                operational.  In the absence of a Data Link Connection
                Management Interface, virtual circuit entries (rows)
                may be created by setting virtual circuit state to
                'active', or deleted by changing Circuit state to
                'invalid'.
                
                Whether or not the row actually disappears is left to
                the implementation, so this object may actually read as
                'invalid' for some arbitrary length of time.  It is
                also legal to set the state of a virtual circuit to
                'inactive' to temporarily disable a given circuit.
                
                The use of 'invalid' is deprecated in this SNMP Version
                2 MIB, in favor of frCircuitRowStatus.
                ''',
                'frcircuitstate',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitThroughput', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Throughput is the average number of 'Frame Relay
                Information Field' bits transferred per second across a
                user network interface in one direction, measured over
                the measurement interval.
                
                If the configured committed burst rate and throughput
                are both non-zero, the measurement interval, T, is
                    T=frCircuitCommittedBurst/frCircuitThroughput.
                
                If the configured committed burst rate and throughput
                are both zero, the measurement interval, T, is
                           T=frCircuitExcessBurst/ifSpeed.
                ''',
                'frcircuitthroughput',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitType', REFERENCE_ENUM_CLASS, 'FrcircuittypeEnum' , 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FrameRelayDteMib.Frcircuittable.Frcircuitentry.FrcircuittypeEnum', 
                [], [], 
                '''                Indication of whether the VC was manually created
                (static), or dynamically created (dynamic) via the data
                link control management interface.
                ''',
                'frcircuittype',
                'FRAME-RELAY-DTE-MIB', False),
            ],
            'FRAME-RELAY-DTE-MIB',
            'frCircuitEntry',
            _yang_ns._namespaces['FRAME-RELAY-DTE-MIB'],
        'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB'
        ),
    },
    'FrameRelayDteMib.Frcircuittable' : {
        'meta_info' : _MetaInfoClass('FrameRelayDteMib.Frcircuittable',
            False, 
            [
            _MetaInfoClassMember('frCircuitEntry', REFERENCE_LIST, 'Frcircuitentry' , 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FrameRelayDteMib.Frcircuittable.Frcircuitentry', 
                [], [], 
                '''                The information regarding a single Data Link
                Connection.  Discontinuities in the counters contained
                in this table are indicated by the value in
                frCircuitCreationTime.
                ''',
                'frcircuitentry',
                'FRAME-RELAY-DTE-MIB', False),
            ],
            'FRAME-RELAY-DTE-MIB',
            'frCircuitTable',
            _yang_ns._namespaces['FRAME-RELAY-DTE-MIB'],
        'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB'
        ),
    },
    'FrameRelayDteMib.Frerrtable.Frerrentry.FrerrtypeEnum' : _MetaInfoEnum('FrerrtypeEnum', 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB',
        {
            'unknownError':'unknownError',
            'receiveShort':'receiveShort',
            'receiveLong':'receiveLong',
            'illegalAddress':'illegalAddress',
            'unknownAddress':'unknownAddress',
            'dlcmiProtoErr':'dlcmiProtoErr',
            'dlcmiUnknownIE':'dlcmiUnknownIE',
            'dlcmiSequenceErr':'dlcmiSequenceErr',
            'dlcmiUnknownRpt':'dlcmiUnknownRpt',
            'noErrorSinceReset':'noErrorSinceReset',
        }, 'FRAME-RELAY-DTE-MIB', _yang_ns._namespaces['FRAME-RELAY-DTE-MIB']),
    'FrameRelayDteMib.Frerrtable.Frerrentry' : {
        'meta_info' : _MetaInfoClass('FrameRelayDteMib.Frerrtable.Frerrentry',
            False, 
            [
            _MetaInfoClassMember('frErrIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The ifIndex Value of the corresponding ifEntry.
                ''',
                'frerrifindex',
                'FRAME-RELAY-DTE-MIB', True),
            _MetaInfoClassMember('frErrData', ATTRIBUTE, 'str' , None, None, 
                [(1, 1600)], [], 
                '''                An octet string containing as much of the error packet
                as possible.  As a minimum, it must contain the Q.922
                Address or as much as was delivered.  It is desirable
                to include all header and demultiplexing information.
                ''',
                'frerrdata',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frErrFaults', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times the interface has gone down since
                it was initialized.
                ''',
                'frerrfaults',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frErrFaultTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time when the interface
                was taken down due to excessive errors.  Excessive
                errors is defined as the time when a DLCMI exceeds the
                frDlcmiErrorThreshold number of errors within
                frDlcmiMonitoredEvents. See FrDlcmiEntry for further
                details.
                ''',
                'frerrfaulttime',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frErrTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at which the error was
                detected.
                ''',
                'frerrtime',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frErrType', REFERENCE_ENUM_CLASS, 'FrerrtypeEnum' , 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FrameRelayDteMib.Frerrtable.Frerrentry.FrerrtypeEnum', 
                [], [], 
                '''                The type of error that was last seen  on  this interface:
                
                receiveShort: frame was not long enough to allow
                        demultiplexing - the address field was incomplete,
                        or for virtual circuits using Multiprotocol over
                        Frame Relay, the protocol identifier was missing
                        or incomplete.
                
                receiveLong: frame exceeded maximum length configured for this
                             interface.
                
                illegalAddress: address field did not match configured format.
                
                unknownAddress: frame received on a virtual circuit which was not
                                active or administratively disabled.
                
                dlcmiProtoErr: unspecified error occurred when attempting to
                               interpret link maintenance frame.
                
                dlcmiUnknownIE: link maintenance frame contained an Information
                                Element type which is not valid for the
                                configured link maintenance protocol.
                
                dlcmiSequenceErr: link maintenance frame contained a sequence
                                  number other than the expected value.
                
                dlcmiUnknownRpt: link maintenance frame contained a Report Type
                                 Information Element whose value was not valid
                                 for the configured link maintenance protocol.
                
                noErrorSinceReset: no errors have been detected since the last
                                   cold start or warm start.
                ''',
                'frerrtype',
                'FRAME-RELAY-DTE-MIB', False),
            ],
            'FRAME-RELAY-DTE-MIB',
            'frErrEntry',
            _yang_ns._namespaces['FRAME-RELAY-DTE-MIB'],
        'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB'
        ),
    },
    'FrameRelayDteMib.Frerrtable' : {
        'meta_info' : _MetaInfoClass('FrameRelayDteMib.Frerrtable',
            False, 
            [
            _MetaInfoClassMember('frErrEntry', REFERENCE_LIST, 'Frerrentry' , 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FrameRelayDteMib.Frerrtable.Frerrentry', 
                [], [], 
                '''                The error information for a single frame relay
                interface.
                ''',
                'frerrentry',
                'FRAME-RELAY-DTE-MIB', False),
            ],
            'FRAME-RELAY-DTE-MIB',
            'frErrTable',
            _yang_ns._namespaces['FRAME-RELAY-DTE-MIB'],
        'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB'
        ),
    },
    'FrameRelayDteMib' : {
        'meta_info' : _MetaInfoClass('FrameRelayDteMib',
            False, 
            [
            _MetaInfoClassMember('frameRelayTrapControl', REFERENCE_CLASS, 'Framerelaytrapcontrol' , 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FrameRelayDteMib.Framerelaytrapcontrol', 
                [], [], 
                '''                ''',
                'framerelaytrapcontrol',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frCircuitTable', REFERENCE_CLASS, 'Frcircuittable' , 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FrameRelayDteMib.Frcircuittable', 
                [], [], 
                '''                A table containing information about specific Data
                Link Connections (DLC) or virtual circuits.
                ''',
                'frcircuittable',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frDlcmiTable', REFERENCE_CLASS, 'Frdlcmitable' , 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FrameRelayDteMib.Frdlcmitable', 
                [], [], 
                '''                The Parameters for the Data Link Connection Management
                Interface for the frame relay service on this
                interface.
                ''',
                'frdlcmitable',
                'FRAME-RELAY-DTE-MIB', False),
            _MetaInfoClassMember('frErrTable', REFERENCE_CLASS, 'Frerrtable' , 'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB', 'FrameRelayDteMib.Frerrtable', 
                [], [], 
                '''                A table containing information about Errors on the
                Frame Relay interface.  Discontinuities in the counters
                contained in this table are the same as apply to the
                ifEntry associated with the Interface.
                ''',
                'frerrtable',
                'FRAME-RELAY-DTE-MIB', False),
            ],
            'FRAME-RELAY-DTE-MIB',
            'FRAME-RELAY-DTE-MIB',
            _yang_ns._namespaces['FRAME-RELAY-DTE-MIB'],
        'ydk.models.cisco_ios_xe.FRAME_RELAY_DTE_MIB'
        ),
    },
}
_meta_table['FrameRelayDteMib.Frdlcmitable.Frdlcmientry']['meta_info'].parent =_meta_table['FrameRelayDteMib.Frdlcmitable']['meta_info']
_meta_table['FrameRelayDteMib.Frcircuittable.Frcircuitentry']['meta_info'].parent =_meta_table['FrameRelayDteMib.Frcircuittable']['meta_info']
_meta_table['FrameRelayDteMib.Frerrtable.Frerrentry']['meta_info'].parent =_meta_table['FrameRelayDteMib.Frerrtable']['meta_info']
_meta_table['FrameRelayDteMib.Framerelaytrapcontrol']['meta_info'].parent =_meta_table['FrameRelayDteMib']['meta_info']
_meta_table['FrameRelayDteMib.Frdlcmitable']['meta_info'].parent =_meta_table['FrameRelayDteMib']['meta_info']
_meta_table['FrameRelayDteMib.Frcircuittable']['meta_info'].parent =_meta_table['FrameRelayDteMib']['meta_info']
_meta_table['FrameRelayDteMib.Frerrtable']['meta_info'].parent =_meta_table['FrameRelayDteMib']['meta_info']
