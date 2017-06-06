


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MplsLdpStdMib.Mplsldplsrobjects.MplsldplsrloopdetectioncapableEnum' : _MetaInfoEnum('MplsldplsrloopdetectioncapableEnum', 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB',
        {
            'none':'none',
            'other':'other',
            'hopCount':'hopCount',
            'pathVector':'pathVector',
            'hopCountAndPathVector':'hopCountAndPathVector',
        }, 'MPLS-LDP-STD-MIB', _yang_ns._namespaces['MPLS-LDP-STD-MIB']),
    'MplsLdpStdMib.Mplsldplsrobjects' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsldplsrobjects',
            False, 
            [
            _MetaInfoClassMember('mplsLdpLsrId', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                The Label Switching Router's Identifier.
                ''',
                'mplsldplsrid',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpLsrLoopDetectionCapable', REFERENCE_ENUM_CLASS, 'MplsldplsrloopdetectioncapableEnum' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldplsrobjects.MplsldplsrloopdetectioncapableEnum', 
                [], [], 
                '''                A indication of whether this
                Label Switching Router supports
                loop detection.
                
                none(1) -- Loop Detection is not supported
                           on this LSR.
                
                other(2) -- Loop Detection is supported but
                            by a method other than those
                            listed below.
                
                hopCount(3) -- Loop Detection is supported by
                               Hop Count only.
                
                pathVector(4) -- Loop Detection is supported by
                                 Path Vector only.
                
                hopCountAndPathVector(5) -- Loop Detection is
                                     supported by both Hop Count
                                     And Path Vector.
                
                Since Loop Detection is determined during
                Session Initialization, an individual session
                may not be running with loop detection.  This
                object simply gives an indication of whether or not the
                LSR has the ability to support Loop Detection and
                which types.
                ''',
                'mplsldplsrloopdetectioncapable',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsLdpLsrObjects',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsldpentityobjects' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsldpentityobjects',
            False, 
            [
            _MetaInfoClassMember('mplsLdpEntityIndexNext', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an appropriate value to
                be used for mplsLdpEntityIndex when creating
                entries in the mplsLdpEntityTable. The value
                0 indicates that no unassigned entries are
                available.
                ''',
                'mplsldpentityindexnext',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityLastChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time of the most
                recent addition or deletion of an entry
                to/from the mplsLdpEntityTable/mplsLdpEntityStatsTable, or
                the most recent change in value of any objects in the
                mplsLdpEntityTable.
                
                
                If no such changes have occurred since the last
                re-initialization of the local management subsystem,
                then this object contains a zero value.
                ''',
                'mplsldpentitylastchange',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsLdpEntityObjects',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsldpsessionobjects' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsldpsessionobjects',
            False, 
            [
            _MetaInfoClassMember('mplsLdpLspFecLastChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time of the most
                recent addition/deletion of an entry
                to/from the mplsLdpLspFecTable or
                the most recent change in values to any objects in the
                mplsLdpLspFecTable.
                
                If no such changes have occurred since the last
                re-initialization of the local management subsystem,
                then this object contains a zero value.
                ''',
                'mplsldplspfeclastchange',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpPeerLastChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time of the most
                recent addition or deletion to/from the
                mplsLdpPeerTable/mplsLdpSessionTable.
                ''',
                'mplsldppeerlastchange',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsLdpSessionObjects',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsfecobjects' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsfecobjects',
            False, 
            [
            _MetaInfoClassMember('mplsFecIndexNext', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an appropriate value to
                be used for mplsFecIndex when creating
                entries in the mplsFecTable. The value
                0 indicates that no unassigned entries are
                available.
                ''',
                'mplsfecindexnext',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsFecLastChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time of the most
                recent addition/deletion of an entry
                to/from the mplsLdpFectTable or
                the most recent change in values to any objects
                in the mplsLdpFecTable.
                
                If no such changes have occurred since the last
                re-initialization of the local management subsystem,
                then this object contains a zero value.
                ''',
                'mplsfeclastchange',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsFecObjects',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry.MplsldpentityadminstatusEnum' : _MetaInfoEnum('MplsldpentityadminstatusEnum', 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'MPLS-LDP-STD-MIB', _yang_ns._namespaces['MPLS-LDP-STD-MIB']),
    'MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry.MplsldpentityoperstatusEnum' : _MetaInfoEnum('MplsldpentityoperstatusEnum', 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB',
        {
            'unknown':'unknown',
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'MPLS-LDP-STD-MIB', _yang_ns._namespaces['MPLS-LDP-STD-MIB']),
    'MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry.MplsldpentitytransportaddrkindEnum' : _MetaInfoEnum('MplsldpentitytransportaddrkindEnum', 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB',
        {
            'interface':'interface',
            'loopback':'loopback',
        }, 'MPLS-LDP-STD-MIB', _yang_ns._namespaces['MPLS-LDP-STD-MIB']),
    'MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry',
            False, 
            [
            _MetaInfoClassMember('mplsLdpEntityLdpId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The LDP identifier.
                ''',
                'mplsldpentityldpid',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpEntityIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This index is used as a secondary index to uniquely
                identify this row.  Before creating a row in this table,
                the 'mplsLdpEntityIndexNext' object should be retrieved.
                That value should be used for the value of this index
                when creating a row in this table.  NOTE:  if a value
                of zero (0) is retrieved, that indicates that no rows
                can be created in this table at this time.
                
                A secondary index (this object) is meaningful to some
                but not all, LDP implementations.  For example
                an LDP implementation which uses PPP would
                use this index to differentiate PPP sub-links.
                
                Another way to use this index is to give this the
                value of ifIndex.  However, this is dependant
                
                
                on the implementation.
                ''',
                'mplsldpentityindex',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpEntityAdminStatus', REFERENCE_ENUM_CLASS, 'MplsldpentityadminstatusEnum' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry.MplsldpentityadminstatusEnum', 
                [], [], 
                '''                The administrative status of this LDP Entity.
                If this object is changed from 'enable' to 'disable'
                and this entity has already attempted to establish
                contact with a Peer, then all contact with that
                Peer is lost and all information from that Peer
                needs to be removed from the MIB. (This implies
                that the network management subsystem should clean
                up any related entry in the mplsLdpPeerTable.  This
                further implies that a 'tear-down' for that session
                is issued and the session and all information related
                to that session cease to exist).
                
                At this point the operator is able to change values
                which are related to this entity.
                
                When the admin status is set back to 'enable', then
                this Entity will attempt to establish a new session
                with the Peer.
                ''',
                'mplsldpentityadminstatus',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityDiscontinuityTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion
                at which any one or more of this entity's counters
                suffered a discontinuity.  The relevant counters
                are the specific instances associated with this
                entity of any Counter32 object contained
                in the 'mplsLdpEntityStatsTable'.  If no such
                discontinuities have occurred since the last
                re-initialization of the local management
                subsystem, then this object contains a zero
                value.
                ''',
                'mplsldpentitydiscontinuitytime',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityHelloHoldTimer', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The 16-bit integer value which is the proposed Hello
                hold timer for this LDP Entity. The Hello Hold time
                in seconds.
                
                
                An LSR maintains a record of Hellos received
                from potential peers.  This object represents
                the Hold Time in the Common Hello Parameters TLV of
                the Hello Message.
                
                A value of 0 is a default value and should be
                interpretted in conjunction with the
                mplsLdpEntityTargetPeer object.
                
                If the value of this object is 0: if the value of the
                mplsLdpEntityTargetPeer object is false(2), then this
                specifies that the Hold Time's actual default value is
                15 seconds (i.e., the default Hold time for Link Hellos
                is 15 seconds).  Otherwise if the value of the
                mplsLdpEntityTargetPeer object is true(1), then this
                specifies that the Hold Time's actual default value is
                45 seconds (i.e., the default Hold time for Targeted
                Hellos is 45 seconds).
                
                A value of 65535 means infinite (i.e., wait forever).
                
                All other values represent the amount of time in
                seconds to wait for a Hello Message.  Setting the
                hold time to a value smaller than 15 is not
                recommended, although not forbidden according
                to RFC3036.
                ''',
                'mplsldpentityhelloholdtimer',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityHopCountLimit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                If the value of this object is 0 (zero),
                then Loop Detection using Hop Counters is
                disabled.
                
                If the value of this object is greater than
                0 (zero) then Loop Detection using Hop
                Counters is enabled, and this object
                specifies this Entity's maximum allowable
                value for the Hop Count.
                Also, the value of the object
                mplsLdpLsrLoopDetectionCapable must be set
                to either 'hopCount(3)' or
                'hopCountAndPathVector(5)' if this object
                has a value greater than 0 (zero), otherwise
                it is ignored.
                ''',
                'mplsldpentityhopcountlimit',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityInitSessionThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                When attempting to establish a session with
                a given Peer, the given LDP Entity should
                send out the SNMP notification,
                'mplsLdpInitSessionThresholdExceeded', when
                the number of Session Initialization messages
                sent exceeds this threshold.
                
                The notification is used to notify an
                operator when this Entity and its Peer are
                possibly engaged in an endless sequence
                of messages as each NAKs the other's
                
                
                Initialization messages with Error Notification
                messages.  Setting this threshold which triggers
                the notification is one way to notify the
                operator.  The notification should be generated
                each time this threshold is exceeded and
                for every subsequent Initialization message
                which is NAK'd with an Error Notification
                message after this threshold is exceeded.
                
                A value of 0 (zero) for this object
                indicates that the threshold is infinity, thus
                the SNMP notification will never be generated.
                ''',
                'mplsldpentityinitsessionthreshold',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityKeepAliveHoldTimer', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The 16-bit integer value which is the proposed keep
                alive hold timer for this LDP Entity.
                ''',
                'mplsldpentitykeepaliveholdtimer',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityLabelDistMethod', REFERENCE_ENUM_CLASS, 'MplslabeldistributionmethodEnum' , 'ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplslabeldistributionmethodEnum', 
                [], [], 
                '''                For any given LDP session, the method of
                label distribution must be specified.
                ''',
                'mplsldpentitylabeldistmethod',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityLabelRetentionMode', REFERENCE_ENUM_CLASS, 'MplsretentionmodeEnum' , 'ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplsretentionmodeEnum', 
                [], [], 
                '''                The LDP Entity can be configured to use either
                conservative or liberal label retention mode.
                
                If the value of this object is conservative(1)
                then advertized label mappings are retained
                only if they will be used to forward packets,
                i.e., if label came from a valid next hop.
                
                If the value of this object is liberal(2)
                then all advertized label mappings are retained
                whether they are from a valid next hop or not.
                ''',
                'mplsldpentitylabelretentionmode',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityLabelType', REFERENCE_ENUM_CLASS, 'MplsldplabeltypeEnum' , 'ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplsldplabeltypeEnum', 
                [], [], 
                '''                Specifies the optional parameters for the LDP
                Initialization Message.
                
                If the value is generic(1) then no
                optional parameters will be sent in
                the LDP Initialization message associated
                with this Entity.
                
                If the value is atmParameters(2) then
                a row must be created in the
                mplsLdpEntityAtmTable, which
                corresponds to this entry.
                
                If the value is frameRelayParameters(3) then
                a row must be created in the
                mplsLdpEntityFrameRelayTable, which
                corresponds to this entry.
                ''',
                'mplsldpentitylabeltype',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityMaxPduLength', ATTRIBUTE, 'int' , None, None, 
                [('256', '65535')], [], 
                '''                The maximum PDU Length that is sent in
                the Common Session Parameters of an Initialization
                Message. According to the LDP Specification [RFC3036]
                a value of 255 or less specifies the
                default maximum length of 4096 octets, this is why
                the value of this object starts at 256.  The operator
                should explicitly choose the default value (i.e., 4096),
                or some other value.
                
                The receiving LSR MUST calculate the maximum PDU
                length for the session by using the smaller of its and
                its peer's proposals for Max PDU Length.
                ''',
                'mplsldpentitymaxpdulength',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityOperStatus', REFERENCE_ENUM_CLASS, 'MplsldpentityoperstatusEnum' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry.MplsldpentityoperstatusEnum', 
                [], [], 
                '''                The operational status of this LDP Entity.
                
                The value of unknown(1) indicates that the
                operational status cannot be determined at
                this time.  The value of unknown should be
                a transient condition before changing
                to enabled(2) or disabled(3).
                ''',
                'mplsldpentityoperstatus',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityPathVectorLimit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                If the value of this object is 0 (zero) then
                Loop Detection for Path Vectors is disabled.
                
                Otherwise, if this object has a value greater than
                zero, then Loop Dection for Path Vectors is enabled,
                and the Path Vector Limit is this value.
                Also, the value of the object,
                'mplsLdpLsrLoopDetectionCapable', must be set to
                either 'pathVector(4)' or 'hopCountAndPathVector(5)',
                if this object has a value greater than 0 (zero),
                otherwise it is ignored.
                ''',
                'mplsldpentitypathvectorlimit',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityProtocolVersion', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The version number of the LDP protocol which will be
                used in the session initialization message.
                
                Section 3.5.3 in the LDP Specification specifies
                that the version of the LDP protocol is negotiated during
                session establishment. The value of this object
                represents the value that is sent in the initialization
                message.
                ''',
                'mplsldpentityprotocolversion',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row.  All writable
                objects in this row may be modified at any
                time, however, as described in detail in
                the section entitled, 'Changing Values After
                Session Establishment', and again described
                in the DESCRIPTION clause of the
                mplsLdpEntityAdminStatus object, if a session
                has been initiated with a Peer, changing objects
                in this table will wreak havoc with the session
                and interrupt traffic.  To repeat again:
                the recommended procedure is to
                set the mplsLdpEntityAdminStatus to down, thereby
                explicitly causing a session to be torn down. Then,
                change objects in this entry, then set
                the mplsLdpEntityAdminStatus to enable,
                which enables a new session to be initiated.
                ''',
                'mplsldpentityrowstatus',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityStatsBadLdpIdentifierErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Bad LDP Identifier
                Fatal Errors detected by the session(s)
                (past and present) associated with this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                mplsLdpEntityDiscontinuityTime.
                ''',
                'mplsldpentitystatsbadldpidentifiererrors',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityStatsBadMessageLengthErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Bad Message
                Length Fatal Errors detected by the session(s)
                (past and present) associated with this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                mplsLdpEntityDiscontinuityTime.
                ''',
                'mplsldpentitystatsbadmessagelengtherrors',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityStatsBadPduLengthErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Bad PDU Length
                Fatal Errors detected by the session(s)
                (past and present) associated with this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                mplsLdpEntityDiscontinuityTime.
                ''',
                'mplsldpentitystatsbadpdulengtherrors',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityStatsBadTlvLengthErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Bad TLV
                Length Fatal Errors detected by the session(s)
                (past and present) associated with this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                mplsLdpEntityDiscontinuityTime.
                ''',
                'mplsldpentitystatsbadtlvlengtherrors',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityStatsKeepAliveTimerExpErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Session Keep Alive
                Timer Expired Errors detected by the session(s)
                (past and present) associated with this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                mplsLdpEntityDiscontinuityTime.
                ''',
                'mplsldpentitystatskeepalivetimerexperrors',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityStatsMalformedTlvValueErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Malformed TLV
                Value Fatal Errors detected by the session(s)
                (past and present) associated with this
                LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                mplsLdpEntityDiscontinuityTime.
                ''',
                'mplsldpentitystatsmalformedtlvvalueerrors',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityStatsSessionAttempts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the Session Initialization messages
                which were sent or received by this LDP Entity and
                were NAK'd.   In other words, this counter counts
                the number of session initializations that failed.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                mplsLdpEntityDiscontinuityTime.
                ''',
                'mplsldpentitystatssessionattempts',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityStatsSessionRejectedAdErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the Session Rejected/Parameters
                Advertisement Mode Error Notification Messages sent
                or received by this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                mplsLdpEntityDiscontinuityTime.
                ''',
                'mplsldpentitystatssessionrejectedaderrors',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityStatsSessionRejectedLRErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the Session Rejected/Parameters
                Label Range Notification Messages sent
                or received by this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                mplsLdpEntityDiscontinuityTime.
                ''',
                'mplsldpentitystatssessionrejectedlrerrors',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityStatsSessionRejectedMaxPduErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the Session Rejected/Parameters
                
                Max Pdu Length Error Notification Messages sent
                or received by this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                mplsLdpEntityDiscontinuityTime.
                ''',
                'mplsldpentitystatssessionrejectedmaxpduerrors',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityStatsSessionRejectedNoHelloErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A count of the Session Rejected/No Hello Error
                Notification Messages sent or received by
                this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                mplsLdpEntityDiscontinuityTime.
                ''',
                'mplsldpentitystatssessionrejectednohelloerrors',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityStatsShutdownReceivedNotifications', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Shutdown Notifications
                received related to session(s) (past and present)
                associated with this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                mplsLdpEntityDiscontinuityTime.
                ''',
                'mplsldpentitystatsshutdownreceivednotifications',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityStatsShutdownSentNotifications', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Shutdown Notfications
                sent related to session(s) (past and present) associated
                with this LDP Entity.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                
                
                mplsLdpEntityDiscontinuityTime.
                ''',
                'mplsldpentitystatsshutdownsentnotifications',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.
                Conceptual rows having the value 'permanent(4)'
                need not allow write-access to any columnar
                objects in the row.
                ''',
                'mplsldpentitystoragetype',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityTargetPeer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this LDP entity uses targeted peer then set
                this to true.
                ''',
                'mplsldpentitytargetpeer',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityTargetPeerAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The value of the internetwork layer address
                used for the Extended Discovery.  The value of
                mplsLdpEntityTargetPeerAddrType specifies how
                this address is to be interpreted.
                ''',
                'mplsldpentitytargetpeeraddr',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityTargetPeerAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The type of the internetwork layer address used for
                the Extended Discovery.  This object indicates how
                the value of mplsLdpEntityTargetPeerAddr is to
                be interpreted.
                ''',
                'mplsldpentitytargetpeeraddrtype',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityTcpPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The TCP Port for
                LDP.  The default value is the well-known
                value of this port.
                ''',
                'mplsldpentitytcpport',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityTransportAddrKind', REFERENCE_ENUM_CLASS, 'MplsldpentitytransportaddrkindEnum' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry.MplsldpentitytransportaddrkindEnum', 
                [], [], 
                '''                This specifies whether the loopback or interface
                address is to be used as the transport address
                in the transport address TLV of the
                hello message.
                
                If the value is interface(1), then the IP
                address of the interface from which hello
                messages are sent is used as the transport
                address in the hello message.
                
                Otherwise, if the value is loopback(2), then the IP
                address of the loopback interface is used as the
                transport address in the hello message.
                ''',
                'mplsldpentitytransportaddrkind',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityUdpDscPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The UDP Discovery Port for
                LDP.  The default value is the
                well-known value for this port.
                ''',
                'mplsldpentityudpdscport',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsLdpEntityEntry',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsldpentitytable' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsldpentitytable',
            False, 
            [
            _MetaInfoClassMember('mplsLdpEntityEntry', REFERENCE_LIST, 'Mplsldpentityentry' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry', 
                [], [], 
                '''                An entry in this table represents an LDP entity.
                An entry can be created by a network administrator
                or by an SNMP agent as instructed by LDP.
                ''',
                'mplsldpentityentry',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsLdpEntityTable',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry.MplsldpsessionroleEnum' : _MetaInfoEnum('MplsldpsessionroleEnum', 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB',
        {
            'unknown':'unknown',
            'active':'active',
            'passive':'passive',
        }, 'MPLS-LDP-STD-MIB', _yang_ns._namespaces['MPLS-LDP-STD-MIB']),
    'MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry.MplsldpsessionstateEnum' : _MetaInfoEnum('MplsldpsessionstateEnum', 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB',
        {
            'nonexistent':'nonexistent',
            'initialized':'initialized',
            'openrec':'openrec',
            'opensent':'opensent',
            'operational':'operational',
        }, 'MPLS-LDP-STD-MIB', _yang_ns._namespaces['MPLS-LDP-STD-MIB']),
    'MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry',
            False, 
            [
            _MetaInfoClassMember('mplsLdpEntityLdpId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'mplsldpentityldpid',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpEntityIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'mplsldpentityindex',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpPeerLdpId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The LDP identifier of this LDP Peer.
                ''',
                'mplsldppeerldpid',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpPeerLabelDistMethod', REFERENCE_ENUM_CLASS, 'MplslabeldistributionmethodEnum' , 'ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplslabeldistributionmethodEnum', 
                [], [], 
                '''                For any given LDP session, the method of
                label distribution must be specified.
                ''',
                'mplsldppeerlabeldistmethod',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpPeerPathVectorLimit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                If the value of this object is 0 (zero) then
                Loop Dection for Path Vectors for this Peer
                is disabled.
                
                Otherwise, if this object has a value greater than
                zero, then Loop Dection for Path  Vectors for this
                Peer is enabled and the Path Vector Limit is this value.
                ''',
                'mplsldppeerpathvectorlimit',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpPeerTransportAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The Internet address advertised by the peer
                in the Hello Message or the Hello source address.
                
                The type of this address is specified by the
                value of the mplsLdpPeerTransportAddrType
                object.
                ''',
                'mplsldppeertransportaddr',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpPeerTransportAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The type of the Internet address for the
                mplsLdpPeerTransportAddr object.  The LDP
                specification describes this as being either
                an IPv4 Transport Address or IPv6 Transport
                
                
                Address which is used in opening the LDP session's
                TCP connection, or if the optional TLV is not
                present, then this is the IPv4/IPv6 source
                address for the UPD packet carrying the Hellos.
                
                This object specifies how the value of the
                mplsLdpPeerTransportAddr object should be
                interpreted.
                ''',
                'mplsldppeertransportaddrtype',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpSessionDiscontinuityTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion
                at which any one or more of this session's counters
                suffered a discontinuity.  The relevant counters are
                the specific instances associated with this session
                of any Counter32 object contained in the
                mplsLdpSessionStatsTable.
                
                The initial value of this object is the value of
                sysUpTime when the entry was created in this table.
                
                Also, a command generator can distinguish when a session
                between a given Entity and Peer goes away and a new
                session is established.  This value would change and
                thus indicate to the command generator that this is a
                different session.
                ''',
                'mplsldpsessiondiscontinuitytime',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpSessionKeepAliveHoldTimeRem', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The keep alive hold time remaining for
                this session.
                ''',
                'mplsldpsessionkeepaliveholdtimerem',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpSessionKeepAliveTime', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The negotiated KeepAlive Time which
                represents the amount of seconds between
                keep alive messages.  The
                mplsLdpEntityKeepAliveHoldTimer
                related to this Session is the
                value that was proposed as the
                KeepAlive Time for this session.
                
                This value is negotiated during
                session initialization between
                the entity's proposed value
                (i.e., the value configured in
                mplsLdpEntityKeepAliveHoldTimer)
                and the peer's proposed
                KeepAlive Hold Timer value.
                This value is the smaller
                of the two proposed values.
                ''',
                'mplsldpsessionkeepalivetime',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpSessionMaxPduLength', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The value of maximum allowable length for LDP PDUs for
                this session.  This value may have been negotiated
                during the Session Initialization.  This object is
                related to the mplsLdpEntityMaxPduLength object.  The
                mplsLdpEntityMaxPduLength object specifies the requested
                LDP PDU length, and this object reflects the negotiated
                LDP PDU length between the Entity and
                the Peer.
                ''',
                'mplsldpsessionmaxpdulength',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpSessionProtocolVersion', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The version of the LDP Protocol which
                this session is using.  This is the version of
                
                
                the LDP protocol which has been negotiated
                during session initialization.
                ''',
                'mplsldpsessionprotocolversion',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpSessionRole', REFERENCE_ENUM_CLASS, 'MplsldpsessionroleEnum' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry.MplsldpsessionroleEnum', 
                [], [], 
                '''                During session establishment the LSR/LER takes either
                the active role or the passive role based on address
                comparisons.  This object indicates whether this LSR/LER
                was behaving in an active role or passive role during
                this session's establishment.
                
                The value of unknown(1), indicates that the role is not
                able to be determined at the present time.
                ''',
                'mplsldpsessionrole',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpSessionState', REFERENCE_ENUM_CLASS, 'MplsldpsessionstateEnum' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry.MplsldpsessionstateEnum', 
                [], [], 
                '''                The current state of the session, all of the
                states 1 to 5 are based on the state machine
                for session negotiation behavior.
                ''',
                'mplsldpsessionstate',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpSessionStateLastChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time this
                Session entered its current state as
                denoted by the mplsLdpSessionState
                object.
                ''',
                'mplsldpsessionstatelastchange',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpSessionStatsUnknownMesTypeErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Unknown Message Type
                Errors detected by this LSR/LER during this session.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                mplsLdpSessionDiscontinuityTime.
                ''',
                'mplsldpsessionstatsunknownmestypeerrors',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpSessionStatsUnknownTlvErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object counts the number of Unknown TLV Errors
                detected by this LSR/LER during this session.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                mplsLdpSessionDiscontinuityTime.
                ''',
                'mplsldpsessionstatsunknowntlverrors',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsLdpPeerEntry',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsldppeertable' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsldppeertable',
            False, 
            [
            _MetaInfoClassMember('mplsLdpPeerEntry', REFERENCE_LIST, 'Mplsldppeerentry' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry', 
                [], [], 
                '''                Information about a single Peer which is related
                to a Session.  This table is augmented by
                the mplsLdpSessionTable.
                ''',
                'mplsldppeerentry',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsLdpPeerTable',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsldphelloadjacencytable.Mplsldphelloadjacencyentry.MplsldphelloadjacencytypeEnum' : _MetaInfoEnum('MplsldphelloadjacencytypeEnum', 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB',
        {
            'link':'link',
            'targeted':'targeted',
        }, 'MPLS-LDP-STD-MIB', _yang_ns._namespaces['MPLS-LDP-STD-MIB']),
    'MplsLdpStdMib.Mplsldphelloadjacencytable.Mplsldphelloadjacencyentry' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsldphelloadjacencytable.Mplsldphelloadjacencyentry',
            False, 
            [
            _MetaInfoClassMember('mplsLdpEntityLdpId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'mplsldpentityldpid',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpEntityIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'mplsldpentityindex',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpPeerLdpId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'mplsldppeerldpid',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpHelloAdjacencyIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An identifier for this specific adjacency.
                ''',
                'mplsldphelloadjacencyindex',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpHelloAdjacencyHoldTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The Hello hold time which is negotiated between
                the Entity and the Peer.  The entity associated
                with this Hello Adjacency issues a proposed
                Hello Hold Time value in the
                mplsLdpEntityHelloHoldTimer object.  The peer
                also proposes a value and this object represents
                the negotiated value.
                
                A value of 0 means the default,
                which is 15 seconds for Link Hellos
                and 45 seconds for Targeted Hellos.
                A value of 65535 indicates an
                infinite hold time.
                ''',
                'mplsldphelloadjacencyholdtime',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpHelloAdjacencyHoldTimeRem', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                If the value of this object is 65535,
                this means that the hold time is infinite
                (i.e., wait forever).
                
                Otherwise, the time remaining for
                this Hello Adjacency to receive its
                next Hello Message.
                
                This interval will change when the 'next'
                Hello Message which corresponds to this
                Hello Adjacency is received unless it
                is infinite.
                ''',
                'mplsldphelloadjacencyholdtimerem',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpHelloAdjacencyType', REFERENCE_ENUM_CLASS, 'MplsldphelloadjacencytypeEnum' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldphelloadjacencytable.Mplsldphelloadjacencyentry.MplsldphelloadjacencytypeEnum', 
                [], [], 
                '''                This adjacency is the result of a 'link'
                hello if the value of this object is link(1).
                
                
                Otherwise, it is a result of a 'targeted'
                hello, targeted(2).
                ''',
                'mplsldphelloadjacencytype',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsLdpHelloAdjacencyEntry',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsldphelloadjacencytable' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsldphelloadjacencytable',
            False, 
            [
            _MetaInfoClassMember('mplsLdpHelloAdjacencyEntry', REFERENCE_LIST, 'Mplsldphelloadjacencyentry' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldphelloadjacencytable.Mplsldphelloadjacencyentry', 
                [], [], 
                '''                Each row represents a single LDP Hello Adjacency.
                An LDP Session can have one or more Hello
                Adjacencies.
                ''',
                'mplsldphelloadjacencyentry',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsLdpHelloAdjacencyTable',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsinsegmentldplsptable.Mplsinsegmentldplspentry' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsinsegmentldplsptable.Mplsinsegmentldplspentry',
            False, 
            [
            _MetaInfoClassMember('mplsLdpEntityLdpId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'mplsldpentityldpid',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpEntityIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'mplsldpentityindex',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpPeerLdpId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'mplsldppeerldpid',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsInSegmentLdpLspIndex', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                This contains the same value as the
                mplsInSegmentIndex in the
                MPLS-LSR-STD-MIB's mplsInSegmentTable.
                ''',
                'mplsinsegmentldplspindex',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsInSegmentLdpLspLabelType', REFERENCE_ENUM_CLASS, 'MplsldplabeltypeEnum' , 'ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplsldplabeltypeEnum', 
                [], [], 
                '''                The Layer 2 Label Type.
                ''',
                'mplsinsegmentldplsplabeltype',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsInSegmentLdpLspType', REFERENCE_ENUM_CLASS, 'MplslsptypeEnum' , 'ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplslsptypeEnum', 
                [], [], 
                '''                The type of LSP connection.
                ''',
                'mplsinsegmentldplsptype',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsInSegmentLdpLspEntry',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsinsegmentldplsptable' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsinsegmentldplsptable',
            False, 
            [
            _MetaInfoClassMember('mplsInSegmentLdpLspEntry', REFERENCE_LIST, 'Mplsinsegmentldplspentry' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsinsegmentldplsptable.Mplsinsegmentldplspentry', 
                [], [], 
                '''                An entry in this table represents information
                on a single LDP LSP which is represented by
                a session's index triple (mplsLdpEntityLdpId,
                mplsLdpEntityIndex, mplsLdpPeerLdpId) AND the
                index for the mplsInSegmentTable
                (mplsInSegmentLdpLspLabelIndex) from the
                MPLS-LSR-STD-MIB.
                
                The information contained in a row is read-only.
                ''',
                'mplsinsegmentldplspentry',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsInSegmentLdpLspTable',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsoutsegmentldplsptable.Mplsoutsegmentldplspentry' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsoutsegmentldplsptable.Mplsoutsegmentldplspentry',
            False, 
            [
            _MetaInfoClassMember('mplsLdpEntityLdpId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'mplsldpentityldpid',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpEntityIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'mplsldpentityindex',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpPeerLdpId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'mplsldppeerldpid',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsOutSegmentLdpLspIndex', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                This contains the same value as the
                mplsOutSegmentIndex in the
                MPLS-LSR-STD-MIB's mplsOutSegmentTable.
                ''',
                'mplsoutsegmentldplspindex',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsOutSegmentLdpLspLabelType', REFERENCE_ENUM_CLASS, 'MplsldplabeltypeEnum' , 'ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplsldplabeltypeEnum', 
                [], [], 
                '''                The Layer 2 Label Type.
                ''',
                'mplsoutsegmentldplsplabeltype',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentLdpLspType', REFERENCE_ENUM_CLASS, 'MplslsptypeEnum' , 'ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplslsptypeEnum', 
                [], [], 
                '''                The type of LSP connection.
                ''',
                'mplsoutsegmentldplsptype',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsOutSegmentLdpLspEntry',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsoutsegmentldplsptable' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsoutsegmentldplsptable',
            False, 
            [
            _MetaInfoClassMember('mplsOutSegmentLdpLspEntry', REFERENCE_LIST, 'Mplsoutsegmentldplspentry' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsoutsegmentldplsptable.Mplsoutsegmentldplspentry', 
                [], [], 
                '''                An entry in this table represents information
                on a single LDP LSP which is represented by
                a session's index triple (mplsLdpEntityLdpId,
                mplsLdpEntityIndex, mplsLdpPeerLdpId) AND the
                index (mplsOutSegmentLdpLspIndex)
                for the mplsOutSegmentTable.
                
                The information contained in a row is read-only.
                ''',
                'mplsoutsegmentldplspentry',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsOutSegmentLdpLspTable',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsfectable.Mplsfecentry.MplsfectypeEnum' : _MetaInfoEnum('MplsfectypeEnum', 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB',
        {
            'prefix':'prefix',
            'hostAddress':'hostAddress',
        }, 'MPLS-LDP-STD-MIB', _yang_ns._namespaces['MPLS-LDP-STD-MIB']),
    'MplsLdpStdMib.Mplsfectable.Mplsfecentry' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsfectable.Mplsfecentry',
            False, 
            [
            _MetaInfoClassMember('mplsFecIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                The index which uniquely identifies this entry.
                ''',
                'mplsfecindex',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsFecAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The value of this object is interpreted based
                on the value of the 'mplsFecAddrType' object.
                
                This address is then further interpretted as
                an being used with the address prefix,
                or as the host address.  This further interpretation
                is indicated by the 'mplsFecType' object.
                In other words, the FEC element is populated
                according to the Prefix FEC Element value encoding, or
                the Host Address FEC Element encoding.
                ''',
                'mplsfecaddr',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsFecAddrPrefixLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '2040')], [], 
                '''                If the value of the 'mplsFecType' is 'hostAddress(2)'
                then this object is undefined.
                
                If the value of 'mplsFecType' is 'prefix(1)'
                then the value of this object is the length in
                bits of the address prefix represented by
                'mplsFecAddr', or zero.  If the value of this
                object is zero, this indicates that the
                prefix matches all addresses.  In this case the
                address prefix MUST also be zero (i.e., 'mplsFecAddr'
                should have the value of zero.)
                ''',
                'mplsfecaddrprefixlength',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsFecAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The value of this object is the type of the
                Internet address.  The value of this object,
                decides how the value of the mplsFecAddr object
                is interpreted.
                ''',
                'mplsfecaddrtype',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsFecRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row.  If the value of this
                object is 'active(1)', then none of the writable objects
                of this entry can be modified, except to set this object
                to 'destroy(6)'.
                
                NOTE: if this row is being referenced by any entry in
                the mplsLdpLspFecTable, then a request to destroy
                this row, will result in an inconsistentValue error.
                ''',
                'mplsfecrowstatus',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsFecStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.
                Conceptual rows having the value 'permanent(4)'
                need not allow write-access to any columnar
                objects in the row.
                ''',
                'mplsfecstoragetype',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsFecType', REFERENCE_ENUM_CLASS, 'MplsfectypeEnum' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsfectable.Mplsfecentry.MplsfectypeEnum', 
                [], [], 
                '''                The type of the FEC.  If the value of this object
                is 'prefix(1)' then the FEC type described by this
                row is an address prefix.
                
                If the value of this object is 'hostAddress(2)' then
                the FEC type described by this row is a host address.
                ''',
                'mplsfectype',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsFecEntry',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsfectable' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsfectable',
            False, 
            [
            _MetaInfoClassMember('mplsFecEntry', REFERENCE_LIST, 'Mplsfecentry' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsfectable.Mplsfecentry', 
                [], [], 
                '''                Each row represents a single FEC Element.
                ''',
                'mplsfecentry',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsFecTable',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsldplspfectable.Mplsldplspfecentry.MplsldplspfecsegmentEnum' : _MetaInfoEnum('MplsldplspfecsegmentEnum', 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB',
        {
            'inSegment':'inSegment',
            'outSegment':'outSegment',
        }, 'MPLS-LDP-STD-MIB', _yang_ns._namespaces['MPLS-LDP-STD-MIB']),
    'MplsLdpStdMib.Mplsldplspfectable.Mplsldplspfecentry' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsldplspfectable.Mplsldplspfecentry',
            False, 
            [
            _MetaInfoClassMember('mplsLdpEntityLdpId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'mplsldpentityldpid',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpEntityIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'mplsldpentityindex',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpPeerLdpId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'mplsldppeerldpid',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpLspFecSegment', REFERENCE_ENUM_CLASS, 'MplsldplspfecsegmentEnum' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldplspfectable.Mplsldplspfecentry.MplsldplspfecsegmentEnum', 
                [], [], 
                '''                If the value is inSegment(1), then this
                indicates that the following index,
                mplsLdpLspFecSegmentIndex, contains the same
                value as the mplsInSegmentLdpLspIndex.
                
                Otherwise, if the value of this object is
                
                
                outSegment(2),  then this
                indicates that following index,
                mplsLdpLspFecSegmentIndex, contains the same
                value as the mplsOutSegmentLdpLspIndex.
                ''',
                'mplsldplspfecsegment',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpLspFecSegmentIndex', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                This index is interpretted by using the value
                of the mplsLdpLspFecSegment.
                
                If the mplsLdpLspFecSegment is inSegment(1),
                then this index has the same value as
                mplsInSegmentLdpLspIndex.
                
                If the mplsLdpLspFecSegment is outSegment(2),
                then this index has the same value as
                mplsOutSegmentLdpLspIndex.
                ''',
                'mplsldplspfecsegmentindex',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpLspFecIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This index identifies the FEC entry in the
                mplsFecTable associated with this session.
                In other words, the value of this index
                is the same as the value of the mplsFecIndex
                that denotes the FEC associated with this
                Session.
                ''',
                'mplsldplspfecindex',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpLspFecRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this conceptual row.  If the
                value of this object is 'active(1)', then
                none of the writable objects of this entry
                can be modified.
                
                The Agent should delete this row when
                the session ceases to exist.  If an
                operator wants to associate the session with
                a different FEC, the recommended
                procedure is (as described in detail in the section
                entitled, 'Changing Values After Session
                Establishment', and again described in the
                DESCRIPTION clause of the
                mplsLdpEntityAdminStatus object)
                is to set the mplsLdpEntityAdminStatus to
                down, thereby explicitly causing a session
                to be torn down. This will also
                cause this entry to be deleted.
                
                Then, set the mplsLdpEntityAdminStatus
                to enable which enables a new session to be initiated.
                Once the session is initiated, an entry may be
                added to this table to associate the new session
                with a FEC.
                ''',
                'mplsldplspfecrowstatus',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpLspFecStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this conceptual row.
                Conceptual rows having the value 'permanent(4)'
                need not allow write-access to any columnar
                objects in the row.
                ''',
                'mplsldplspfecstoragetype',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsLdpLspFecEntry',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsldplspfectable' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsldplspfectable',
            False, 
            [
            _MetaInfoClassMember('mplsLdpLspFecEntry', REFERENCE_LIST, 'Mplsldplspfecentry' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldplspfectable.Mplsldplspfecentry', 
                [], [], 
                '''                An entry represents a LDP LSP
                to FEC association.
                ''',
                'mplsldplspfecentry',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsLdpLspFecTable',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsldpsessionpeeraddrtable.Mplsldpsessionpeeraddrentry' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsldpsessionpeeraddrtable.Mplsldpsessionpeeraddrentry',
            False, 
            [
            _MetaInfoClassMember('mplsLdpEntityLdpId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'mplsldpentityldpid',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpEntityIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'mplsldpentityindex',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpPeerLdpId', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'mplsldppeerldpid',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpSessionPeerAddrIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An index which uniquely identifies this entry within
                a given session.
                ''',
                'mplsldpsessionpeeraddrindex',
                'MPLS-LDP-STD-MIB', True),
            _MetaInfoClassMember('mplsLdpSessionPeerNextHopAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The next hop address.  The type of this address
                is specified by the value of the
                mplsLdpSessionPeerNextHopAddrType.
                ''',
                'mplsldpsessionpeernexthopaddr',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpSessionPeerNextHopAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The internetwork layer address type of this Next Hop
                Address as specified in the Label Address Message
                associated with this Session. The value of this
                object indicates how to interpret the value of
                
                
                mplsLdpSessionPeerNextHopAddr.
                ''',
                'mplsldpsessionpeernexthopaddrtype',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsLdpSessionPeerAddrEntry',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib.Mplsldpsessionpeeraddrtable' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib.Mplsldpsessionpeeraddrtable',
            False, 
            [
            _MetaInfoClassMember('mplsLdpSessionPeerAddrEntry', REFERENCE_LIST, 'Mplsldpsessionpeeraddrentry' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldpsessionpeeraddrtable.Mplsldpsessionpeeraddrentry', 
                [], [], 
                '''                An entry in this table represents information on
                a session's single next hop address which was
                advertised in an Address Message from the LDP peer.
                The information contained in a row is read-only.
                ''',
                'mplsldpsessionpeeraddrentry',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'mplsLdpSessionPeerAddrTable',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
    'MplsLdpStdMib' : {
        'meta_info' : _MetaInfoClass('MplsLdpStdMib',
            False, 
            [
            _MetaInfoClassMember('mplsFecObjects', REFERENCE_CLASS, 'Mplsfecobjects' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsfecobjects', 
                [], [], 
                '''                ''',
                'mplsfecobjects',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsFecTable', REFERENCE_CLASS, 'Mplsfectable' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsfectable', 
                [], [], 
                '''                This table represents the FEC
                (Forwarding Equivalence Class)
                Information associated with an LSP.
                ''',
                'mplsfectable',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsInSegmentLdpLspTable', REFERENCE_CLASS, 'Mplsinsegmentldplsptable' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsinsegmentldplsptable', 
                [], [], 
                '''                A table of LDP LSP's which
                map to the mplsInSegmentTable in the
                MPLS-LSR-STD-MIB module.
                ''',
                'mplsinsegmentldplsptable',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityObjects', REFERENCE_CLASS, 'Mplsldpentityobjects' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldpentityobjects', 
                [], [], 
                '''                ''',
                'mplsldpentityobjects',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpEntityTable', REFERENCE_CLASS, 'Mplsldpentitytable' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldpentitytable', 
                [], [], 
                '''                This table contains information about the
                MPLS Label Distribution Protocol Entities which
                exist on this Label Switching Router (LSR)
                or Label Edge Router (LER).
                ''',
                'mplsldpentitytable',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpHelloAdjacencyTable', REFERENCE_CLASS, 'Mplsldphelloadjacencytable' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldphelloadjacencytable', 
                [], [], 
                '''                A table of Hello Adjacencies for Sessions.
                ''',
                'mplsldphelloadjacencytable',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpLspFecTable', REFERENCE_CLASS, 'Mplsldplspfectable' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldplspfectable', 
                [], [], 
                '''                A table which shows the relationship between
                LDP LSPs and FECs.  Each row represents
                a single LDP LSP to FEC association.
                ''',
                'mplsldplspfectable',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpLsrObjects', REFERENCE_CLASS, 'Mplsldplsrobjects' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldplsrobjects', 
                [], [], 
                '''                ''',
                'mplsldplsrobjects',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpPeerTable', REFERENCE_CLASS, 'Mplsldppeertable' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldppeertable', 
                [], [], 
                '''                Information about LDP peers known by Entities in
                the mplsLdpEntityTable.  The information in this table
                is based on information from the Entity-Peer interaction
                during session initialization but is not appropriate
                for the mplsLdpSessionTable, because objects in this
                table may or may not be used in session establishment.
                ''',
                'mplsldppeertable',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpSessionObjects', REFERENCE_CLASS, 'Mplsldpsessionobjects' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldpsessionobjects', 
                [], [], 
                '''                ''',
                'mplsldpsessionobjects',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsLdpSessionPeerAddrTable', REFERENCE_CLASS, 'Mplsldpsessionpeeraddrtable' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsldpsessionpeeraddrtable', 
                [], [], 
                '''                This table 'extends' the mplsLdpSessionTable.
                This table is used to store Label Address Information
                from Label Address Messages received by this LSR from
                Peers.  This table is read-only and should be updated
                
                
                when Label Withdraw Address Messages are received, i.e.,
                Rows should be deleted as appropriate.
                
                NOTE:  since more than one address may be contained
                in a Label Address Message, this table 'sparse augments',
                the mplsLdpSessionTable's information.
                ''',
                'mplsldpsessionpeeraddrtable',
                'MPLS-LDP-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentLdpLspTable', REFERENCE_CLASS, 'Mplsoutsegmentldplsptable' , 'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB', 'MplsLdpStdMib.Mplsoutsegmentldplsptable', 
                [], [], 
                '''                A table of LDP LSP's which
                map to the mplsOutSegmentTable in the
                MPLS-LSR-STD-MIB.
                ''',
                'mplsoutsegmentldplsptable',
                'MPLS-LDP-STD-MIB', False),
            ],
            'MPLS-LDP-STD-MIB',
            'MPLS-LDP-STD-MIB',
            _yang_ns._namespaces['MPLS-LDP-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_LDP_STD_MIB'
        ),
    },
}
_meta_table['MplsLdpStdMib.Mplsldpentitytable.Mplsldpentityentry']['meta_info'].parent =_meta_table['MplsLdpStdMib.Mplsldpentitytable']['meta_info']
_meta_table['MplsLdpStdMib.Mplsldppeertable.Mplsldppeerentry']['meta_info'].parent =_meta_table['MplsLdpStdMib.Mplsldppeertable']['meta_info']
_meta_table['MplsLdpStdMib.Mplsldphelloadjacencytable.Mplsldphelloadjacencyentry']['meta_info'].parent =_meta_table['MplsLdpStdMib.Mplsldphelloadjacencytable']['meta_info']
_meta_table['MplsLdpStdMib.Mplsinsegmentldplsptable.Mplsinsegmentldplspentry']['meta_info'].parent =_meta_table['MplsLdpStdMib.Mplsinsegmentldplsptable']['meta_info']
_meta_table['MplsLdpStdMib.Mplsoutsegmentldplsptable.Mplsoutsegmentldplspentry']['meta_info'].parent =_meta_table['MplsLdpStdMib.Mplsoutsegmentldplsptable']['meta_info']
_meta_table['MplsLdpStdMib.Mplsfectable.Mplsfecentry']['meta_info'].parent =_meta_table['MplsLdpStdMib.Mplsfectable']['meta_info']
_meta_table['MplsLdpStdMib.Mplsldplspfectable.Mplsldplspfecentry']['meta_info'].parent =_meta_table['MplsLdpStdMib.Mplsldplspfectable']['meta_info']
_meta_table['MplsLdpStdMib.Mplsldpsessionpeeraddrtable.Mplsldpsessionpeeraddrentry']['meta_info'].parent =_meta_table['MplsLdpStdMib.Mplsldpsessionpeeraddrtable']['meta_info']
_meta_table['MplsLdpStdMib.Mplsldplsrobjects']['meta_info'].parent =_meta_table['MplsLdpStdMib']['meta_info']
_meta_table['MplsLdpStdMib.Mplsldpentityobjects']['meta_info'].parent =_meta_table['MplsLdpStdMib']['meta_info']
_meta_table['MplsLdpStdMib.Mplsldpsessionobjects']['meta_info'].parent =_meta_table['MplsLdpStdMib']['meta_info']
_meta_table['MplsLdpStdMib.Mplsfecobjects']['meta_info'].parent =_meta_table['MplsLdpStdMib']['meta_info']
_meta_table['MplsLdpStdMib.Mplsldpentitytable']['meta_info'].parent =_meta_table['MplsLdpStdMib']['meta_info']
_meta_table['MplsLdpStdMib.Mplsldppeertable']['meta_info'].parent =_meta_table['MplsLdpStdMib']['meta_info']
_meta_table['MplsLdpStdMib.Mplsldphelloadjacencytable']['meta_info'].parent =_meta_table['MplsLdpStdMib']['meta_info']
_meta_table['MplsLdpStdMib.Mplsinsegmentldplsptable']['meta_info'].parent =_meta_table['MplsLdpStdMib']['meta_info']
_meta_table['MplsLdpStdMib.Mplsoutsegmentldplsptable']['meta_info'].parent =_meta_table['MplsLdpStdMib']['meta_info']
_meta_table['MplsLdpStdMib.Mplsfectable']['meta_info'].parent =_meta_table['MplsLdpStdMib']['meta_info']
_meta_table['MplsLdpStdMib.Mplsldplspfectable']['meta_info'].parent =_meta_table['MplsLdpStdMib']['meta_info']
_meta_table['MplsLdpStdMib.Mplsldpsessionpeeraddrtable']['meta_info'].parent =_meta_table['MplsLdpStdMib']['meta_info']
