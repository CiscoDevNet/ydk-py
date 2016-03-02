


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CiscoEntPerfHistInterval_Enum' : _MetaInfoEnum('CiscoEntPerfHistInterval_Enum', 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB',
        {
            'oneMinute':'ONEMINUTE',
            'fiveMinutes':'FIVEMINUTES',
            'fifteenMinutes':'FIFTEENMINUTES',
        }, 'CISCO-ENTITY-PERFORMANCE-MIB', _yang_ns._namespaces['CISCO-ENTITY-PERFORMANCE-MIB']),
    'CiscoEntPerfIntervalAlgo_Enum' : _MetaInfoEnum('CiscoEntPerfIntervalAlgo_Enum', 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB',
        {
            'unknown':'UNKNOWN',
            'other':'OTHER',
            'current':'CURRENT',
            'algoSMA':'ALGOSMA',
        }, 'CISCO-ENTITY-PERFORMANCE-MIB', _yang_ns._namespaces['CISCO-ENTITY-PERFORMANCE-MIB']),
    'CiscoEntPerfInterval_Enum' : _MetaInfoEnum('CiscoEntPerfInterval_Enum', 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB',
        {
            'current':'CURRENT',
            'oneMinute':'ONEMINUTE',
            'fiveMinutes':'FIVEMINUTES',
            'fifteenMinutes':'FIFTEENMINUTES',
        }, 'CISCO-ENTITY-PERFORMANCE-MIB', _yang_ns._namespaces['CISCO-ENTITY-PERFORMANCE-MIB']),
    'CiscoEntPerfType_Enum' : _MetaInfoEnum('CiscoEntPerfType_Enum', 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB',
        {
            'utilization':'UTILIZATION',
            'bitInputRate':'BITINPUTRATE',
            'bitOutputRate':'BITOUTPUTRATE',
            'bitDropRate':'BITDROPRATE',
            'packetInputRate':'PACKETINPUTRATE',
            'packetOutputRate':'PACKETOUTPUTRATE',
            'packetDropRate':'PACKETDROPRATE',
        }, 'CISCO-ENTITY-PERFORMANCE-MIB', _yang_ns._namespaces['CISCO-ENTITY-PERFORMANCE-MIB']),
    'CiscoEntPerfRange_Enum' : _MetaInfoEnum('CiscoEntPerfRange_Enum', 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB',
        {
            'rangePercentage':'RANGEPERCENTAGE',
            'rangeInt32':'RANGEINT32',
            'rangeInt64':'RANGEINT64',
        }, 'CISCO-ENTITY-PERFORMANCE-MIB', _yang_ns._namespaces['CISCO-ENTITY-PERFORMANCE-MIB']),
    'CISCOENTITYPERFORMANCEMIB.CepConfigTable.CepConfigEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYPERFORMANCEMIB.CepConfigTable.CepConfigEntry',
            False, 
            [
            _MetaInfoClassMember('cepConfigInterval', REFERENCE_ENUM_CLASS, 'CiscoEntPerfInterval_Enum' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CiscoEntPerfInterval_Enum', 
                [], [], 
                '''                This object identifies the time interval for which the
                performance configuration being applied. The interval 
                values can be current, 1 minute, etc. as specified in 
                the CiscoEntPerfInterval.
                ''',
                'cepconfiginterval',
                'CISCO-ENTITY-PERFORMANCE-MIB', True),
            _MetaInfoClassMember('cepConfigPerfType', REFERENCE_ENUM_CLASS, 'CiscoEntPerfType_Enum' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CiscoEntPerfType_Enum', 
                [], [], 
                '''                This object identifies the performance measurement type for
                which the performance configuration being applied.
                ''',
                'cepconfigperftype',
                'CISCO-ENTITY-PERFORMANCE-MIB', True),
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-PERFORMANCE-MIB', True),
            _MetaInfoClassMember('cepConfigFallingThreshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object contains the falling threshold value for a
                specific performance measurement type at a specific
                performance interval. The value of this object must 
                be less than cepConfigRisingThreshold.
                
                The supported range of this object can be identified by
                the object 'cepConfigPerfRange'.
                
                The value of zero indicates that no comparison is being
                made between the cepStatsMeasurement object value and the
                threshold value, therefore no event action will be generated.
                ''',
                'cepconfigfallingthreshold',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            _MetaInfoClassMember('cepConfigPerfRange', REFERENCE_ENUM_CLASS, 'CiscoEntPerfRange_Enum' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CiscoEntPerfRange_Enum', 
                [], [], 
                '''                This object indicates the range used by the performance
                configuration objects such as cepConfigRisingThreshold, etc.
                for the specific performance measurement type.
                ''',
                'cepconfigperfrange',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            _MetaInfoClassMember('cepConfigRisingThreshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object contains the rising threshold value for a
                specific performance measurement type at a specific
                performance time interval. The value of this object must 
                be greater than cepConfigFallingThreshold.
                
                The supported range of this object can be identified by
                the object 'cepConfigPerfRange'.
                
                The value of zero indicates that no comparison is being
                made between the cepStatsMeasurement object value and the
                threshold value, therefore no event action will be generated.
                ''',
                'cepconfigrisingthreshold',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            _MetaInfoClassMember('cepConfigThresholdNotifEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object provides the control to the threshold notification
                for a specific entity performance type at a specific interval.
                
                The notification will be sent based on this object value and the
                global object 'cepThresholdNotifEnabled'. The following table
                would explain when the notification would be generated.
                
                cepThresholdNotifEnabled cepConfigThresholdNotifEnabled Notify
                ======================== ============================== ======
                true                      true                          Yes
                true                      false                         No
                false                     true                          No
                false                     false                         No
                ''',
                'cepconfigthresholdnotifenabled',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            ],
            'CISCO-ENTITY-PERFORMANCE-MIB',
            'cepConfigEntry',
            _yang_ns._namespaces['CISCO-ENTITY-PERFORMANCE-MIB'],
        'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB'
        ),
    },
    'CISCOENTITYPERFORMANCEMIB.CepConfigTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYPERFORMANCEMIB.CepConfigTable',
            False, 
            [
            _MetaInfoClassMember('cepConfigEntry', REFERENCE_LIST, 'CepConfigEntry' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CISCOENTITYPERFORMANCEMIB.CepConfigTable.CepConfigEntry', 
                [], [], 
                '''                A conceptual row in the cepConfigTable. There is an entry in
                this table for each entity by a value of entPhysicalIndex,
                the supported performance time interval by a value of
                cepConfigInterval, and the supported performance type by a 
                value of cepConfigPerfType.
                ''',
                'cepconfigentry',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            ],
            'CISCO-ENTITY-PERFORMANCE-MIB',
            'cepConfigTable',
            _yang_ns._namespaces['CISCO-ENTITY-PERFORMANCE-MIB'],
        'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB'
        ),
    },
    'CISCOENTITYPERFORMANCEMIB.CepEntityIntervalTable.CepEntityIntervalEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYPERFORMANCEMIB.CepEntityIntervalTable.CepEntityIntervalEntry',
            False, 
            [
            _MetaInfoClassMember('cepHistInterval', REFERENCE_ENUM_CLASS, 'CiscoEntPerfHistInterval_Enum' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CiscoEntPerfHistInterval_Enum', 
                [], [], 
                '''                This object identifies the time interval for which the
                performance history being applied. The interval 
                values can be 1 minute, 5 minutes, etc. as specified in 
                the CiscoEntPerfHistInterval.
                ''',
                'cephistinterval',
                'CISCO-ENTITY-PERFORMANCE-MIB', True),
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-PERFORMANCE-MIB', True),
            _MetaInfoClassMember('cepIntervalTimeElapsed', ATTRIBUTE, 'int' , None, None, 
                [(0, 899)], [], 
                '''                This object provides the number of seconds that have elapsed
                since the beginning of the chosen interval on this entity.
                If for some reason, such as an adjustment in the system's
                time-of-day clock, the current interval exceeds the maximum
                value, the agent will return the maximum value for the
                chosen interval.
                
                For example:
                Interval            Maximum value
                ========            =============
                15 minutes            899
                 5 minutes            299
                 1 minutes            59
                ''',
                'cepintervaltimeelapsed',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            _MetaInfoClassMember('cepValidIntervalCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 96)], [], 
                '''                This object provides the number of completed intervals for
                which valid entity performance data has been collected for the
                chosen interval. The value will be 96 unless the entity was
                brought online within the last 1.36/8/24 hours for 1/5/15
                minutes interval respectively, in which case the value will
                be the number of completed 1/5/15 minute intervals since the
                entity has been online.
                ''',
                'cepvalidintervalcount',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            ],
            'CISCO-ENTITY-PERFORMANCE-MIB',
            'cepEntityIntervalEntry',
            _yang_ns._namespaces['CISCO-ENTITY-PERFORMANCE-MIB'],
        'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB'
        ),
    },
    'CISCOENTITYPERFORMANCEMIB.CepEntityIntervalTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYPERFORMANCEMIB.CepEntityIntervalTable',
            False, 
            [
            _MetaInfoClassMember('cepEntityIntervalEntry', REFERENCE_LIST, 'CepEntityIntervalEntry' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CISCOENTITYPERFORMANCEMIB.CepEntityIntervalTable.CepEntityIntervalEntry', 
                [], [], 
                '''                A conceptual row in the cepEntityIntervalTable. There is
                an entry in this table for each entity by a value of
                entPhysicalIndex, and the supported performance history
                time interval by a value of cepHistInterval.
                ''',
                'cepentityintervalentry',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            ],
            'CISCO-ENTITY-PERFORMANCE-MIB',
            'cepEntityIntervalTable',
            _yang_ns._namespaces['CISCO-ENTITY-PERFORMANCE-MIB'],
        'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB'
        ),
    },
    'CISCOENTITYPERFORMANCEMIB.CepEntityTable.CepEntityEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYPERFORMANCEMIB.CepEntityTable.CepEntityEntry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-PERFORMANCE-MIB', True),
            _MetaInfoClassMember('cepEntityLastReloadTime', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object provides the entity last reload time.
                ''',
                'cepentitylastreloadtime',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            _MetaInfoClassMember('cepEntityNumReloads', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object provides the number of times the entity is
                reloaded, since the entity host is up.
                ''',
                'cepentitynumreloads',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            ],
            'CISCO-ENTITY-PERFORMANCE-MIB',
            'cepEntityEntry',
            _yang_ns._namespaces['CISCO-ENTITY-PERFORMANCE-MIB'],
        'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB'
        ),
    },
    'CISCOENTITYPERFORMANCEMIB.CepEntityTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYPERFORMANCEMIB.CepEntityTable',
            False, 
            [
            _MetaInfoClassMember('cepEntityEntry', REFERENCE_LIST, 'CepEntityEntry' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CISCOENTITYPERFORMANCEMIB.CepEntityTable.CepEntityEntry', 
                [], [], 
                '''                A conceptual row in the cepEntityTable. There is an entry
                in this table for each entity which supports performance
                monitoring, as defined by a value of entPhysicalIndex.
                ''',
                'cepentityentry',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            ],
            'CISCO-ENTITY-PERFORMANCE-MIB',
            'cepEntityTable',
            _yang_ns._namespaces['CISCO-ENTITY-PERFORMANCE-MIB'],
        'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB'
        ),
    },
    'CISCOENTITYPERFORMANCEMIB.CepIntervalStatsTable.CepIntervalStatsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYPERFORMANCEMIB.CepIntervalStatsTable.CepIntervalStatsEntry',
            False, 
            [
            _MetaInfoClassMember('cepConfigPerfType', REFERENCE_ENUM_CLASS, 'CiscoEntPerfType_Enum' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CiscoEntPerfType_Enum', 
                [], [], 
                '''                ''',
                'cepconfigperftype',
                'CISCO-ENTITY-PERFORMANCE-MIB', True),
            _MetaInfoClassMember('cepHistInterval', REFERENCE_ENUM_CLASS, 'CiscoEntPerfHistInterval_Enum' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CiscoEntPerfHistInterval_Enum', 
                [], [], 
                '''                ''',
                'cephistinterval',
                'CISCO-ENTITY-PERFORMANCE-MIB', True),
            _MetaInfoClassMember('cepIntervalNumber', ATTRIBUTE, 'int' , None, None, 
                [(1, 96)], [], 
                '''                An interval number between 1 and 96, where 1 is the most
                recently completed interval and 96 is the least recently
                completed interval.
                
                For example, if it is 15 minutes interval history, then the
                96 is the interval number completed 23 hours and 45 minutes
                prior to interval 1.
                ''',
                'cepintervalnumber',
                'CISCO-ENTITY-PERFORMANCE-MIB', True),
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-PERFORMANCE-MIB', True),
            _MetaInfoClassMember('cepIntervalStatsCreateTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object provides the time stamp at which the specific
                performance statistics gets created.
                ''',
                'cepintervalstatscreatetime',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            _MetaInfoClassMember('cepIntervalStatsMeasurement', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object provides the specific performance statistics of
                an entity over the specified interval. The range of this object
                can be identified by object 'cepIntervalStatsRange'.
                ''',
                'cepintervalstatsmeasurement',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            _MetaInfoClassMember('cepIntervalStatsRange', REFERENCE_ENUM_CLASS, 'CiscoEntPerfRange_Enum' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CiscoEntPerfRange_Enum', 
                [], [], 
                '''                This object provides the range information for the object
                'cepIntervalStatsMeasurement'.
                ''',
                'cepintervalstatsrange',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            _MetaInfoClassMember('cepIntervalStatsValidData', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object indicates whether the performance statistics for
                this interval is valid. The value 'true' means the performance
                statistics is valid, otherwise the performance statistics is
                invalid for the interval.
                ''',
                'cepintervalstatsvaliddata',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            ],
            'CISCO-ENTITY-PERFORMANCE-MIB',
            'cepIntervalStatsEntry',
            _yang_ns._namespaces['CISCO-ENTITY-PERFORMANCE-MIB'],
        'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB'
        ),
    },
    'CISCOENTITYPERFORMANCEMIB.CepIntervalStatsTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYPERFORMANCEMIB.CepIntervalStatsTable',
            False, 
            [
            _MetaInfoClassMember('cepIntervalStatsEntry', REFERENCE_LIST, 'CepIntervalStatsEntry' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CISCOENTITYPERFORMANCEMIB.CepIntervalStatsTable.CepIntervalStatsEntry', 
                [], [], 
                '''                A conceptual row in the cepIntervalStatsTable. There is
                an entry in this table for each entity by a value of
                entPhysicalIndex, the supported performance history time
                interval by a value of cepHistInterval, the supported
                performance statistics by a value of cepConfigPerfType
                and the interval number by a value of cepIntervalNumber.
                ''',
                'cepintervalstatsentry',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            ],
            'CISCO-ENTITY-PERFORMANCE-MIB',
            'cepIntervalStatsTable',
            _yang_ns._namespaces['CISCO-ENTITY-PERFORMANCE-MIB'],
        'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB'
        ),
    },
    'CISCOENTITYPERFORMANCEMIB.CepStatsTable.CepStatsEntry' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYPERFORMANCEMIB.CepStatsTable.CepStatsEntry',
            False, 
            [
            _MetaInfoClassMember('cepConfigInterval', REFERENCE_ENUM_CLASS, 'CiscoEntPerfInterval_Enum' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CiscoEntPerfInterval_Enum', 
                [], [], 
                '''                ''',
                'cepconfiginterval',
                'CISCO-ENTITY-PERFORMANCE-MIB', True),
            _MetaInfoClassMember('cepConfigPerfType', REFERENCE_ENUM_CLASS, 'CiscoEntPerfType_Enum' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CiscoEntPerfType_Enum', 
                [], [], 
                '''                ''',
                'cepconfigperftype',
                'CISCO-ENTITY-PERFORMANCE-MIB', True),
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENTITY-PERFORMANCE-MIB', True),
            _MetaInfoClassMember('cepStatsAlgorithm', REFERENCE_ENUM_CLASS, 'CiscoEntPerfIntervalAlgo_Enum' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CiscoEntPerfIntervalAlgo_Enum', 
                [], [], 
                '''                This object provides the algorithm used to calculate the
                entity performance statistics over the specified interval.
                ''',
                'cepstatsalgorithm',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            _MetaInfoClassMember('cepStatsMeasurement', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object provides a specific performance measurement of the
                entity over the specified interval. The range of this object
                can be identified by the object 'cepConfigPerfRange'.
                ''',
                'cepstatsmeasurement',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            ],
            'CISCO-ENTITY-PERFORMANCE-MIB',
            'cepStatsEntry',
            _yang_ns._namespaces['CISCO-ENTITY-PERFORMANCE-MIB'],
        'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB'
        ),
    },
    'CISCOENTITYPERFORMANCEMIB.CepStatsTable' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYPERFORMANCEMIB.CepStatsTable',
            False, 
            [
            _MetaInfoClassMember('cepStatsEntry', REFERENCE_LIST, 'CepStatsEntry' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CISCOENTITYPERFORMANCEMIB.CepStatsTable.CepStatsEntry', 
                [], [], 
                '''                A conceptual row in the cepStatsTable. There is an entry in
                this table for each entity by a value of entPhysicalIndex,
                the supported performance time interval by a value of
                cepConfigInterval, and the supported performance type by a 
                value of cepConfigPerfType.
                ''',
                'cepstatsentry',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            ],
            'CISCO-ENTITY-PERFORMANCE-MIB',
            'cepStatsTable',
            _yang_ns._namespaces['CISCO-ENTITY-PERFORMANCE-MIB'],
        'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB'
        ),
    },
    'CISCOENTITYPERFORMANCEMIB.CiscoEntityPerformanceMIBNotifObjects' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYPERFORMANCEMIB.CiscoEntityPerformanceMIBNotifObjects',
            False, 
            [
            _MetaInfoClassMember('cepThresholdNotifEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This object controls the entity performance measurement
                rising/falling threshold notification. When this object
                contains a value of 'true', then generation of entity
                rising/falling threshold notification is enabled. If this
                object contains a value of 'false', then generation of
                entity rising/falling threshold notification is disabled.
                
                The generation of the rising/falling threshold depends
                on this global value as well as the object
                'cepConfigThresholdNotifEnabled' present in cepConfigTable.
                ''',
                'cepthresholdnotifenabled',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            ],
            'CISCO-ENTITY-PERFORMANCE-MIB',
            'ciscoEntityPerformanceMIBNotifObjects',
            _yang_ns._namespaces['CISCO-ENTITY-PERFORMANCE-MIB'],
        'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB'
        ),
    },
    'CISCOENTITYPERFORMANCEMIB' : {
        'meta_info' : _MetaInfoClass('CISCOENTITYPERFORMANCEMIB',
            False, 
            [
            _MetaInfoClassMember('cepConfigTable', REFERENCE_CLASS, 'CepConfigTable' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CISCOENTITYPERFORMANCEMIB.CepConfigTable', 
                [], [], 
                '''                This table maintains the performance configuration information
                for each physical entity at various performance time intervals
                such as current, 1 minute, etc.
                
                An agent creates a conceptual row to this table corresponding
                to a physical entity for each supported performance measurement 
                and a performance interval upon detection.
                
                The agent destroys a conceptual row from this table       
                corresponding to a physical entity for a specific 
                performance measurement and an interval upon removal 
                of the physical entity.
                ''',
                'cepconfigtable',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            _MetaInfoClassMember('cepEntityIntervalTable', REFERENCE_CLASS, 'CepEntityIntervalTable' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CISCOENTITYPERFORMANCEMIB.CepEntityIntervalTable', 
                [], [], 
                '''                This table maintains the interval information for each entity
                at various interval period.
                
                An agent creates a conceptual row to this table corresponding
                to a physical entity upon detection of a physical entity
                supporting the specific performance interval statistics
                collection.
                
                An agent destroys a conceptual row from this table
                corresponding to a physical entity upon removal of
                the physical entity.
                ''',
                'cepentityintervaltable',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            _MetaInfoClassMember('cepEntityTable', REFERENCE_CLASS, 'CepEntityTable' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CISCOENTITYPERFORMANCEMIB.CepEntityTable', 
                [], [], 
                '''                This table maintains the specific performance information for
                each physical entity, which supports performance monitoring.
                
                An agent creates a conceptual row to this table corresponding
                to a physical entity upon detection of a physical entity
                supporting the performance monitoring.
                
                An agent destroys a conceptual row from this table
                corresponding to a physical entity upon removal of
                the physical entity.
                ''',
                'cepentitytable',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            _MetaInfoClassMember('cepIntervalStatsTable', REFERENCE_CLASS, 'CepIntervalStatsTable' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CISCOENTITYPERFORMANCEMIB.CepIntervalStatsTable', 
                [], [], 
                '''                This table contains specific performance statistics collected
                by each entity over the specified interval.
                
                The table has the maximum of 96 buckets for all the supported
                intervals. The following table would list the total hours of
                history maintained for various intervals. 
                
                Intervals (minutes)  Buckets        History
                =========            =======        =======
                15                    96            24 hours
                5                     96             8 hours
                1                     96             1 hour 36 minutes
                
                An agent creates a conceptual row to this table corresponding
                to a physical entity upon detection of a physical entity
                supporting the specific performance statistics for a specific
                interval.
                
                An agent destroys a conceptual row from this table
                corresponding to a physical entity upon removal of
                the physical entity.
                
                The support for 15-minutes interval history is required for
                all the entities supporting performance data. However, the
                support for 1-minute and 5-minutes interval history for 
                entities are optional and at the descretion of the device
                supporting the performance monitoring.
                ''',
                'cepintervalstatstable',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            _MetaInfoClassMember('cepStatsTable', REFERENCE_CLASS, 'CepStatsTable' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CISCOENTITYPERFORMANCEMIB.CepStatsTable', 
                [], [], 
                '''                This table maintains entity running performance, which
                are collected at various performance intervals.
                
                An agent creates a conceptual row to this table corresponding
                to a physical entity for each supported performance measurement 
                and a performance interval upon detection.
                
                The agent destroys a conceptual row from this table       
                corresponding to a physical entity for a specific 
                performance measurement and an interval upon removal 
                of the physical entity.
                ''',
                'cepstatstable',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            _MetaInfoClassMember('ciscoEntityPerformanceMIBNotifObjects', REFERENCE_CLASS, 'CiscoEntityPerformanceMIBNotifObjects' , 'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB', 'CISCOENTITYPERFORMANCEMIB.CiscoEntityPerformanceMIBNotifObjects', 
                [], [], 
                '''                ''',
                'ciscoentityperformancemibnotifobjects',
                'CISCO-ENTITY-PERFORMANCE-MIB', False),
            ],
            'CISCO-ENTITY-PERFORMANCE-MIB',
            'CISCO-ENTITY-PERFORMANCE-MIB',
            _yang_ns._namespaces['CISCO-ENTITY-PERFORMANCE-MIB'],
        'ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB'
        ),
    },
}
_meta_table['CISCOENTITYPERFORMANCEMIB.CepConfigTable.CepConfigEntry']['meta_info'].parent =_meta_table['CISCOENTITYPERFORMANCEMIB.CepConfigTable']['meta_info']
_meta_table['CISCOENTITYPERFORMANCEMIB.CepEntityIntervalTable.CepEntityIntervalEntry']['meta_info'].parent =_meta_table['CISCOENTITYPERFORMANCEMIB.CepEntityIntervalTable']['meta_info']
_meta_table['CISCOENTITYPERFORMANCEMIB.CepEntityTable.CepEntityEntry']['meta_info'].parent =_meta_table['CISCOENTITYPERFORMANCEMIB.CepEntityTable']['meta_info']
_meta_table['CISCOENTITYPERFORMANCEMIB.CepIntervalStatsTable.CepIntervalStatsEntry']['meta_info'].parent =_meta_table['CISCOENTITYPERFORMANCEMIB.CepIntervalStatsTable']['meta_info']
_meta_table['CISCOENTITYPERFORMANCEMIB.CepStatsTable.CepStatsEntry']['meta_info'].parent =_meta_table['CISCOENTITYPERFORMANCEMIB.CepStatsTable']['meta_info']
_meta_table['CISCOENTITYPERFORMANCEMIB.CepConfigTable']['meta_info'].parent =_meta_table['CISCOENTITYPERFORMANCEMIB']['meta_info']
_meta_table['CISCOENTITYPERFORMANCEMIB.CepEntityIntervalTable']['meta_info'].parent =_meta_table['CISCOENTITYPERFORMANCEMIB']['meta_info']
_meta_table['CISCOENTITYPERFORMANCEMIB.CepEntityTable']['meta_info'].parent =_meta_table['CISCOENTITYPERFORMANCEMIB']['meta_info']
_meta_table['CISCOENTITYPERFORMANCEMIB.CepIntervalStatsTable']['meta_info'].parent =_meta_table['CISCOENTITYPERFORMANCEMIB']['meta_info']
_meta_table['CISCOENTITYPERFORMANCEMIB.CepStatsTable']['meta_info'].parent =_meta_table['CISCOENTITYPERFORMANCEMIB']['meta_info']
_meta_table['CISCOENTITYPERFORMANCEMIB.CiscoEntityPerformanceMIBNotifObjects']['meta_info'].parent =_meta_table['CISCOENTITYPERFORMANCEMIB']['meta_info']
