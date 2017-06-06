


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MplsTeStdMib.Mplstescalars' : {
        'meta_info' : _MetaInfoClass('MplsTeStdMib.Mplstescalars',
            False, 
            [
            _MetaInfoClassMember('mplsTunnelActive', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of tunnels active on this device. A
                tunnel is considered active if the
                mplsTunnelOperStatus is up(1).
                ''',
                'mplstunnelactive',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelConfigured', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of tunnels configured on this device. A
                tunnel is considered configured if the
                mplsTunnelRowStatus is active(1).
                ''',
                'mplstunnelconfigured',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelMaxHops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum number of hops that can be specified for
                a tunnel on this device.
                ''',
                'mplstunnelmaxhops',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelNotificationMaxRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This variable indicates the maximum number of
                notifications issued per second. If events occur
                more rapidly, the implementation may simply fail to
                emit these notifications during that period, or may
                queue them until an appropriate time. A value of 0
                means no throttling is applied and events may be
                notified at the rate at which they occur.
                ''',
                'mplstunnelnotificationmaxrate',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelTEDistProto', REFERENCE_BITS, 'Mplstunneltedistproto' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstescalars.Mplstunneltedistproto', 
                [], [], 
                '''                The traffic engineering distribution protocol(s)
                used by this LSR. Note that an LSR may support more
                than one distribution protocol simultaneously.
                ''',
                'mplstunneltedistproto',
                'MPLS-TE-STD-MIB', False),
            ],
            'MPLS-TE-STD-MIB',
            'mplsTeScalars',
            _yang_ns._namespaces['MPLS-TE-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB'
        ),
    },
    'MplsTeStdMib.Mplsteobjects' : {
        'meta_info' : _MetaInfoClass('MplsTeStdMib.Mplsteobjects',
            False, 
            [
            _MetaInfoClassMember('mplsTunnelHopListIndexNext', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains an appropriate value to be used
                for mplsTunnelHopListIndex when creating entries in
                the mplsTunnelHopTable.  If the number of
                unassigned entries is exhausted, a retrieval
                operation will return a value of 0.  This object
                may also return a value of 0 when the LSR is unable
                to accept conceptual row creation, for example, if
                the mplsTunnelHopTable is implemented as read-only.
                To obtain the value of mplsTunnelHopListIndex for a
                new entry in the mplsTunnelHopTable, the manager
                issues a management protocol retrieval operation to
                obtain the current value of mplsTunnelHopIndex.
                
                When the SET is performed to create a row in the
                mplsTunnelHopTable, the Command Responder (agent)
                must determine whether the value is indeed still
                unused; Two Network Management Applications may
                attempt to create a row (configuration entry)
                simultaneously and use the same value. If it is
                currently unused, the SET succeeds and the Command
                Responder (agent) changes the value of this object,
                according to an implementation-specific algorithm.
                If the value is in use, however, the SET fails.  The
                Network Management Application must then re-read
                this variable to obtain a new usable value.
                ''',
                'mplstunnelhoplistindexnext',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelIndexNext', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object contains an unused value for
                mplsTunnelIndex, or a zero to indicate
                that none exist. Negative values are not allowed,
                as they do not correspond to valid values of
                mplsTunnelIndex.
                
                Note that this object offers an unused value
                for an mplsTunnelIndex value at the ingress
                side of a tunnel. At other LSRs the value
                of mplsTunnelIndex SHOULD be taken from the
                value signaled by the MPLS signaling protocol.
                ''',
                'mplstunnelindexnext',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelNotificationEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this object is true, then it enables the
                generation of mplsTunnelUp and mplsTunnelDown
                traps, otherwise these traps are not emitted.
                ''',
                'mplstunnelnotificationenable',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelResourceIndexNext', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object contains the next appropriate value to
                be used for mplsTunnelResourceIndex when creating
                entries in the mplsTunnelResourceTable. If the
                number of unassigned entries is exhausted, a
                retrieval operation will return a value of 0.  This
                object may also return a value of 0 when the LSR is
                unable to accept conceptual row creation, for
                example, if the mplsTunnelTable is implemented as
                read-only.  To obtain the mplsTunnelResourceIndex
                value for a new entry, the manager must first issue
                a management protocol retrieval operation to obtain
                the current value of this object.
                
                When the SET is performed to create a row in the
                mplsTunnelResourceTable, the Command Responder
                (agent) must determine whether the value is indeed
                still unused; Two Network Management Applications
                may attempt to create a row (configuration entry)
                simultaneously and use the same value. If it is
                currently unused, the SET succeeds and the Command
                Responder (agent) changes the value of this object,
                according to an implementation-specific algorithm.
                If the value is in use, however, the SET fails.  The
                Network Management Application must then re-read
                this variable to obtain a new usable value.
                ''',
                'mplstunnelresourceindexnext',
                'MPLS-TE-STD-MIB', False),
            ],
            'MPLS-TE-STD-MIB',
            'mplsTeObjects',
            _yang_ns._namespaces['MPLS-TE-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB'
        ),
    },
    'MplsTeStdMib.Mplstunneltable.Mplstunnelentry.MplstunneladminstatusEnum' : _MetaInfoEnum('MplstunneladminstatusEnum', 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB',
        {
            'up':'up',
            'down':'down',
            'testing':'testing',
        }, 'MPLS-TE-STD-MIB', _yang_ns._namespaces['MPLS-TE-STD-MIB']),
    'MplsTeStdMib.Mplstunneltable.Mplstunnelentry.MplstunneloperstatusEnum' : _MetaInfoEnum('MplstunneloperstatusEnum', 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB',
        {
            'up':'up',
            'down':'down',
            'testing':'testing',
            'unknown':'unknown',
            'dormant':'dormant',
            'notPresent':'notPresent',
            'lowerLayerDown':'lowerLayerDown',
        }, 'MPLS-TE-STD-MIB', _yang_ns._namespaces['MPLS-TE-STD-MIB']),
    'MplsTeStdMib.Mplstunneltable.Mplstunnelentry.MplstunnelroleEnum' : _MetaInfoEnum('MplstunnelroleEnum', 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB',
        {
            'head':'head',
            'transit':'transit',
            'tail':'tail',
            'headTail':'headTail',
        }, 'MPLS-TE-STD-MIB', _yang_ns._namespaces['MPLS-TE-STD-MIB']),
    'MplsTeStdMib.Mplstunneltable.Mplstunnelentry.MplstunnelsignallingprotoEnum' : _MetaInfoEnum('MplstunnelsignallingprotoEnum', 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB',
        {
            'none':'none',
            'rsvp':'rsvp',
            'crldp':'crldp',
            'other':'other',
        }, 'MPLS-TE-STD-MIB', _yang_ns._namespaces['MPLS-TE-STD-MIB']),
    'MplsTeStdMib.Mplstunneltable.Mplstunnelentry' : {
        'meta_info' : _MetaInfoClass('MplsTeStdMib.Mplstunneltable.Mplstunnelentry',
            False, 
            [
            _MetaInfoClassMember('mplsTunnelIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Uniquely identifies a set of tunnel instances
                between a pair of ingress and egress LSRs.
                Managers should obtain new values for row
                creation in this table by reading
                mplsTunnelIndexNext. When
                the MPLS signalling protocol is rsvp(2) this value
                SHOULD be equal to the value signaled in the
                Tunnel Id of the Session object. When the MPLS
                signalling protocol is crldp(3) this value
                SHOULD be equal to the value signaled in the
                LSP ID.
                ''',
                'mplstunnelindex',
                'MPLS-TE-STD-MIB', True),
            _MetaInfoClassMember('mplsTunnelInstance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Uniquely identifies a particular instance of a
                tunnel between a pair of ingress and egress LSRs.
                It is useful to identify multiple instances of
                tunnels for the purposes of backup and parallel
                tunnels. When the MPLS signaling protocol is
                rsvp(2) this value SHOULD be equal to the LSP Id
                of the Sender Template object. When the signaling
                protocol is crldp(3) there is no equivalent
                signaling object.
                ''',
                'mplstunnelinstance',
                'MPLS-TE-STD-MIB', True),
            _MetaInfoClassMember('mplsTunnelIngressLSRId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Identity of the ingress LSR associated with this
                tunnel instance. When the MPLS signalling protocol
                is rsvp(2) this value SHOULD be equal to the Tunnel
                Sender Address in the Sender Template object and MAY
                be equal to the Extended Tunnel Id field in the
                SESSION object. When the MPLS signalling protocol is
                crldp(3) this value SHOULD be equal to the Ingress
                LSR Router ID field in the LSPID TLV object.
                ''',
                'mplstunnelingresslsrid',
                'MPLS-TE-STD-MIB', True),
            _MetaInfoClassMember('mplsTunnelEgressLSRId', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Identity of the egress LSR associated with this
                tunnel instance.
                ''',
                'mplstunnelegresslsrid',
                'MPLS-TE-STD-MIB', True),
            _MetaInfoClassMember('mplsTunnelAdminStatus', REFERENCE_ENUM_CLASS, 'MplstunneladminstatusEnum' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunneltable.Mplstunnelentry.MplstunneladminstatusEnum', 
                [], [], 
                '''                Indicates the desired operational status of this
                tunnel.
                ''',
                'mplstunneladminstatus',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelARHopTableIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index into the mplsTunnelARHopTable entry that
                specifies the actual hops traversed by the tunnel.
                This is automatically updated by the agent when the
                actual hops becomes available.
                ''',
                'mplstunnelarhoptableindex',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelCHopTableIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index into the mplsTunnelCHopTable entry that
                specifies the computed hops traversed by the
                tunnel. This is automatically updated by the agent
                when computed hops become available or when
                computed hops get modified.
                ''',
                'mplstunnelchoptableindex',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelCreationTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Specifies the value of SysUpTime when the first
                instance of this tunnel came into existence.
                That is, when the value of mplsTunnelOperStatus
                was first set to up(1).
                ''',
                'mplstunnelcreationtime',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelDescr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A textual string containing information about the
                tunnel.  If there is no description this object
                contains a zero length string. This object is may
                not be signaled by MPLS signaling protocols,
                consequentally the value of this object at transit
                and egress LSRs MAY be automatically generated or
                absent.
                ''',
                'mplstunneldescr',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelExcludeAnyAffinity', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A link satisfies the exclude-any constraint if and
                only if the link contains none of the
                administrative groups specified in the constraint.
                ''',
                'mplstunnelexcludeanyaffinity',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelHoldingPrio', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Indicates the holding priority for this tunnel.
                ''',
                'mplstunnelholdingprio',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelHopTableIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Index into the mplsTunnelHopTable entry that
                specifies the explicit route hops for this tunnel.
                This object is meaningful only at the head-end of
                the tunnel.
                ''',
                'mplstunnelhoptableindex',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                If mplsTunnelIsIf is set to true, then this value
                contains the LSR-assigned ifIndex which corresponds
                to an entry in the interfaces table.  Otherwise
                this variable should contain the value of zero
                indicating that a valid ifIndex was not assigned to
                this tunnel interface.
                ''',
                'mplstunnelifindex',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelIncludeAllAffinity', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A link satisfies the include-all constraint if and
                only if the link contains all of the administrative
                groups specified in the constraint.
                ''',
                'mplstunnelincludeallaffinity',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelIncludeAnyAffinity', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A link satisfies the include-any constraint if and
                only if the constraint is zero, or the link and the
                constraint have a resource class in common.
                ''',
                'mplstunnelincludeanyaffinity',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelInstancePriority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This value indicates which priority, in descending
                order, with 0 indicating the lowest priority,
                within a group of tunnel instances. A group of
                tunnel instances is defined as a set of LSPs with
                the same mplsTunnelIndex in this table, but with a
                different mplsTunnelInstance. Tunnel instance
                priorities are used to denote the priority at which
                a particular tunnel instance will supercede
                another. Instances of tunnels containing the same
                mplsTunnelInstancePriority will be used for load
                sharing.
                ''',
                'mplstunnelinstancepriority',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelInstanceUpTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This value identifies the total time that this
                tunnel instance's operStatus has been Up(1).
                ''',
                'mplstunnelinstanceuptime',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelIsIf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Denotes whether or not this tunnel corresponds to an
                interface represented in the interfaces group
                table. Note that if this variable is set to true
                then the ifName of the interface corresponding to
                this tunnel should have a value equal to
                mplsTunnelName.  Also see the description of ifName
                in RFC 2863.  This object is meaningful only at the
                ingress and egress LSRs.
                ''',
                'mplstunnelisif',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelLastPathChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Specifies the time since the last change to the
                actual path for this tunnel instance.
                ''',
                'mplstunnellastpathchange',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelLocalProtectInUse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates that the local repair mechanism is in use
                to maintain this tunnel (usually in the face of an
                outage of the link it was previously routed over).
                ''',
                'mplstunnellocalprotectinuse',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The canonical name assigned to the tunnel. This name
                can be used to refer to the tunnel on the LSR's
                console port.  If mplsTunnelIsIf is set to true
                then the ifName of the interface corresponding to
                this tunnel should have a value equal to
                mplsTunnelName.  Also see the description of ifName
                in RFC 2863.
                ''',
                'mplstunnelname',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelOperStatus', REFERENCE_ENUM_CLASS, 'MplstunneloperstatusEnum' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunneltable.Mplstunnelentry.MplstunneloperstatusEnum', 
                [], [], 
                '''                Indicates the actual operational status of this
                tunnel, which is typically but not limited to, a
                function of the state of individual segments of
                this tunnel.
                ''',
                'mplstunneloperstatus',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelOwner', REFERENCE_ENUM_CLASS, 'MplsownerEnum' , 'ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'MplsownerEnum', 
                [], [], 
                '''                Denotes the entity that created and is responsible
                for managing this tunnel. This column is
                automatically filled by the agent on creation of a
                row.
                ''',
                'mplstunnelowner',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelPathChanges', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Specifies the number of times the actual path for
                this tunnel instance has changed.
                ''',
                'mplstunnelpathchanges',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelPathInUse', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This value denotes the configured path that was
                chosen for this tunnel. This value reflects the
                secondary index into mplsTunnelHopTable. This path
                may not exactly match the one in
                mplsTunnelARHopTable due to the fact that some CSPF
                modification may have taken place. See
                mplsTunnelARHopTable for the actual path being
                taken by the tunnel. A value of zero denotes that
                no path is currently in use or available.
                ''',
                'mplstunnelpathinuse',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelPerfBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of bytes forwarded by the tunnel.
                This object should represents the 32-bit
                value of the least significant part of the
                64-bit value if both mplsTunnelPerfHCBytes
                is returned.
                ''',
                'mplstunnelperfbytes',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelPerfErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets dropped because of errors or for
                other reasons.
                ''',
                'mplstunnelperferrors',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelPerfHCBytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High capacity counter for number of bytes forwarded
                by the tunnel.
                ''',
                'mplstunnelperfhcbytes',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelPerfHCPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                High capacity counter for number of packets
                forwarded by the tunnel. 
                ''',
                'mplstunnelperfhcpackets',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelPerfPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets forwarded by the tunnel.
                This object should represents the 32-bit
                value of the least significant part of the
                64-bit value if both mplsTunnelPerfHCPackets
                is returned.
                ''',
                'mplstunnelperfpackets',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelPrimaryInstance', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Specifies the instance index of the primary instance
                of this tunnel. More details of the definition of
                tunnel instances and the primary tunnel instance
                can be found in the description of the TEXTUAL-CONVENTION
                MplsTunnelInstanceIndex.
                ''',
                'mplstunnelprimaryinstance',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelPrimaryUpTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Specifies the total time the primary instance of
                this tunnel has been active. The primary instance
                of this tunnel is defined in
                mplsTunnelPrimaryInstance.
                ''',
                'mplstunnelprimaryuptime',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelResourcePointer', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This variable represents a pointer to the traffic
                parameter specification for this tunnel.  This
                value may point at an entry in the
                mplsTunnelResourceEntry to indicate which
                mplsTunnelResourceEntry is to be assigned to this
                LSP instance.  This value may optionally point at
                an externally defined traffic parameter
                specification table.  A value of zeroDotZero
                indicates best-effort treatment.  By having the
                same value of this object, two or more LSPs can
                indicate resource sharing.
                ''',
                'mplstunnelresourcepointer',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelRole', REFERENCE_ENUM_CLASS, 'MplstunnelroleEnum' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunneltable.Mplstunnelentry.MplstunnelroleEnum', 
                [], [], 
                '''                This value signifies the role that this tunnel
                entry/instance represents. This value MUST be set
                to head(1) at the originating point of the tunnel.
                This value MUST be set to transit(2) at transit
                points along the tunnel, if transit points are
                supported. This value MUST be set to tail(3) at the
                terminating point of the tunnel if tunnel tails are
                supported.
                
                The value headTail(4) is provided for tunnels that
                begin and end on the same LSR.
                ''',
                'mplstunnelrole',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This variable is used to create, modify, and/or
                delete a row in this table.  When a row in this
                table is in active(1) state, no objects in that row
                can be modified by the agent except
                mplsTunnelAdminStatus, mplsTunnelRowStatus and
                mplsTunnelStorageType.
                ''',
                'mplstunnelrowstatus',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelSessionAttributes', REFERENCE_BITS, 'Mplstunnelsessionattributes' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunneltable.Mplstunnelentry.Mplstunnelsessionattributes', 
                [], [], 
                '''                This bit mask indicates optional session values for
                this tunnel. The following describes these bit
                fields:
                
                fastRerouteThis flag indicates that the any tunnel
                hop may choose to reroute this tunnel without
                tearing it down.  This flag permits transit routers
                to use a local repair mechanism which may result in
                violation of the explicit routing of this tunnel.
                When a fault is detected on an adjacent downstream
                link or node, a transit router can re-route traffic
                for fast service restoration.
                
                mergingPermitted This flag permits transit routers
                to merge this session with other RSVP sessions for
                the purpose of reducing resource overhead on
                downstream transit routers, thereby providing
                better network scaling.
                
                isPersistent  Indicates whether this tunnel should
                be restored automatically after a failure occurs.
                
                isPinned   This flag indicates whether the loose-
                routed hops of this tunnel are to be pinned.
                
                recordRouteThis flag indicates whether or not the
                signalling protocol should remember the tunnel path
                after it has been signaled.
                ''',
                'mplstunnelsessionattributes',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelSetupPrio', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                Indicates the setup priority of this tunnel.
                ''',
                'mplstunnelsetupprio',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelSignallingProto', REFERENCE_ENUM_CLASS, 'MplstunnelsignallingprotoEnum' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunneltable.Mplstunnelentry.MplstunnelsignallingprotoEnum', 
                [], [], 
                '''                The signalling protocol, if any, used to setup this
                tunnel.
                ''',
                'mplstunnelsignallingproto',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelStateTransitions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Specifies the number of times the state
                (mplsTunnelOperStatus) of this tunnel instance has
                changed.
                ''',
                'mplstunnelstatetransitions',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this tunnel entry.
                Conceptual rows having the value 'permanent'
                need not allow write-access to any columnar
                objects in the row.
                ''',
                'mplstunnelstoragetype',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelTotalUpTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This value represents the aggregate up time for all
                instances of this tunnel, if available. If this
                value is unavailable, it MUST return a value of 0.
                ''',
                'mplstunneltotaluptime',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelXCPointer', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This variable points to a row in the mplsXCTable.
                This table identifies the segments that compose
                this tunnel, their characteristics, and
                relationships to each other. A value of zeroDotZero
                indicates that no LSP has been associated with this
                tunnel yet.
                ''',
                'mplstunnelxcpointer',
                'MPLS-TE-STD-MIB', False),
            ],
            'MPLS-TE-STD-MIB',
            'mplsTunnelEntry',
            _yang_ns._namespaces['MPLS-TE-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB'
        ),
    },
    'MplsTeStdMib.Mplstunneltable' : {
        'meta_info' : _MetaInfoClass('MplsTeStdMib.Mplstunneltable',
            False, 
            [
            _MetaInfoClassMember('mplsTunnelEntry', REFERENCE_LIST, 'Mplstunnelentry' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunneltable.Mplstunnelentry', 
                [], [], 
                '''                An entry in this table represents an MPLS tunnel.
                An entry can be created by a network administrator
                or by an SNMP agent as instructed by an MPLS
                signalling protocol. Whenever a new entry is
                created with mplsTunnelIsIf set to true(1), then a
                corresponding entry is created in ifTable as well
                (see RFC 2863). The ifType of this entry is
                mplsTunnel(150).
                
                A tunnel entry needs to be uniquely identified across
                a MPLS network. Indices mplsTunnelIndex and
                mplsTunnelInstance uniquely identify a tunnel on
                the LSR originating the tunnel.  To uniquely
                identify a tunnel across an MPLS network requires
                index mplsTunnelIngressLSRId.  The last index
                mplsTunnelEgressLSRId is useful in identifying all
                instances of a tunnel that terminate on the same
                egress LSR.
                ''',
                'mplstunnelentry',
                'MPLS-TE-STD-MIB', False),
            ],
            'MPLS-TE-STD-MIB',
            'mplsTunnelTable',
            _yang_ns._namespaces['MPLS-TE-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB'
        ),
    },
    'MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry.MplstunnelhopentrypathcompEnum' : _MetaInfoEnum('MplstunnelhopentrypathcompEnum', 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB',
        {
            'dynamic':'dynamic',
            'explicit':'explicit',
        }, 'MPLS-TE-STD-MIB', _yang_ns._namespaces['MPLS-TE-STD-MIB']),
    'MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry.MplstunnelhoptypeEnum' : _MetaInfoEnum('MplstunnelhoptypeEnum', 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB',
        {
            'strict':'strict',
            'loose':'loose',
        }, 'MPLS-TE-STD-MIB', _yang_ns._namespaces['MPLS-TE-STD-MIB']),
    'MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry' : {
        'meta_info' : _MetaInfoClass('MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry',
            False, 
            [
            _MetaInfoClassMember('mplsTunnelHopListIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Primary index into this table identifying a
                particular explicit route object.
                ''',
                'mplstunnelhoplistindex',
                'MPLS-TE-STD-MIB', True),
            _MetaInfoClassMember('mplsTunnelHopPathOptionIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Secondary index into this table identifying a
                particular group of hops representing a particular
                configured path. This is otherwise known as a path
                option.
                ''',
                'mplstunnelhoppathoptionindex',
                'MPLS-TE-STD-MIB', True),
            _MetaInfoClassMember('mplsTunnelHopIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Tertiary index into this table identifying a
                particular hop.
                ''',
                'mplstunnelhopindex',
                'MPLS-TE-STD-MIB', True),
            _MetaInfoClassMember('mplsTunnelHopAddrType', REFERENCE_ENUM_CLASS, 'TehopaddresstypeEnum' , 'ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'TehopaddresstypeEnum', 
                [], [], 
                '''                The Hop Address Type of this tunnel hop.
                
                The value of this object cannot be changed
                if the value of the corresponding
                mplsTunnelHopRowStatus object is 'active'.
                
                Note that lspid(5) is a valid option only
                for tunnels signaled via CRLDP.
                ''',
                'mplstunnelhopaddrtype',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelHopAddrUnnum', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                If mplsTunnelHopAddrType is set to unnum(4), then
                this value will contain the interface identifier of
                the unnumbered interface for this hop. This object
                should be used in conjunction with
                mplsTunnelHopIpAddress which would contain the LSR
                Router ID in this case. Otherwise the agent should
                set this object to zero-length string and the
                manager should ignore this.
                ''',
                'mplstunnelhopaddrunnum',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelHopAsNumber', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                If mplsTunnelHopAddrType is set to asnumber(3), then
                this value will contain the AS number of this hop.
                Otherwise the agent should set this object to zero-
                length string and the manager should ignore this.
                ''',
                'mplstunnelhopasnumber',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelHopEntryPathComp', REFERENCE_ENUM_CLASS, 'MplstunnelhopentrypathcompEnum' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry.MplstunnelhopentrypathcompEnum', 
                [], [], 
                '''                If this value is set to dynamic, then the user
                should only specify the source and destination of
                the path and expect that the CSPF will calculate
                the remainder of the path.  If this value is set to
                explicit, the user should specify the entire path
                for the tunnel to take.  This path may contain
                strict or loose hops.  Each hop along a specific
                path SHOULD have this object set to the same value
                ''',
                'mplstunnelhopentrypathcomp',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelHopInclude', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this value is set to true, then this indicates
                that this hop must be included in the tunnel's
                path. If this value is set to 'false', then this hop
                must be avoided when calculating the path for this
                tunnel. The default value of this object is 'true',
                so that by default all indicated hops are included
                in the CSPF path computation. If this object is set
                to 'false' the value of mplsTunnelHopType should be
                ignored.
                ''',
                'mplstunnelhopinclude',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelHopIpAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The Tunnel Hop Address for this tunnel hop.
                
                The type of this address is determined by the
                value of the corresponding mplsTunnelHopAddrType.
                
                The value of this object cannot be changed
                if the value of the corresponding
                mplsTunnelHopRowStatus object is 'active'.
                ''',
                'mplstunnelhopipaddr',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelHopIpPrefixLen', ATTRIBUTE, 'int' , None, None, 
                [('0', '2040')], [], 
                '''                If mplsTunnelHopAddrType is set to ipv4(1) or
                ipv6(2), then this value will contain an
                appropriate prefix length for the IP address in
                object mplsTunnelHopIpAddr. Otherwise this value
                is irrelevant and should be ignored.
                ''',
                'mplstunnelhopipprefixlen',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelHopLspId', ATTRIBUTE, 'str' , None, None, 
                [(2, None), (6, None)], [], 
                '''                If mplsTunnelHopAddrType is set to lspid(5), then
                this value will contain the LSPID of a tunnel of
                this hop. The present tunnel being configured is
                tunneled through this hop (using label stacking).
                This object is otherwise insignificant and should
                contain a value of 0 to indicate this fact.
                ''',
                'mplstunnelhoplspid',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelHopPathOptionName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The description of this series of hops as they
                relate to the specified path option. The
                value of this object SHOULD be the same for
                each hop in the series that comprises a
                path option.
                ''',
                'mplstunnelhoppathoptionname',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelHopRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This variable is used to create, modify, and/or
                delete a row in this table.  When a row in this
                table is in active(1) state, no objects in that row
                can be modified by the agent except
                mplsTunnelHopRowStatus and
                mplsTunnelHopStorageType.
                ''',
                'mplstunnelhoprowstatus',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelHopStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this Hop entry. Conceptual
                rows having the value 'permanent' need not
                allow write-access to any columnar objects
                in the row.
                ''',
                'mplstunnelhopstoragetype',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelHopType', REFERENCE_ENUM_CLASS, 'MplstunnelhoptypeEnum' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry.MplstunnelhoptypeEnum', 
                [], [], 
                '''                Denotes whether this tunnel hop is routed in a
                strict or loose fashion. The value of this object
                has no meaning if the mplsTunnelHopInclude object
                is set to 'false'.
                ''',
                'mplstunnelhoptype',
                'MPLS-TE-STD-MIB', False),
            ],
            'MPLS-TE-STD-MIB',
            'mplsTunnelHopEntry',
            _yang_ns._namespaces['MPLS-TE-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB'
        ),
    },
    'MplsTeStdMib.Mplstunnelhoptable' : {
        'meta_info' : _MetaInfoClass('MplsTeStdMib.Mplstunnelhoptable',
            False, 
            [
            _MetaInfoClassMember('mplsTunnelHopEntry', REFERENCE_LIST, 'Mplstunnelhopentry' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry', 
                [], [], 
                '''                An entry in this table represents a tunnel hop.  An
                entry is created by a network administrator for
                signaled ERLSP set up by an MPLS signalling
                protocol.
                ''',
                'mplstunnelhopentry',
                'MPLS-TE-STD-MIB', False),
            ],
            'MPLS-TE-STD-MIB',
            'mplsTunnelHopTable',
            _yang_ns._namespaces['MPLS-TE-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB'
        ),
    },
    'MplsTeStdMib.Mplstunnelresourcetable.Mplstunnelresourceentry.MplstunnelresourcefrequencyEnum' : _MetaInfoEnum('MplstunnelresourcefrequencyEnum', 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB',
        {
            'unspecified':'unspecified',
            'frequent':'frequent',
            'veryFrequent':'veryFrequent',
        }, 'MPLS-TE-STD-MIB', _yang_ns._namespaces['MPLS-TE-STD-MIB']),
    'MplsTeStdMib.Mplstunnelresourcetable.Mplstunnelresourceentry' : {
        'meta_info' : _MetaInfoClass('MplsTeStdMib.Mplstunnelresourcetable.Mplstunnelresourceentry',
            False, 
            [
            _MetaInfoClassMember('mplsTunnelResourceIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                Uniquely identifies this row.
                ''',
                'mplstunnelresourceindex',
                'MPLS-TE-STD-MIB', True),
            _MetaInfoClassMember('mplsTunnelResourceExBurstSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Excess burst size in bytes.  The implementations
                which do not implement this variable must return
                noSuchObject exception for this object and must
                not allow a user to set this value.
                ''',
                'mplstunnelresourceexburstsize',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelResourceFrequency', REFERENCE_ENUM_CLASS, 'MplstunnelresourcefrequencyEnum' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunnelresourcetable.Mplstunnelresourceentry.MplstunnelresourcefrequencyEnum', 
                [], [], 
                '''                The granularity of the availability of committed
                rate.  The implementations which do not implement
                this variable must return unspecified(1) for this
                value and must not allow a user to set this value.
                ''',
                'mplstunnelresourcefrequency',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelResourceMaxBurstSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum burst size in bytes.
                ''',
                'mplstunnelresourcemaxburstsize',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelResourceMaxRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum rate in bits/second.  Note that setting
                mplsTunnelResourceMaxRate,
                mplsTunnelResourceMeanRate, and
                mplsTunnelResourceMaxBurstSize to 0 indicates best-
                effort treatment.
                ''',
                'mplstunnelresourcemaxrate',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelResourceMeanBurstSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The mean burst size in bytes.  The implementations
                which do not implement this variable must return
                a noSuchObject exception for this object and must
                not allow a user to set this object.
                ''',
                'mplstunnelresourcemeanburstsize',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelResourceMeanRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object is copied into an instance of
                mplsTrafficParamMeanRate in the
                mplsTrafficParamTable. The OID of this table entry
                is then copied into the corresponding
                mplsInSegmentTrafficParamPtr.
                ''',
                'mplstunnelresourcemeanrate',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelResourceRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This variable is used to create, modify, and/or
                delete a row in this table.  When a row in this
                table is in active(1) state, no objects in that row
                can be modified by the agent except
                mplsTunnelResourceRowStatus and
                mplsTunnelResourceStorageType.
                ''',
                'mplstunnelresourcerowstatus',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelResourceStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this Hop entry. Conceptual
                rows having the value 'permanent' need not
                allow write-access to any columnar objects
                in the row.
                ''',
                'mplstunnelresourcestoragetype',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelResourceWeight', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The relative weight for using excess bandwidth above
                its committed rate.  The value of 0 means that
                weight is not applicable for the CR-LSP.
                ''',
                'mplstunnelresourceweight',
                'MPLS-TE-STD-MIB', False),
            ],
            'MPLS-TE-STD-MIB',
            'mplsTunnelResourceEntry',
            _yang_ns._namespaces['MPLS-TE-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB'
        ),
    },
    'MplsTeStdMib.Mplstunnelresourcetable' : {
        'meta_info' : _MetaInfoClass('MplsTeStdMib.Mplstunnelresourcetable',
            False, 
            [
            _MetaInfoClassMember('mplsTunnelResourceEntry', REFERENCE_LIST, 'Mplstunnelresourceentry' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunnelresourcetable.Mplstunnelresourceentry', 
                [], [], 
                '''                An entry in this table represents a set of resources
                for an MPLS tunnel.  An entry can be created by a
                network administrator or by an SNMP agent as
                instructed by any MPLS signalling protocol.
                An entry in this table referenced by a tunnel instance
                with zero mplsTunnelInstance value indicates a
                configured set of resource parameter. An entry
                referenced by a tunnel instance with a non-zero
                mplsTunnelInstance reflects the in-use resource
                parameters for the tunnel instance which may have
                been negotiated or modified by the MPLS signaling
                protocols.
                ''',
                'mplstunnelresourceentry',
                'MPLS-TE-STD-MIB', False),
            ],
            'MPLS-TE-STD-MIB',
            'mplsTunnelResourceTable',
            _yang_ns._namespaces['MPLS-TE-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB'
        ),
    },
    'MplsTeStdMib.Mplstunnelarhoptable.Mplstunnelarhopentry' : {
        'meta_info' : _MetaInfoClass('MplsTeStdMib.Mplstunnelarhoptable.Mplstunnelarhopentry',
            False, 
            [
            _MetaInfoClassMember('mplsTunnelARHopListIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Primary index into this table identifying a
                particular recorded hop list.
                ''',
                'mplstunnelarhoplistindex',
                'MPLS-TE-STD-MIB', True),
            _MetaInfoClassMember('mplsTunnelARHopIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Secondary index into this table identifying the
                particular hop.
                ''',
                'mplstunnelarhopindex',
                'MPLS-TE-STD-MIB', True),
            _MetaInfoClassMember('mplsTunnelARHopAddrType', REFERENCE_ENUM_CLASS, 'TehopaddresstypeEnum' , 'ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'TehopaddresstypeEnum', 
                [], [], 
                '''                The Hop Address Type of this tunnel hop.
                
                Note that lspid(5) is a valid option only
                for tunnels signaled via CRLDP.
                ''',
                'mplstunnelarhopaddrtype',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelARHopAddrUnnum', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                If mplsTunnelARHopAddrType is set to unnum(4), then
                this value will contain the interface identifier of
                the unnumbered interface for this hop. This object
                should be used in conjunction with
                mplsTunnelARHopIpAddr which would contain the LSR
                Router ID in this case. Otherwise the agent should
                set this object to zero-length string and the
                manager should ignore this.
                ''',
                'mplstunnelarhopaddrunnum',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelARHopIpAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The Tunnel Hop Address for this tunnel hop.
                
                The type of this address is determined by the
                value of the corresponding mplsTunnelARHopAddrType.
                If mplsTunnelARHopAddrType is set to unnum(4),
                 then this value contains the LSR Router ID of the
                 unnumbered interface. Otherwise the agent SHOULD
                 set this object to the zero-length string and the
                 manager should ignore this object.
                ''',
                'mplstunnelarhopipaddr',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelARHopLspId', ATTRIBUTE, 'str' , None, None, 
                [(2, None), (6, None)], [], 
                '''                If mplsTunnelARHopAddrType is set to lspid(5), then
                this value will contain the LSP ID of this hop.
                This object is otherwise insignificant and should
                contain a value of 0 to indicate this fact.
                ''',
                'mplstunnelarhoplspid',
                'MPLS-TE-STD-MIB', False),
            ],
            'MPLS-TE-STD-MIB',
            'mplsTunnelARHopEntry',
            _yang_ns._namespaces['MPLS-TE-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB'
        ),
    },
    'MplsTeStdMib.Mplstunnelarhoptable' : {
        'meta_info' : _MetaInfoClass('MplsTeStdMib.Mplstunnelarhoptable',
            False, 
            [
            _MetaInfoClassMember('mplsTunnelARHopEntry', REFERENCE_LIST, 'Mplstunnelarhopentry' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunnelarhoptable.Mplstunnelarhopentry', 
                [], [], 
                '''                An entry in this table represents a tunnel hop.  An
                entry is created by the agent for signaled ERLSP
                set up by an MPLS signalling protocol.
                ''',
                'mplstunnelarhopentry',
                'MPLS-TE-STD-MIB', False),
            ],
            'MPLS-TE-STD-MIB',
            'mplsTunnelARHopTable',
            _yang_ns._namespaces['MPLS-TE-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB'
        ),
    },
    'MplsTeStdMib.Mplstunnelchoptable.Mplstunnelchopentry.MplstunnelchoptypeEnum' : _MetaInfoEnum('MplstunnelchoptypeEnum', 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB',
        {
            'strict':'strict',
            'loose':'loose',
        }, 'MPLS-TE-STD-MIB', _yang_ns._namespaces['MPLS-TE-STD-MIB']),
    'MplsTeStdMib.Mplstunnelchoptable.Mplstunnelchopentry' : {
        'meta_info' : _MetaInfoClass('MplsTeStdMib.Mplstunnelchoptable.Mplstunnelchopentry',
            False, 
            [
            _MetaInfoClassMember('mplsTunnelCHopListIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Primary index into this table identifying a
                particular computed hop list.
                ''',
                'mplstunnelchoplistindex',
                'MPLS-TE-STD-MIB', True),
            _MetaInfoClassMember('mplsTunnelCHopIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Secondary index into this table identifying the
                particular hop.
                ''',
                'mplstunnelchopindex',
                'MPLS-TE-STD-MIB', True),
            _MetaInfoClassMember('mplsTunnelCHopAddrType', REFERENCE_ENUM_CLASS, 'TehopaddresstypeEnum' , 'ydk.models.cisco_ios_xe.MPLS_TC_STD_MIB', 'TehopaddresstypeEnum', 
                [], [], 
                '''                The Hop Address Type of this tunnel hop.
                
                Note that lspid(5) is a valid option only
                for tunnels signaled via CRLDP.
                ''',
                'mplstunnelchopaddrtype',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelCHopAddrUnnum', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                If mplsTunnelCHopAddrType is set to unnum(4), then
                this value will contain the unnumbered interface
                identifier of this hop. This object should be used
                in conjunction with mplsTunnelCHopIpAddr which
                would contain the LSR Router ID in this case.
                Otherwise the agent should set this object to zero-
                length string and the manager should ignore this.
                ''',
                'mplstunnelchopaddrunnum',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelCHopAsNumber', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                If mplsTunnelCHopAddrType is set to asnumber(3),
                then this value will contain the AS number of this
                hop. Otherwise the agent should set this object to
                zero-length string and the manager should ignore
                this.
                ''',
                'mplstunnelchopasnumber',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelCHopIpAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                The Tunnel Hop Address for this tunnel hop.
                The type of this address is determined by the
                 value of the corresponding mplsTunnelCHopAddrType.
                
                If mplsTunnelCHopAddrType is set to unnum(4), then
                 this value will contain the LSR Router ID of the
                 unnumbered interface. Otherwise the agent should
                 set this object to the zero-length string and the
                 manager SHOULD ignore this object.
                ''',
                'mplstunnelchopipaddr',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelCHopIpPrefixLen', ATTRIBUTE, 'int' , None, None, 
                [('0', '2040')], [], 
                '''                If mplsTunnelCHopAddrType is set to ipv4(1) or
                ipv6(2), then this value will contain an
                appropriate prefix length for the IP address in
                object mplsTunnelCHopIpAddr. Otherwise this value
                is irrelevant and should be ignored.
                ''',
                'mplstunnelchopipprefixlen',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelCHopLspId', ATTRIBUTE, 'str' , None, None, 
                [(2, None), (6, None)], [], 
                '''                If mplsTunnelCHopAddrType is set to lspid(5), then
                this value will contain the LSP ID of this hop.
                This object is otherwise insignificant and should
                contain a value of 0 to indicate this fact.
                ''',
                'mplstunnelchoplspid',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelCHopType', REFERENCE_ENUM_CLASS, 'MplstunnelchoptypeEnum' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunnelchoptable.Mplstunnelchopentry.MplstunnelchoptypeEnum', 
                [], [], 
                '''                Denotes whether this is tunnel hop is routed in a
                strict or loose fashion.
                ''',
                'mplstunnelchoptype',
                'MPLS-TE-STD-MIB', False),
            ],
            'MPLS-TE-STD-MIB',
            'mplsTunnelCHopEntry',
            _yang_ns._namespaces['MPLS-TE-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB'
        ),
    },
    'MplsTeStdMib.Mplstunnelchoptable' : {
        'meta_info' : _MetaInfoClass('MplsTeStdMib.Mplstunnelchoptable',
            False, 
            [
            _MetaInfoClassMember('mplsTunnelCHopEntry', REFERENCE_LIST, 'Mplstunnelchopentry' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunnelchoptable.Mplstunnelchopentry', 
                [], [], 
                '''                An entry in this table represents a tunnel hop.  An
                entry in this table is created by a path
                computation engine using CSPF techniques applied to
                the information collected by routing protocols and
                the hops specified in the corresponding
                mplsTunnelHopTable.
                ''',
                'mplstunnelchopentry',
                'MPLS-TE-STD-MIB', False),
            ],
            'MPLS-TE-STD-MIB',
            'mplsTunnelCHopTable',
            _yang_ns._namespaces['MPLS-TE-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB'
        ),
    },
    'MplsTeStdMib.Mplstunnelcrldprestable.Mplstunnelcrldpresentry.MplstunnelcrldpresfrequencyEnum' : _MetaInfoEnum('MplstunnelcrldpresfrequencyEnum', 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB',
        {
            'unspecified':'unspecified',
            'frequent':'frequent',
            'veryFrequent':'veryFrequent',
        }, 'MPLS-TE-STD-MIB', _yang_ns._namespaces['MPLS-TE-STD-MIB']),
    'MplsTeStdMib.Mplstunnelcrldprestable.Mplstunnelcrldpresentry' : {
        'meta_info' : _MetaInfoClass('MplsTeStdMib.Mplstunnelcrldprestable.Mplstunnelcrldpresentry',
            False, 
            [
            _MetaInfoClassMember('mplsTunnelResourceIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'mplstunnelresourceindex',
                'MPLS-TE-STD-MIB', True),
            _MetaInfoClassMember('mplsTunnelCRLDPResExBurstSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Excess burst size in bytes.
                ''',
                'mplstunnelcrldpresexburstsize',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelCRLDPResFlags', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                The value of the 1 byte Flags conveyed as part of
                the traffic parameters during the establishment of
                the CRLSP. The bits in this object are to be
                interpreted as follows.
                
                +--+--+--+--+--+--+--+--+
                | Res |F6|F5|F4|F3|F2|F1|
                +--+--+--+--+--+--+--+--+
                
                Res - These bits are reserved. Zero on transmission.
                Ignored on receipt.
                F1 - Corresponds to the PDR.
                F2 - Corresponds to the PBS.
                F3 - Corresponds to the CDR.
                F4 - Corresponds to the CBS.
                F5 - Corresponds to the EBS.
                F6 - Corresponds to the Weight.
                
                Each flag if is a Negotiable Flag corresponding to a
                Traffic Parameter. The Negotiable Flag value zero
                denotes Not Negotiable and value one denotes
                Negotiable.
                ''',
                'mplstunnelcrldpresflags',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelCRLDPResFrequency', REFERENCE_ENUM_CLASS, 'MplstunnelcrldpresfrequencyEnum' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunnelcrldprestable.Mplstunnelcrldpresentry.MplstunnelcrldpresfrequencyEnum', 
                [], [], 
                '''                The granularity of the availability of committed
                rate.
                ''',
                'mplstunnelcrldpresfrequency',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelCRLDPResMeanBurstSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The mean burst size in bytes.
                ''',
                'mplstunnelcrldpresmeanburstsize',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelCRLDPResRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This variable is used to create, modify, and/or
                delete a row in this table.  When a row in this
                table is in active(1) state, no objects in that row
                can be modified by the agent except
                mplsTunnelCRLDPResRowStatus and
                mplsTunnelCRLDPResStorageType.
                ''',
                'mplstunnelcrldpresrowstatus',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelCRLDPResStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this CR-LDP Resource entry.
                Conceptual rows having the value 'permanent'
                need not allow write-access to any columnar
                objects in the row.
                ''',
                'mplstunnelcrldpresstoragetype',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelCRLDPResWeight', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The relative weight for using excess bandwidth above
                its committed rate.  The value of 0 means that
                weight is not applicable for the CR-LSP.
                ''',
                'mplstunnelcrldpresweight',
                'MPLS-TE-STD-MIB', False),
            ],
            'MPLS-TE-STD-MIB',
            'mplsTunnelCRLDPResEntry',
            _yang_ns._namespaces['MPLS-TE-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB'
        ),
    },
    'MplsTeStdMib.Mplstunnelcrldprestable' : {
        'meta_info' : _MetaInfoClass('MplsTeStdMib.Mplstunnelcrldprestable',
            False, 
            [
            _MetaInfoClassMember('mplsTunnelCRLDPResEntry', REFERENCE_LIST, 'Mplstunnelcrldpresentry' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunnelcrldprestable.Mplstunnelcrldpresentry', 
                [], [], 
                '''                An entry in this table represents a set of resources
                for an MPLS tunnel established using CRLDP
                (mplsTunnelSignallingProto equal to crldp (3)). An
                entry can be created by a network administrator or
                by an SNMP agent as instructed by any MPLS
                signalling protocol.
                ''',
                'mplstunnelcrldpresentry',
                'MPLS-TE-STD-MIB', False),
            ],
            'MPLS-TE-STD-MIB',
            'mplsTunnelCRLDPResTable',
            _yang_ns._namespaces['MPLS-TE-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB'
        ),
    },
    'MplsTeStdMib' : {
        'meta_info' : _MetaInfoClass('MplsTeStdMib',
            False, 
            [
            _MetaInfoClassMember('mplsTeObjects', REFERENCE_CLASS, 'Mplsteobjects' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplsteobjects', 
                [], [], 
                '''                ''',
                'mplsteobjects',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTeScalars', REFERENCE_CLASS, 'Mplstescalars' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstescalars', 
                [], [], 
                '''                ''',
                'mplstescalars',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelARHopTable', REFERENCE_CLASS, 'Mplstunnelarhoptable' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunnelarhoptable', 
                [], [], 
                '''                The mplsTunnelARHopTable is used to indicate the
                hops for an MPLS tunnel defined in mplsTunnelTable,
                as reported by the MPLS signalling protocol. Thus at
                a transit LSR, this table (if the table is supported
                and if the signaling protocol is recording actual
                route information) contains the actual route of the
                whole tunnel. If the signaling protocol is not
                recording the actual route, this table MAY report
                the information from the mplsTunnelHopTable or the
                mplsTunnelCHopTable.
                
                Each row in this table is indexed by
                mplsTunnelARHopListIndex. Each row also has a
                secondary index mplsTunnelARHopIndex, corresponding
                to the next hop that this row corresponds to.
                
                Please note that since the information necessary to
                build entries within this table is not provided by
                some MPLS signalling protocols, implementation of
                this table is optional. Furthermore, since the
                information in this table is actually provided by
                the MPLS signalling protocol after the path has
                been set-up, the entries in this table are provided
                only for observation, and hence, all variables in
                this table are accessible exclusively as read-
                only.
                
                Note also that the contents of this table may change
                while it is being read because of re-routing
                activities. A network administrator may verify that
                the actual route read is consistent by reference to
                the mplsTunnelLastPathChange object.
                ''',
                'mplstunnelarhoptable',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelCHopTable', REFERENCE_CLASS, 'Mplstunnelchoptable' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunnelchoptable', 
                [], [], 
                '''                The mplsTunnelCHopTable is used to indicate the
                hops, strict or loose, for an MPLS tunnel defined
                in mplsTunnelTable, as computed by a constraint-
                based routing protocol, based on the
                mplsTunnelHopTable for the outgoing direction of
                the tunnel. Thus at a transit LSR, this table (if
                the table is supported) MAY contain the path
                computed by the CSPF engine on (or on behalf of)
                this LSR. Each row in this table is indexed by
                mplsTunnelCHopListIndex.  Each row also has a
                secondary index mplsTunnelCHopIndex, corresponding
                to the next hop that this row corresponds to. In
                case we want to specify a particular interface on
                the originating LSR of an outgoing tunnel by which
                we want packets to exit the LSR, we specify this as
                the first hop for this tunnel in
                mplsTunnelCHopTable.
                
                Please note that since the information necessary to
                build entries within this table may not be
                supported by some LSRs, implementation of this
                table is optional. Furthermore, since the
                information in this table describes the path
                computed by the CSPF engine the entries in this
                table are read-only.
                ''',
                'mplstunnelchoptable',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelCRLDPResTable', REFERENCE_CLASS, 'Mplstunnelcrldprestable' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunnelcrldprestable', 
                [], [], 
                '''                The mplsTunnelCRLDPResTable allows a manager to
                specify which CR-LDP-specific resources are desired
                for an MPLS tunnel if that tunnel is signaled using
                CR-LDP. Note that these attributes are in addition
                to those specified in mplsTunnelResourceTable. This
                table also allows several tunnels to point to a
                single entry in this table, implying that these
                tunnels should share resources.
                ''',
                'mplstunnelcrldprestable',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelHopTable', REFERENCE_CLASS, 'Mplstunnelhoptable' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunnelhoptable', 
                [], [], 
                '''                The mplsTunnelHopTable is used to indicate the hops,
                strict or loose, for an instance of an MPLS tunnel
                defined in mplsTunnelTable, when it is established
                via signalling, for the outgoing direction of the
                tunnel. Thus at a transit LSR, this table contains
                the desired path of the tunnel from this LSR
                onwards. Each row in this table is indexed by
                mplsTunnelHopListIndex which corresponds to a group
                of hop lists or path options.  Each row also has a
                secondary index mplsTunnelHopIndex, which indicates
                a group of hops (also known as a path option).
                Finally, the third index, mplsTunnelHopIndex
                indicates the specific hop information for a path
                option. In case we want to specify a particular
                interface on the originating LSR of an outgoing
                tunnel by which we want packets to exit the LSR,
                we specify this as the first hop for this tunnel in
                mplsTunnelHopTable.
                ''',
                'mplstunnelhoptable',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelResourceTable', REFERENCE_CLASS, 'Mplstunnelresourcetable' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunnelresourcetable', 
                [], [], 
                '''                The mplsTunnelResourceTable allows a manager to
                specify which resources are desired for an MPLS
                tunnel.  This table also allows several tunnels to
                point to a single entry in this table, implying
                that these tunnels should share resources.
                ''',
                'mplstunnelresourcetable',
                'MPLS-TE-STD-MIB', False),
            _MetaInfoClassMember('mplsTunnelTable', REFERENCE_CLASS, 'Mplstunneltable' , 'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB', 'MplsTeStdMib.Mplstunneltable', 
                [], [], 
                '''                The mplsTunnelTable allows new MPLS tunnels to be
                created between an LSR and a remote endpoint, and
                existing tunnels to be reconfigured or removed.
                Note that only point-to-point tunnel segments are
                supported, although multipoint-to-point and point-
                to-multipoint connections are supported by an LSR
                acting as a cross-connect.  Each MPLS tunnel can
                thus have one out-segment originating at this LSR
                and/or one in-segment terminating at this LSR.
                ''',
                'mplstunneltable',
                'MPLS-TE-STD-MIB', False),
            ],
            'MPLS-TE-STD-MIB',
            'MPLS-TE-STD-MIB',
            _yang_ns._namespaces['MPLS-TE-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_TE_STD_MIB'
        ),
    },
}
_meta_table['MplsTeStdMib.Mplstunneltable.Mplstunnelentry']['meta_info'].parent =_meta_table['MplsTeStdMib.Mplstunneltable']['meta_info']
_meta_table['MplsTeStdMib.Mplstunnelhoptable.Mplstunnelhopentry']['meta_info'].parent =_meta_table['MplsTeStdMib.Mplstunnelhoptable']['meta_info']
_meta_table['MplsTeStdMib.Mplstunnelresourcetable.Mplstunnelresourceentry']['meta_info'].parent =_meta_table['MplsTeStdMib.Mplstunnelresourcetable']['meta_info']
_meta_table['MplsTeStdMib.Mplstunnelarhoptable.Mplstunnelarhopentry']['meta_info'].parent =_meta_table['MplsTeStdMib.Mplstunnelarhoptable']['meta_info']
_meta_table['MplsTeStdMib.Mplstunnelchoptable.Mplstunnelchopentry']['meta_info'].parent =_meta_table['MplsTeStdMib.Mplstunnelchoptable']['meta_info']
_meta_table['MplsTeStdMib.Mplstunnelcrldprestable.Mplstunnelcrldpresentry']['meta_info'].parent =_meta_table['MplsTeStdMib.Mplstunnelcrldprestable']['meta_info']
_meta_table['MplsTeStdMib.Mplstescalars']['meta_info'].parent =_meta_table['MplsTeStdMib']['meta_info']
_meta_table['MplsTeStdMib.Mplsteobjects']['meta_info'].parent =_meta_table['MplsTeStdMib']['meta_info']
_meta_table['MplsTeStdMib.Mplstunneltable']['meta_info'].parent =_meta_table['MplsTeStdMib']['meta_info']
_meta_table['MplsTeStdMib.Mplstunnelhoptable']['meta_info'].parent =_meta_table['MplsTeStdMib']['meta_info']
_meta_table['MplsTeStdMib.Mplstunnelresourcetable']['meta_info'].parent =_meta_table['MplsTeStdMib']['meta_info']
_meta_table['MplsTeStdMib.Mplstunnelarhoptable']['meta_info'].parent =_meta_table['MplsTeStdMib']['meta_info']
_meta_table['MplsTeStdMib.Mplstunnelchoptable']['meta_info'].parent =_meta_table['MplsTeStdMib']['meta_info']
_meta_table['MplsTeStdMib.Mplstunnelcrldprestable']['meta_info'].parent =_meta_table['MplsTeStdMib']['meta_info']
