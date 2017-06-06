


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MplsVpnMib.Mplsvpnscalars' : {
        'meta_info' : _MetaInfoClass('MplsVpnMib.Mplsvpnscalars',
            False, 
            [
            _MetaInfoClassMember('mplsVpnActiveVrfs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of VRFs which are active on this node.
                That is, those VRFs whose corresponding mplsVpnVrfOperStatus 
                object value is equal to operational (1).
                ''',
                'mplsvpnactivevrfs',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnConfiguredVrfs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of VRFs which are configured on this node.
                ''',
                'mplsvpnconfiguredvrfs',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnConnectedInterfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of interfaces connected to a VRF.
                ''',
                'mplsvpnconnectedinterfaces',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnNotificationEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this object is true, then it enables the
                generation of all notifications defined in 
                this MIB.
                ''',
                'mplsvpnnotificationenable',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfConfMaxPossibleRoutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Denotes maximum number of routes which the device
                will allow all VRFs jointly to hold. If this value is
                set to 0, this indicates that the device is 
                unable to determine the absolute maximum. In this
                case, the configured maximum MAY not actually
                be allowed by the device.
                ''',
                'mplsvpnvrfconfmaxpossibleroutes',
                'MPLS-VPN-MIB', False),
            ],
            'MPLS-VPN-MIB',
            'mplsVpnScalars',
            _yang_ns._namespaces['MPLS-VPN-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_VPN_MIB'
        ),
    },
    'MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry.MplsvpninterfacelabeledgetypeEnum' : _MetaInfoEnum('MplsvpninterfacelabeledgetypeEnum', 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB',
        {
            'providerEdge':'providerEdge',
            'customerEdge':'customerEdge',
        }, 'MPLS-VPN-MIB', _yang_ns._namespaces['MPLS-VPN-MIB']),
    'MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry.MplsvpninterfacevpnclassificationEnum' : _MetaInfoEnum('MplsvpninterfacevpnclassificationEnum', 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB',
        {
            'carrierOfCarrier':'carrierOfCarrier',
            'enterprise':'enterprise',
            'interProvider':'interProvider',
        }, 'MPLS-VPN-MIB', _yang_ns._namespaces['MPLS-VPN-MIB']),
    'MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry' : {
        'meta_info' : _MetaInfoClass('MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry',
            False, 
            [
            _MetaInfoClassMember('mplsVpnVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                ''',
                'mplsvpnvrfname',
                'MPLS-VPN-MIB', True),
            _MetaInfoClassMember('mplsVpnInterfaceConfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                This is a unique index for an entry in the
                MplsVPNInterfaceConfTable. A non-zero index for an
                entry indicates the ifIndex for the corresponding
                interface entry in the MPLS-VPN-layer in the ifTable.
                Note that this table does not necessarily correspond
                one-to-one with all entries in the Interface MIB
                having an ifType of MPLS-layer; rather, only those
                which are enabled for MPLS/BGP VPN functionality.
                ''',
                'mplsvpninterfaceconfindex',
                'MPLS-VPN-MIB', True),
            _MetaInfoClassMember('mplsVpnInterfaceConfRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The row status for this entry. This value is
                used to create a row in this table, signifying
                that the specified interface is to be associated
                with the specified interface. If this operation
                succeeds, the interface will have been associated,
                otherwise the agent would not allow the association. 
                If the agent only allows read-only operations on
                this table, it will create entries in this table
                as they are created.
                ''',
                'mplsvpninterfaceconfrowstatus',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnInterfaceConfStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this entry.
                ''',
                'mplsvpninterfaceconfstoragetype',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnInterfaceLabelEdgeType', REFERENCE_ENUM_CLASS, 'MplsvpninterfacelabeledgetypeEnum' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry.MplsvpninterfacelabeledgetypeEnum', 
                [], [], 
                '''                Either the providerEdge(0) (PE) or customerEdge(1)
                (CE) bit MUST be set.
                ''',
                'mplsvpninterfacelabeledgetype',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnInterfaceVpnClassification', REFERENCE_ENUM_CLASS, 'MplsvpninterfacevpnclassificationEnum' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry.MplsvpninterfacevpnclassificationEnum', 
                [], [], 
                '''                Denotes whether this link participates in a
                carrier-of-carrier's, enterprise, or inter-provider
                scenario.
                ''',
                'mplsvpninterfacevpnclassification',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnInterfaceVpnRouteDistProtocol', REFERENCE_BITS, 'Mplsvpninterfacevpnroutedistprotocol' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry.Mplsvpninterfacevpnroutedistprotocol', 
                [], [], 
                '''                Denotes the route distribution protocol across the
                PE-CE link. Note that more than one routing protocol
                may be enabled at the same time.
                ''',
                'mplsvpninterfacevpnroutedistprotocol',
                'MPLS-VPN-MIB', False),
            ],
            'MPLS-VPN-MIB',
            'mplsVpnInterfaceConfEntry',
            _yang_ns._namespaces['MPLS-VPN-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_VPN_MIB'
        ),
    },
    'MplsVpnMib.Mplsvpninterfaceconftable' : {
        'meta_info' : _MetaInfoClass('MplsVpnMib.Mplsvpninterfaceconftable',
            False, 
            [
            _MetaInfoClassMember('mplsVpnInterfaceConfEntry', REFERENCE_LIST, 'Mplsvpninterfaceconfentry' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry', 
                [], [], 
                '''                An entry in this table is created by an LSR for
                every interface capable of supporting MPLS/BGP VPN.
                
                
                Each entry in this table is meant to correspond to
                an entry in the Interfaces Table.
                ''',
                'mplsvpninterfaceconfentry',
                'MPLS-VPN-MIB', False),
            ],
            'MPLS-VPN-MIB',
            'mplsVpnInterfaceConfTable',
            _yang_ns._namespaces['MPLS-VPN-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_VPN_MIB'
        ),
    },
    'MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry.MplsvpnvrfoperstatusEnum' : _MetaInfoEnum('MplsvpnvrfoperstatusEnum', 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB',
        {
            'up':'up',
            'down':'down',
        }, 'MPLS-VPN-MIB', _yang_ns._namespaces['MPLS-VPN-MIB']),
    'MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry' : {
        'meta_info' : _MetaInfoClass('MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry',
            False, 
            [
            _MetaInfoClassMember('mplsVpnVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                The human-readable name of this VPN. This MAY
                be equivalent to the RFC2685 VPN-ID.
                ''',
                'mplsvpnvrfname',
                'MPLS-VPN-MIB', True),
            _MetaInfoClassMember('mplsVpnVrfActiveInterfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of interfaces connected to this VRF with 
                
                
                ifOperStatus = up(1). 
                
                This counter should be incremented when:
                
                a. When the ifOperStatus of one of the connected interfaces 
                   changes from down(2) to up(1).
                
                b. When an interface with ifOperStatus = up(1) is connected
                   to this VRF.
                
                This counter should be decremented when:
                
                a. When the ifOperStatus of one of the connected interfaces 
                   changes from up(1) to down(2).
                
                b. When one of the connected interfaces with 
                   ifOperStatus = up(1) gets disconnected from this VRF.
                ''',
                'mplsvpnvrfactiveinterfaces',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfAssociatedInterfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of interfaces connected to this VRF 
                (independent of ifOperStatus type).
                ''',
                'mplsvpnvrfassociatedinterfaces',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfConfHighRouteThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Denotes high-level water marker for the number of
                routes which  this VRF may hold.
                ''',
                'mplsvpnvrfconfhighroutethreshold',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfConfLastChanged', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at the time of the last
                change of this table entry, which includes changes of
                VRF parameters defined in this table or addition or
                deletion of interfaces associated with this VRF.
                ''',
                'mplsvpnvrfconflastchanged',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfConfMaxRoutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Denotes maximum number of routes which this VRF is
                configured to hold. This value MUST be less than or
                equal to mplsVrfMaxPossibleRoutes unless it is set
                to 0.
                ''',
                'mplsvpnvrfconfmaxroutes',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfConfMidRouteThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Denotes mid-level water marker for the number
                of routes which  this VRF may hold.
                ''',
                'mplsvpnvrfconfmidroutethreshold',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfConfRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This variable is used to create, modify, and/or
                delete a row in this table.
                ''',
                'mplsvpnvrfconfrowstatus',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfConfStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this entry.
                ''',
                'mplsvpnvrfconfstoragetype',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfCreationTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time at which this VRF entry was created.
                ''',
                'mplsvpnvrfcreationtime',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfDescription', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The human-readable description of this VRF.
                ''',
                'mplsvpnvrfdescription',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfOperStatus', REFERENCE_ENUM_CLASS, 'MplsvpnvrfoperstatusEnum' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry.MplsvpnvrfoperstatusEnum', 
                [], [], 
                '''                Denotes whether a VRF is operational or not. A VRF is 
                up(1) when at least one interface associated with the
                VRF, which ifOperStatus is up(1). A VRF is down(2) when:
                
                a. There does not exist at least one interface whose
                   ifOperStatus is up(1).
                
                b. There are no interfaces associated with the VRF.
                ''',
                'mplsvpnvrfoperstatus',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfPerfCurrNumRoutes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of routes currently used by this VRF.
                ''',
                'mplsvpnvrfperfcurrnumroutes',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfPerfRoutesAdded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of routes added to this VPN/VRF over the
                coarse of its lifetime.
                ''',
                'mplsvpnvrfperfroutesadded',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfPerfRoutesDeleted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of routes removed from this VPN/VRF.
                ''',
                'mplsvpnvrfperfroutesdeleted',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteDistinguisher', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                The route distinguisher for this VRF.
                ''',
                'mplsvpnvrfroutedistinguisher',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfSecIllegalLabelRcvThresh', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of illegally received labels above which this 
                notification is issued.
                ''',
                'mplsvpnvrfsecillegallabelrcvthresh',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfSecIllegalLabelViolations', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of illegally received labels on this VPN/VRF.
                ''',
                'mplsvpnvrfsecillegallabelviolations',
                'MPLS-VPN-MIB', False),
            ],
            'MPLS-VPN-MIB',
            'mplsVpnVrfEntry',
            _yang_ns._namespaces['MPLS-VPN-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_VPN_MIB'
        ),
    },
    'MplsVpnMib.Mplsvpnvrftable' : {
        'meta_info' : _MetaInfoClass('MplsVpnMib.Mplsvpnvrftable',
            False, 
            [
            _MetaInfoClassMember('mplsVpnVrfEntry', REFERENCE_LIST, 'Mplsvpnvrfentry' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry', 
                [], [], 
                '''                An entry in this table is created by an LSR for
                every VRF capable of supporting MPLS/BGP VPN. The
                indexing provides an ordering of VRFs per-VPN
                interface.
                ''',
                'mplsvpnvrfentry',
                'MPLS-VPN-MIB', False),
            ],
            'MPLS-VPN-MIB',
            'mplsVpnVrfTable',
            _yang_ns._namespaces['MPLS-VPN-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_VPN_MIB'
        ),
    },
    'MplsVpnMib.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry.MplsvpnvrfroutetargettypeEnum' : _MetaInfoEnum('MplsvpnvrfroutetargettypeEnum', 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB',
        {
            'import':'import_',
            'export':'export',
            'both':'both',
        }, 'MPLS-VPN-MIB', _yang_ns._namespaces['MPLS-VPN-MIB']),
    'MplsVpnMib.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry' : {
        'meta_info' : _MetaInfoClass('MplsVpnMib.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry',
            False, 
            [
            _MetaInfoClassMember('mplsVpnVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                ''',
                'mplsvpnvrfname',
                'MPLS-VPN-MIB', True),
            _MetaInfoClassMember('mplsVpnVrfRouteTargetIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Auxiliary index for route-targets configured for a 
                particular VRF.
                ''',
                'mplsvpnvrfroutetargetindex',
                'MPLS-VPN-MIB', True),
            _MetaInfoClassMember('mplsVpnVrfRouteTargetType', REFERENCE_ENUM_CLASS, 'MplsvpnvrfroutetargettypeEnum' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry.MplsvpnvrfroutetargettypeEnum', 
                [], [], 
                '''                The route target export distribution type.
                ''',
                'mplsvpnvrfroutetargettype',
                'MPLS-VPN-MIB', True),
            _MetaInfoClassMember('mplsVpnVrfRouteTarget', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                The route target distribution policy.
                ''',
                'mplsvpnvrfroutetarget',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteTargetDescr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of the route target.
                ''',
                'mplsvpnvrfroutetargetdescr',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteTargetRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                Row status for this entry.
                ''',
                'mplsvpnvrfroutetargetrowstatus',
                'MPLS-VPN-MIB', False),
            ],
            'MPLS-VPN-MIB',
            'mplsVpnVrfRouteTargetEntry',
            _yang_ns._namespaces['MPLS-VPN-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_VPN_MIB'
        ),
    },
    'MplsVpnMib.Mplsvpnvrfroutetargettable' : {
        'meta_info' : _MetaInfoClass('MplsVpnMib.Mplsvpnvrfroutetargettable',
            False, 
            [
            _MetaInfoClassMember('mplsVpnVrfRouteTargetEntry', REFERENCE_LIST, 'Mplsvpnvrfroutetargetentry' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry', 
                [], [], 
                '''                 An entry in this table is created by an LSR for
                each route target configured for a VRF supporting
                a MPLS/BGP VPN instance. The indexing provides an
                ordering per-VRF instance.
                ''',
                'mplsvpnvrfroutetargetentry',
                'MPLS-VPN-MIB', False),
            ],
            'MPLS-VPN-MIB',
            'mplsVpnVrfRouteTargetTable',
            _yang_ns._namespaces['MPLS-VPN-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_VPN_MIB'
        ),
    },
    'MplsVpnMib.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry.MplsvpnvrfbgpnbrroleEnum' : _MetaInfoEnum('MplsvpnvrfbgpnbrroleEnum', 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB',
        {
            'ce':'ce',
            'pe':'pe',
        }, 'MPLS-VPN-MIB', _yang_ns._namespaces['MPLS-VPN-MIB']),
    'MplsVpnMib.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry' : {
        'meta_info' : _MetaInfoClass('MplsVpnMib.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry',
            False, 
            [
            _MetaInfoClassMember('mplsVpnVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                ''',
                'mplsvpnvrfname',
                'MPLS-VPN-MIB', True),
            _MetaInfoClassMember('mplsVpnInterfaceConfIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'mplsvpninterfaceconfindex',
                'MPLS-VPN-MIB', True),
            _MetaInfoClassMember('mplsVpnVrfBgpNbrIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This is a unique tertiary index for an entry in the
                MplsVpnVrfBgpNbrAddrEntry Table.
                ''',
                'mplsvpnvrfbgpnbrindex',
                'MPLS-VPN-MIB', True),
            _MetaInfoClassMember('mplsVpnVrfBgpNbrAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Denotes the EBGP neighbor address.
                ''',
                'mplsvpnvrfbgpnbraddr',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfBgpNbrRole', REFERENCE_ENUM_CLASS, 'MplsvpnvrfbgpnbrroleEnum' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry.MplsvpnvrfbgpnbrroleEnum', 
                [], [], 
                '''                Denotes the role played by this EBGP neighbor
                with respect to this VRF.
                ''',
                'mplsvpnvrfbgpnbrrole',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfBgpNbrRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This variable is used to create, modify, and/or
                delete a row in this table.
                ''',
                'mplsvpnvrfbgpnbrrowstatus',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfBgpNbrStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                The storage type for this entry.
                ''',
                'mplsvpnvrfbgpnbrstoragetype',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfBgpNbrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                Denotes the address family of the PE address.
                ''',
                'mplsvpnvrfbgpnbrtype',
                'MPLS-VPN-MIB', False),
            ],
            'MPLS-VPN-MIB',
            'mplsVpnVrfBgpNbrAddrEntry',
            _yang_ns._namespaces['MPLS-VPN-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_VPN_MIB'
        ),
    },
    'MplsVpnMib.Mplsvpnvrfbgpnbraddrtable' : {
        'meta_info' : _MetaInfoClass('MplsVpnMib.Mplsvpnvrfbgpnbraddrtable',
            False, 
            [
            _MetaInfoClassMember('mplsVpnVrfBgpNbrAddrEntry', REFERENCE_LIST, 'Mplsvpnvrfbgpnbraddrentry' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry', 
                [], [], 
                '''                An entry in this table is created by an LSR for
                every VRF capable of supporting MPLS/BGP VPN. The
                indexing provides an ordering of VRFs per-VPN
                interface.
                ''',
                'mplsvpnvrfbgpnbraddrentry',
                'MPLS-VPN-MIB', False),
            ],
            'MPLS-VPN-MIB',
            'mplsVpnVrfBgpNbrAddrTable',
            _yang_ns._namespaces['MPLS-VPN-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_VPN_MIB'
        ),
    },
    'MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry.MplsvpnvrfbgppathattratomicaggregateEnum' : _MetaInfoEnum('MplsvpnvrfbgppathattratomicaggregateEnum', 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB',
        {
            'lessSpecificRrouteNotSelected':'lessSpecificRrouteNotSelected',
            'lessSpecificRouteSelected':'lessSpecificRouteSelected',
        }, 'MPLS-VPN-MIB', _yang_ns._namespaces['MPLS-VPN-MIB']),
    'MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry.MplsvpnvrfbgppathattrbestEnum' : _MetaInfoEnum('MplsvpnvrfbgppathattrbestEnum', 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB',
        {
            'false':'false',
            'true':'true',
        }, 'MPLS-VPN-MIB', _yang_ns._namespaces['MPLS-VPN-MIB']),
    'MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry.MplsvpnvrfbgppathattroriginEnum' : _MetaInfoEnum('MplsvpnvrfbgppathattroriginEnum', 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB',
        {
            'igp':'igp',
            'egp':'egp',
            'incomplete':'incomplete',
        }, 'MPLS-VPN-MIB', _yang_ns._namespaces['MPLS-VPN-MIB']),
    'MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry' : {
        'meta_info' : _MetaInfoClass('MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry',
            False, 
            [
            _MetaInfoClassMember('mplsVpnVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                ''',
                'mplsvpnvrfname',
                'MPLS-VPN-MIB', True),
            _MetaInfoClassMember('mplsVpnVrfBgpPathAttrIpAddrPrefix', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                An IP address prefix in the Network Layer
                Reachability Information field.  This object
                is an IP address containing the prefix with
                length specified by mplsVpnVrfBgpPathAttrIpAddrPrefixLen.
                Any bits beyond the length specified by
                mplsVpnVrfBgpPathAttrIpAddrPrefixLen are zeroed.
                ''',
                'mplsvpnvrfbgppathattripaddrprefix',
                'MPLS-VPN-MIB', True),
            _MetaInfoClassMember('mplsVpnVrfBgpPathAttrIpAddrPrefixLen', ATTRIBUTE, 'int' , None, None, 
                [('0', '32')], [], 
                '''                Length in bits of the IP address prefix
                in the Network Layer Reachability
                Information field.
                ''',
                'mplsvpnvrfbgppathattripaddrprefixlen',
                'MPLS-VPN-MIB', True),
            _MetaInfoClassMember('mplsVpnVrfBgpPathAttrPeer', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The IP address of the peer where the path
                information was learned.
                ''',
                'mplsvpnvrfbgppathattrpeer',
                'MPLS-VPN-MIB', True),
            _MetaInfoClassMember('mplsVpnVrfBgpPathAttrAggregatorAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The IP address of the last BGP4 speaker
                that performed route aggregation.  A value
                of 0.0.0.0 indicates the absence of this
                attribute.
                ''',
                'mplsvpnvrfbgppathattraggregatoraddr',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfBgpPathAttrAggregatorAS', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The AS number of the last BGP4 speaker that
                performed route aggregation.  A value of
                zero (0) indicates the absence of this
                attribute.
                ''',
                'mplsvpnvrfbgppathattraggregatoras',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfBgpPathAttrASPathSegment', ATTRIBUTE, 'str' , None, None, 
                [(2, 255)], [], 
                '''                The sequence of AS path segments.  Each AS
                path segment is represented by a triple
                <type, length, value>.
                
                 The type is a 1-octet field which has two
                 possible values:
                     1      AS_SET: unordered set of ASs a
                            route in the UPDATE
                            message has traversed
                     2      AS_SEQUENCE: ordered set of ASs
                            a route in the UPDATE
                            message has traversed.
                            The length is a 1-octet field containing the
                
                
                            number of ASs in the value field.
                
                            The value field contains one or more AS
                            numbers, each AS is represented in the octet
                            string as a pair of octets according to the
                            following algorithm:
                
                            first-byte-of-pair = ASNumber / 256;
                            second-byte-of-pair = ASNumber & 255;
                ''',
                'mplsvpnvrfbgppathattraspathsegment',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfBgpPathAttrAtomicAggregate', REFERENCE_ENUM_CLASS, 'MplsvpnvrfbgppathattratomicaggregateEnum' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry.MplsvpnvrfbgppathattratomicaggregateEnum', 
                [], [], 
                '''                Whether or not the local system has
                selected a less specific route without
                selecting a more specific route.
                ''',
                'mplsvpnvrfbgppathattratomicaggregate',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfBgpPathAttrBest', REFERENCE_ENUM_CLASS, 'MplsvpnvrfbgppathattrbestEnum' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry.MplsvpnvrfbgppathattrbestEnum', 
                [], [], 
                '''                An indication of whether or not this route
                was chosen as the best BGP4 route.
                ''',
                'mplsvpnvrfbgppathattrbest',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfBgpPathAttrCalcLocalPref', ATTRIBUTE, 'int' , None, None, 
                [('-1', '2147483647')], [], 
                '''                The degree of preference calculated by the
                receiving BGP4 speaker for an advertised
                route.  A value of -1 indicates the
                absence of this attribute.
                ''',
                'mplsvpnvrfbgppathattrcalclocalpref',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfBgpPathAttrLocalPref', ATTRIBUTE, 'int' , None, None, 
                [('-1', '2147483647')], [], 
                '''                The originating BGP4 speaker's degree of
                preference for an advertised route.  A
                value of -1 indicates the absence of this
                attribute.
                ''',
                'mplsvpnvrfbgppathattrlocalpref',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfBgpPathAttrMultiExitDisc', ATTRIBUTE, 'int' , None, None, 
                [('-1', '2147483647')], [], 
                '''                This metric is used to discriminate
                between multiple exit points to an
                adjacent autonomous system.  A value of -1
                indicates the absence of this attribute.
                ''',
                'mplsvpnvrfbgppathattrmultiexitdisc',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfBgpPathAttrNextHop', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The address of the border router that
                should be used for the destination
                network.
                ''',
                'mplsvpnvrfbgppathattrnexthop',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfBgpPathAttrOrigin', REFERENCE_ENUM_CLASS, 'MplsvpnvrfbgppathattroriginEnum' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry.MplsvpnvrfbgppathattroriginEnum', 
                [], [], 
                '''                The ultimate origin of the path
                information.
                ''',
                'mplsvpnvrfbgppathattrorigin',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfBgpPathAttrUnknown', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                One or more path attributes not understood
                by this BGP4 speaker.  Size zero (0)
                indicates the absence of such
                attribute(s).  Octets beyond the maximum
                size, if any, are not recorded by this
                object.
                ''',
                'mplsvpnvrfbgppathattrunknown',
                'MPLS-VPN-MIB', False),
            ],
            'MPLS-VPN-MIB',
            'mplsVpnVrfBgpNbrPrefixEntry',
            _yang_ns._namespaces['MPLS-VPN-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_VPN_MIB'
        ),
    },
    'MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable' : {
        'meta_info' : _MetaInfoClass('MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable',
            False, 
            [
            _MetaInfoClassMember('mplsVpnVrfBgpNbrPrefixEntry', REFERENCE_LIST, 'Mplsvpnvrfbgpnbrprefixentry' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry', 
                [], [], 
                '''                An entry in this table is created by an LSR for
                every BGP prefix associated with a VRF supporting a 
                MPLS/BGP VPN. The indexing provides an ordering of 
                BGP prefixes per VRF.
                ''',
                'mplsvpnvrfbgpnbrprefixentry',
                'MPLS-VPN-MIB', False),
            ],
            'MPLS-VPN-MIB',
            'mplsVpnVrfBgpNbrPrefixTable',
            _yang_ns._namespaces['MPLS-VPN-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_VPN_MIB'
        ),
    },
    'MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry.MplsvpnvrfrouteprotoEnum' : _MetaInfoEnum('MplsvpnvrfrouteprotoEnum', 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB',
        {
            'other':'other',
            'local':'local',
            'netmgmt':'netmgmt',
            'icmp':'icmp',
            'egp':'egp',
            'ggp':'ggp',
            'hello':'hello',
            'rip':'rip',
            'isIs':'isIs',
            'esIs':'esIs',
            'ciscoIgrp':'ciscoIgrp',
            'bbnSpfIgp':'bbnSpfIgp',
            'ospf':'ospf',
            'bgp':'bgp',
            'idpr':'idpr',
            'ciscoEigrp':'ciscoEigrp',
        }, 'MPLS-VPN-MIB', _yang_ns._namespaces['MPLS-VPN-MIB']),
    'MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry.MplsvpnvrfroutetypeEnum' : _MetaInfoEnum('MplsvpnvrfroutetypeEnum', 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB',
        {
            'other':'other',
            'reject':'reject',
            'local':'local',
            'remote':'remote',
        }, 'MPLS-VPN-MIB', _yang_ns._namespaces['MPLS-VPN-MIB']),
    'MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry' : {
        'meta_info' : _MetaInfoClass('MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry',
            False, 
            [
            _MetaInfoClassMember('mplsVpnVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                ''',
                'mplsvpnvrfname',
                'MPLS-VPN-MIB', True),
            _MetaInfoClassMember('mplsVpnVrfRouteDest', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                The destination IP address of this route.
                This object may not take a Multicast (Class D)
                address value.
                
                Any assignment (implicit or otherwise) of an
                instance of this object to a value x must be
                rejected if the bit-wise logical-AND of x with
                the value of the corresponding instance of the
                mplsVpnVrfRouteMask object is not equal to x.
                ''',
                'mplsvpnvrfroutedest',
                'MPLS-VPN-MIB', True),
            _MetaInfoClassMember('mplsVpnVrfRouteMask', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                Indicate the mask to be logical-ANDed with the
                destination  address  before  being compared to
                the value  in  the  mplsVpnVrfRouteDest field.
                For those  systems  that  do  not support
                arbitrary subnet masks, an agent constructs the
                value of the mplsVpnVrfRouteMask by reference
                
                
                to the IP Address Class.
                
                Any assignment (implicit or otherwise) of an
                instance of this object to a value x must be
                rejected if the bit-wise logical-AND of x with
                the value of the corresponding instance of the
                mplsVpnVrfRouteDest object is not equal to
                mplsVpnVrfRouteDest.
                ''',
                'mplsvpnvrfroutemask',
                'MPLS-VPN-MIB', True),
            _MetaInfoClassMember('mplsVpnVrfRouteTos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The IP TOS Field is used to specify the policy to
                be applied to this route.  The encoding of IP TOS
                is as specified  by  the  following convention.
                Zero indicates the default path if no more
                specific policy applies.
                
                +-----+-----+-----+-----+-----+-----+-----+-----+
                |                 |                       |     |
                |   PRECEDENCE    |    TYPE OF SERVICE    |  0  |
                |                 |                       |     |
                +-----+-----+-----+-----+-----+-----+-----+-----+
                
                           IP TOS                IP TOS
                      Field     Policy      Field     Policy
                      Contents    Code      Contents    Code
                      0 0 0 0  ==>   0      0 0 0 1  ==>   2
                      0 0 1 0  ==>   4      0 0 1 1  ==>   6
                      0 1 0 0  ==>   8      0 1 0 1  ==>  10
                      0 1 1 0  ==>  12      0 1 1 1  ==>  14
                      1 0 0 0  ==>  16      1 0 0 1  ==>  18
                      1 0 1 0  ==>  20      1 0 1 1  ==>  22
                      1 1 0 0  ==>  24      1 1 0 1  ==>  26
                      1 1 1 0  ==>  28      1 1 1 1  ==>  30.
                ''',
                'mplsvpnvrfroutetos',
                'MPLS-VPN-MIB', True),
            _MetaInfoClassMember('mplsVpnVrfRouteNextHop', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                On remote routes, the address of the next
                system en route; Otherwise, 0.0.0.0. .
                ''',
                'mplsvpnvrfroutenexthop',
                'MPLS-VPN-MIB', True),
            _MetaInfoClassMember('mplsVpnVrfRouteAge', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of seconds since this route was
                last updated or otherwise determined to be
                correct. Note that no semantics of `too old'
                can be implied except through knowledge of the
                routing protocol by which the route was
                learned.
                ''',
                'mplsvpnvrfrouteage',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteDestAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The address type of the mplsVpnVrfRouteDest
                entry.
                ''',
                'mplsvpnvrfroutedestaddrtype',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The ifIndex value that identifies the local
                interface  through  which  the next hop of this
                route should be reached.
                ''',
                'mplsvpnvrfrouteifindex',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteInfo', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                A reference to MIB definitions specific to the
                particular routing protocol which is responsi-
                
                
                ble for this route, as determined by the  value
                specified  in the route's mplsVpnVrfRouteProto
                value. If this information is not present, its
                value SHOULD be set to the OBJECT IDENTIFIER
                { 0 0 }, which is a syntactically valid object
                identif-ier, and any implementation conforming
                to ASN.1 and the Basic Encoding Rules must be
                able to generate and recognize this value.
                ''',
                'mplsvpnvrfrouteinfo',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteMaskAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The address type of mplsVpnVrfRouteMask.
                ''',
                'mplsvpnvrfroutemaskaddrtype',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteMetric1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The primary routing metric for this route.
                The semantics of this metric are determined by
                the routing-protocol specified in  the  route's
                mplsVpnVrfRouteProto value. If this metric is not
                used, its value should be set to -1.
                ''',
                'mplsvpnvrfroutemetric1',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteMetric2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                An alternate routing metric for this route.
                The semantics of this metric are determined by
                the routing-protocol specified in  the  route's
                mplsVpnVrfRouteProto value. If this metric is not
                used, its value should be set to -1.
                ''',
                'mplsvpnvrfroutemetric2',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteMetric3', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                An alternate routing metric for this route.
                The semantics of this metric are determined by
                the routing-protocol specified in  the  route's
                mplsVpnVrfRouteProto value. If this metric is not
                used, its value should be set to -1.
                ''',
                'mplsvpnvrfroutemetric3',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteMetric4', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                An alternate routing metric for this route.
                The semantics of this metric are determined by
                the routing-protocol specified in  the  route's
                mplsVpnVrfRouteProto value. If this metric is not
                used, its value should be set to -1.
                ''',
                'mplsvpnvrfroutemetric4',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteMetric5', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                An alternate routing metric for this route.
                The semantics of this metric are determined by
                the routing-protocol specified in  the  route's
                mplsVpnVrfRouteProto value. If this metric is not
                used, its value should be set to -1.
                ''',
                'mplsvpnvrfroutemetric5',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteNextHopAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The address type of the mplsVpnVrfRouteNextHopAddrType
                object.
                ''',
                'mplsvpnvrfroutenexthopaddrtype',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteNextHopAS', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Autonomous System Number of the Next Hop.
                The semantics of this object are determined by
                the routing-protocol specified in the route's
                mplsVpnVrfRouteProto value. When this object is
                unknown or not relevant its value should be set
                to zero.
                ''',
                'mplsvpnvrfroutenexthopas',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteProto', REFERENCE_ENUM_CLASS, 'MplsvpnvrfrouteprotoEnum' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry.MplsvpnvrfrouteprotoEnum', 
                [], [], 
                '''                The routing mechanism via which this route was
                learned.  Inclusion of values for gateway rout-
                ing protocols is not  intended  to  imply  that
                hosts should support those protocols.
                ''',
                'mplsvpnvrfrouteproto',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                Row status for this table. It is used according
                to row installation and removal conventions.
                ''',
                'mplsvpnvrfrouterowstatus',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                Storage type value.
                ''',
                'mplsvpnvrfroutestoragetype',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteType', REFERENCE_ENUM_CLASS, 'MplsvpnvrfroutetypeEnum' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry.MplsvpnvrfroutetypeEnum', 
                [], [], 
                '''                The type of route.  Note that local(3)  refers
                to a route for which the next hop is the final
                destination; remote(4) refers to a route for
                that the next  hop is not the final destination.
                Routes which do not result in traffic forwarding or
                rejection should not be displayed even if the
                implementation keeps them stored internally.
                
                reject (2) refers to a route which, if matched,
                discards the message as unreachable. This is used
                in some protocols as a means of correctly aggregating
                routes.
                ''',
                'mplsvpnvrfroutetype',
                'MPLS-VPN-MIB', False),
            ],
            'MPLS-VPN-MIB',
            'mplsVpnVrfRouteEntry',
            _yang_ns._namespaces['MPLS-VPN-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_VPN_MIB'
        ),
    },
    'MplsVpnMib.Mplsvpnvrfroutetable' : {
        'meta_info' : _MetaInfoClass('MplsVpnMib.Mplsvpnvrfroutetable',
            False, 
            [
            _MetaInfoClassMember('mplsVpnVrfRouteEntry', REFERENCE_LIST, 'Mplsvpnvrfrouteentry' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry', 
                [], [], 
                '''                An entry in this table is created by an LSR for every route
                present configured (either dynamically or statically) within
                the context of a specific VRF capable of supporting MPLS/BGP
                VPN. The indexing provides an ordering of VRFs per-VPN
                interface.
                ''',
                'mplsvpnvrfrouteentry',
                'MPLS-VPN-MIB', False),
            ],
            'MPLS-VPN-MIB',
            'mplsVpnVrfRouteTable',
            _yang_ns._namespaces['MPLS-VPN-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_VPN_MIB'
        ),
    },
    'MplsVpnMib' : {
        'meta_info' : _MetaInfoClass('MplsVpnMib',
            False, 
            [
            _MetaInfoClassMember('mplsVpnInterfaceConfTable', REFERENCE_CLASS, 'Mplsvpninterfaceconftable' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpninterfaceconftable', 
                [], [], 
                '''                This table specifies per-interface MPLS capability
                and associated information.
                ''',
                'mplsvpninterfaceconftable',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnScalars', REFERENCE_CLASS, 'Mplsvpnscalars' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnscalars', 
                [], [], 
                '''                ''',
                'mplsvpnscalars',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfBgpNbrAddrTable', REFERENCE_CLASS, 'Mplsvpnvrfbgpnbraddrtable' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnvrfbgpnbraddrtable', 
                [], [], 
                '''                Each entry in this table specifies a per-interface 
                MPLS/EBGP neighbor.
                ''',
                'mplsvpnvrfbgpnbraddrtable',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfBgpNbrPrefixTable', REFERENCE_CLASS, 'Mplsvpnvrfbgpnbrprefixtable' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable', 
                [], [], 
                '''                This table specifies per-VRF vpnv4 multi-protocol
                prefixes supported by BGP.
                ''',
                'mplsvpnvrfbgpnbrprefixtable',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteTable', REFERENCE_CLASS, 'Mplsvpnvrfroutetable' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnvrfroutetable', 
                [], [], 
                '''                This table specifies per-interface MPLS/BGP VPN VRF Table
                routing information. Entries in this table define VRF routing
                entries associated with the specified MPLS/VPN interfaces. Note
                that this table contains both BGP and IGP routes, as both may
                appear in the same VRF.
                ''',
                'mplsvpnvrfroutetable',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfRouteTargetTable', REFERENCE_CLASS, 'Mplsvpnvrfroutetargettable' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnvrfroutetargettable', 
                [], [], 
                '''                This table specifies per-VRF route target association.
                Each entry identifies a connectivity policy supported
                as part of a VPN.
                ''',
                'mplsvpnvrfroutetargettable',
                'MPLS-VPN-MIB', False),
            _MetaInfoClassMember('mplsVpnVrfTable', REFERENCE_CLASS, 'Mplsvpnvrftable' , 'ydk.models.cisco_ios_xe.MPLS_VPN_MIB', 'MplsVpnMib.Mplsvpnvrftable', 
                [], [], 
                '''                This table specifies per-interface MPLS/BGP VPN
                VRF Table capability and associated information.
                Entries in this table define VRF routing instances
                associated with MPLS/VPN interfaces. Note that
                multiple interfaces can belong to the same VRF
                instance. The collection of all VRF instances
                comprises an actual VPN.
                ''',
                'mplsvpnvrftable',
                'MPLS-VPN-MIB', False),
            ],
            'MPLS-VPN-MIB',
            'MPLS-VPN-MIB',
            _yang_ns._namespaces['MPLS-VPN-MIB'],
        'ydk.models.cisco_ios_xe.MPLS_VPN_MIB'
        ),
    },
}
_meta_table['MplsVpnMib.Mplsvpninterfaceconftable.Mplsvpninterfaceconfentry']['meta_info'].parent =_meta_table['MplsVpnMib.Mplsvpninterfaceconftable']['meta_info']
_meta_table['MplsVpnMib.Mplsvpnvrftable.Mplsvpnvrfentry']['meta_info'].parent =_meta_table['MplsVpnMib.Mplsvpnvrftable']['meta_info']
_meta_table['MplsVpnMib.Mplsvpnvrfroutetargettable.Mplsvpnvrfroutetargetentry']['meta_info'].parent =_meta_table['MplsVpnMib.Mplsvpnvrfroutetargettable']['meta_info']
_meta_table['MplsVpnMib.Mplsvpnvrfbgpnbraddrtable.Mplsvpnvrfbgpnbraddrentry']['meta_info'].parent =_meta_table['MplsVpnMib.Mplsvpnvrfbgpnbraddrtable']['meta_info']
_meta_table['MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable.Mplsvpnvrfbgpnbrprefixentry']['meta_info'].parent =_meta_table['MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable']['meta_info']
_meta_table['MplsVpnMib.Mplsvpnvrfroutetable.Mplsvpnvrfrouteentry']['meta_info'].parent =_meta_table['MplsVpnMib.Mplsvpnvrfroutetable']['meta_info']
_meta_table['MplsVpnMib.Mplsvpnscalars']['meta_info'].parent =_meta_table['MplsVpnMib']['meta_info']
_meta_table['MplsVpnMib.Mplsvpninterfaceconftable']['meta_info'].parent =_meta_table['MplsVpnMib']['meta_info']
_meta_table['MplsVpnMib.Mplsvpnvrftable']['meta_info'].parent =_meta_table['MplsVpnMib']['meta_info']
_meta_table['MplsVpnMib.Mplsvpnvrfroutetargettable']['meta_info'].parent =_meta_table['MplsVpnMib']['meta_info']
_meta_table['MplsVpnMib.Mplsvpnvrfbgpnbraddrtable']['meta_info'].parent =_meta_table['MplsVpnMib']['meta_info']
_meta_table['MplsVpnMib.Mplsvpnvrfbgpnbrprefixtable']['meta_info'].parent =_meta_table['MplsVpnMib']['meta_info']
_meta_table['MplsVpnMib.Mplsvpnvrfroutetable']['meta_info'].parent =_meta_table['MplsVpnMib']['meta_info']
