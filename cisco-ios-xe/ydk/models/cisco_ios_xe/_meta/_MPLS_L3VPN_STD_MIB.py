


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Mplsl3VpnrttypeEnum' : _MetaInfoEnum('Mplsl3VpnrttypeEnum', 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB',
        {
            'import':'import_',
            'export':'export',
            'both':'both',
        }, 'MPLS-L3VPN-STD-MIB', _yang_ns._namespaces['MPLS-L3VPN-STD-MIB']),
    'MplsL3VpnStdMib.Mplsl3Vpnscalars' : {
        'meta_info' : _MetaInfoClass('MplsL3VpnStdMib.Mplsl3Vpnscalars',
            False, 
            [
            _MetaInfoClassMember('mplsL3VpnActiveVrfs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of VRFs that are active on this node.
                That is, those VRFs whose corresponding mplsL3VpnVrfOperStatus
                object value is equal to operational (1).
                ''',
                'mplsl3vpnactivevrfs',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnConfiguredVrfs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of VRFs that are configured on this node.
                ''',
                'mplsl3vpnconfiguredvrfs',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnConnectedInterfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of interfaces connected to a VRF.
                ''',
                'mplsl3vpnconnectedinterfaces',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnIllLblRcvThrsh', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of illegally received labels above which
                the mplsNumVrfSecIllglLblThrshExcd notification
                is issued.  The persistence of this value mimics
                that of the device's configuration.
                ''',
                'mplsl3vpnilllblrcvthrsh',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnNotificationEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this object is true, then it enables the
                generation of all notifications defined in
                this MIB.  This object's value should be
                preserved across agent reboots.
                ''',
                'mplsl3vpnnotificationenable',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfConfMaxPossRts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Denotes maximum number of routes that the device
                will allow all VRFs jointly to hold.  If this value is
                set to 0, this indicates that the device is
                unable to determine the absolute maximum.  In this
                case, the configured maximum MAY not actually
                be allowed by the device.
                ''',
                'mplsl3vpnvrfconfmaxpossrts',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfConfRteMxThrshTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Denotes the interval in seconds, at which the route max threshold
                notification may be reissued after the maximum value has been
                exceeded (or has been reached if mplsL3VpnVrfConfMaxRoutes and
                mplsL3VpnVrfConfHighRteThresh are equal) and the initial
                notification has been issued.  This value is intended to prevent
                continuous generation of notifications by an agent in the event
                that routes are continually added to a VRF after it has reached
                its maximum value.  If this value is set to 0, the agent should
                only issue a single notification at the time that the maximum
                threshold has been reached, and should not issue any more
                notifications until the value of routes has fallen below the
                configured threshold value.  This is the recommended default
                behavior.
                ''',
                'mplsl3vpnvrfconfrtemxthrshtime',
                'MPLS-L3VPN-STD-MIB', False),
            ],
            'MPLS-L3VPN-STD-MIB',
            'mplsL3VpnScalars',
            _yang_ns._namespaces['MPLS-L3VPN-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB'
        ),
    },
    'MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry.Mplsl3VpnifvpnclassificationEnum' : _MetaInfoEnum('Mplsl3VpnifvpnclassificationEnum', 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB',
        {
            'carrierOfCarrier':'carrierOfCarrier',
            'enterprise':'enterprise',
            'interProvider':'interProvider',
        }, 'MPLS-L3VPN-STD-MIB', _yang_ns._namespaces['MPLS-L3VPN-STD-MIB']),
    'MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry' : {
        'meta_info' : _MetaInfoClass('MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry',
            False, 
            [
            _MetaInfoClassMember('mplsL3VpnVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                ''',
                'mplsl3vpnvrfname',
                'MPLS-L3VPN-STD-MIB', True),
            _MetaInfoClassMember('mplsL3VpnIfConfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This is a unique index for an entry in the
                mplsL3VpnIfConfTable.  A non-zero index for an
                entry indicates the ifIndex for the corresponding
                interface entry in the MPLS-VPN-layer in the ifTable.
                Note that this table does not necessarily correspond
                one-to-one with all entries in the Interface MIB
                having an ifType of MPLS-layer; rather, only those
                that are enabled for MPLS L3VPN functionality.
                ''',
                'mplsl3vpnifconfindex',
                'MPLS-L3VPN-STD-MIB', True),
            _MetaInfoClassMember('mplsL3VpnIfConfRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This variable is used to create, modify, and/or
                delete a row in this table.  Rows in this
                table signify that the specified interface is
                associated with this VRF.  If the row creation
                operation succeeds, the interface will have been
                associated with the specified VRF, otherwise the
                agent MUST not allow the association.  If the agent
                only allows read-only operations on this table, it
                MUST create entries in this table as they are created
                on the device.  When a row in this table is in
                active(1) state, no objects in that row can be
                modified except mplsL3VpnIfConfStorageType and
                mplsL3VpnIfConfRowStatus.
                ''',
                'mplsl3vpnifconfrowstatus',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnIfConfStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this VPN If entry.
                Conceptual rows having the value 'permanent'
                need not allow write access to any columnar
                objects in the row.
                ''',
                'mplsl3vpnifconfstoragetype',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnIfVpnClassification', REFERENCE_ENUM_CLASS, 'Mplsl3VpnifvpnclassificationEnum' , 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB', 'MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry.Mplsl3VpnifvpnclassificationEnum', 
                [], [], 
                '''                Denotes whether this link participates in a
                carrier's carrier, enterprise, or inter-provider
                scenario.
                ''',
                'mplsl3vpnifvpnclassification',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnIfVpnRouteDistProtocol', REFERENCE_BITS, 'Mplsl3Vpnifvpnroutedistprotocol' , 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB', 'MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry.Mplsl3Vpnifvpnroutedistprotocol', 
                [], [], 
                '''                Denotes the route distribution protocol across the
                PE-CE link.  Note that more than one routing protocol
                may be enabled at the same time; thus, this object is
                specified as a bitmask.  For example, static(5) and
                ospf(2) are a typical configuration.
                ''',
                'mplsl3vpnifvpnroutedistprotocol',
                'MPLS-L3VPN-STD-MIB', False),
            ],
            'MPLS-L3VPN-STD-MIB',
            'mplsL3VpnIfConfEntry',
            _yang_ns._namespaces['MPLS-L3VPN-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB'
        ),
    },
    'MplsL3VpnStdMib.Mplsl3Vpnifconftable' : {
        'meta_info' : _MetaInfoClass('MplsL3VpnStdMib.Mplsl3Vpnifconftable',
            False, 
            [
            _MetaInfoClassMember('mplsL3VpnIfConfEntry', REFERENCE_LIST, 'Mplsl3Vpnifconfentry' , 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB', 'MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry', 
                [], [], 
                '''                An entry in this table is created by an LSR for
                every interface capable of supporting MPLS L3VPN.
                Each entry in this table is meant to correspond to
                an entry in the Interfaces Table.
                ''',
                'mplsl3vpnifconfentry',
                'MPLS-L3VPN-STD-MIB', False),
            ],
            'MPLS-L3VPN-STD-MIB',
            'mplsL3VpnIfConfTable',
            _yang_ns._namespaces['MPLS-L3VPN-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB'
        ),
    },
    'MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry.Mplsl3VpnvrfconfadminstatusEnum' : _MetaInfoEnum('Mplsl3VpnvrfconfadminstatusEnum', 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB',
        {
            'up':'up',
            'down':'down',
            'testing':'testing',
        }, 'MPLS-L3VPN-STD-MIB', _yang_ns._namespaces['MPLS-L3VPN-STD-MIB']),
    'MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry.Mplsl3VpnvrfoperstatusEnum' : _MetaInfoEnum('Mplsl3VpnvrfoperstatusEnum', 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB',
        {
            'up':'up',
            'down':'down',
        }, 'MPLS-L3VPN-STD-MIB', _yang_ns._namespaces['MPLS-L3VPN-STD-MIB']),
    'MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry' : {
        'meta_info' : _MetaInfoClass('MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry',
            False, 
            [
            _MetaInfoClassMember('mplsL3VpnVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                The human-readable name of this VPN.  This MAY
                be equivalent to the [RFC2685] VPN-ID, but may
                also vary.  If it is set to the VPN ID, it MUST
                be equivalent to the value of mplsL3VpnVrfVpnId.
                It is strongly recommended that all sites supporting
                VRFs that are part of the same VPN use the same
                naming convention for VRFs as well as the same VPN
                ID.
                ''',
                'mplsl3vpnvrfname',
                'MPLS-L3VPN-STD-MIB', True),
            _MetaInfoClassMember('mplsL3VpnVrfActiveInterfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of interfaces connected to this VRF with
                ifOperStatus = up(1).
                
                This value should increase when an interface is associated
                with the corresponding VRF and its corresponding ifOperStatus
                is equal to up(1).  If an interface is associated whose
                ifOperStatus is not up(1), then the value is not incremented
                until such time as it transitions to this state.
                
                This value should be decremented when an interface is
                disassociated with a VRF or the corresponding ifOperStatus
                transitions out of the up(1) state to any other state.
                ''',
                'mplsl3vpnvrfactiveinterfaces',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfAssociatedInterfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of interfaces connected to this VRF
                (independent of ifOperStatus type).
                ''',
                'mplsl3vpnvrfassociatedinterfaces',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfConfAdminStatus', REFERENCE_ENUM_CLASS, 'Mplsl3VpnvrfconfadminstatusEnum' , 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB', 'MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry.Mplsl3VpnvrfconfadminstatusEnum', 
                [], [], 
                '''                Indicates the desired operational status of this
                VRF.
                ''',
                'mplsl3vpnvrfconfadminstatus',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfConfHighRteThresh', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Denotes high-level water marker for the number of
                routes that this VRF may hold.
                ''',
                'mplsl3vpnvrfconfhighrtethresh',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfConfLastChanged', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time of the last
                change of this table entry, which includes changes of
                VRF parameters defined in this table or addition or
                deletion of interfaces associated with this VRF.
                ''',
                'mplsl3vpnvrfconflastchanged',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfConfMaxRoutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Denotes maximum number of routes that this VRF is
                configured to hold.  This value MUST be less than or
                equal to mplsL3VpnVrfConfMaxPossRts unless it is set
                to 0.
                ''',
                'mplsl3vpnvrfconfmaxroutes',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfConfMidRteThresh', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Denotes mid-level water marker for the number
                of routes that this VRF may hold.
                ''',
                'mplsl3vpnvrfconfmidrtethresh',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfConfRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This variable is used to create, modify, and/or
                delete a row in this table.
                
                When a row in this table is in active(1) state, no
                objects in that row can be modified except
                mplsL3VpnVrfConfAdminStatus, mplsL3VpnVrfConfRowStatus,
                and mplsL3VpnVrfConfStorageType.
                ''',
                'mplsl3vpnvrfconfrowstatus',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfConfStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this VPN VRF entry.
                Conceptual rows having the value 'permanent'
                need not allow write access to any columnar
                objects in the row.
                ''',
                'mplsl3vpnvrfconfstoragetype',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfCreationTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time at which this VRF entry was created.
                ''',
                'mplsl3vpnvrfcreationtime',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfDescription', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The human-readable description of this VRF.
                ''',
                'mplsl3vpnvrfdescription',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfOperStatus', REFERENCE_ENUM_CLASS, 'Mplsl3VpnvrfoperstatusEnum' , 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB', 'MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry.Mplsl3VpnvrfoperstatusEnum', 
                [], [], 
                '''                Denotes whether or not a VRF is operational.  A VRF is
                up(1) when there is at least one interface associated
                with the VRF whose ifOperStatus is up(1).  A VRF is
                down(2) when:
                a. There does not exist at least one interface whose
                   ifOperStatus is up(1).
                b. There are no interfaces associated with the VRF.
                ''',
                'mplsl3vpnvrfoperstatus',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfPerfCurrNumRoutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of routes currently used by this
                VRF.
                ''',
                'mplsl3vpnvrfperfcurrnumroutes',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfPerfDiscTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion at
                which any one or more of this entry's counters suffered
                a discontinuity.  If no such discontinuities have
                occurred since the last re-initialization of the local
                management subsystem, then this object contains a zero
                value.
                ''',
                'mplsl3vpnvrfperfdisctime',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfPerfRoutesAdded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of routes added to this VPN/VRF
                since the last discontinuity.  Discontinuities in
                the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                mplsL3VpnVrfPerfDiscTime.
                ''',
                'mplsl3vpnvrfperfroutesadded',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfPerfRoutesDeleted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of routes removed from this VPN/VRF.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                mplsL3VpnVrfPerfDiscTime.
                ''',
                'mplsl3vpnvrfperfroutesdeleted',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfPerfRoutesDropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This counter should be incremented when the number of routes
                contained by the specified VRF exceeds or attempts to exceed
                the maximum allowed value as indicated by
                mplsL3VpnVrfMaxRouteThreshold.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                mplsL3VpnVrfPerfDiscTime.
                ''',
                'mplsl3vpnvrfperfroutesdropped',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfRD', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                The route distinguisher for this VRF.
                ''',
                'mplsl3vpnvrfrd',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfSecDiscontinuityTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion at
                which any one or more of this entry's counters suffered
                a discontinuity.  If no such discontinuities have
                occurred since the last re-initialization of the local
                management subsystem, then this object contains a zero
                value.
                ''',
                'mplsl3vpnvrfsecdiscontinuitytime',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfSecIllegalLblVltns', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of illegally received
                labels on this VPN/VRF.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at
                other times as indicated by the value of
                mplsL3VpnVrfSecDiscontinuityTime.
                ''',
                'mplsl3vpnvrfsecillegallblvltns',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfVpnId', ATTRIBUTE, 'str' , None, None, 
                [(0, None), (7, None)], [], 
                '''                The VPN ID as specified in [RFC2685].  If a VPN ID
                has not been specified for this VRF, then this
                variable SHOULD be set to a zero-length OCTET
                STRING.
                ''',
                'mplsl3vpnvrfvpnid',
                'MPLS-L3VPN-STD-MIB', False),
            ],
            'MPLS-L3VPN-STD-MIB',
            'mplsL3VpnVrfEntry',
            _yang_ns._namespaces['MPLS-L3VPN-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB'
        ),
    },
    'MplsL3VpnStdMib.Mplsl3Vpnvrftable' : {
        'meta_info' : _MetaInfoClass('MplsL3VpnStdMib.Mplsl3Vpnvrftable',
            False, 
            [
            _MetaInfoClassMember('mplsL3VpnVrfEntry', REFERENCE_LIST, 'Mplsl3Vpnvrfentry' , 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB', 'MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry', 
                [], [], 
                '''                An entry in this table is created by an LSR for
                every VRF capable of supporting MPLS L3VPN.  The
                indexing provides an ordering of VRFs per-VPN
                interface.
                ''',
                'mplsl3vpnvrfentry',
                'MPLS-L3VPN-STD-MIB', False),
            ],
            'MPLS-L3VPN-STD-MIB',
            'mplsL3VpnVrfTable',
            _yang_ns._namespaces['MPLS-L3VPN-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB'
        ),
    },
    'MplsL3VpnStdMib.Mplsl3Vpnvrfrttable.Mplsl3Vpnvrfrtentry' : {
        'meta_info' : _MetaInfoClass('MplsL3VpnStdMib.Mplsl3Vpnvrfrttable.Mplsl3Vpnvrfrtentry',
            False, 
            [
            _MetaInfoClassMember('mplsL3VpnVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                ''',
                'mplsl3vpnvrfname',
                'MPLS-L3VPN-STD-MIB', True),
            _MetaInfoClassMember('mplsL3VpnVrfRTIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Auxiliary index for route targets configured for a
                particular VRF.
                ''',
                'mplsl3vpnvrfrtindex',
                'MPLS-L3VPN-STD-MIB', True),
            _MetaInfoClassMember('mplsL3VpnVrfRTType', REFERENCE_ENUM_CLASS, 'Mplsl3VpnrttypeEnum' , 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB', 'Mplsl3VpnrttypeEnum', 
                [], [], 
                '''                The route target distribution type.
                ''',
                'mplsl3vpnvrfrttype',
                'MPLS-L3VPN-STD-MIB', True),
            _MetaInfoClassMember('mplsL3VpnVrfRT', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                The route target distribution policy.
                ''',
                'mplsl3vpnvrfrt',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfRTDescr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of the route target.
                ''',
                'mplsl3vpnvrfrtdescr',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfRTRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This variable is used to create, modify, and/or
                delete a row in this table.  When a row in this
                table is in active(1) state, no objects in that row
                can be modified except mplsL3VpnVrfRTRowStatus.
                ''',
                'mplsl3vpnvrfrtrowstatus',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfRTStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this VPN route target (RT) entry.
                Conceptual rows having the value 'permanent'
                need not allow write access to any columnar
                objects in the row.
                ''',
                'mplsl3vpnvrfrtstoragetype',
                'MPLS-L3VPN-STD-MIB', False),
            ],
            'MPLS-L3VPN-STD-MIB',
            'mplsL3VpnVrfRTEntry',
            _yang_ns._namespaces['MPLS-L3VPN-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB'
        ),
    },
    'MplsL3VpnStdMib.Mplsl3Vpnvrfrttable' : {
        'meta_info' : _MetaInfoClass('MplsL3VpnStdMib.Mplsl3Vpnvrfrttable',
            False, 
            [
            _MetaInfoClassMember('mplsL3VpnVrfRTEntry', REFERENCE_LIST, 'Mplsl3Vpnvrfrtentry' , 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB', 'MplsL3VpnStdMib.Mplsl3Vpnvrfrttable.Mplsl3Vpnvrfrtentry', 
                [], [], 
                '''                An entry in this table is created by an LSR for
                each route target configured for a VRF supporting
                a MPLS L3VPN instance.  The indexing provides an
                ordering per-VRF instance.  See [RFC4364] for a
                complete definition of a route target.
                ''',
                'mplsl3vpnvrfrtentry',
                'MPLS-L3VPN-STD-MIB', False),
            ],
            'MPLS-L3VPN-STD-MIB',
            'mplsL3VpnVrfRTTable',
            _yang_ns._namespaces['MPLS-L3VPN-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB'
        ),
    },
    'MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry.Mplsl3VpnvrfrteinetcidrtypeEnum' : _MetaInfoEnum('Mplsl3VpnvrfrteinetcidrtypeEnum', 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB',
        {
            'other':'other',
            'reject':'reject',
            'local':'local',
            'remote':'remote',
            'blackhole':'blackhole',
        }, 'MPLS-L3VPN-STD-MIB', _yang_ns._namespaces['MPLS-L3VPN-STD-MIB']),
    'MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry' : {
        'meta_info' : _MetaInfoClass('MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry',
            False, 
            [
            _MetaInfoClassMember('mplsL3VpnVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                ''',
                'mplsl3vpnvrfname',
                'MPLS-L3VPN-STD-MIB', True),
            _MetaInfoClassMember('mplsL3VpnVrfRteInetCidrDestType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The type of the mplsL3VpnVrfRteInetCidrDest address, as
                defined in the InetAddress MIB.
                
                Only those address types that may appear in an actual
                routing table are allowed as values of this object.
                ''',
                'mplsl3vpnvrfrteinetcidrdesttype',
                'MPLS-L3VPN-STD-MIB', True),
            _MetaInfoClassMember('mplsL3VpnVrfRteInetCidrDest', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The destination IP address of this route.
                
                The type of this address is determined by the value of
                the mplsL3VpnVrfRteInetCidrDestType object.
                
                The values for the index objects
                mplsL3VpnVrfRteInetCidrDest and
                mplsL3VpnVrfRteInetCidrPfxLen must be consistent.  When
                the value of mplsL3VpnVrfRteInetCidrDest is x, then
                the bitwise logical-AND of x with the value of the mask
                formed from the corresponding index object
                mplsL3VpnVrfRteInetCidrPfxLen MUST be
                equal to x.  If not, then the index pair is not
                consistent and an inconsistentName error must be
                returned on SET or CREATE requests.
                ''',
                'mplsl3vpnvrfrteinetcidrdest',
                'MPLS-L3VPN-STD-MIB', True),
            _MetaInfoClassMember('mplsL3VpnVrfRteInetCidrPfxLen', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Indicates the number of leading one bits that form the
                
                mask to be logical-ANDed with the destination address
                before being compared to the value in the
                mplsL3VpnVrfRteInetCidrDest field.
                
                The values for the index objects
                mplsL3VpnVrfRteInetCidrDest and
                mplsL3VpnVrfRteInetCidrPfxLen must be consistent.  When
                the value of mplsL3VpnVrfRteInetCidrDest is x, then the
                bitwise logical-AND of x with the value of the mask
                formed from the corresponding index object
                mplsL3VpnVrfRteInetCidrPfxLen MUST be
                equal to x.  If not, then the index pair is not
                consistent and an inconsistentName error must be
                returned on SET or CREATE requests.
                ''',
                'mplsl3vpnvrfrteinetcidrpfxlen',
                'MPLS-L3VPN-STD-MIB', True),
            _MetaInfoClassMember('mplsL3VpnVrfRteInetCidrPolicy', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object is an opaque object without any defined
                semantics.  Its purpose is to serve as an additional
                index that may delineate between multiple entries to
                the same destination.  The value { 0 0 } shall be used
                as the default value for this object.
                ''',
                'mplsl3vpnvrfrteinetcidrpolicy',
                'MPLS-L3VPN-STD-MIB', True),
            _MetaInfoClassMember('mplsL3VpnVrfRteInetCidrNHopType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The type of the mplsL3VpnVrfRteInetCidrNextHop address,
                as defined in the InetAddress MIB.
                
                Value should be set to unknown(0) for non-remote
                routes.
                
                Only those address types that may appear in an actual
                routing table are allowed as values of this object.
                ''',
                'mplsl3vpnvrfrteinetcidrnhoptype',
                'MPLS-L3VPN-STD-MIB', True),
            _MetaInfoClassMember('mplsL3VpnVrfRteInetCidrNextHop', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                On remote routes, the address of the next system en
                route.  For non-remote routes, a zero-length string.
                The type of this address is determined by the value of
                the mplsL3VpnVrfRteInetCidrNHopType object.
                ''',
                'mplsl3vpnvrfrteinetcidrnexthop',
                'MPLS-L3VPN-STD-MIB', True),
            _MetaInfoClassMember('mplsL3VpnVrfRteInetCidrAge', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of seconds since this route was last updated
                or otherwise determined to be correct.  Note that no
                semantics of 'too old' can be implied except through
                knowledge of the routing protocol by which the route
                was learned.
                ''',
                'mplsl3vpnvrfrteinetcidrage',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfRteInetCidrIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The ifIndex value that identifies the local interface
                through which the next hop of this route should be
                reached.  A value of 0 is valid and represents the
                scenario where no interface is specified.
                ''',
                'mplsl3vpnvrfrteinetcidrifindex',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfRteInetCidrMetric1', ATTRIBUTE, 'int' , None, None, 
                [('-1', '2147483647')], [], 
                '''                The primary routing metric for this route.  The
                semantics of this metric are determined by the
                
                routing protocol specified in the route's
                mplsL3VpnVrfRteInetCidrProto value.  If this
                metric is not used, its value should be set to
                -1.
                ''',
                'mplsl3vpnvrfrteinetcidrmetric1',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfRteInetCidrMetric2', ATTRIBUTE, 'int' , None, None, 
                [('-1', '2147483647')], [], 
                '''                An alternate routing metric for this route.  The
                semantics of this metric are determined by the routing
                protocol specified in the route's
                mplsL3VpnVrfRteInetCidrProto
                value.  If this metric is not used, its value should be
                set to -1.
                ''',
                'mplsl3vpnvrfrteinetcidrmetric2',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfRteInetCidrMetric3', ATTRIBUTE, 'int' , None, None, 
                [('-1', '2147483647')], [], 
                '''                An alternate routing metric for this route.  The
                semantics of this metric are determined by the routing
                protocol specified in the route's
                mplsL3VpnVrfRteInetCidrProto
                value.  If this metric is not used, its value should be
                set to -1.
                ''',
                'mplsl3vpnvrfrteinetcidrmetric3',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfRteInetCidrMetric4', ATTRIBUTE, 'int' , None, None, 
                [('-1', '2147483647')], [], 
                '''                An alternate routing metric for this route.  The
                semantics of this metric are determined by the routing
                protocol specified in the route's
                mplsL3VpnVrfRteInetCidrProto value.  If this metric
                is not used, its value should be set to -1.
                ''',
                'mplsl3vpnvrfrteinetcidrmetric4',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfRteInetCidrMetric5', ATTRIBUTE, 'int' , None, None, 
                [('-1', '2147483647')], [], 
                '''                An alternate routing metric for this route.  The
                semantics of this metric are determined by the routing
                protocol specified in the route's
                mplsL3VpnVrfRteInetCidrProto value.  If this metric is
                not used, its value should be set to -1.
                ''',
                'mplsl3vpnvrfrteinetcidrmetric5',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfRteInetCidrNextHopAS', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Autonomous System Number of the next hop.  The
                semantics of this object are determined by the
                routing protocol specified in the route's
                mplsL3VpnVrfRteInetCidrProto value.  When this
                object is unknown or not relevant, its value should
                be set to zero.
                ''',
                'mplsl3vpnvrfrteinetcidrnexthopas',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfRteInetCidrProto', REFERENCE_ENUM_CLASS, 'IanaiprouteprotocolEnum' , 'ydk.models.cisco_ios_xe.IANA_RTPROTO_MIB', 'IanaiprouteprotocolEnum', 
                [], [], 
                '''                The routing mechanism via which this route was learned.
                Inclusion of values for gateway routing protocols is
                not intended to imply that hosts should support those
                protocols.
                ''',
                'mplsl3vpnvrfrteinetcidrproto',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfRteInetCidrStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The row status variable, used according to row
                installation and removal conventions.
                
                A row entry cannot be modified when the status is
                marked as active(1).
                ''',
                'mplsl3vpnvrfrteinetcidrstatus',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfRteInetCidrType', REFERENCE_ENUM_CLASS, 'Mplsl3VpnvrfrteinetcidrtypeEnum' , 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB', 'MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry.Mplsl3VpnvrfrteinetcidrtypeEnum', 
                [], [], 
                '''                The type of route.  Note that local(3) refers to a
                route for which the next hop is the final destination;
                remote(4) refers to a route for which the next hop is
                not the final destination.
                
                Routes that do not result in traffic forwarding or
                rejection should not be displayed even if the
                implementation keeps them stored internally.
                
                reject(2) refers to a route that, if matched, discards
                the message as unreachable and returns a notification
                (e.g., ICMP error) to the message sender.  This is used
                in some protocols as a means of correctly aggregating
                routes.
                
                blackhole(5) refers to a route that, if matched,
                discards the message silently.
                ''',
                'mplsl3vpnvrfrteinetcidrtype',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfRteXCPointer', ATTRIBUTE, 'str' , None, None, 
                [(1, 24)], [], 
                '''                Index into mplsXCTable that identifies which cross-
                connect entry is associated with this VRF route entry
                by containing the mplsXCIndex of that cross-connect entry.
                The string containing the single-octet 0x00 indicates that
                a label stack is not associated with this route entry.  This
                can be the case because the label bindings have not yet
                been established, or because some change in the agent has
                removed them.
                
                When the label stack associated with this VRF route is created,
                it MUST establish the associated cross-connect
                entry in the mplsXCTable and then set that index to the value
                of this object.  Changes to the cross-connect object in the
                mplsXCTable MUST automatically be reflected in the value of
                this object.  If this object represents a static routing entry,
                then the manager must ensure that this entry is maintained
                consistently in the corresponding mplsXCTable as well.
                ''',
                'mplsl3vpnvrfrtexcpointer',
                'MPLS-L3VPN-STD-MIB', False),
            ],
            'MPLS-L3VPN-STD-MIB',
            'mplsL3VpnVrfRteEntry',
            _yang_ns._namespaces['MPLS-L3VPN-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB'
        ),
    },
    'MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable' : {
        'meta_info' : _MetaInfoClass('MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable',
            False, 
            [
            _MetaInfoClassMember('mplsL3VpnVrfRteEntry', REFERENCE_LIST, 'Mplsl3Vpnvrfrteentry' , 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB', 'MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry', 
                [], [], 
                '''                An entry in this table is created by an LSR for every route
                present configured (either dynamically or statically) within
                the context of a specific VRF capable of supporting MPLS/BGP
                VPN.  The indexing provides an ordering of VRFs per-VPN
                interface.
                
                Implementers need to be aware that there are quite a few
                index objects that together can exceed the size allowed
                for an Object Identifier (OID).  So implementers must make
                sure that OIDs of column instances in this table will have
                no more than 128 sub-identifiers, otherwise they cannot be
                accessed using SNMPv1, SNMPv2c, or SNMPv3.
                ''',
                'mplsl3vpnvrfrteentry',
                'MPLS-L3VPN-STD-MIB', False),
            ],
            'MPLS-L3VPN-STD-MIB',
            'mplsL3VpnVrfRteTable',
            _yang_ns._namespaces['MPLS-L3VPN-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB'
        ),
    },
    'MplsL3VpnStdMib' : {
        'meta_info' : _MetaInfoClass('MplsL3VpnStdMib',
            False, 
            [
            _MetaInfoClassMember('mplsL3VpnIfConfTable', REFERENCE_CLASS, 'Mplsl3Vpnifconftable' , 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB', 'MplsL3VpnStdMib.Mplsl3Vpnifconftable', 
                [], [], 
                '''                This table specifies per-interface MPLS capability
                and associated information.
                ''',
                'mplsl3vpnifconftable',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnScalars', REFERENCE_CLASS, 'Mplsl3Vpnscalars' , 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB', 'MplsL3VpnStdMib.Mplsl3Vpnscalars', 
                [], [], 
                '''                ''',
                'mplsl3vpnscalars',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfRteTable', REFERENCE_CLASS, 'Mplsl3Vpnvrfrtetable' , 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB', 'MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable', 
                [], [], 
                '''                This table specifies per-interface MPLS L3VPN VRF Table
                routing information.  Entries in this table define VRF routing
                entries associated with the specified MPLS/VPN interfaces.  Note
                
                that this table contains both BGP and Interior Gateway Protocol
                IGP routes, as both may appear in the same VRF.
                ''',
                'mplsl3vpnvrfrtetable',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfRTTable', REFERENCE_CLASS, 'Mplsl3Vpnvrfrttable' , 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB', 'MplsL3VpnStdMib.Mplsl3Vpnvrfrttable', 
                [], [], 
                '''                This table specifies per-VRF route target association.
                Each entry identifies a connectivity policy supported
                as part of a VPN.
                ''',
                'mplsl3vpnvrfrttable',
                'MPLS-L3VPN-STD-MIB', False),
            _MetaInfoClassMember('mplsL3VpnVrfTable', REFERENCE_CLASS, 'Mplsl3Vpnvrftable' , 'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB', 'MplsL3VpnStdMib.Mplsl3Vpnvrftable', 
                [], [], 
                '''                This table specifies per-interface MPLS L3VPN
                VRF Table capability and associated information.
                Entries in this table define VRF routing instances
                associated with MPLS/VPN interfaces.  Note that
                multiple interfaces can belong to the same VRF
                instance.  The collection of all VRF instances
                comprises an actual VPN.
                ''',
                'mplsl3vpnvrftable',
                'MPLS-L3VPN-STD-MIB', False),
            ],
            'MPLS-L3VPN-STD-MIB',
            'MPLS-L3VPN-STD-MIB',
            _yang_ns._namespaces['MPLS-L3VPN-STD-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_L3VPN_STD_MIB'
        ),
    },
}
_meta_table['MplsL3VpnStdMib.Mplsl3Vpnifconftable.Mplsl3Vpnifconfentry']['meta_info'].parent =_meta_table['MplsL3VpnStdMib.Mplsl3Vpnifconftable']['meta_info']
_meta_table['MplsL3VpnStdMib.Mplsl3Vpnvrftable.Mplsl3Vpnvrfentry']['meta_info'].parent =_meta_table['MplsL3VpnStdMib.Mplsl3Vpnvrftable']['meta_info']
_meta_table['MplsL3VpnStdMib.Mplsl3Vpnvrfrttable.Mplsl3Vpnvrfrtentry']['meta_info'].parent =_meta_table['MplsL3VpnStdMib.Mplsl3Vpnvrfrttable']['meta_info']
_meta_table['MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable.Mplsl3Vpnvrfrteentry']['meta_info'].parent =_meta_table['MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable']['meta_info']
_meta_table['MplsL3VpnStdMib.Mplsl3Vpnscalars']['meta_info'].parent =_meta_table['MplsL3VpnStdMib']['meta_info']
_meta_table['MplsL3VpnStdMib.Mplsl3Vpnifconftable']['meta_info'].parent =_meta_table['MplsL3VpnStdMib']['meta_info']
_meta_table['MplsL3VpnStdMib.Mplsl3Vpnvrftable']['meta_info'].parent =_meta_table['MplsL3VpnStdMib']['meta_info']
_meta_table['MplsL3VpnStdMib.Mplsl3Vpnvrfrttable']['meta_info'].parent =_meta_table['MplsL3VpnStdMib']['meta_info']
_meta_table['MplsL3VpnStdMib.Mplsl3Vpnvrfrtetable']['meta_info'].parent =_meta_table['MplsL3VpnStdMib']['meta_info']
