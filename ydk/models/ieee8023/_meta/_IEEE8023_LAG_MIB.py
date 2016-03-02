


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'ChurnState_Enum' : _MetaInfoEnum('ChurnState_Enum', 'ydk.models.ieee8023.IEEE8023_LAG_MIB',
        {
            'noChurn':'NOCHURN',
            'churn':'CHURN',
            'churnMonitor':'CHURNMONITOR',
        }, 'IEEE8023-LAG-MIB', _yang_ns._namespaces['IEEE8023-LAG-MIB']),
    'IEEE8023LAGMIB.Dot3adAggPortDebugTable.Dot3adAggPortDebugEntry.Dot3adAggPortDebugMuxState_Enum' : _MetaInfoEnum('Dot3adAggPortDebugMuxState_Enum', 'ydk.models.ieee8023.IEEE8023_LAG_MIB',
        {
            'detached':'DETACHED',
            'waiting':'WAITING',
            'attached':'ATTACHED',
            'collecting':'COLLECTING',
            'distributing':'DISTRIBUTING',
            'collectingDistributing':'COLLECTINGDISTRIBUTING',
        }, 'IEEE8023-LAG-MIB', _yang_ns._namespaces['IEEE8023-LAG-MIB']),
    'IEEE8023LAGMIB.Dot3adAggPortDebugTable.Dot3adAggPortDebugEntry.Dot3adAggPortDebugRxState_Enum' : _MetaInfoEnum('Dot3adAggPortDebugRxState_Enum', 'ydk.models.ieee8023.IEEE8023_LAG_MIB',
        {
            'currentRx':'CURRENTRX',
            'expired':'EXPIRED',
            'defaulted':'DEFAULTED',
            'initialize':'INITIALIZE',
            'lacpDisabled':'LACPDISABLED',
            'portDisabled':'PORTDISABLED',
        }, 'IEEE8023-LAG-MIB', _yang_ns._namespaces['IEEE8023-LAG-MIB']),
    'IEEE8023LAGMIB.Dot3adAggPortDebugTable.Dot3adAggPortDebugEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8023LAGMIB.Dot3adAggPortDebugTable.Dot3adAggPortDebugEntry',
            False, 
            [
            _MetaInfoClassMember('dot3adAggPortIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'dot3adaggportindex',
                'IEEE8023-LAG-MIB', True),
            _MetaInfoClassMember('dot3adAggPortDebugActorChangeCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Count of the number of times the Actor's perception of
                the LAG ID for this Aggregation Port has changed.
                This value is read-only.
                ''',
                'dot3adaggportdebugactorchangecount',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortDebugActorChurnCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Count of the number of times the Actor Churn state
                machine has entered the ACTOR_CHURN state.
                This value is read-only.
                ''',
                'dot3adaggportdebugactorchurncount',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortDebugActorChurnState', REFERENCE_ENUM_CLASS, 'ChurnState_Enum' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'ChurnState_Enum', 
                [], [], 
                '''                The state of the Actor Churn Detection machine
                (43.4.17) for the Aggregation Port. A value of `noChurn'
                indicates that the state machine is in either the
                NO_ACTOR_CHURN or the ACTOR_CHURN_MONITOR state, and
                `churn' indicates that the state machine is in the
                ACTOR_CHURN state. This value is read-only.
                ''',
                'dot3adaggportdebugactorchurnstate',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortDebugActorSyncTransitionCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Count of the number of times the Actor's Mux state
                machine (43.4.15) has entered the IN_SYNC state.
                This value is read-only.
                ''',
                'dot3adaggportdebugactorsynctransitioncount',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortDebugLastRxTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of aTimeSinceSystemReset (F.2.1) when
                the last LACPDU was received by this Aggregation Port.
                This value is read-only.
                ''',
                'dot3adaggportdebuglastrxtime',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortDebugMuxReason', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                A human-readable text string indicating the reason
                for the most recent change of Mux machine state.
                This value is read-only.
                ''',
                'dot3adaggportdebugmuxreason',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortDebugMuxState', REFERENCE_ENUM_CLASS, 'Dot3adAggPortDebugMuxState_Enum' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'IEEE8023LAGMIB.Dot3adAggPortDebugTable.Dot3adAggPortDebugEntry.Dot3adAggPortDebugMuxState_Enum', 
                [], [], 
                '''                This attribute holds the value `detached' if the Mux
                state machine (43.4.14) for the Aggregation Port is in
                the DETACHED state, `waiting' if the Mux state machine
                is in the WAITING state, `attached' if the Mux state
                machine for the Aggregation Port is in the ATTACHED
                state, `collecting' if the Mux state machine for the
                Aggregation Port is in the COLLECTING state,
                `distributing' if the Mux state machine for the
                Aggregation Port is in the DISTRIBUTING state, and
                `collectingDistributing' if the Mux state machine for
                the Aggregation Port is in the COLLECTING_DISTRIBUTING
                state. This value is read-only.
                ''',
                'dot3adaggportdebugmuxstate',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortDebugPartnerChangeCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Count of the number of times the Partner's perception
                of the LAG ID (see 43.3.6.1) for this Aggregation Port
                has changed. This value is read-only.
                ''',
                'dot3adaggportdebugpartnerchangecount',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortDebugPartnerChurnCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Count of the number of times the Partner Churn
                state machine has entered the PARTNER_CHURN state.
                This value is read-only.
                ''',
                'dot3adaggportdebugpartnerchurncount',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortDebugPartnerChurnState', REFERENCE_ENUM_CLASS, 'ChurnState_Enum' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'ChurnState_Enum', 
                [], [], 
                '''                The state of the Partner Churn Detection machine
                (43.4.17) for the Aggregation Port. A value of `noChurn'
                indicates that the state machine is in either the
                NO_PARTNER_CHURN or the PARTNER_CHURN_MONITOR state, and
                `churn' indicates that the state machine is in the
                PARTNER_CHURN state. This value is read-only.
                ''',
                'dot3adaggportdebugpartnerchurnstate',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortDebugPartnerSyncTransitionCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Count of the number of times the Partner's Mux
                state machine (43.4.15) has entered the IN_SYNC state.
                This value is read-only.
                ''',
                'dot3adaggportdebugpartnersynctransitioncount',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortDebugRxState', REFERENCE_ENUM_CLASS, 'Dot3adAggPortDebugRxState_Enum' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'IEEE8023LAGMIB.Dot3adAggPortDebugTable.Dot3adAggPortDebugEntry.Dot3adAggPortDebugRxState_Enum', 
                [], [], 
                '''                This attribute holds the value `currentRx' if the
                Receive state machine for the Aggregation Port is in the
                CURRENT state, `expired' if the Receive state machine is
                in the EXPIRED state, `defaulted' if the Receive state
                machine is in the DEFAULTED state, `initialize' if the
                Receive state machine is in the INITIALIZE state,
                `lacpDisabled' if the Receive state machine is in the
                LACP_DISABLED state, or `portDisabled' if the Receive
                state machine is in the PORT_DISABLED state.
                This value is read-only.
                ''',
                'dot3adaggportdebugrxstate',
                'IEEE8023-LAG-MIB', False),
            ],
            'IEEE8023-LAG-MIB',
            'dot3adAggPortDebugEntry',
            _yang_ns._namespaces['IEEE8023-LAG-MIB'],
        'ydk.models.ieee8023.IEEE8023_LAG_MIB'
        ),
    },
    'IEEE8023LAGMIB.Dot3adAggPortDebugTable' : {
        'meta_info' : _MetaInfoClass('IEEE8023LAGMIB.Dot3adAggPortDebugTable',
            False, 
            [
            _MetaInfoClassMember('dot3adAggPortDebugEntry', REFERENCE_LIST, 'Dot3adAggPortDebugEntry' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'IEEE8023LAGMIB.Dot3adAggPortDebugTable.Dot3adAggPortDebugEntry', 
                [], [], 
                '''                A list of the debug parameters for a port.
                ''',
                'dot3adaggportdebugentry',
                'IEEE8023-LAG-MIB', False),
            ],
            'IEEE8023-LAG-MIB',
            'dot3adAggPortDebugTable',
            _yang_ns._namespaces['IEEE8023-LAG-MIB'],
        'ydk.models.ieee8023.IEEE8023_LAG_MIB'
        ),
    },
    'IEEE8023LAGMIB.Dot3adAggPortListTable.Dot3adAggPortListEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8023LAGMIB.Dot3adAggPortListTable.Dot3adAggPortListEntry',
            False, 
            [
            _MetaInfoClassMember('dot3adAggIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'dot3adaggindex',
                'IEEE8023-LAG-MIB', True),
            _MetaInfoClassMember('clagAggPortListPorts', ATTRIBUTE, 'str' , None, None, 
                [(2, 256)], [], 
                '''                This object contains a list of ports currently associated
                with this Aggregator in the format of
                '[number_of_ports][cieIfDot1dBaseMappingPort1][...]
                 [cieIfDot1dBaseMappingPortn]'
                
                where
                [number_of_ports] is of size 2 octet and indicates
                the number of ports contains in this object. It
                also indicates the number of cieIfDot1dBaseMappingPort field
                following this field. 
                
                [cieIfDot1dBaseMappingPort'n'] is the value of 
                cieIfDot1dBaseMappingPort of the 'n' port associated with this
                Aggregation and has size of 2 octets where n is up to
                [number_of_ports].
                ''',
                'clagaggportlistports',
                'CISCO-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortListPorts', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The complete set of ports currently associated with
                this Aggregator.  Each bit set in this list represents
                an Actor Port member of this Link Aggregation.
                ''',
                'dot3adaggportlistports',
                'IEEE8023-LAG-MIB', False),
            ],
            'IEEE8023-LAG-MIB',
            'dot3adAggPortListEntry',
            _yang_ns._namespaces['IEEE8023-LAG-MIB'],
        'ydk.models.ieee8023.IEEE8023_LAG_MIB'
        ),
    },
    'IEEE8023LAGMIB.Dot3adAggPortListTable' : {
        'meta_info' : _MetaInfoClass('IEEE8023LAGMIB.Dot3adAggPortListTable',
            False, 
            [
            _MetaInfoClassMember('dot3adAggPortListEntry', REFERENCE_LIST, 'Dot3adAggPortListEntry' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'IEEE8023LAGMIB.Dot3adAggPortListTable.Dot3adAggPortListEntry', 
                [], [], 
                '''                A list of the ports associated with a given Aggregator.
                This is indexed by the ifIndex of the Aggregator.
                ''',
                'dot3adaggportlistentry',
                'IEEE8023-LAG-MIB', False),
            ],
            'IEEE8023-LAG-MIB',
            'dot3adAggPortListTable',
            _yang_ns._namespaces['IEEE8023-LAG-MIB'],
        'ydk.models.ieee8023.IEEE8023_LAG_MIB'
        ),
    },
    'IEEE8023LAGMIB.Dot3adAggPortStatsTable.Dot3adAggPortStatsEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8023LAGMIB.Dot3adAggPortStatsTable.Dot3adAggPortStatsEntry',
            False, 
            [
            _MetaInfoClassMember('dot3adAggPortIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'dot3adaggportindex',
                'IEEE8023-LAG-MIB', True),
            _MetaInfoClassMember('dot3adAggPortStatsIllegalRx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of frames received that carry the Slow
                Protocols Ethernet Type value (43B.4), but contain a
                badly formed PDU or an illegal value of Protocol Subtype
                (43B.4). This value is read-only.
                ''',
                'dot3adaggportstatsillegalrx',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortStatsLACPDUsRx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of valid LACPDUs received on this
                Aggregation Port. This value is read-only.
                ''',
                'dot3adaggportstatslacpdusrx',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortStatsLACPDUsTx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of LACPDUs transmitted on this
                Aggregation Port. This value is read-only.
                ''',
                'dot3adaggportstatslacpdustx',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortStatsMarkerPDUsRx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of valid Marker PDUs received on this
                Aggregation Port. This value is read-only.
                ''',
                'dot3adaggportstatsmarkerpdusrx',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortStatsMarkerPDUsTx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Marker PDUs transmitted on this
                Aggregation Port. This value is read-only.
                ''',
                'dot3adaggportstatsmarkerpdustx',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortStatsMarkerResponsePDUsRx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of valid Marker Response PDUs received on
                this Aggregation Port. This value is read-only.
                ''',
                'dot3adaggportstatsmarkerresponsepdusrx',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortStatsMarkerResponsePDUsTx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of Marker Response PDUs transmitted
                on this Aggregation Port. This value is read-only.
                ''',
                'dot3adaggportstatsmarkerresponsepdustx',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortStatsUnknownRx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of frames received that either:
                - carry the Slow Protocols Ethernet Type value (43B.4),
                  but contain an unknown PDU,  or:
                - are addressed to the Slow Protocols group MAC
                  Address (43B.3), but do not carry the Slow Protocols
                  Ethernet Type.
                This value is read-only.
                ''',
                'dot3adaggportstatsunknownrx',
                'IEEE8023-LAG-MIB', False),
            ],
            'IEEE8023-LAG-MIB',
            'dot3adAggPortStatsEntry',
            _yang_ns._namespaces['IEEE8023-LAG-MIB'],
        'ydk.models.ieee8023.IEEE8023_LAG_MIB'
        ),
    },
    'IEEE8023LAGMIB.Dot3adAggPortStatsTable' : {
        'meta_info' : _MetaInfoClass('IEEE8023LAGMIB.Dot3adAggPortStatsTable',
            False, 
            [
            _MetaInfoClassMember('dot3adAggPortStatsEntry', REFERENCE_LIST, 'Dot3adAggPortStatsEntry' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'IEEE8023LAGMIB.Dot3adAggPortStatsTable.Dot3adAggPortStatsEntry', 
                [], [], 
                '''                A list of Link Aggregation Control Protocol statistics
                for each port on this device.
                ''',
                'dot3adaggportstatsentry',
                'IEEE8023-LAG-MIB', False),
            ],
            'IEEE8023-LAG-MIB',
            'dot3adAggPortStatsTable',
            _yang_ns._namespaces['IEEE8023-LAG-MIB'],
        'ydk.models.ieee8023.IEEE8023_LAG_MIB'
        ),
    },
    'IEEE8023LAGMIB.Dot3adAggPortTable.Dot3adAggPortEntry.ClagAggPortRate_Enum' : _MetaInfoEnum('ClagAggPortRate_Enum', 'ydk.models.ieee8023.IEEE8023_LAG_MIB',
        {
            'fast':'FAST',
            'normal':'NORMAL',
        }, 'CISCO-LAG-MIB', _yang_ns._namespaces['CISCO-LAG-MIB']),
    'IEEE8023LAGMIB.Dot3adAggPortTable.Dot3adAggPortEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8023LAGMIB.Dot3adAggPortTable.Dot3adAggPortEntry',
            False, 
            [
            _MetaInfoClassMember('dot3adAggPortIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The ifIndex of the port
                ''',
                'dot3adaggportindex',
                'IEEE8023-LAG-MIB', True),
            _MetaInfoClassMember('clagAggPortAdminStatus', REFERENCE_ENUM_CLASS, 'ClagPortAdminStatus_Enum' , 'ydk.models.lag.CISCO_LAG_MIB', 'ClagPortAdminStatus_Enum', 
                [], [], 
                '''                The administrative status of the LACP protocol on this
                aggregation port.
                ''',
                'clagaggportadminstatus',
                'CISCO-LAG-MIB', False),
            _MetaInfoClassMember('clagAggPortRate', REFERENCE_ENUM_CLASS, 'ClagAggPortRate_Enum' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'IEEE8023LAGMIB.Dot3adAggPortTable.Dot3adAggPortEntry.ClagAggPortRate_Enum', 
                [], [], 
                '''                Specifies the requested exchange rate of LACP packets
                on this interface.
                fast(1)  :    The device requests its peers to send LACP packets 
                              at fast rate to this interface.
                normal(2):    The decice requests its peers to send LACP packets
                              at normal rate to this interface.
                ''',
                'clagaggportrate',
                'CISCO-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortActorAdminKey', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The current administrative value of the Key for the
                Aggregation Port. This is a 16-bit read-write value.
                The meaning of particular Key values is of local
                significance.
                ''',
                'dot3adaggportactoradminkey',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortActorAdminState', REFERENCE_BITS, 'LacpState_Bits' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'LacpState_Bits', 
                [], [], 
                '''                A string of 8 bits, corresponding to the administrative
                values of Actor_State (43.4.2) as transmitted by the
                Actor in LACPDUs. The first bit corresponds to bit 0 of
                Actor_State (LACP_Activity),
                the second bit corresponds to bit 1 (LACP_Timeout),
                the third bit corresponds to bit 2 (Aggregation),
                the fourth bit corresponds to bit 3 (Synchronization),
                the fifth bit corresponds to bit 4 (Collecting),
                the sixth bit corresponds to bit 5 (Distributing),
                the seventh bit corresponds to bit 6 (Defaulted),
                and the eighth bit corresponds to bit 7 (Expired).
                These values allow administrative control over the
                values of LACP_Activity, LACP_Timeout and Aggregation.
                This attribute value is read-write.
                ''',
                'dot3adaggportactoradminstate',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortActorOperKey', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The current operational value of the Key for the
                Aggregation Port. This is a 16-bit read-only value.
                The meaning of particular Key values is of local
                significance.
                ''',
                'dot3adaggportactoroperkey',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortActorOperState', REFERENCE_BITS, 'LacpState_Bits' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'LacpState_Bits', 
                [], [], 
                '''                A string of 8 bits, corresponding to the current
                operational values of Actor_State as transmitted by the
                Actor in LACPDUs. The bit allocations are as defined in
                30.7.2.1.20. This attribute value is read-only.
                ''',
                'dot3adaggportactoroperstate',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortActorPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The port number locally assigned to the Aggregation
                Port. The port number is communicated in LACPDUs as the
                Actor_Port. This value is read-only.
                ''',
                'dot3adaggportactorport',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortActorPortPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The priority value assigned to this Aggregation Port.
                This 16-bit value is read-write.
                ''',
                'dot3adaggportactorportpriority',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortActorSystemID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                A 6-octet read-only MAC address value that defines the
                value of the System ID for the System that contains this
                Aggregation Port.
                ''',
                'dot3adaggportactorsystemid',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortActorSystemPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                A 2-octet read-write value used to define the priority
                value associated with the Actor's System ID.
                ''',
                'dot3adaggportactorsystempriority',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortAggregateOrIndividual', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A read-only Boolean value indicating whether the
                Aggregation Port is able to Aggregate (`TRUE') or is
                only able to operate as an Individual link (`FALSE').
                ''',
                'dot3adaggportaggregateorindividual',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortAttachedAggID', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The identifier value of the Aggregator that this
                Aggregation Port is currently attached to. Zero
                indicates that the Aggregation Port is not currently
                attached to an Aggregator.  This value is read-only.
                ''',
                'dot3adaggportattachedaggid',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortPartnerAdminKey', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The current administrative value of the Key for the
                protocol Partner. This is a 16-bit read-write value.
                The assigned value is used, along with the value of
                aAggPortPartnerAdminSystemPriority,
                aAggPortPartnerAdminSystemID, aAggPortPartnerAdminPort,
                and aAggPortPartnerAdminPortPriority, in order to
                achieve manually configured aggregation.
                ''',
                'dot3adaggportpartneradminkey',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortPartnerAdminPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The current administrative value of the port number for
                the protocol Partner. This is a 16-bit read-write value.
                The assigned value is used, along with the value of
                aAggPortPartnerAdminSystemPriority,
                aAggPortPartnerAdminSystemID, aAggPortPartnerAdminKey,
                and aAggPortPartnerAdminPortPriority, in order to
                achieve manually configured aggregation.
                ''',
                'dot3adaggportpartneradminport',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortPartnerAdminPortPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The current administrative value of the port priority
                for the protocol Partner. This is a 16-bit read-write
                value. The assigned value is used, along with the value
                of aAggPortPartnerAdminSystemPriority,
                aAggPortPartnerAdminSystemID, aAggPortPartnerAdminKey,
                and aAggPortPartnerAdminPort, in order to achieve
                manually configured aggregation.
                ''',
                'dot3adaggportpartneradminportpriority',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortPartnerAdminState', REFERENCE_BITS, 'LacpState_Bits' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'LacpState_Bits', 
                [], [], 
                '''                A string of 8 bits, corresponding to the current
                administrative value of Actor_State for the protocol
                Partner. The bit allocations are as defined in
                30.7.2.1.20. This attribute value is read-write. The
                assigned value is used in order to achieve manually
                configured aggregation.
                ''',
                'dot3adaggportpartneradminstate',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortPartnerAdminSystemID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                A 6-octet read-write MACAddress value representing the
                administrative value of the Aggregation Port's protocol
                Partner's System ID. The assigned value is used, along
                with the value of aAggPortPartnerAdminSystemPriority,
                aAggPortPartnerAdminKey, aAggPortPartnerAdminPort, and
                aAggPortPartnerAdminPortPriority, in order to achieve
                manually configured aggregation.
                ''',
                'dot3adaggportpartneradminsystemid',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortPartnerAdminSystemPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                A 2-octet read-write value used to define the
                administrative value of priority associated with the
                Partner's System ID. The assigned value is used, along
                with the value of aAggPortPartnerAdminSystemID,
                aAggPortPartnerAdminKey, aAggPortPartnerAdminPort, and
                aAggPortPartnerAdminPortPriority, in order to achieve
                manually configured aggregation.
                ''',
                'dot3adaggportpartneradminsystempriority',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortPartnerOperKey', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The current operational value of the Key for the
                protocol Partner. The value of this attribute may
                contain the manually configured value carried in
                aAggPortPartnerAdminKey if there is no protocol Partner.
                This is a 16-bit read-only value.
                ''',
                'dot3adaggportpartneroperkey',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortPartnerOperPort', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The operational port number assigned to this
                Aggregation Port by the Aggregation Port's protocol
                Partner. The value of this attribute may contain the
                manually configured value carried in
                aAggPortPartnerAdminPort if there is no protocol
                Partner. This 16-bit value is read-only.
                ''',
                'dot3adaggportpartneroperport',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortPartnerOperPortPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The priority value assigned to this Aggregation Port by
                the Partner. The value of this attribute may contain the
                manually configured value carried in
                aAggPortPartnerAdminPortPriority if there is no protocol
                Partner. This 16-bit value is read-only.
                ''',
                'dot3adaggportpartneroperportpriority',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortPartnerOperState', REFERENCE_BITS, 'LacpState_Bits' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'LacpState_Bits', 
                [], [], 
                '''                A string of 8 bits, corresponding to the current values
                of Actor_State in the most recently received LACPDU
                transmitted by the protocol Partner. The bit allocations
                are as defined in 30.7.2.1.20. In the absence of an
                active protocol Partner, this value may reflect the
                manually configured value aAggPortPartnerAdminState.
                This attribute value is read-only.
                ''',
                'dot3adaggportpartneroperstate',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortPartnerOperSystemID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                A 6-octet read-only MACAddress value representing the
                current value of the Aggregation Port's protocol
                Partner's System ID. A value of zero indicates that
                there is no known protocol Partner. The value of this
                attribute may contain the manually configured value
                carried in aAggPortPartnerAdminSystemID if there is no
                protocol Partner.
                ''',
                'dot3adaggportpartneropersystemid',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortPartnerOperSystemPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                A 2-octet read-only value indicating the operational
                value of priority associated with the Partner's System
                ID. The value of this attribute may contain the manually
                configured value carried in
                aAggPortPartnerAdminSystemPriority if there is no
                protocol Partner.
                ''',
                'dot3adaggportpartneropersystempriority',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortSelectedAggID', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The identifier value of the Aggregator that this
                Aggregation Port has currently selected. Zero indicates
                that the Aggregation Port has not selected an
                Aggregator, either because it is in the process of
                detaching from an Aggregator or because there is no
                suitable Aggregator available for it to select.
                This value is read-only.
                ''',
                'dot3adaggportselectedaggid',
                'IEEE8023-LAG-MIB', False),
            ],
            'IEEE8023-LAG-MIB',
            'dot3adAggPortEntry',
            _yang_ns._namespaces['IEEE8023-LAG-MIB'],
        'ydk.models.ieee8023.IEEE8023_LAG_MIB'
        ),
    },
    'IEEE8023LAGMIB.Dot3adAggPortTable' : {
        'meta_info' : _MetaInfoClass('IEEE8023LAGMIB.Dot3adAggPortTable',
            False, 
            [
            _MetaInfoClassMember('dot3adAggPortEntry', REFERENCE_LIST, 'Dot3adAggPortEntry' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'IEEE8023LAGMIB.Dot3adAggPortTable.Dot3adAggPortEntry', 
                [], [], 
                '''                A list of Link Aggregation Control configuration
                parameters for each Aggregation Port on this device.
                ''',
                'dot3adaggportentry',
                'IEEE8023-LAG-MIB', False),
            ],
            'IEEE8023-LAG-MIB',
            'dot3adAggPortTable',
            _yang_ns._namespaces['IEEE8023-LAG-MIB'],
        'ydk.models.ieee8023.IEEE8023_LAG_MIB'
        ),
    },
    'IEEE8023LAGMIB.Dot3adAggTable.Dot3adAggEntry' : {
        'meta_info' : _MetaInfoClass('IEEE8023LAGMIB.Dot3adAggTable.Dot3adAggEntry',
            False, 
            [
            _MetaInfoClassMember('dot3adAggIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The unique identifier allocated to this Aggregator by
                the local System.  This attribute identifies an
                Aggregator instance among the subordinate managed
                objects of the containing object.
                This value is read-only.
                ''',
                'dot3adaggindex',
                'IEEE8023-LAG-MIB', True),
            _MetaInfoClassMember('dot3adAggActorAdminKey', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The current administrative value of the Key for the
                Aggregator. The administrative Key value may differ from
                the operational Key value for the reasons discussed in
                43.6.2. This is a 16-bit, read-write value. The meaning
                of particular Key values is of local significance.
                ''',
                'dot3adaggactoradminkey',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggActorOperKey', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The current operational value of the Key for the
                Aggregator. The administrative Key value may differ from
                the operational Key value for the reasons discussed in
                43.6.2.  This is a 16-bit read-only value. The meaning
                of particular Key values is of local significance.
                ''',
                'dot3adaggactoroperkey',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggActorSystemID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                A 6-octet read-write MAC address value used as a unique
                identifier for the System that contains this Aggregator.
                NOTE-From the perspective of the Link Aggregation
                mechanisms described in Clause 43, only a single
                combination of Actor's System ID and System Priority are
                considered, and no distinction is made between the
                values of these parameters for an Aggregator and the
                port(s) that are associated with it; i.e., the protocol
                is described in terms of the operation of aggregation
                within a single System. However, the managed objects
                provided for the Aggregator and the port both allow
                management of these parameters. The result of this is to
                permit a single piece of equipment to be configured by
                management to contain more than one System from the
                point of view of the operation of Link Aggregation. This
                may be of particular use in the configuration of
                equipment that has limited aggregation capability (see
                43.6).
                ''',
                'dot3adaggactorsystemid',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggActorSystemPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                A 2-octet read-write value indicating the priority
                value associated with the Actor's System ID.
                ''',
                'dot3adaggactorsystempriority',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggAggregateOrIndividual', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A read-only Boolean value indicating whether the
                Aggregator represents an Aggregate (`TRUE') or
                an Individual link (`FALSE').
                ''',
                'dot3adaggaggregateorindividual',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggCollectorMaxDelay', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The value of this 16-bit read-write attribute defines
                the maximum delay, in tens of microseconds, that may be
                imposed by the Frame Collector between receiving a frame
                from an Aggregator Parser, and either delivering the
                frame to its MAC Client or discarding the frame (see
                43.2.3.1.1).
                ''',
                'dot3adaggcollectormaxdelay',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggMACAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                A 6-octet read-only value carrying the individual
                MAC address assigned to the Aggregator.
                ''',
                'dot3adaggmacaddress',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPartnerOperKey', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The current operational value of the Key for the
                Aggregator's current protocol Partner. This is a 16-bit
                read-only value. If the aggregation is manually
                configured, this Key value will be a value assigned by
                the local System.
                ''',
                'dot3adaggpartneroperkey',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPartnerSystemID', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                A 6-octet read-only MAC address value consisting of the
                unique identifier for the current protocol Partner of
                this Aggregator. A value of zero indicates that there is
                no known Partner. If the aggregation is manually
                configured, this System ID value will be a value
                assigned by the local System.
                ''',
                'dot3adaggpartnersystemid',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPartnerSystemPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                A 2-octet read-only value that indicates the priority
                value associated with the Partner's System ID. If the
                aggregation is manually configured, this System Priority
                value will be a value assigned by the local System.
                ''',
                'dot3adaggpartnersystempriority',
                'IEEE8023-LAG-MIB', False),
            ],
            'IEEE8023-LAG-MIB',
            'dot3adAggEntry',
            _yang_ns._namespaces['IEEE8023-LAG-MIB'],
        'ydk.models.ieee8023.IEEE8023_LAG_MIB'
        ),
    },
    'IEEE8023LAGMIB.Dot3adAggTable' : {
        'meta_info' : _MetaInfoClass('IEEE8023LAGMIB.Dot3adAggTable',
            False, 
            [
            _MetaInfoClassMember('dot3adAggEntry', REFERENCE_LIST, 'Dot3adAggEntry' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'IEEE8023LAGMIB.Dot3adAggTable.Dot3adAggEntry', 
                [], [], 
                '''                A list of the Aggregator parameters. This is indexed
                by the ifIndex of the Aggregator.
                ''',
                'dot3adaggentry',
                'IEEE8023-LAG-MIB', False),
            ],
            'IEEE8023-LAG-MIB',
            'dot3adAggTable',
            _yang_ns._namespaces['IEEE8023-LAG-MIB'],
        'ydk.models.ieee8023.IEEE8023_LAG_MIB'
        ),
    },
    'IEEE8023LAGMIB.LagMIBObjects' : {
        'meta_info' : _MetaInfoClass('IEEE8023LAGMIB.LagMIBObjects',
            False, 
            [
            _MetaInfoClassMember('dot3adTablesLastChanged', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the time of the most recent
                change to the dot3adAggTable, dot3adAggPortListTable, or
                dot3adAggPortTable.
                ''',
                'dot3adtableslastchanged',
                'IEEE8023-LAG-MIB', False),
            ],
            'IEEE8023-LAG-MIB',
            'lagMIBObjects',
            _yang_ns._namespaces['IEEE8023-LAG-MIB'],
        'ydk.models.ieee8023.IEEE8023_LAG_MIB'
        ),
    },
    'IEEE8023LAGMIB' : {
        'meta_info' : _MetaInfoClass('IEEE8023LAGMIB',
            False, 
            [
            _MetaInfoClassMember('dot3adAggPortDebugTable', REFERENCE_CLASS, 'Dot3adAggPortDebugTable' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'IEEE8023LAGMIB.Dot3adAggPortDebugTable', 
                [], [], 
                '''                A table that contains Link Aggregation debug
                information about every port that is associated with
                this device.  A row appears in this table for each
                physical port.
                ''',
                'dot3adaggportdebugtable',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortListTable', REFERENCE_CLASS, 'Dot3adAggPortListTable' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'IEEE8023LAGMIB.Dot3adAggPortListTable', 
                [], [], 
                '''                A table that contains a list of all the ports
                associated with each Aggregator.
                ''',
                'dot3adaggportlisttable',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortStatsTable', REFERENCE_CLASS, 'Dot3adAggPortStatsTable' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'IEEE8023LAGMIB.Dot3adAggPortStatsTable', 
                [], [], 
                '''                A table that contains Link Aggregation information
                about every port that is associated with this device.
                A row appears in this table for each physical port.
                ''',
                'dot3adaggportstatstable',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggPortTable', REFERENCE_CLASS, 'Dot3adAggPortTable' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'IEEE8023LAGMIB.Dot3adAggPortTable', 
                [], [], 
                '''                A table that contains Link Aggregation Control
                configuration information about every
                Aggregation Port associated with this device.
                A row appears in this table for each physical port.
                ''',
                'dot3adaggporttable',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('dot3adAggTable', REFERENCE_CLASS, 'Dot3adAggTable' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'IEEE8023LAGMIB.Dot3adAggTable', 
                [], [], 
                '''                A table that contains information about every
                Aggregator that is associated with this System.
                ''',
                'dot3adaggtable',
                'IEEE8023-LAG-MIB', False),
            _MetaInfoClassMember('lagMIBObjects', REFERENCE_CLASS, 'LagMIBObjects' , 'ydk.models.ieee8023.IEEE8023_LAG_MIB', 'IEEE8023LAGMIB.LagMIBObjects', 
                [], [], 
                '''                ''',
                'lagmibobjects',
                'IEEE8023-LAG-MIB', False),
            ],
            'IEEE8023-LAG-MIB',
            'IEEE8023-LAG-MIB',
            _yang_ns._namespaces['IEEE8023-LAG-MIB'],
        'ydk.models.ieee8023.IEEE8023_LAG_MIB'
        ),
    },
}
_meta_table['IEEE8023LAGMIB.Dot3adAggPortDebugTable.Dot3adAggPortDebugEntry']['meta_info'].parent =_meta_table['IEEE8023LAGMIB.Dot3adAggPortDebugTable']['meta_info']
_meta_table['IEEE8023LAGMIB.Dot3adAggPortListTable.Dot3adAggPortListEntry']['meta_info'].parent =_meta_table['IEEE8023LAGMIB.Dot3adAggPortListTable']['meta_info']
_meta_table['IEEE8023LAGMIB.Dot3adAggPortStatsTable.Dot3adAggPortStatsEntry']['meta_info'].parent =_meta_table['IEEE8023LAGMIB.Dot3adAggPortStatsTable']['meta_info']
_meta_table['IEEE8023LAGMIB.Dot3adAggPortTable.Dot3adAggPortEntry']['meta_info'].parent =_meta_table['IEEE8023LAGMIB.Dot3adAggPortTable']['meta_info']
_meta_table['IEEE8023LAGMIB.Dot3adAggTable.Dot3adAggEntry']['meta_info'].parent =_meta_table['IEEE8023LAGMIB.Dot3adAggTable']['meta_info']
_meta_table['IEEE8023LAGMIB.Dot3adAggPortDebugTable']['meta_info'].parent =_meta_table['IEEE8023LAGMIB']['meta_info']
_meta_table['IEEE8023LAGMIB.Dot3adAggPortListTable']['meta_info'].parent =_meta_table['IEEE8023LAGMIB']['meta_info']
_meta_table['IEEE8023LAGMIB.Dot3adAggPortStatsTable']['meta_info'].parent =_meta_table['IEEE8023LAGMIB']['meta_info']
_meta_table['IEEE8023LAGMIB.Dot3adAggPortTable']['meta_info'].parent =_meta_table['IEEE8023LAGMIB']['meta_info']
_meta_table['IEEE8023LAGMIB.Dot3adAggTable']['meta_info'].parent =_meta_table['IEEE8023LAGMIB']['meta_info']
_meta_table['IEEE8023LAGMIB.LagMIBObjects']['meta_info'].parent =_meta_table['IEEE8023LAGMIB']['meta_info']
