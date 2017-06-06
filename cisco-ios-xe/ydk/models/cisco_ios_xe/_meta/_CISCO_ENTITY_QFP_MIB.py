


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoqfpmemoryresourceEnum' : _MetaInfoEnum('CiscoqfpmemoryresourceEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB',
        {
            'dram':'dram',
        }, 'CISCO-ENTITY-QFP-MIB', _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB']),
    'CiscoqfptimeintervalEnum' : _MetaInfoEnum('CiscoqfptimeintervalEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB',
        {
            'fiveSeconds':'fiveSeconds',
            'oneMinute':'oneMinute',
            'fiveMinutes':'fiveMinutes',
            'sixtyMinutes':'sixtyMinutes',
        }, 'CISCO-ENTITY-QFP-MIB', _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB']),
    'CiscoEntityQfpMib.Ciscoentityqfp.CeqfpfiveminutesutilalgoEnum' : _MetaInfoEnum('CeqfpfiveminutesutilalgoEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB',
        {
            'unknown':'unknown',
            'fiveSecSMA':'fiveSecSMA',
        }, 'CISCO-ENTITY-QFP-MIB', _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB']),
    'CiscoEntityQfpMib.Ciscoentityqfp.CeqfpfivesecondutilalgoEnum' : _MetaInfoEnum('CeqfpfivesecondutilalgoEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB',
        {
            'unknown':'unknown',
            'fiveSecSample':'fiveSecSample',
        }, 'CISCO-ENTITY-QFP-MIB', _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB']),
    'CiscoEntityQfpMib.Ciscoentityqfp.CeqfponeminuteutilalgoEnum' : _MetaInfoEnum('CeqfponeminuteutilalgoEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB',
        {
            'unknown':'unknown',
            'fiveSecSMA':'fiveSecSMA',
        }, 'CISCO-ENTITY-QFP-MIB', _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB']),
    'CiscoEntityQfpMib.Ciscoentityqfp.CeqfpsixtyminutesutilalgoEnum' : _MetaInfoEnum('CeqfpsixtyminutesutilalgoEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB',
        {
            'unknown':'unknown',
            'fiveSecSMA':'fiveSecSMA',
        }, 'CISCO-ENTITY-QFP-MIB', _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB']),
    'CiscoEntityQfpMib.Ciscoentityqfp' : {
        'meta_info' : _MetaInfoClass('CiscoEntityQfpMib.Ciscoentityqfp',
            False, 
            [
            _MetaInfoClassMember('ceqfpFiveMinutesUtilAlgo', REFERENCE_ENUM_CLASS, 'CeqfpfiveminutesutilalgoEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoEntityQfpMib.Ciscoentityqfp.CeqfpfiveminutesutilalgoEnum', 
                [], [], 
                '''                This objects represents the method used to calculate 5 Minutes
                interval utilization data. The enumerated values are described
                below.
                
                unknown    (1) - The calculation method is unknown
                fiveSecSMA (2) - The value is calculated using Simple Moving  
                                 Average of last 60 five seconds utilization
                                 data.
                ''',
                'ceqfpfiveminutesutilalgo',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpFiveSecondUtilAlgo', REFERENCE_ENUM_CLASS, 'CeqfpfivesecondutilalgoEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoEntityQfpMib.Ciscoentityqfp.CeqfpfivesecondutilalgoEnum', 
                [], [], 
                '''                This objects represents the method used to calculate 5 Second
                interval utilization data. The enumerated values are described
                below.
                
                unknown       (1) - The calculation method is unknown
                fiveSecSample (2) - The value is calculated based on the last
                                    5 second sampling period of utilization
                                    data.
                ''',
                'ceqfpfivesecondutilalgo',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpOneMinuteUtilAlgo', REFERENCE_ENUM_CLASS, 'CeqfponeminuteutilalgoEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoEntityQfpMib.Ciscoentityqfp.CeqfponeminuteutilalgoEnum', 
                [], [], 
                '''                This objects represents the method used to calculate 1 Minute
                interval utilization data. The enumerated values are described
                below.
                
                unknown    (1) - The calculation method is unknown
                fiveSecSMA (2) - The value is calculated using Simple Moving  
                                 Average of last 12 five seconds utilization
                                 data.
                ''',
                'ceqfponeminuteutilalgo',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpSixtyMinutesUtilAlgo', REFERENCE_ENUM_CLASS, 'CeqfpsixtyminutesutilalgoEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoEntityQfpMib.Ciscoentityqfp.CeqfpsixtyminutesutilalgoEnum', 
                [], [], 
                '''                This objects represents the method used to calculate 60 Minutes
                interval utilization data. The enumerated values are described
                below.
                
                unknown    (1) - The calculation method is unknown
                fiveSecSMA (1) - The value is calculated using Simple Moving  
                                 Average of last 720 five seconds utilization
                                 data.
                ''',
                'ceqfpsixtyminutesutilalgo',
                'CISCO-ENTITY-QFP-MIB', False),
            ],
            'CISCO-ENTITY-QFP-MIB',
            'ciscoEntityQfp',
            _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB'
        ),
    },
    'CiscoEntityQfpMib.Ciscoentityqfpnotif' : {
        'meta_info' : _MetaInfoClass('CiscoEntityQfpMib.Ciscoentityqfpnotif',
            False, 
            [
            _MetaInfoClassMember('ceqfpMemoryResThreshNotifEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object controls memory resource rising and falling
                threshold notification.
                
                When this object contains a value 'true', then generation of
                memory resource threshold notification is enabled. If this
                object contains a value 'false', then generation of memory
                resource threshold notification is disabled.
                ''',
                'ceqfpmemoryresthreshnotifenabled',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpThroughputNotifEnabled', ATTRIBUTE, 'int' , None, None, 
                [('0', '2')], [], 
                '''                This object controls throughput rate notification.
                
                When this object contains a value 'true', then generation of
                ceqfpThroughputNotif is enabled. If this object contains a value
                'false', then generation of ceqfpThroughputNotif is disabled.
                ''',
                'ceqfpthroughputnotifenabled',
                'CISCO-ENTITY-QFP-MIB', False),
            ],
            'CISCO-ENTITY-QFP-MIB',
            'ciscoEntityQfpNotif',
            _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB'
        ),
    },
    'CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry.CeqfpsystemstateEnum' : _MetaInfoEnum('CeqfpsystemstateEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB',
        {
            'unknown':'unknown',
            'reset':'reset',
            'init':'init',
            'active':'active',
            'activeSolo':'activeSolo',
            'standby':'standby',
            'hotStandby':'hotStandby',
        }, 'CISCO-ENTITY-QFP-MIB', _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB']),
    'CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry.CeqfpsystemtrafficdirectionEnum' : _MetaInfoEnum('CeqfpsystemtrafficdirectionEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB',
        {
            'none':'none',
            'ingress':'ingress',
            'egress':'egress',
            'both':'both',
        }, 'CISCO-ENTITY-QFP-MIB', _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB']),
    'CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-QFP-MIB', True),
            _MetaInfoClassMember('ceqfpNumberSystemLoads', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the number of times the QFP is loaded,
                since the QFP host is up.
                ''',
                'ceqfpnumbersystemloads',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpSystemLastLoadTime', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object represents the QFP last load time.
                ''',
                'ceqfpsystemlastloadtime',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpSystemState', REFERENCE_ENUM_CLASS, 'CeqfpsystemstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry.CeqfpsystemstateEnum', 
                [], [], 
                '''                This object represents the current QFP state. The enumerated
                values are described below.
                
                unknown (1)    - The state of the QFP is unknown
                reset (2)      - The QFP is reset
                init (3)       - The QFP is being initialized
                active (4)     - The QFP is active in a system with redundant
                                 QFP
                activeSolo (5) - The QFP is active and there is no redundant
                                 QFP in the system
                standby (6)    - The QFP is standby in a redundant system.
                hotStandby (7) - The QFP is standby and synchronized with
                                 active, so that a switchover in this state
                                 will preserve state of the active. Stateful 
                                 datapath features are synchronized between the
                                 active QFP and standby QFP
                ''',
                'ceqfpsystemstate',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpSystemTrafficDirection', REFERENCE_ENUM_CLASS, 'CeqfpsystemtrafficdirectionEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry.CeqfpsystemtrafficdirectionEnum', 
                [], [], 
                '''                This object represents the traffic direction that this QFP is
                assigned to process. The enumerated values are described below.
                
                none (1)    - The QFP is not assigned to processes any traffic
                              yet
                ingress (2) - The QFP processes inbound traffic
                egress (3)  - The QFP processes outbound traffic
                both (4)    - The QFP processes both inbound and outbound
                              traffic
                ''',
                'ceqfpsystemtrafficdirection',
                'CISCO-ENTITY-QFP-MIB', False),
            ],
            'CISCO-ENTITY-QFP-MIB',
            'ceqfpSystemEntry',
            _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB'
        ),
    },
    'CiscoEntityQfpMib.Ceqfpsystemtable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityQfpMib.Ceqfpsystemtable',
            False, 
            [
            _MetaInfoClassMember('ceqfpSystemEntry', REFERENCE_LIST, 'Ceqfpsystementry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry', 
                [], [], 
                '''                A conceptual row in the ceqfpSystemTable. There is an entry
                in this table for each QFP entity, as defined by a value of
                entPhysicalIndex.
                ''',
                'ceqfpsystementry',
                'CISCO-ENTITY-QFP-MIB', False),
            ],
            'CISCO-ENTITY-QFP-MIB',
            'ceqfpSystemTable',
            _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB'
        ),
    },
    'CiscoEntityQfpMib.Ceqfputilizationtable.Ceqfputilizationentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityQfpMib.Ceqfputilizationtable.Ceqfputilizationentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-QFP-MIB', True),
            _MetaInfoClassMember('ceqfpUtilTimeInterval', REFERENCE_ENUM_CLASS, 'CiscoqfptimeintervalEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoqfptimeintervalEnum', 
                [], [], 
                '''                This object identifies the time interval for which the
                utilization statistics being collected. The interval 
                values can be 5 second, 1 minute, etc. as specified in 
                the CiscoQfpTimeInterval.
                ''',
                'ceqfputiltimeinterval',
                'CISCO-ENTITY-QFP-MIB', True),
            _MetaInfoClassMember('ceqfpUtilInputNonPriorityBitRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object represents the QFP input channel non-priority
                bit rate during this interval.
                ''',
                'ceqfputilinputnonprioritybitrate',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpUtilInputNonPriorityPktRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object represents the QFP input channel non-priority
                packet rate during this interval.
                ''',
                'ceqfputilinputnonprioritypktrate',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpUtilInputPriorityBitRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object represents the QFP input channel priority bit rate
                during this interval.
                ''',
                'ceqfputilinputprioritybitrate',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpUtilInputPriorityPktRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object represents the QFP input channel priority packet
                rate during this interval.
                ''',
                'ceqfputilinputprioritypktrate',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpUtilInputTotalBitRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object represents the QFP input channel total bit rate
                during this interval, which includes both priority and
                non-priority input bit rate.
                ''',
                'ceqfputilinputtotalbitrate',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpUtilInputTotalPktRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object represents the QFP input channel total packet rate
                during this interval, which includes both priority and
                non-priority input packet rate.
                ''',
                'ceqfputilinputtotalpktrate',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpUtilOutputNonPriorityBitRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object represents the QFP output channel non-priority
                bit rate during this interval.
                ''',
                'ceqfputiloutputnonprioritybitrate',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpUtilOutputNonPriorityPktRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object represents the QFP output channel non-priority
                packet rate during this interval.
                ''',
                'ceqfputiloutputnonprioritypktrate',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpUtilOutputPriorityBitRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object represents the QFP output channel priority bit
                rate during this interval.
                ''',
                'ceqfputiloutputprioritybitrate',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpUtilOutputPriorityPktRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object represents the QFP output channel priority packet
                rate during this interval.
                ''',
                'ceqfputiloutputprioritypktrate',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpUtilOutputTotalBitRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object represents the QFP output channel total bit rate
                during this interval, which includes both priority and
                non-priority bit rate.
                ''',
                'ceqfputiloutputtotalbitrate',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpUtilOutputTotalPktRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object represents the QFP output channel total packet rate
                during this interval, which includes both priority and
                non-priority output packet rate.
                ''',
                'ceqfputiloutputtotalpktrate',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpUtilProcessingLoad', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                This object represents the QFP processing load during this
                interval.
                ''',
                'ceqfputilprocessingload',
                'CISCO-ENTITY-QFP-MIB', False),
            ],
            'CISCO-ENTITY-QFP-MIB',
            'ceqfpUtilizationEntry',
            _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB'
        ),
    },
    'CiscoEntityQfpMib.Ceqfputilizationtable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityQfpMib.Ceqfputilizationtable',
            False, 
            [
            _MetaInfoClassMember('ceqfpUtilizationEntry', REFERENCE_LIST, 'Ceqfputilizationentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoEntityQfpMib.Ceqfputilizationtable.Ceqfputilizationentry', 
                [], [], 
                '''                A conceptual row in the ceqfpUtilizationTable. There is
                an entry in this table for each QFP entity by a value of
                entPhysicalIndex and the supported time interval by a value 
                of ceqfpUtilTimeInterval.
                
                The method of utilization data calculation for each interval
                period can be identified through the respective interval
                scalar objects. For example the utilizaiton data calculation
                method for 'fiveSecond' interval can be identified by
                ceqfpFiveSecondUtilAlgo.
                ''',
                'ceqfputilizationentry',
                'CISCO-ENTITY-QFP-MIB', False),
            ],
            'CISCO-ENTITY-QFP-MIB',
            'ceqfpUtilizationTable',
            _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB'
        ),
    },
    'CiscoEntityQfpMib.Ceqfpmemoryresourcetable.Ceqfpmemoryresourceentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityQfpMib.Ceqfpmemoryresourcetable.Ceqfpmemoryresourceentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-QFP-MIB', True),
            _MetaInfoClassMember('ceqfpMemoryResType', REFERENCE_ENUM_CLASS, 'CiscoqfpmemoryresourceEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoqfpmemoryresourceEnum', 
                [], [], 
                '''                This object indicates the type of the memory resource used by
                the QFP. This object is one of the indices to uniquely identify
                the QFP memory resource type.
                ''',
                'ceqfpmemoryrestype',
                'CISCO-ENTITY-QFP-MIB', True),
            _MetaInfoClassMember('ceqfpMemoryHCResFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object is a 64-bit version of ceqfpMemoryResFree.
                ''',
                'ceqfpmemoryhcresfree',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpMemoryHCResInUse', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object is a 64-bit version of ceqfpMemoryInRes.
                ''',
                'ceqfpmemoryhcresinuse',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpMemoryHCResLowFreeWatermark', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object is a 64-bit version of
                ceqfpMemoryResLowFreeWatermark.
                ''',
                'ceqfpmemoryhcreslowfreewatermark',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpMemoryHCResTotal', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object is a 64-bit version of ceqfpMemoryResTotal.
                ''',
                'ceqfpmemoryhcrestotal',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpMemoryResFallingThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                This object represents the falling threshold value for this
                memory resource. A value of zero means that the falling
                threshold is not supported for this memory resource.
                
                The value of this object can not be set to higher than or
                equal to ceqfpMemoryResRisingThreshold.
                
                A falling (ceqfpMemoryResRisingThreshNotif) notification 
                will be generated, whenever the memory resource usage
                (ceqfpMemoryHCResInUse) is equal to or lesser than this value.
                
                After a falling notification is generated, another 
                such notification will not be generated until the 
                ceqfpMemoryResInUse rises above this value and reaches 
                the ceqfpMemoryResRisingThreshold.
                ''',
                'ceqfpmemoryresfallingthreshold',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpMemoryResFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the memory which is currently free on
                this memory resource.
                ''',
                'ceqfpmemoryresfree',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpMemoryResFreeOvrflw', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the upper 32-bit of ceqfpMemoryResFree.
                This object needs to be supported only when the value of
                ceqfpMemoryResFree exceeds 32-bit, otherwise this object value
                would be set to 0.
                ''',
                'ceqfpmemoryresfreeovrflw',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpMemoryResInUse', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the memory which is currently under use
                on this memory resource.
                ''',
                'ceqfpmemoryresinuse',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpMemoryResInUseOvrflw', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the upper 32-bit of
                ceqfpMemoryResInUse.
                This object needs to be supported only when the value of
                ceqfpMemoryResInUse exceeds 32-bit, otherwise this object value
                would be set to 0.
                ''',
                'ceqfpmemoryresinuseovrflw',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpMemoryResLowFreeWatermark', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents lowest free water mark on this memory
                resource.
                ''',
                'ceqfpmemoryreslowfreewatermark',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpMemoryResLowFreeWatermarkOvrflw', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the upper 32-bit of
                ceqfpMemoryResLowFreeWatermark. This object needs to be
                supported only when the value of ceqfpMemoryResLowFreeWatermark
                exceeds 32-bit, otherwise this object value would be set to 0.
                ''',
                'ceqfpmemoryreslowfreewatermarkovrflw',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpMemoryResRisingThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                This object represents the rising threshold value for this
                memory resource. A value of zero means that the rising
                threshold is not supported for this memory resource.
                
                The value of this object can not be set to lower than or
                equal to ceqfpMemoryResFallingThreshold.
                
                A rising (ceqfpMemoryResRisingThreshNotif) notification
                will be generated, whenever the memory resource usage
                (ceqfpMemoryHCResInUse) is equal to or greater than this
                value.
                
                After a rising notification is generated, another such 
                notification will not be generated until the 
                ceqfpMemoryResInUse falls below this value and reaches 
                the ceqfpMemoryResFallingThreshold.
                ''',
                'ceqfpmemoryresrisingthreshold',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpMemoryResTotal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents total memory available on this memory
                resource.
                ''',
                'ceqfpmemoryrestotal',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpMemoryResTotalOvrflw', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the upper 32-bit of
                ceqfpMemoryResTotal.
                This object needs to be supported only when the value of
                ceqfpMemoryResTotal exceeds 32-bit, otherwise this object value
                would be set to 0.
                ''',
                'ceqfpmemoryrestotalovrflw',
                'CISCO-ENTITY-QFP-MIB', False),
            ],
            'CISCO-ENTITY-QFP-MIB',
            'ceqfpMemoryResourceEntry',
            _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB'
        ),
    },
    'CiscoEntityQfpMib.Ceqfpmemoryresourcetable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityQfpMib.Ceqfpmemoryresourcetable',
            False, 
            [
            _MetaInfoClassMember('ceqfpMemoryResourceEntry', REFERENCE_LIST, 'Ceqfpmemoryresourceentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoEntityQfpMib.Ceqfpmemoryresourcetable.Ceqfpmemoryresourceentry', 
                [], [], 
                '''                A conceptual row in the ceqfpMemoryResourceTable. There
                is an entry in this table for each QFP entity by a value 
                of entPhysicalIndex and the supported memory resource type 
                by a value of ceqfpMemoryResType.
                ''',
                'ceqfpmemoryresourceentry',
                'CISCO-ENTITY-QFP-MIB', False),
            ],
            'CISCO-ENTITY-QFP-MIB',
            'ceqfpMemoryResourceTable',
            _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB'
        ),
    },
    'CiscoEntityQfpMib.Ceqfpthroughputtable.Ceqfpthroughputentry.CeqfpthroughputlevelEnum' : _MetaInfoEnum('CeqfpthroughputlevelEnum', 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB',
        {
            'normal':'normal',
            'warning':'warning',
            'exceed':'exceed',
        }, 'CISCO-ENTITY-QFP-MIB', _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB']),
    'CiscoEntityQfpMib.Ceqfpthroughputtable.Ceqfpthroughputentry' : {
        'meta_info' : _MetaInfoClass('CiscoEntityQfpMib.Ceqfpthroughputtable.Ceqfpthroughputentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-QFP-MIB', True),
            _MetaInfoClassMember('ceqfpThroughputAvgRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The object represents the average throughput rate in the
                interval ceqfpThroughputInterval.
                ''',
                'ceqfpthroughputavgrate',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpThroughputInterval', ATTRIBUTE, 'int' , None, None, 
                [('10', '86400')], [], 
                '''                The object represents the configured time interval at which the
                ceqfpThroughputLevel is checked.
                ''',
                'ceqfpthroughputinterval',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpThroughputLevel', REFERENCE_ENUM_CLASS, 'CeqfpthroughputlevelEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoEntityQfpMib.Ceqfpthroughputtable.Ceqfpthroughputentry.CeqfpthroughputlevelEnum', 
                [], [], 
                '''                This object represents the current throughput level for
                installed throughput license.
                
                                normal  (1) - Throughput usage is normal
                                warning (2) - Throughput usage has crossed the
                                              configured threshold limit
                                exceed  (3) - Throughput usage has exceeded the
                                              total licensed bandwidth
                ''',
                'ceqfpthroughputlevel',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpThroughputLicensedBW', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                This object represents the bandwidth for installed
                throughput license.
                ''',
                'ceqfpthroughputlicensedbw',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpThroughputThreshold', ATTRIBUTE, 'int' , None, None, 
                [('75', '95')], [], 
                '''                The object represents the configured throughput threshold.
                ''',
                'ceqfpthroughputthreshold',
                'CISCO-ENTITY-QFP-MIB', False),
            ],
            'CISCO-ENTITY-QFP-MIB',
            'ceqfpThroughputEntry',
            _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB'
        ),
    },
    'CiscoEntityQfpMib.Ceqfpthroughputtable' : {
        'meta_info' : _MetaInfoClass('CiscoEntityQfpMib.Ceqfpthroughputtable',
            False, 
            [
            _MetaInfoClassMember('ceqfpThroughputEntry', REFERENCE_LIST, 'Ceqfpthroughputentry' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoEntityQfpMib.Ceqfpthroughputtable.Ceqfpthroughputentry', 
                [], [], 
                '''                A conceptual row in the ceqfpThroughputTable. There is an entry
                in this table for each QFP entity, as defined by a value of
                entPhysicalIndex.
                ''',
                'ceqfpthroughputentry',
                'CISCO-ENTITY-QFP-MIB', False),
            ],
            'CISCO-ENTITY-QFP-MIB',
            'ceqfpThroughputTable',
            _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB'
        ),
    },
    'CiscoEntityQfpMib' : {
        'meta_info' : _MetaInfoClass('CiscoEntityQfpMib',
            False, 
            [
            _MetaInfoClassMember('ceqfpMemoryResourceTable', REFERENCE_CLASS, 'Ceqfpmemoryresourcetable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoEntityQfpMib.Ceqfpmemoryresourcetable', 
                [], [], 
                '''                This table maintains the memory resources statistics for
                each QFP physical entity.
                
                An agent creates a conceptual row to this table corresponding
                to a QFP physical entity and its supported memory resource type
                upon detection of a physical entity supporting the memory 
                resource statistics for a memory resource type.
                
                An agent destroys a conceptual row from this table       
                corresponding to a QFP physical entity and its supported
                memory resource type upon removal of the QFP host physical
                entity or it does not receive memory resource statistics
                update for a certain time period. The time period to wait
                before deleting an entry from this table would be the
                discretion of the supporting device.
                ''',
                'ceqfpmemoryresourcetable',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpSystemTable', REFERENCE_CLASS, 'Ceqfpsystemtable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoEntityQfpMib.Ceqfpsystemtable', 
                [], [], 
                '''                This table maintains the QFP system information for each QFP
                physical entity.
                
                An agent creates a conceptual row to this table corresponding
                to a QFP physical entity upon detection of a physical entity
                supporting the QFP system information.
                
                An agent destroys a conceptual row from this table       
                corresponding to a QFP physical entity upon removal
                of the QFP host physical entity.
                ''',
                'ceqfpsystemtable',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpThroughputTable', REFERENCE_CLASS, 'Ceqfpthroughputtable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoEntityQfpMib.Ceqfpthroughputtable', 
                [], [], 
                '''                This table maintains the throughput information for each
                QFP physical entity.
                
                        An agent creates a conceptual row to this table
                corresponding to a QFP physical entity upon detection of a
                physical entity supporting the QFP throughput information.
                
                        An agent destroys a conceptual row from this table     
                
                corresponding to a QFP physical entity upon removal of the QFP
                host physical entity.
                ''',
                'ceqfpthroughputtable',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ceqfpUtilizationTable', REFERENCE_CLASS, 'Ceqfputilizationtable' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoEntityQfpMib.Ceqfputilizationtable', 
                [], [], 
                '''                This table maintains the utilization statistics collected
                by each QFP physical entity at various time interval such as
                last 5 seconds, 1 minute, etc.
                
                An agent creates a conceptual row to this table corresponding
                to a QFP physical entity for a time interval upon detection of
                a physical entity supporting the utilization statistics for a
                time interval.
                
                The agent destroys a conceptual row from this table       
                corresponding to a QFP physical entity for a time interval
                upon removal of the QFP host physical entity or it does not
                receive the utilization statistics update for a certain time
                period. The time period to wait before deleting an entry from
                this table would be the discretion of the supporting device.
                ''',
                'ceqfputilizationtable',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ciscoEntityQfp', REFERENCE_CLASS, 'Ciscoentityqfp' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoEntityQfpMib.Ciscoentityqfp', 
                [], [], 
                '''                ''',
                'ciscoentityqfp',
                'CISCO-ENTITY-QFP-MIB', False),
            _MetaInfoClassMember('ciscoEntityQfpNotif', REFERENCE_CLASS, 'Ciscoentityqfpnotif' , 'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB', 'CiscoEntityQfpMib.Ciscoentityqfpnotif', 
                [], [], 
                '''                ''',
                'ciscoentityqfpnotif',
                'CISCO-ENTITY-QFP-MIB', False),
            ],
            'CISCO-ENTITY-QFP-MIB',
            'CISCO-ENTITY-QFP-MIB',
            _yang_ns._namespaces['CISCO-ENTITY-QFP-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB'
        ),
    },
}
_meta_table['CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry']['meta_info'].parent =_meta_table['CiscoEntityQfpMib.Ceqfpsystemtable']['meta_info']
_meta_table['CiscoEntityQfpMib.Ceqfputilizationtable.Ceqfputilizationentry']['meta_info'].parent =_meta_table['CiscoEntityQfpMib.Ceqfputilizationtable']['meta_info']
_meta_table['CiscoEntityQfpMib.Ceqfpmemoryresourcetable.Ceqfpmemoryresourceentry']['meta_info'].parent =_meta_table['CiscoEntityQfpMib.Ceqfpmemoryresourcetable']['meta_info']
_meta_table['CiscoEntityQfpMib.Ceqfpthroughputtable.Ceqfpthroughputentry']['meta_info'].parent =_meta_table['CiscoEntityQfpMib.Ceqfpthroughputtable']['meta_info']
_meta_table['CiscoEntityQfpMib.Ciscoentityqfp']['meta_info'].parent =_meta_table['CiscoEntityQfpMib']['meta_info']
_meta_table['CiscoEntityQfpMib.Ciscoentityqfpnotif']['meta_info'].parent =_meta_table['CiscoEntityQfpMib']['meta_info']
_meta_table['CiscoEntityQfpMib.Ceqfpsystemtable']['meta_info'].parent =_meta_table['CiscoEntityQfpMib']['meta_info']
_meta_table['CiscoEntityQfpMib.Ceqfputilizationtable']['meta_info'].parent =_meta_table['CiscoEntityQfpMib']['meta_info']
_meta_table['CiscoEntityQfpMib.Ceqfpmemoryresourcetable']['meta_info'].parent =_meta_table['CiscoEntityQfpMib']['meta_info']
_meta_table['CiscoEntityQfpMib.Ceqfpthroughputtable']['meta_info'].parent =_meta_table['CiscoEntityQfpMib']['meta_info']
