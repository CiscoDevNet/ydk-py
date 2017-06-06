""" CISCO_ENTITY_QFP_MIB 

This MIB module defines managed objects that facilitate the
management of Quantum Flow Processors (QFP), which are listed
in the ENTITY\-MIB (RFC 4133) entPhysicalTable as an
entPhysicalClass of 'cpu'.

The Quantum Flow Processors (QFP) technology is an architecture
family developed by Cisco, which has fully integrated and
programmable networking chip set that controls different
functions of a system such as packet forwarding.

This module contains objects to monitor various QFP
statistics such as system, utilization, memory, etc.

The utilization statistics can be used for future capacity
planning. The calculation of this statistics may vary by
devices which host QFPs, hence the user must refer to the
specific device document of interest for the exact method
of calculation. The utilization statistics have the following
terminology.

o Input \- Communication channel where packets arrive on the
          QFP.

o Output \- Communication channel where packets leave the QFP.

o Priority \- A classification applied to packets indicating
             they should be treated with greater urgency.

o Non\-Priority \- A classification applied to packets indicating
                 they should be treated with lesser urgency.

o Processing Load \- The percentage of time over some interval
                    that the QFP has spent forwarding packets,
                    relative to the total time spent both 
                    forwarding packets and being idle.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CiscoqfpmemoryresourceEnum(Enum):
    """
    CiscoqfpmemoryresourceEnum

    An enumerated integer\-value describing various memory resources

    used by the QFP.

    dram (1) \- Dynamic Random Access Memory (DRAM) memory resource

    .. data:: dram = 1

    """

    dram = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
        return meta._meta_table['CiscoqfpmemoryresourceEnum']


class CiscoqfptimeintervalEnum(Enum):
    """
    CiscoqfptimeintervalEnum

    An enumerated integer\-value describing the available interval

    values for which the periodic statistics are to be collected.

    fiveSeconds (1)   \- Interval to collect last 5 seconds       

                        statistics

    oneMinute(2)      \- Interval to collect last 1 minute

                        statistics

    fiveMinutes(3)    \- Interval to collect last 5 minutes       

                        statistics

    sixtyMinutes(4)   \- Interval to collect last 60 minutes       

                        statistics

    .. data:: fiveSeconds = 1

    .. data:: oneMinute = 2

    .. data:: fiveMinutes = 3

    .. data:: sixtyMinutes = 4

    """

    fiveSeconds = 1

    oneMinute = 2

    fiveMinutes = 3

    sixtyMinutes = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
        return meta._meta_table['CiscoqfptimeintervalEnum']



class CiscoEntityQfpMib(object):
    """
    
    
    .. attribute:: ceqfpmemoryresourcetable
    
    	This table maintains the memory resources statistics for each QFP physical entity.  An agent creates a conceptual row to this table corresponding to a QFP physical entity and its supported memory resource type upon detection of a physical entity supporting the memory  resource statistics for a memory resource type.  An agent destroys a conceptual row from this table        corresponding to a QFP physical entity and its supported memory resource type upon removal of the QFP host physical entity or it does not receive memory resource statistics update for a certain time period. The time period to wait before deleting an entry from this table would be the discretion of the supporting device
    	**type**\:   :py:class:`Ceqfpmemoryresourcetable <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfpmemoryresourcetable>`
    
    .. attribute:: ceqfpsystemtable
    
    	This table maintains the QFP system information for each QFP physical entity.  An agent creates a conceptual row to this table corresponding to a QFP physical entity upon detection of a physical entity supporting the QFP system information.  An agent destroys a conceptual row from this table        corresponding to a QFP physical entity upon removal of the QFP host physical entity
    	**type**\:   :py:class:`Ceqfpsystemtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfpsystemtable>`
    
    .. attribute:: ceqfpthroughputtable
    
    	This table maintains the throughput information for each QFP physical entity.          An agent creates a conceptual row to this table corresponding to a QFP physical entity upon detection of a physical entity supporting the QFP throughput information.          An agent destroys a conceptual row from this table       corresponding to a QFP physical entity upon removal of the QFP host physical entity
    	**type**\:   :py:class:`Ceqfpthroughputtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfpthroughputtable>`
    
    .. attribute:: ceqfputilizationtable
    
    	This table maintains the utilization statistics collected by each QFP physical entity at various time interval such as last 5 seconds, 1 minute, etc.  An agent creates a conceptual row to this table corresponding to a QFP physical entity for a time interval upon detection of a physical entity supporting the utilization statistics for a time interval.  The agent destroys a conceptual row from this table        corresponding to a QFP physical entity for a time interval upon removal of the QFP host physical entity or it does not receive the utilization statistics update for a certain time period. The time period to wait before deleting an entry from this table would be the discretion of the supporting device
    	**type**\:   :py:class:`Ceqfputilizationtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfputilizationtable>`
    
    .. attribute:: ciscoentityqfp
    
    	
    	**type**\:   :py:class:`Ciscoentityqfp <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ciscoentityqfp>`
    
    .. attribute:: ciscoentityqfpnotif
    
    	
    	**type**\:   :py:class:`Ciscoentityqfpnotif <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ciscoentityqfpnotif>`
    
    

    """

    _prefix = 'CISCO-ENTITY-QFP-MIB'
    _revision = '2014-06-18'

    def __init__(self):
        self.ceqfpmemoryresourcetable = CiscoEntityQfpMib.Ceqfpmemoryresourcetable()
        self.ceqfpmemoryresourcetable.parent = self
        self.ceqfpsystemtable = CiscoEntityQfpMib.Ceqfpsystemtable()
        self.ceqfpsystemtable.parent = self
        self.ceqfpthroughputtable = CiscoEntityQfpMib.Ceqfpthroughputtable()
        self.ceqfpthroughputtable.parent = self
        self.ceqfputilizationtable = CiscoEntityQfpMib.Ceqfputilizationtable()
        self.ceqfputilizationtable.parent = self
        self.ciscoentityqfp = CiscoEntityQfpMib.Ciscoentityqfp()
        self.ciscoentityqfp.parent = self
        self.ciscoentityqfpnotif = CiscoEntityQfpMib.Ciscoentityqfpnotif()
        self.ciscoentityqfpnotif.parent = self


    class Ciscoentityqfp(object):
        """
        
        
        .. attribute:: ceqfpfiveminutesutilalgo
        
        	This objects represents the method used to calculate 5 Minutes interval utilization data. The enumerated values are described below.  unknown    (1) \- The calculation method is unknown fiveSecSMA (2) \- The value is calculated using Simple Moving                    Average of last 60 five seconds utilization                  data
        	**type**\:   :py:class:`CeqfpfiveminutesutilalgoEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ciscoentityqfp.CeqfpfiveminutesutilalgoEnum>`
        
        .. attribute:: ceqfpfivesecondutilalgo
        
        	This objects represents the method used to calculate 5 Second interval utilization data. The enumerated values are described below.  unknown       (1) \- The calculation method is unknown fiveSecSample (2) \- The value is calculated based on the last                     5 second sampling period of utilization                     data
        	**type**\:   :py:class:`CeqfpfivesecondutilalgoEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ciscoentityqfp.CeqfpfivesecondutilalgoEnum>`
        
        .. attribute:: ceqfponeminuteutilalgo
        
        	This objects represents the method used to calculate 1 Minute interval utilization data. The enumerated values are described below.  unknown    (1) \- The calculation method is unknown fiveSecSMA (2) \- The value is calculated using Simple Moving                    Average of last 12 five seconds utilization                  data
        	**type**\:   :py:class:`CeqfponeminuteutilalgoEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ciscoentityqfp.CeqfponeminuteutilalgoEnum>`
        
        .. attribute:: ceqfpsixtyminutesutilalgo
        
        	This objects represents the method used to calculate 60 Minutes interval utilization data. The enumerated values are described below.  unknown    (1) \- The calculation method is unknown fiveSecSMA (1) \- The value is calculated using Simple Moving                    Average of last 720 five seconds utilization                  data
        	**type**\:   :py:class:`CeqfpsixtyminutesutilalgoEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ciscoentityqfp.CeqfpsixtyminutesutilalgoEnum>`
        
        

        """

        _prefix = 'CISCO-ENTITY-QFP-MIB'
        _revision = '2014-06-18'

        def __init__(self):
            self.parent = None
            self.ceqfpfiveminutesutilalgo = None
            self.ceqfpfivesecondutilalgo = None
            self.ceqfponeminuteutilalgo = None
            self.ceqfpsixtyminutesutilalgo = None

        class CeqfpfiveminutesutilalgoEnum(Enum):
            """
            CeqfpfiveminutesutilalgoEnum

            This objects represents the method used to calculate 5 Minutes

            interval utilization data. The enumerated values are described

            below.

            unknown    (1) \- The calculation method is unknown

            fiveSecSMA (2) \- The value is calculated using Simple Moving  

                             Average of last 60 five seconds utilization

                             data.

            .. data:: unknown = 1

            .. data:: fiveSecSMA = 2

            """

            unknown = 1

            fiveSecSMA = 2


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
                return meta._meta_table['CiscoEntityQfpMib.Ciscoentityqfp.CeqfpfiveminutesutilalgoEnum']


        class CeqfpfivesecondutilalgoEnum(Enum):
            """
            CeqfpfivesecondutilalgoEnum

            This objects represents the method used to calculate 5 Second

            interval utilization data. The enumerated values are described

            below.

            unknown       (1) \- The calculation method is unknown

            fiveSecSample (2) \- The value is calculated based on the last

                                5 second sampling period of utilization

                                data.

            .. data:: unknown = 1

            .. data:: fiveSecSample = 2

            """

            unknown = 1

            fiveSecSample = 2


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
                return meta._meta_table['CiscoEntityQfpMib.Ciscoentityqfp.CeqfpfivesecondutilalgoEnum']


        class CeqfponeminuteutilalgoEnum(Enum):
            """
            CeqfponeminuteutilalgoEnum

            This objects represents the method used to calculate 1 Minute

            interval utilization data. The enumerated values are described

            below.

            unknown    (1) \- The calculation method is unknown

            fiveSecSMA (2) \- The value is calculated using Simple Moving  

                             Average of last 12 five seconds utilization

                             data.

            .. data:: unknown = 1

            .. data:: fiveSecSMA = 2

            """

            unknown = 1

            fiveSecSMA = 2


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
                return meta._meta_table['CiscoEntityQfpMib.Ciscoentityqfp.CeqfponeminuteutilalgoEnum']


        class CeqfpsixtyminutesutilalgoEnum(Enum):
            """
            CeqfpsixtyminutesutilalgoEnum

            This objects represents the method used to calculate 60 Minutes

            interval utilization data. The enumerated values are described

            below.

            unknown    (1) \- The calculation method is unknown

            fiveSecSMA (1) \- The value is calculated using Simple Moving  

                             Average of last 720 five seconds utilization

                             data.

            .. data:: unknown = 1

            .. data:: fiveSecSMA = 2

            """

            unknown = 1

            fiveSecSMA = 2


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
                return meta._meta_table['CiscoEntityQfpMib.Ciscoentityqfp.CeqfpsixtyminutesutilalgoEnum']


        @property
        def _common_path(self):

            return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ciscoEntityQfp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ceqfpfiveminutesutilalgo is not None:
                return True

            if self.ceqfpfivesecondutilalgo is not None:
                return True

            if self.ceqfponeminuteutilalgo is not None:
                return True

            if self.ceqfpsixtyminutesutilalgo is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
            return meta._meta_table['CiscoEntityQfpMib.Ciscoentityqfp']['meta_info']


    class Ciscoentityqfpnotif(object):
        """
        
        
        .. attribute:: ceqfpmemoryresthreshnotifenabled
        
        	This object controls memory resource rising and falling threshold notification.  When this object contains a value 'true', then generation of memory resource threshold notification is enabled. If this object contains a value 'false', then generation of memory resource threshold notification is disabled
        	**type**\:  bool
        
        .. attribute:: ceqfpthroughputnotifenabled
        
        	This object controls throughput rate notification.  When this object contains a value 'true', then generation of ceqfpThroughputNotif is enabled. If this object contains a value 'false', then generation of ceqfpThroughputNotif is disabled
        	**type**\:  int
        
        	**range:** 0..2
        
        

        """

        _prefix = 'CISCO-ENTITY-QFP-MIB'
        _revision = '2014-06-18'

        def __init__(self):
            self.parent = None
            self.ceqfpmemoryresthreshnotifenabled = None
            self.ceqfpthroughputnotifenabled = None

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ciscoEntityQfpNotif'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ceqfpmemoryresthreshnotifenabled is not None:
                return True

            if self.ceqfpthroughputnotifenabled is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
            return meta._meta_table['CiscoEntityQfpMib.Ciscoentityqfpnotif']['meta_info']


    class Ceqfpsystemtable(object):
        """
        This table maintains the QFP system information for each QFP
        physical entity.
        
        An agent creates a conceptual row to this table corresponding
        to a QFP physical entity upon detection of a physical entity
        supporting the QFP system information.
        
        An agent destroys a conceptual row from this table       
        corresponding to a QFP physical entity upon removal
        of the QFP host physical entity.
        
        .. attribute:: ceqfpsystementry
        
        	A conceptual row in the ceqfpSystemTable. There is an entry in this table for each QFP entity, as defined by a value of entPhysicalIndex
        	**type**\: list of    :py:class:`Ceqfpsystementry <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-QFP-MIB'
        _revision = '2014-06-18'

        def __init__(self):
            self.parent = None
            self.ceqfpsystementry = YList()
            self.ceqfpsystementry.parent = self
            self.ceqfpsystementry.name = 'ceqfpsystementry'


        class Ceqfpsystementry(object):
            """
            A conceptual row in the ceqfpSystemTable. There is an entry
            in this table for each QFP entity, as defined by a value of
            entPhysicalIndex.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceqfpnumbersystemloads
            
            	This object represents the number of times the QFP is loaded, since the QFP host is up
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceqfpsystemlastloadtime
            
            	This object represents the QFP last load time
            	**type**\:  str
            
            .. attribute:: ceqfpsystemstate
            
            	This object represents the current QFP state. The enumerated values are described below.  unknown (1)    \- The state of the QFP is unknown reset (2)      \- The QFP is reset init (3)       \- The QFP is being initialized active (4)     \- The QFP is active in a system with redundant                  QFP activeSolo (5) \- The QFP is active and there is no redundant                  QFP in the system standby (6)    \- The QFP is standby in a redundant system. hotStandby (7) \- The QFP is standby and synchronized with                  active, so that a switchover in this state                  will preserve state of the active. Stateful                   datapath features are synchronized between the                  active QFP and standby QFP
            	**type**\:   :py:class:`CeqfpsystemstateEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry.CeqfpsystemstateEnum>`
            
            .. attribute:: ceqfpsystemtrafficdirection
            
            	This object represents the traffic direction that this QFP is assigned to process. The enumerated values are described below.  none (1)    \- The QFP is not assigned to processes any traffic               yet ingress (2) \- The QFP processes inbound traffic egress (3)  \- The QFP processes outbound traffic both (4)    \- The QFP processes both inbound and outbound               traffic
            	**type**\:   :py:class:`CeqfpsystemtrafficdirectionEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry.CeqfpsystemtrafficdirectionEnum>`
            
            

            """

            _prefix = 'CISCO-ENTITY-QFP-MIB'
            _revision = '2014-06-18'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.ceqfpnumbersystemloads = None
                self.ceqfpsystemlastloadtime = None
                self.ceqfpsystemstate = None
                self.ceqfpsystemtrafficdirection = None

            class CeqfpsystemstateEnum(Enum):
                """
                CeqfpsystemstateEnum

                This object represents the current QFP state. The enumerated

                values are described below.

                unknown (1)    \- The state of the QFP is unknown

                reset (2)      \- The QFP is reset

                init (3)       \- The QFP is being initialized

                active (4)     \- The QFP is active in a system with redundant

                                 QFP

                activeSolo (5) \- The QFP is active and there is no redundant

                                 QFP in the system

                standby (6)    \- The QFP is standby in a redundant system.

                hotStandby (7) \- The QFP is standby and synchronized with

                                 active, so that a switchover in this state

                                 will preserve state of the active. Stateful 

                                 datapath features are synchronized between the

                                 active QFP and standby QFP

                .. data:: unknown = 1

                .. data:: reset = 2

                .. data:: init = 3

                .. data:: active = 4

                .. data:: activeSolo = 5

                .. data:: standby = 6

                .. data:: hotStandby = 7

                """

                unknown = 1

                reset = 2

                init = 3

                active = 4

                activeSolo = 5

                standby = 6

                hotStandby = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
                    return meta._meta_table['CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry.CeqfpsystemstateEnum']


            class CeqfpsystemtrafficdirectionEnum(Enum):
                """
                CeqfpsystemtrafficdirectionEnum

                This object represents the traffic direction that this QFP is

                assigned to process. The enumerated values are described below.

                none (1)    \- The QFP is not assigned to processes any traffic

                              yet

                ingress (2) \- The QFP processes inbound traffic

                egress (3)  \- The QFP processes outbound traffic

                both (4)    \- The QFP processes both inbound and outbound

                              traffic

                .. data:: none = 1

                .. data:: ingress = 2

                .. data:: egress = 3

                .. data:: both = 4

                """

                none = 1

                ingress = 2

                egress = 3

                both = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
                    return meta._meta_table['CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry.CeqfpsystemtrafficdirectionEnum']


            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ceqfpSystemTable/CISCO-ENTITY-QFP-MIB:ceqfpSystemEntry[CISCO-ENTITY-QFP-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.ceqfpnumbersystemloads is not None:
                    return True

                if self.ceqfpsystemlastloadtime is not None:
                    return True

                if self.ceqfpsystemstate is not None:
                    return True

                if self.ceqfpsystemtrafficdirection is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
                return meta._meta_table['CiscoEntityQfpMib.Ceqfpsystemtable.Ceqfpsystementry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ceqfpSystemTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ceqfpsystementry is not None:
                for child_ref in self.ceqfpsystementry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
            return meta._meta_table['CiscoEntityQfpMib.Ceqfpsystemtable']['meta_info']


    class Ceqfputilizationtable(object):
        """
        This table maintains the utilization statistics collected
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
        
        .. attribute:: ceqfputilizationentry
        
        	A conceptual row in the ceqfpUtilizationTable. There is an entry in this table for each QFP entity by a value of entPhysicalIndex and the supported time interval by a value  of ceqfpUtilTimeInterval.  The method of utilization data calculation for each interval period can be identified through the respective interval scalar objects. For example the utilizaiton data calculation method for 'fiveSecond' interval can be identified by ceqfpFiveSecondUtilAlgo
        	**type**\: list of    :py:class:`Ceqfputilizationentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfputilizationtable.Ceqfputilizationentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-QFP-MIB'
        _revision = '2014-06-18'

        def __init__(self):
            self.parent = None
            self.ceqfputilizationentry = YList()
            self.ceqfputilizationentry.parent = self
            self.ceqfputilizationentry.name = 'ceqfputilizationentry'


        class Ceqfputilizationentry(object):
            """
            A conceptual row in the ceqfpUtilizationTable. There is
            an entry in this table for each QFP entity by a value of
            entPhysicalIndex and the supported time interval by a value 
            of ceqfpUtilTimeInterval.
            
            The method of utilization data calculation for each interval
            period can be identified through the respective interval
            scalar objects. For example the utilizaiton data calculation
            method for 'fiveSecond' interval can be identified by
            ceqfpFiveSecondUtilAlgo.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceqfputiltimeinterval  <key>
            
            	This object identifies the time interval for which the utilization statistics being collected. The interval  values can be 5 second, 1 minute, etc. as specified in  the CiscoQfpTimeInterval
            	**type**\:   :py:class:`CiscoqfptimeintervalEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoqfptimeintervalEnum>`
            
            .. attribute:: ceqfputilinputnonprioritybitrate
            
            	This object represents the QFP input channel non\-priority bit rate during this interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits per second
            
            .. attribute:: ceqfputilinputnonprioritypktrate
            
            	This object represents the QFP input channel non\-priority packet rate during this interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets per second
            
            .. attribute:: ceqfputilinputprioritybitrate
            
            	This object represents the QFP input channel priority bit rate during this interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits per second
            
            .. attribute:: ceqfputilinputprioritypktrate
            
            	This object represents the QFP input channel priority packet rate during this interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets per second
            
            .. attribute:: ceqfputilinputtotalbitrate
            
            	This object represents the QFP input channel total bit rate during this interval, which includes both priority and non\-priority input bit rate
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits per second
            
            .. attribute:: ceqfputilinputtotalpktrate
            
            	This object represents the QFP input channel total packet rate during this interval, which includes both priority and non\-priority input packet rate
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets per second
            
            .. attribute:: ceqfputiloutputnonprioritybitrate
            
            	This object represents the QFP output channel non\-priority bit rate during this interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits per second
            
            .. attribute:: ceqfputiloutputnonprioritypktrate
            
            	This object represents the QFP output channel non\-priority packet rate during this interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets per second
            
            .. attribute:: ceqfputiloutputprioritybitrate
            
            	This object represents the QFP output channel priority bit rate during this interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits per second
            
            .. attribute:: ceqfputiloutputprioritypktrate
            
            	This object represents the QFP output channel priority packet rate during this interval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets per second
            
            .. attribute:: ceqfputiloutputtotalbitrate
            
            	This object represents the QFP output channel total bit rate during this interval, which includes both priority and non\-priority bit rate
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits per second
            
            .. attribute:: ceqfputiloutputtotalpktrate
            
            	This object represents the QFP output channel total packet rate during this interval, which includes both priority and non\-priority output packet rate
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets per second
            
            .. attribute:: ceqfputilprocessingload
            
            	This object represents the QFP processing load during this interval
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            

            """

            _prefix = 'CISCO-ENTITY-QFP-MIB'
            _revision = '2014-06-18'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.ceqfputiltimeinterval = None
                self.ceqfputilinputnonprioritybitrate = None
                self.ceqfputilinputnonprioritypktrate = None
                self.ceqfputilinputprioritybitrate = None
                self.ceqfputilinputprioritypktrate = None
                self.ceqfputilinputtotalbitrate = None
                self.ceqfputilinputtotalpktrate = None
                self.ceqfputiloutputnonprioritybitrate = None
                self.ceqfputiloutputnonprioritypktrate = None
                self.ceqfputiloutputprioritybitrate = None
                self.ceqfputiloutputprioritypktrate = None
                self.ceqfputiloutputtotalbitrate = None
                self.ceqfputiloutputtotalpktrate = None
                self.ceqfputilprocessingload = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')
                if self.ceqfputiltimeinterval is None:
                    raise YPYModelError('Key property ceqfputiltimeinterval is None')

                return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ceqfpUtilizationTable/CISCO-ENTITY-QFP-MIB:ceqfpUtilizationEntry[CISCO-ENTITY-QFP-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + '][CISCO-ENTITY-QFP-MIB:ceqfpUtilTimeInterval = ' + str(self.ceqfputiltimeinterval) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.ceqfputiltimeinterval is not None:
                    return True

                if self.ceqfputilinputnonprioritybitrate is not None:
                    return True

                if self.ceqfputilinputnonprioritypktrate is not None:
                    return True

                if self.ceqfputilinputprioritybitrate is not None:
                    return True

                if self.ceqfputilinputprioritypktrate is not None:
                    return True

                if self.ceqfputilinputtotalbitrate is not None:
                    return True

                if self.ceqfputilinputtotalpktrate is not None:
                    return True

                if self.ceqfputiloutputnonprioritybitrate is not None:
                    return True

                if self.ceqfputiloutputnonprioritypktrate is not None:
                    return True

                if self.ceqfputiloutputprioritybitrate is not None:
                    return True

                if self.ceqfputiloutputprioritypktrate is not None:
                    return True

                if self.ceqfputiloutputtotalbitrate is not None:
                    return True

                if self.ceqfputiloutputtotalpktrate is not None:
                    return True

                if self.ceqfputilprocessingload is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
                return meta._meta_table['CiscoEntityQfpMib.Ceqfputilizationtable.Ceqfputilizationentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ceqfpUtilizationTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ceqfputilizationentry is not None:
                for child_ref in self.ceqfputilizationentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
            return meta._meta_table['CiscoEntityQfpMib.Ceqfputilizationtable']['meta_info']


    class Ceqfpmemoryresourcetable(object):
        """
        This table maintains the memory resources statistics for
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
        
        .. attribute:: ceqfpmemoryresourceentry
        
        	A conceptual row in the ceqfpMemoryResourceTable. There is an entry in this table for each QFP entity by a value  of entPhysicalIndex and the supported memory resource type  by a value of ceqfpMemoryResType
        	**type**\: list of    :py:class:`Ceqfpmemoryresourceentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfpmemoryresourcetable.Ceqfpmemoryresourceentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-QFP-MIB'
        _revision = '2014-06-18'

        def __init__(self):
            self.parent = None
            self.ceqfpmemoryresourceentry = YList()
            self.ceqfpmemoryresourceentry.parent = self
            self.ceqfpmemoryresourceentry.name = 'ceqfpmemoryresourceentry'


        class Ceqfpmemoryresourceentry(object):
            """
            A conceptual row in the ceqfpMemoryResourceTable. There
            is an entry in this table for each QFP entity by a value 
            of entPhysicalIndex and the supported memory resource type 
            by a value of ceqfpMemoryResType.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceqfpmemoryrestype  <key>
            
            	This object indicates the type of the memory resource used by the QFP. This object is one of the indices to uniquely identify the QFP memory resource type
            	**type**\:   :py:class:`CiscoqfpmemoryresourceEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoqfpmemoryresourceEnum>`
            
            .. attribute:: ceqfpmemoryhcresfree
            
            	This object is a 64\-bit version of ceqfpMemoryResFree
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryhcresinuse
            
            	This object is a 64\-bit version of ceqfpMemoryInRes
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryhcreslowfreewatermark
            
            	This object is a 64\-bit version of ceqfpMemoryResLowFreeWatermark
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryhcrestotal
            
            	This object is a 64\-bit version of ceqfpMemoryResTotal
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryresfallingthreshold
            
            	This object represents the falling threshold value for this memory resource. A value of zero means that the falling threshold is not supported for this memory resource.  The value of this object can not be set to higher than or equal to ceqfpMemoryResRisingThreshold.  A falling (ceqfpMemoryResRisingThreshNotif) notification  will be generated, whenever the memory resource usage (ceqfpMemoryHCResInUse) is equal to or lesser than this value.  After a falling notification is generated, another  such notification will not be generated until the  ceqfpMemoryResInUse rises above this value and reaches  the ceqfpMemoryResRisingThreshold
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            .. attribute:: ceqfpmemoryresfree
            
            	This object represents the memory which is currently free on this memory resource
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryresfreeovrflw
            
            	This object represents the upper 32\-bit of ceqfpMemoryResFree. This object needs to be supported only when the value of ceqfpMemoryResFree exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryresinuse
            
            	This object represents the memory which is currently under use on this memory resource
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryresinuseovrflw
            
            	This object represents the upper 32\-bit of ceqfpMemoryResInUse. This object needs to be supported only when the value of ceqfpMemoryResInUse exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryreslowfreewatermark
            
            	This object represents lowest free water mark on this memory resource
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryreslowfreewatermarkovrflw
            
            	This object represents the upper 32\-bit of ceqfpMemoryResLowFreeWatermark. This object needs to be supported only when the value of ceqfpMemoryResLowFreeWatermark exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryresrisingthreshold
            
            	This object represents the rising threshold value for this memory resource. A value of zero means that the rising threshold is not supported for this memory resource.  The value of this object can not be set to lower than or equal to ceqfpMemoryResFallingThreshold.  A rising (ceqfpMemoryResRisingThreshNotif) notification will be generated, whenever the memory resource usage (ceqfpMemoryHCResInUse) is equal to or greater than this value.  After a rising notification is generated, another such  notification will not be generated until the  ceqfpMemoryResInUse falls below this value and reaches  the ceqfpMemoryResFallingThreshold
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            .. attribute:: ceqfpmemoryrestotal
            
            	This object represents total memory available on this memory resource
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo bytes
            
            .. attribute:: ceqfpmemoryrestotalovrflw
            
            	This object represents the upper 32\-bit of ceqfpMemoryResTotal. This object needs to be supported only when the value of ceqfpMemoryResTotal exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo bytes
            
            

            """

            _prefix = 'CISCO-ENTITY-QFP-MIB'
            _revision = '2014-06-18'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.ceqfpmemoryrestype = None
                self.ceqfpmemoryhcresfree = None
                self.ceqfpmemoryhcresinuse = None
                self.ceqfpmemoryhcreslowfreewatermark = None
                self.ceqfpmemoryhcrestotal = None
                self.ceqfpmemoryresfallingthreshold = None
                self.ceqfpmemoryresfree = None
                self.ceqfpmemoryresfreeovrflw = None
                self.ceqfpmemoryresinuse = None
                self.ceqfpmemoryresinuseovrflw = None
                self.ceqfpmemoryreslowfreewatermark = None
                self.ceqfpmemoryreslowfreewatermarkovrflw = None
                self.ceqfpmemoryresrisingthreshold = None
                self.ceqfpmemoryrestotal = None
                self.ceqfpmemoryrestotalovrflw = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')
                if self.ceqfpmemoryrestype is None:
                    raise YPYModelError('Key property ceqfpmemoryrestype is None')

                return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ceqfpMemoryResourceTable/CISCO-ENTITY-QFP-MIB:ceqfpMemoryResourceEntry[CISCO-ENTITY-QFP-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + '][CISCO-ENTITY-QFP-MIB:ceqfpMemoryResType = ' + str(self.ceqfpmemoryrestype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.ceqfpmemoryrestype is not None:
                    return True

                if self.ceqfpmemoryhcresfree is not None:
                    return True

                if self.ceqfpmemoryhcresinuse is not None:
                    return True

                if self.ceqfpmemoryhcreslowfreewatermark is not None:
                    return True

                if self.ceqfpmemoryhcrestotal is not None:
                    return True

                if self.ceqfpmemoryresfallingthreshold is not None:
                    return True

                if self.ceqfpmemoryresfree is not None:
                    return True

                if self.ceqfpmemoryresfreeovrflw is not None:
                    return True

                if self.ceqfpmemoryresinuse is not None:
                    return True

                if self.ceqfpmemoryresinuseovrflw is not None:
                    return True

                if self.ceqfpmemoryreslowfreewatermark is not None:
                    return True

                if self.ceqfpmemoryreslowfreewatermarkovrflw is not None:
                    return True

                if self.ceqfpmemoryresrisingthreshold is not None:
                    return True

                if self.ceqfpmemoryrestotal is not None:
                    return True

                if self.ceqfpmemoryrestotalovrflw is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
                return meta._meta_table['CiscoEntityQfpMib.Ceqfpmemoryresourcetable.Ceqfpmemoryresourceentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ceqfpMemoryResourceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ceqfpmemoryresourceentry is not None:
                for child_ref in self.ceqfpmemoryresourceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
            return meta._meta_table['CiscoEntityQfpMib.Ceqfpmemoryresourcetable']['meta_info']


    class Ceqfpthroughputtable(object):
        """
        This table maintains the throughput information for each
        QFP physical entity.
        
                An agent creates a conceptual row to this table
        corresponding to a QFP physical entity upon detection of a
        physical entity supporting the QFP throughput information.
        
                An agent destroys a conceptual row from this table     
        
        corresponding to a QFP physical entity upon removal of the QFP
        host physical entity.
        
        .. attribute:: ceqfpthroughputentry
        
        	A conceptual row in the ceqfpThroughputTable. There is an entry in this table for each QFP entity, as defined by a value of entPhysicalIndex
        	**type**\: list of    :py:class:`Ceqfpthroughputentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfpthroughputtable.Ceqfpthroughputentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-QFP-MIB'
        _revision = '2014-06-18'

        def __init__(self):
            self.parent = None
            self.ceqfpthroughputentry = YList()
            self.ceqfpthroughputentry.parent = self
            self.ceqfpthroughputentry.name = 'ceqfpthroughputentry'


        class Ceqfpthroughputentry(object):
            """
            A conceptual row in the ceqfpThroughputTable. There is an entry
            in this table for each QFP entity, as defined by a value of
            entPhysicalIndex.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceqfpthroughputavgrate
            
            	The object represents the average throughput rate in the interval ceqfpThroughputInterval
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits per second
            
            .. attribute:: ceqfpthroughputinterval
            
            	The object represents the configured time interval at which the ceqfpThroughputLevel is checked
            	**type**\:  int
            
            	**range:** 10..86400
            
            	**units**\: seconds
            
            .. attribute:: ceqfpthroughputlevel
            
            	This object represents the current throughput level for installed throughput license.                  normal  (1) \- Throughput usage is normal                 warning (2) \- Throughput usage has crossed the                               configured threshold limit                 exceed  (3) \- Throughput usage has exceeded the                               total licensed bandwidth
            	**type**\:   :py:class:`CeqfpthroughputlevelEnum <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoEntityQfpMib.Ceqfpthroughputtable.Ceqfpthroughputentry.CeqfpthroughputlevelEnum>`
            
            .. attribute:: ceqfpthroughputlicensedbw
            
            	This object represents the bandwidth for installed throughput license
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bits per second
            
            .. attribute:: ceqfpthroughputthreshold
            
            	The object represents the configured throughput threshold
            	**type**\:  int
            
            	**range:** 75..95
            
            	**units**\: percent
            
            

            """

            _prefix = 'CISCO-ENTITY-QFP-MIB'
            _revision = '2014-06-18'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.ceqfpthroughputavgrate = None
                self.ceqfpthroughputinterval = None
                self.ceqfpthroughputlevel = None
                self.ceqfpthroughputlicensedbw = None
                self.ceqfpthroughputthreshold = None

            class CeqfpthroughputlevelEnum(Enum):
                """
                CeqfpthroughputlevelEnum

                This object represents the current throughput level for

                installed throughput license.

                                normal  (1) \- Throughput usage is normal

                                warning (2) \- Throughput usage has crossed the

                                              configured threshold limit

                                exceed  (3) \- Throughput usage has exceeded the

                                              total licensed bandwidth

                .. data:: normal = 1

                .. data:: warning = 2

                .. data:: exceed = 3

                """

                normal = 1

                warning = 2

                exceed = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
                    return meta._meta_table['CiscoEntityQfpMib.Ceqfpthroughputtable.Ceqfpthroughputentry.CeqfpthroughputlevelEnum']


            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ceqfpThroughputTable/CISCO-ENTITY-QFP-MIB:ceqfpThroughputEntry[CISCO-ENTITY-QFP-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.ceqfpthroughputavgrate is not None:
                    return True

                if self.ceqfpthroughputinterval is not None:
                    return True

                if self.ceqfpthroughputlevel is not None:
                    return True

                if self.ceqfpthroughputlicensedbw is not None:
                    return True

                if self.ceqfpthroughputthreshold is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
                return meta._meta_table['CiscoEntityQfpMib.Ceqfpthroughputtable.Ceqfpthroughputentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ceqfpThroughputTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ceqfpthroughputentry is not None:
                for child_ref in self.ceqfpthroughputentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
            return meta._meta_table['CiscoEntityQfpMib.Ceqfpthroughputtable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.ceqfpmemoryresourcetable is not None and self.ceqfpmemoryresourcetable._has_data():
            return True

        if self.ceqfpsystemtable is not None and self.ceqfpsystemtable._has_data():
            return True

        if self.ceqfpthroughputtable is not None and self.ceqfpthroughputtable._has_data():
            return True

        if self.ceqfputilizationtable is not None and self.ceqfputilizationtable._has_data():
            return True

        if self.ciscoentityqfp is not None and self.ciscoentityqfp._has_data():
            return True

        if self.ciscoentityqfpnotif is not None and self.ciscoentityqfpnotif._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENTITY_QFP_MIB as meta
        return meta._meta_table['CiscoEntityQfpMib']['meta_info']


