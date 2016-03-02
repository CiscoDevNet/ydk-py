""" CISCO_ENTITY_PERFORMANCE_MIB 

This MIB module defines managed objects that facilitate to
monitor performance of any physical entity, which are listed in
the ENTITY\-MIB (RFC 4133) entPhysicalTable.

The performance monitoring includes utilization, input/output
packet/byte rates, etc. This monitoring is through the
measurement periods of current, 1\-minute, 5\-minutes,
15\-minutes.

The performance data calculation method would vary for each
entity for a specific interval, hence users of this MIB should
obtain the information using the object cepStatsAlgorithm for a
specific interval.

The performance statistics can be accumulated for the 1\-minute,
5\-minutes and 15\-minutes (recommended) intervals. At any one
time, an agent maintains one current (incomplete) interval for
each interval type and up to 96 completed interval number. Fewer
than 96 interval number of data will be available if the agent
has been restarted within the last 24 hours for 15 minutes
interval, 8 hours for 5 minutes interval, and 1.36 hours for 1
minute interval.

There is no requirement for an agent to ensure fixed
relationship between the start of a one/five/fifteen minute
intervals and wall clock, however some agents may align the
fifteen minutes interval with quarter hours.

The following terminologies apply within the scope of this MIB.

o entity \- Any physical entity which can support performance 
           monitoring as specified in this MIB

o Utilization \- The ratio of current usage to the maximum 
                capacity the entity can handle

o Input \- Communication channel where packets arrive on the
          entity

o Output \- Communication channel where packets leave the entity

Acronyms
========
SMA \- Simple Moving Average

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CiscoEntPerfHistInterval_Enum(Enum):
    """
    CiscoEntPerfHistInterval_Enum

    This textual convention denotes an enumerated integer\-value
    that represents the available interval values for which the
    historic performance statistics are to be collected.
    
    oneMinute (1)       \- Last 1 minute statistics
    fiveMinutes (2)     \- Last 5 minutes statistics
    fifteenMinutes (3)  \- Last 15 minutes statistics

    """

    ONEMINUTE = 1

    FIVEMINUTES = 2

    FIFTEENMINUTES = 3


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_PERFORMANCE_MIB as meta
        return meta._meta_table['CiscoEntPerfHistInterval_Enum']


class CiscoEntPerfIntervalAlgo_Enum(Enum):
    """
    CiscoEntPerfIntervalAlgo_Enum

    This textual convention denotes an enumerated integer\-value
    that represents the method used to calculate the specific
    interval data.
    
    unknown (1) \- The calculation method is unknown
    other (2)   \- The calculation method is not list in this       
                  enumeration.
    current (3) \- This is current data
    algoSMA (4) \- Simple Moving Average over the specified interval

    """

    UNKNOWN = 1

    OTHER = 2

    CURRENT = 3

    ALGOSMA = 4


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_PERFORMANCE_MIB as meta
        return meta._meta_table['CiscoEntPerfIntervalAlgo_Enum']


class CiscoEntPerfInterval_Enum(Enum):
    """
    CiscoEntPerfInterval_Enum

    This textual convention denotes an enumerated integer\-value
    that represents the available interval values for which the
    periodic statistics are to be collected.
    
    current (1)         \- Current interval to collect statistics.
                          In case of any entity which only start
                          collecting statistics from last 5/10
                          seconds then the entity can choose this
                          interval
    oneMinute (2)       \- Interval to collect last 1 minute       
                          statistics
    fiveMinutes (3)     \- Interval to collect last 5 minutes
                          statistics
    fifteenMinutes (4)  \- Interval to collect last 15 minutes 
                          statistics

    """

    CURRENT = 1

    ONEMINUTE = 2

    FIVEMINUTES = 3

    FIFTEENMINUTES = 4


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_PERFORMANCE_MIB as meta
        return meta._meta_table['CiscoEntPerfInterval_Enum']


class CiscoEntPerfRange_Enum(Enum):
    """
    CiscoEntPerfRange_Enum

    This textual convention indicates the allowed range for
    the specified measurement of entity performance.
    
    rangePercentage(1)  0 \- 100
    rangeInt32(2)       0 \- 4294967295
    rangeInt64(3)       0 \- 18446744073709551615

    """

    RANGEPERCENTAGE = 1

    RANGEINT32 = 2

    RANGEINT64 = 3


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_PERFORMANCE_MIB as meta
        return meta._meta_table['CiscoEntPerfRange_Enum']


class CiscoEntPerfType_Enum(Enum):
    """
    CiscoEntPerfType_Enum

    This textual convention denotes an enumerated integer\-value
    that represents the available various measurement types.
    
    utilization(1) \- The ratio of current usage to the maximum 
                     capacity the entity can handle
    bitInputRate(2) \- Input bit rate
    bitOutputRate(3) \- Output bit rate
    bitDropRate(4) \-  Drop bit rate
    packetInputRate(5) \- Input packet rate
    packetOutputRate(6) \- Output packet rate
    packetDropRate(7) \-  Drop packet rate

    """

    UTILIZATION = 1

    BITINPUTRATE = 2

    BITOUTPUTRATE = 3

    BITDROPRATE = 4

    PACKETINPUTRATE = 5

    PACKETOUTPUTRATE = 6

    PACKETDROPRATE = 7


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_PERFORMANCE_MIB as meta
        return meta._meta_table['CiscoEntPerfType_Enum']



class CISCOENTITYPERFORMANCEMIB(object):
    """
    
    
    .. attribute:: cepconfigtable
    
    	This table maintains the performance configuration information for each physical entity at various performance time intervals such as current, 1 minute, etc.  An agent creates a conceptual row to this table corresponding to a physical entity for each supported performance measurement  and a performance interval upon detection.  The agent destroys a conceptual row from this table        corresponding to a physical entity for a specific  performance measurement and an interval upon removal  of the physical entity
    	**type**\: :py:class:`CepConfigTable <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CISCOENTITYPERFORMANCEMIB.CepConfigTable>`
    
    .. attribute:: cepentityintervaltable
    
    	This table maintains the interval information for each entity at various interval period.  An agent creates a conceptual row to this table corresponding to a physical entity upon detection of a physical entity supporting the specific performance interval statistics collection.  An agent destroys a conceptual row from this table corresponding to a physical entity upon removal of the physical entity
    	**type**\: :py:class:`CepEntityIntervalTable <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CISCOENTITYPERFORMANCEMIB.CepEntityIntervalTable>`
    
    .. attribute:: cepentitytable
    
    	This table maintains the specific performance information for each physical entity, which supports performance monitoring.  An agent creates a conceptual row to this table corresponding to a physical entity upon detection of a physical entity supporting the performance monitoring.  An agent destroys a conceptual row from this table corresponding to a physical entity upon removal of the physical entity
    	**type**\: :py:class:`CepEntityTable <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CISCOENTITYPERFORMANCEMIB.CepEntityTable>`
    
    .. attribute:: cepintervalstatstable
    
    	This table contains specific performance statistics collected by each entity over the specified interval.  The table has the maximum of 96 buckets for all the supported intervals. The following table would list the total hours of history maintained for various intervals.   Intervals (minutes)  Buckets        History =========            =======        ======= 15                    96            24 hours 5                     96             8 hours 1                     96             1 hour 36 minutes  An agent creates a conceptual row to this table corresponding to a physical entity upon detection of a physical entity supporting the specific performance statistics for a specific interval.  An agent destroys a conceptual row from this table corresponding to a physical entity upon removal of the physical entity.  The support for 15\-minutes interval history is required for all the entities supporting performance data. However, the support for 1\-minute and 5\-minutes interval history for  entities are optional and at the descretion of the device supporting the performance monitoring
    	**type**\: :py:class:`CepIntervalStatsTable <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CISCOENTITYPERFORMANCEMIB.CepIntervalStatsTable>`
    
    .. attribute:: cepstatstable
    
    	This table maintains entity running performance, which are collected at various performance intervals.  An agent creates a conceptual row to this table corresponding to a physical entity for each supported performance measurement  and a performance interval upon detection.  The agent destroys a conceptual row from this table        corresponding to a physical entity for a specific  performance measurement and an interval upon removal  of the physical entity
    	**type**\: :py:class:`CepStatsTable <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CISCOENTITYPERFORMANCEMIB.CepStatsTable>`
    
    .. attribute:: ciscoentityperformancemibnotifobjects
    
    	
    	**type**\: :py:class:`CiscoEntityPerformanceMIBNotifObjects <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CISCOENTITYPERFORMANCEMIB.CiscoEntityPerformanceMIBNotifObjects>`
    
    

    """

    _prefix = 'cisco-entity'
    _revision = '2010-09-09'

    def __init__(self):
        self.cepconfigtable = CISCOENTITYPERFORMANCEMIB.CepConfigTable()
        self.cepconfigtable.parent = self
        self.cepentityintervaltable = CISCOENTITYPERFORMANCEMIB.CepEntityIntervalTable()
        self.cepentityintervaltable.parent = self
        self.cepentitytable = CISCOENTITYPERFORMANCEMIB.CepEntityTable()
        self.cepentitytable.parent = self
        self.cepintervalstatstable = CISCOENTITYPERFORMANCEMIB.CepIntervalStatsTable()
        self.cepintervalstatstable.parent = self
        self.cepstatstable = CISCOENTITYPERFORMANCEMIB.CepStatsTable()
        self.cepstatstable.parent = self
        self.ciscoentityperformancemibnotifobjects = CISCOENTITYPERFORMANCEMIB.CiscoEntityPerformanceMIBNotifObjects()
        self.ciscoentityperformancemibnotifobjects.parent = self


    class CepConfigTable(object):
        """
        This table maintains the performance configuration information
        for each physical entity at various performance time intervals
        such as current, 1 minute, etc.
        
        An agent creates a conceptual row to this table corresponding
        to a physical entity for each supported performance measurement 
        and a performance interval upon detection.
        
        The agent destroys a conceptual row from this table       
        corresponding to a physical entity for a specific 
        performance measurement and an interval upon removal 
        of the physical entity.
        
        .. attribute:: cepconfigentry
        
        	A conceptual row in the cepConfigTable. There is an entry in this table for each entity by a value of entPhysicalIndex, the supported performance time interval by a value of cepConfigInterval, and the supported performance type by a  value of cepConfigPerfType
        	**type**\: list of :py:class:`CepConfigEntry <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CISCOENTITYPERFORMANCEMIB.CepConfigTable.CepConfigEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2010-09-09'

        def __init__(self):
            self.parent = None
            self.cepconfigentry = YList()
            self.cepconfigentry.parent = self
            self.cepconfigentry.name = 'cepconfigentry'


        class CepConfigEntry(object):
            """
            A conceptual row in the cepConfigTable. There is an entry in
            this table for each entity by a value of entPhysicalIndex,
            the supported performance time interval by a value of
            cepConfigInterval, and the supported performance type by a 
            value of cepConfigPerfType.
            
            .. attribute:: cepconfiginterval
            
            	This object identifies the time interval for which the performance configuration being applied. The interval  values can be current, 1 minute, etc. as specified in  the CiscoEntPerfInterval
            	**type**\: :py:class:`CiscoEntPerfInterval_Enum <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CiscoEntPerfInterval_Enum>`
            
            .. attribute:: cepconfigperftype
            
            	This object identifies the performance measurement type for which the performance configuration being applied
            	**type**\: :py:class:`CiscoEntPerfType_Enum <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CiscoEntPerfType_Enum>`
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cepconfigfallingthreshold
            
            	This object contains the falling threshold value for a specific performance measurement type at a specific performance interval. The value of this object must  be less than cepConfigRisingThreshold.  The supported range of this object can be identified by the object 'cepConfigPerfRange'.  The value of zero indicates that no comparison is being made between the cepStatsMeasurement object value and the threshold value, therefore no event action will be generated
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cepconfigperfrange
            
            	This object indicates the range used by the performance configuration objects such as cepConfigRisingThreshold, etc. for the specific performance measurement type
            	**type**\: :py:class:`CiscoEntPerfRange_Enum <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CiscoEntPerfRange_Enum>`
            
            .. attribute:: cepconfigrisingthreshold
            
            	This object contains the rising threshold value for a specific performance measurement type at a specific performance time interval. The value of this object must  be greater than cepConfigFallingThreshold.  The supported range of this object can be identified by the object 'cepConfigPerfRange'.  The value of zero indicates that no comparison is being made between the cepStatsMeasurement object value and the threshold value, therefore no event action will be generated
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cepconfigthresholdnotifenabled
            
            	This object provides the control to the threshold notification for a specific entity performance type at a specific interval.  The notification will be sent based on this object value and the global object 'cepThresholdNotifEnabled'. The following table would explain when the notification would be generated.  cepThresholdNotifEnabled cepConfigThresholdNotifEnabled Notify ======================== ============================== ====== true                      true                          Yes true                      false                         No false                     true                          No false                     false                         No
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2010-09-09'

            def __init__(self):
                self.parent = None
                self.cepconfiginterval = None
                self.cepconfigperftype = None
                self.entphysicalindex = None
                self.cepconfigfallingthreshold = None
                self.cepconfigperfrange = None
                self.cepconfigrisingthreshold = None
                self.cepconfigthresholdnotifenabled = None

            @property
            def _common_path(self):
                if self.cepconfiginterval is None:
                    raise YPYDataValidationError('Key property cepconfiginterval is None')
                if self.cepconfigperftype is None:
                    raise YPYDataValidationError('Key property cepconfigperftype is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-PERFORMANCE-MIB:CISCO-ENTITY-PERFORMANCE-MIB/CISCO-ENTITY-PERFORMANCE-MIB:cepConfigTable/CISCO-ENTITY-PERFORMANCE-MIB:cepConfigEntry[CISCO-ENTITY-PERFORMANCE-MIB:cepConfigInterval = ' + str(self.cepconfiginterval) + '][CISCO-ENTITY-PERFORMANCE-MIB:cepConfigPerfType = ' + str(self.cepconfigperftype) + '][CISCO-ENTITY-PERFORMANCE-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cepconfiginterval is not None:
                    return True

                if self.cepconfigperftype is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.cepconfigfallingthreshold is not None:
                    return True

                if self.cepconfigperfrange is not None:
                    return True

                if self.cepconfigrisingthreshold is not None:
                    return True

                if self.cepconfigthresholdnotifenabled is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_PERFORMANCE_MIB as meta
                return meta._meta_table['CISCOENTITYPERFORMANCEMIB.CepConfigTable.CepConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-PERFORMANCE-MIB:CISCO-ENTITY-PERFORMANCE-MIB/CISCO-ENTITY-PERFORMANCE-MIB:cepConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cepconfigentry is not None:
                for child_ref in self.cepconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_PERFORMANCE_MIB as meta
            return meta._meta_table['CISCOENTITYPERFORMANCEMIB.CepConfigTable']['meta_info']


    class CepEntityIntervalTable(object):
        """
        This table maintains the interval information for each entity
        at various interval period.
        
        An agent creates a conceptual row to this table corresponding
        to a physical entity upon detection of a physical entity
        supporting the specific performance interval statistics
        collection.
        
        An agent destroys a conceptual row from this table
        corresponding to a physical entity upon removal of
        the physical entity.
        
        .. attribute:: cepentityintervalentry
        
        	A conceptual row in the cepEntityIntervalTable. There is an entry in this table for each entity by a value of entPhysicalIndex, and the supported performance history time interval by a value of cepHistInterval
        	**type**\: list of :py:class:`CepEntityIntervalEntry <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CISCOENTITYPERFORMANCEMIB.CepEntityIntervalTable.CepEntityIntervalEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2010-09-09'

        def __init__(self):
            self.parent = None
            self.cepentityintervalentry = YList()
            self.cepentityintervalentry.parent = self
            self.cepentityintervalentry.name = 'cepentityintervalentry'


        class CepEntityIntervalEntry(object):
            """
            A conceptual row in the cepEntityIntervalTable. There is
            an entry in this table for each entity by a value of
            entPhysicalIndex, and the supported performance history
            time interval by a value of cepHistInterval.
            
            .. attribute:: cephistinterval
            
            	This object identifies the time interval for which the performance history being applied. The interval  values can be 1 minute, 5 minutes, etc. as specified in  the CiscoEntPerfHistInterval
            	**type**\: :py:class:`CiscoEntPerfHistInterval_Enum <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CiscoEntPerfHistInterval_Enum>`
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cepintervaltimeelapsed
            
            	This object provides the number of seconds that have elapsed since the beginning of the chosen interval on this entity. If for some reason, such as an adjustment in the system's time\-of\-day clock, the current interval exceeds the maximum value, the agent will return the maximum value for the chosen interval.  For example\: Interval            Maximum value ========            ============= 15 minutes            899  5 minutes            299  1 minutes            59
            	**type**\: int
            
            	**range:** 0..899
            
            .. attribute:: cepvalidintervalcount
            
            	This object provides the number of completed intervals for which valid entity performance data has been collected for the chosen interval. The value will be 96 unless the entity was brought online within the last 1.36/8/24 hours for 1/5/15 minutes interval respectively, in which case the value will be the number of completed 1/5/15 minute intervals since the entity has been online
            	**type**\: int
            
            	**range:** 0..96
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2010-09-09'

            def __init__(self):
                self.parent = None
                self.cephistinterval = None
                self.entphysicalindex = None
                self.cepintervaltimeelapsed = None
                self.cepvalidintervalcount = None

            @property
            def _common_path(self):
                if self.cephistinterval is None:
                    raise YPYDataValidationError('Key property cephistinterval is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-PERFORMANCE-MIB:CISCO-ENTITY-PERFORMANCE-MIB/CISCO-ENTITY-PERFORMANCE-MIB:cepEntityIntervalTable/CISCO-ENTITY-PERFORMANCE-MIB:cepEntityIntervalEntry[CISCO-ENTITY-PERFORMANCE-MIB:cepHistInterval = ' + str(self.cephistinterval) + '][CISCO-ENTITY-PERFORMANCE-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cephistinterval is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.cepintervaltimeelapsed is not None:
                    return True

                if self.cepvalidintervalcount is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_PERFORMANCE_MIB as meta
                return meta._meta_table['CISCOENTITYPERFORMANCEMIB.CepEntityIntervalTable.CepEntityIntervalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-PERFORMANCE-MIB:CISCO-ENTITY-PERFORMANCE-MIB/CISCO-ENTITY-PERFORMANCE-MIB:cepEntityIntervalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cepentityintervalentry is not None:
                for child_ref in self.cepentityintervalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_PERFORMANCE_MIB as meta
            return meta._meta_table['CISCOENTITYPERFORMANCEMIB.CepEntityIntervalTable']['meta_info']


    class CepEntityTable(object):
        """
        This table maintains the specific performance information for
        each physical entity, which supports performance monitoring.
        
        An agent creates a conceptual row to this table corresponding
        to a physical entity upon detection of a physical entity
        supporting the performance monitoring.
        
        An agent destroys a conceptual row from this table
        corresponding to a physical entity upon removal of
        the physical entity.
        
        .. attribute:: cepentityentry
        
        	A conceptual row in the cepEntityTable. There is an entry in this table for each entity which supports performance monitoring, as defined by a value of entPhysicalIndex
        	**type**\: list of :py:class:`CepEntityEntry <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CISCOENTITYPERFORMANCEMIB.CepEntityTable.CepEntityEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2010-09-09'

        def __init__(self):
            self.parent = None
            self.cepentityentry = YList()
            self.cepentityentry.parent = self
            self.cepentityentry.name = 'cepentityentry'


        class CepEntityEntry(object):
            """
            A conceptual row in the cepEntityTable. There is an entry
            in this table for each entity which supports performance
            monitoring, as defined by a value of entPhysicalIndex.
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cepentitylastreloadtime
            
            	This object provides the entity last reload time
            	**type**\: str
            
            .. attribute:: cepentitynumreloads
            
            	This object provides the number of times the entity is reloaded, since the entity host is up
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2010-09-09'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cepentitylastreloadtime = None
                self.cepentitynumreloads = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-PERFORMANCE-MIB:CISCO-ENTITY-PERFORMANCE-MIB/CISCO-ENTITY-PERFORMANCE-MIB:cepEntityTable/CISCO-ENTITY-PERFORMANCE-MIB:cepEntityEntry[CISCO-ENTITY-PERFORMANCE-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.entphysicalindex is not None:
                    return True

                if self.cepentitylastreloadtime is not None:
                    return True

                if self.cepentitynumreloads is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_PERFORMANCE_MIB as meta
                return meta._meta_table['CISCOENTITYPERFORMANCEMIB.CepEntityTable.CepEntityEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-PERFORMANCE-MIB:CISCO-ENTITY-PERFORMANCE-MIB/CISCO-ENTITY-PERFORMANCE-MIB:cepEntityTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cepentityentry is not None:
                for child_ref in self.cepentityentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_PERFORMANCE_MIB as meta
            return meta._meta_table['CISCOENTITYPERFORMANCEMIB.CepEntityTable']['meta_info']


    class CepIntervalStatsTable(object):
        """
        This table contains specific performance statistics collected
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
        
        The support for 15\-minutes interval history is required for
        all the entities supporting performance data. However, the
        support for 1\-minute and 5\-minutes interval history for 
        entities are optional and at the descretion of the device
        supporting the performance monitoring.
        
        .. attribute:: cepintervalstatsentry
        
        	A conceptual row in the cepIntervalStatsTable. There is an entry in this table for each entity by a value of entPhysicalIndex, the supported performance history time interval by a value of cepHistInterval, the supported performance statistics by a value of cepConfigPerfType and the interval number by a value of cepIntervalNumber
        	**type**\: list of :py:class:`CepIntervalStatsEntry <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CISCOENTITYPERFORMANCEMIB.CepIntervalStatsTable.CepIntervalStatsEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2010-09-09'

        def __init__(self):
            self.parent = None
            self.cepintervalstatsentry = YList()
            self.cepintervalstatsentry.parent = self
            self.cepintervalstatsentry.name = 'cepintervalstatsentry'


        class CepIntervalStatsEntry(object):
            """
            A conceptual row in the cepIntervalStatsTable. There is
            an entry in this table for each entity by a value of
            entPhysicalIndex, the supported performance history time
            interval by a value of cepHistInterval, the supported
            performance statistics by a value of cepConfigPerfType
            and the interval number by a value of cepIntervalNumber.
            
            .. attribute:: cepconfigperftype
            
            	
            	**type**\: :py:class:`CiscoEntPerfType_Enum <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CiscoEntPerfType_Enum>`
            
            .. attribute:: cephistinterval
            
            	
            	**type**\: :py:class:`CiscoEntPerfHistInterval_Enum <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CiscoEntPerfHistInterval_Enum>`
            
            .. attribute:: cepintervalnumber
            
            	An interval number between 1 and 96, where 1 is the most recently completed interval and 96 is the least recently completed interval.  For example, if it is 15 minutes interval history, then the 96 is the interval number completed 23 hours and 45 minutes prior to interval 1
            	**type**\: int
            
            	**range:** 1..96
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cepintervalstatscreatetime
            
            	This object provides the time stamp at which the specific performance statistics gets created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cepintervalstatsmeasurement
            
            	This object provides the specific performance statistics of an entity over the specified interval. The range of this object can be identified by object 'cepIntervalStatsRange'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cepintervalstatsrange
            
            	This object provides the range information for the object 'cepIntervalStatsMeasurement'
            	**type**\: :py:class:`CiscoEntPerfRange_Enum <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CiscoEntPerfRange_Enum>`
            
            .. attribute:: cepintervalstatsvaliddata
            
            	This object indicates whether the performance statistics for this interval is valid. The value 'true' means the performance statistics is valid, otherwise the performance statistics is invalid for the interval
            	**type**\: bool
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2010-09-09'

            def __init__(self):
                self.parent = None
                self.cepconfigperftype = None
                self.cephistinterval = None
                self.cepintervalnumber = None
                self.entphysicalindex = None
                self.cepintervalstatscreatetime = None
                self.cepintervalstatsmeasurement = None
                self.cepintervalstatsrange = None
                self.cepintervalstatsvaliddata = None

            @property
            def _common_path(self):
                if self.cepconfigperftype is None:
                    raise YPYDataValidationError('Key property cepconfigperftype is None')
                if self.cephistinterval is None:
                    raise YPYDataValidationError('Key property cephistinterval is None')
                if self.cepintervalnumber is None:
                    raise YPYDataValidationError('Key property cepintervalnumber is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-PERFORMANCE-MIB:CISCO-ENTITY-PERFORMANCE-MIB/CISCO-ENTITY-PERFORMANCE-MIB:cepIntervalStatsTable/CISCO-ENTITY-PERFORMANCE-MIB:cepIntervalStatsEntry[CISCO-ENTITY-PERFORMANCE-MIB:cepConfigPerfType = ' + str(self.cepconfigperftype) + '][CISCO-ENTITY-PERFORMANCE-MIB:cepHistInterval = ' + str(self.cephistinterval) + '][CISCO-ENTITY-PERFORMANCE-MIB:cepIntervalNumber = ' + str(self.cepintervalnumber) + '][CISCO-ENTITY-PERFORMANCE-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cepconfigperftype is not None:
                    return True

                if self.cephistinterval is not None:
                    return True

                if self.cepintervalnumber is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.cepintervalstatscreatetime is not None:
                    return True

                if self.cepintervalstatsmeasurement is not None:
                    return True

                if self.cepintervalstatsrange is not None:
                    return True

                if self.cepintervalstatsvaliddata is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_PERFORMANCE_MIB as meta
                return meta._meta_table['CISCOENTITYPERFORMANCEMIB.CepIntervalStatsTable.CepIntervalStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-PERFORMANCE-MIB:CISCO-ENTITY-PERFORMANCE-MIB/CISCO-ENTITY-PERFORMANCE-MIB:cepIntervalStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cepintervalstatsentry is not None:
                for child_ref in self.cepintervalstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_PERFORMANCE_MIB as meta
            return meta._meta_table['CISCOENTITYPERFORMANCEMIB.CepIntervalStatsTable']['meta_info']


    class CepStatsTable(object):
        """
        This table maintains entity running performance, which
        are collected at various performance intervals.
        
        An agent creates a conceptual row to this table corresponding
        to a physical entity for each supported performance measurement 
        and a performance interval upon detection.
        
        The agent destroys a conceptual row from this table       
        corresponding to a physical entity for a specific 
        performance measurement and an interval upon removal 
        of the physical entity.
        
        .. attribute:: cepstatsentry
        
        	A conceptual row in the cepStatsTable. There is an entry in this table for each entity by a value of entPhysicalIndex, the supported performance time interval by a value of cepConfigInterval, and the supported performance type by a  value of cepConfigPerfType
        	**type**\: list of :py:class:`CepStatsEntry <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CISCOENTITYPERFORMANCEMIB.CepStatsTable.CepStatsEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2010-09-09'

        def __init__(self):
            self.parent = None
            self.cepstatsentry = YList()
            self.cepstatsentry.parent = self
            self.cepstatsentry.name = 'cepstatsentry'


        class CepStatsEntry(object):
            """
            A conceptual row in the cepStatsTable. There is an entry in
            this table for each entity by a value of entPhysicalIndex,
            the supported performance time interval by a value of
            cepConfigInterval, and the supported performance type by a 
            value of cepConfigPerfType.
            
            .. attribute:: cepconfiginterval
            
            	
            	**type**\: :py:class:`CiscoEntPerfInterval_Enum <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CiscoEntPerfInterval_Enum>`
            
            .. attribute:: cepconfigperftype
            
            	
            	**type**\: :py:class:`CiscoEntPerfType_Enum <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CiscoEntPerfType_Enum>`
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cepstatsalgorithm
            
            	This object provides the algorithm used to calculate the entity performance statistics over the specified interval
            	**type**\: :py:class:`CiscoEntPerfIntervalAlgo_Enum <ydk.models.entity.CISCO_ENTITY_PERFORMANCE_MIB.CiscoEntPerfIntervalAlgo_Enum>`
            
            .. attribute:: cepstatsmeasurement
            
            	This object provides a specific performance measurement of the entity over the specified interval. The range of this object can be identified by the object 'cepConfigPerfRange'
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2010-09-09'

            def __init__(self):
                self.parent = None
                self.cepconfiginterval = None
                self.cepconfigperftype = None
                self.entphysicalindex = None
                self.cepstatsalgorithm = None
                self.cepstatsmeasurement = None

            @property
            def _common_path(self):
                if self.cepconfiginterval is None:
                    raise YPYDataValidationError('Key property cepconfiginterval is None')
                if self.cepconfigperftype is None:
                    raise YPYDataValidationError('Key property cepconfigperftype is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-PERFORMANCE-MIB:CISCO-ENTITY-PERFORMANCE-MIB/CISCO-ENTITY-PERFORMANCE-MIB:cepStatsTable/CISCO-ENTITY-PERFORMANCE-MIB:cepStatsEntry[CISCO-ENTITY-PERFORMANCE-MIB:cepConfigInterval = ' + str(self.cepconfiginterval) + '][CISCO-ENTITY-PERFORMANCE-MIB:cepConfigPerfType = ' + str(self.cepconfigperftype) + '][CISCO-ENTITY-PERFORMANCE-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cepconfiginterval is not None:
                    return True

                if self.cepconfigperftype is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.cepstatsalgorithm is not None:
                    return True

                if self.cepstatsmeasurement is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_PERFORMANCE_MIB as meta
                return meta._meta_table['CISCOENTITYPERFORMANCEMIB.CepStatsTable.CepStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-PERFORMANCE-MIB:CISCO-ENTITY-PERFORMANCE-MIB/CISCO-ENTITY-PERFORMANCE-MIB:cepStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cepstatsentry is not None:
                for child_ref in self.cepstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_PERFORMANCE_MIB as meta
            return meta._meta_table['CISCOENTITYPERFORMANCEMIB.CepStatsTable']['meta_info']


    class CiscoEntityPerformanceMIBNotifObjects(object):
        """
        
        
        .. attribute:: cepthresholdnotifenabled
        
        	This object controls the entity performance measurement rising/falling threshold notification. When this object contains a value of 'true', then generation of entity rising/falling threshold notification is enabled. If this object contains a value of 'false', then generation of entity rising/falling threshold notification is disabled.  The generation of the rising/falling threshold depends on this global value as well as the object 'cepConfigThresholdNotifEnabled' present in cepConfigTable
        	**type**\: bool
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2010-09-09'

        def __init__(self):
            self.parent = None
            self.cepthresholdnotifenabled = None

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-PERFORMANCE-MIB:CISCO-ENTITY-PERFORMANCE-MIB/CISCO-ENTITY-PERFORMANCE-MIB:ciscoEntityPerformanceMIBNotifObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cepthresholdnotifenabled is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_PERFORMANCE_MIB as meta
            return meta._meta_table['CISCOENTITYPERFORMANCEMIB.CiscoEntityPerformanceMIBNotifObjects']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-ENTITY-PERFORMANCE-MIB:CISCO-ENTITY-PERFORMANCE-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cepconfigtable is not None and self.cepconfigtable._has_data():
            return True

        if self.cepconfigtable is not None and self.cepconfigtable.is_presence():
            return True

        if self.cepentityintervaltable is not None and self.cepentityintervaltable._has_data():
            return True

        if self.cepentityintervaltable is not None and self.cepentityintervaltable.is_presence():
            return True

        if self.cepentitytable is not None and self.cepentitytable._has_data():
            return True

        if self.cepentitytable is not None and self.cepentitytable.is_presence():
            return True

        if self.cepintervalstatstable is not None and self.cepintervalstatstable._has_data():
            return True

        if self.cepintervalstatstable is not None and self.cepintervalstatstable.is_presence():
            return True

        if self.cepstatstable is not None and self.cepstatstable._has_data():
            return True

        if self.cepstatstable is not None and self.cepstatstable.is_presence():
            return True

        if self.ciscoentityperformancemibnotifobjects is not None and self.ciscoentityperformancemibnotifobjects._has_data():
            return True

        if self.ciscoentityperformancemibnotifobjects is not None and self.ciscoentityperformancemibnotifobjects.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_PERFORMANCE_MIB as meta
        return meta._meta_table['CISCOENTITYPERFORMANCEMIB']['meta_info']


