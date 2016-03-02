


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'QBRIDGEMIB.Dot1qBase.Dot1qVlanVersionNumber_Enum' : _MetaInfoEnum('Dot1qVlanVersionNumber_Enum', 'ydk.models.q.Q_BRIDGE_MIB',
        {
            'version1':'VERSION1',
        }, 'Q-BRIDGE-MIB', _yang_ns._namespaces['Q-BRIDGE-MIB']),
    'QBRIDGEMIB.Dot1qBase' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qBase',
            False, 
            [
            _MetaInfoClassMember('dot1qGvrpStatus', REFERENCE_ENUM_CLASS, 'EnabledStatus_Enum' , 'ydk.models.p.P_BRIDGE_MIB', 'EnabledStatus_Enum', 
                [], [], 
                '''                The administrative status requested by management for
                GVRP.  The value enabled(1) indicates that GVRP should
                be enabled on this device, on all ports for which it has
                not been specifically disabled.  When disabled(2), GVRP
                is disabled on all ports, and all GVRP packets will be
                forwarded transparently.  This object affects all GVRP
                Applicant and Registrar state machines.  A transition
                from disabled(2) to enabled(1) will cause a reset of all
                GVRP state machines on all ports.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1qgvrpstatus',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qMaxSupportedVlans', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The maximum number of IEEE 802.1Q VLANs that this
                device supports.
                ''',
                'dot1qmaxsupportedvlans',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qMaxVlanId', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                The maximum IEEE 802.1Q VLAN-ID that this device
                
                supports.
                ''',
                'dot1qmaxvlanid',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qNumVlans', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of IEEE 802.1Q VLANs that are
                configured in this device.
                ''',
                'dot1qnumvlans',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qVlanVersionNumber', REFERENCE_ENUM_CLASS, 'Dot1qVlanVersionNumber_Enum' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qBase.Dot1qVlanVersionNumber_Enum', 
                [], [], 
                '''                The version number of IEEE 802.1Q that this device
                supports.
                ''',
                'dot1qvlanversionnumber',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qBase',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qFdbTable.Dot1qFdbEntry' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qFdbTable.Dot1qFdbEntry',
            False, 
            [
            _MetaInfoClassMember('dot1qFdbId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The identity of this Filtering Database.
                ''',
                'dot1qfdbid',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qFdbDynamicCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The current number of dynamic entries in this
                Filtering Database.
                ''',
                'dot1qfdbdynamiccount',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qFdbEntry',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qFdbTable' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qFdbTable',
            False, 
            [
            _MetaInfoClassMember('dot1qFdbEntry', REFERENCE_LIST, 'Dot1qFdbEntry' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qFdbTable.Dot1qFdbEntry', 
                [], [], 
                '''                Information about a specific Filtering Database.
                ''',
                'dot1qfdbentry',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qFdbTable',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qForwardAllTable.Dot1qForwardAllEntry' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qForwardAllTable.Dot1qForwardAllEntry',
            False, 
            [
            _MetaInfoClassMember('dot1qVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'dot1qvlanindex',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qForwardAllForbiddenPorts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The set of ports configured by management in this VLAN
                for which the Service Requirement attribute Forward All
                Multicast Groups may not be dynamically registered by
                GMRP.  This value will be restored after the device is
                reset.  A port may not be added in this set if it is
                already a member of the set of ports in
                dot1qForwardAllStaticPorts.  The default value is a
                string of zeros of appropriate length.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1qforwardallforbiddenports',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qForwardAllPorts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The complete set of ports in this VLAN to which all
                multicast group-addressed frames are to be forwarded.
                This includes ports for which this need has been
                determined dynamically by GMRP, or configured statically
                by management.
                ''',
                'dot1qforwardallports',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qForwardAllStaticPorts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The set of ports configured by management in this VLAN
                to which all multicast group-addressed frames are to be
                forwarded.  Ports entered in this list will also appear
                in the complete set shown by dot1qForwardAllPorts.  This
                value will be restored after the device is reset.  This
                only applies to ports that are members of the VLAN,
                defined by dot1qVlanCurrentEgressPorts.  A port may not
                be added in this set if it is already a member of the
                set of ports in dot1qForwardAllForbiddenPorts.  The
                default value is a string of ones of appropriate length,
                to indicate the standard behaviour of using basic
                filtering services, i.e., forward all multicasts to all
                ports.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1qforwardallstaticports',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qForwardAllEntry',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qForwardAllTable' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qForwardAllTable',
            False, 
            [
            _MetaInfoClassMember('dot1qForwardAllEntry', REFERENCE_LIST, 'Dot1qForwardAllEntry' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qForwardAllTable.Dot1qForwardAllEntry', 
                [], [], 
                '''                Forwarding information for a VLAN, specifying the set
                of ports to which all multicasts should be forwarded,
                configured statically by management or dynamically by
                GMRP.
                ''',
                'dot1qforwardallentry',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qForwardAllTable',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qForwardUnregisteredTable.Dot1qForwardUnregisteredEntry' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qForwardUnregisteredTable.Dot1qForwardUnregisteredEntry',
            False, 
            [
            _MetaInfoClassMember('dot1qVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'dot1qvlanindex',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qForwardUnregisteredForbiddenPorts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The set of ports configured by management in this VLAN
                for which the Service Requirement attribute Forward
                Unregistered Multicast Groups may not be dynamically
                registered by GMRP.  This value will be restored after
                the device is reset.  A port may not be added in this
                set if it is already a member of the set of ports in
                dot1qForwardUnregisteredStaticPorts.  The default value
                is a string of zeros of appropriate length.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1qforwardunregisteredforbiddenports',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qForwardUnregisteredPorts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The complete set of ports in this VLAN to which
                multicast group-addressed frames for which there is no
                more specific forwarding information will be forwarded.
                This includes ports for which this need has been
                determined dynamically by GMRP, or configured statically
                by management.
                ''',
                'dot1qforwardunregisteredports',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qForwardUnregisteredStaticPorts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The set of ports configured by management, in this
                VLAN, to which multicast group-addressed frames for
                which there is no more specific forwarding information
                
                are to be forwarded.  Ports entered in this list will
                also appear in the complete set shown by
                dot1qForwardUnregisteredPorts.  This value will be
                restored after the device is reset.  A port may not be
                added in this set if it is already a member of the set
                of ports in dot1qForwardUnregisteredForbiddenPorts.  The
                default value is a string of zeros of appropriate
                length, although this has no effect with the default
                value of dot1qForwardAllStaticPorts.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1qforwardunregisteredstaticports',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qForwardUnregisteredEntry',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qForwardUnregisteredTable' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qForwardUnregisteredTable',
            False, 
            [
            _MetaInfoClassMember('dot1qForwardUnregisteredEntry', REFERENCE_LIST, 'Dot1qForwardUnregisteredEntry' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qForwardUnregisteredTable.Dot1qForwardUnregisteredEntry', 
                [], [], 
                '''                Forwarding information for a VLAN, specifying the set
                of ports to which all multicasts for which there is no
                more specific forwarding information shall be forwarded.
                This is configured statically by management or
                dynamically by GMRP.
                ''',
                'dot1qforwardunregisteredentry',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qForwardUnregisteredTable',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qLearningConstraintsTable.Dot1qLearningConstraintsEntry.Dot1qConstraintType_Enum' : _MetaInfoEnum('Dot1qConstraintType_Enum', 'ydk.models.q.Q_BRIDGE_MIB',
        {
            'independent':'INDEPENDENT',
            'shared':'SHARED',
        }, 'Q-BRIDGE-MIB', _yang_ns._namespaces['Q-BRIDGE-MIB']),
    'QBRIDGEMIB.Dot1qLearningConstraintsTable.Dot1qLearningConstraintsEntry' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qLearningConstraintsTable.Dot1qLearningConstraintsEntry',
            False, 
            [
            _MetaInfoClassMember('dot1qConstraintSet', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The identity of the constraint set to which
                dot1qConstraintVlan belongs.  These values may be chosen
                by the management station.
                ''',
                'dot1qconstraintset',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qConstraintVlan', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The index of the row in dot1qVlanCurrentTable for the
                VLAN constrained by this entry.
                ''',
                'dot1qconstraintvlan',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qConstraintStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this entry.
                ''',
                'dot1qconstraintstatus',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qConstraintType', REFERENCE_ENUM_CLASS, 'Dot1qConstraintType_Enum' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qLearningConstraintsTable.Dot1qLearningConstraintsEntry.Dot1qConstraintType_Enum', 
                [], [], 
                '''                The type of constraint this entry defines.
                independent(1) - the VLAN, dot1qConstraintVlan,
                    uses a filtering database independent from all
                    other VLANs in the same set, defined by
                    dot1qConstraintSet.
                shared(2) - the VLAN, dot1qConstraintVlan, shares
                    the same filtering database as all other VLANs
                    in the same set, defined by dot1qConstraintSet.
                ''',
                'dot1qconstrainttype',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qLearningConstraintsEntry',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qLearningConstraintsTable' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qLearningConstraintsTable',
            False, 
            [
            _MetaInfoClassMember('dot1qLearningConstraintsEntry', REFERENCE_LIST, 'Dot1qLearningConstraintsEntry' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qLearningConstraintsTable.Dot1qLearningConstraintsEntry', 
                [], [], 
                '''                A learning constraint defined for a VLAN.
                ''',
                'dot1qlearningconstraintsentry',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qLearningConstraintsTable',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable.Dot1qPortVlanHCStatisticsEntry' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable.Dot1qPortVlanHCStatisticsEntry',
            False, 
            [
            _MetaInfoClassMember('dot1dBasePort', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'dot1dbaseport',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'dot1qvlanindex',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qTpVlanPortHCInDiscards', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of valid frames received by this port from
                its segment that were classified as belonging to this
                VLAN and that were discarded due to VLAN-related reasons.
                Specifically, the IEEE 802.1Q counters for Discard
                Inbound and Discard on Ingress Filtering.
                ''',
                'dot1qtpvlanporthcindiscards',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qTpVlanPortHCInFrames', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of valid frames received by this port from
                its segment that were classified as belonging to this
                VLAN.  Note that a frame received on this port is
                counted by this object if and only if it is for a
                
                protocol being processed by the local forwarding process
                for this VLAN.  This object includes received bridge
                management frames classified as belonging to this VLAN
                (e.g., GMRP, but not GVRP or STP).
                ''',
                'dot1qtpvlanporthcinframes',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qTpVlanPortHCOutFrames', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of valid frames transmitted by this port to
                its segment from the local forwarding process for this
                VLAN.  This includes bridge management frames originated
                by this device that are classified as belonging to this
                VLAN (e.g., GMRP, but not GVRP or STP).
                ''',
                'dot1qtpvlanporthcoutframes',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qPortVlanHCStatisticsEntry',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable',
            False, 
            [
            _MetaInfoClassMember('dot1qPortVlanHCStatisticsEntry', REFERENCE_LIST, 'Dot1qPortVlanHCStatisticsEntry' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable.Dot1qPortVlanHCStatisticsEntry', 
                [], [], 
                '''                Traffic statistics for a VLAN on a high-capacity
                interface.
                ''',
                'dot1qportvlanhcstatisticsentry',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qPortVlanHCStatisticsTable',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qPortVlanStatisticsTable.Dot1qPortVlanStatisticsEntry' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qPortVlanStatisticsTable.Dot1qPortVlanStatisticsEntry',
            False, 
            [
            _MetaInfoClassMember('dot1dBasePort', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'dot1dbaseport',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'dot1qvlanindex',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qTpVlanPortInDiscards', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of valid frames received by this port from
                its segment that were classified as belonging to this
                VLAN and that were discarded due to VLAN-related reasons.
                Specifically, the IEEE 802.1Q counters for Discard
                Inbound and Discard on Ingress Filtering.
                ''',
                'dot1qtpvlanportindiscards',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qTpVlanPortInFrames', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of valid frames received by this port from
                its segment that were classified as belonging to this
                VLAN.  Note that a frame received on this port is
                counted by this object if and only if it is for a
                protocol being processed by the local forwarding process
                for this VLAN.  This object includes received bridge
                management frames classified as belonging to this VLAN
                (e.g., GMRP, but not GVRP or STP.
                ''',
                'dot1qtpvlanportinframes',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qTpVlanPortInOverflowDiscards', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the associated
                dot1qTpVlanPortInDiscards counter has overflowed.
                ''',
                'dot1qtpvlanportinoverflowdiscards',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qTpVlanPortInOverflowFrames', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the associated
                dot1qTpVlanPortInFrames counter has overflowed.
                ''',
                'dot1qtpvlanportinoverflowframes',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qTpVlanPortOutFrames', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of valid frames transmitted by this port to
                its segment from the local forwarding process for this
                VLAN.  This includes bridge management frames originated
                by this device that are classified as belonging to this
                VLAN (e.g., GMRP, but not GVRP or STP).
                ''',
                'dot1qtpvlanportoutframes',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qTpVlanPortOutOverflowFrames', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times the associated
                dot1qTpVlanPortOutFrames counter has overflowed.
                ''',
                'dot1qtpvlanportoutoverflowframes',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qPortVlanStatisticsEntry',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qPortVlanStatisticsTable' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qPortVlanStatisticsTable',
            False, 
            [
            _MetaInfoClassMember('dot1qPortVlanStatisticsEntry', REFERENCE_LIST, 'Dot1qPortVlanStatisticsEntry' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qPortVlanStatisticsTable.Dot1qPortVlanStatisticsEntry', 
                [], [], 
                '''                Traffic statistics for a VLAN on an interface.
                ''',
                'dot1qportvlanstatisticsentry',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qPortVlanStatisticsTable',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qStaticMulticastTable.Dot1qStaticMulticastEntry.Dot1qStaticMulticastStatus_Enum' : _MetaInfoEnum('Dot1qStaticMulticastStatus_Enum', 'ydk.models.q.Q_BRIDGE_MIB',
        {
            'other':'OTHER',
            'invalid':'INVALID',
            'permanent':'PERMANENT',
            'deleteOnReset':'DELETEONRESET',
            'deleteOnTimeout':'DELETEONTIMEOUT',
        }, 'Q-BRIDGE-MIB', _yang_ns._namespaces['Q-BRIDGE-MIB']),
    'QBRIDGEMIB.Dot1qStaticMulticastTable.Dot1qStaticMulticastEntry' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qStaticMulticastTable.Dot1qStaticMulticastEntry',
            False, 
            [
            _MetaInfoClassMember('dot1qStaticMulticastAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The destination MAC address in a frame to which this
                entry's filtering information applies.  This object must
                take the value of a Multicast or Broadcast address.
                ''',
                'dot1qstaticmulticastaddress',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qStaticMulticastReceivePort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Either the value '0' or the port number of the port
                from which a frame must be received in order for this
                entry's filtering information to apply.  A value of zero
                indicates that this entry applies on all ports of the
                device for which there is no other applicable entry.
                ''',
                'dot1qstaticmulticastreceiveport',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'dot1qvlanindex',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qStaticMulticastForbiddenEgressPorts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The set of ports to which frames received from a
                specific port and destined for a specific Multicast or
                Broadcast MAC address must not be forwarded, regardless
                of any dynamic information, e.g., from GMRP.  A port may
                not be added in this set if it is already a member of the
                set of ports in dot1qStaticMulticastStaticEgressPorts.
                The default value of this object is a string of zeros of
                appropriate length.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1qstaticmulticastforbiddenegressports',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qStaticMulticastStaticEgressPorts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The set of ports to which frames received from a
                specific port and destined for a specific Multicast or
                Broadcast MAC address must be forwarded, regardless of
                any dynamic information, e.g., from GMRP.  A port may not
                be added in this set if it is already a member of the
                set of ports in dot1qStaticMulticastForbiddenEgressPorts.
                The default value of this object is a string of ones of
                appropriate length.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1qstaticmulticaststaticegressports',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qStaticMulticastStatus', REFERENCE_ENUM_CLASS, 'Dot1qStaticMulticastStatus_Enum' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qStaticMulticastTable.Dot1qStaticMulticastEntry.Dot1qStaticMulticastStatus_Enum', 
                [], [], 
                '''                This object indicates the status of this entry.
                other(1) - this entry is currently in use, but
                    the conditions under which it will remain
                    so differ from the following values.
                
                invalid(2) - writing this value to the object
                    removes the corresponding entry.
                permanent(3) - this entry is currently in use
                    and will remain so after the next reset of
                    the bridge.
                deleteOnReset(4) - this entry is currently in
                    use and will remain so until the next
                    reset of the bridge.
                deleteOnTimeout(5) - this entry is currently in
                    use and will remain so until it is aged out.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1qstaticmulticaststatus',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qStaticMulticastEntry',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qStaticMulticastTable' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qStaticMulticastTable',
            False, 
            [
            _MetaInfoClassMember('dot1qStaticMulticastEntry', REFERENCE_LIST, 'Dot1qStaticMulticastEntry' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qStaticMulticastTable.Dot1qStaticMulticastEntry', 
                [], [], 
                '''                Filtering information configured into the device by
                (local or network) management specifying the set of
                ports to which frames received from this specific port
                
                for this VLAN and containing this Multicast or Broadcast
                destination address are allowed to be forwarded.
                ''',
                'dot1qstaticmulticastentry',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qStaticMulticastTable',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qStaticUnicastTable.Dot1qStaticUnicastEntry.Dot1qStaticUnicastStatus_Enum' : _MetaInfoEnum('Dot1qStaticUnicastStatus_Enum', 'ydk.models.q.Q_BRIDGE_MIB',
        {
            'other':'OTHER',
            'invalid':'INVALID',
            'permanent':'PERMANENT',
            'deleteOnReset':'DELETEONRESET',
            'deleteOnTimeout':'DELETEONTIMEOUT',
        }, 'Q-BRIDGE-MIB', _yang_ns._namespaces['Q-BRIDGE-MIB']),
    'QBRIDGEMIB.Dot1qStaticUnicastTable.Dot1qStaticUnicastEntry' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qStaticUnicastTable.Dot1qStaticUnicastEntry',
            False, 
            [
            _MetaInfoClassMember('dot1qFdbId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'dot1qfdbid',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qStaticUnicastAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The destination MAC address in a frame to which this
                entry's filtering information applies.  This object must
                take the value of a unicast address.
                ''',
                'dot1qstaticunicastaddress',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qStaticUnicastReceivePort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Either the value '0' or the port number of the port
                from which a frame must be received in order for this
                entry's filtering information to apply.  A value of zero
                indicates that this entry applies on all ports of the
                device for which there is no other applicable entry.
                ''',
                'dot1qstaticunicastreceiveport',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qStaticUnicastAllowedToGoTo', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The set of ports for which a frame with a specific
                unicast address will be flooded in the event that it
                has not been learned.  It also specifies the set of
                ports on which a specific unicast address may be dynamically
                learned.  The dot1qTpFdbTable will have an equivalent
                entry with a dot1qTpFdbPort value of '0' until this
                address has been learned, at which point it will be updated
                with the port the address has been seen on.  This only
                applies to ports that are members of the VLAN, defined
                by dot1qVlanCurrentEgressPorts.  The default value of
                this object is a string of ones of appropriate length.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1qstaticunicastallowedtogoto',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qStaticUnicastStatus', REFERENCE_ENUM_CLASS, 'Dot1qStaticUnicastStatus_Enum' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qStaticUnicastTable.Dot1qStaticUnicastEntry.Dot1qStaticUnicastStatus_Enum', 
                [], [], 
                '''                This object indicates the status of this entry.
                other(1) - this entry is currently in use, but
                
                    the conditions under which it will remain
                    so differ from the following values.
                invalid(2) - writing this value to the object
                    removes the corresponding entry.
                permanent(3) - this entry is currently in use
                    and will remain so after the next reset of
                    the bridge.
                deleteOnReset(4) - this entry is currently in
                    use and will remain so until the next
                    reset of the bridge.
                deleteOnTimeout(5) - this entry is currently in
                    use and will remain so until it is aged out.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1qstaticunicaststatus',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qStaticUnicastEntry',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qStaticUnicastTable' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qStaticUnicastTable',
            False, 
            [
            _MetaInfoClassMember('dot1qStaticUnicastEntry', REFERENCE_LIST, 'Dot1qStaticUnicastEntry' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qStaticUnicastTable.Dot1qStaticUnicastEntry', 
                [], [], 
                '''                Filtering information configured into the device by
                (local or network) management specifying the set of
                ports to which frames received from a specific port and
                containing a specific unicast destination address are
                allowed to be forwarded.
                ''',
                'dot1qstaticunicastentry',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qStaticUnicastTable',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qTpFdbTable.Dot1qTpFdbEntry.Dot1qTpFdbStatus_Enum' : _MetaInfoEnum('Dot1qTpFdbStatus_Enum', 'ydk.models.q.Q_BRIDGE_MIB',
        {
            'other':'OTHER',
            'invalid':'INVALID',
            'learned':'LEARNED',
            'self':'SELF',
            'mgmt':'MGMT',
        }, 'Q-BRIDGE-MIB', _yang_ns._namespaces['Q-BRIDGE-MIB']),
    'QBRIDGEMIB.Dot1qTpFdbTable.Dot1qTpFdbEntry' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qTpFdbTable.Dot1qTpFdbEntry',
            False, 
            [
            _MetaInfoClassMember('dot1qFdbId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'dot1qfdbid',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qTpFdbAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                A unicast MAC address for which the device has
                forwarding and/or filtering information.
                ''',
                'dot1qtpfdbaddress',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qTpFdbPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Either the value '0', or the port number of the port on
                which a frame having a source address equal to the value
                of the corresponding instance of dot1qTpFdbAddress has
                been seen.  A value of '0' indicates that the port
                number has not been learned but that the device does
                have some forwarding/filtering information about this
                address (e.g., in the dot1qStaticUnicastTable).
                Implementors are encouraged to assign the port value to
                this object whenever it is learned, even for addresses
                for which the corresponding value of dot1qTpFdbStatus is
                not learned(3).
                ''',
                'dot1qtpfdbport',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qTpFdbStatus', REFERENCE_ENUM_CLASS, 'Dot1qTpFdbStatus_Enum' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qTpFdbTable.Dot1qTpFdbEntry.Dot1qTpFdbStatus_Enum', 
                [], [], 
                '''                The status of this entry.  The meanings of the values
                are:
                    other(1) - none of the following.  This may include
                        the case where some other MIB object (not the
                        corresponding instance of dot1qTpFdbPort, nor an
                        entry in the dot1qStaticUnicastTable) is being
                        used to determine if and how frames addressed to
                        the value of the corresponding instance of
                        dot1qTpFdbAddress are being forwarded.
                    invalid(2) - this entry is no longer valid (e.g., it
                
                        was learned but has since aged out), but has not
                        yet been flushed from the table.
                    learned(3) - the value of the corresponding instance
                        of dot1qTpFdbPort was learned and is being used.
                    self(4) - the value of the corresponding instance of
                        dot1qTpFdbAddress represents one of the device's
                        addresses.  The corresponding instance of
                        dot1qTpFdbPort indicates which of the device's
                        ports has this address.
                    mgmt(5) - the value of the corresponding instance of
                        dot1qTpFdbAddress is also the value of an
                        existing instance of dot1qStaticAddress.
                ''',
                'dot1qtpfdbstatus',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qTpFdbEntry',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qTpFdbTable' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qTpFdbTable',
            False, 
            [
            _MetaInfoClassMember('dot1qTpFdbEntry', REFERENCE_LIST, 'Dot1qTpFdbEntry' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qTpFdbTable.Dot1qTpFdbEntry', 
                [], [], 
                '''                Information about a specific unicast MAC address for
                which the device has some forwarding and/or filtering
                information.
                ''',
                'dot1qtpfdbentry',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qTpFdbTable',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qTpGroupTable.Dot1qTpGroupEntry' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qTpGroupTable.Dot1qTpGroupEntry',
            False, 
            [
            _MetaInfoClassMember('dot1qTpGroupAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The destination Group MAC address in a frame to which
                this entry's filtering information applies.
                ''',
                'dot1qtpgroupaddress',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'dot1qvlanindex',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qTpGroupEgressPorts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The complete set of ports, in this VLAN, to which
                frames destined for this Group MAC address are currently
                being explicitly forwarded.  This does not include ports
                for which this address is only implicitly forwarded, in
                the dot1qForwardAllPorts list.
                ''',
                'dot1qtpgroupegressports',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qTpGroupLearnt', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The subset of ports in dot1qTpGroupEgressPorts that
                were learned by GMRP or some other dynamic mechanism, in
                this Filtering database.
                ''',
                'dot1qtpgrouplearnt',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qTpGroupEntry',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qTpGroupTable' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qTpGroupTable',
            False, 
            [
            _MetaInfoClassMember('dot1qTpGroupEntry', REFERENCE_LIST, 'Dot1qTpGroupEntry' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qTpGroupTable.Dot1qTpGroupEntry', 
                [], [], 
                '''                Filtering information configured into the bridge by
                management, or learned dynamically, specifying the set of
                ports to which frames received on a VLAN and containing
                a specific Group destination address are allowed to be
                forwarded.  The subset of these ports learned dynamically
                is also provided.
                ''',
                'dot1qtpgroupentry',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qTpGroupTable',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qVlan.Dot1qConstraintTypeDefault_Enum' : _MetaInfoEnum('Dot1qConstraintTypeDefault_Enum', 'ydk.models.q.Q_BRIDGE_MIB',
        {
            'independent':'INDEPENDENT',
            'shared':'SHARED',
        }, 'Q-BRIDGE-MIB', _yang_ns._namespaces['Q-BRIDGE-MIB']),
    'QBRIDGEMIB.Dot1qVlan' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qVlan',
            False, 
            [
            _MetaInfoClassMember('dot1qConstraintSetDefault', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The identity of the constraint set to which a VLAN
                belongs, if there is not an explicit entry for that VLAN
                in dot1qLearningConstraintsTable.
                
                The value of this object MUST be retained across
                reinitializations of the management system.
                ''',
                'dot1qconstraintsetdefault',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qConstraintTypeDefault', REFERENCE_ENUM_CLASS, 'Dot1qConstraintTypeDefault_Enum' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qVlan.Dot1qConstraintTypeDefault_Enum', 
                [], [], 
                '''                The type of constraint set to which a VLAN belongs, if
                there is not an explicit entry for that VLAN in
                dot1qLearningConstraintsTable.  The types are as defined
                for dot1qConstraintType.
                
                The value of this object MUST be retained across
                
                reinitializations of the management system.
                ''',
                'dot1qconstrainttypedefault',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qNextFreeLocalVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, None), (4096, 2147483647)], [], 
                '''                The next available value for dot1qVlanIndex of a local
                VLAN entry in dot1qVlanStaticTable.  This will report
                values >=4096 if a new Local VLAN may be created or else
                the value 0 if this is not possible.
                
                A row creation operation in this table for an entry with a local
                VlanIndex value may fail if the current value of this object
                is not used as the index.  Even if the value read is used,
                there is no guarantee that it will still be the valid index
                when the create operation is attempted; another manager may
                have already got in during the intervening time interval.
                In this case, dot1qNextFreeLocalVlanIndex should be re-read
                
                and the creation re-tried with the new value.
                
                This value will automatically change when the current value is
                used to create a new row.
                ''',
                'dot1qnextfreelocalvlanindex',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qVlanNumDeletes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times a VLAN entry has been deleted from
                the dot1qVlanCurrentTable (for any reason).  If an entry
                is deleted, then inserted, and then deleted, this
                counter will be incremented by 2.
                ''',
                'dot1qvlannumdeletes',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qVlan',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry.Dot1qVlanStatus_Enum' : _MetaInfoEnum('Dot1qVlanStatus_Enum', 'ydk.models.q.Q_BRIDGE_MIB',
        {
            'other':'OTHER',
            'permanent':'PERMANENT',
            'dynamicGvrp':'DYNAMICGVRP',
        }, 'Q-BRIDGE-MIB', _yang_ns._namespaces['Q-BRIDGE-MIB']),
    'QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry',
            False, 
            [
            _MetaInfoClassMember('dot1qVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The VLAN-ID or other identifier referring to this VLAN.
                ''',
                'dot1qvlanindex',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qVlanTimeMark', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                A TimeFilter for this entry.  See the TimeFilter
                textual convention to see how this works.
                ''',
                'dot1qvlantimemark',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qVlanCreationTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when this VLAN was created.
                ''',
                'dot1qvlancreationtime',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qVlanCurrentEgressPorts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The set of ports that are transmitting traffic for
                this VLAN as either tagged or untagged frames.
                ''',
                'dot1qvlancurrentegressports',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qVlanCurrentUntaggedPorts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The set of ports that are transmitting traffic for
                this VLAN as untagged frames.
                ''',
                'dot1qvlancurrentuntaggedports',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qVlanFdbId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The Filtering Database used by this VLAN.  This is one
                of the dot1qFdbId values in the dot1qFdbTable.  This
                value is allocated automatically by the device whenever
                
                the VLAN is created: either dynamically by GVRP, or by
                management, in dot1qVlanStaticTable.  Allocation of this
                value follows the learning constraints defined for this
                VLAN in dot1qLearningConstraintsTable.
                ''',
                'dot1qvlanfdbid',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qVlanStatus', REFERENCE_ENUM_CLASS, 'Dot1qVlanStatus_Enum' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry.Dot1qVlanStatus_Enum', 
                [], [], 
                '''                This object indicates the status of this entry.
                other(1) - this entry is currently in use, but the
                    conditions under which it will remain so differ
                    from the following values.
                permanent(2) - this entry, corresponding to an entry
                    in dot1qVlanStaticTable, is currently in use and
                    will remain so after the next reset of the
                    device.  The port lists for this entry include
                    ports from the equivalent dot1qVlanStaticTable
                    entry and ports learned dynamically.
                dynamicGvrp(3) - this entry is currently in use
                
                    and will remain so until removed by GVRP.  There
                    is no static entry for this VLAN, and it will be
                    removed when the last port leaves the VLAN.
                ''',
                'dot1qvlanstatus',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qVlanCurrentEntry',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qVlanCurrentTable' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qVlanCurrentTable',
            False, 
            [
            _MetaInfoClassMember('dot1qVlanCurrentEntry', REFERENCE_LIST, 'Dot1qVlanCurrentEntry' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry', 
                [], [], 
                '''                Information for a VLAN configured into the device by
                
                (local or network) management, or dynamically created
                as a result of GVRP requests received.
                ''',
                'dot1qvlancurrententry',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qVlanCurrentTable',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qVlanStaticTable.Dot1qVlanStaticEntry' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qVlanStaticTable.Dot1qVlanStaticEntry',
            False, 
            [
            _MetaInfoClassMember('dot1qVlanIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'dot1qvlanindex',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1qVlanForbiddenEgressPorts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The set of ports that are prohibited by management
                from being included in the egress list for this VLAN.
                Changes to this object that cause a port to be included
                or excluded affect the per-port, per-VLAN Registrar
                control for Registration Forbidden for the relevant GVRP
                state machine on each port.  A port may not be added in
                this set if it is already a member of the set of ports
                in dot1qVlanStaticEgressPorts.  The default value of
                this object is a string of zeros of appropriate length,
                excluding all ports from the forbidden set.
                ''',
                'dot1qvlanforbiddenegressports',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qVlanStaticEgressPorts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The set of ports that are permanently assigned to the
                egress list for this VLAN by management.  Changes to a
                bit in this object affect the per-port, per-VLAN
                Registrar control for Registration Fixed for the
                relevant GVRP state machine on each port.  A port may
                not be added in this set if it is already a member of
                the set of ports in dot1qVlanForbiddenEgressPorts.  The
                default value of this object is a string of zeros of
                appropriate length, indicating not fixed.
                ''',
                'dot1qvlanstaticegressports',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qVlanStaticName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                An administratively assigned string, which may be used
                to identify the VLAN.
                ''',
                'dot1qvlanstaticname',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qVlanStaticRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object indicates the status of this entry.
                ''',
                'dot1qvlanstaticrowstatus',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qVlanStaticUntaggedPorts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The set of ports that should transmit egress packets
                for this VLAN as untagged.  The default value of this
                object for the default VLAN (dot1qVlanIndex = 1) is a string
                of appropriate length including all ports.  There is no
                specified default for other VLANs.  If a device agent cannot
                support the set of ports being set, then it will reject the
                set operation with an error.  For example, a
                manager might attempt to set more than one VLAN to be untagged
                on egress where the device does not support this IEEE 802.1Q
                option.
                ''',
                'dot1qvlanstaticuntaggedports',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qVlanStaticEntry',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1qVlanStaticTable' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1qVlanStaticTable',
            False, 
            [
            _MetaInfoClassMember('dot1qVlanStaticEntry', REFERENCE_LIST, 'Dot1qVlanStaticEntry' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qVlanStaticTable.Dot1qVlanStaticEntry', 
                [], [], 
                '''                Static information for a VLAN configured into the
                device by (local or network) management.
                ''',
                'dot1qvlanstaticentry',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1qVlanStaticTable',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1vProtocolGroupTable.Dot1vProtocolGroupEntry.Dot1vProtocolTemplateFrameType_Enum' : _MetaInfoEnum('Dot1vProtocolTemplateFrameType_Enum', 'ydk.models.q.Q_BRIDGE_MIB',
        {
            'ethernet':'ETHERNET',
            'rfc1042':'RFC1042',
            'snap8021H':'SNAP8021H',
            'snapOther':'SNAPOTHER',
            'llcOther':'LLCOTHER',
        }, 'Q-BRIDGE-MIB', _yang_ns._namespaces['Q-BRIDGE-MIB']),
    'QBRIDGEMIB.Dot1vProtocolGroupTable.Dot1vProtocolGroupEntry' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1vProtocolGroupTable.Dot1vProtocolGroupEntry',
            False, 
            [
            _MetaInfoClassMember('dot1vProtocolTemplateFrameType', REFERENCE_ENUM_CLASS, 'Dot1vProtocolTemplateFrameType_Enum' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1vProtocolGroupTable.Dot1vProtocolGroupEntry.Dot1vProtocolTemplateFrameType_Enum', 
                [], [], 
                '''                The data-link encapsulation format or the
                'detagged_frame_type' in a Protocol Template.
                ''',
                'dot1vprotocoltemplateframetype',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1vProtocolTemplateProtocolValue', ATTRIBUTE, 'str' , None, None, 
                [(2, None), (5, None)], [], 
                '''                The identification of the protocol above the data-link
                layer in a Protocol Template.  Depending on the
                frame type, the octet string will have one of the
                following values:
                
                For 'ethernet', 'rfc1042' and 'snap8021H',
                    this is the 16-bit (2-octet) IEEE 802.3 Type Field.
                For 'snapOther',
                    this is the 40-bit (5-octet) PID.
                For 'llcOther',
                    this is the 2-octet IEEE 802.2 Link Service Access
                    Point (LSAP) pair: first octet for Destination Service
                    Access Point (DSAP) and second octet for Source Service
                    Access Point (SSAP).
                ''',
                'dot1vprotocoltemplateprotocolvalue',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1vProtocolGroupId', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                Represents a group of protocols that are associated
                together when assigning a VID to a frame.
                ''',
                'dot1vprotocolgroupid',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1vProtocolGroupRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object indicates the status of this entry.
                ''',
                'dot1vprotocolgrouprowstatus',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1vProtocolGroupEntry',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1vProtocolGroupTable' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1vProtocolGroupTable',
            False, 
            [
            _MetaInfoClassMember('dot1vProtocolGroupEntry', REFERENCE_LIST, 'Dot1vProtocolGroupEntry' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1vProtocolGroupTable.Dot1vProtocolGroupEntry', 
                [], [], 
                '''                A mapping from a Protocol Template to a Protocol
                Group Identifier.
                ''',
                'dot1vprotocolgroupentry',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1vProtocolGroupTable',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1vProtocolPortTable.Dot1vProtocolPortEntry' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1vProtocolPortTable.Dot1vProtocolPortEntry',
            False, 
            [
            _MetaInfoClassMember('dot1dBasePort', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'dot1dbaseport',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1vProtocolPortGroupId', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                Designates a group of protocols in the Protocol
                Group Database.
                ''',
                'dot1vprotocolportgroupid',
                'Q-BRIDGE-MIB', True),
            _MetaInfoClassMember('dot1vProtocolPortGroupVid', ATTRIBUTE, 'int' , None, None, 
                [(1, 4094)], [], 
                '''                The VID associated with a group of protocols for
                each port.
                ''',
                'dot1vprotocolportgroupvid',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1vProtocolPortRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object indicates the status of this entry.
                ''',
                'dot1vprotocolportrowstatus',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1vProtocolPortEntry',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB.Dot1vProtocolPortTable' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB.Dot1vProtocolPortTable',
            False, 
            [
            _MetaInfoClassMember('dot1vProtocolPortEntry', REFERENCE_LIST, 'Dot1vProtocolPortEntry' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1vProtocolPortTable.Dot1vProtocolPortEntry', 
                [], [], 
                '''                A VID set for a port.
                ''',
                'dot1vprotocolportentry',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'dot1vProtocolPortTable',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
    'QBRIDGEMIB' : {
        'meta_info' : _MetaInfoClass('QBRIDGEMIB',
            False, 
            [
            _MetaInfoClassMember('dot1qBase', REFERENCE_CLASS, 'Dot1qBase' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qBase', 
                [], [], 
                '''                ''',
                'dot1qbase',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qFdbTable', REFERENCE_CLASS, 'Dot1qFdbTable' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qFdbTable', 
                [], [], 
                '''                A table that contains configuration and control
                information for each Filtering Database currently
                operating on this device.  Entries in this table appear
                automatically when VLANs are assigned FDB IDs in the
                dot1qVlanCurrentTable.
                ''',
                'dot1qfdbtable',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qForwardAllTable', REFERENCE_CLASS, 'Dot1qForwardAllTable' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qForwardAllTable', 
                [], [], 
                '''                A table containing forwarding information for each
                
                VLAN, specifying the set of ports to which forwarding of
                all multicasts applies, configured statically by
                management or dynamically by GMRP.  An entry appears in
                this table for all VLANs that are currently
                instantiated.
                ''',
                'dot1qforwardalltable',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qForwardUnregisteredTable', REFERENCE_CLASS, 'Dot1qForwardUnregisteredTable' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qForwardUnregisteredTable', 
                [], [], 
                '''                A table containing forwarding information for each
                VLAN, specifying the set of ports to which forwarding of
                multicast group-addressed frames for which no
                more specific forwarding information applies.  This is
                configured statically by management and determined
                dynamically by GMRP.  An entry appears in this table for
                all VLANs that are currently instantiated.
                ''',
                'dot1qforwardunregisteredtable',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qLearningConstraintsTable', REFERENCE_CLASS, 'Dot1qLearningConstraintsTable' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qLearningConstraintsTable', 
                [], [], 
                '''                A table containing learning constraints for sets of
                Shared and Independent VLANs.
                ''',
                'dot1qlearningconstraintstable',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qPortVlanHCStatisticsTable', REFERENCE_CLASS, 'Dot1qPortVlanHCStatisticsTable' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable', 
                [], [], 
                '''                A table containing per-port, per-VLAN statistics for
                traffic on high-capacity interfaces.
                ''',
                'dot1qportvlanhcstatisticstable',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qPortVlanStatisticsTable', REFERENCE_CLASS, 'Dot1qPortVlanStatisticsTable' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qPortVlanStatisticsTable', 
                [], [], 
                '''                A table containing per-port, per-VLAN statistics for
                traffic received.  Separate objects are provided for both the
                most-significant and least-significant bits of statistics
                counters for ports that are associated with this transparent
                bridge.  The most-significant bit objects are only required on
                high-capacity interfaces, as defined in the conformance clauses
                for these objects.  This mechanism is provided as a way to read
                64-bit counters for agents that support only SNMPv1.
                
                Note that the reporting of most-significant and least-
                significant counter bits separately runs the risk of missing
                an overflow of the lower bits in the interval between sampling.
                The manager must be aware of this possibility, even within the
                same varbindlist, when interpreting the results of a request or
                
                asynchronous notification.
                ''',
                'dot1qportvlanstatisticstable',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qStaticMulticastTable', REFERENCE_CLASS, 'Dot1qStaticMulticastTable' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qStaticMulticastTable', 
                [], [], 
                '''                A table containing filtering information for Multicast
                and Broadcast MAC addresses for each VLAN, configured
                into the device by (local or network) management
                specifying the set of ports to which frames received
                from specific ports and containing specific Multicast
                and Broadcast destination addresses are allowed to be
                forwarded.  A value of zero in this table (as the port
                number from which frames with a specific destination
                address are received) is used to specify all ports for
                which there is no specific entry in this table for that
                particular destination address.  Entries are valid for
                Multicast and Broadcast addresses only.
                ''',
                'dot1qstaticmulticasttable',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qStaticUnicastTable', REFERENCE_CLASS, 'Dot1qStaticUnicastTable' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qStaticUnicastTable', 
                [], [], 
                '''                A table containing filtering information for Unicast
                MAC addresses for each Filtering Database, configured
                into the device by (local or network) management
                specifying the set of ports to which frames received
                from specific ports and containing specific unicast
                destination addresses are allowed to be forwarded.  A
                value of zero in this table (as the port number from
                
                which frames with a specific destination address are
                received) is used to specify all ports for which there
                is no specific entry in this table for that particular
                destination address.  Entries are valid for unicast
                addresses only.
                ''',
                'dot1qstaticunicasttable',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qTpFdbTable', REFERENCE_CLASS, 'Dot1qTpFdbTable' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qTpFdbTable', 
                [], [], 
                '''                A table that contains information about unicast entries
                for which the device has forwarding and/or filtering
                information.  This information is used by the
                transparent bridging function in determining how to
                propagate a received frame.
                ''',
                'dot1qtpfdbtable',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qTpGroupTable', REFERENCE_CLASS, 'Dot1qTpGroupTable' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qTpGroupTable', 
                [], [], 
                '''                A table containing filtering information for VLANs
                configured into the bridge by (local or network)
                management, or learned dynamically, specifying the set of
                ports to which frames received on a VLAN for this FDB
                and containing a specific Group destination address are
                allowed to be forwarded.
                ''',
                'dot1qtpgrouptable',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qVlan', REFERENCE_CLASS, 'Dot1qVlan' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qVlan', 
                [], [], 
                '''                ''',
                'dot1qvlan',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qVlanCurrentTable', REFERENCE_CLASS, 'Dot1qVlanCurrentTable' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qVlanCurrentTable', 
                [], [], 
                '''                A table containing current configuration information
                for each VLAN currently configured into the device by
                (local or network) management, or dynamically created
                as a result of GVRP requests received.
                ''',
                'dot1qvlancurrenttable',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1qVlanStaticTable', REFERENCE_CLASS, 'Dot1qVlanStaticTable' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1qVlanStaticTable', 
                [], [], 
                '''                A table containing static configuration information for
                each VLAN configured into the device by (local or
                network) management.  All entries are permanent and will
                be restored after the device is reset.
                ''',
                'dot1qvlanstatictable',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1vProtocolGroupTable', REFERENCE_CLASS, 'Dot1vProtocolGroupTable' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1vProtocolGroupTable', 
                [], [], 
                '''                A table that contains mappings from Protocol
                Templates to Protocol Group Identifiers used for
                Port-and-Protocol-based VLAN Classification.
                ''',
                'dot1vprotocolgrouptable',
                'Q-BRIDGE-MIB', False),
            _MetaInfoClassMember('dot1vProtocolPortTable', REFERENCE_CLASS, 'Dot1vProtocolPortTable' , 'ydk.models.q.Q_BRIDGE_MIB', 'QBRIDGEMIB.Dot1vProtocolPortTable', 
                [], [], 
                '''                A table that contains VID sets used for
                Port-and-Protocol-based VLAN Classification.
                ''',
                'dot1vprotocolporttable',
                'Q-BRIDGE-MIB', False),
            ],
            'Q-BRIDGE-MIB',
            'Q-BRIDGE-MIB',
            _yang_ns._namespaces['Q-BRIDGE-MIB'],
        'ydk.models.q.Q_BRIDGE_MIB'
        ),
    },
}
_meta_table['QBRIDGEMIB.Dot1qFdbTable.Dot1qFdbEntry']['meta_info'].parent =_meta_table['QBRIDGEMIB.Dot1qFdbTable']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qForwardAllTable.Dot1qForwardAllEntry']['meta_info'].parent =_meta_table['QBRIDGEMIB.Dot1qForwardAllTable']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qForwardUnregisteredTable.Dot1qForwardUnregisteredEntry']['meta_info'].parent =_meta_table['QBRIDGEMIB.Dot1qForwardUnregisteredTable']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qLearningConstraintsTable.Dot1qLearningConstraintsEntry']['meta_info'].parent =_meta_table['QBRIDGEMIB.Dot1qLearningConstraintsTable']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable.Dot1qPortVlanHCStatisticsEntry']['meta_info'].parent =_meta_table['QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qPortVlanStatisticsTable.Dot1qPortVlanStatisticsEntry']['meta_info'].parent =_meta_table['QBRIDGEMIB.Dot1qPortVlanStatisticsTable']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qStaticMulticastTable.Dot1qStaticMulticastEntry']['meta_info'].parent =_meta_table['QBRIDGEMIB.Dot1qStaticMulticastTable']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qStaticUnicastTable.Dot1qStaticUnicastEntry']['meta_info'].parent =_meta_table['QBRIDGEMIB.Dot1qStaticUnicastTable']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qTpFdbTable.Dot1qTpFdbEntry']['meta_info'].parent =_meta_table['QBRIDGEMIB.Dot1qTpFdbTable']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qTpGroupTable.Dot1qTpGroupEntry']['meta_info'].parent =_meta_table['QBRIDGEMIB.Dot1qTpGroupTable']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qVlanCurrentTable.Dot1qVlanCurrentEntry']['meta_info'].parent =_meta_table['QBRIDGEMIB.Dot1qVlanCurrentTable']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qVlanStaticTable.Dot1qVlanStaticEntry']['meta_info'].parent =_meta_table['QBRIDGEMIB.Dot1qVlanStaticTable']['meta_info']
_meta_table['QBRIDGEMIB.Dot1vProtocolGroupTable.Dot1vProtocolGroupEntry']['meta_info'].parent =_meta_table['QBRIDGEMIB.Dot1vProtocolGroupTable']['meta_info']
_meta_table['QBRIDGEMIB.Dot1vProtocolPortTable.Dot1vProtocolPortEntry']['meta_info'].parent =_meta_table['QBRIDGEMIB.Dot1vProtocolPortTable']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qBase']['meta_info'].parent =_meta_table['QBRIDGEMIB']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qFdbTable']['meta_info'].parent =_meta_table['QBRIDGEMIB']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qForwardAllTable']['meta_info'].parent =_meta_table['QBRIDGEMIB']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qForwardUnregisteredTable']['meta_info'].parent =_meta_table['QBRIDGEMIB']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qLearningConstraintsTable']['meta_info'].parent =_meta_table['QBRIDGEMIB']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qPortVlanHCStatisticsTable']['meta_info'].parent =_meta_table['QBRIDGEMIB']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qPortVlanStatisticsTable']['meta_info'].parent =_meta_table['QBRIDGEMIB']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qStaticMulticastTable']['meta_info'].parent =_meta_table['QBRIDGEMIB']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qStaticUnicastTable']['meta_info'].parent =_meta_table['QBRIDGEMIB']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qTpFdbTable']['meta_info'].parent =_meta_table['QBRIDGEMIB']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qTpGroupTable']['meta_info'].parent =_meta_table['QBRIDGEMIB']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qVlan']['meta_info'].parent =_meta_table['QBRIDGEMIB']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qVlanCurrentTable']['meta_info'].parent =_meta_table['QBRIDGEMIB']['meta_info']
_meta_table['QBRIDGEMIB.Dot1qVlanStaticTable']['meta_info'].parent =_meta_table['QBRIDGEMIB']['meta_info']
_meta_table['QBRIDGEMIB.Dot1vProtocolGroupTable']['meta_info'].parent =_meta_table['QBRIDGEMIB']['meta_info']
_meta_table['QBRIDGEMIB.Dot1vProtocolPortTable']['meta_info'].parent =_meta_table['QBRIDGEMIB']['meta_info']
