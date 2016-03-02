


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'MPLSLSRSTDMIB.MplsInSegmentMapTable.MplsInSegmentMapEntry' : {
        'meta_info' : _MetaInfoClass('MPLSLSRSTDMIB.MplsInSegmentMapTable.MplsInSegmentMapEntry',
            False, 
            [
            _MetaInfoClassMember('mplsInSegmentMapInterface', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                This index contains the same value as the
                mplsInSegmentIndex in the mplsInSegmentTable.
                ''',
                'mplsinsegmentmapinterface',
                'MPLS-LSR-STD-MIB', True),
            _MetaInfoClassMember('mplsInSegmentMapLabel', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This index contains the same value as the
                mplsInSegmentLabel in the mplsInSegmentTable.
                ''',
                'mplsinsegmentmaplabel',
                'MPLS-LSR-STD-MIB', True),
            _MetaInfoClassMember('mplsInSegmentMapLabelPtrIndex', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This index contains the same value as the
                mplsInSegmentLabelPtr.
                
                If the label for the InSegment cannot be represented
                fully within the mplsInSegmentLabel object,
                this index MUST point to the first accessible
                column of a conceptual row in an external table containing
                the label.  In this case, the mplsInSegmentTopLabel
                object SHOULD be set to 0 and ignored. This object MUST
                be set to zeroDotZero otherwise.
                ''',
                'mplsinsegmentmaplabelptrindex',
                'MPLS-LSR-STD-MIB', True),
            _MetaInfoClassMember('mplsInSegmentMapIndex', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                The mplsInSegmentIndex that corresponds
                to the mplsInSegmentInterface and
                mplsInSegmentLabel, or the mplsInSegmentInterface
                and mplsInSegmentLabelPtr, if applicable.
                The string containing the single octet 0x00
                MUST not be returned.
                ''',
                'mplsinsegmentmapindex',
                'MPLS-LSR-STD-MIB', False),
            ],
            'MPLS-LSR-STD-MIB',
            'mplsInSegmentMapEntry',
            _yang_ns._namespaces['MPLS-LSR-STD-MIB'],
        'ydk.models.mpls.MPLS_LSR_STD_MIB'
        ),
    },
    'MPLSLSRSTDMIB.MplsInSegmentMapTable' : {
        'meta_info' : _MetaInfoClass('MPLSLSRSTDMIB.MplsInSegmentMapTable',
            False, 
            [
            _MetaInfoClassMember('mplsInSegmentMapEntry', REFERENCE_LIST, 'MplsInSegmentMapEntry' , 'ydk.models.mpls.MPLS_LSR_STD_MIB', 'MPLSLSRSTDMIB.MplsInSegmentMapTable.MplsInSegmentMapEntry', 
                [], [], 
                '''                An entry in this table represents one interface
                and incoming label pair.
                
                In cases where the label cannot fit into the
                mplsInSegmentLabel object, the mplsInSegmentLabelPtr
                will indicate this by being set to the first accessible
                column in the appropriate extension table's row,
                and the mplsInSegmentLabel SHOULD be set to 0.
                In all other cases when the label is
                represented within the mplsInSegmentLabel object, the
                mplsInSegmentLabelPtr MUST be 0.0.
                
                Implementors need to be aware that if the value of
                the mplsInSegmentMapLabelPtrIndex (an OID) has more
                that 111 sub-identifiers, then OIDs of column
                instances in this table will have more than 128
                sub-identifiers and cannot be accessed using SNMPv1,
                SNMPv2c, or SNMPv3.
                ''',
                'mplsinsegmentmapentry',
                'MPLS-LSR-STD-MIB', False),
            ],
            'MPLS-LSR-STD-MIB',
            'mplsInSegmentMapTable',
            _yang_ns._namespaces['MPLS-LSR-STD-MIB'],
        'ydk.models.mpls.MPLS_LSR_STD_MIB'
        ),
    },
    'MPLSLSRSTDMIB.MplsInSegmentTable.MplsInSegmentEntry' : {
        'meta_info' : _MetaInfoClass('MPLSLSRSTDMIB.MplsInSegmentTable.MplsInSegmentEntry',
            False, 
            [
            _MetaInfoClassMember('mplsInSegmentIndex', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                The index for this in-segment. The
                string containing the single octet 0x00
                MUST not be used as an index.
                ''',
                'mplsinsegmentindex',
                'MPLS-LSR-STD-MIB', True),
            _MetaInfoClassMember('mplsInSegmentAddrFamily', REFERENCE_ENUM_CLASS, 'AddressFamilyNumbers_Enum' , 'ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressFamilyNumbers_Enum', 
                [], [], 
                '''                The IANA address family [IANAFamily] of packets
                received on this segment, which is used at an egress
                LSR to deliver them to the appropriate layer 3 entity.
                A value of other(0) indicates that the family type is
                either unknown or undefined; this SHOULD NOT be used
                at an egress LSR. This object cannot be
                modified if mplsInSegmentRowStatus is active(1).
                ''',
                'mplsinsegmentaddrfamily',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInSegmentInterface', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                This object represents the
                interface index for the incoming MPLS interface.  A
                value of zero represents all interfaces participating in
                the per-platform label space.  This may only be used
                in cases where the incoming interface and label
                are associated with the same mplsXCEntry. Specifically,
                given a label and any incoming interface pair from the
                per-platform label space, the outgoing label/interface
                mapping remains the same. If this is not the case,
                then individual entries MUST exist that
                can then be mapped to unique mplsXCEntries.
                ''',
                'mplsinsegmentinterface',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInSegmentLabel', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                If the corresponding instance of mplsInSegmentLabelPtr is
                zeroDotZero then this object MUST contain the incoming label
                associated with this in-segment. If not this object SHOULD
                be zero and MUST be ignored.
                ''',
                'mplsinsegmentlabel',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInSegmentLabelPtr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                If the label for this segment cannot be represented
                fully within the mplsInSegmentLabel object,
                this object MUST point to the first accessible
                column of a conceptual row in an external table containing
                the label.  In this case, the mplsInSegmentTopLabel
                object SHOULD be set to 0 and ignored. This object MUST
                be set to zeroDotZero otherwise.
                ''',
                'mplsinsegmentlabelptr',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInSegmentNPop', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The number of labels to pop from the incoming
                packet.  Normally only the top label is popped from
                the packet and used for all switching decisions for
                that packet.  This is indicated by setting this
                object to the default value of 1. If an LSR supports
                popping of more than one label, this object MUST
                be set to that number. This object cannot be modified
                if mplsInSegmentRowStatus is active(1).
                ''',
                'mplsinsegmentnpop',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInSegmentOwner', REFERENCE_ENUM_CLASS, 'MplsOwner_Enum' , 'ydk.models.mpls.MPLS_TC_STD_MIB', 'MplsOwner_Enum', 
                [], [], 
                '''                Denotes the entity that created and is responsible
                for managing this segment.
                ''',
                'mplsinsegmentowner',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInSegmentPerfDiscards', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of labeled packets received on this in-
                segment, which were chosen to be discarded even
                though no errors had been detected to prevent their
                being transmitted.  One possible reason for
                discarding such a labeled packet could be to free up
                buffer space.
                ''',
                'mplsinsegmentperfdiscards',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInSegmentPerfDiscontinuityTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime on the most recent occasion
                at which any one or more of this segment's Counter32
                or Counter64 suffered a discontinuity. If no such
                discontinuities have occurred since the last re-
                initialization of the local management subsystem,
                then this object contains a zero value.
                ''',
                'mplsinsegmentperfdiscontinuitytime',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInSegmentPerfErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of errored packets received on this
                segment.
                ''',
                'mplsinsegmentperferrors',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInSegmentPerfHCOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The total number of octets received.  This is the 64
                bit version of mplsInSegmentPerfOctets,
                if mplsInSegmentPerfHCOctets is supported according to
                the rules spelled out in RFC2863.
                ''',
                'mplsinsegmentperfhcoctets',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInSegmentPerfOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This value represents the total number of octets
                received by this segment. It MUST be equal to the
                least significant 32 bits of
                mplsInSegmentPerfHCOctets
                if mplsInSegmentPerfHCOctets is supported according to
                the rules spelled out in RFC2863.
                ''',
                'mplsinsegmentperfoctets',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInSegmentPerfPackets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of packets received by this segment.
                ''',
                'mplsinsegmentperfpackets',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInSegmentRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This variable is used to create, modify, and/or
                delete a row in this table. When a row in this
                table has a row in the active(1) state, no
                objects in this row can be modified except the
                mplsInSegmentRowStatus and mplsInSegmentStorageType.
                ''',
                'mplsinsegmentrowstatus',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInSegmentStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This variable indicates the storage type for this
                object. The agent MUST ensure that this object's
                value remains consistent with the associated
                mplsXCEntry. Conceptual rows having the value
                'permanent' need not allow write-access to any
                columnar objects in the row.
                ''',
                'mplsinsegmentstoragetype',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInSegmentTrafficParamPtr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This variable represents a pointer to the traffic
                parameter specification for this in-segment.  This
                value may point at an entry in the
                mplsTunnelResourceTable in the MPLS-TE-STD-MIB (RFC3812)
                to indicate which traffic parameter settings for this
                segment if it represents an LSP used for a TE tunnel.
                
                This value may optionally point at an
                externally defined traffic parameter specification
                table.  A value of zeroDotZero indicates best-effort
                treatment.  By having the same value of this object,
                two or more segments can indicate resource sharing
                of such things as LSP queue space, etc.
                
                This object cannot be modified if mplsInSegmentRowStatus
                is active(1).  For entries in this table that
                are preserved after a re-boot, the agent MUST ensure
                that their integrity be preserved, or this object should
                be set to 0.0 if it cannot.
                ''',
                'mplsinsegmenttrafficparamptr',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInSegmentXCIndex', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                Index into mplsXCTable which identifies which cross-
                connect entry this segment is part of.  The string
                containing the single octet 0x00 indicates that this
                entry is not referred to by any cross-connect entry.
                When a cross-connect entry is created which this
                in-segment is a part of, this object is automatically
                updated to reflect the value of mplsXCIndex of that
                cross-connect entry.
                ''',
                'mplsinsegmentxcindex',
                'MPLS-LSR-STD-MIB', False),
            ],
            'MPLS-LSR-STD-MIB',
            'mplsInSegmentEntry',
            _yang_ns._namespaces['MPLS-LSR-STD-MIB'],
        'ydk.models.mpls.MPLS_LSR_STD_MIB'
        ),
    },
    'MPLSLSRSTDMIB.MplsInSegmentTable' : {
        'meta_info' : _MetaInfoClass('MPLSLSRSTDMIB.MplsInSegmentTable',
            False, 
            [
            _MetaInfoClassMember('mplsInSegmentEntry', REFERENCE_LIST, 'MplsInSegmentEntry' , 'ydk.models.mpls.MPLS_LSR_STD_MIB', 'MPLSLSRSTDMIB.MplsInSegmentTable.MplsInSegmentEntry', 
                [], [], 
                '''                An entry in this table represents one incoming
                segment as is represented in an LSR's LFIB.
                An entry can be created by a network
                administrator or an SNMP agent, or an MPLS signaling
                protocol.  The creator of the entry is denoted by
                mplsInSegmentOwner.
                The value of mplsInSegmentRowStatus cannot be active(1)
                unless the ifTable entry corresponding to
                mplsInSegmentInterface exists.  An entry in this table
                must match any incoming packets, and indicates an
                instance of mplsXCEntry based on which forwarding
                and/or switching actions are taken.
                ''',
                'mplsinsegmententry',
                'MPLS-LSR-STD-MIB', False),
            ],
            'MPLS-LSR-STD-MIB',
            'mplsInSegmentTable',
            _yang_ns._namespaces['MPLS-LSR-STD-MIB'],
        'ydk.models.mpls.MPLS_LSR_STD_MIB'
        ),
    },
    'MPLSLSRSTDMIB.MplsInterfaceTable.MplsInterfaceEntry' : {
        'meta_info' : _MetaInfoClass('MPLSLSRSTDMIB.MplsInterfaceTable.MplsInterfaceEntry',
            False, 
            [
            _MetaInfoClassMember('mplsInterfaceIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                This is a unique index for an entry in the
                MplsInterfaceTable.  A non-zero index for an
                entry indicates the ifIndex for the corresponding
                interface entry of the MPLS-layer in the ifTable.
                The entry with index 0 represents the per-platform
                label space and contains parameters that apply to all
                interfaces that participate in the per-platform label
                space. Other entries defined in this table represent
                additional MPLS interfaces that may participate in either
                the per-platform or per-interface label spaces, or both.
                ''',
                'mplsinterfaceindex',
                'MPLS-LSR-STD-MIB', True),
            _MetaInfoClassMember('mplsInterfaceAvailableBandwidth', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This value indicates the total amount of available
                bandwidth available on this interface and is
                specified in kilobits per second (Kbps).  This value
                is calculated as the difference between the amount
                of bandwidth currently in use and that specified in
                mplsInterfaceTotalBandwidth.  This variable is not
                applicable when applied to the interface with index
                0. When this value cannot be measured, this value
                should contain the nominal bandwidth.
                ''',
                'mplsinterfaceavailablebandwidth',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInterfaceLabelMaxIn', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This is the maximum value of an MPLS label that this
                LSR is willing to receive on this interface.
                ''',
                'mplsinterfacelabelmaxin',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInterfaceLabelMaxOut', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This is the maximum value of an MPLS label that this
                LSR is willing to send on this interface.
                ''',
                'mplsinterfacelabelmaxout',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInterfaceLabelMinIn', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This is the minimum value of an MPLS label that this
                LSR is willing to receive on this interface.
                ''',
                'mplsinterfacelabelminin',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInterfaceLabelMinOut', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This is the minimum value of an MPLS label that this
                LSR is willing to send on this interface.
                ''',
                'mplsinterfacelabelminout',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInterfaceLabelParticipationType', REFERENCE_BITS, 'MplsInterfaceLabelParticipationType_Bits' , 'ydk.models.mpls.MPLS_LSR_STD_MIB', 'MPLSLSRSTDMIB.MplsInterfaceTable.MplsInterfaceEntry.MplsInterfaceLabelParticipationType_Bits', 
                [], [], 
                '''                If the value of the mplsInterfaceIndex for this
                entry is zero, then this entry corresponds to the
                per-platform label space for all interfaces configured
                to use that label space. In this case the perPlatform(0)
                bit MUST be set; the perInterface(1) bit is meaningless
                and MUST be ignored.
                
                The remainder of this description applies to entries
                with a non-zero value of mplsInterfaceIndex.
                
                If the perInterface(1) bit is set then the value of
                mplsInterfaceLabelMinIn, mplsInterfaceLabelMaxIn,
                mplsInterfaceLabelMinOut, and
                mplsInterfaceLabelMaxOut for this entry reflect the
                label ranges for this interface.
                
                If only the perPlatform(0) bit is set, then the value of
                mplsInterfaceLabelMinIn, mplsInterfaceLabelMaxIn,
                mplsInterfaceLabelMinOut, and
                mplsInterfaceLabelMaxOut for this entry MUST be
                identical to the instance of these objects with
                index 0.  These objects may only vary from the entry
                with index 0 if both the perPlatform(0) and perInterface(1)
                bits are set.
                
                In all cases, at a minimum one of the perPlatform(0) or
                perInterface(1) bits MUST be set to indicate that
                at least one label space is in use by this interface. In
                all cases, agents MUST ensure that label ranges are
                specified consistently and MUST return an
                inconsistentValue error when they do not.
                ''',
                'mplsinterfacelabelparticipationtype',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInterfacePerfInLabelLookupFailures', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object counts the number of labeled packets
                that have been received on this interface and which
                were discarded because there was no matching cross-
                connect entry. This object MUST count on a per-
                interface basis regardless of which label space the
                interface participates in.
                ''',
                'mplsinterfaceperfinlabellookupfailures',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInterfacePerfInLabelsInUse', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object counts the number of labels that are in
                use at this point in time on this interface in the
                incoming direction. If the interface participates in
                only the per-platform label space, then the value of
                the instance of this object MUST be identical to
                the value of the instance with index 0. If the
                interface participates in the per-interface label
                space, then the instance of this object MUST
                represent the number of per-interface labels that
                are in use on this interface.
                ''',
                'mplsinterfaceperfinlabelsinuse',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInterfacePerfOutFragmentedPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object counts the number of outgoing MPLS
                packets that required fragmentation before
                transmission on this interface. This object MUST
                count on a per-interface basis regardless of which
                label space the interface participates in.
                ''',
                'mplsinterfaceperfoutfragmentedpkts',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInterfacePerfOutLabelsInUse', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object counts the number of top-most labels in
                the outgoing label stacks that are in use at this
                point in time on this interface. This object MUST
                count on a per-interface basis regardless of which
                label space the interface participates in.
                ''',
                'mplsinterfaceperfoutlabelsinuse',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInterfaceTotalBandwidth', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This value indicates the total amount of usable
                bandwidth on this interface and is specified in
                kilobits per second (Kbps).  This variable is not
                applicable when applied to the interface with index
                0. When this value cannot be measured, this value
                should contain the nominal bandwidth.
                ''',
                'mplsinterfacetotalbandwidth',
                'MPLS-LSR-STD-MIB', False),
            ],
            'MPLS-LSR-STD-MIB',
            'mplsInterfaceEntry',
            _yang_ns._namespaces['MPLS-LSR-STD-MIB'],
        'ydk.models.mpls.MPLS_LSR_STD_MIB'
        ),
    },
    'MPLSLSRSTDMIB.MplsInterfaceTable' : {
        'meta_info' : _MetaInfoClass('MPLSLSRSTDMIB.MplsInterfaceTable',
            False, 
            [
            _MetaInfoClassMember('mplsInterfaceEntry', REFERENCE_LIST, 'MplsInterfaceEntry' , 'ydk.models.mpls.MPLS_LSR_STD_MIB', 'MPLSLSRSTDMIB.MplsInterfaceTable.MplsInterfaceEntry', 
                [], [], 
                '''                A conceptual row in this table is created
                automatically by an LSR for every interface capable
                of supporting MPLS and which is configured to do so.
                A conceptual row in this table will exist if and only if
                a corresponding entry in ifTable exists with ifType =
                mpls(166). If this associated entry in ifTable is
                operationally disabled (thus removing MPLS
                capabilities on that interface), the corresponding
                entry in this table MUST be deleted shortly thereafter.
                An conceptual row with index 0 is created if the LSR
                supports per-platform labels. This conceptual row
                represents the per-platform label space and contains
                parameters that apply to all interfaces that participate
                in the per-platform label space. Other conceptual rows
                in this table represent MPLS interfaces that may
                participate in either the per-platform or per-
                interface label spaces, or both.  Implementations
                that either only support per-platform labels,
                or have only them configured, may choose to return
                just the mplsInterfaceEntry of 0 and not return
                the other rows. This will greatly reduce the number
                of objects returned. Further information about label
                space participation of an interface is provided in
                the DESCRIPTION clause of
                mplsInterfaceLabelParticipationType.
                ''',
                'mplsinterfaceentry',
                'MPLS-LSR-STD-MIB', False),
            ],
            'MPLS-LSR-STD-MIB',
            'mplsInterfaceTable',
            _yang_ns._namespaces['MPLS-LSR-STD-MIB'],
        'ydk.models.mpls.MPLS_LSR_STD_MIB'
        ),
    },
    'MPLSLSRSTDMIB.MplsLabelStackTable.MplsLabelStackEntry' : {
        'meta_info' : _MetaInfoClass('MPLSLSRSTDMIB.MplsLabelStackTable.MplsLabelStackEntry',
            False, 
            [
            _MetaInfoClassMember('mplsLabelStackIndex', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                Primary index for this row identifying a stack of
                labels to be pushed on an outgoing packet, beneath
                the top label. An index containing the string with
                a single octet 0x00 MUST not be used.
                ''',
                'mplslabelstackindex',
                'MPLS-LSR-STD-MIB', True),
            _MetaInfoClassMember('mplsLabelStackLabelIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                Secondary index for this row identifying one label
                of the stack.  Note that an entry with a smaller
                mplsLabelStackLabelIndex would refer to a label
                higher up the label stack and would be popped at a
                downstream LSR before a label represented by a
                higher mplsLabelStackLabelIndex at a downstream
                LSR.
                ''',
                'mplslabelstacklabelindex',
                'MPLS-LSR-STD-MIB', True),
            _MetaInfoClassMember('mplsLabelStackLabel', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The label to pushed.
                ''',
                'mplslabelstacklabel',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsLabelStackLabelPtr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                If the label for this segment cannot be represented
                fully within the mplsLabelStackLabel object,
                this object MUST point to the first accessible
                column of a conceptual row in an external table containing
                the label.  In this case, the mplsLabelStackLabel
                object SHOULD be set to 0 and ignored. This object
                MUST be set to zeroDotZero otherwise.
                ''',
                'mplslabelstacklabelptr',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsLabelStackRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                For creating, modifying, and deleting this row.
                When a row in this table has a row in the active(1)
                state, no objects in this row except this object
                and the mplsLabelStackStorageType can be modified.
                ''',
                'mplslabelstackrowstatus',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsLabelStackStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This variable indicates the storage type for this
                object. This object cannot be modified if
                mplsLabelStackRowStatus is active(1).
                No objects are required to be writable for
                rows in this table with this object set to
                permanent(4).
                
                The agent MUST ensure that all related entries
                in this table retain the same value for this
                object.  Agents MUST ensure that the storage type
                for all entries related to a particular mplsXCEntry
                retain the same value for this object as the
                mplsXCEntry's StorageType.
                ''',
                'mplslabelstackstoragetype',
                'MPLS-LSR-STD-MIB', False),
            ],
            'MPLS-LSR-STD-MIB',
            'mplsLabelStackEntry',
            _yang_ns._namespaces['MPLS-LSR-STD-MIB'],
        'ydk.models.mpls.MPLS_LSR_STD_MIB'
        ),
    },
    'MPLSLSRSTDMIB.MplsLabelStackTable' : {
        'meta_info' : _MetaInfoClass('MPLSLSRSTDMIB.MplsLabelStackTable',
            False, 
            [
            _MetaInfoClassMember('mplsLabelStackEntry', REFERENCE_LIST, 'MplsLabelStackEntry' , 'ydk.models.mpls.MPLS_LSR_STD_MIB', 'MPLSLSRSTDMIB.MplsLabelStackTable.MplsLabelStackEntry', 
                [], [], 
                '''                An entry in this table represents one label which is
                to be pushed onto an outgoing packet, beneath the
                top label.  An entry can be created by a network
                administrator or by an SNMP agent as instructed by
                an MPLS signaling protocol.
                ''',
                'mplslabelstackentry',
                'MPLS-LSR-STD-MIB', False),
            ],
            'MPLS-LSR-STD-MIB',
            'mplsLabelStackTable',
            _yang_ns._namespaces['MPLS-LSR-STD-MIB'],
        'ydk.models.mpls.MPLS_LSR_STD_MIB'
        ),
    },
    'MPLSLSRSTDMIB.MplsLsrObjects' : {
        'meta_info' : _MetaInfoClass('MPLSLSRSTDMIB.MplsLsrObjects',
            False, 
            [
            _MetaInfoClassMember('mplsInSegmentIndexNext', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                This object contains the next available value to
                be used for mplsInSegmentIndex when creating entries
                in the mplsInSegmentTable. The special value of a
                string containing the single octet 0x00 indicates
                that no new entries can be created in this table.
                Agents not allowing managers to create entries
                in this table MUST set this object to this special
                value.
                ''',
                'mplsinsegmentindexnext',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsLabelStackIndexNext', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                This object contains the next available value to
                be used for mplsLabelStackIndex when creating entries
                in the mplsLabelStackTable. The special string
                containing the single octet 0x00
                indicates that no more new entries can be created
                in the relevant table.  Agents not allowing managers
                to create entries in this table MUST set this value
                to the string containing the single octet 0x00.
                ''',
                'mplslabelstackindexnext',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsMaxLabelStackDepth', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The maximum stack depth supported by this LSR.
                ''',
                'mplsmaxlabelstackdepth',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentIndexNext', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                This object contains the next available value to
                be used for mplsOutSegmentIndex when creating entries
                in the mplsOutSegmentTable. The special value of a
                string containing the single octet 0x00
                indicates that no new entries can be created in this
                table. Agents not allowing managers to create entries
                in this table MUST set this object to this special
                value.
                ''',
                'mplsoutsegmentindexnext',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsXCIndexNext', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                This object contains the next available value to
                be used for mplsXCIndex when creating entries in
                the mplsXCTable. A special value of the zero length
                string indicates that no more new entries can be created
                in the relevant table.  Agents not allowing managers
                to create entries in this table MUST set this value
                to the zero length string.
                ''',
                'mplsxcindexnext',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsXCNotificationsEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this object is set to true(1), then it enables
                the emission of mplsXCUp and mplsXCDown
                notifications; otherwise these notifications are not
                emitted.
                ''',
                'mplsxcnotificationsenable',
                'MPLS-LSR-STD-MIB', False),
            ],
            'MPLS-LSR-STD-MIB',
            'mplsLsrObjects',
            _yang_ns._namespaces['MPLS-LSR-STD-MIB'],
        'ydk.models.mpls.MPLS_LSR_STD_MIB'
        ),
    },
    'MPLSLSRSTDMIB.MplsOutSegmentTable.MplsOutSegmentEntry' : {
        'meta_info' : _MetaInfoClass('MPLSLSRSTDMIB.MplsOutSegmentTable.MplsOutSegmentEntry',
            False, 
            [
            _MetaInfoClassMember('mplsOutSegmentIndex', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                This value contains a unique index for this row.
                While a value of a string containing the single
                octet 0x00 is not valid as an index for entries
                in this table, it can be supplied as a valid value
                to index the mplsXCTable to represent entries for
                which no out-segment has been configured or
                exists.
                ''',
                'mplsoutsegmentindex',
                'MPLS-LSR-STD-MIB', True),
            _MetaInfoClassMember('mplsOutSegmentInterface', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                This value must contain the interface index of the
                outgoing interface. This object cannot be modified
                if mplsOutSegmentRowStatus is active(1). The
                mplsOutSegmentRowStatus cannot be set to active(1)
                until this object is set to a value corresponding to
                a valid ifEntry.
                ''',
                'mplsoutsegmentinterface',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentNextHopAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The internet address of the next hop. The type of
                this address is determined by the value of the
                mplslOutSegmentNextHopAddrType object.
                
                This object cannot be modified if
                mplsOutSegmentRowStatus is active(1).
                ''',
                'mplsoutsegmentnexthopaddr',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentNextHopAddrType', REFERENCE_ENUM_CLASS, 'InetAddressType_Enum' , 'ydk.models.inet.INET_ADDRESS_MIB', 'InetAddressType_Enum', 
                [], [], 
                '''                Indicates the next hop Internet address type.
                Only values unknown(0), ipv4(1) or ipv6(2)
                have to be supported.
                
                A value of unknown(0) is allowed only when
                the outgoing interface is of type point-to-point.
                If any other unsupported values are attempted in a set
                operation, the agent MUST return an inconsistentValue
                error.
                ''',
                'mplsoutsegmentnexthopaddrtype',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentOwner', REFERENCE_ENUM_CLASS, 'MplsOwner_Enum' , 'ydk.models.mpls.MPLS_TC_STD_MIB', 'MplsOwner_Enum', 
                [], [], 
                '''                Denotes the entity which created and is responsible
                for managing this segment.
                ''',
                'mplsoutsegmentowner',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentPerfDiscards', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of labeled packets attempted to be transmitted
                on this out-segment, which were chosen to be discarded
                even though no errors had been detected to prevent their
                being transmitted. One possible reason for
                discarding such a labeled packet could be to free up
                buffer space.
                ''',
                'mplsoutsegmentperfdiscards',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentPerfDiscontinuityTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime on the most recent occasion
                at which any one or more of this segment's Counter32
                or Counter64 suffered a discontinuity. If no such
                discontinuities have occurred since the last re-
                initialization of the local management subsystem,
                then this object contains a zero value.
                ''',
                'mplsoutsegmentperfdiscontinuitytime',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentPerfErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of packets that could not be sent due to
                errors on this segment.
                ''',
                'mplsoutsegmentperferrors',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentPerfHCOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Total number of octets sent.  This is the 64 bit
                version of mplsOutSegmentPerfOctets,
                if mplsOutSegmentPerfHCOctets is supported according to
                the rules spelled out in RFC2863.
                ''',
                'mplsoutsegmentperfhcoctets',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentPerfOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This value contains the total number of octets sent
                on this segment. It MUST be equal to the least
                significant 32 bits of mplsOutSegmentPerfHCOctets
                if mplsOutSegmentPerfHCOctets is supported according to
                the rules spelled out in RFC2863.
                ''',
                'mplsoutsegmentperfoctets',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentPerfPackets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This value contains the total number of packets sent
                on this segment.
                ''',
                'mplsoutsegmentperfpackets',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentPushTopLabel', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This value indicates whether or not a top label
                should be pushed onto the outgoing packet's label
                stack.  The value of this variable MUST be set to
                true(1) if the outgoing interface does not support
                pop-and-go (and no label stack remains). For example,
                on ATM interface, or if the segment represents a
                tunnel origination.  Note that it is considered
                an error in the case that mplsOutSegmentPushTopLabel
                is set to false, but the cross-connect entry which
                refers to this out-segment has a non-zero
                mplsLabelStackIndex.  The LSR MUST ensure that this
                situation does not happen. This object cannot be
                modified if mplsOutSegmentRowStatus is active(1).
                ''',
                'mplsoutsegmentpushtoplabel',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                For creating, modifying, and deleting this row.
                When a row in this table has a row in the active(1)
                state, no objects in this row can be modified
                except the mplsOutSegmentRowStatus or
                mplsOutSegmentStorageType.
                ''',
                'mplsoutsegmentrowstatus',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This variable indicates the storage type for this
                object. The agent MUST ensure that this object's value
                remains consistent with the associated mplsXCEntry.
                Conceptual rows having the value 'permanent'
                need not allow write-access to any columnar
                objects in the row.
                ''',
                'mplsoutsegmentstoragetype',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentTopLabel', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                If mplsOutSegmentPushTopLabel is true then this
                represents the label that should be pushed onto the
                top of the outgoing packet's label stack. Otherwise
                this value SHOULD be set to 0 by the management
                station and MUST be ignored by the agent. This
                object cannot be modified if mplsOutSegmentRowStatus
                is active(1).
                ''',
                'mplsoutsegmenttoplabel',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentTopLabelPtr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                If the label for this segment cannot be represented
                fully within the mplsOutSegmentLabel object,
                this object MUST point to the first accessible
                column of a conceptual row in an external table containing
                the label.  In this case, the mplsOutSegmentTopLabel
                object SHOULD be set to 0 and ignored. This object
                MUST be set to zeroDotZero otherwise.
                ''',
                'mplsoutsegmenttoplabelptr',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentTrafficParamPtr', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This variable represents a pointer to the traffic
                parameter specification for this out-segment.  This
                value may point at an entry in the
                MplsTunnelResourceEntry in the MPLS-TE-STD-MIB (RFC3812)
                
                RFC Editor: Please fill in RFC number.
                
                to indicate which traffic parameter settings for this
                segment if it represents an LSP used for a TE tunnel.
                
                This value may optionally point at an
                externally defined traffic parameter specification
                table.  A value of zeroDotZero indicates best-effort
                treatment.  By having the same value of this object,
                two or more segments can indicate resource sharing
                of such things as LSP queue space, etc.
                
                This object cannot be modified if
                mplsOutSegmentRowStatus is active(1).
                For entries in this table that
                are preserved after a re-boot, the agent MUST ensure
                that their integrity be preserved, or this object should
                be set to 0.0 if it cannot.
                ''',
                'mplsoutsegmenttrafficparamptr',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentXCIndex', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                Index into mplsXCTable which identifies which cross-
                connect entry this segment is part of.  A value of
                the string containing the single octet 0x00
                indicates that this entry is not referred
                to by any cross-connect entry.  When a cross-connect
                entry is created which this out-segment is a part of,
                this object MUST be updated by the agent to reflect
                the value of mplsXCIndex of that cross-connect
                entry.
                ''',
                'mplsoutsegmentxcindex',
                'MPLS-LSR-STD-MIB', False),
            ],
            'MPLS-LSR-STD-MIB',
            'mplsOutSegmentEntry',
            _yang_ns._namespaces['MPLS-LSR-STD-MIB'],
        'ydk.models.mpls.MPLS_LSR_STD_MIB'
        ),
    },
    'MPLSLSRSTDMIB.MplsOutSegmentTable' : {
        'meta_info' : _MetaInfoClass('MPLSLSRSTDMIB.MplsOutSegmentTable',
            False, 
            [
            _MetaInfoClassMember('mplsOutSegmentEntry', REFERENCE_LIST, 'MplsOutSegmentEntry' , 'ydk.models.mpls.MPLS_LSR_STD_MIB', 'MPLSLSRSTDMIB.MplsOutSegmentTable.MplsOutSegmentEntry', 
                [], [], 
                '''                An entry in this table represents one outgoing
                segment.  An entry can be created by a network
                administrator, an SNMP agent, or an MPLS signaling
                protocol.  The object mplsOutSegmentOwner indicates
                the creator of this entry. The value of
                mplsOutSegmentRowStatus cannot be active(1) unless
                the ifTable entry corresponding to
                mplsOutSegmentInterface exists.
                
                Note that the indexing of this table uses a single,
                arbitrary index (mplsOutSegmentIndex) to indicate
                which out-segment (i.e.: label) is being switched to
                from which in-segment (i.e: label) or in-segments.
                This is necessary because it is possible to have an
                equal-cost multi-path situation where two identical
                out-going labels are assigned to the same
                cross-connect (i.e.: they go to two different neighboring
                LSRs); thus, requiring two out-segments. In order to
                preserve the uniqueness of the references
                by the mplsXCEntry, an arbitrary integer must be used as
                the index for this table.
                ''',
                'mplsoutsegmententry',
                'MPLS-LSR-STD-MIB', False),
            ],
            'MPLS-LSR-STD-MIB',
            'mplsOutSegmentTable',
            _yang_ns._namespaces['MPLS-LSR-STD-MIB'],
        'ydk.models.mpls.MPLS_LSR_STD_MIB'
        ),
    },
    'MPLSLSRSTDMIB.MplsXCTable.MplsXCEntry.MplsXCAdminStatus_Enum' : _MetaInfoEnum('MplsXCAdminStatus_Enum', 'ydk.models.mpls.MPLS_LSR_STD_MIB',
        {
            'up':'UP',
            'down':'DOWN',
            'testing':'TESTING',
        }, 'MPLS-LSR-STD-MIB', _yang_ns._namespaces['MPLS-LSR-STD-MIB']),
    'MPLSLSRSTDMIB.MplsXCTable.MplsXCEntry.MplsXCOperStatus_Enum' : _MetaInfoEnum('MplsXCOperStatus_Enum', 'ydk.models.mpls.MPLS_LSR_STD_MIB',
        {
            'up':'UP',
            'down':'DOWN',
            'testing':'TESTING',
            'unknown':'UNKNOWN',
            'dormant':'DORMANT',
            'notPresent':'NOTPRESENT',
            'lowerLayerDown':'LOWERLAYERDOWN',
        }, 'MPLS-LSR-STD-MIB', _yang_ns._namespaces['MPLS-LSR-STD-MIB']),
    'MPLSLSRSTDMIB.MplsXCTable.MplsXCEntry' : {
        'meta_info' : _MetaInfoClass('MPLSLSRSTDMIB.MplsXCTable.MplsXCEntry',
            False, 
            [
            _MetaInfoClassMember('mplsXCIndex', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                Primary index for the conceptual row identifying a
                group of cross-connect segments. The string
                containing a single octet 0x00 is an invalid index.
                ''',
                'mplsxcindex',
                'MPLS-LSR-STD-MIB', True),
            _MetaInfoClassMember('mplsXCInSegmentIndex', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                Incoming label index.
                If this object is set to the string containing
                a single octet 0x00, this indicates a special
                case outlined in the table's description above.
                In this case no corresponding mplsInSegmentEntry
                shall exist.
                ''',
                'mplsxcinsegmentindex',
                'MPLS-LSR-STD-MIB', True),
            _MetaInfoClassMember('mplsXCOutSegmentIndex', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                Index of out-segment for LSPs not terminating on
                this LSR if not set to the string containing the
                single octet 0x00. If the segment identified by this
                entry is terminating, then this object MUST be set to
                the string containing a single octet 0x00 to indicate
                that no corresponding mplsOutSegmentEntry shall
                exist.
                ''',
                'mplsxcoutsegmentindex',
                'MPLS-LSR-STD-MIB', True),
            _MetaInfoClassMember('mplsXCAdminStatus', REFERENCE_ENUM_CLASS, 'MplsXCAdminStatus_Enum' , 'ydk.models.mpls.MPLS_LSR_STD_MIB', 'MPLSLSRSTDMIB.MplsXCTable.MplsXCEntry.MplsXCAdminStatus_Enum', 
                [], [], 
                '''                The desired operational status of this segment.
                ''',
                'mplsxcadminstatus',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsXCLabelStackIndex', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                Primary index into mplsLabelStackTable identifying a
                stack of labels to be pushed beneath the top label.
                Note that the top label identified by the out-
                segment ensures that all the components of a
                multipoint-to-point connection have the same
                outgoing label. A value of the string containing the
                single octet 0x00 indicates that no labels are to
                be stacked beneath the top label.
                This object cannot be modified if mplsXCRowStatus is
                active(1).
                ''',
                'mplsxclabelstackindex',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsXCLspId', ATTRIBUTE, 'str' , None, None, 
                [(2, None), (6, None)], [], 
                '''                This value identifies the label switched path that
                this cross-connect entry belongs to. This object
                cannot be modified if mplsXCRowStatus is active(1)
                except for this object.
                ''',
                'mplsxclspid',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsXCOperStatus', REFERENCE_ENUM_CLASS, 'MplsXCOperStatus_Enum' , 'ydk.models.mpls.MPLS_LSR_STD_MIB', 'MPLSLSRSTDMIB.MplsXCTable.MplsXCEntry.MplsXCOperStatus_Enum', 
                [], [], 
                '''                The actual operational status of this cross-
                connect.
                ''',
                'mplsxcoperstatus',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsXCOwner', REFERENCE_ENUM_CLASS, 'MplsOwner_Enum' , 'ydk.models.mpls.MPLS_TC_STD_MIB', 'MplsOwner_Enum', 
                [], [], 
                '''                Denotes the entity that created and is responsible
                for managing this cross-connect.
                ''',
                'mplsxcowner',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsXCRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                For creating, modifying, and deleting this row.
                When a row in this table has a row in the active(1)
                state, no objects in this row except this object
                and the mplsXCStorageType can be modified. 
                ''',
                'mplsxcrowstatus',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsXCStorageType', REFERENCE_ENUM_CLASS, 'StorageType_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'StorageType_Enum', 
                [], [], 
                '''                This variable indicates the storage type for this
                object. The agent MUST ensure that the associated in
                and out segments also have the same StorageType value
                and are restored consistently upon system restart.
                This value SHOULD be set to permanent(4) if created
                as a result of a static LSP configuration.
                
                Conceptual rows having the value 'permanent'
                need not allow write-access to any columnar
                objects in the row.
                ''',
                'mplsxcstoragetype',
                'MPLS-LSR-STD-MIB', False),
            ],
            'MPLS-LSR-STD-MIB',
            'mplsXCEntry',
            _yang_ns._namespaces['MPLS-LSR-STD-MIB'],
        'ydk.models.mpls.MPLS_LSR_STD_MIB'
        ),
    },
    'MPLSLSRSTDMIB.MplsXCTable' : {
        'meta_info' : _MetaInfoClass('MPLSLSRSTDMIB.MplsXCTable',
            False, 
            [
            _MetaInfoClassMember('mplsXCEntry', REFERENCE_LIST, 'MplsXCEntry' , 'ydk.models.mpls.MPLS_LSR_STD_MIB', 'MPLSLSRSTDMIB.MplsXCTable.MplsXCEntry', 
                [], [], 
                '''                A row in this table represents one cross-connect
                entry.  It is indexed by the following objects:
                
                - cross-connect index mplsXCIndex that uniquely
                  identifies a group of cross-connect entries
                
                - in-segment index, mplsXCInSegmentIndex
                
                - out-segment index, mplsXCOutSegmentIndex
                
                LSPs originating at this LSR:
                These are represented by using the special
                of value of mplsXCInSegmentIndex set to the
                string containing a single octet 0x00. In
                this case the mplsXCOutSegmentIndex
                MUST not be the string containing a single
                octet 0x00.
                
                LSPs terminating at this LSR:
                These are represented by using the special value
                mplsXCOutSegmentIndex set to the string containing
                a single octet 0x00.
                
                Special labels:
                Entries indexed by the strings containing the
                reserved MPLS label values as a single octet 0x00
                through 0x0f (inclusive) imply LSPs terminating at
                this LSR.  Note that situations where LSPs are
                terminated with incoming label equal to the string
                containing a single octet 0x00 can be distinguished
                from LSPs originating at this LSR because the
                mplsXCOutSegmentIndex equals the string containing the
                single octet 0x00.
                
                An entry can be created by a network administrator
                or by an SNMP agent as instructed by an MPLS
                signaling protocol.
                ''',
                'mplsxcentry',
                'MPLS-LSR-STD-MIB', False),
            ],
            'MPLS-LSR-STD-MIB',
            'mplsXCTable',
            _yang_ns._namespaces['MPLS-LSR-STD-MIB'],
        'ydk.models.mpls.MPLS_LSR_STD_MIB'
        ),
    },
    'MPLSLSRSTDMIB' : {
        'meta_info' : _MetaInfoClass('MPLSLSRSTDMIB',
            False, 
            [
            _MetaInfoClassMember('mplsInSegmentMapTable', REFERENCE_CLASS, 'MplsInSegmentMapTable' , 'ydk.models.mpls.MPLS_LSR_STD_MIB', 'MPLSLSRSTDMIB.MplsInSegmentMapTable', 
                [], [], 
                '''                This table specifies the mapping from the
                mplsInSegmentIndex to the corresponding
                mplsInSegmentInterface and mplsInSegmentLabel
                objects. The purpose of this table is to
                provide the manager with an alternative
                means by which to locate in-segments.
                ''',
                'mplsinsegmentmaptable',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInSegmentTable', REFERENCE_CLASS, 'MplsInSegmentTable' , 'ydk.models.mpls.MPLS_LSR_STD_MIB', 'MPLSLSRSTDMIB.MplsInSegmentTable', 
                [], [], 
                '''                This table contains a description of the incoming MPLS
                segments (labels) to an LSR and their associated parameters.
                The index for this table is mplsInSegmentIndex.
                The index structure of this table is specifically designed
                to handle many different MPLS implementations that manage
                their labels both in a distributed and centralized manner.
                The table is also designed to handle existing MPLS labels
                as defined in RFC3031 as well as longer ones that may
                be necessary in the future.
                
                In cases where the label cannot fit into the
                mplsInSegmentLabel object, the mplsInSegmentLabelPtr
                will indicate this by being set to the first accessible
                column in the appropriate extension table's row.
                In this case an additional table MUST
                be provided and MUST be indexed by at least the indexes
                used by this table. In all other cases when the label is
                represented within the mplsInSegmentLabel object, the
                mplsInSegmentLabelPtr MUST be set to 0.0. Due to the
                fact that MPLS labels may not exceed 24 bits, the
                mplsInSegmentLabelPtr object is only a provision for
                future-proofing the MIB module. Thus, the definition
                of any extension tables is beyond the scope of this
                MIB module.
                ''',
                'mplsinsegmenttable',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsInterfaceTable', REFERENCE_CLASS, 'MplsInterfaceTable' , 'ydk.models.mpls.MPLS_LSR_STD_MIB', 'MPLSLSRSTDMIB.MplsInterfaceTable', 
                [], [], 
                '''                This table specifies per-interface MPLS capability
                and associated information.
                ''',
                'mplsinterfacetable',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsLabelStackTable', REFERENCE_CLASS, 'MplsLabelStackTable' , 'ydk.models.mpls.MPLS_LSR_STD_MIB', 'MPLSLSRSTDMIB.MplsLabelStackTable', 
                [], [], 
                '''                This table specifies the label stack to be pushed
                onto a packet, beneath the top label.  Entries into
                this table are referred to from mplsXCTable.
                ''',
                'mplslabelstacktable',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsLsrObjects', REFERENCE_CLASS, 'MplsLsrObjects' , 'ydk.models.mpls.MPLS_LSR_STD_MIB', 'MPLSLSRSTDMIB.MplsLsrObjects', 
                [], [], 
                '''                ''',
                'mplslsrobjects',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsOutSegmentTable', REFERENCE_CLASS, 'MplsOutSegmentTable' , 'ydk.models.mpls.MPLS_LSR_STD_MIB', 'MPLSLSRSTDMIB.MplsOutSegmentTable', 
                [], [], 
                '''                This table contains a representation of the outgoing
                segments from an LSR.
                ''',
                'mplsoutsegmenttable',
                'MPLS-LSR-STD-MIB', False),
            _MetaInfoClassMember('mplsXCTable', REFERENCE_CLASS, 'MplsXCTable' , 'ydk.models.mpls.MPLS_LSR_STD_MIB', 'MPLSLSRSTDMIB.MplsXCTable', 
                [], [], 
                '''                This table specifies information for switching
                between LSP segments.  It supports point-to-point,
                point-to-multipoint and multipoint-to-point
                connections.  mplsLabelStackTable specifies the
                label stack information for a cross-connect LSR and
                is referred to from mplsXCTable.
                ''',
                'mplsxctable',
                'MPLS-LSR-STD-MIB', False),
            ],
            'MPLS-LSR-STD-MIB',
            'MPLS-LSR-STD-MIB',
            _yang_ns._namespaces['MPLS-LSR-STD-MIB'],
        'ydk.models.mpls.MPLS_LSR_STD_MIB'
        ),
    },
}
_meta_table['MPLSLSRSTDMIB.MplsInSegmentMapTable.MplsInSegmentMapEntry']['meta_info'].parent =_meta_table['MPLSLSRSTDMIB.MplsInSegmentMapTable']['meta_info']
_meta_table['MPLSLSRSTDMIB.MplsInSegmentTable.MplsInSegmentEntry']['meta_info'].parent =_meta_table['MPLSLSRSTDMIB.MplsInSegmentTable']['meta_info']
_meta_table['MPLSLSRSTDMIB.MplsInterfaceTable.MplsInterfaceEntry']['meta_info'].parent =_meta_table['MPLSLSRSTDMIB.MplsInterfaceTable']['meta_info']
_meta_table['MPLSLSRSTDMIB.MplsLabelStackTable.MplsLabelStackEntry']['meta_info'].parent =_meta_table['MPLSLSRSTDMIB.MplsLabelStackTable']['meta_info']
_meta_table['MPLSLSRSTDMIB.MplsOutSegmentTable.MplsOutSegmentEntry']['meta_info'].parent =_meta_table['MPLSLSRSTDMIB.MplsOutSegmentTable']['meta_info']
_meta_table['MPLSLSRSTDMIB.MplsXCTable.MplsXCEntry']['meta_info'].parent =_meta_table['MPLSLSRSTDMIB.MplsXCTable']['meta_info']
_meta_table['MPLSLSRSTDMIB.MplsInSegmentMapTable']['meta_info'].parent =_meta_table['MPLSLSRSTDMIB']['meta_info']
_meta_table['MPLSLSRSTDMIB.MplsInSegmentTable']['meta_info'].parent =_meta_table['MPLSLSRSTDMIB']['meta_info']
_meta_table['MPLSLSRSTDMIB.MplsInterfaceTable']['meta_info'].parent =_meta_table['MPLSLSRSTDMIB']['meta_info']
_meta_table['MPLSLSRSTDMIB.MplsLabelStackTable']['meta_info'].parent =_meta_table['MPLSLSRSTDMIB']['meta_info']
_meta_table['MPLSLSRSTDMIB.MplsLsrObjects']['meta_info'].parent =_meta_table['MPLSLSRSTDMIB']['meta_info']
_meta_table['MPLSLSRSTDMIB.MplsOutSegmentTable']['meta_info'].parent =_meta_table['MPLSLSRSTDMIB']['meta_info']
_meta_table['MPLSLSRSTDMIB.MplsXCTable']['meta_info'].parent =_meta_table['MPLSLSRSTDMIB']['meta_info']
