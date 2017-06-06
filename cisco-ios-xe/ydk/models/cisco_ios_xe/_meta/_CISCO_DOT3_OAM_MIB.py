


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry.Cdot3OamadminstateEnum' : _MetaInfoEnum('Cdot3OamadminstateEnum', 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB',
        {
            'disabled':'disabled',
            'enabled':'enabled',
        }, 'CISCO-DOT3-OAM-MIB', _yang_ns._namespaces['CISCO-DOT3-OAM-MIB']),
    'CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry.Cdot3OammodeEnum' : _MetaInfoEnum('Cdot3OammodeEnum', 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB',
        {
            'active':'active',
            'passive':'passive',
        }, 'CISCO-DOT3-OAM-MIB', _yang_ns._namespaces['CISCO-DOT3-OAM-MIB']),
    'CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry.Cdot3OamoperstatusEnum' : _MetaInfoEnum('Cdot3OamoperstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB',
        {
            'disabled':'disabled',
            'linkFault':'linkFault',
            'passiveWait':'passiveWait',
            'activeSendLocal':'activeSendLocal',
            'sendLocalAndRemote':'sendLocalAndRemote',
            'sendLocalAndRemoteOk':'sendLocalAndRemoteOk',
            'oamPeeringLocallyRejected':'oamPeeringLocallyRejected',
            'oamPeeringRemotelyRejected':'oamPeeringRemotelyRejected',
            'operational':'operational',
            'nonOperHalfDuplex':'nonOperHalfDuplex',
        }, 'CISCO-DOT3-OAM-MIB', _yang_ns._namespaces['CISCO-DOT3-OAM-MIB']),
    'CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry' : {
        'meta_info' : _MetaInfoClass('CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-DOT3-OAM-MIB', True),
            _MetaInfoClassMember('cdot3OamAdminState', REFERENCE_ENUM_CLASS, 'Cdot3OamadminstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry.Cdot3OamadminstateEnum', 
                [], [], 
                '''                This object is used to provision the default administrative
                OAM mode for this interface.  This object represents the
                desired state of OAM for this interface.  
                
                The cdot3OamAdminState always starts in the disabled(1) state
                until an explicit management action or configuration
                information retained by the system causes a transition to the
                enabled(2) state.   When enabled(2), Ethernet OAM will attempt
                to operate over this interface.  
                ''',
                'cdot3oamadminstate',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamConfigRevision', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The configuration revision of the OAM entity as reflected in
                the latest OAMPDU sent by the OAM entity.  The config revision
                is used by OAM entities to indicate configuration changes have
                occurred which might require the peer OAM entity to
                re-evaluate whether OAM peering is allowed. 
                ''',
                'cdot3oamconfigrevision',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamFunctionsSupported', REFERENCE_BITS, 'Cdot3Oamfunctionssupported' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry.Cdot3Oamfunctionssupported', 
                [], [], 
                '''                The OAM functions supported on this Ethernet like interface.
                OAM consists of separate functional sets beyond the basic
                discovery process which is always required.  These functional
                groups can be supported independently by any implementation.
                These values are communicated to the peer via the local
                configuration field of Information OAMPDUs.  
                
                Setting 'unidirectionalSupport(0)' indicates that the OAM
                entity supports the transmission of OAMPDUs on links that are
                operating in unidirectional mode (traffic flowing in one
                direction only).  Setting 'loopbackSupport(1)' indicates the
                OAM entity can initiate and respond to loopback commands.
                Setting 'eventSupport(2)' indicates the OAM entity can send
                and receive Event Notification OAMPDUs. Setting
                'variableSupport(3)' indicates the OAM entity can send and
                receive Variable Request and Response OAMPDUs.  
                ''',
                'cdot3oamfunctionssupported',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamMaxOamPduSize', ATTRIBUTE, 'int' , None, None, 
                [('64', '1518')], [], 
                '''                The largest OAMPDU that the OAM entity supports.  OAM
                entities exchange maximum OAMPDU sizes and negotiate to use
                the smaller of the two maximum OAMPDU sizes between the peers.
                This value is determined by the local implementation.  
                ''',
                'cdot3oammaxoampdusize',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamMode', REFERENCE_ENUM_CLASS, 'Cdot3OammodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry.Cdot3OammodeEnum', 
                [], [], 
                '''                This object configures the mode of OAM operation for this
                Ethernet like interface.  OAM on Ethernet interfaces may be in
                'active' mode or 'passive' mode.  These two modes differ in
                that active mode provides additional capabilities to initiate
                monitoring activities with the remote OAM peer entity, while
                passive mode generally waits for the peer to initiate OAM
                actions with it.  As an example, an active OAM entity can put
                the remote OAM entity in a loopback state, where a passive OAM
                entity cannot.  
                
                The default value of cdot3OamMode is dependent on the type of
                system on which this Ethernet like interface resides.  The
                default value should be 'active(1)' unless it is known that
                this system should take on a subservient role to the other
                device connected over this interface.  
                
                Changing this value results in incrementing the configuration
                revision field of locally generated OAMPDUs (30.3.6.1.12) and
                potentially re-doing the OAM discovery process if the
                cdot3OamOperStatus was already operational(9).  
                ''',
                'cdot3oammode',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamOperStatus', REFERENCE_ENUM_CLASS, 'Cdot3OamoperstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry.Cdot3OamoperstatusEnum', 
                [], [], 
                '''                At initialization and failure conditions, two OAM entities on
                the same full-duplex Ethernet link begin a discovery phase to
                determine what OAM capabilities may be used on that link.  The
                progress of this initialization is controlled by the OAM
                sublayer.  
                           
                This value is always disabled(1) if OAM is disabled on this
                interface via the cdot3OamAdminState.  
                
                If the link has detected a fault and is transmitting OAMPDUs
                with a link fault indication, the value is linkFault(2). Also,
                if the interface is not operational (ifOperStatus is not 
                up(1)), linkFault(2) is returned.  Note that the object 
                ifOperStatus may not be up(1) as a result of link failure or
                administrative action (ifAdminState being down(2) or
                testing(3)).  
                                 
                The passiveWait(3) state is returned only by OAM entities in
                passive mode (cdot3OamMode) and reflects the state in which the
                OAM entity is waiting to see if the peer device is OAM
                capable.  The activeSendLocal(4) value is used by active mode
                devices (cdot3OamMode) and reflects the OAM entity actively
                trying to discover whether the peer has OAM capability but has
                not yet made that determination.  
                                 
                The state sendLocalAndRemote(5) reflects that the local OAM
                entity has discovered the peer but has not yet accepted or
                rejected the configuration of the peer.  The local device can,
                for whatever reason, decide that the peer device is
                unacceptable and decline OAM peering.  If the local OAM entity
                rejects the peer OAM entity, the state becomes
                oamPeeringLocallyRejected(7).  If the OAM peering is allowed
                by the local device, the state moves to
                sendLocalAndRemoteOk(6).  Note that both the
                sendLocalAndRemote(5) and oamPeeringLocallyRejected(7) states
                fall within the state SEND_LOCAL_REMOTE of the Discovery state
                diagram [802.3ah, Figure 57-5], with the difference being
                whether the local OAM client has actively rejected the peering
                or has just not indicated any decision yet.  Whether a peering
                decision has been made is indicated via the local flags field
                in the OAMPDU (reflected in the aOAMLocalFlagsField of
                30.3.6.1.10).  
                
                If the remote OAM entity rejects the peering, the state
                becomes oamPeeringRemotelyRejected(8).  Note that both the
                sendLocalAndRemoteOk(6) and oamPeeringRemotelyRejected(8)
                states fall within the state SEND_LOCAL_REMOTE_OK of the
                Discovery state diagram [802.3ah, Figure 57-5], with the
                difference being whether the remote OAM client has rejected
                the peering or has just not yet decided.  This is indicated
                via the remote flags field in the OAM PDU (reflected in the
                aOAMRemoteFlagsField of 30.3.6.1.11).  
                                 
                When the local OAM entity learns that both it and the remote
                OAM entity have accepted the peering, the state moves to
                operational(9) corresponding to the SEND_ANY state of the
                Discovery state diagram [802.3ah, Figure 57-5].  
                
                Since Ethernet OAM functions are not designed to work
                completely over half-duplex interfaces, the value
                nonOperHalfDuplex(10) is returned whenever Ethernet OAM is
                enabled (cdot3OamAdminState is enabled(1)) but the interface is
                in half-duplex operation.  
                ''',
                'cdot3oamoperstatus',
                'CISCO-DOT3-OAM-MIB', False),
            ],
            'CISCO-DOT3-OAM-MIB',
            'cdot3OamEntry',
            _yang_ns._namespaces['CISCO-DOT3-OAM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB'
        ),
    },
    'CiscoDot3OamMib.Cdot3Oamtable' : {
        'meta_info' : _MetaInfoClass('CiscoDot3OamMib.Cdot3Oamtable',
            False, 
            [
            _MetaInfoClassMember('cdot3OamEntry', REFERENCE_LIST, 'Cdot3Oamentry' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry', 
                [], [], 
                '''                An entry in the table, containing information on the Ethernet
                OAM function for a single Ethernet like interface. Entries in
                the table are created automatically for each interface
                supporting Ethernet OAM. The status of the row entry can be
                determined from cdot3OamOperStatus.  
                
                A cdot3OamEntry is indexed in the cdot3OamTable by the ifIndex
                object of the Interfaces MIB.  
                ''',
                'cdot3oamentry',
                'CISCO-DOT3-OAM-MIB', False),
            ],
            'CISCO-DOT3-OAM-MIB',
            'cdot3OamTable',
            _yang_ns._namespaces['CISCO-DOT3-OAM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB'
        ),
    },
    'CiscoDot3OamMib.Cdot3Oampeertable.Cdot3Oampeerentry.Cdot3OampeermodeEnum' : _MetaInfoEnum('Cdot3OampeermodeEnum', 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB',
        {
            'active':'active',
            'passive':'passive',
            'unknown':'unknown',
        }, 'CISCO-DOT3-OAM-MIB', _yang_ns._namespaces['CISCO-DOT3-OAM-MIB']),
    'CiscoDot3OamMib.Cdot3Oampeertable.Cdot3Oampeerentry' : {
        'meta_info' : _MetaInfoClass('CiscoDot3OamMib.Cdot3Oampeertable.Cdot3Oampeerentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-DOT3-OAM-MIB', True),
            _MetaInfoClassMember('cdot3OamPeerConfigRevision', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The configuration revision of the OAM peer as reflected in
                the latest OAMPDU.  This attribute is changed by the peer
                whenever it has a local configuration change for Ethernet OAM
                this interface.  The configuration revision can be determined
                from the Revision field of the Local Information TLV of the
                most recently received Information OAMPDU with a Local
                Information TLV. A value of zero is returned if no Local
                Information TLV has been received.  
                ''',
                'cdot3oampeerconfigrevision',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamPeerFunctionsSupported', REFERENCE_BITS, 'Cdot3Oampeerfunctionssupported' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oampeertable.Cdot3Oampeerentry.Cdot3Oampeerfunctionssupported', 
                [], [], 
                '''                The OAM functions supported on this Ethernet like interface.
                OAM consists of separate functionality sets above the basic
                discovery process.  This value indicates the capabilities of
                the peer OAM entity with respect to these functions.  This
                value is initialized so all bits are clear. 
                
                If unidirectionalSupport(0) is set, then the peer OAM entity
                supports sending OAM frames on Ethernet interfaces when the
                receive path is known to be inoperable.   If
                loopbackSupport(1) is set, then the peer OAM entity can send
                and receive OAM loopback commands.  If eventSupport(2) is set,
                then the peer OAM entity can send and receive event OAMPDUs to
                signal various error conditions. If variableSupport(3) is set,
                then the peer OAM entity can send and receive variable
                requests to monitor attribute value as described in Clause 57
                of [802.3ah].   
                
                The capabilities of the OAM peer can be determined from the
                configuration field of the Local Information TLV of the most
                recently received Information OAMPDU with a Local Information
                TLV.  All zeros are returned if no Local Information TLV has
                yet been received. 
                ''',
                'cdot3oampeerfunctionssupported',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamPeerMacAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The MAC address of the peer OAM entity.  The MAC address is
                derived from the most recently received OAMPDU.
                ''',
                'cdot3oampeermacaddress',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamPeerMaxOamPduSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '1518')], [], 
                '''                The maximum size of OAMPDU supported by the peer as reflected
                in the latest Information OAMPDU received with a Local
                Information TLV.   Ethernet OAM on this interface must not use
                OAMPDUs that exceed this size.  The maximum OAMPDU size can be
                determined from the PDU Configuration field of the Local
                Information TLV of the last Information OAMPDU received from
                the peer.  A value of zero is returned if no Local Information
                TLV has been received.  Otherwise, the value of the OAM peer's
                maximum OAMPDU size is returned in this value.  
                Note that the values 1..63 are invalid sizes for Ethernet
                frames and should never appear. 
                ''',
                'cdot3oampeermaxoampdusize',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamPeerMode', REFERENCE_ENUM_CLASS, 'Cdot3OampeermodeEnum' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oampeertable.Cdot3Oampeerentry.Cdot3OampeermodeEnum', 
                [], [], 
                '''                The mode of the OAM peer as reflected in the latest
                Information OAMPDU received with a Local Information TLV.  The
                mode of the peer can be determined from the Configuration
                field in the Local Information TLV of the last Information
                OAMPDU received from the peer.  The value is unknown(3)
                whenever no Local Information TLV has been received.  The
                values of active(1) and passive(2) are returned when a Local
                Information TLV has been received indicating the peer is in
                active or passive mode, respectively. 
                ''',
                'cdot3oampeermode',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamPeerVendorInfo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Vendor Info of the OAM peer as reflected in the latest
                Information OAMPDU received with a Local Information TLV.  The
                vendor information field is within the Local Information TLV,
                and can be used to determine additional information about the
                peer entity.  The format of the vendor information is
                unspecified within the 32-bit field.  This value is
                initialized to zero before any Local Information TLV is
                received.  
                ''',
                'cdot3oampeervendorinfo',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamPeerVendorOui', ATTRIBUTE, 'str' , None, None, 
                [(3, None)], [], 
                '''                The OUI of the OAM peer as reflected in the latest
                Information OAMPDU received with a Local Information TLV.  The
                OUI can be used to identify the vendor of the remote OAM
                entity.  This value is initialized to zero before any Local
                Information TLV is received.  
                ''',
                'cdot3oampeervendoroui',
                'CISCO-DOT3-OAM-MIB', False),
            ],
            'CISCO-DOT3-OAM-MIB',
            'cdot3OamPeerEntry',
            _yang_ns._namespaces['CISCO-DOT3-OAM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB'
        ),
    },
    'CiscoDot3OamMib.Cdot3Oampeertable' : {
        'meta_info' : _MetaInfoClass('CiscoDot3OamMib.Cdot3Oampeertable',
            False, 
            [
            _MetaInfoClassMember('cdot3OamPeerEntry', REFERENCE_LIST, 'Cdot3Oampeerentry' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oampeertable.Cdot3Oampeerentry', 
                [], [], 
                '''                An entry in the table, containing information on the peer OAM
                entity for a single Ethernet like interface.  
                
                Note that there is at most one OAM peer for each Ethernet like
                interface.  Entries are automatically created when information
                about the OAM peer entity becomes available, and automatically
                deleted when the OAM peer entity is no longer in
                communication.  Peer information is not available when
                cdot3OamOperStatus is disabled(1), linkFault(2),
                passiveWait(3), activeSendLocal(4). or nonOperHalfDuplex(10)). 
                ''',
                'cdot3oampeerentry',
                'CISCO-DOT3-OAM-MIB', False),
            ],
            'CISCO-DOT3-OAM-MIB',
            'cdot3OamPeerTable',
            _yang_ns._namespaces['CISCO-DOT3-OAM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB'
        ),
    },
    'CiscoDot3OamMib.Cdot3Oamloopbacktable.Cdot3Oamloopbackentry.Cdot3OamloopbackignorerxEnum' : _MetaInfoEnum('Cdot3OamloopbackignorerxEnum', 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB',
        {
            'ignore':'ignore',
            'process':'process',
        }, 'CISCO-DOT3-OAM-MIB', _yang_ns._namespaces['CISCO-DOT3-OAM-MIB']),
    'CiscoDot3OamMib.Cdot3Oamloopbacktable.Cdot3Oamloopbackentry.Cdot3OamloopbackstatusEnum' : _MetaInfoEnum('Cdot3OamloopbackstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB',
        {
            'noLoopback':'noLoopback',
            'initiatingLoopback':'initiatingLoopback',
            'remoteLoopback':'remoteLoopback',
            'terminatingLoopback':'terminatingLoopback',
            'localLoopback':'localLoopback',
            'unknown':'unknown',
        }, 'CISCO-DOT3-OAM-MIB', _yang_ns._namespaces['CISCO-DOT3-OAM-MIB']),
    'CiscoDot3OamMib.Cdot3Oamloopbacktable.Cdot3Oamloopbackentry' : {
        'meta_info' : _MetaInfoClass('CiscoDot3OamMib.Cdot3Oamloopbacktable.Cdot3Oamloopbackentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-DOT3-OAM-MIB', True),
            _MetaInfoClassMember('cdot3OamLoopbackIgnoreRx', REFERENCE_ENUM_CLASS, 'Cdot3OamloopbackignorerxEnum' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oamloopbacktable.Cdot3Oamloopbackentry.Cdot3OamloopbackignorerxEnum', 
                [], [], 
                '''                Since OAM loopback is a disruptive operation (user traffic
                does not pass), this attribute provides a mechanism to provide
                controls over whether received OAM loopback commands are
                processed or ignored.  When the value is ignore(1), received
                loopback commands are ignored.  When the value is process(2),
                OAM loopback commands are processed.  The default value is to
                ignore loopback commands (ignore(1)).  
                ''',
                'cdot3oamloopbackignorerx',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamLoopbackStatus', REFERENCE_ENUM_CLASS, 'Cdot3OamloopbackstatusEnum' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oamloopbacktable.Cdot3Oamloopbackentry.Cdot3OamloopbackstatusEnum', 
                [], [], 
                '''                The loopback status of the OAM entity.  This status is
                determined by a combination of the local parser and
                multiplexer states, the remote parser and multiplexer states,
                as well as by the actions of the local OAM client.  When
                operating in normal mode with no loopback in progress, the
                status reads noLoopback(1).  
                
                The values initiatingLooopback(2) and terminatingLoopback(4)
                can be read or written.  The other values can only be read -
                they can never be written.  Writing initiatingLoopback causes
                the local OAM entity to start the loopback process with its
                peer.  This value can only be written when the status is
                noLoopback(1).  Writing the value initiatingLoopback(2) in any
                other state has no effect.  When in remoteLoopback(3), writing
                terminatingLoopback(4) causes the local OAM entity to initiate
                the termination of the loopback state.  Writing
                terminatingLoopack(4) in any other state has no effect.                    
                If the OAM client initiates a looopback and has sent an
                Loopback OAMPDU and is waiting for a response, where the local
                parser and multiplexer states are DISCARD (see [802.3ah,
                57.2.11.1]), the status is 'initiatingLoopback'.  In this
                case, the local OAM entity has yet to receive any
                acknowledgement that the remote OAM entity has received its
                loopback command request.  
                                
                If the local OAM client knows that the remote OAM entity is in
                loopback mode (via the remote state information as described
                in [802.3ah, 57.2.11.1, 30.3.6.1.15]), the status is
                remoteLoopback(3).  If the local OAM client is in the process
                of terminating the remote loopback [802.3ah, 57.2.11.3,
                30.3.6.1.14], with its local multiplexer and parser states in
                DISCARD, the status is terminatingLoopback(4).  If the remote
                OAM client has put the local OAM entity in loopback mode as
                indicated by its local parser state, the status is
                localLoopback(5).  
                
                The unknown(6) status indicates the parser and multiplexer
                combination is unexpected.  This status may be returned if the
                OAM loopback is in a transition state but should not persist. 
                
                The values of this attribute correspond to the following
                values of the local and remote parser and multiplexer states. 
                
                  value            LclPrsr   LclMux    RmtPrsr   RmtMux
                  noLoopback         FWD       FWD       FWD       FWD  
                  initLoopback     DISCARD   DISCARD     FWD       FWD 
                  rmtLoopback      DISCARD     FWD      LPBK    DISCARD
                  tmtngLoopback    DISCARD   DISCARD    LPBK    DISCARD
                  lclLoopback        LPBK    DISCARD   DISCARD     FWD
                  unknown            ***   any other combination   ***
                ''',
                'cdot3oamloopbackstatus',
                'CISCO-DOT3-OAM-MIB', False),
            ],
            'CISCO-DOT3-OAM-MIB',
            'cdot3OamLoopbackEntry',
            _yang_ns._namespaces['CISCO-DOT3-OAM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB'
        ),
    },
    'CiscoDot3OamMib.Cdot3Oamloopbacktable' : {
        'meta_info' : _MetaInfoClass('CiscoDot3OamMib.Cdot3Oamloopbacktable',
            False, 
            [
            _MetaInfoClassMember('cdot3OamLoopbackEntry', REFERENCE_LIST, 'Cdot3Oamloopbackentry' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oamloopbacktable.Cdot3Oamloopbackentry', 
                [], [], 
                '''                An entry in the table, containing information on the loopback
                status for a single Ethernet like interface.  Entries in the
                table are automatically created whenever the local OAM entity
                supports loopback capabilities.  The loopback status on the
                interface can be determined from the cdot3OamLoopbackStatus
                object.  
                ''',
                'cdot3oamloopbackentry',
                'CISCO-DOT3-OAM-MIB', False),
            ],
            'CISCO-DOT3-OAM-MIB',
            'cdot3OamLoopbackTable',
            _yang_ns._namespaces['CISCO-DOT3-OAM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB'
        ),
    },
    'CiscoDot3OamMib.Cdot3Oamstatstable.Cdot3Oamstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoDot3OamMib.Cdot3Oamstatstable.Cdot3Oamstatsentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-DOT3-OAM-MIB', True),
            _MetaInfoClassMember('cdot3OamDuplicateEventNotificationRx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the number of duplicate Event OAMPDUs received on
                this interface.  Event notification OAMPDUs may be sent in
                duplicate to increase the probability of successfully being
                received, given the possibility that a frame may be lost in
                transit.  
                
                A duplicate Event Notification OAMPDU is indicated as an Event
                Notification OAMPDU with a Sequence Number field that is
                identical to the previously received Event Notification OAMPDU
                Sequence Number.  
                
                Discontinuities of this counter can occur at re-initialization
                of the management system, and at other times as indicated by
                the value of the ifCounterDiscontinuityTime.  
                ''',
                'cdot3oamduplicateeventnotificationrx',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamDuplicateEventNotificationTx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the number of duplicate Event OAMPDUs transmitted
                on this interface.  Event notification OAMPDUs may be sent in
                duplicate to increase the probability of successfully being
                received, given the possibility that a frame may be lost in
                transit.  
                
                A duplicate Event Notification OAMPDU is indicated as an Event
                Notification OAMPDU with a Sequence Number field that is
                identical to the previously transmitted Event Notification
                OAMPDU Sequence Number.  
                
                Discontinuities of this counter can occur at re-initialization
                of the management system, and at other times as indicated by
                the value of the ifCounterDiscontinuityTime.  
                ''',
                'cdot3oamduplicateeventnotificationtx',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamFramesLostDueToOam', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the number of frames that were dropped by the OAM
                multiplexer.  Since the OAM multiplexer has multiple inputs
                and a single output, there may be cases where frames are
                dropped due to transmit resource contention.  This counter is
                incremented whenever a frame is dropped by the OAM layer.
                Note that any Ethernet frame, not just OAMPDUs, may be dropped
                by the OAM layer.  This can occur when an OAMPDU takes
                precedence over a 'normal' frame resulting in the 'normal'
                frame being dropped.  
                
                When this counter is incremented, no other counters in this
                MIB are incremented.  
                              
                Discontinuities of this counter can occur at re-initialization
                of the management system, and at other times as indicated by
                the value of the ifCounterDiscontinuityTime.  
                ''',
                'cdot3oamframeslostduetooam',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamInformationRx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the number of Information OAMPDUs received on this
                interface.
                
                Discontinuities of this counter can occur at re-initialization
                of the management system, and at other times as indicated by
                the value of the ifCounterDiscontinuityTime.  
                ''',
                'cdot3oaminformationrx',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamInformationTx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the number of Information OAMPDUs transmitted on
                this interface.
                
                Discontinuities of this counter can occur at re-initialization
                of the management system, and at other times as indicated by
                the value of the ifCounterDiscontinuityTime.  
                ''',
                'cdot3oaminformationtx',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamLoopbackControlRx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the number of Loopback Control OAMPDUs received
                on this interface.  
                
                Discontinuities of this counter can occur at re-initialization
                of the management system, and at other times as indicated by
                the value of the ifCounterDiscontinuityTime.  
                ''',
                'cdot3oamloopbackcontrolrx',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamLoopbackControlTx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the number of Loopback Control OAMPDUs transmitted
                on this interface.  
                
                Discontinuities of this counter can occur at re-initialization
                of the management system, and at other times as indicated by
                the value of the ifCounterDiscontinuityTime.  
                ''',
                'cdot3oamloopbackcontroltx',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamOrgSpecificRx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the number of Organization Specific OAMPDUs
                received on this interface.  
                
                Discontinuities of this counter can occur at re-initialization
                of the management system, and at other times as indicated by
                the value of the ifCounterDiscontinuityTime.  
                ''',
                'cdot3oamorgspecificrx',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamOrgSpecificTx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the number of Organization Specific OAMPDUs
                transmitted on this interface.  
                
                Discontinuities of this counter can occur at re-initialization
                of the management system, and at other times as indicated by
                the value of the ifCounterDiscontinuityTime.  
                ''',
                'cdot3oamorgspecifictx',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamUniqueEventNotificationRx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the number of unique Event OAMPDUs received on
                this interface.  Event notification OAMPDUs may be sent in
                duplicate to increase the probability of successfully being
                received, given the possibility that a frame may be lost in
                transit.  Duplicate Event Notification receptions are counted
                by cdot3OamDuplicateEventNotificationRx.  
                
                A unique Event Notification OAMPDU is indicated as an Event
                Notification OAMPDU with a Sequence Number field that is
                distinct from the previously received Event Notification
                OAMPDU Sequence Number.  
                
                Discontinuities of this counter can occur at re-initialization
                of the management system, and at other times as indicated by
                the value of the ifCounterDiscontinuityTime.  
                ''',
                'cdot3oamuniqueeventnotificationrx',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamUniqueEventNotificationTx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the number of unique Event OAMPDUs transmitted on
                this interface.  Event notifications may be sent in duplicate
                to increase the probability of successfully being received,
                given the possibility that a frame may be lost in transit.
                Duplicate Event Notification transmissions are counted by
                cdot3OamDuplicateEventNotificationTx.  
                
                A unique Event Notification OAMPDU is indicated as an Event
                Notification OAMPDU with a Sequence Number field that is
                distinct from the previously transmitted Event Notification
                OAMPDU Sequence Number.  
                
                Discontinuities of this counter can occur at re-initialization
                of the management system, and at other times as indicated by
                the value of the ifCounterDiscontinuityTime.  
                ''',
                'cdot3oamuniqueeventnotificationtx',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamUnsupportedCodesRx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the number of OAMPDUs received on this interface
                with an unsupported op-code.  
                
                Discontinuities of this counter can occur at re-initialization
                of the management system, and at other times as indicated by
                the value of the ifCounterDiscontinuityTime.  
                ''',
                'cdot3oamunsupportedcodesrx',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamUnsupportedCodesTx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the number of OAMPDUs transmitted on this
                interface with an unsupported op-code.  
                
                Discontinuities of this counter can occur at re-initialization
                of the management system, and at other times as indicated by
                the value of the ifCounterDiscontinuityTime.  
                ''',
                'cdot3oamunsupportedcodestx',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamVariableRequestRx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the number of Variable Request OAMPDUs received on
                this interface.  
                
                Discontinuities of this counter can occur at re-initialization
                of the management system, and at other times as indicated by
                the value of the ifCounterDiscontinuityTime.  
                ''',
                'cdot3oamvariablerequestrx',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamVariableRequestTx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the number of Variable Request OAMPDUs transmitted
                on this interface.  
                
                Discontinuities of this counter can occur at re-initialization
                of the management system, and at other times as indicated by
                the value of the ifCounterDiscontinuityTime.  
                ''',
                'cdot3oamvariablerequesttx',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamVariableResponseRx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the number of Variable Response OAMPDUs received
                on this interface.  
                
                Discontinuities of this counter can occur at re-initialization
                of the management system, and at other times as indicated by
                the value of the ifCounterDiscontinuityTime.  
                ''',
                'cdot3oamvariableresponserx',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamVariableResponseTx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the number of Variable Response OAMPDUs
                transmitted on this interface.  
                
                Discontinuities of this counter can occur at re-initialization
                of the management system, and at other times as indicated by
                the value of the ifCounterDiscontinuityTime.  
                ''',
                'cdot3oamvariableresponsetx',
                'CISCO-DOT3-OAM-MIB', False),
            ],
            'CISCO-DOT3-OAM-MIB',
            'cdot3OamStatsEntry',
            _yang_ns._namespaces['CISCO-DOT3-OAM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB'
        ),
    },
    'CiscoDot3OamMib.Cdot3Oamstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoDot3OamMib.Cdot3Oamstatstable',
            False, 
            [
            _MetaInfoClassMember('cdot3OamStatsEntry', REFERENCE_LIST, 'Cdot3Oamstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oamstatstable.Cdot3Oamstatsentry', 
                [], [], 
                '''                An entry in the table, containing statistics information on
                the Ethernet OAM function for a single Ethernet like
                interface.  Entries are automatically created for every entry
                in the cdot3OamTable.  Counters are maintained across
                transitions in cdot3OamOperStatus.  
                ''',
                'cdot3oamstatsentry',
                'CISCO-DOT3-OAM-MIB', False),
            ],
            'CISCO-DOT3-OAM-MIB',
            'cdot3OamStatsTable',
            _yang_ns._namespaces['CISCO-DOT3-OAM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB'
        ),
    },
    'CiscoDot3OamMib.Cdot3Oameventconfigtable.Cdot3Oameventconfigentry' : {
        'meta_info' : _MetaInfoClass('CiscoDot3OamMib.Cdot3Oameventconfigtable.Cdot3Oameventconfigentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-DOT3-OAM-MIB', True),
            _MetaInfoClassMember('cdot3OamCriticalEventEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, the local OAM entity should attempt to indicate a
                critical event via the OAMPDU flags to its peer OAM entity
                when a critical event occurs.   The exact definition of a
                critical event is implementation dependent.  If the system
                does not support critical event capability, setting this
                object has no effect, and reading the object should always
                result in 'false'.  
                                
                By default, this object should have the value true for
                Ethernet like interfaces that support OAM.  If the OAM layer
                does not support event notifications (as indicated via the
                cdot3OamFunctionsSupported attribute), this value is ignored.
                ''',
                'cdot3oamcriticaleventenable',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamDyingGaspEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, the local OAM entity should attempt to indicate a
                dying gasp via the OAMPDU flags field to its peer OAM entity
                when a dying gasp event occurs.  The exact definition of a
                dying gasp event is implementation dependent.  If the system
                does not support dying gasp capability, setting this object
                has no effect, and reading the object should always result in
                'false'.  
                                
                By default, this object should have the value true for
                Ethernet like interfaces that support OAM.  If the OAM layer
                does not support event notifications (as indicated via the
                cdot3OamFunctionsSupported attribute), this value is ignored.
                ''',
                'cdot3oamdyinggaspenable',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamErrFrameEvNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, the OAM entity should send an Event Notification
                OAMPDU when an Errored Frame Event occurs. 
                                
                By default, this object should have the value true for
                Ethernet like interfaces that support OAM.  If the OAM layer
                does not support event notifications (as indicated via the
                cdot3OamFunctionsSupported attribute), this value is ignored. 
                ''',
                'cdot3oamerrframeevnotifenable',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamErrFramePeriodEvNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, the OAM entity should send an Event Notification
                OAMPDU when an Errored Frame Period Event occurs. 
                
                By default, this object should have the value true for
                Ethernet like interfaces that support OAM.  If the OAM layer
                does not support event notifications (as indicated via the
                cdot3OamFunctionsSupported attribute), this value is ignored. 
                ''',
                'cdot3oamerrframeperiodevnotifenable',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamErrFramePeriodThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of frame errors that must occur for this event to
                be triggered.  The default value is one frame error.  If the
                threshold value is zero, then an Event Notification OAMPDU is
                sent periodically (at the end of every window).  This can be
                used as an asynchronous notification to the peer OAM entity of
                the statistics related to this threshold crossing alarm.
                                
                If cdot3OamErrFramePeriodThreshold frame errors occur within a
                window of cdot3OamErrFramePeriodWindow frames, an Event
                Notification OAMPDU should be generated with an Errored Frame
                Period Event TLV indicating the threshold has been crossed in
                this window.  
                ''',
                'cdot3oamerrframeperiodthreshold',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamErrFramePeriodWindow', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of frames over which the threshold is defined.
                The default value of the window is the number of minimum size
                Ethernet frames that can be received over the physical layer
                in one second.  
                                
                If cdot3OamErrFramePeriodThreshold frame errors occur within a
                window of cdot3OamErrFramePeriodWindow frames, an Event
                Notification OAMPDU should be generated with an Errored Frame
                Period Event TLV indicating the threshold has been crossed in
                this window.  
                ''',
                'cdot3oamerrframeperiodwindow',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamErrFrameSecsEvNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, the local OAM entity should send an Event
                Notification OAMPDU when an Errored Frame Seconds Event
                occurs. 
                                
                By default, this object should have the value true for
                Ethernet like interfaces that support OAM.  If the OAM layer
                does not support event notifications (as indicated via the
                cdot3OamFunctionsSupported attribute), this value is ignored.
                ''',
                'cdot3oamerrframesecsevnotifenable',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamErrFrameSecsSummaryThreshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '900')], [], 
                '''                The number of errored frame seconds that must occur for this
                event to be triggered.  The default value is one errored frame
                second. If the threshold value is zero, then an Event
                Notification OAMPDU is sent periodically (at the end of every
                window).  This can be used as an asynchronous notification to
                the peer OAM entity of the statistics related to this
                threshold crossing alarm. 
                                
                If cdot3OamErrFrameSecsSummaryThreshold frame errors occur
                within a window of cdot3OamErrFrameSecsSummaryWindow (in tenths
                of seconds), an Event Notification OAMPDU should be generated
                with an Errored Frame Seconds Summary Event TLV indicating the
                threshold has been crossed in this window.  
                ''',
                'cdot3oamerrframesecssummarythreshold',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamErrFrameSecsSummaryWindow', ATTRIBUTE, 'int' , None, None, 
                [('100', '9000')], [], 
                '''                The amount of time (in 100ms intervals) over which the
                threshold is defined.  The default value is 100 (10 seconds).  
                                
                If cdot3OamErrFrameSecsSummaryThreshold frame errors occur
                within a window of cdot3OamErrFrameSecsSummaryWindow (in tenths
                of seconds), an Event Notification OAMPDU should be generated
                with an Errored Frame Seconds Summary Event TLV indicating the
                threshold has been crossed in this window.  
                ''',
                'cdot3oamerrframesecssummarywindow',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamErrFrameThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of frame errors that must occur for this event to
                be triggered.  The default value is one frame error. If the
                threshold value is zero, then an Event Notification OAMPDU is
                sent periodically (at the end of every window).  This can be
                used as an asynchronous notification to the peer OAM entity of
                the statistics related to this threshold crossing alarm. 
                                
                If cdot3OamErrFrameThreshold frame errors occur within a window
                of cdot3OamErrFrameWindow (in tenths of seconds), an Event
                Notification OAMPDU should be generated with an Errored Frame
                Event TLV indicating the threshold has been crossed in this
                window.  
                ''',
                'cdot3oamerrframethreshold',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamErrFrameWindow', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The amount of time (in 100ms increments) over which the
                threshold is defined.  The default value is 10 (1 second).  
                                
                If cdot3OamErrFrameThreshold frame errors occur within a window
                of cdot3OamErrFrameWindow seconds (measured in tenths of
                seconds), an Event Notification OAMPDU should be generated
                with an Errored Frame Event TLV indicating the threshold has
                been crossed in this window.  
                ''',
                'cdot3oamerrframewindow',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamErrSymPeriodEvNotifEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If true, the OAM entity should send an Event Notification
                OAMPDU when an Errored Symbol Period Event occurs. 
                By default, this object should have the value true for
                Ethernet like interfaces that support OAM.  If the OAM layer
                does not support event notifications (as indicated via the
                cdot3OamFunctionsSupported attribute), this value is ignored.
                ''',
                'cdot3oamerrsymperiodevnotifenable',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamErrSymPeriodThresholdHi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The two objects cdot3OamErrSymPeriodThresholdHi and
                cdot3OamErrSymPeriodThresholdLo together form an unsigned
                64-bit integer representing the number of symbol errors that
                must occur within a given window to cause this event.  
                
                This is defined as
                
                  cdot3OamErrSymPeriodThreshold =
                                    ((2^32) * cdot3OamErrSymPeriodThresholdHi)
                                            + cdot3OamErrSymPeriodThresholdLo
                                   
                If cdot3OamErrSymPeriodThreshold symbol errors occur within a
                window of cdot3OamErrSymPeriodWindow symbols, an Event
                Notification OAMPDU should be generated with an Errored Symbol
                Period Event TLV indicating the threshold has been crossed in
                this window.  
                
                The default value for cdot3OamErrSymPeriodThreshold is one
                symbol errors.  If the threshold value is zero, then an Event
                Notification OAMPDU is sent periodically (at the end of every
                window).  This can be used as an asynchronous notification to
                the peer OAM entity of the statistics related to this
                threshold crossing alarm.  
                ''',
                'cdot3oamerrsymperiodthresholdhi',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamErrSymPeriodThresholdLo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The two objects cdot3OamErrSymPeriodThresholdHi and
                cdot3OamErrSymPeriodThresholdLo together form an unsigned
                64-bit integer representing the number of symbol errors that
                must occur within a given window to cause this event.  
                
                This is defined as
                
                  cdot3OamErrSymPeriodThreshold =
                                    ((2^32) * cdot3OamErrSymPeriodThresholdHi)
                                            + cdot3OamErrSymPeriodThresholdLo
                                   
                If cdot3OamErrSymPeriodThreshold symbol errors occur within a
                window of cdot3OamErrSymPeriodWindow symbols, an Event
                Notification OAMPDU should be generated with an Errored Symbol
                Period Event TLV indicating the threshold has been crossed in
                this window.  
                
                The default value for cdot3OamErrSymPeriodThreshold is one
                symbol error. If the threshold value is zero, then an Event
                Notification OAMPDU is sent periodically (at the end of every
                window).  This can be used as an asynchronous notification to
                the peer OAM entity of the statistics related to this
                threshold crossing alarm. 
                ''',
                'cdot3oamerrsymperiodthresholdlo',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamErrSymPeriodWindowHi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The two objects cdot3OamErrSymPeriodWindowHi and
                cdot3OamErrSymPeriodLo together form an unsigned 64-bit
                integer representing the number of symbols over which this
                threshold event is defined.  This is defined as
                
                cdot3OamErrSymPeriodWindow = ((2^32)*cdot3OamErrSymPeriodWindowHi)
                                                + cdot3OamErrSymPeriodWindowLo
                
                If cdot3OamErrSymPeriodThreshold symbol errors occur within a
                window of cdot3OamErrSymPeriodWindow symbols, an Event
                Notification OAMPDU should be generated with an Errored Symbol
                Period Event TLV indicating the threshold has been crossed in
                this window.  
                
                The default value for cdot3OamErrSymPeriodWindow is the number
                of symbols in one second for the underlying physical layer.
                ''',
                'cdot3oamerrsymperiodwindowhi',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamErrSymPeriodWindowLo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The two objects cdot3OamErrSymPeriodWindowHi and
                cdot3OamErrSymPeriodWindowLo together form an unsigned 64-bit
                integer representing the number of symbols over which this
                threshold event is defined.  This is defined as
                
                cdot3OamErrSymPeriodWindow = ((2^32)*cdot3OamErrSymPeriodWindowHi)
                                                + cdot3OamErrSymPeriodWindowLo
                
                If cdot3OamErrSymPeriodThreshold symbol errors occur within a
                window of cdot3OamErrSymPeriodWindow symbols, an Event
                Notification OAMPDU should be generated with an Errored Symbol
                Period Event TLV indicating the threshold has been crossed in
                this window.  
                
                The default value for cdot3OamErrSymPeriodWindow is the number
                of symbols in one second for the underlying physical layer. 
                ''',
                'cdot3oamerrsymperiodwindowlo',
                'CISCO-DOT3-OAM-MIB', False),
            ],
            'CISCO-DOT3-OAM-MIB',
            'cdot3OamEventConfigEntry',
            _yang_ns._namespaces['CISCO-DOT3-OAM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB'
        ),
    },
    'CiscoDot3OamMib.Cdot3Oameventconfigtable' : {
        'meta_info' : _MetaInfoClass('CiscoDot3OamMib.Cdot3Oameventconfigtable',
            False, 
            [
            _MetaInfoClassMember('cdot3OamEventConfigEntry', REFERENCE_LIST, 'Cdot3Oameventconfigentry' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oameventconfigtable.Cdot3Oameventconfigentry', 
                [], [], 
                '''                Entries are automatically created and deleted from this
                table, and exist whenever the OAM entity supports Ethernet OAM
                events (as indicated by the eventSupport bit in
                cdot3OamFunctionsSuppported).  Values in the table are
                maintained across changes to the value of cdot3OamOperStatus.
                
                Event configuration controls when the local management entity
                sends Event Notification OAMPDUs to its OAM peer, and when
                certain event flags are set or cleared in OAMPDUs. 
                ''',
                'cdot3oameventconfigentry',
                'CISCO-DOT3-OAM-MIB', False),
            ],
            'CISCO-DOT3-OAM-MIB',
            'cdot3OamEventConfigTable',
            _yang_ns._namespaces['CISCO-DOT3-OAM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB'
        ),
    },
    'CiscoDot3OamMib.Cdot3Oameventlogtable.Cdot3Oameventlogentry.Cdot3OameventloglocationEnum' : _MetaInfoEnum('Cdot3OameventloglocationEnum', 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB',
        {
            'local':'local',
            'remote':'remote',
        }, 'CISCO-DOT3-OAM-MIB', _yang_ns._namespaces['CISCO-DOT3-OAM-MIB']),
    'CiscoDot3OamMib.Cdot3Oameventlogtable.Cdot3Oameventlogentry' : {
        'meta_info' : _MetaInfoClass('CiscoDot3OamMib.Cdot3Oameventlogtable.Cdot3Oameventlogentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'CISCO-DOT3-OAM-MIB', True),
            _MetaInfoClassMember('cdot3OamEventLogIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                An arbitrary integer for identifying individual events
                within the event log.  
                ''',
                'cdot3oameventlogindex',
                'CISCO-DOT3-OAM-MIB', True),
            _MetaInfoClassMember('cdot3OamEventLogEventTotal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Each Event Notification TLV contains a running total of the
                number of times an event has occurred, as well as the number
                of times an Event Notification for the event has been
                transmitted.  For non-threshold crossing events, the number of
                events (cdot3OamLogRunningTotal) and the number of resultant
                Event Notifications (cdot3OamLogEventTotal) should be
                identical. 
                
                For threshold crossing events, since multiple occurrences may
                be required to cross the threshold, these values are likely
                different.  This value represents the total number of times
                one or more of these occurrences have resulted in an Event
                Notification (for example, 51 when 3253 symbol errors have
                occurred since the last reset, which has resulted in 51 symbol
                error threshold crossing events since the last reset).  
                ''',
                'cdot3oameventlogeventtotal',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamEventLogLocation', REFERENCE_ENUM_CLASS, 'Cdot3OameventloglocationEnum' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oameventlogtable.Cdot3Oameventlogentry.Cdot3OameventloglocationEnum', 
                [], [], 
                '''                Whether this event occurred locally (local(1)), or was 
                received from the OAM peer via Ethernet OAM (remote(2)).
                ''',
                'cdot3oameventloglocation',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamEventLogOui', ATTRIBUTE, 'str' , None, None, 
                [(3, None)], [], 
                '''                The OUI of the entity defining the object type.  All IEEE
                802.3 defined events (as appearing in [802.3ah] except for the
                Organizationally Unique Event TLVs) use the IEEE 802.3 OUI of
                0x0180C2.  Organizations defining their own Event Notification
                TLVs include their OUI in the Event Notification TLV which
                gets reflected here.  
                ''',
                'cdot3oameventlogoui',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamEventLogRunningTotal', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Each Event Notification TLV contains a running total of the
                number of times an event has occurred, as well as the number
                of times an Event Notification for the event has been
                transmitted.  For non-threshold crossing events, the number of
                events (cdot3OamLogRunningTotal) and the number of resultant
                Event Notifications (cdot3OamLogEventTotal) should be
                identical. 
                
                For threshold crossing events, since multiple occurrences may
                be required to cross the threshold, these values are likely
                different.  This value represents the total number of times
                this event has happened since the last reset (for example,
                3253, when 3253 symbol errors have occurred since the last
                reset, which has resulted in 51 symbol error threshold
                crossing events since the last reset).  
                ''',
                'cdot3oameventlogrunningtotal',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamEventLogThresholdHi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If the event represents a threshold crossing event, the two
                objects cdot3OamEventThresholdHi and cdot3OamEventThresholdLo
                form an unsigned 64-bit integer yielding the value that was
                crossed for the threshold crossing event (for example, 10,
                when 11 occurrences happened in 5 seconds while the threshold
                was 10).  The two objects are combined as:
                
                cdot3OamEventLogThreshold = ((2^32) * cdot3OamEventLogThresholdHi)
                                                 + cdot3OamEventLogThresholdLo
                
                Otherwise, this value is returned as all F's (2^32 -1) and 
                adds no useful information.  
                ''',
                'cdot3oameventlogthresholdhi',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamEventLogThresholdLo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If the event represents a threshold crossing event, the two
                objects cdot3OamEventThresholdHi and cdot3OamEventThresholdLo
                form an unsigned 64-bit integer yielding the value that was
                crossed for the threshold crossing event (for example, 10,
                when 11 occurrences happened in 5 seconds while the threshold
                was 10).  The two objects are combined as:
                
                cdot3OamEventLogThreshold = ((2^32) * cdot3OamEventLogThresholdHi)
                                                 + cdot3OamEventLogThresholdLo
                
                Otherwise, this value is returned as all F's (2^32 - 1) and
                adds no useful information.  
                ''',
                'cdot3oameventlogthresholdlo',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamEventLogTimestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time of the logged event.  For
                locally generated events, the time of the event can be
                accurately retrieved from sysUpTime.  For remotely generated
                events, the time of the event is indicated by the reception of
                the Event Notification OAMPDU indicating the event occurred on
                the peer.  A system may attempt to adjust the timestamp value
                to more accurately reflect the time of the event at the peer
                OAM entity by using other information, such as that found in
                the timestamp found of the Event Notification TLVs, which
                provides an indication of the relative time between events at
                the peer entity.  
                ''',
                'cdot3oameventlogtimestamp',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamEventLogType', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The type of event that generated this entry in the event log.
                
                When the OUI is the IEEE 802.3 OUI of 0x0180C2, the following
                event types are defined:
                    erroredSymbolEvent(1), 
                    erroredFramePeriodEvent (2), 
                    erroredFrameEvent(3),
                    erroredFrameSecondsEvent(4), 
                    linkFault(256), 
                    dyingGaspEvent(257),
                    criticalLinkEvent(258)
                The first four are considered threshold crossing events as
                they are generated when a metric exceeds a given value within
                a specified window.  The other three are not threshold
                crossing events.  
                
                When the OUI is not 71874 (0x0180C2 in hex), then some other
                organization has defined the event space.  If event subtyping
                is known to the implementation, it may be reflected here.
                Otherwise, this value should return all Fs (2^32 - 1).  
                ''',
                'cdot3oameventlogtype',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamEventLogValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                If the event represents a threshold crossing event, this
                value indicates the value of the parameter within the given
                window that generated this event (for example, 11, when 11
                occurrences happened in 5 seconds while the threshold was 10).  
                
                Otherwise, this value is returned as all F's 
                (2^64 - 1) and adds no useful information.  
                ''',
                'cdot3oameventlogvalue',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamEventLogWindowHi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If the event represents a threshold crossing event, the two
                objects cdot3OamEventWindowHi and cdot3OamEventWindowLo form an
                unsigned 64-bit integer yielding the window over which the
                value was measured for the threshold crossing event (for
                example, 5, when 11 occurrences happened in 5 seconds while
                the threshold was 10).   The two objects are combined as:
                
                cdot3OamEventLogWindow = ((2^32) * cdot3OamEventLogWindowHi)
                                                + cdot3OamEventLogWindowLo
                
                
                Otherwise, this value is returned as all F's (2^32 - 1) and 
                adds no useful information.  
                ''',
                'cdot3oameventlogwindowhi',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamEventLogWindowLo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If the event represents a threshold crossing event, the two
                objects cdot3OamEventWindowHi and cdot3OamEventWindowLo form an
                unsigned 64-bit integer yielding the window over which the
                value was measured for the threshold crossing event (for
                example, 5, when 11 occurrences happened in 5 seconds while
                the threshold was 10).   The two objects are combined as:
                
                cdot3OamEventLogWindow = ((2^32) * cdot3OamEventLogWindowHi)
                                                + cdot3OamEventLogWindowLo
                
                Otherwise, this value is returned as all F's (2^32 - 1) and 
                adds no useful information.  
                ''',
                'cdot3oameventlogwindowlo',
                'CISCO-DOT3-OAM-MIB', False),
            ],
            'CISCO-DOT3-OAM-MIB',
            'cdot3OamEventLogEntry',
            _yang_ns._namespaces['CISCO-DOT3-OAM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB'
        ),
    },
    'CiscoDot3OamMib.Cdot3Oameventlogtable' : {
        'meta_info' : _MetaInfoClass('CiscoDot3OamMib.Cdot3Oameventlogtable',
            False, 
            [
            _MetaInfoClassMember('cdot3OamEventLogEntry', REFERENCE_LIST, 'Cdot3Oameventlogentry' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oameventlogtable.Cdot3Oameventlogentry', 
                [], [], 
                '''                An entry in the cdot3OamEventLogTable.  Entries are
                automatically created whenever Ethernet OAM events occur at
                the local OAM entity, and when Event Notification OAMPDUs are
                received at the local OAM entity (indicating events have
                occurred at the peer OAM entity).  The size of the table is
                implementation dependent, but when the table becomes full,
                older events are automatically deleted to make room for newer
                events.  The table index cdot3OamEventLogIndex increments for
                each new entry, and when the maximum value is reached the
                value restarts at zero.  
                ''',
                'cdot3oameventlogentry',
                'CISCO-DOT3-OAM-MIB', False),
            ],
            'CISCO-DOT3-OAM-MIB',
            'cdot3OamEventLogTable',
            _yang_ns._namespaces['CISCO-DOT3-OAM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB'
        ),
    },
    'CiscoDot3OamMib' : {
        'meta_info' : _MetaInfoClass('CiscoDot3OamMib',
            False, 
            [
            _MetaInfoClassMember('cdot3OamEventConfigTable', REFERENCE_CLASS, 'Cdot3Oameventconfigtable' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oameventconfigtable', 
                [], [], 
                '''                Ethernet OAM includes the ability to generate and receive
                Event Notification OAMPDUs to indicate various link problems.
                This table contains the mechanisms to enable Event
                Notifications and configure the thresholds to generate the
                standard Ethernet OAM events.  There is one entry in the table
                for every entry in cdot3OamTable that supports OAM events
                (where cdot3OamFunctionsSupported includes the eventSupport
                bit set). The values in the table are maintained across
                changes to cdot3OamOperStatus.  
                
                The standard threshold crossing events are:
                  - Errored Symbol Period Event.  Generated when the number of
                    symbol errors exceeds a threshold within a given window 
                    defined by a number of symbols (for example, 1,000 symbols
                    out of 1,000,000 had errors).  
                  - Errored Frame Period Event.  Generated when the number of 
                    frame errors exceeds a threshold within a given window 
                    defined by a number of frames (for example, 10 frames out
                    of 1000 had errors).  
                  - Errored Frame Event.  Generated when the number of frame 
                    errors exceeds a threshold within a given window defined 
                    by a period of time (for example, 10 frames in 1 second 
                    had errors).
                  - Errored Frame Seconds Summary Event.  Generated when the 
                    number of errored frame seconds exceeds a threshold within
                    a given time period (for example, 10 errored frame seconds
                    within the last 100 seconds).  An errored frame second is 
                    defined as a 1 second interval which had >0 frame errors.  
                There are other events (dying gasp, critical events) that are
                not threshold crossing events but which can be
                enabled/disabled via this table.  
                ''',
                'cdot3oameventconfigtable',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamEventLogTable', REFERENCE_CLASS, 'Cdot3Oameventlogtable' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oameventlogtable', 
                [], [], 
                '''                This table records a history of the events that have occurred
                at the Ethernet OAM level.  These events can include locally
                detected events, which may result in locally generated
                OAMPDUs, and remotely detected events, which are detected by
                the OAM peer entity and signaled to the local entity via
                Ethernet OAM.  Ethernet OAM events can be signaled by Event
                Notification OAMPDUs or by the flags field in any OAMPDU.  
                
                This table contains both threshold crossing events and
                non-threshold crossing events.  The parameters for the
                threshold window, threshold value, and actual value
                (cdot3OamEventLogWindowXX, cdot3OamEventLogThresholdXX,
                cdot3OamEventLogValue) are only applicable to threshold
                crossing events, and are returned as all F's (2^32 - 1) for
                non-threshold crossing events.  
                Entries in the table are automatically created when such
                events are detected.  The size of the table is implementation
                dependent.  When the table reaches its maximum size, older
                entries are automatically deleted to make room for newer
                entries. 
                ''',
                'cdot3oameventlogtable',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamLoopbackTable', REFERENCE_CLASS, 'Cdot3Oamloopbacktable' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oamloopbacktable', 
                [], [], 
                '''                This table contains controls for the loopback state of the
                local link as well as indicating the status of the loopback
                function.  There is one entry in this table for each entry in
                cdot3OamTable that supports loopback functionality (where
                cdot3OamFunctionsSupported includes the loopbackSupport bit
                set).
                
                Loopback can be used to place the remote OAM entity in a state
                where every received frame (except OAMPDUs) is echoed back
                over the same interface on which they were received.   In this
                state, at the remote entity, 'normal' traffic is disabled as
                only the looped back frames are transmitted on the interface.
                Loopback is thus an intrusive operation that prohibits normal
                data flow and should be used accordingly.  
                ''',
                'cdot3oamloopbacktable',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamPeerTable', REFERENCE_CLASS, 'Cdot3Oampeertable' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oampeertable', 
                [], [], 
                '''                This table contains information about the OAM peer for a
                particular Ethernet like interface. OAM entities communicate
                with a single OAM peer entity on Ethernet links on which OAM
                is enabled and operating properly.  There is one entry in this
                table for each entry in the cdot3OamTable for which information
                on the peer OAM entity is available.  
                ''',
                'cdot3oampeertable',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamStatsTable', REFERENCE_CLASS, 'Cdot3Oamstatstable' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oamstatstable', 
                [], [], 
                '''                This table contains statistics for the OAM function on a
                particular Ethernet like interface. There is an entry in the
                table for every entry in the cdot3OamTable. 
                
                The counters in this table are defined as 32-bit entries to
                match the counter size as defined in [802.3ah].  Given the OAM
                protocol is a slow protocol, the counters increment at a slow
                rate. 
                ''',
                'cdot3oamstatstable',
                'CISCO-DOT3-OAM-MIB', False),
            _MetaInfoClassMember('cdot3OamTable', REFERENCE_CLASS, 'Cdot3Oamtable' , 'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB', 'CiscoDot3OamMib.Cdot3Oamtable', 
                [], [], 
                '''                This table contains the primary controls and status for the
                OAM capabilities of an Ethernet like interface.  There will be
                one row in this table for each Ethernet like interface in the
                system that supports the OAM functions defined in [802.3ah].
                ''',
                'cdot3oamtable',
                'CISCO-DOT3-OAM-MIB', False),
            ],
            'CISCO-DOT3-OAM-MIB',
            'CISCO-DOT3-OAM-MIB',
            _yang_ns._namespaces['CISCO-DOT3-OAM-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_DOT3_OAM_MIB'
        ),
    },
}
_meta_table['CiscoDot3OamMib.Cdot3Oamtable.Cdot3Oamentry']['meta_info'].parent =_meta_table['CiscoDot3OamMib.Cdot3Oamtable']['meta_info']
_meta_table['CiscoDot3OamMib.Cdot3Oampeertable.Cdot3Oampeerentry']['meta_info'].parent =_meta_table['CiscoDot3OamMib.Cdot3Oampeertable']['meta_info']
_meta_table['CiscoDot3OamMib.Cdot3Oamloopbacktable.Cdot3Oamloopbackentry']['meta_info'].parent =_meta_table['CiscoDot3OamMib.Cdot3Oamloopbacktable']['meta_info']
_meta_table['CiscoDot3OamMib.Cdot3Oamstatstable.Cdot3Oamstatsentry']['meta_info'].parent =_meta_table['CiscoDot3OamMib.Cdot3Oamstatstable']['meta_info']
_meta_table['CiscoDot3OamMib.Cdot3Oameventconfigtable.Cdot3Oameventconfigentry']['meta_info'].parent =_meta_table['CiscoDot3OamMib.Cdot3Oameventconfigtable']['meta_info']
_meta_table['CiscoDot3OamMib.Cdot3Oameventlogtable.Cdot3Oameventlogentry']['meta_info'].parent =_meta_table['CiscoDot3OamMib.Cdot3Oameventlogtable']['meta_info']
_meta_table['CiscoDot3OamMib.Cdot3Oamtable']['meta_info'].parent =_meta_table['CiscoDot3OamMib']['meta_info']
_meta_table['CiscoDot3OamMib.Cdot3Oampeertable']['meta_info'].parent =_meta_table['CiscoDot3OamMib']['meta_info']
_meta_table['CiscoDot3OamMib.Cdot3Oamloopbacktable']['meta_info'].parent =_meta_table['CiscoDot3OamMib']['meta_info']
_meta_table['CiscoDot3OamMib.Cdot3Oamstatstable']['meta_info'].parent =_meta_table['CiscoDot3OamMib']['meta_info']
_meta_table['CiscoDot3OamMib.Cdot3Oameventconfigtable']['meta_info'].parent =_meta_table['CiscoDot3OamMib']['meta_info']
_meta_table['CiscoDot3OamMib.Cdot3Oameventlogtable']['meta_info'].parent =_meta_table['CiscoDot3OamMib']['meta_info']
