


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOIETFFRRMIB.CmplsFrrConstTable.CmplsFrrConstEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFFRRMIB.CmplsFrrConstTable.CmplsFrrConstEntry',
            False, 
            [
            _MetaInfoClassMember('cmplsFrrConstIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                Uniquely identifies an interface for which fast reroute is
                configured. Tabular entries indexed with a 0 value apply to all
                interfaces on this device for which the FRR feature can operate
                on.
                ''',
                'cmplsfrrconstifindex',
                'CISCO-IETF-FRR-MIB', True),
            _MetaInfoClassMember('cmplsFrrConstTunnelIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Uniquely identifies a tunnel for which fast reroute is
                requested.
                ''',
                'cmplsfrrconsttunnelindex',
                'CISCO-IETF-FRR-MIB', True),
            _MetaInfoClassMember('cmplsFrrConstTunnelInstance', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Uniquely identifies an instance of this tunnel for which fast
                reroute is requested.
                ''',
                'cmplsfrrconsttunnelinstance',
                'CISCO-IETF-FRR-MIB', True),
            _MetaInfoClassMember('cmplsFrrConstBandwidth', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This variable represents the bandwidth for detour LSPs of this
                tunnel, in units of thousands of bits per second (Kbps).
                ''',
                'cmplsfrrconstbandwidth',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrConstExclAllAffinity', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                A link satisfies the exclude-all constraint if and only if the
                link contains none of the administrative groups specified in the
                constraint.
                ''',
                'cmplsfrrconstexclallaffinity',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrConstHoldingPrio', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Indicates the holding priority for detour LSP.
                ''',
                'cmplsfrrconstholdingprio',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrConstHopLimit', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The maximum number of hops that the detour LSP may traverse.
                ''',
                'cmplsfrrconsthoplimit',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrConstInclAllAffinity', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                A link satisfies the include-all constraint if and only if the
                link contains all of the administrative groups specified in the
                constraint.
                ''',
                'cmplsfrrconstinclallaffinity',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrConstInclAnyAffinity', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                A link satisfies the include-any constraint if and only if the
                constraint is zero, or the link and the constraint have a
                resource class in common.
                ''',
                'cmplsfrrconstinclanyaffinity',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrConstNumProtectedTunOnIf', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of tunnels protected on this interface.
                ''',
                'cmplsfrrconstnumprotectedtunonif',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrConstNumProtectingTunOnIf', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of backup tunnels protecting the specified
                interface.
                ''',
                'cmplsfrrconstnumprotectingtunonif',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrConstRowStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                This object is used to create, modify, and/or delete a row in
                this table.
                ''',
                'cmplsfrrconstrowstatus',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrConstSetupPrio', ATTRIBUTE, 'int' , None, None, 
                [(0, 7)], [], 
                '''                Indicates the setup priority of detour LSP.
                ''',
                'cmplsfrrconstsetupprio',
                'CISCO-IETF-FRR-MIB', False),
            ],
            'CISCO-IETF-FRR-MIB',
            'cmplsFrrConstEntry',
            _yang_ns._namespaces['CISCO-IETF-FRR-MIB'],
        'ydk.models.ietf.CISCO_IETF_FRR_MIB'
        ),
    },
    'CISCOIETFFRRMIB.CmplsFrrConstTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFFRRMIB.CmplsFrrConstTable',
            False, 
            [
            _MetaInfoClassMember('cmplsFrrConstEntry', REFERENCE_LIST, 'CmplsFrrConstEntry' , 'ydk.models.ietf.CISCO_IETF_FRR_MIB', 'CISCOIETFFRRMIB.CmplsFrrConstTable.CmplsFrrConstEntry', 
                [], [], 
                '''                An entry in this table represents detour LSP or bypass tunnel 
                setup constraints for a tunnel instance to be protected by 
                detour LSPs or a tunnel. Agents must allow entries in this table 
                to be created only for tunnel instances that require fast-reroute.
                Entries indexed with mplsFrrConstIfIndex set to 0 apply to all
                interfaces on this device for which the FRR feature can operate
                on.
                ''',
                'cmplsfrrconstentry',
                'CISCO-IETF-FRR-MIB', False),
            ],
            'CISCO-IETF-FRR-MIB',
            'cmplsFrrConstTable',
            _yang_ns._namespaces['CISCO-IETF-FRR-MIB'],
        'ydk.models.ietf.CISCO_IETF_FRR_MIB'
        ),
    },
    'CISCOIETFFRRMIB.CmplsFrrFacRouteDBTable.CmplsFrrFacRouteDBEntry.CmplsFrrFacRouteProtectedTunStatus_Enum' : _MetaInfoEnum('CmplsFrrFacRouteProtectedTunStatus_Enum', 'ydk.models.ietf.CISCO_IETF_FRR_MIB',
        {
            'active':'ACTIVE',
            'ready':'READY',
            'partial':'PARTIAL',
        }, 'CISCO-IETF-FRR-MIB', _yang_ns._namespaces['CISCO-IETF-FRR-MIB']),
    'CISCOIETFFRRMIB.CmplsFrrFacRouteDBTable.CmplsFrrFacRouteDBEntry.CmplsFrrFacRouteProtectingTunProtectionType_Enum' : _MetaInfoEnum('CmplsFrrFacRouteProtectingTunProtectionType_Enum', 'ydk.models.ietf.CISCO_IETF_FRR_MIB',
        {
            'linkProtection':'LINKPROTECTION',
            'nodeProtection':'NODEPROTECTION',
        }, 'CISCO-IETF-FRR-MIB', _yang_ns._namespaces['CISCO-IETF-FRR-MIB']),
    'CISCOIETFFRRMIB.CmplsFrrFacRouteDBTable.CmplsFrrFacRouteDBEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFFRRMIB.CmplsFrrFacRouteDBTable.CmplsFrrFacRouteDBEntry',
            False, 
            [
            _MetaInfoClassMember('cmplsFrrFacRouteProtectedIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                Uniquely identifies the interface configured for FRR protection.
                ''',
                'cmplsfrrfacrouteprotectedifindex',
                'CISCO-IETF-FRR-MIB', True),
            _MetaInfoClassMember('cmplsFrrFacRouteProtectedTunEgressLSRId', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                Uniquely identifies an mplsTunnelEntry that is
                being protected by FRR.
                ''',
                'cmplsfrrfacrouteprotectedtunegresslsrid',
                'CISCO-IETF-FRR-MIB', True),
            _MetaInfoClassMember('cmplsFrrFacRouteProtectedTunIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Uniquely identifies an mplsTunnelEntry that is
                being protected by FRR.
                ''',
                'cmplsfrrfacrouteprotectedtunindex',
                'CISCO-IETF-FRR-MIB', True),
            _MetaInfoClassMember('cmplsFrrFacRouteProtectedTunIngressLSRId', ATTRIBUTE, 'str' , None, None, 
                [(4, None)], [], 
                '''                Uniquely identifies an mplsTunnelEntry that is
                being protected by FRR.
                ''',
                'cmplsfrrfacrouteprotectedtuningresslsrid',
                'CISCO-IETF-FRR-MIB', True),
            _MetaInfoClassMember('cmplsFrrFacRouteProtectedTunInstance', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Uniquely identifies an mplsTunnelEntry that is
                being protected by FRR.
                ''',
                'cmplsfrrfacrouteprotectedtuninstance',
                'CISCO-IETF-FRR-MIB', True),
            _MetaInfoClassMember('cmplsFrrFacRouteProtectingTunIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Uniquely identifies the mplsTunnelEntry primary index for
                the tunnel head interface designated to protect the 
                interface as specified in the mplsFrrFacRouteIfProtectedIndex
                (and all of the tunnels using this interface).
                ''',
                'cmplsfrrfacrouteprotectingtunindex',
                'CISCO-IETF-FRR-MIB', True),
            _MetaInfoClassMember('cmplsFrrFacRouteProtectedTunStatus', REFERENCE_ENUM_CLASS, 'CmplsFrrFacRouteProtectedTunStatus_Enum' , 'ydk.models.ietf.CISCO_IETF_FRR_MIB', 'CISCOIETFFRRMIB.CmplsFrrFacRouteDBTable.CmplsFrrFacRouteDBEntry.CmplsFrrFacRouteProtectedTunStatus_Enum', 
                [], [], 
                '''                Specifies the state of the protected tunnel.
                
                active  This tunnel's label has been placed in the
                         LFIB and is ready to be applied to incoming
                         packets.
                         
                ready -  This tunnel's label entry has been created but is
                         not yet in the LFIB.
                         
                partial - This tunnel's label entry as not been fully
                          created.
                ''',
                'cmplsfrrfacrouteprotectedtunstatus',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrFacRouteProtectingTunProtectionType', REFERENCE_ENUM_CLASS, 'CmplsFrrFacRouteProtectingTunProtectionType_Enum' , 'ydk.models.ietf.CISCO_IETF_FRR_MIB', 'CISCOIETFFRRMIB.CmplsFrrFacRouteDBTable.CmplsFrrFacRouteDBEntry.CmplsFrrFacRouteProtectingTunProtectionType_Enum', 
                [], [], 
                '''                Indicates type of the resource protection.
                ''',
                'cmplsfrrfacrouteprotectingtunprotectiontype',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrFacRouteProtectingTunResvBw', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Specifies the amount of bandwidth in megabytes per second
                that is actually reserved by the backup tunnel for
                facility backup. This value is repeated here from the MPLS-
                TE MIB because the tunnel entry will reveal the bandwidth
                reserved by the signaling protocol, which is typically 0
                for backup tunnels so as to not over-book bandwidth.
                However, internal reservations are typically made on the
                PLR, thus this value should be revealed here.
                ''',
                'cmplsfrrfacrouteprotectingtunresvbw',
                'CISCO-IETF-FRR-MIB', False),
            ],
            'CISCO-IETF-FRR-MIB',
            'cmplsFrrFacRouteDBEntry',
            _yang_ns._namespaces['CISCO-IETF-FRR-MIB'],
        'ydk.models.ietf.CISCO_IETF_FRR_MIB'
        ),
    },
    'CISCOIETFFRRMIB.CmplsFrrFacRouteDBTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFFRRMIB.CmplsFrrFacRouteDBTable',
            False, 
            [
            _MetaInfoClassMember('cmplsFrrFacRouteDBEntry', REFERENCE_LIST, 'CmplsFrrFacRouteDBEntry' , 'ydk.models.ietf.CISCO_IETF_FRR_MIB', 'CISCOIETFFRRMIB.CmplsFrrFacRouteDBTable.CmplsFrrFacRouteDBEntry', 
                [], [], 
                '''                An entry in the mplsFrrDBTable represents a single protected
                LSP, protected by a backup tunnel and defined for a specific
                protected interface. Note that for brevity, managers should
                consult the mplsTunnelTable present in the MPLS-TE MIB for
                additional information about the protecting and protected
                tunnels, and the ifEntry in the IF-MIB for the protected
                interface.
                ''',
                'cmplsfrrfacroutedbentry',
                'CISCO-IETF-FRR-MIB', False),
            ],
            'CISCO-IETF-FRR-MIB',
            'cmplsFrrFacRouteDBTable',
            _yang_ns._namespaces['CISCO-IETF-FRR-MIB'],
        'ydk.models.ietf.CISCO_IETF_FRR_MIB'
        ),
    },
    'CISCOIETFFRRMIB.CmplsFrrLogTable.CmplsFrrLogEntry.CmplsFrrLogEventType_Enum' : _MetaInfoEnum('CmplsFrrLogEventType_Enum', 'ydk.models.ietf.CISCO_IETF_FRR_MIB',
        {
            'other':'OTHER',
            'protected':'PROTECTED',
        }, 'CISCO-IETF-FRR-MIB', _yang_ns._namespaces['CISCO-IETF-FRR-MIB']),
    'CISCOIETFFRRMIB.CmplsFrrLogTable.CmplsFrrLogEntry' : {
        'meta_info' : _MetaInfoClass('CISCOIETFFRRMIB.CmplsFrrLogTable.CmplsFrrLogEntry',
            False, 
            [
            _MetaInfoClassMember('cmplsFrrLogIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Uniquely identifies a fast reroute event entry.
                ''',
                'cmplsfrrlogindex',
                'CISCO-IETF-FRR-MIB', True),
            _MetaInfoClassMember('cmplsFrrLogEventDuration', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object describes the duration of this event.
                ''',
                'cmplsfrrlogeventduration',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrLogEventReasonString', ATTRIBUTE, 'str' , None, None, 
                [(128, None)], [], 
                '''                This object contains an implementation-specific explanation
                of the event.
                ''',
                'cmplsfrrlogeventreasonstring',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrLogEventTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object provides the amount of time ticks since this
                event occured.
                ''',
                'cmplsfrrlogeventtime',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrLogEventType', REFERENCE_ENUM_CLASS, 'CmplsFrrLogEventType_Enum' , 'ydk.models.ietf.CISCO_IETF_FRR_MIB', 'CISCOIETFFRRMIB.CmplsFrrLogTable.CmplsFrrLogEntry.CmplsFrrLogEventType_Enum', 
                [], [], 
                '''                This object describes what type of fast reroute event
                occured.
                ''',
                'cmplsfrrlogeventtype',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrLogInterface', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                This object indicates which interface was affected by this
                FRR event. This value may be set to 0 if
                mplsFrrConstProtectionMethod is set to oneToOneBackup(0).
                ''',
                'cmplsfrrloginterface',
                'CISCO-IETF-FRR-MIB', False),
            ],
            'CISCO-IETF-FRR-MIB',
            'cmplsFrrLogEntry',
            _yang_ns._namespaces['CISCO-IETF-FRR-MIB'],
        'ydk.models.ietf.CISCO_IETF_FRR_MIB'
        ),
    },
    'CISCOIETFFRRMIB.CmplsFrrLogTable' : {
        'meta_info' : _MetaInfoClass('CISCOIETFFRRMIB.CmplsFrrLogTable',
            False, 
            [
            _MetaInfoClassMember('cmplsFrrLogEntry', REFERENCE_LIST, 'CmplsFrrLogEntry' , 'ydk.models.ietf.CISCO_IETF_FRR_MIB', 'CISCOIETFFRRMIB.CmplsFrrLogTable.CmplsFrrLogEntry', 
                [], [], 
                '''                An entry in this table is created to describe one fast
                reroute event.  Entries in this table are only created and
                destroyed by the agent implementation. The maximum number 
                of entries in this log is governed by the scalar.
                ''',
                'cmplsfrrlogentry',
                'CISCO-IETF-FRR-MIB', False),
            ],
            'CISCO-IETF-FRR-MIB',
            'cmplsFrrLogTable',
            _yang_ns._namespaces['CISCO-IETF-FRR-MIB'],
        'ydk.models.ietf.CISCO_IETF_FRR_MIB'
        ),
    },
    'CISCOIETFFRRMIB.CmplsFrrScalars.CmplsFrrConstProtectionMethod_Enum' : _MetaInfoEnum('CmplsFrrConstProtectionMethod_Enum', 'ydk.models.ietf.CISCO_IETF_FRR_MIB',
        {
            'oneToOneBackup':'ONETOONEBACKUP',
            'facilityBackup':'FACILITYBACKUP',
        }, 'CISCO-IETF-FRR-MIB', _yang_ns._namespaces['CISCO-IETF-FRR-MIB']),
    'CISCOIETFFRRMIB.CmplsFrrScalars' : {
        'meta_info' : _MetaInfoClass('CISCOIETFFRRMIB.CmplsFrrScalars',
            False, 
            [
            _MetaInfoClassMember('cmplsFrrActProtectedIfs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the number of interfaces currently being protected 
                by the FRR feature if mplsFrrConstProtectionMethod is set to
                facilityBackup(1), otherwise this value should return 0 to
                indicate that LSPs traversing any interface may be protected.
                This value MUST be less than or equal to mplsFrrConfIfs.
                ''',
                'cmplsfrractprotectedifs',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrActProtectedLSPs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the number of LSPs currently protected by 
                the FRR feature. If mplsFrrConstProtectionMethod is set 
                to facilityBackup(1)this object MUST return 0.
                ''',
                'cmplsfrractprotectedlsps',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrActProtectedTuns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the number of bypass tunnels indicated in
                mplsFrrConfProtectingTuns whose operStatus
                is up(1) indicating that they are currently protecting
                facilities on this LSR using the FRR feature. This
                object MUST return 0 if mplsFrrConstProtectionMethod 
                is set to facilityBackup(1).
                ''',
                'cmplsfrractprotectedtuns',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrConfProtectingTuns', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the number of bypass tunnels configured to 
                protect facilities on this LSR using the FRR feature 
                if mplsFrrConstProtectionMethod is set to 
                facilityBackup(1), otherwise this value MUST return 
                0.
                ''',
                'cmplsfrrconfprotectingtuns',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrConstProtectionMethod', REFERENCE_ENUM_CLASS, 'CmplsFrrConstProtectionMethod_Enum' , 'ydk.models.ietf.CISCO_IETF_FRR_MIB', 'CISCOIETFFRRMIB.CmplsFrrScalars.CmplsFrrConstProtectionMethod_Enum', 
                [], [], 
                '''                Indicates which protection method is to be used for fast
                reroute. Some devices may require a reboot of their routing
                processors if this variable is changed. An agent which
                does not wish to reboot or modify its FRR mode 
                MUST return an inconsistentValue error. Please 
                consult the device's agent capability statement 
                for more details.
                ''',
                'cmplsfrrconstprotectionmethod',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrDetourIncoming', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of detour LSPs entering the device if
                mplsFrrConstProtectionMethod is set to oneToOneBackup(0), or
                or 0 if mplsFrrConstProtectionMethod is set to
                facilityBackup(1).
                ''',
                'cmplsfrrdetourincoming',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrDetourOriginating', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of detour LSPs originating at this PLR if
                mplsFrrConstProtectionMethod is set to oneToOneBackup(0).
                This object MUST return 0 if the mplsFrrConstProtectionMethod 
                is set to facilityBackup(1).
                ''',
                'cmplsfrrdetouroriginating',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrDetourOutgoing', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of detour LSPs leaving the device if
                mplsFrrConstProtectionMethod is set to oneToOneBackup(0),
                or 0 if mplsFrrConstProtectionMethod is set to 
                to facilityBackup(1).
                ''',
                'cmplsfrrdetouroutgoing',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrLogTableCurrEntries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the current number of entries in the FRR log
                table.
                ''',
                'cmplsfrrlogtablecurrentries',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrLogTableMaxEntries', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the maximum number of entries allowed in the FRR
                Log table. Agents receiving SETs for values that cannot be
                used must return an inconsistent value error. If a manager
                sets this value to 0, this indicates that no logging should
                take place by the agent.  
                
                If this value is returned as 0, this indicates
                that no additional log entries will be added to the current
                table either because the table has been completely
                filled or logging has been disabled. However, agents
                may wish to not delete existing entries in the log table
                so that managers may review them in the future. 
                
                It is implied that when mplsFrrLogTableCurrEntries 
                has reached the value of this variable, that logging 
                entries may not continue to be added to the table, 
                although existing ones may remain.  Furthermore, an
                agent may begin to delete existing (perhaps the
                oldest entries) entries to make room for new ones.
                ''',
                'cmplsfrrlogtablemaxentries',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrNotifMaxRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This variable indicates the number of milliseconds
                that must elapse between notification emissions. If
                events occur more rapidly, the implementation may
                simply fail to emit these notifications during that
                period, or may queue them until an appropriate
                time in the future. A value of 0 means no minimum 
                elapsed period is specified.
                ''',
                'cmplsfrrnotifmaxrate',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrNotifsEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enables or disables FRR notifications defined in this MIB
                module. Notifications are disabled by default.
                ''',
                'cmplsfrrnotifsenabled',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrNumOfConfIfs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Indicates the number of MPLS interfaces configured for 
                protection by the FRR feature, otherwise this value
                MUST return 0 to indicate that LSPs traversing any 
                interface may be protected.
                ''',
                'cmplsfrrnumofconfifs',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrSwitchover', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of tunnel instances that are switched over to their
                corresponding detour LSP if mplsFrrConstProtectionMethod is set
                to oneToOneBackup(0), or tunnels being switched over if
                mplsFrrConstProtectionMethod is set to facilityBackup(1).
                ''',
                'cmplsfrrswitchover',
                'CISCO-IETF-FRR-MIB', False),
            ],
            'CISCO-IETF-FRR-MIB',
            'cmplsFrrScalars',
            _yang_ns._namespaces['CISCO-IETF-FRR-MIB'],
        'ydk.models.ietf.CISCO_IETF_FRR_MIB'
        ),
    },
    'CISCOIETFFRRMIB' : {
        'meta_info' : _MetaInfoClass('CISCOIETFFRRMIB',
            False, 
            [
            _MetaInfoClassMember('cmplsFrrConstTable', REFERENCE_CLASS, 'CmplsFrrConstTable' , 'ydk.models.ietf.CISCO_IETF_FRR_MIB', 'CISCOIETFFRRMIB.CmplsFrrConstTable', 
                [], [], 
                '''                This table shows detour setup constraints.
                ''',
                'cmplsfrrconsttable',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrFacRouteDBTable', REFERENCE_CLASS, 'CmplsFrrFacRouteDBTable' , 'ydk.models.ietf.CISCO_IETF_FRR_MIB', 'CISCOIETFFRRMIB.CmplsFrrFacRouteDBTable', 
                [], [], 
                '''                The mplsFrrFacRouteDBTable provides information about the 
                fast reroute database.  Each entry belongs to an interface,
                protecting backup tunnel and protected tunnel. MPLS 
                interfaces defined on this node are protected by backup
                tunnels and are indexed by mplsFrrFacRouteProtectedIndex.
                Backup tunnels defined to protect the tunnels traversing an
                interface, and are indexed by 
                mplsFrrFacRouteProtectingTunIndex.  Note that the tunnel 
                instance index is not required, since it is implied to be 0, 
                which indicates the tunnel head interface for the protecting 
                tunnel. The protecting tunnel is defined to exist on the PLR 
                in the FRR specification.  Protected tunnels are the LSPs that 
                traverse the protected link.  These LSPs are uniquely 
                identified by mplsFrrFacRouteProtectedTunIndex,
                mplsFrrFacRouteProtectedTunInstance, 
                mplsFrrFacRouteProtectedTunIngressLSRId, and 
                mplsFrrFacRouteProtectedTunEgressLSRId.
                ''',
                'cmplsfrrfacroutedbtable',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrLogTable', REFERENCE_CLASS, 'CmplsFrrLogTable' , 'ydk.models.ietf.CISCO_IETF_FRR_MIB', 'CISCOIETFFRRMIB.CmplsFrrLogTable', 
                [], [], 
                '''                The fast reroute log table records fast reroute events such
                as protected links going up or down or the FRR feature
                kicking in.
                ''',
                'cmplsfrrlogtable',
                'CISCO-IETF-FRR-MIB', False),
            _MetaInfoClassMember('cmplsFrrScalars', REFERENCE_CLASS, 'CmplsFrrScalars' , 'ydk.models.ietf.CISCO_IETF_FRR_MIB', 'CISCOIETFFRRMIB.CmplsFrrScalars', 
                [], [], 
                '''                ''',
                'cmplsfrrscalars',
                'CISCO-IETF-FRR-MIB', False),
            ],
            'CISCO-IETF-FRR-MIB',
            'CISCO-IETF-FRR-MIB',
            _yang_ns._namespaces['CISCO-IETF-FRR-MIB'],
        'ydk.models.ietf.CISCO_IETF_FRR_MIB'
        ),
    },
}
_meta_table['CISCOIETFFRRMIB.CmplsFrrConstTable.CmplsFrrConstEntry']['meta_info'].parent =_meta_table['CISCOIETFFRRMIB.CmplsFrrConstTable']['meta_info']
_meta_table['CISCOIETFFRRMIB.CmplsFrrFacRouteDBTable.CmplsFrrFacRouteDBEntry']['meta_info'].parent =_meta_table['CISCOIETFFRRMIB.CmplsFrrFacRouteDBTable']['meta_info']
_meta_table['CISCOIETFFRRMIB.CmplsFrrLogTable.CmplsFrrLogEntry']['meta_info'].parent =_meta_table['CISCOIETFFRRMIB.CmplsFrrLogTable']['meta_info']
_meta_table['CISCOIETFFRRMIB.CmplsFrrConstTable']['meta_info'].parent =_meta_table['CISCOIETFFRRMIB']['meta_info']
_meta_table['CISCOIETFFRRMIB.CmplsFrrFacRouteDBTable']['meta_info'].parent =_meta_table['CISCOIETFFRRMIB']['meta_info']
_meta_table['CISCOIETFFRRMIB.CmplsFrrLogTable']['meta_info'].parent =_meta_table['CISCOIETFFRRMIB']['meta_info']
_meta_table['CISCOIETFFRRMIB.CmplsFrrScalars']['meta_info'].parent =_meta_table['CISCOIETFFRRMIB']['meta_info']
