


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'OspfauthenticationtypeEnum' : _MetaInfoEnum('OspfauthenticationtypeEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'none':'none',
            'simplePassword':'simplePassword',
            'md5':'md5',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'StatusEnum' : _MetaInfoEnum('StatusEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfgeneralgroup.OspfrestartexitreasonEnum' : _MetaInfoEnum('OspfrestartexitreasonEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'none':'none',
            'inProgress':'inProgress',
            'completed':'completed',
            'timedOut':'timedOut',
            'topologyChanged':'topologyChanged',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfgeneralgroup.OspfrestartstatusEnum' : _MetaInfoEnum('OspfrestartstatusEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'notRestarting':'notRestarting',
            'plannedRestart':'plannedRestart',
            'unplannedRestart':'unplannedRestart',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfgeneralgroup.OspfrestartsupportEnum' : _MetaInfoEnum('OspfrestartsupportEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'none':'none',
            'plannedOnly':'plannedOnly',
            'plannedAndUnplanned':'plannedAndUnplanned',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfgeneralgroup.OspfstubrouteradvertisementEnum' : _MetaInfoEnum('OspfstubrouteradvertisementEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'doNotAdvertise':'doNotAdvertise',
            'advertise':'advertise',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfgeneralgroup.OspfversionnumberEnum' : _MetaInfoEnum('OspfversionnumberEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'version2':'version2',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfgeneralgroup' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfgeneralgroup',
            False, 
            [
            _MetaInfoClassMember('ospfAdminStat', REFERENCE_ENUM_CLASS, 'StatusEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'StatusEnum', 
                [], [], 
                '''                The administrative status of OSPF in the
                router.  The value 'enabled' denotes that the
                OSPF Process is active on at least one interface;
                'disabled' disables it on all interfaces.
                
                This object is persistent and when written
                the entity SHOULD save the change to non-volatile storage.
                ''',
                'ospfadminstat',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAreaBdrRtrStatus', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A flag to note whether this router is an Area
                Border Router.
                ''',
                'ospfareabdrrtrstatus',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfASBdrRtrStatus', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A flag to note whether this router is configured as
                an Autonomous System Border Router.
                
                This object is persistent and when written the
                entity SHOULD save the change to non-volatile storage.
                ''',
                'ospfasbdrrtrstatus',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAsLsaCksumSum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The 32-bit unsigned sum of the LS checksums of
                the AS link state advertisements contained in the AS-scope
                link state database.  This sum can be used to determine
                if there has been a change in a router's AS-scope link
                state database, and to compare the AS-scope link state
                database of two routers.
                ''',
                'ospfaslsacksumsum',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAsLsaCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of AS-scope link state
                advertisements in the AS-scope link state database.
                ''',
                'ospfaslsacount',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfDemandExtensions', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The router's support for demand routing.
                This object is persistent and when written
                the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospfdemandextensions',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfDiscontinuityTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion
                at which any one of this MIB's counters suffered
                a discontinuity.
                
                If no such discontinuities have occurred since the last
                re-initialization of the local management subsystem,
                then this object contains a zero value.
                ''',
                'ospfdiscontinuitytime',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfExitOverflowInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The number of seconds that, after entering
                OverflowState, a router will attempt to leave
                OverflowState.  This allows the router to again
                originate non-default AS-external LSAs.  When
                set to 0, the router will not leave
                overflow state until restarted.
                
                This object is persistent and when written
                the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospfexitoverflowinterval',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfExternLsaCksumSum', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The 32-bit sum of the LS checksums of
                the external link state advertisements
                contained in the link state database.  This sum
                can be used to determine if there has been a
                change in a router's link state database and
                to compare the link state database of two
                routers.  The value should be treated as unsigned
                when comparing two sums of checksums.
                ''',
                'ospfexternlsacksumsum',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfExternLsaCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of external (LS type-5) link state
                advertisements in the link state database.
                ''',
                'ospfexternlsacount',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfExtLsdbLimit', ATTRIBUTE, 'int' , None, None, 
                [('-1', '2147483647')], [], 
                '''                The maximum number of non-default
                AS-external LSAs entries that can be stored in the
                link state database.  If the value is -1, then
                there is no limit.
                
                When the number of non-default AS-external LSAs
                in a router's link state database reaches
                ospfExtLsdbLimit, the router enters
                overflow state.  The router never holds more than
                ospfExtLsdbLimit non-default AS-external LSAs
                in its database.  OspfExtLsdbLimit MUST be set
                identically in all routers attached to the OSPF
                backbone and/or any regular OSPF area (i.e.,
                OSPF stub areas and NSSAs are excluded).
                
                This object is persistent and when written
                the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospfextlsdblimit',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfMulticastExtensions', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                A bit mask indicating whether the router is
                forwarding IP multicast (Class D) datagrams
                based on the algorithms defined in the
                multicast extensions to OSPF.
                
                Bit 0, if set, indicates that the router can
                
                forward IP multicast datagrams in the router's
                directly attached areas (called intra-area
                multicast routing).
                
                Bit 1, if set, indicates that the router can
                forward IP multicast datagrams between OSPF
                areas (called inter-area multicast routing).
                
                Bit 2, if set, indicates that the router can
                forward IP multicast datagrams between
                Autonomous Systems (called inter-AS multicast
                routing).
                
                Only certain combinations of bit settings are
                allowed, namely: 0 (no multicast forwarding is
                enabled), 1 (intra-area multicasting only), 3
                (intra-area and inter-area multicasting), 5
                (intra-area and inter-AS multicasting), and 7
                (multicasting everywhere).  By default, no
                multicast forwarding is enabled.
                
                This object is persistent and when written
                the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospfmulticastextensions',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfOpaqueLsaSupport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The router's support for Opaque LSA types.
                ''',
                'ospfopaquelsasupport',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfOriginateNewLsas', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of new link state advertisements
                that have been originated.  This number is
                incremented each time the router originates a new
                LSA.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management system,
                and at other times as indicated by the value of
                ospfDiscontinuityTime.
                ''',
                'ospforiginatenewlsas',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfReferenceBandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reference bandwidth in kilobits/second for
                
                calculating default interface metrics.  The
                default value is 100,000 KBPS (100 MBPS).
                
                This object is persistent and when written
                the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospfreferencebandwidth',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfRestartAge', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining time in current OSPF graceful restart
                interval.
                ''',
                'ospfrestartage',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfRestartExitReason', REFERENCE_ENUM_CLASS, 'OspfrestartexitreasonEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfgeneralgroup.OspfrestartexitreasonEnum', 
                [], [], 
                '''                Describes the outcome of the last attempt at a
                graceful restart.  If the value is 'none', no restart
                has yet been attempted.  If the value is 'inProgress',
                a restart attempt is currently underway.
                ''',
                'ospfrestartexitreason',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfRestartInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '1800')], [], 
                '''                Configured OSPF graceful restart timeout interval.
                
                This object is persistent and when written
                the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospfrestartinterval',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfRestartStatus', REFERENCE_ENUM_CLASS, 'OspfrestartstatusEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfgeneralgroup.OspfrestartstatusEnum', 
                [], [], 
                '''                Current status of OSPF graceful restart.
                ''',
                'ospfrestartstatus',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfRestartStrictLsaChecking', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates if strict LSA checking is enabled for
                graceful restart.
                
                This object is persistent and when written
                the entity SHOULD save the change to non-volatile
                
                storage.
                ''',
                'ospfrestartstrictlsachecking',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfRestartSupport', REFERENCE_ENUM_CLASS, 'OspfrestartsupportEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfgeneralgroup.OspfrestartsupportEnum', 
                [], [], 
                '''                The router's support for OSPF graceful restart.
                Options include: no restart support, only planned
                restarts, or both planned and unplanned restarts.
                
                This object is persistent and when written
                the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospfrestartsupport',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfRFC1583Compatibility', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates metrics used to choose among multiple
                AS-external LSAs.  When RFC1583Compatibility is set to
                enabled, only cost will be used when choosing among
                multiple AS-external LSAs advertising the same
                destination.  When RFC1583Compatibility is set to
                disabled, preference will be driven first by type of
                path using cost only to break ties.
                
                This object is persistent and when written
                the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospfrfc1583compatibility',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfRouterId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                A 32-bit integer uniquely identifying the
                router in the Autonomous System.
                By convention, to ensure uniqueness, this
                should default to the value of one of the
                router's IP interface addresses.
                
                This object is persistent and when written
                the entity SHOULD save the change to non-volatile storage.
                ''',
                'ospfrouterid',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfRxNewLsas', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of link state advertisements received
                that are determined to be new instantiations.
                This number does not include newer instantiations
                of self-originated link state advertisements.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management system,
                and at other times as indicated by the value of
                ospfDiscontinuityTime.
                ''',
                'ospfrxnewlsas',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfStubRouterAdvertisement', REFERENCE_ENUM_CLASS, 'OspfstubrouteradvertisementEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfgeneralgroup.OspfstubrouteradvertisementEnum', 
                [], [], 
                '''                This object controls the advertisement of
                stub router LSAs by the router.  The value
                doNotAdvertise will result in the advertisement
                of a standard router LSA and is the default value.
                
                This object is persistent and when written
                the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospfstubrouteradvertisement',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfStubRouterSupport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The router's support for stub router functionality.
                ''',
                'ospfstubroutersupport',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfTOSSupport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The router's support for type-of-service routing.
                
                This object is persistent and when written
                the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospftossupport',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVersionNumber', REFERENCE_ENUM_CLASS, 'OspfversionnumberEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfgeneralgroup.OspfversionnumberEnum', 
                [], [], 
                '''                The current version number of the OSPF protocol is 2.
                ''',
                'ospfversionnumber',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfGeneralGroup',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfareatable.Ospfareaentry.CospfareanssatranslatorroleEnum' : _MetaInfoEnum('CospfareanssatranslatorroleEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'always':'always',
            'candidate':'candidate',
        }, 'CISCO-OSPF-MIB', _yang_ns._namespaces['CISCO-OSPF-MIB']),
    'OspfMib.Ospfareatable.Ospfareaentry.CospfareanssatranslatorstateEnum' : _MetaInfoEnum('CospfareanssatranslatorstateEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'enabled':'enabled',
            'elected':'elected',
            'disabled':'disabled',
        }, 'CISCO-OSPF-MIB', _yang_ns._namespaces['CISCO-OSPF-MIB']),
    'OspfMib.Ospfareatable.Ospfareaentry.OspfareanssatranslatorroleEnum' : _MetaInfoEnum('OspfareanssatranslatorroleEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'always':'always',
            'candidate':'candidate',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfareatable.Ospfareaentry.OspfareanssatranslatorstateEnum' : _MetaInfoEnum('OspfareanssatranslatorstateEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'enabled':'enabled',
            'elected':'elected',
            'disabled':'disabled',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfareatable.Ospfareaentry.OspfareasummaryEnum' : _MetaInfoEnum('OspfareasummaryEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'noAreaSummary':'noAreaSummary',
            'sendAreaSummary':'sendAreaSummary',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfareatable.Ospfareaentry.OspfimportasexternEnum' : _MetaInfoEnum('OspfimportasexternEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'importExternal':'importExternal',
            'importNoExternal':'importNoExternal',
            'importNssa':'importNssa',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfareatable.Ospfareaentry' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfareatable.Ospfareaentry',
            False, 
            [
            _MetaInfoClassMember('ospfAreaId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                A 32-bit integer uniquely identifying an area.
                Area ID 0.0.0.0 is used for the OSPF backbone.
                ''',
                'ospfareaid',
                'OSPF-MIB', True),
            _MetaInfoClassMember('cospfAreaNssaTranslatorEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of Translator State changes
                that have occurred since the last boot-up.
                ''',
                'cospfareanssatranslatorevents',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfAreaNssaTranslatorRole', REFERENCE_ENUM_CLASS, 'CospfareanssatranslatorroleEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfareatable.Ospfareaentry.CospfareanssatranslatorroleEnum', 
                [], [], 
                '''                Indicates an NSSA Border router's ability to
                perform NSSA translation of type-7 LSAs into
                type-5 LSAs.
                ''',
                'cospfareanssatranslatorrole',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfAreaNssaTranslatorState', REFERENCE_ENUM_CLASS, 'CospfareanssatranslatorstateEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfareatable.Ospfareaentry.CospfareanssatranslatorstateEnum', 
                [], [], 
                '''                Indicates if and how an NSSA Border router is
                performing NSSA translation of type-7 LSAs into type-5
                LSAs. When this object set to enabled, the NSSA Border
                router's cospfAreaNssaExtTranslatorRole has been set to
                always. When this object is set to elected, a candidate
                NSSA Border router is Translating type-7 LSAs into type-5.
                When this object is set to disabled, a candidate NSSA
                Border router is NOT translating type-7 LSAs into type-5.
                ''',
                'cospfareanssatranslatorstate',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfOpaqueAreaLsaCksumSum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The 32-bit unsigned sum of the Opaque Area and AS 
                link-state advertisements' LS checksums contained 
                link state database of this area.  The sum can be 
                used to determine if there has been a change in the 
                link state database for Opaque Area and AS link-state
                advertisements
                ''',
                'cospfopaquearealsacksumsum',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfOpaqueAreaLsaCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of Opaque Area and AS link-state 
                advertisements in the link state database of this
                area.
                ''',
                'cospfopaquearealsacount',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('ospfAreaBdrRtrCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of Area Border Routers reachable
                within this area.  This is initially zero and is
                calculated in each Shortest Path First (SPF) pass.
                ''',
                'ospfareabdrrtrcount',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAreaLsaCksumSum', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The 32-bit sum of the link state
                advertisements' LS checksums contained in this
                area's link state database.  This sum excludes
                external (LS type-5) link state advertisements.
                The sum can be used to determine if there has
                been a change in a router's link state
                database, and to compare the link state database of
                two routers.  The value should be treated as unsigned
                when comparing two sums of checksums.
                ''',
                'ospfarealsacksumsum',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAreaLsaCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of link state advertisements
                in this area's link state database, excluding
                AS-external LSAs.
                ''',
                'ospfarealsacount',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAreaNssaTranslatorEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of translator state changes
                that have occurred since the last boot-up.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at other
                times as indicated by the value of ospfDiscontinuityTime.
                ''',
                'ospfareanssatranslatorevents',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAreaNssaTranslatorRole', REFERENCE_ENUM_CLASS, 'OspfareanssatranslatorroleEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfareatable.Ospfareaentry.OspfareanssatranslatorroleEnum', 
                [], [], 
                '''                Indicates an NSSA border router's ability to
                perform NSSA translation of type-7 LSAs into
                type-5 LSAs.
                ''',
                'ospfareanssatranslatorrole',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAreaNssaTranslatorStabilityInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The number of seconds after an elected translator
                determines its services are no longer required, that
                it should continue to perform its translation duties.
                ''',
                'ospfareanssatranslatorstabilityinterval',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAreaNssaTranslatorState', REFERENCE_ENUM_CLASS, 'OspfareanssatranslatorstateEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfareatable.Ospfareaentry.OspfareanssatranslatorstateEnum', 
                [], [], 
                '''                Indicates if and how an NSSA border router is
                performing NSSA translation of type-7 LSAs into type-5
                
                LSAs.  When this object is set to enabled, the NSSA Border
                router's OspfAreaNssaExtTranslatorRole has been set to
                always.  When this object is set to elected, a candidate
                NSSA Border router is Translating type-7 LSAs into type-5.
                When this object is set to disabled, a candidate NSSA
                border router is NOT translating type-7 LSAs into type-5.
                ''',
                'ospfareanssatranslatorstate',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAreaStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object permits management of the table by
                facilitating actions such as row creation,
                construction, and destruction.
                
                The value of this object has no effect on
                whether other objects in this conceptual row can be
                modified.
                ''',
                'ospfareastatus',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAreaSummary', REFERENCE_ENUM_CLASS, 'OspfareasummaryEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfareatable.Ospfareaentry.OspfareasummaryEnum', 
                [], [], 
                '''                The variable ospfAreaSummary controls the
                import of summary LSAs into stub and NSSA areas.
                It has no effect on other areas.
                
                If it is noAreaSummary, the router will not
                originate summary LSAs into the stub or NSSA area.
                It will rely entirely on its default route.
                
                If it is sendAreaSummary, the router will both
                summarize and propagate summary LSAs.
                ''',
                'ospfareasummary',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAsBdrRtrCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of Autonomous System Border
                Routers reachable within this area.  This is
                initially zero and is calculated in each SPF
                pass.
                ''',
                'ospfasbdrrtrcount',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAuthType', REFERENCE_ENUM_CLASS, 'OspfauthenticationtypeEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfauthenticationtypeEnum', 
                [], [], 
                '''                The authentication type specified for an area.
                ''',
                'ospfauthtype',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfImportAsExtern', REFERENCE_ENUM_CLASS, 'OspfimportasexternEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfareatable.Ospfareaentry.OspfimportasexternEnum', 
                [], [], 
                '''                Indicates if an area is a stub area, NSSA, or standard
                area.  Type-5 AS-external LSAs and type-11 Opaque LSAs are
                not imported into stub areas or NSSAs.  NSSAs import
                AS-external data as type-7 LSAs
                ''',
                'ospfimportasextern',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfSpfRuns', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times that the intra-area route
                table has been calculated using this area's
                link state database.  This is typically done
                using Dijkstra's algorithm.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at other
                times as indicated by the value of ospfDiscontinuityTime.
                ''',
                'ospfspfruns',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfAreaEntry',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfareatable' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfareatable',
            False, 
            [
            _MetaInfoClassMember('ospfAreaEntry', REFERENCE_LIST, 'Ospfareaentry' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfareatable.Ospfareaentry', 
                [], [], 
                '''                Information describing the configured parameters and
                cumulative statistics of one of the router's attached areas.
                The interfaces and virtual links are configured as part of
                these areas.  Area 0.0.0.0, by definition, is the backbone
                area.
                
                Information in this table is persistent and when this object
                is written the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospfareaentry',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfAreaTable',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfstubareatable.Ospfstubareaentry.OspfstubmetrictypeEnum' : _MetaInfoEnum('OspfstubmetrictypeEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'ospfMetric':'ospfMetric',
            'comparableCost':'comparableCost',
            'nonComparable':'nonComparable',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfstubareatable.Ospfstubareaentry' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfstubareatable.Ospfstubareaentry',
            False, 
            [
            _MetaInfoClassMember('ospfStubAreaId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The 32-bit identifier for the stub area.  On
                creation, this can be derived from the
                instance.
                ''',
                'ospfstubareaid',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfStubTOS', ATTRIBUTE, 'int' , None, None, 
                [('0', '30')], [], 
                '''                The Type of Service associated with the
                metric.  On creation, this can be derived from
                
                the instance.
                ''',
                'ospfstubtos',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfStubMetric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                The metric value applied at the indicated Type
                of Service.  By default, this equals the least
                metric at the Type of Service among the
                interfaces to other areas.
                ''',
                'ospfstubmetric',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfStubMetricType', REFERENCE_ENUM_CLASS, 'OspfstubmetrictypeEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfstubareatable.Ospfstubareaentry.OspfstubmetrictypeEnum', 
                [], [], 
                '''                This variable displays the type of metric
                advertised as a default route.
                ''',
                'ospfstubmetrictype',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfStubStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object permits management of the table by
                facilitating actions such as row creation,
                construction, and destruction.
                
                The value of this object has no effect on
                whether other objects in this conceptual row can be
                modified.
                ''',
                'ospfstubstatus',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfStubAreaEntry',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfstubareatable' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfstubareatable',
            False, 
            [
            _MetaInfoClassMember('ospfStubAreaEntry', REFERENCE_LIST, 'Ospfstubareaentry' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfstubareatable.Ospfstubareaentry', 
                [], [], 
                '''                The metric for a given Type of Service that
                will be advertised by a default Area Border
                Router into a stub area.
                
                Information in this table is persistent and when this object
                is written the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospfstubareaentry',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfStubAreaTable',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospflsdbtable.Ospflsdbentry.OspflsdbtypeEnum' : _MetaInfoEnum('OspflsdbtypeEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'routerLink':'routerLink',
            'networkLink':'networkLink',
            'summaryLink':'summaryLink',
            'asSummaryLink':'asSummaryLink',
            'asExternalLink':'asExternalLink',
            'multicastLink':'multicastLink',
            'nssaExternalLink':'nssaExternalLink',
            'areaOpaqueLink':'areaOpaqueLink',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospflsdbtable.Ospflsdbentry' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospflsdbtable.Ospflsdbentry',
            False, 
            [
            _MetaInfoClassMember('ospfLsdbAreaId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The 32-bit identifier of the area from which
                the LSA was received.
                ''',
                'ospflsdbareaid',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfLsdbType', REFERENCE_ENUM_CLASS, 'OspflsdbtypeEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospflsdbtable.Ospflsdbentry.OspflsdbtypeEnum', 
                [], [], 
                '''                The type of the link state advertisement.
                Each link state type has a separate advertisement
                format.
                
                Note: External link state advertisements are permitted
                for backward compatibility, but should be displayed
                in the ospfAsLsdbTable rather than here.
                ''',
                'ospflsdbtype',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfLsdbLsid', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Link State ID is an LS Type Specific field
                containing either a Router ID or an IP address;
                it identifies the piece of the routing domain
                that is being described by the advertisement.
                ''',
                'ospflsdblsid',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfLsdbRouterId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The 32-bit number that uniquely identifies the
                originating router in the Autonomous System.
                ''',
                'ospflsdbrouterid',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfLsdbAdvertisement', ATTRIBUTE, 'str' , None, None, 
                [(1, 65535)], [], 
                '''                The entire link state advertisement, including
                its header.
                
                Note that for variable length LSAs, SNMP agents
                may not be able to return the largest string size.
                ''',
                'ospflsdbadvertisement',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfLsdbAge', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This field is the age of the link state advertisement
                in seconds.
                ''',
                'ospflsdbage',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfLsdbChecksum', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This field is the checksum of the complete contents of
                the advertisement, excepting the age field.  The age field
                is excepted so that an advertisement's age can be
                incremented without updating the checksum.  The checksum
                used is the same that is used for ISO connectionless
                
                datagrams; it is commonly referred to as the
                Fletcher checksum.
                ''',
                'ospflsdbchecksum',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfLsdbSequence', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The sequence number field is a signed 32-bit
                integer.  It starts with the value '80000001'h,
                or -'7FFFFFFF'h, and increments until '7FFFFFFF'h.
                Thus, a typical sequence number will be very negative.
                It is used to detect old and duplicate Link State
                Advertisements.  The space of sequence numbers is linearly
                ordered.  The larger the sequence number, the more recent
                the advertisement.
                ''',
                'ospflsdbsequence',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfLsdbEntry',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospflsdbtable' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospflsdbtable',
            False, 
            [
            _MetaInfoClassMember('ospfLsdbEntry', REFERENCE_LIST, 'Ospflsdbentry' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospflsdbtable.Ospflsdbentry', 
                [], [], 
                '''                A single link state advertisement.
                ''',
                'ospflsdbentry',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfLsdbTable',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfarearangetable.Ospfarearangeentry.OspfarearangeeffectEnum' : _MetaInfoEnum('OspfarearangeeffectEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'advertiseMatching':'advertiseMatching',
            'doNotAdvertiseMatching':'doNotAdvertiseMatching',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfarearangetable.Ospfarearangeentry' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfarearangetable.Ospfarearangeentry',
            False, 
            [
            _MetaInfoClassMember('ospfAreaRangeAreaId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The area that the address range is to be found
                within.
                ''',
                'ospfarearangeareaid',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfAreaRangeNet', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the net or subnet indicated
                by the range.
                ''',
                'ospfarearangenet',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfAreaRangeEffect', REFERENCE_ENUM_CLASS, 'OspfarearangeeffectEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfarearangetable.Ospfarearangeentry.OspfarearangeeffectEnum', 
                [], [], 
                '''                Subnets subsumed by ranges either trigger the
                advertisement of the indicated summary
                (advertiseMatching) or result in the subnet's not
                being advertised at all outside the area.
                ''',
                'ospfarearangeeffect',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAreaRangeMask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The subnet mask that pertains to the net or
                subnet.
                ''',
                'ospfarearangemask',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAreaRangeStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object permits management of the table by
                facilitating actions such as row creation,
                construction, and destruction.
                
                The value of this object has no effect on
                whether other objects in this conceptual row can be
                modified.
                ''',
                'ospfarearangestatus',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfAreaRangeEntry',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfarearangetable' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfarearangetable',
            False, 
            [
            _MetaInfoClassMember('ospfAreaRangeEntry', REFERENCE_LIST, 'Ospfarearangeentry' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfarearangetable.Ospfarearangeentry', 
                [], [], 
                '''                A single area address range.
                
                Information in this table is persistent and when this object
                is written the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospfarearangeentry',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfAreaRangeTable',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfhosttable.Ospfhostentry' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfhosttable.Ospfhostentry',
            False, 
            [
            _MetaInfoClassMember('ospfHostIpAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the host.
                ''',
                'ospfhostipaddress',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfHostTOS', ATTRIBUTE, 'int' , None, None, 
                [('0', '30')], [], 
                '''                The Type of Service of the route being configured.
                ''',
                'ospfhosttos',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfHostAreaID', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The OSPF area to which the host belongs.
                Deprecated by ospfHostCfgAreaID.
                ''',
                'ospfhostareaid',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfHostCfgAreaID', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                To configure the OSPF area to which the host belongs.
                ''',
                'ospfhostcfgareaid',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfHostMetric', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The metric to be advertised.
                ''',
                'ospfhostmetric',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfHostStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object permits management of the table by
                facilitating actions such as row creation,
                construction, and destruction.
                
                The value of this object has no effect on
                whether other objects in this conceptual row can be
                modified.
                ''',
                'ospfhoststatus',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfHostEntry',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfhosttable' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfhosttable',
            False, 
            [
            _MetaInfoClassMember('ospfHostEntry', REFERENCE_LIST, 'Ospfhostentry' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfhosttable.Ospfhostentry', 
                [], [], 
                '''                A metric to be advertised, for a given type of
                service, when a given host is reachable.
                
                Information in this table is persistent and when this object
                is written the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospfhostentry',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfHostTable',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfiftable.Ospfifentry.OspfifmulticastforwardingEnum' : _MetaInfoEnum('OspfifmulticastforwardingEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'blocked':'blocked',
            'multicast':'multicast',
            'unicast':'unicast',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfiftable.Ospfifentry.OspfifstateEnum' : _MetaInfoEnum('OspfifstateEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'down':'down',
            'loopback':'loopback',
            'waiting':'waiting',
            'pointToPoint':'pointToPoint',
            'designatedRouter':'designatedRouter',
            'backupDesignatedRouter':'backupDesignatedRouter',
            'otherDesignatedRouter':'otherDesignatedRouter',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfiftable.Ospfifentry.OspfiftypeEnum' : _MetaInfoEnum('OspfiftypeEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'broadcast':'broadcast',
            'nbma':'nbma',
            'pointToPoint':'pointToPoint',
            'pointToMultipoint':'pointToMultipoint',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfiftable.Ospfifentry' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfiftable.Ospfifentry',
            False, 
            [
            _MetaInfoClassMember('ospfIfIpAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of this OSPF interface.
                ''',
                'ospfifipaddress',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfAddressLessIf', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                For the purpose of easing the instancing of
                addressed and addressless interfaces; this
                variable takes the value 0 on interfaces with
                IP addresses and the corresponding value of
                ifIndex for interfaces having no IP address.
                ''',
                'ospfaddresslessif',
                'OSPF-MIB', True),
            _MetaInfoClassMember('cospfIfLsaCksumSum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The 32-bit unsigned sum of the link-state advertisements'
                LS checksums contained in this interface's link-local link 
                state database. The sum can be used to determine if there has
                been a change in the interface's link state database, and to
                compare the interface link-state database of routers 
                attached to the same subnet.
                ''',
                'cospfiflsacksumsum',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfIfLsaCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of link-local link state advertisements
                in this interface's link-local link state database.
                ''',
                'cospfiflsacount',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfAdminStat', REFERENCE_ENUM_CLASS, 'StatusEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'StatusEnum', 
                [], [], 
                '''                The OSPF interface's administrative status.
                The value formed on the interface, and the interface
                will be advertised as an internal route to some area.
                The value 'disabled' denotes that the interface is
                external to OSPF.
                ''',
                'ospfifadminstat',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfAreaId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                A 32-bit integer uniquely identifying the area
                to which the interface connects.  Area ID
                0.0.0.0 is used for the OSPF backbone.
                ''',
                'ospfifareaid',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfAuthKey', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                The cleartext password used as an OSPF
                authentication key when simplePassword security
                is enabled.  This object does not access any OSPF
                cryptogaphic (e.g., MD5) authentication key under
                any circumstance.
                
                If the key length is shorter than 8 octets, the
                agent will left adjust and zero fill to 8 octets.
                
                Unauthenticated interfaces need no authentication
                key, and simple password authentication cannot use
                a key of more than 8 octets.
                
                Note that the use of simplePassword authentication
                is NOT recommended when there is concern regarding
                attack upon the OSPF system.  SimplePassword
                authentication is only sufficient to protect against
                accidental misconfigurations because it re-uses
                cleartext passwords [RFC1704].
                
                When read, ospfIfAuthKey always returns an octet
                string of length zero.
                ''',
                'ospfifauthkey',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfAuthType', REFERENCE_ENUM_CLASS, 'OspfauthenticationtypeEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfauthenticationtypeEnum', 
                [], [], 
                '''                The authentication type specified for an interface.
                
                Note that this object can be used to engage
                in significant attacks against an OSPF router.
                ''',
                'ospfifauthtype',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfBackupDesignatedRouter', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the backup designated
                router.
                ''',
                'ospfifbackupdesignatedrouter',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfBackupDesignatedRouterId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Router ID of the backup designated router.
                ''',
                'ospfifbackupdesignatedrouterid',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfDemand', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether Demand OSPF procedures (hello
                suppression to FULL neighbors and setting the
                DoNotAge flag on propagated LSAs) should be
                performed on this interface.
                ''',
                'ospfifdemand',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfDesignatedRouter', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the designated router.
                ''',
                'ospfifdesignatedrouter',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfDesignatedRouterId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Router ID of the designated router.
                ''',
                'ospfifdesignatedrouterid',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times this OSPF interface has
                changed its state or an error has occurred.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at other
                times as indicated by the value of ospfDiscontinuityTime.
                ''',
                'ospfifevents',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfHelloInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The length of time, in seconds, between the Hello packets
                that the router sends on the interface.  This value must be
                the same for all routers attached to a common network.
                ''',
                'ospfifhellointerval',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfLsaCksumSum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The 32-bit unsigned sum of the Link State
                Advertisements' LS checksums contained in this
                interface's link-local link state database.
                The sum can be used to determine if there has
                been a change in the interface's link state
                database and to compare the interface link state
                database of routers attached to the same subnet.
                ''',
                'ospfiflsacksumsum',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfLsaCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of link-local link state advertisements
                in this interface's link-local link state database.
                ''',
                'ospfiflsacount',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfMulticastForwarding', REFERENCE_ENUM_CLASS, 'OspfifmulticastforwardingEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfiftable.Ospfifentry.OspfifmulticastforwardingEnum', 
                [], [], 
                '''                The way multicasts should be forwarded on this
                interface: not forwarded, forwarded as data
                link multicasts, or forwarded as data link
                unicasts.  Data link multicasting is not
                meaningful on point-to-point and NBMA interfaces,
                and setting ospfMulticastForwarding to 0 effectively
                disables all multicast forwarding.
                ''',
                'ospfifmulticastforwarding',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfPollInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The larger time interval, in seconds, between the Hello
                packets sent to an inactive non-broadcast multi-access
                neighbor.
                ''',
                'ospfifpollinterval',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfRetransInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                The number of seconds between link state advertisement
                retransmissions, for adjacencies belonging to this
                interface.  This value is also used when retransmitting
                
                database description and Link State request packets.
                Note that minimal value SHOULD be 1 second.
                ''',
                'ospfifretransinterval',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfRtrDeadInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The number of seconds that a router's Hello packets have
                not been seen before its neighbors declare the router down.
                This should be some multiple of the Hello interval.  This
                value must be the same for all routers attached to a common
                network.
                ''',
                'ospfifrtrdeadinterval',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfRtrPriority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The priority of this interface.  Used in
                multi-access networks, this field is used in
                the designated router election algorithm.  The
                value 0 signifies that the router is not eligible
                to become the designated router on this particular
                network.  In the event of a tie in this value,
                routers will use their Router ID as a tie breaker.
                ''',
                'ospfifrtrpriority',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfState', REFERENCE_ENUM_CLASS, 'OspfifstateEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfiftable.Ospfifentry.OspfifstateEnum', 
                [], [], 
                '''                The OSPF Interface State.
                ''',
                'ospfifstate',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object permits management of the table by
                facilitating actions such as row creation,
                construction, and destruction.
                
                The value of this object has no effect on
                whether other objects in this conceptual row can be
                modified.
                ''',
                'ospfifstatus',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfTransitDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                The estimated number of seconds it takes to
                transmit a link state update packet over this
                interface.  Note that the minimal value SHOULD be
                1 second.
                ''',
                'ospfiftransitdelay',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfType', REFERENCE_ENUM_CLASS, 'OspfiftypeEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfiftable.Ospfifentry.OspfiftypeEnum', 
                [], [], 
                '''                The OSPF interface type.
                By way of a default, this field may be intuited
                from the corresponding value of ifType.
                Broadcast LANs, such as Ethernet and IEEE 802.5,
                take the value 'broadcast', X.25 and similar
                technologies take the value 'nbma', and links
                that are definitively point to point take the
                value 'pointToPoint'.
                ''',
                'ospfiftype',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfIfEntry',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfiftable' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfiftable',
            False, 
            [
            _MetaInfoClassMember('ospfIfEntry', REFERENCE_LIST, 'Ospfifentry' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfiftable.Ospfifentry', 
                [], [], 
                '''                The OSPF interface entry describes one interface
                from the viewpoint of OSPF.
                
                Information in this table is persistent and when this object
                is written the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospfifentry',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfIfTable',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfifmetrictable.Ospfifmetricentry' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfifmetrictable.Ospfifmetricentry',
            False, 
            [
            _MetaInfoClassMember('ospfIfMetricIpAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of this OSPF interface.  On row
                creation, this can be derived from the instance.
                ''',
                'ospfifmetricipaddress',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfIfMetricAddressLessIf', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                For the purpose of easing the instancing of
                addressed and addressless interfaces; this
                variable takes the value 0 on interfaces with
                IP addresses and the value of ifIndex for
                interfaces having no IP address.  On row
                creation, this can be derived from the instance.
                ''',
                'ospfifmetricaddresslessif',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfIfMetricTOS', ATTRIBUTE, 'int' , None, None, 
                [('0', '30')], [], 
                '''                The Type of Service metric being referenced.
                On row creation, this can be derived from the
                instance.
                ''',
                'ospfifmetrictos',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfIfMetricStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object permits management of the table by
                facilitating actions such as row creation,
                construction, and destruction.
                
                The value of this object has no effect on
                whether other objects in this conceptual row can be
                modified.
                ''',
                'ospfifmetricstatus',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfMetricValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The metric of using this Type of Service on
                this interface.  The default value of the TOS 0
                metric is 10^8 / ifSpeed.
                ''',
                'ospfifmetricvalue',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfIfMetricEntry',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfifmetrictable' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfifmetrictable',
            False, 
            [
            _MetaInfoClassMember('ospfIfMetricEntry', REFERENCE_LIST, 'Ospfifmetricentry' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfifmetrictable.Ospfifmetricentry', 
                [], [], 
                '''                A particular TOS metric for a non-virtual interface
                identified by the interface index.
                
                Information in this table is persistent and when this object
                is written the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospfifmetricentry',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfIfMetricTable',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfvirtiftable.Ospfvirtifentry.OspfvirtifstateEnum' : _MetaInfoEnum('OspfvirtifstateEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'down':'down',
            'pointToPoint':'pointToPoint',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfvirtiftable.Ospfvirtifentry' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfvirtiftable.Ospfvirtifentry',
            False, 
            [
            _MetaInfoClassMember('ospfVirtIfAreaId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The transit area that the virtual link
                traverses.  By definition, this is not 0.0.0.0.
                ''',
                'ospfvirtifareaid',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfVirtIfNeighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Router ID of the virtual neighbor.
                ''',
                'ospfvirtifneighbor',
                'OSPF-MIB', True),
            _MetaInfoClassMember('cospfVirtIfLsaCksumSum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The 32-bit unsigned sum of the link-state advertisements'
                LS checksums contained in this
                virtual interface's link-local link state database.
                The sum can be used to determine if there has
                been a change in the virtual interface's link state database,
                and to compare the virtual interface link-state
                database of the virtual neighbors.
                ''',
                'cospfvirtiflsacksumsum',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('cospfVirtIfLsaCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of link-local link state advertisements
                in this virtual interface's link-local link state database.
                ''',
                'cospfvirtiflsacount',
                'CISCO-OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtIfAuthKey', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                The cleartext password used as an OSPF
                authentication key when simplePassword security
                is enabled.  This object does not access any OSPF
                cryptogaphic (e.g., MD5) authentication key under
                any circumstance.
                
                If the key length is shorter than 8 octets, the
                agent will left adjust and zero fill to 8 octets.
                
                Unauthenticated interfaces need no authentication
                key, and simple password authentication cannot use
                a key of more than 8 octets.
                
                Note that the use of simplePassword authentication
                is NOT recommended when there is concern regarding
                attack upon the OSPF system.  SimplePassword
                authentication is only sufficient to protect against
                accidental misconfigurations because it re-uses
                cleartext passwords.  [RFC1704]
                
                When read, ospfIfAuthKey always returns an octet
                string of length zero.
                ''',
                'ospfvirtifauthkey',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtIfAuthType', REFERENCE_ENUM_CLASS, 'OspfauthenticationtypeEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfauthenticationtypeEnum', 
                [], [], 
                '''                The authentication type specified for a virtual interface.
                
                Note that this object can be used to engage
                in significant attacks against an OSPF router.
                ''',
                'ospfvirtifauthtype',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtIfEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of state changes or error events on
                this virtual link.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at other
                times as indicated by the value of ospfDiscontinuityTime.
                ''',
                'ospfvirtifevents',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtIfHelloInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                The length of time, in seconds, between the
                Hello packets that the router sends on the
                interface.  This value must be the same for the
                virtual neighbor.
                ''',
                'ospfvirtifhellointerval',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtIfLsaCksumSum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The 32-bit unsigned sum of the link state
                advertisements' LS checksums contained in this
                virtual interface's link-local link state database.
                The sum can be used to determine if there has
                been a change in the virtual interface's link state
                database, and to compare the virtual interface
                link state database of the virtual neighbors.
                ''',
                'ospfvirtiflsacksumsum',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtIfLsaCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The total number of link-local link state advertisements
                in this virtual interface's link-local link state database.
                ''',
                'ospfvirtiflsacount',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtIfRetransInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                The number of seconds between link state
                avertisement retransmissions, for adjacencies
                belonging to this interface.  This value is
                also used when retransmitting database
                description and Link State request packets.  This
                value should be well over the expected
                round-trip time.  Note that the minimal value SHOULD be
                1 second.
                ''',
                'ospfvirtifretransinterval',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtIfRtrDeadInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The number of seconds that a router's Hello
                packets have not been seen before its
                neighbors declare the router down.  This should be
                some multiple of the Hello interval.  This
                value must be the same for the virtual neighbor.
                ''',
                'ospfvirtifrtrdeadinterval',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtIfState', REFERENCE_ENUM_CLASS, 'OspfvirtifstateEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfvirtiftable.Ospfvirtifentry.OspfvirtifstateEnum', 
                [], [], 
                '''                OSPF virtual interface states.
                ''',
                'ospfvirtifstate',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtIfStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object permits management of the table by
                facilitating actions such as row creation,
                construction, and destruction.
                
                The value of this object has no effect on
                whether other objects in this conceptual row can be
                modified.
                ''',
                'ospfvirtifstatus',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtIfTransitDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                The estimated number of seconds it takes to
                transmit a Link State update packet over this
                interface.  Note that the minimal value SHOULD be
                1 second.
                ''',
                'ospfvirtiftransitdelay',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfVirtIfEntry',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfvirtiftable' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfvirtiftable',
            False, 
            [
            _MetaInfoClassMember('ospfVirtIfEntry', REFERENCE_LIST, 'Ospfvirtifentry' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfvirtiftable.Ospfvirtifentry', 
                [], [], 
                '''                Information about a single virtual interface.
                
                Information in this table is persistent and when this object
                is written the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospfvirtifentry',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfVirtIfTable',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfnbrtable.Ospfnbrentry.OspfnbmanbrpermanenceEnum' : _MetaInfoEnum('OspfnbmanbrpermanenceEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'dynamic':'dynamic',
            'permanent':'permanent',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfnbrtable.Ospfnbrentry.OspfnbrrestarthelperexitreasonEnum' : _MetaInfoEnum('OspfnbrrestarthelperexitreasonEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'none':'none',
            'inProgress':'inProgress',
            'completed':'completed',
            'timedOut':'timedOut',
            'topologyChanged':'topologyChanged',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfnbrtable.Ospfnbrentry.OspfnbrrestarthelperstatusEnum' : _MetaInfoEnum('OspfnbrrestarthelperstatusEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'notHelping':'notHelping',
            'helping':'helping',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfnbrtable.Ospfnbrentry.OspfnbrstateEnum' : _MetaInfoEnum('OspfnbrstateEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'down':'down',
            'attempt':'attempt',
            'init':'init',
            'twoWay':'twoWay',
            'exchangeStart':'exchangeStart',
            'exchange':'exchange',
            'loading':'loading',
            'full':'full',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfnbrtable.Ospfnbrentry' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfnbrtable.Ospfnbrentry',
            False, 
            [
            _MetaInfoClassMember('ospfNbrIpAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address this neighbor is using in its
                IP source address.  Note that, on addressless
                links, this will not be 0.0.0.0 but the
                
                address of another of the neighbor's interfaces.
                ''',
                'ospfnbripaddr',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfNbrAddressLessIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                On an interface having an IP address, zero.
                On addressless interfaces, the corresponding
                value of ifIndex in the Internet Standard MIB.
                On row creation, this can be derived from the
                instance.
                ''',
                'ospfnbraddresslessindex',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfNbmaNbrPermanence', REFERENCE_ENUM_CLASS, 'OspfnbmanbrpermanenceEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfnbrtable.Ospfnbrentry.OspfnbmanbrpermanenceEnum', 
                [], [], 
                '''                This variable displays the status of the entry;
                'dynamic' and 'permanent' refer to how the neighbor
                became known.
                ''',
                'ospfnbmanbrpermanence',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfNbmaNbrStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object permits management of the table by
                facilitating actions such as row creation,
                construction, and destruction.
                
                The value of this object has no effect on
                whether other objects in this conceptual row can be
                modified.
                ''',
                'ospfnbmanbrstatus',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfNbrEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times this neighbor relationship
                has changed state or an error has occurred.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at other
                times as indicated by the value of ospfDiscontinuityTime.
                ''',
                'ospfnbrevents',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfNbrHelloSuppressed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether Hellos are being suppressed
                to the neighbor.
                ''',
                'ospfnbrhellosuppressed',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfNbrLsRetransQLen', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The current length of the retransmission
                queue.
                ''',
                'ospfnbrlsretransqlen',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfNbrOptions', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                A bit mask corresponding to the neighbor's
                options field.
                
                Bit 0, if set, indicates that the system will
                operate on Type of Service metrics other than
                TOS 0.  If zero, the neighbor will ignore all
                metrics except the TOS 0 metric.
                
                Bit 1, if set, indicates that the associated
                area accepts and operates on external
                information; if zero, it is a stub area.
                
                Bit 2, if set, indicates that the system is
                capable of routing IP multicast datagrams, that is
                that it implements the multicast extensions to
                OSPF.
                
                Bit 3, if set, indicates that the associated
                area is an NSSA.  These areas are capable of
                carrying type-7 external advertisements, which
                are translated into type-5 external advertisements
                at NSSA borders.
                ''',
                'ospfnbroptions',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfNbrPriority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The priority of this neighbor in the designated
                router election algorithm.  The value 0 signifies
                that the neighbor is not eligible to become
                the designated router on this particular network.
                ''',
                'ospfnbrpriority',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfNbrRestartHelperAge', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining time in current OSPF graceful restart
                interval, if the router is acting as a restart
                helper for the neighbor.
                ''',
                'ospfnbrrestarthelperage',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfNbrRestartHelperExitReason', REFERENCE_ENUM_CLASS, 'OspfnbrrestarthelperexitreasonEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfnbrtable.Ospfnbrentry.OspfnbrrestarthelperexitreasonEnum', 
                [], [], 
                '''                Describes the outcome of the last attempt at acting
                as a graceful restart helper for the neighbor.
                ''',
                'ospfnbrrestarthelperexitreason',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfNbrRestartHelperStatus', REFERENCE_ENUM_CLASS, 'OspfnbrrestarthelperstatusEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfnbrtable.Ospfnbrentry.OspfnbrrestarthelperstatusEnum', 
                [], [], 
                '''                Indicates whether the router is acting
                as a graceful restart helper for the neighbor.
                ''',
                'ospfnbrrestarthelperstatus',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfNbrRtrId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                A 32-bit integer (represented as a type
                IpAddress) uniquely identifying the neighboring
                router in the Autonomous System.
                ''',
                'ospfnbrrtrid',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfNbrState', REFERENCE_ENUM_CLASS, 'OspfnbrstateEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfnbrtable.Ospfnbrentry.OspfnbrstateEnum', 
                [], [], 
                '''                The state of the relationship with this neighbor.
                ''',
                'ospfnbrstate',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfNbrEntry',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfnbrtable' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfnbrtable',
            False, 
            [
            _MetaInfoClassMember('ospfNbrEntry', REFERENCE_LIST, 'Ospfnbrentry' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfnbrtable.Ospfnbrentry', 
                [], [], 
                '''                The information regarding a single neighbor.
                
                Information in this table is persistent and when this object
                is written the entity SHOULD save the change to non-volatile
                
                storage.
                ''',
                'ospfnbrentry',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfNbrTable',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry.OspfvirtnbrrestarthelperexitreasonEnum' : _MetaInfoEnum('OspfvirtnbrrestarthelperexitreasonEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'none':'none',
            'inProgress':'inProgress',
            'completed':'completed',
            'timedOut':'timedOut',
            'topologyChanged':'topologyChanged',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry.OspfvirtnbrrestarthelperstatusEnum' : _MetaInfoEnum('OspfvirtnbrrestarthelperstatusEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'notHelping':'notHelping',
            'helping':'helping',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry.OspfvirtnbrstateEnum' : _MetaInfoEnum('OspfvirtnbrstateEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'down':'down',
            'attempt':'attempt',
            'init':'init',
            'twoWay':'twoWay',
            'exchangeStart':'exchangeStart',
            'exchange':'exchange',
            'loading':'loading',
            'full':'full',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry',
            False, 
            [
            _MetaInfoClassMember('ospfVirtNbrArea', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Transit Area Identifier.
                ''',
                'ospfvirtnbrarea',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfVirtNbrRtrId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                A 32-bit integer uniquely identifying the
                neighboring router in the Autonomous System.
                ''',
                'ospfvirtnbrrtrid',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfVirtNbrEvents', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times this virtual link has
                changed its state or an error has occurred.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, and at other
                times as indicated by the value of ospfDiscontinuityTime.
                ''',
                'ospfvirtnbrevents',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtNbrHelloSuppressed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether Hellos are being suppressed
                to the neighbor.
                ''',
                'ospfvirtnbrhellosuppressed',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtNbrIpAddr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address this virtual neighbor is using.
                ''',
                'ospfvirtnbripaddr',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtNbrLsRetransQLen', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The current length of the retransmission
                queue.
                ''',
                'ospfvirtnbrlsretransqlen',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtNbrOptions', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                A bit mask corresponding to the neighbor's
                options field.
                
                Bit 1, if set, indicates that the system will
                operate on Type of Service metrics other than
                TOS 0.  If zero, the neighbor will ignore all
                metrics except the TOS 0 metric.
                
                Bit 2, if set, indicates that the system is
                network multicast capable, i.e., that it
                implements OSPF multicast routing.
                ''',
                'ospfvirtnbroptions',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtNbrRestartHelperAge', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining time in current OSPF graceful restart
                interval, if the router is acting as a restart
                helper for the neighbor.
                ''',
                'ospfvirtnbrrestarthelperage',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtNbrRestartHelperExitReason', REFERENCE_ENUM_CLASS, 'OspfvirtnbrrestarthelperexitreasonEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry.OspfvirtnbrrestarthelperexitreasonEnum', 
                [], [], 
                '''                Describes the outcome of the last attempt at acting
                as a graceful restart helper for the neighbor.
                ''',
                'ospfvirtnbrrestarthelperexitreason',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtNbrRestartHelperStatus', REFERENCE_ENUM_CLASS, 'OspfvirtnbrrestarthelperstatusEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry.OspfvirtnbrrestarthelperstatusEnum', 
                [], [], 
                '''                Indicates whether the router is acting
                as a graceful restart helper for the neighbor.
                ''',
                'ospfvirtnbrrestarthelperstatus',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtNbrState', REFERENCE_ENUM_CLASS, 'OspfvirtnbrstateEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry.OspfvirtnbrstateEnum', 
                [], [], 
                '''                The state of the virtual neighbor relationship.
                ''',
                'ospfvirtnbrstate',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfVirtNbrEntry',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfvirtnbrtable' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfvirtnbrtable',
            False, 
            [
            _MetaInfoClassMember('ospfVirtNbrEntry', REFERENCE_LIST, 'Ospfvirtnbrentry' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry', 
                [], [], 
                '''                Virtual neighbor information.
                ''',
                'ospfvirtnbrentry',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfVirtNbrTable',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfextlsdbtable.Ospfextlsdbentry.OspfextlsdbtypeEnum' : _MetaInfoEnum('OspfextlsdbtypeEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'asExternalLink':'asExternalLink',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfextlsdbtable.Ospfextlsdbentry' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfextlsdbtable.Ospfextlsdbentry',
            False, 
            [
            _MetaInfoClassMember('ospfExtLsdbType', REFERENCE_ENUM_CLASS, 'OspfextlsdbtypeEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfextlsdbtable.Ospfextlsdbentry.OspfextlsdbtypeEnum', 
                [], [], 
                '''                The type of the link state advertisement.
                Each link state type has a separate advertisement
                format.
                ''',
                'ospfextlsdbtype',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfExtLsdbLsid', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Link State ID is an LS Type Specific field
                containing either a Router ID or an IP address;
                it identifies the piece of the routing domain
                that is being described by the advertisement.
                ''',
                'ospfextlsdblsid',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfExtLsdbRouterId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The 32-bit number that uniquely identifies the
                originating router in the Autonomous System.
                ''',
                'ospfextlsdbrouterid',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfExtLsdbAdvertisement', ATTRIBUTE, 'str' , None, None, 
                [(36, None)], [], 
                '''                The entire link state advertisement, including
                its header.
                ''',
                'ospfextlsdbadvertisement',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfExtLsdbAge', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This field is the age of the link state
                advertisement in seconds.
                ''',
                'ospfextlsdbage',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfExtLsdbChecksum', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This field is the checksum of the complete
                contents of the advertisement, excepting the
                age field.  The age field is excepted so that
                an advertisement's age can be incremented
                without updating the checksum.  The checksum
                used is the same that is used for ISO
                connectionless datagrams; it is commonly referred
                to as the Fletcher checksum.
                ''',
                'ospfextlsdbchecksum',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfExtLsdbSequence', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The sequence number field is a signed 32-bit
                integer.  It starts with the value '80000001'h,
                or -'7FFFFFFF'h, and increments until '7FFFFFFF'h.
                Thus, a typical sequence number will be very negative.
                It is used to detect old and duplicate link state
                advertisements.  The space of sequence numbers is linearly
                ordered.  The larger the sequence number, the more recent
                the advertisement.
                ''',
                'ospfextlsdbsequence',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfExtLsdbEntry',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfextlsdbtable' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfextlsdbtable',
            False, 
            [
            _MetaInfoClassMember('ospfExtLsdbEntry', REFERENCE_LIST, 'Ospfextlsdbentry' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfextlsdbtable.Ospfextlsdbentry', 
                [], [], 
                '''                A single link state advertisement.
                ''',
                'ospfextlsdbentry',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfExtLsdbTable',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry.OspfareaaggregateeffectEnum' : _MetaInfoEnum('OspfareaaggregateeffectEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'advertiseMatching':'advertiseMatching',
            'doNotAdvertiseMatching':'doNotAdvertiseMatching',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry.OspfareaaggregatelsdbtypeEnum' : _MetaInfoEnum('OspfareaaggregatelsdbtypeEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'summaryLink':'summaryLink',
            'nssaExternalLink':'nssaExternalLink',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry',
            False, 
            [
            _MetaInfoClassMember('ospfAreaAggregateAreaID', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The area within which the address aggregate is to be
                found.
                ''',
                'ospfareaaggregateareaid',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfAreaAggregateLsdbType', REFERENCE_ENUM_CLASS, 'OspfareaaggregatelsdbtypeEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry.OspfareaaggregatelsdbtypeEnum', 
                [], [], 
                '''                The type of the address aggregate.  This field
                specifies the Lsdb type that this address
                aggregate applies to.
                ''',
                'ospfareaaggregatelsdbtype',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfAreaAggregateNet', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the net or subnet indicated
                by the range.
                ''',
                'ospfareaaggregatenet',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfAreaAggregateMask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The subnet mask that pertains to the net or
                subnet.
                ''',
                'ospfareaaggregatemask',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfAreaAggregateEffect', REFERENCE_ENUM_CLASS, 'OspfareaaggregateeffectEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry.OspfareaaggregateeffectEnum', 
                [], [], 
                '''                Subnets subsumed by ranges either trigger the
                advertisement of the indicated aggregate
                (advertiseMatching) or result in the subnet's not
                being advertised at all outside the area.
                ''',
                'ospfareaaggregateeffect',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAreaAggregateExtRouteTag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                External route tag to be included in NSSA (type-7)
                LSAs.
                ''',
                'ospfareaaggregateextroutetag',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAreaAggregateStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object permits management of the table by
                facilitating actions such as row creation,
                construction, and destruction.
                
                The value of this object has no effect on
                whether other objects in this conceptual row can be
                modified.
                ''',
                'ospfareaaggregatestatus',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfAreaAggregateEntry',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfareaaggregatetable' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfareaaggregatetable',
            False, 
            [
            _MetaInfoClassMember('ospfAreaAggregateEntry', REFERENCE_LIST, 'Ospfareaaggregateentry' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry', 
                [], [], 
                '''                A single area aggregate entry.
                
                Information in this table is persistent and when this object
                is written the entity SHOULD save the change to non-volatile
                storage.
                ''',
                'ospfareaaggregateentry',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfAreaAggregateTable',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospflocallsdbtable.Ospflocallsdbentry.OspflocallsdbtypeEnum' : _MetaInfoEnum('OspflocallsdbtypeEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'localOpaqueLink':'localOpaqueLink',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospflocallsdbtable.Ospflocallsdbentry' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospflocallsdbtable.Ospflocallsdbentry',
            False, 
            [
            _MetaInfoClassMember('ospfLocalLsdbIpAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the interface from
                which the LSA was received if the interface is
                numbered.
                ''',
                'ospflocallsdbipaddress',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfLocalLsdbAddressLessIf', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The interface index of the interface from
                which the LSA was received if the interface is
                unnumbered.
                ''',
                'ospflocallsdbaddresslessif',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfLocalLsdbType', REFERENCE_ENUM_CLASS, 'OspflocallsdbtypeEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospflocallsdbtable.Ospflocallsdbentry.OspflocallsdbtypeEnum', 
                [], [], 
                '''                The type of the link state advertisement.
                Each link state type has a separate
                advertisement format.
                ''',
                'ospflocallsdbtype',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfLocalLsdbLsid', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Link State ID is an LS Type Specific field
                containing a 32-bit identifier in IP address format;
                it identifies the piece of the routing domain
                that is being described by the advertisement.
                ''',
                'ospflocallsdblsid',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfLocalLsdbRouterId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The 32-bit number that uniquely identifies the
                originating router in the Autonomous System.
                ''',
                'ospflocallsdbrouterid',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfLocalLsdbAdvertisement', ATTRIBUTE, 'str' , None, None, 
                [(1, 65535)], [], 
                '''                The entire link state advertisement, including
                its header.
                
                Note that for variable length LSAs, SNMP agents
                may not be able to return the largest string size.
                ''',
                'ospflocallsdbadvertisement',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfLocalLsdbAge', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This field is the age of the link state
                advertisement in seconds.
                ''',
                'ospflocallsdbage',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfLocalLsdbChecksum', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This field is the checksum of the complete
                contents of the advertisement, excepting the
                age field.  The age field is excepted so that
                an advertisement's age can be incremented
                without updating the checksum.  The checksum
                used is the same that is used for ISO
                connectionless datagrams; it is commonly referred
                to as the Fletcher checksum.
                ''',
                'ospflocallsdbchecksum',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfLocalLsdbSequence', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The sequence number field is a signed 32-bit
                integer.  It starts with the value '80000001'h,
                or -'7FFFFFFF'h, and increments until '7FFFFFFF'h.
                Thus, a typical sequence number will be very negative.
                It is used to detect old and duplicate link state
                advertisements.  The space of sequence numbers is linearly
                ordered.  The larger the sequence number, the more recent
                the advertisement.
                ''',
                'ospflocallsdbsequence',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfLocalLsdbEntry',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospflocallsdbtable' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospflocallsdbtable',
            False, 
            [
            _MetaInfoClassMember('ospfLocalLsdbEntry', REFERENCE_LIST, 'Ospflocallsdbentry' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospflocallsdbtable.Ospflocallsdbentry', 
                [], [], 
                '''                A single link state advertisement.
                ''',
                'ospflocallsdbentry',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfLocalLsdbTable',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry.OspfvirtlocallsdbtypeEnum' : _MetaInfoEnum('OspfvirtlocallsdbtypeEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'localOpaqueLink':'localOpaqueLink',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry',
            False, 
            [
            _MetaInfoClassMember('ospfVirtLocalLsdbTransitArea', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The transit area that the virtual link
                traverses.  By definition, this is not 0.0.0.0.
                ''',
                'ospfvirtlocallsdbtransitarea',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfVirtLocalLsdbNeighbor', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Router ID of the virtual neighbor.
                ''',
                'ospfvirtlocallsdbneighbor',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfVirtLocalLsdbType', REFERENCE_ENUM_CLASS, 'OspfvirtlocallsdbtypeEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry.OspfvirtlocallsdbtypeEnum', 
                [], [], 
                '''                The type of the link state advertisement.
                Each link state type has a separate
                advertisement format.
                ''',
                'ospfvirtlocallsdbtype',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfVirtLocalLsdbLsid', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Link State ID is an LS Type Specific field
                containing a 32-bit identifier in IP address format;
                it identifies the piece of the routing domain
                that is being described by the advertisement.
                ''',
                'ospfvirtlocallsdblsid',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfVirtLocalLsdbRouterId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The 32-bit number that uniquely identifies the
                originating router in the Autonomous System.
                ''',
                'ospfvirtlocallsdbrouterid',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfVirtLocalLsdbAdvertisement', ATTRIBUTE, 'str' , None, None, 
                [(1, 65535)], [], 
                '''                The entire link state advertisement, including
                its header.
                ''',
                'ospfvirtlocallsdbadvertisement',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtLocalLsdbAge', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This field is the age of the link state
                advertisement in seconds.
                ''',
                'ospfvirtlocallsdbage',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtLocalLsdbChecksum', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This field is the checksum of the complete
                contents of the advertisement, excepting the
                age field.  The age field is excepted so that
                
                an advertisement's age can be incremented
                without updating the checksum.  The checksum
                used is the same that is used for ISO
                connectionless datagrams; it is commonly
                referred to as the Fletcher checksum.
                ''',
                'ospfvirtlocallsdbchecksum',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtLocalLsdbSequence', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The sequence number field is a signed 32-bit
                integer.  It starts with the value '80000001'h,
                or -'7FFFFFFF'h, and increments until '7FFFFFFF'h.
                Thus, a typical sequence number will be very negative.
                It is used to detect old and duplicate link state
                advertisements.  The space of sequence numbers is linearly
                ordered.  The larger the sequence number, the more recent
                the advertisement.
                ''',
                'ospfvirtlocallsdbsequence',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfVirtLocalLsdbEntry',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfvirtlocallsdbtable' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfvirtlocallsdbtable',
            False, 
            [
            _MetaInfoClassMember('ospfVirtLocalLsdbEntry', REFERENCE_LIST, 'Ospfvirtlocallsdbentry' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry', 
                [], [], 
                '''                A single link state advertisement.
                ''',
                'ospfvirtlocallsdbentry',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfVirtLocalLsdbTable',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfaslsdbtable.Ospfaslsdbentry.OspfaslsdbtypeEnum' : _MetaInfoEnum('OspfaslsdbtypeEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'asExternalLink':'asExternalLink',
            'asOpaqueLink':'asOpaqueLink',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfaslsdbtable.Ospfaslsdbentry' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfaslsdbtable.Ospfaslsdbentry',
            False, 
            [
            _MetaInfoClassMember('ospfAsLsdbType', REFERENCE_ENUM_CLASS, 'OspfaslsdbtypeEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfaslsdbtable.Ospfaslsdbentry.OspfaslsdbtypeEnum', 
                [], [], 
                '''                The type of the link state advertisement.
                Each link state type has a separate
                advertisement format.
                ''',
                'ospfaslsdbtype',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfAsLsdbLsid', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The Link State ID is an LS Type Specific field
                containing either a Router ID or an IP address;
                
                it identifies the piece of the routing domain
                that is being described by the advertisement.
                ''',
                'ospfaslsdblsid',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfAsLsdbRouterId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The 32-bit number that uniquely identifies the
                originating router in the Autonomous System.
                ''',
                'ospfaslsdbrouterid',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfAsLsdbAdvertisement', ATTRIBUTE, 'str' , None, None, 
                [(1, 65535)], [], 
                '''                The entire link state advertisement, including
                its header.
                ''',
                'ospfaslsdbadvertisement',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAsLsdbAge', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This field is the age of the link state
                advertisement in seconds.
                ''',
                'ospfaslsdbage',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAsLsdbChecksum', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This field is the checksum of the complete
                contents of the advertisement, excepting the
                age field.  The age field is excepted so that
                an advertisement's age can be incremented
                without updating the checksum.  The checksum
                used is the same that is used for ISO
                connectionless datagrams; it is commonly referred
                to as the Fletcher checksum.
                ''',
                'ospfaslsdbchecksum',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAsLsdbSequence', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The sequence number field is a signed 32-bit
                integer.  It starts with the value '80000001'h,
                or -'7FFFFFFF'h, and increments until '7FFFFFFF'h.
                Thus, a typical sequence number will be very negative.
                It is used to detect old and duplicate link state
                advertisements.  The space of sequence numbers is linearly
                ordered.  The larger the sequence number, the more recent
                the advertisement.
                ''',
                'ospfaslsdbsequence',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfAsLsdbEntry',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfaslsdbtable' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfaslsdbtable',
            False, 
            [
            _MetaInfoClassMember('ospfAsLsdbEntry', REFERENCE_LIST, 'Ospfaslsdbentry' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfaslsdbtable.Ospfaslsdbentry', 
                [], [], 
                '''                A single link state advertisement.
                ''',
                'ospfaslsdbentry',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfAsLsdbTable',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfarealsacounttable.Ospfarealsacountentry.OspfarealsacountlsatypeEnum' : _MetaInfoEnum('OspfarealsacountlsatypeEnum', 'ydk.models.cisco_ios_xe.OSPF_MIB',
        {
            'routerLink':'routerLink',
            'networkLink':'networkLink',
            'summaryLink':'summaryLink',
            'asSummaryLink':'asSummaryLink',
            'multicastLink':'multicastLink',
            'nssaExternalLink':'nssaExternalLink',
            'areaOpaqueLink':'areaOpaqueLink',
        }, 'OSPF-MIB', _yang_ns._namespaces['OSPF-MIB']),
    'OspfMib.Ospfarealsacounttable.Ospfarealsacountentry' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfarealsacounttable.Ospfarealsacountentry',
            False, 
            [
            _MetaInfoClassMember('ospfAreaLsaCountAreaId', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                This entry Area ID.
                ''',
                'ospfarealsacountareaid',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfAreaLsaCountLsaType', REFERENCE_ENUM_CLASS, 'OspfarealsacountlsatypeEnum' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfarealsacounttable.Ospfarealsacountentry.OspfarealsacountlsatypeEnum', 
                [], [], 
                '''                This entry LSA type.
                ''',
                'ospfarealsacountlsatype',
                'OSPF-MIB', True),
            _MetaInfoClassMember('ospfAreaLsaCountNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of LSAs of a given type for a given area.
                ''',
                'ospfarealsacountnumber',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfAreaLsaCountEntry',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib.Ospfarealsacounttable' : {
        'meta_info' : _MetaInfoClass('OspfMib.Ospfarealsacounttable',
            False, 
            [
            _MetaInfoClassMember('ospfAreaLsaCountEntry', REFERENCE_LIST, 'Ospfarealsacountentry' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfarealsacounttable.Ospfarealsacountentry', 
                [], [], 
                '''                An entry with a number of link advertisements
                
                of a given type for a given area.
                ''',
                'ospfarealsacountentry',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'ospfAreaLsaCountTable',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
    'OspfMib' : {
        'meta_info' : _MetaInfoClass('OspfMib',
            False, 
            [
            _MetaInfoClassMember('ospfAreaAggregateTable', REFERENCE_CLASS, 'Ospfareaaggregatetable' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfareaaggregatetable', 
                [], [], 
                '''                The Area Aggregate Table acts as an adjunct
                to the Area Table.  It describes those address aggregates
                that are configured to be propagated from an area.
                Its purpose is to reduce the amount of information
                that is known beyond an Area's borders.
                
                It contains a set of IP address ranges
                specified by an IP address/IP network mask pair.
                For example, a class B address range of X.X.X.X
                with a network mask of 255.255.0.0 includes all IP
                addresses from X.X.0.0 to X.X.255.255.
                
                Note that if ranges are configured such that one range
                subsumes another range (e.g., 10.0.0.0 mask 255.0.0.0
                and 10.1.0.0 mask 255.255.0.0),
                the most specific match is the preferred one.
                ''',
                'ospfareaaggregatetable',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAreaLsaCountTable', REFERENCE_CLASS, 'Ospfarealsacounttable' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfarealsacounttable', 
                [], [], 
                '''                This table maintains per-area, per-LSA-type counters
                ''',
                'ospfarealsacounttable',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAreaRangeTable', REFERENCE_CLASS, 'Ospfarearangetable' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfarearangetable', 
                [], [], 
                '''                The Address Range Table acts as an adjunct to the Area
                Table.  It describes those Address Range Summaries that
                are configured to be propagated from an Area to reduce
                the amount of information about it that is known beyond
                its borders.  It contains a set of IP address ranges
                specified by an IP address/IP network mask pair.
                For example, class B address range of X.X.X.X
                with a network mask of 255.255.0.0 includes all IP
                addresses from X.X.0.0 to X.X.255.255.
                
                Note that this table is obsoleted and is replaced
                by the Area Aggregate Table.
                ''',
                'ospfarearangetable',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAreaTable', REFERENCE_CLASS, 'Ospfareatable' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfareatable', 
                [], [], 
                '''                Information describing the configured parameters and
                cumulative statistics of the router's attached areas.
                The interfaces and virtual links are configured
                as part of these areas.  Area 0.0.0.0, by definition,
                is the backbone area.
                ''',
                'ospfareatable',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfAsLsdbTable', REFERENCE_CLASS, 'Ospfaslsdbtable' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfaslsdbtable', 
                [], [], 
                '''                The OSPF Process's AS-scope LSA link state database.
                The database contains the AS-scope Link State
                Advertisements from throughout the areas that
                the device is attached to.
                
                This table is identical to the OSPF LSDB Table
                in format, but contains only AS-scope Link State
                Advertisements.  The purpose is to allow AS-scope
                LSAs to be displayed once for the router rather
                than once in each non-stub area.
                ''',
                'ospfaslsdbtable',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfExtLsdbTable', REFERENCE_CLASS, 'Ospfextlsdbtable' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfextlsdbtable', 
                [], [], 
                '''                The OSPF Process's external LSA link state database.
                
                This table is identical to the OSPF LSDB Table
                in format, but contains only external link state
                advertisements.  The purpose is to allow external
                
                LSAs to be displayed once for the router rather
                than once in each non-stub area.
                
                Note that external LSAs are also in the AS-scope link state
                database.
                ''',
                'ospfextlsdbtable',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfGeneralGroup', REFERENCE_CLASS, 'Ospfgeneralgroup' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfgeneralgroup', 
                [], [], 
                '''                ''',
                'ospfgeneralgroup',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfHostTable', REFERENCE_CLASS, 'Ospfhosttable' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfhosttable', 
                [], [], 
                '''                The Host/Metric Table indicates what hosts are directly
                
                attached to the router, what metrics and types
                of service should be advertised for them,
                and what areas they are found within.
                ''',
                'ospfhosttable',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfMetricTable', REFERENCE_CLASS, 'Ospfifmetrictable' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfifmetrictable', 
                [], [], 
                '''                The Metric Table describes the metrics to be advertised
                for a specified interface at the various types of service.
                As such, this table is an adjunct of the OSPF Interface
                Table.
                
                Types of service, as defined by RFC 791, have the ability
                to request low delay, high bandwidth, or reliable linkage.
                
                For the purposes of this specification, the measure of
                bandwidth:
                
                Metric = referenceBandwidth / ifSpeed
                
                is the default value.
                The default reference bandwidth is 10^8.
                For multiple link interfaces, note that ifSpeed is the sum
                of the individual link speeds.  This yields a number having
                the following typical values:
                
                Network Type/bit rate   Metric
                
                >= 100 MBPS                 1
                Ethernet/802.3             10
                E1                         48
                T1 (ESF)                   65
                64 KBPS                    1562
                56 KBPS                    1785
                19.2 KBPS                  5208
                9.6 KBPS                   10416
                
                Routes that are not specified use the default
                (TOS 0) metric.
                
                Note that the default reference bandwidth can be configured
                using the general group object ospfReferenceBandwidth.
                ''',
                'ospfifmetrictable',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfIfTable', REFERENCE_CLASS, 'Ospfiftable' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfiftable', 
                [], [], 
                '''                The OSPF Interface Table describes the interfaces
                from the viewpoint of OSPF.
                It augments the ipAddrTable with OSPF specific information.
                ''',
                'ospfiftable',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfLocalLsdbTable', REFERENCE_CLASS, 'Ospflocallsdbtable' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospflocallsdbtable', 
                [], [], 
                '''                The OSPF Process's link-local link state database
                for non-virtual links.
                This table is identical to the OSPF LSDB Table
                in format, but contains only link-local Link State
                Advertisements for non-virtual links.  The purpose is
                to allow link-local LSAs to be displayed for each
                non-virtual interface.  This table is implemented to
                support type-9 LSAs that are defined
                in 'The OSPF Opaque LSA Option'.
                ''',
                'ospflocallsdbtable',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfLsdbTable', REFERENCE_CLASS, 'Ospflsdbtable' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospflsdbtable', 
                [], [], 
                '''                The OSPF Process's link state database (LSDB).
                The LSDB contains the link state advertisements
                from throughout the areas that the device is attached to.
                ''',
                'ospflsdbtable',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfNbrTable', REFERENCE_CLASS, 'Ospfnbrtable' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfnbrtable', 
                [], [], 
                '''                A table describing all non-virtual neighbors
                in the locality of the OSPF router.
                ''',
                'ospfnbrtable',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfStubAreaTable', REFERENCE_CLASS, 'Ospfstubareatable' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfstubareatable', 
                [], [], 
                '''                The set of metrics that will be advertised
                by a default Area Border Router into a stub area.
                ''',
                'ospfstubareatable',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtIfTable', REFERENCE_CLASS, 'Ospfvirtiftable' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfvirtiftable', 
                [], [], 
                '''                Information about this router's virtual interfaces
                that the OSPF Process is configured to carry on.
                ''',
                'ospfvirtiftable',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtLocalLsdbTable', REFERENCE_CLASS, 'Ospfvirtlocallsdbtable' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfvirtlocallsdbtable', 
                [], [], 
                '''                The OSPF Process's link-local link state database
                for virtual links.
                
                This table is identical to the OSPF LSDB Table
                in format, but contains only link-local Link State
                Advertisements for virtual links.  The purpose is to
                allow link-local LSAs to be displayed for each virtual
                interface.  This table is implemented to support type-9 LSAs
                that are defined in 'The OSPF Opaque LSA Option'.
                ''',
                'ospfvirtlocallsdbtable',
                'OSPF-MIB', False),
            _MetaInfoClassMember('ospfVirtNbrTable', REFERENCE_CLASS, 'Ospfvirtnbrtable' , 'ydk.models.cisco_ios_xe.OSPF_MIB', 'OspfMib.Ospfvirtnbrtable', 
                [], [], 
                '''                This table describes all virtual neighbors.
                Since virtual links are configured
                in the Virtual Interface Table, this table is read-only.
                ''',
                'ospfvirtnbrtable',
                'OSPF-MIB', False),
            ],
            'OSPF-MIB',
            'OSPF-MIB',
            _yang_ns._namespaces['OSPF-MIB'],
        'ydk.models.cisco_ios_xe.OSPF_MIB'
        ),
    },
}
_meta_table['OspfMib.Ospfareatable.Ospfareaentry']['meta_info'].parent =_meta_table['OspfMib.Ospfareatable']['meta_info']
_meta_table['OspfMib.Ospfstubareatable.Ospfstubareaentry']['meta_info'].parent =_meta_table['OspfMib.Ospfstubareatable']['meta_info']
_meta_table['OspfMib.Ospflsdbtable.Ospflsdbentry']['meta_info'].parent =_meta_table['OspfMib.Ospflsdbtable']['meta_info']
_meta_table['OspfMib.Ospfarearangetable.Ospfarearangeentry']['meta_info'].parent =_meta_table['OspfMib.Ospfarearangetable']['meta_info']
_meta_table['OspfMib.Ospfhosttable.Ospfhostentry']['meta_info'].parent =_meta_table['OspfMib.Ospfhosttable']['meta_info']
_meta_table['OspfMib.Ospfiftable.Ospfifentry']['meta_info'].parent =_meta_table['OspfMib.Ospfiftable']['meta_info']
_meta_table['OspfMib.Ospfifmetrictable.Ospfifmetricentry']['meta_info'].parent =_meta_table['OspfMib.Ospfifmetrictable']['meta_info']
_meta_table['OspfMib.Ospfvirtiftable.Ospfvirtifentry']['meta_info'].parent =_meta_table['OspfMib.Ospfvirtiftable']['meta_info']
_meta_table['OspfMib.Ospfnbrtable.Ospfnbrentry']['meta_info'].parent =_meta_table['OspfMib.Ospfnbrtable']['meta_info']
_meta_table['OspfMib.Ospfvirtnbrtable.Ospfvirtnbrentry']['meta_info'].parent =_meta_table['OspfMib.Ospfvirtnbrtable']['meta_info']
_meta_table['OspfMib.Ospfextlsdbtable.Ospfextlsdbentry']['meta_info'].parent =_meta_table['OspfMib.Ospfextlsdbtable']['meta_info']
_meta_table['OspfMib.Ospfareaaggregatetable.Ospfareaaggregateentry']['meta_info'].parent =_meta_table['OspfMib.Ospfareaaggregatetable']['meta_info']
_meta_table['OspfMib.Ospflocallsdbtable.Ospflocallsdbentry']['meta_info'].parent =_meta_table['OspfMib.Ospflocallsdbtable']['meta_info']
_meta_table['OspfMib.Ospfvirtlocallsdbtable.Ospfvirtlocallsdbentry']['meta_info'].parent =_meta_table['OspfMib.Ospfvirtlocallsdbtable']['meta_info']
_meta_table['OspfMib.Ospfaslsdbtable.Ospfaslsdbentry']['meta_info'].parent =_meta_table['OspfMib.Ospfaslsdbtable']['meta_info']
_meta_table['OspfMib.Ospfarealsacounttable.Ospfarealsacountentry']['meta_info'].parent =_meta_table['OspfMib.Ospfarealsacounttable']['meta_info']
_meta_table['OspfMib.Ospfgeneralgroup']['meta_info'].parent =_meta_table['OspfMib']['meta_info']
_meta_table['OspfMib.Ospfareatable']['meta_info'].parent =_meta_table['OspfMib']['meta_info']
_meta_table['OspfMib.Ospfstubareatable']['meta_info'].parent =_meta_table['OspfMib']['meta_info']
_meta_table['OspfMib.Ospflsdbtable']['meta_info'].parent =_meta_table['OspfMib']['meta_info']
_meta_table['OspfMib.Ospfarearangetable']['meta_info'].parent =_meta_table['OspfMib']['meta_info']
_meta_table['OspfMib.Ospfhosttable']['meta_info'].parent =_meta_table['OspfMib']['meta_info']
_meta_table['OspfMib.Ospfiftable']['meta_info'].parent =_meta_table['OspfMib']['meta_info']
_meta_table['OspfMib.Ospfifmetrictable']['meta_info'].parent =_meta_table['OspfMib']['meta_info']
_meta_table['OspfMib.Ospfvirtiftable']['meta_info'].parent =_meta_table['OspfMib']['meta_info']
_meta_table['OspfMib.Ospfnbrtable']['meta_info'].parent =_meta_table['OspfMib']['meta_info']
_meta_table['OspfMib.Ospfvirtnbrtable']['meta_info'].parent =_meta_table['OspfMib']['meta_info']
_meta_table['OspfMib.Ospfextlsdbtable']['meta_info'].parent =_meta_table['OspfMib']['meta_info']
_meta_table['OspfMib.Ospfareaaggregatetable']['meta_info'].parent =_meta_table['OspfMib']['meta_info']
_meta_table['OspfMib.Ospflocallsdbtable']['meta_info'].parent =_meta_table['OspfMib']['meta_info']
_meta_table['OspfMib.Ospfvirtlocallsdbtable']['meta_info'].parent =_meta_table['OspfMib']['meta_info']
_meta_table['OspfMib.Ospfaslsdbtable']['meta_info'].parent =_meta_table['OspfMib']['meta_info']
_meta_table['OspfMib.Ospfarealsacounttable']['meta_info'].parent =_meta_table['OspfMib']['meta_info']
