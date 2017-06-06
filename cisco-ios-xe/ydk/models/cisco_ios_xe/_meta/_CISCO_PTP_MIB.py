


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'ClockprofiletypeEnum' : _MetaInfoEnum('ClockprofiletypeEnum', 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB',
        {
            'default':'default',
            'telecom':'telecom',
            'vendorspecific':'vendorspecific',
        }, 'CISCO-PTP-MIB', _yang_ns._namespaces['CISCO-PTP-MIB']),
    'ClocktxmodetypeEnum' : _MetaInfoEnum('ClocktxmodetypeEnum', 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB',
        {
            'unicast':'unicast',
            'multicast':'multicast',
            'multicastmix':'multicastmix',
        }, 'CISCO-PTP-MIB', _yang_ns._namespaces['CISCO-PTP-MIB']),
    'ClockqualityaccuracytypeEnum' : _MetaInfoEnum('ClockqualityaccuracytypeEnum', 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB',
        {
            'reserved00':'reserved00',
            'nanoSecond25':'nanoSecond25',
            'nanoSecond100':'nanoSecond100',
            'nanoSecond250':'nanoSecond250',
            'microSec1':'microSec1',
            'microSec2dot5':'microSec2dot5',
            'microSec10':'microSec10',
            'microSec25':'microSec25',
            'microSec100':'microSec100',
            'microSec250':'microSec250',
            'milliSec1':'milliSec1',
            'milliSec2dot5':'milliSec2dot5',
            'milliSec10':'milliSec10',
            'milliSec25':'milliSec25',
            'milliSec100':'milliSec100',
            'milliSec250':'milliSec250',
            'second1':'second1',
            'second10':'second10',
            'secondGreater10':'secondGreater10',
            'unknown':'unknown',
            'reserved255':'reserved255',
        }, 'CISCO-PTP-MIB', _yang_ns._namespaces['CISCO-PTP-MIB']),
    'ClocktimesourcetypeEnum' : _MetaInfoEnum('ClocktimesourcetypeEnum', 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB',
        {
            'atomicClock':'atomicClock',
            'gps':'gps',
            'terrestrialRadio':'terrestrialRadio',
            'ptp':'ptp',
            'ntp':'ntp',
            'handSet':'handSet',
            'other':'other',
            'internalOsillator':'internalOsillator',
        }, 'CISCO-PTP-MIB', _yang_ns._namespaces['CISCO-PTP-MIB']),
    'ClockportstateEnum' : _MetaInfoEnum('ClockportstateEnum', 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB',
        {
            'initializing':'initializing',
            'faulty':'faulty',
            'disabled':'disabled',
            'listening':'listening',
            'preMaster':'preMaster',
            'master':'master',
            'passive':'passive',
            'uncalibrated':'uncalibrated',
            'slave':'slave',
        }, 'CISCO-PTP-MIB', _yang_ns._namespaces['CISCO-PTP-MIB']),
    'ClocktypeEnum' : _MetaInfoEnum('ClocktypeEnum', 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB',
        {
            'ordinaryClock':'ordinaryClock',
            'boundaryClock':'boundaryClock',
            'transparentClock':'transparentClock',
            'boundaryNode':'boundaryNode',
        }, 'CISCO-PTP-MIB', _yang_ns._namespaces['CISCO-PTP-MIB']),
    'ClockstatetypeEnum' : _MetaInfoEnum('ClockstatetypeEnum', 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB',
        {
            'freerun':'freerun',
            'holdover':'holdover',
            'acquiring':'acquiring',
            'frequencyLocked':'frequencyLocked',
            'phaseAligned':'phaseAligned',
        }, 'CISCO-PTP-MIB', _yang_ns._namespaces['CISCO-PTP-MIB']),
    'ClockmechanismtypeEnum' : _MetaInfoEnum('ClockmechanismtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB',
        {
            'e2e':'e2e',
            'p2p':'p2p',
            'disabled':'disabled',
        }, 'CISCO-PTP-MIB', _yang_ns._namespaces['CISCO-PTP-MIB']),
    'ClockroletypeEnum' : _MetaInfoEnum('ClockroletypeEnum', 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB',
        {
            'master':'master',
            'slave':'slave',
        }, 'CISCO-PTP-MIB', _yang_ns._namespaces['CISCO-PTP-MIB']),
    'CiscoPtpMib.Ciscoptpmibsysteminfo' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Ciscoptpmibsysteminfo',
            False, 
            [
            _MetaInfoClassMember('cPtpSystemProfile', REFERENCE_ENUM_CLASS, 'ClockprofiletypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockprofiletypeEnum', 
                [], [], 
                '''                This object specifies the PTP Profile implemented on the
                system.
                ''',
                'cptpsystemprofile',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'ciscoPtpMIBSystemInfo',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpsystemtable.Cptpsystementry' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpsystemtable.Cptpsystementry',
            False, 
            [
            _MetaInfoClassMember('cPtpDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the domain number used to create logical
                group of PTP devices. The Clock Domain is a logical group of
                clocks and devices that synchronize with each other using the
                PTP protocol.
                
                
                0           Default domain
                1           Alternate domain 1
                2           Alternate domain 2
                3           Alternate domain 3
                4 - 127     User-defined domains
                128 - 255   Reserved
                ''',
                'cptpdomainindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the instance of the Clock for this
                domain.
                ''',
                'cptpinstanceindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpDomainClockPortPhysicalInterfacesTotal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the total number of clock port Physical
                interfaces configured within a domain instance for PTP
                communications.
                ''',
                'cptpdomainclockportphysicalinterfacestotal',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpDomainClockPortsTotal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the total number of clock ports
                configured within a domain.
                ''',
                'cptpdomainclockportstotal',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpSystemEntry',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpsystemtable' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpsystemtable',
            False, 
            [
            _MetaInfoClassMember('cPtpSystemEntry', REFERENCE_LIST, 'Cptpsystementry' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpsystemtable.Cptpsystementry', 
                [], [], 
                '''                An entry in the table, containing count information about a
                single domain. New row entries are added when the PTP clock for
                this domain is configured, while the unconfiguration of the PTP
                clock removes it.
                ''',
                'cptpsystementry',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpSystemTable',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpsystemdomaintable.Cptpsystemdomainentry' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpsystemdomaintable.Cptpsystemdomainentry',
            False, 
            [
            _MetaInfoClassMember('cPtpSystemDomainClockTypeIndex', REFERENCE_ENUM_CLASS, 'ClocktypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClocktypeEnum', 
                [], [], 
                '''                This object specifies the clock type as defined in the
                Textual convention description.
                ''',
                'cptpsystemdomainclocktypeindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpSystemDomainTotals', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the  total number of PTP domains for this
                particular clock type configured in this node.
                ''',
                'cptpsystemdomaintotals',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpSystemDomainEntry',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpsystemdomaintable' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpsystemdomaintable',
            False, 
            [
            _MetaInfoClassMember('cPtpSystemDomainEntry', REFERENCE_LIST, 'Cptpsystemdomainentry' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpsystemdomaintable.Cptpsystemdomainentry', 
                [], [], 
                '''                An entry in the table, containing information about a single
                clock mode for the PTP system. A row entry gets added when PTP
                clocks are configured on the router.
                ''',
                'cptpsystemdomainentry',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpSystemDomainTable',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclocknodetable.Cptpclocknodeentry' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclocknodetable.Cptpclocknodeentry',
            False, 
            [
            _MetaInfoClassMember('cPtpClockDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the  domain number used to create logical
                group of PTP devices.
                ''',
                'cptpclockdomainindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockTypeIndex', REFERENCE_ENUM_CLASS, 'ClocktypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClocktypeEnum', 
                [], [], 
                '''                This object specifies the clock type as defined in the
                Textual convention description.
                ''',
                'cptpclocktypeindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the instance of the Clock for this clock
                type for the given domain.
                ''',
                'cptpclockinstanceindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockInput1ppsEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the node is enabled for PTP input
                clocking using the 1pps interface.
                ''',
                'cptpclockinput1ppsenabled',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockInput1ppsInterface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the 1pps interface used for PTP input
                clocking.
                ''',
                'cptpclockinput1ppsinterface',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockInputFrequencyEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether enabled for Frequency input using
                the 1.544 Mhz, 2.048 Mhz, or 10Mhz timing interface.
                ''',
                'cptpclockinputfrequencyenabled',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockOutput1ppsEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the node is enabled for PTP input
                clocking using the 1pps interface.
                ''',
                'cptpclockoutput1ppsenabled',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockOutput1ppsInterface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the 1pps interface used for PTP output
                clocking.
                ''',
                'cptpclockoutput1ppsinterface',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockOutput1ppsOffsetEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether an offset is configured in order
                to compensate for a known phase error such as network
                asymmetry.
                ''',
                'cptpclockoutput1ppsoffsetenabled',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockOutput1ppsOffsetNegative', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the added (fixed) offset to the
                1pps output is negative or not.  When object returns TRUE the
                offset is negative and when object returns FALSE the offset is
                positive.
                ''',
                'cptpclockoutput1ppsoffsetnegative',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockOutput1ppsOffsetValue', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the fixed offset value configured to be
                added for the 1pps output.
                ''',
                'cptpclockoutput1ppsoffsetvalue',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockTODEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the node is enabled for TOD.
                ''',
                'cptpclocktodenabled',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockTODInterface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the interface used for PTP TOD.
                ''',
                'cptpclocktodinterface',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockNodeEntry',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclocknodetable' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclocknodetable',
            False, 
            [
            _MetaInfoClassMember('cPtpClockNodeEntry', REFERENCE_LIST, 'Cptpclocknodeentry' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclocknodetable.Cptpclocknodeentry', 
                [], [], 
                '''                An entry in the table, containing information about a single
                domain. A entry is added when a new PTP clock domain is
                configured on the router.
                ''',
                'cptpclocknodeentry',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockNodeTable',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclockcurrentdstable.Cptpclockcurrentdsentry' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclockcurrentdstable.Cptpclockcurrentdsentry',
            False, 
            [
            _MetaInfoClassMember('cPtpClockCurrentDSDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the domain number used to create logical
                group of PTP devices.
                ''',
                'cptpclockcurrentdsdomainindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockCurrentDSClockTypeIndex', REFERENCE_ENUM_CLASS, 'ClocktypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClocktypeEnum', 
                [], [], 
                '''                This object specifies the clock type as defined in the
                Textual convention description.
                ''',
                'cptpclockcurrentdsclocktypeindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockCurrentDSInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the instance of the clock for this clock
                type in the given domain.
                ''',
                'cptpclockcurrentdsinstanceindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockCurrentDSMeanPathDelay', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                This object specifies the current clock dataset
                MeanPathDelay value.
                
                The mean path delay between a pair of ports as measure by the
                delay request-response mechanism.
                ''',
                'cptpclockcurrentdsmeanpathdelay',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockCurrentDSOffsetFromMaster', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                This object specifies the current clock dataset ClockOffset
                value. The value of the computation of the offset in time
                between
                a slave and a master clock.
                ''',
                'cptpclockcurrentdsoffsetfrommaster',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockCurrentDSStepsRemoved', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The current clock dataset StepsRemoved value.
                
                This object specifies the distance measured by the number of
                Boundary clocks between the local clock and the Foreign master
                as indicated in the stepsRemoved field of Announce messages.
                ''',
                'cptpclockcurrentdsstepsremoved',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockCurrentDSEntry',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclockcurrentdstable' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclockcurrentdstable',
            False, 
            [
            _MetaInfoClassMember('cPtpClockCurrentDSEntry', REFERENCE_LIST, 'Cptpclockcurrentdsentry' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclockcurrentdstable.Cptpclockcurrentdsentry', 
                [], [], 
                '''                An entry in the table, containing information about a single
                PTP clock Current Datasets for a domain.
                ''',
                'cptpclockcurrentdsentry',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockCurrentDSTable',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclockparentdstable.Cptpclockparentdsentry' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclockparentdstable.Cptpclockparentdsentry',
            False, 
            [
            _MetaInfoClassMember('cPtpClockParentDSDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the domain number used to create logical
                group of PTP devices.
                ''',
                'cptpclockparentdsdomainindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockParentDSClockTypeIndex', REFERENCE_ENUM_CLASS, 'ClocktypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClocktypeEnum', 
                [], [], 
                '''                This object specifies the clock type as defined in the
                Textual convention description.
                ''',
                'cptpclockparentdsclocktypeindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockParentDSInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the instance of the clock for this clock
                type in the given domain.
                ''',
                'cptpclockparentdsinstanceindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockParentDSClockPhChRate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object specifies the clock's parent dataset
                ParentClockPhaseChangeRate value.
                
                This value is an estimate of the parent clocks phase change
                rate as measured by the slave clock.
                ''',
                'cptpclockparentdsclockphchrate',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockParentDSGMClockIdentity', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                This object specifies the parent dataset Grandmaster clock
                identity.
                ''',
                'cptpclockparentdsgmclockidentity',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockParentDSGMClockPriority1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object specifies the parent dataset Grandmaster clock
                priority1.
                ''',
                'cptpclockparentdsgmclockpriority1',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockParentDSGMClockPriority2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object specifies the parent dataset grandmaster clock
                priority2.
                ''',
                'cptpclockparentdsgmclockpriority2',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockParentDSGMClockQualityAccuracy', REFERENCE_ENUM_CLASS, 'ClockqualityaccuracytypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockqualityaccuracytypeEnum', 
                [], [], 
                '''                This object specifies the parent dataset grandmaster clock
                quality accuracy.
                ''',
                'cptpclockparentdsgmclockqualityaccuracy',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockParentDSGMClockQualityClass', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the parent dataset grandmaster clock
                quality class.
                ''',
                'cptpclockparentdsgmclockqualityclass',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockParentDSGMClockQualityOffset', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the parent dataset grandmaster clock
                quality offset.
                ''',
                'cptpclockparentdsgmclockqualityoffset',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockParentDSOffset', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                This object specifies the Parent Dataset
                ParentOffsetScaledLogVariance value.
                
                This value is the variance of the parent clocks phase as
                measured by the local clock.
                ''',
                'cptpclockparentdsoffset',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockParentDSParentPortIdentity', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the value of portIdentity of the port on
                the master that issues the Sync messages used in synchronizing
                this clock.
                ''',
                'cptpclockparentdsparentportidentity',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockParentDSParentStats', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies the Parent Dataset ParentStats value.
                
                This value indicates whether the values of ParentDSOffset
                and ParentDSClockPhChRate have been measured and are valid.
                A TRUE value shall indicate valid data.
                ''',
                'cptpclockparentdsparentstats',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockParentDSEntry',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclockparentdstable' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclockparentdstable',
            False, 
            [
            _MetaInfoClassMember('cPtpClockParentDSEntry', REFERENCE_LIST, 'Cptpclockparentdsentry' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclockparentdstable.Cptpclockparentdsentry', 
                [], [], 
                '''                An entry in the table, containing information about a single
                PTP clock Parent Datasets for a domain.
                ''',
                'cptpclockparentdsentry',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockParentDSTable',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclockdefaultdstable.Cptpclockdefaultdsentry' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclockdefaultdstable.Cptpclockdefaultdsentry',
            False, 
            [
            _MetaInfoClassMember('cPtpClockDefaultDSDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the domain number used to create logical
                group of PTP devices.
                ''',
                'cptpclockdefaultdsdomainindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockDefaultDSClockTypeIndex', REFERENCE_ENUM_CLASS, 'ClocktypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClocktypeEnum', 
                [], [], 
                '''                This object specifies the clock type as defined in the
                Textual convention description.
                ''',
                'cptpclockdefaultdsclocktypeindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockDefaultDSInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the instance of the clock for this clock
                type in the given domain.
                ''',
                'cptpclockdefaultdsinstanceindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockDefaultDSClockIdentity', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                This object specifies the default Datasets clock identity.
                ''',
                'cptpclockdefaultdsclockidentity',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockDefaultDSPriority1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object specifies the default Datasets clock Priority1.
                ''',
                'cptpclockdefaultdspriority1',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockDefaultDSPriority2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object specifies the default Datasets clock Priority2.
                ''',
                'cptpclockdefaultdspriority2',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockDefaultDSQualityAccuracy', REFERENCE_ENUM_CLASS, 'ClockqualityaccuracytypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockqualityaccuracytypeEnum', 
                [], [], 
                '''                This object specifies the default dataset Quality Accurarcy.
                ''',
                'cptpclockdefaultdsqualityaccuracy',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockDefaultDSQualityClass', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the default dataset Quality Class.
                ''',
                'cptpclockdefaultdsqualityclass',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockDefaultDSQualityOffset', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object specifies the default dataset Quality offset.
                ''',
                'cptpclockdefaultdsqualityoffset',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockDefaultDSSlaveOnly', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the SlaveOnly flag is set.
                ''',
                'cptpclockdefaultdsslaveonly',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockDefaultDSTwoStepFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies whether the Two Step process is used.
                ''',
                'cptpclockdefaultdstwostepflag',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockDefaultDSEntry',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclockdefaultdstable' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclockdefaultdstable',
            False, 
            [
            _MetaInfoClassMember('cPtpClockDefaultDSEntry', REFERENCE_LIST, 'Cptpclockdefaultdsentry' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclockdefaultdstable.Cptpclockdefaultdsentry', 
                [], [], 
                '''                An entry in the table, containing information about a single
                PTP clock Default Datasets for a domain.
                ''',
                'cptpclockdefaultdsentry',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockDefaultDSTable',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclockrunningtable.Cptpclockrunningentry' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclockrunningtable.Cptpclockrunningentry',
            False, 
            [
            _MetaInfoClassMember('cPtpClockRunningDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the domain number used to create logical
                group of PTP devices.
                ''',
                'cptpclockrunningdomainindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockRunningClockTypeIndex', REFERENCE_ENUM_CLASS, 'ClocktypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClocktypeEnum', 
                [], [], 
                '''                This object specifies the clock type as defined in the
                Textual convention description.
                ''',
                'cptpclockrunningclocktypeindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockRunningInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the instance of the clock for this clock
                type in the given domain.
                ''',
                'cptpclockrunninginstanceindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockRunningPacketsReceived', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object specifies the total number of all packet Unicast
                and multicast that have been received for this clock in this
                domain for this type.
                ''',
                'cptpclockrunningpacketsreceived',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockRunningPacketsSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object specifies the total number of all packet Unicast
                and multicast that have been sent out for this clock in this
                domain for this type.
                ''',
                'cptpclockrunningpacketssent',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockRunningState', REFERENCE_ENUM_CLASS, 'ClockstatetypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockstatetypeEnum', 
                [], [], 
                '''                This object specifies the Clock state returned by PTP engine
                which was described earlier.
                
                Freerun state. Applies to a slave device that is not locked to
                a master. This is the initial state a slave starts out with
                when
                it is not getting any PTP packets from the master or because of
                some other input error (erroneous packets, etc).
                
                Holdover state. In this state the slave device is locked to a
                master but communication with the master is lost or the
                timestamps in the ptp packets are incorrect. But since the
                slave was locked to the master, it can run with the same
                accuracy for
                sometime. The slave can continue to operate in this state for
                some time. If communication with the master is not restored for
                a while, the device is moved to the FREERUN state.
                
                Acquiring state. The slave device is receiving packets from a
                master and is trying to acquire a lock.
                
                Freq_locked state. Slave device is locked to the Master with
                respect to frequency, but not phase aligned
                
                Phase_aligned state. Locked to the master with respect to
                frequency and phase.
                ''',
                'cptpclockrunningstate',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockRunningEntry',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclockrunningtable' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclockrunningtable',
            False, 
            [
            _MetaInfoClassMember('cPtpClockRunningEntry', REFERENCE_LIST, 'Cptpclockrunningentry' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclockrunningtable.Cptpclockrunningentry', 
                [], [], 
                '''                An entry in the table, containing information about a single
                PTP clock running Datasets for a domain.
                ''',
                'cptpclockrunningentry',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockRunningTable',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclocktimepropertiesdstable.Cptpclocktimepropertiesdsentry' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclocktimepropertiesdstable.Cptpclocktimepropertiesdsentry',
            False, 
            [
            _MetaInfoClassMember('cPtpClockTimePropertiesDSDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the domain number used to create logical
                group of PTP devices.
                ''',
                'cptpclocktimepropertiesdsdomainindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockTimePropertiesDSClockTypeIndex', REFERENCE_ENUM_CLASS, 'ClocktypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClocktypeEnum', 
                [], [], 
                '''                This object specifies the clock type as defined in the
                Textual convention description.
                ''',
                'cptpclocktimepropertiesdsclocktypeindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockTimePropertiesDSInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the instance of the clock for this clock
                type in the given domain.
                ''',
                'cptpclocktimepropertiesdsinstanceindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockTimePropertiesDSCurrentUTCOffset', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object specifies the timeproperties dataset value of
                current UTC offset.
                
                In PTP systems whose epoch is the PTP epoch, the value of
                timePropertiesDS.currentUtcOffset is the offset
                between TAI and UTC; otherwise the value has no meaning. The
                value shall be in units of seconds.
                The initialization value shall be selected as follows:
                a) If the timePropertiesDS.ptpTimescale (see 8.2.4.8) is TRUE,
                the value is the value obtained from a
                primary reference if the value is known at the time of
                initialization, else.
                b) The value shall be the current number of leap seconds (7.2.3)
                when the node is designed.
                ''',
                'cptpclocktimepropertiesdscurrentutcoffset',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockTimePropertiesDSCurrentUTCOffsetValid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies the timeproperties dataset value of
                whether current UTC offset is valid.
                ''',
                'cptpclocktimepropertiesdscurrentutcoffsetvalid',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockTimePropertiesDSFreqTraceable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies the Frequency Traceable value in the
                clock Current Dataset.
                ''',
                'cptpclocktimepropertiesdsfreqtraceable',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockTimePropertiesDSLeap59', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies the Leap59 value in the clock Current
                Dataset.
                ''',
                'cptpclocktimepropertiesdsleap59',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockTimePropertiesDSLeap61', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies the Leap61 value in the clock Current
                Dataset.
                ''',
                'cptpclocktimepropertiesdsleap61',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockTimePropertiesDSPTPTimescale', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies the PTP Timescale value in the clock
                Current Dataset.
                ''',
                'cptpclocktimepropertiesdsptptimescale',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockTimePropertiesDSSource', REFERENCE_ENUM_CLASS, 'ClocktimesourcetypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClocktimesourcetypeEnum', 
                [], [], 
                '''                This object specifies the Timesource value in the clock Current
                Dataset.
                ''',
                'cptpclocktimepropertiesdssource',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockTimePropertiesDSTimeTraceable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies the Timetraceable value in the clock
                Current Dataset.
                ''',
                'cptpclocktimepropertiesdstimetraceable',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockTimePropertiesDSEntry',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclocktimepropertiesdstable' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclocktimepropertiesdstable',
            False, 
            [
            _MetaInfoClassMember('cPtpClockTimePropertiesDSEntry', REFERENCE_LIST, 'Cptpclocktimepropertiesdsentry' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclocktimepropertiesdstable.Cptpclocktimepropertiesdsentry', 
                [], [], 
                '''                An entry in the table, containing information about a single
                PTP clock timeproperties Datasets for a domain.
                ''',
                'cptpclocktimepropertiesdsentry',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockTimePropertiesDSTable',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclocktransdefaultdstable.Cptpclocktransdefaultdsentry' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclocktransdefaultdstable.Cptpclocktransdefaultdsentry',
            False, 
            [
            _MetaInfoClassMember('cPtpClockTransDefaultDSDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the domain number used to create logical
                group of PTP devices.
                ''',
                'cptpclocktransdefaultdsdomainindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockTransDefaultDSInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the instance of the clock for this clock
                type in the given domain.
                ''',
                'cptpclocktransdefaultdsinstanceindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockTransDefaultDSClockIdentity', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                This object specifies the value of the clockIdentity attribute
                of the local clock.
                ''',
                'cptpclocktransdefaultdsclockidentity',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockTransDefaultDSDelay', REFERENCE_ENUM_CLASS, 'ClockmechanismtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockmechanismtypeEnum', 
                [], [], 
                '''                This object, if the transparent clock is an end-to-end
                transparent clock, has the value shall be E2E; If the
                transparent clock is a peer-to-peer transparent clock, the
                value
                shall be P2P.
                ''',
                'cptpclocktransdefaultdsdelay',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockTransDefaultDSNumOfPorts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the number of PTP ports of the device.
                ''',
                'cptpclocktransdefaultdsnumofports',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockTransDefaultDSPrimaryDomain', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object specifies the value of the primary syntonization
                domain. The initialization value shall be 0.
                ''',
                'cptpclocktransdefaultdsprimarydomain',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockTransDefaultDSEntry',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclocktransdefaultdstable' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclocktransdefaultdstable',
            False, 
            [
            _MetaInfoClassMember('cPtpClockTransDefaultDSEntry', REFERENCE_LIST, 'Cptpclocktransdefaultdsentry' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclocktransdefaultdstable.Cptpclocktransdefaultdsentry', 
                [], [], 
                '''                An entry in the table, containing information about a single
                PTP Transparent clock Default Datasets for a domain.
                ''',
                'cptpclocktransdefaultdsentry',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockTransDefaultDSTable',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclockporttable.Cptpclockportentry' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclockporttable.Cptpclockportentry',
            False, 
            [
            _MetaInfoClassMember('cPtpClockPortDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the domain number used to create logical
                group of PTP devices.
                ''',
                'cptpclockportdomainindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortClockTypeIndex', REFERENCE_ENUM_CLASS, 'ClocktypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClocktypeEnum', 
                [], [], 
                '''                This object specifies the clock type as defined in the
                Textual convention description.
                ''',
                'cptpclockportclocktypeindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortClockInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the instance of the clock for this clock
                type in the given domain.
                ''',
                'cptpclockportclockinstanceindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortTablePortNumberIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                This object specifies the PTP Portnumber for this port.
                ''',
                'cptpclockporttableportnumberindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortCurrentPeerAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the current peer's network address used
                for PTP communication. Based on the scenario and the setup
                involved, the values might look like these -
                Scenario                   Value
                -------------------   ----------------
                Single Master          master port
                Multiple Masters       selected master port
                Single Slave           slave port
                Multiple Slaves        <empty>
                
                (In relevant setups, information on available
                slaves and available masters will be available through 
                cPtpClockPortAssociateTable)
                ''',
                'cptpclockportcurrentpeeraddress',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortCurrentPeerAddressType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object specifies the current peer's network address used
                for PTP communication. Based on the scenario and the setup
                involved, the values might look like these -
                Scenario                   Value
                -------------------   ----------------
                Single Master          master port
                Multiple Masters       selected master port
                Single Slave           slave port
                Multiple Slaves        <empty>
                
                (In relevant setups, information on available
                slaves and available masters will be available through 
                cPtpClockPortAssociateTable)
                ''',
                'cptpclockportcurrentpeeraddresstype',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                This object specifies the PTP clock port name configured on the
                router.
                ''',
                'cptpclockportname',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortNumOfAssociatedPorts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies -
                For a master port - the number of PTP slave sessions (peers)
                associated with this PTP port.
                For a slave port - the number of masters available to this slave
                port (might or might not be peered).
                ''',
                'cptpclockportnumofassociatedports',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortRole', REFERENCE_ENUM_CLASS, 'ClockroletypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockroletypeEnum', 
                [], [], 
                '''                This object describes the current role (slave/master) of the
                port.
                ''',
                'cptpclockportrole',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortSyncOneStep', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies that one-step clock operation between
                the PTP master and slave device is enabled.
                ''',
                'cptpclockportsynconestep',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockPortEntry',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclockporttable' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclockporttable',
            False, 
            [
            _MetaInfoClassMember('cPtpClockPortEntry', REFERENCE_LIST, 'Cptpclockportentry' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclockporttable.Cptpclockportentry', 
                [], [], 
                '''                An entry in the table, containing information about a single
                clock port.
                ''',
                'cptpclockportentry',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockPortTable',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclockportdstable.Cptpclockportdsentry' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclockportdstable.Cptpclockportdsentry',
            False, 
            [
            _MetaInfoClassMember('cPtpClockPortDSDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the domain number used to create logical
                group of PTP devices.
                ''',
                'cptpclockportdsdomainindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortDSClockTypeIndex', REFERENCE_ENUM_CLASS, 'ClocktypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClocktypeEnum', 
                [], [], 
                '''                This object specifies the clock type as defined in the
                Textual convention description.
                ''',
                'cptpclockportdsclocktypeindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortDSClockInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the instance of the clock for this clock
                type in the given domain.
                ''',
                'cptpclockportdsclockinstanceindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortDSPortNumberIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                This object specifies the PTP portnumber associated with this
                PTP port.
                ''',
                'cptpclockportdsportnumberindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortDSAnnouncementInterval', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object specifies the Announce message transmission
                interval associated with this clock port.
                ''',
                'cptpclockportdsannouncementinterval',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortDSAnnounceRctTimeout', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object specifies the Announce receipt timeout associated
                with this clock port.
                ''',
                'cptpclockportdsannouncercttimeout',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortDSDelayMech', REFERENCE_ENUM_CLASS, 'ClockmechanismtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockmechanismtypeEnum', 
                [], [], 
                '''                This object specifies the delay mechanism used. If the clock
                is an end-to-end clock, the value of the is e2e, else if the
                clock is a peer to-peer clock, the value shall be p2p.
                ''',
                'cptpclockportdsdelaymech',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortDSGrantDuration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object specifies the grant duration allocated by the
                master.
                ''',
                'cptpclockportdsgrantduration',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortDSMinDelayReqInterval', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object specifies the Delay_Req message transmission
                interval.
                ''',
                'cptpclockportdsmindelayreqinterval',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortDSName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                This object specifies the PTP clock port name.
                ''',
                'cptpclockportdsname',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortDSPeerDelayReqInterval', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object specifies the Pdelay_Req message transmission
                interval.
                ''',
                'cptpclockportdspeerdelayreqinterval',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortDSPeerMeanPathDelay', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                This object specifies the peer meanPathDelay.
                ''',
                'cptpclockportdspeermeanpathdelay',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortDSPortIdentity', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object specifies the PTP clock port Identity.
                ''',
                'cptpclockportdsportidentity',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortDSPTPVersion', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object specifies the PTP version being used.
                ''',
                'cptpclockportdsptpversion',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortDSSyncInterval', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object specifies the Sync message transmission interval.
                ''',
                'cptpclockportdssyncinterval',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockPortDSEntry',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclockportdstable' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclockportdstable',
            False, 
            [
            _MetaInfoClassMember('cPtpClockPortDSEntry', REFERENCE_LIST, 'Cptpclockportdsentry' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclockportdstable.Cptpclockportdsentry', 
                [], [], 
                '''                An entry in the table, containing port dataset information for
                a single clock port.
                ''',
                'cptpclockportdsentry',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockPortDSTable',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclockportrunningtable.Cptpclockportrunningentry' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclockportrunningtable.Cptpclockportrunningentry',
            False, 
            [
            _MetaInfoClassMember('cPtpClockPortRunningDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the domain number used to create logical
                group of PTP devices.
                ''',
                'cptpclockportrunningdomainindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortRunningClockTypeIndex', REFERENCE_ENUM_CLASS, 'ClocktypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClocktypeEnum', 
                [], [], 
                '''                This object specifies the clock type as defined in the
                Textual convention description.
                ''',
                'cptpclockportrunningclocktypeindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortRunningClockInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the instance of the clock for this clock
                type in the given domain.
                ''',
                'cptpclockportrunningclockinstanceindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortRunningPortNumberIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                This object specifies the PTP portnumber associated with this
                clock port.
                ''',
                'cptpclockportrunningportnumberindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortRunningEncapsulationType', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object specifies the type of encapsulation if the
                interface is adding extra  layers (eg. VLAN, Pseudowire
                encapsulation...) for the PTP messages.
                ''',
                'cptpclockportrunningencapsulationtype',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortRunningInterfaceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object specifies the interface on the router being used by
                the PTP Clock for PTP communication.
                ''',
                'cptpclockportrunninginterfaceindex',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortRunningIPversion', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object specifirst the IP version being used for PTP
                communication (the mapping used).
                ''',
                'cptpclockportrunningipversion',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortRunningName', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                This object specifies the PTP clock port name.
                ''',
                'cptpclockportrunningname',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortRunningPacketsReceived', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object specifies the packets received on the clock port
                (cummulative).
                ''',
                'cptpclockportrunningpacketsreceived',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortRunningPacketsSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object specifies the packets sent on the clock port
                (cummulative).
                ''',
                'cptpclockportrunningpacketssent',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortRunningRole', REFERENCE_ENUM_CLASS, 'ClockroletypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockroletypeEnum', 
                [], [], 
                '''                This object specifies the Clock Role.
                ''',
                'cptpclockportrunningrole',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortRunningRxMode', REFERENCE_ENUM_CLASS, 'ClocktxmodetypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClocktxmodetypeEnum', 
                [], [], 
                '''                This object specifie the clock receive mode as
                
                unicast:       Using unicast commnuication channel.
                multicast:     Using Multicast communication channel.
                multicast-mix: Using multicast-unicast communication channel
                ''',
                'cptpclockportrunningrxmode',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortRunningState', REFERENCE_ENUM_CLASS, 'ClockportstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClockportstateEnum', 
                [], [], 
                '''                This object specifies the port state returned by PTP engine.
                
                initializing - In this state a port initializes
                               its data sets, hardware, and
                               communication facilities.
                faulty       - The fault state of the protocol.
                disabled     - The port shall not place any
                               messages on its communication path.
                listening    - The port is waiting for the
                               announceReceiptTimeout to expire or
                               to receive an Announce message from
                               a master.
                preMaster    - The port shall behave in all respects
                               as though it were in the MASTER state
                               except that it shall not place any
                               messages on its communication path
                               except for Pdelay_Req, Pdelay_Resp,
                               Pdelay_Resp_Follow_Up, signaling, or
                               management messages.
                master       - The port is behaving as a master port.           
                
                passive      - The port shall not place any
                               messages on its communication path
                               except for Pdelay_Req, Pdelay_Resp,
                               Pdelay_Resp_Follow_Up, or signaling
                               messages, or management messages
                               that are a required response to
                               another management message
                uncalibrated - The local port is preparing to
                               synchronize to the master port.
                slave        - The port is synchronizing to the
                               selected master port.
                ''',
                'cptpclockportrunningstate',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortRunningTxMode', REFERENCE_ENUM_CLASS, 'ClocktxmodetypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClocktxmodetypeEnum', 
                [], [], 
                '''                This object specifies the clock transmission mode as
                
                unicast:       Using unicast commnuication channel.
                multicast:     Using Multicast communication channel.
                multicast-mix: Using multicast-unicast communication channel
                ''',
                'cptpclockportrunningtxmode',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockPortRunningEntry',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclockportrunningtable' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclockportrunningtable',
            False, 
            [
            _MetaInfoClassMember('cPtpClockPortRunningEntry', REFERENCE_LIST, 'Cptpclockportrunningentry' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclockportrunningtable.Cptpclockportrunningentry', 
                [], [], 
                '''                An entry in the table, containing runing dataset information
                about a single clock port.
                ''',
                'cptpclockportrunningentry',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockPortRunningTable',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclockporttransdstable.Cptpclockporttransdsentry' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclockporttransdstable.Cptpclockporttransdsentry',
            False, 
            [
            _MetaInfoClassMember('cPtpClockPortTransDSDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the domain number used to create logical
                group of PTP devices.
                ''',
                'cptpclockporttransdsdomainindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortTransDSInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the instance of the clock for this clock
                type in the given domain.
                ''',
                'cptpclockporttransdsinstanceindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortTransDSPortNumberIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                This object specifies the PTP port number associated with this
                port.
                ''',
                'cptpclockporttransdsportnumberindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortTransDSFaultyFlag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object specifies the value TRUE if the port is faulty
                and FALSE if the port is operating normally.
                ''',
                'cptpclockporttransdsfaultyflag',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortTransDSlogMinPdelayReqInt', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This object specifies the value of the logarithm to the
                base 2 of the minPdelayReqInterval.
                ''',
                'cptpclockporttransdslogminpdelayreqint',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortTransDSPeerMeanPathDelay', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                This object specifies, (if the delayMechanism used is P2P) the
                value is the estimate of the current one-way propagation delay,
                i.e., <meanPathDelay> on the link attached to this port
                computed
                using the peer delay mechanism. If the value of the
                delayMechanism
                used is E2E, then the value will be zero.
                ''',
                'cptpclockporttransdspeermeanpathdelay',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortTransDSPortIdentity', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                This object specifies the value of the PortIdentity
                attribute of the local port.
                ''',
                'cptpclockporttransdsportidentity',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockPortTransDSEntry',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclockporttransdstable' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclockporttransdstable',
            False, 
            [
            _MetaInfoClassMember('cPtpClockPortTransDSEntry', REFERENCE_LIST, 'Cptpclockporttransdsentry' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclockporttransdstable.Cptpclockporttransdsentry', 
                [], [], 
                '''                An entry in the table, containing clock port Transparent
                dataset information about a single clock port
                ''',
                'cptpclockporttransdsentry',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockPortTransDSTable',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclockportassociatetable.Cptpclockportassociateentry' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclockportassociatetable.Cptpclockportassociateentry',
            False, 
            [
            _MetaInfoClassMember('cPtpClockPortCurrentDomainIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the given port's domain number.
                ''',
                'cptpclockportcurrentdomainindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortCurrentClockTypeIndex', REFERENCE_ENUM_CLASS, 'ClocktypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'ClocktypeEnum', 
                [], [], 
                '''                This object specifies the given port's clock type.
                ''',
                'cptpclockportcurrentclocktypeindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortCurrentClockInstanceIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                This object specifies the instance of the clock for this clock
                type in the given domain.
                ''',
                'cptpclockportcurrentclockinstanceindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortCurrentPortNumberIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                This object specifies the PTP Port Number for the given port.
                ''',
                'cptpclockportcurrentportnumberindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortAssociatePortIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                This object specifies the associated port's serial number in
                the current port's context.
                ''',
                'cptpclockportassociateportindex',
                'CISCO-PTP-MIB', True),
            _MetaInfoClassMember('cPtpClockPortAssociateAddress', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the peer port's network address used for
                PTP communication.
                ''',
                'cptpclockportassociateaddress',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortAssociateAddressType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object specifies the peer port's network address type used
                for PTP communication.
                ''',
                'cptpclockportassociateaddresstype',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortAssociateInErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object specifies the input errors associated with the
                peer port.
                ''',
                'cptpclockportassociateinerrors',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortAssociateOutErrors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object specifies the output errors associated with the
                peer port.
                ''',
                'cptpclockportassociateouterrors',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortAssociatePacketsReceived', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets received from this peer port by the
                current port.
                ''',
                'cptpclockportassociatepacketsreceived',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortAssociatePacketsSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of packets sent to this peer port from the current
                port.
                ''',
                'cptpclockportassociatepacketssent',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockPortAssociateEntry',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib.Cptpclockportassociatetable' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib.Cptpclockportassociatetable',
            False, 
            [
            _MetaInfoClassMember('cPtpClockPortAssociateEntry', REFERENCE_LIST, 'Cptpclockportassociateentry' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclockportassociatetable.Cptpclockportassociateentry', 
                [], [], 
                '''                An entry in the table, containing information about a single
                associated port for the given clockport.
                ''',
                'cptpclockportassociateentry',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'cPtpClockPortAssociateTable',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
    'CiscoPtpMib' : {
        'meta_info' : _MetaInfoClass('CiscoPtpMib',
            False, 
            [
            _MetaInfoClassMember('ciscoPtpMIBSystemInfo', REFERENCE_CLASS, 'Ciscoptpmibsysteminfo' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Ciscoptpmibsysteminfo', 
                [], [], 
                '''                ''',
                'ciscoptpmibsysteminfo',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockCurrentDSTable', REFERENCE_CLASS, 'Cptpclockcurrentdstable' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclockcurrentdstable', 
                [], [], 
                '''                Table of information about the PTP clock Current Datasets for
                all domains.
                ''',
                'cptpclockcurrentdstable',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockDefaultDSTable', REFERENCE_CLASS, 'Cptpclockdefaultdstable' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclockdefaultdstable', 
                [], [], 
                '''                Table of information about the PTP clock Default Datasets for
                all domains.
                ''',
                'cptpclockdefaultdstable',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockNodeTable', REFERENCE_CLASS, 'Cptpclocknodetable' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclocknodetable', 
                [], [], 
                '''                Table of information about the PTP system for a given domain.
                ''',
                'cptpclocknodetable',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockParentDSTable', REFERENCE_CLASS, 'Cptpclockparentdstable' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclockparentdstable', 
                [], [], 
                '''                Table of information about the PTP clock Parent Datasets for
                all domains.
                ''',
                'cptpclockparentdstable',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortAssociateTable', REFERENCE_CLASS, 'Cptpclockportassociatetable' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclockportassociatetable', 
                [], [], 
                '''                Table of information about a given port's associated ports.
                
                For a master port - multiple slave ports which have established
                sessions with the current master port.  
                For a slave port - the list of masters available for a given
                slave port. 
                
                Session information (pkts, errors) to be displayed based on
                availability and scenario.
                ''',
                'cptpclockportassociatetable',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortDSTable', REFERENCE_CLASS, 'Cptpclockportdstable' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclockportdstable', 
                [], [], 
                '''                Table of information about the clock ports dataset for a
                particular domain.
                ''',
                'cptpclockportdstable',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortRunningTable', REFERENCE_CLASS, 'Cptpclockportrunningtable' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclockportrunningtable', 
                [], [], 
                '''                Table of information about the clock ports running dataset for
                a particular domain.
                ''',
                'cptpclockportrunningtable',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortTable', REFERENCE_CLASS, 'Cptpclockporttable' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclockporttable', 
                [], [], 
                '''                Table of information about the clock ports for a particular
                domain.
                ''',
                'cptpclockporttable',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockPortTransDSTable', REFERENCE_CLASS, 'Cptpclockporttransdstable' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclockporttransdstable', 
                [], [], 
                '''                Table of information about the Transparent clock ports running
                dataset for a particular domain.
                ''',
                'cptpclockporttransdstable',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockRunningTable', REFERENCE_CLASS, 'Cptpclockrunningtable' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclockrunningtable', 
                [], [], 
                '''                Table of information about the PTP clock Running Datasets for
                all domains.
                ''',
                'cptpclockrunningtable',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockTimePropertiesDSTable', REFERENCE_CLASS, 'Cptpclocktimepropertiesdstable' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclocktimepropertiesdstable', 
                [], [], 
                '''                Table of information about the PTP clock Timeproperties
                Datasets for all domains.
                ''',
                'cptpclocktimepropertiesdstable',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpClockTransDefaultDSTable', REFERENCE_CLASS, 'Cptpclocktransdefaultdstable' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpclocktransdefaultdstable', 
                [], [], 
                '''                Table of information about the PTP Transparent clock Default
                Datasets for all domains.
                ''',
                'cptpclocktransdefaultdstable',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpSystemDomainTable', REFERENCE_CLASS, 'Cptpsystemdomaintable' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpsystemdomaintable', 
                [], [], 
                '''                Table of information about the PTP system for all clock modes
                -- ordinary, boundary or transparent.
                ''',
                'cptpsystemdomaintable',
                'CISCO-PTP-MIB', False),
            _MetaInfoClassMember('cPtpSystemTable', REFERENCE_CLASS, 'Cptpsystemtable' , 'ydk.models.cisco_ios_xe.CISCO_PTP_MIB', 'CiscoPtpMib.Cptpsystemtable', 
                [], [], 
                '''                Table of count information about the PTP system for all
                domains.
                ''',
                'cptpsystemtable',
                'CISCO-PTP-MIB', False),
            ],
            'CISCO-PTP-MIB',
            'CISCO-PTP-MIB',
            _yang_ns._namespaces['CISCO-PTP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PTP_MIB'
        ),
    },
}
_meta_table['CiscoPtpMib.Cptpsystemtable.Cptpsystementry']['meta_info'].parent =_meta_table['CiscoPtpMib.Cptpsystemtable']['meta_info']
_meta_table['CiscoPtpMib.Cptpsystemdomaintable.Cptpsystemdomainentry']['meta_info'].parent =_meta_table['CiscoPtpMib.Cptpsystemdomaintable']['meta_info']
_meta_table['CiscoPtpMib.Cptpclocknodetable.Cptpclocknodeentry']['meta_info'].parent =_meta_table['CiscoPtpMib.Cptpclocknodetable']['meta_info']
_meta_table['CiscoPtpMib.Cptpclockcurrentdstable.Cptpclockcurrentdsentry']['meta_info'].parent =_meta_table['CiscoPtpMib.Cptpclockcurrentdstable']['meta_info']
_meta_table['CiscoPtpMib.Cptpclockparentdstable.Cptpclockparentdsentry']['meta_info'].parent =_meta_table['CiscoPtpMib.Cptpclockparentdstable']['meta_info']
_meta_table['CiscoPtpMib.Cptpclockdefaultdstable.Cptpclockdefaultdsentry']['meta_info'].parent =_meta_table['CiscoPtpMib.Cptpclockdefaultdstable']['meta_info']
_meta_table['CiscoPtpMib.Cptpclockrunningtable.Cptpclockrunningentry']['meta_info'].parent =_meta_table['CiscoPtpMib.Cptpclockrunningtable']['meta_info']
_meta_table['CiscoPtpMib.Cptpclocktimepropertiesdstable.Cptpclocktimepropertiesdsentry']['meta_info'].parent =_meta_table['CiscoPtpMib.Cptpclocktimepropertiesdstable']['meta_info']
_meta_table['CiscoPtpMib.Cptpclocktransdefaultdstable.Cptpclocktransdefaultdsentry']['meta_info'].parent =_meta_table['CiscoPtpMib.Cptpclocktransdefaultdstable']['meta_info']
_meta_table['CiscoPtpMib.Cptpclockporttable.Cptpclockportentry']['meta_info'].parent =_meta_table['CiscoPtpMib.Cptpclockporttable']['meta_info']
_meta_table['CiscoPtpMib.Cptpclockportdstable.Cptpclockportdsentry']['meta_info'].parent =_meta_table['CiscoPtpMib.Cptpclockportdstable']['meta_info']
_meta_table['CiscoPtpMib.Cptpclockportrunningtable.Cptpclockportrunningentry']['meta_info'].parent =_meta_table['CiscoPtpMib.Cptpclockportrunningtable']['meta_info']
_meta_table['CiscoPtpMib.Cptpclockporttransdstable.Cptpclockporttransdsentry']['meta_info'].parent =_meta_table['CiscoPtpMib.Cptpclockporttransdstable']['meta_info']
_meta_table['CiscoPtpMib.Cptpclockportassociatetable.Cptpclockportassociateentry']['meta_info'].parent =_meta_table['CiscoPtpMib.Cptpclockportassociatetable']['meta_info']
_meta_table['CiscoPtpMib.Ciscoptpmibsysteminfo']['meta_info'].parent =_meta_table['CiscoPtpMib']['meta_info']
_meta_table['CiscoPtpMib.Cptpsystemtable']['meta_info'].parent =_meta_table['CiscoPtpMib']['meta_info']
_meta_table['CiscoPtpMib.Cptpsystemdomaintable']['meta_info'].parent =_meta_table['CiscoPtpMib']['meta_info']
_meta_table['CiscoPtpMib.Cptpclocknodetable']['meta_info'].parent =_meta_table['CiscoPtpMib']['meta_info']
_meta_table['CiscoPtpMib.Cptpclockcurrentdstable']['meta_info'].parent =_meta_table['CiscoPtpMib']['meta_info']
_meta_table['CiscoPtpMib.Cptpclockparentdstable']['meta_info'].parent =_meta_table['CiscoPtpMib']['meta_info']
_meta_table['CiscoPtpMib.Cptpclockdefaultdstable']['meta_info'].parent =_meta_table['CiscoPtpMib']['meta_info']
_meta_table['CiscoPtpMib.Cptpclockrunningtable']['meta_info'].parent =_meta_table['CiscoPtpMib']['meta_info']
_meta_table['CiscoPtpMib.Cptpclocktimepropertiesdstable']['meta_info'].parent =_meta_table['CiscoPtpMib']['meta_info']
_meta_table['CiscoPtpMib.Cptpclocktransdefaultdstable']['meta_info'].parent =_meta_table['CiscoPtpMib']['meta_info']
_meta_table['CiscoPtpMib.Cptpclockporttable']['meta_info'].parent =_meta_table['CiscoPtpMib']['meta_info']
_meta_table['CiscoPtpMib.Cptpclockportdstable']['meta_info'].parent =_meta_table['CiscoPtpMib']['meta_info']
_meta_table['CiscoPtpMib.Cptpclockportrunningtable']['meta_info'].parent =_meta_table['CiscoPtpMib']['meta_info']
_meta_table['CiscoPtpMib.Cptpclockporttransdstable']['meta_info'].parent =_meta_table['CiscoPtpMib']['meta_info']
_meta_table['CiscoPtpMib.Cptpclockportassociatetable']['meta_info'].parent =_meta_table['CiscoPtpMib']['meta_info']
