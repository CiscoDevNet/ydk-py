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

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class CiscoQfpMemoryResource_Enum(Enum):
    """
    CiscoQfpMemoryResource_Enum

    An enumerated integer\-value describing various memory resources
    used by the QFP.
    
    dram (1) \- Dynamic Random Access Memory (DRAM) memory resource

    """

    DRAM = 1


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
        return meta._meta_table['CiscoQfpMemoryResource_Enum']


class CiscoQfpTimeInterval_Enum(Enum):
    """
    CiscoQfpTimeInterval_Enum

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

    """

    FIVESECONDS = 1

    ONEMINUTE = 2

    FIVEMINUTES = 3

    SIXTYMINUTES = 4


    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
        return meta._meta_table['CiscoQfpTimeInterval_Enum']



class CISCOENTITYQFPMIB(object):
    """
    
    
    .. attribute:: ceqfpmemoryresourcetable
    
    	This table maintains the memory resources statistics for each QFP physical entity.  An agent creates a conceptual row to this table corresponding to a QFP physical entity and its supported memory resource type upon detection of a physical entity supporting the memory  resource statistics for a memory resource type.  An agent destroys a conceptual row from this table        corresponding to a QFP physical entity and its supported memory resource type upon removal of the QFP host physical entity or it does not receive memory resource statistics update for a certain time period. The time period to wait before deleting an entry from this table would be the discretion of the supporting device
    	**type**\: :py:class:`CeqfpMemoryResourceTable <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.CeqfpMemoryResourceTable>`
    
    .. attribute:: ceqfpsystemtable
    
    	This table maintains the QFP system information for each QFP physical entity.  An agent creates a conceptual row to this table corresponding to a QFP physical entity upon detection of a physical entity supporting the QFP system information.  An agent destroys a conceptual row from this table        corresponding to a QFP physical entity upon removal of the QFP host physical entity
    	**type**\: :py:class:`CeqfpSystemTable <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.CeqfpSystemTable>`
    
    .. attribute:: ceqfpthroughputtable
    
    	This table maintains the throughput information for each QFP physical entity.          An agent creates a conceptual row to this table corresponding to a QFP physical entity upon detection of a physical entity supporting the QFP throughput information.          An agent destroys a conceptual row from this table       corresponding to a QFP physical entity upon removal of the QFP host physical entity
    	**type**\: :py:class:`CeqfpThroughputTable <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.CeqfpThroughputTable>`
    
    .. attribute:: ceqfputilizationtable
    
    	This table maintains the utilization statistics collected by each QFP physical entity at various time interval such as last 5 seconds, 1 minute, etc.  An agent creates a conceptual row to this table corresponding to a QFP physical entity for a time interval upon detection of a physical entity supporting the utilization statistics for a time interval.  The agent destroys a conceptual row from this table        corresponding to a QFP physical entity for a time interval upon removal of the QFP host physical entity or it does not receive the utilization statistics update for a certain time period. The time period to wait before deleting an entry from this table would be the discretion of the supporting device
    	**type**\: :py:class:`CeqfpUtilizationTable <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.CeqfpUtilizationTable>`
    
    .. attribute:: ciscoentityqfp
    
    	
    	**type**\: :py:class:`CiscoEntityQfp <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.CiscoEntityQfp>`
    
    .. attribute:: ciscoentityqfpnotif
    
    	
    	**type**\: :py:class:`CiscoEntityQfpNotif <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.CiscoEntityQfpNotif>`
    
    

    """

    _prefix = 'cisco-entity'
    _revision = '2014-06-18'

    def __init__(self):
        self.ceqfpmemoryresourcetable = CISCOENTITYQFPMIB.CeqfpMemoryResourceTable()
        self.ceqfpmemoryresourcetable.parent = self
        self.ceqfpsystemtable = CISCOENTITYQFPMIB.CeqfpSystemTable()
        self.ceqfpsystemtable.parent = self
        self.ceqfpthroughputtable = CISCOENTITYQFPMIB.CeqfpThroughputTable()
        self.ceqfpthroughputtable.parent = self
        self.ceqfputilizationtable = CISCOENTITYQFPMIB.CeqfpUtilizationTable()
        self.ceqfputilizationtable.parent = self
        self.ciscoentityqfp = CISCOENTITYQFPMIB.CiscoEntityQfp()
        self.ciscoentityqfp.parent = self
        self.ciscoentityqfpnotif = CISCOENTITYQFPMIB.CiscoEntityQfpNotif()
        self.ciscoentityqfpnotif.parent = self


    class CeqfpMemoryResourceTable(object):
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
        	**type**\: list of :py:class:`CeqfpMemoryResourceEntry <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.CeqfpMemoryResourceTable.CeqfpMemoryResourceEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2014-06-18'

        def __init__(self):
            self.parent = None
            self.ceqfpmemoryresourceentry = YList()
            self.ceqfpmemoryresourceentry.parent = self
            self.ceqfpmemoryresourceentry.name = 'ceqfpmemoryresourceentry'


        class CeqfpMemoryResourceEntry(object):
            """
            A conceptual row in the ceqfpMemoryResourceTable. There
            is an entry in this table for each QFP entity by a value 
            of entPhysicalIndex and the supported memory resource type 
            by a value of ceqfpMemoryResType.
            
            .. attribute:: ceqfpmemoryrestype
            
            	This object indicates the type of the memory resource used by the QFP. This object is one of the indices to uniquely identify the QFP memory resource type
            	**type**\: :py:class:`CiscoQfpMemoryResource_Enum <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CiscoQfpMemoryResource_Enum>`
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ceqfpmemoryhcresfree
            
            	This object is a 64\-bit version of ceqfpMemoryResFree
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceqfpmemoryhcresinuse
            
            	This object is a 64\-bit version of ceqfpMemoryInRes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceqfpmemoryhcreslowfreewatermark
            
            	This object is a 64\-bit version of ceqfpMemoryResLowFreeWatermark
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceqfpmemoryhcrestotal
            
            	This object is a 64\-bit version of ceqfpMemoryResTotal
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceqfpmemoryresfallingthreshold
            
            	This object represents the falling threshold value for this memory resource. A value of zero means that the falling threshold is not supported for this memory resource.  The value of this object can not be set to higher than or equal to ceqfpMemoryResRisingThreshold.  A falling (ceqfpMemoryResRisingThreshNotif) notification  will be generated, whenever the memory resource usage (ceqfpMemoryHCResInUse) is equal to or lesser than this value.  After a falling notification is generated, another  such notification will not be generated until the  ceqfpMemoryResInUse rises above this value and reaches  the ceqfpMemoryResRisingThreshold
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: ceqfpmemoryresfree
            
            	This object represents the memory which is currently free on this memory resource
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceqfpmemoryresfreeovrflw
            
            	This object represents the upper 32\-bit of ceqfpMemoryResFree. This object needs to be supported only when the value of ceqfpMemoryResFree exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceqfpmemoryresinuse
            
            	This object represents the memory which is currently under use on this memory resource
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceqfpmemoryresinuseovrflw
            
            	This object represents the upper 32\-bit of ceqfpMemoryResInUse. This object needs to be supported only when the value of ceqfpMemoryResInUse exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceqfpmemoryreslowfreewatermark
            
            	This object represents lowest free water mark on this memory resource
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceqfpmemoryreslowfreewatermarkovrflw
            
            	This object represents the upper 32\-bit of ceqfpMemoryResLowFreeWatermark. This object needs to be supported only when the value of ceqfpMemoryResLowFreeWatermark exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceqfpmemoryresrisingthreshold
            
            	This object represents the rising threshold value for this memory resource. A value of zero means that the rising threshold is not supported for this memory resource.  The value of this object can not be set to lower than or equal to ceqfpMemoryResFallingThreshold.  A rising (ceqfpMemoryResRisingThreshNotif) notification will be generated, whenever the memory resource usage (ceqfpMemoryHCResInUse) is equal to or greater than this value.  After a rising notification is generated, another such  notification will not be generated until the  ceqfpMemoryResInUse falls below this value and reaches  the ceqfpMemoryResFallingThreshold
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: ceqfpmemoryrestotal
            
            	This object represents total memory available on this memory resource
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceqfpmemoryrestotalovrflw
            
            	This object represents the upper 32\-bit of ceqfpMemoryResTotal. This object needs to be supported only when the value of ceqfpMemoryResTotal exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2014-06-18'

            def __init__(self):
                self.parent = None
                self.ceqfpmemoryrestype = None
                self.entphysicalindex = None
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
                if self.ceqfpmemoryrestype is None:
                    raise YPYDataValidationError('Key property ceqfpmemoryrestype is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ceqfpMemoryResourceTable/CISCO-ENTITY-QFP-MIB:ceqfpMemoryResourceEntry[CISCO-ENTITY-QFP-MIB:ceqfpMemoryResType = ' + str(self.ceqfpmemoryrestype) + '][CISCO-ENTITY-QFP-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ceqfpmemoryrestype is not None:
                    return True

                if self.entphysicalindex is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
                return meta._meta_table['CISCOENTITYQFPMIB.CeqfpMemoryResourceTable.CeqfpMemoryResourceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ceqfpMemoryResourceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ceqfpmemoryresourceentry is not None:
                for child_ref in self.ceqfpmemoryresourceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
            return meta._meta_table['CISCOENTITYQFPMIB.CeqfpMemoryResourceTable']['meta_info']


    class CeqfpSystemTable(object):
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
        	**type**\: list of :py:class:`CeqfpSystemEntry <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.CeqfpSystemTable.CeqfpSystemEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2014-06-18'

        def __init__(self):
            self.parent = None
            self.ceqfpsystementry = YList()
            self.ceqfpsystementry.parent = self
            self.ceqfpsystementry.name = 'ceqfpsystementry'


        class CeqfpSystemEntry(object):
            """
            A conceptual row in the ceqfpSystemTable. There is an entry
            in this table for each QFP entity, as defined by a value of
            entPhysicalIndex.
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ceqfpnumbersystemloads
            
            	This object represents the number of times the QFP is loaded, since the QFP host is up
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceqfpsystemlastloadtime
            
            	This object represents the QFP last load time
            	**type**\: str
            
            .. attribute:: ceqfpsystemstate
            
            	This object represents the current QFP state. The enumerated values are described below.  unknown (1)    \- The state of the QFP is unknown reset (2)      \- The QFP is reset init (3)       \- The QFP is being initialized active (4)     \- The QFP is active in a system with redundant                  QFP activeSolo (5) \- The QFP is active and there is no redundant                  QFP in the system standby (6)    \- The QFP is standby in a redundant system. hotStandby (7) \- The QFP is standby and synchronized with                  active, so that a switchover in this state                  will preserve state of the active. Stateful                   datapath features are synchronized between the                  active QFP and standby QFP
            	**type**\: :py:class:`CeqfpSystemState_Enum <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.CeqfpSystemTable.CeqfpSystemEntry.CeqfpSystemState_Enum>`
            
            .. attribute:: ceqfpsystemtrafficdirection
            
            	This object represents the traffic direction that this QFP is assigned to process. The enumerated values are described below.  none (1)    \- The QFP is not assigned to processes any traffic               yet ingress (2) \- The QFP processes inbound traffic egress (3)  \- The QFP processes outbound traffic both (4)    \- The QFP processes both inbound and outbound               traffic
            	**type**\: :py:class:`CeqfpSystemTrafficDirection_Enum <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.CeqfpSystemTable.CeqfpSystemEntry.CeqfpSystemTrafficDirection_Enum>`
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2014-06-18'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.ceqfpnumbersystemloads = None
                self.ceqfpsystemlastloadtime = None
                self.ceqfpsystemstate = None
                self.ceqfpsystemtrafficdirection = None

            class CeqfpSystemState_Enum(Enum):
                """
                CeqfpSystemState_Enum

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

                """

                UNKNOWN = 1

                RESET = 2

                INIT = 3

                ACTIVE = 4

                ACTIVESOLO = 5

                STANDBY = 6

                HOTSTANDBY = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
                    return meta._meta_table['CISCOENTITYQFPMIB.CeqfpSystemTable.CeqfpSystemEntry.CeqfpSystemState_Enum']


            class CeqfpSystemTrafficDirection_Enum(Enum):
                """
                CeqfpSystemTrafficDirection_Enum

                This object represents the traffic direction that this QFP is
                assigned to process. The enumerated values are described below.
                
                none (1)    \- The QFP is not assigned to processes any traffic
                              yet
                ingress (2) \- The QFP processes inbound traffic
                egress (3)  \- The QFP processes outbound traffic
                both (4)    \- The QFP processes both inbound and outbound
                              traffic

                """

                NONE = 1

                INGRESS = 2

                EGRESS = 3

                BOTH = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
                    return meta._meta_table['CISCOENTITYQFPMIB.CeqfpSystemTable.CeqfpSystemEntry.CeqfpSystemTrafficDirection_Enum']


            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ceqfpSystemTable/CISCO-ENTITY-QFP-MIB:ceqfpSystemEntry[CISCO-ENTITY-QFP-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

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

                if self.ceqfpnumbersystemloads is not None:
                    return True

                if self.ceqfpsystemlastloadtime is not None:
                    return True

                if self.ceqfpsystemstate is not None:
                    return True

                if self.ceqfpsystemtrafficdirection is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
                return meta._meta_table['CISCOENTITYQFPMIB.CeqfpSystemTable.CeqfpSystemEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ceqfpSystemTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ceqfpsystementry is not None:
                for child_ref in self.ceqfpsystementry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
            return meta._meta_table['CISCOENTITYQFPMIB.CeqfpSystemTable']['meta_info']


    class CeqfpThroughputTable(object):
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
        	**type**\: list of :py:class:`CeqfpThroughputEntry <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.CeqfpThroughputTable.CeqfpThroughputEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2014-06-18'

        def __init__(self):
            self.parent = None
            self.ceqfpthroughputentry = YList()
            self.ceqfpthroughputentry.parent = self
            self.ceqfpthroughputentry.name = 'ceqfpthroughputentry'


        class CeqfpThroughputEntry(object):
            """
            A conceptual row in the ceqfpThroughputTable. There is an entry
            in this table for each QFP entity, as defined by a value of
            entPhysicalIndex.
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ceqfpthroughputavgrate
            
            	The object represents the average throughput rate in the interval ceqfpThroughputInterval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceqfpthroughputinterval
            
            	The object represents the configured time interval at which the ceqfpThroughputLevel is checked
            	**type**\: int
            
            	**range:** 10..86400
            
            .. attribute:: ceqfpthroughputlevel
            
            	This object represents the current throughput level for installed throughput license.                  normal  (1) \- Throughput usage is normal                 warning (2) \- Throughput usage has crossed the                               configured threshold limit                 exceed  (3) \- Throughput usage has exceeded the                               total licensed bandwidth
            	**type**\: :py:class:`CeqfpThroughputLevel_Enum <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.CeqfpThroughputTable.CeqfpThroughputEntry.CeqfpThroughputLevel_Enum>`
            
            .. attribute:: ceqfpthroughputlicensedbw
            
            	This object represents the bandwidth for installed throughput license
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceqfpthroughputthreshold
            
            	The object represents the configured throughput threshold
            	**type**\: int
            
            	**range:** 75..95
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2014-06-18'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.ceqfpthroughputavgrate = None
                self.ceqfpthroughputinterval = None
                self.ceqfpthroughputlevel = None
                self.ceqfpthroughputlicensedbw = None
                self.ceqfpthroughputthreshold = None

            class CeqfpThroughputLevel_Enum(Enum):
                """
                CeqfpThroughputLevel_Enum

                This object represents the current throughput level for
                installed throughput license.
                
                                normal  (1) \- Throughput usage is normal
                                warning (2) \- Throughput usage has crossed the
                                              configured threshold limit
                                exceed  (3) \- Throughput usage has exceeded the
                                              total licensed bandwidth

                """

                NORMAL = 1

                WARNING = 2

                EXCEED = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
                    return meta._meta_table['CISCOENTITYQFPMIB.CeqfpThroughputTable.CeqfpThroughputEntry.CeqfpThroughputLevel_Enum']


            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ceqfpThroughputTable/CISCO-ENTITY-QFP-MIB:ceqfpThroughputEntry[CISCO-ENTITY-QFP-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
                return meta._meta_table['CISCOENTITYQFPMIB.CeqfpThroughputTable.CeqfpThroughputEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ceqfpThroughputTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ceqfpthroughputentry is not None:
                for child_ref in self.ceqfpthroughputentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
            return meta._meta_table['CISCOENTITYQFPMIB.CeqfpThroughputTable']['meta_info']


    class CeqfpUtilizationTable(object):
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
        	**type**\: list of :py:class:`CeqfpUtilizationEntry <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.CeqfpUtilizationTable.CeqfpUtilizationEntry>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2014-06-18'

        def __init__(self):
            self.parent = None
            self.ceqfputilizationentry = YList()
            self.ceqfputilizationentry.parent = self
            self.ceqfputilizationentry.name = 'ceqfputilizationentry'


        class CeqfpUtilizationEntry(object):
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
            
            .. attribute:: ceqfputiltimeinterval
            
            	This object identifies the time interval for which the utilization statistics being collected. The interval  values can be 5 second, 1 minute, etc. as specified in  the CiscoQfpTimeInterval
            	**type**\: :py:class:`CiscoQfpTimeInterval_Enum <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CiscoQfpTimeInterval_Enum>`
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ceqfputilinputnonprioritybitrate
            
            	This object represents the QFP input channel non\-priority bit rate during this interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceqfputilinputnonprioritypktrate
            
            	This object represents the QFP input channel non\-priority packet rate during this interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceqfputilinputprioritybitrate
            
            	This object represents the QFP input channel priority bit rate during this interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceqfputilinputprioritypktrate
            
            	This object represents the QFP input channel priority packet rate during this interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceqfputilinputtotalbitrate
            
            	This object represents the QFP input channel total bit rate during this interval, which includes both priority and non\-priority input bit rate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceqfputilinputtotalpktrate
            
            	This object represents the QFP input channel total packet rate during this interval, which includes both priority and non\-priority input packet rate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceqfputiloutputnonprioritybitrate
            
            	This object represents the QFP output channel non\-priority bit rate during this interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceqfputiloutputnonprioritypktrate
            
            	This object represents the QFP output channel non\-priority packet rate during this interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceqfputiloutputprioritybitrate
            
            	This object represents the QFP output channel priority bit rate during this interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceqfputiloutputprioritypktrate
            
            	This object represents the QFP output channel priority packet rate during this interval
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceqfputiloutputtotalbitrate
            
            	This object represents the QFP output channel total bit rate during this interval, which includes both priority and non\-priority bit rate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceqfputiloutputtotalpktrate
            
            	This object represents the QFP output channel total packet rate during this interval, which includes both priority and non\-priority output packet rate
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceqfputilprocessingload
            
            	This object represents the QFP processing load during this interval
            	**type**\: int
            
            	**range:** 0..100
            
            

            """

            _prefix = 'cisco-entity'
            _revision = '2014-06-18'

            def __init__(self):
                self.parent = None
                self.ceqfputiltimeinterval = None
                self.entphysicalindex = None
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
                if self.ceqfputiltimeinterval is None:
                    raise YPYDataValidationError('Key property ceqfputiltimeinterval is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ceqfpUtilizationTable/CISCO-ENTITY-QFP-MIB:ceqfpUtilizationEntry[CISCO-ENTITY-QFP-MIB:ceqfpUtilTimeInterval = ' + str(self.ceqfputiltimeinterval) + '][CISCO-ENTITY-QFP-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ceqfputiltimeinterval is not None:
                    return True

                if self.entphysicalindex is not None:
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

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
                return meta._meta_table['CISCOENTITYQFPMIB.CeqfpUtilizationTable.CeqfpUtilizationEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ceqfpUtilizationTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ceqfputilizationentry is not None:
                for child_ref in self.ceqfputilizationentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
            return meta._meta_table['CISCOENTITYQFPMIB.CeqfpUtilizationTable']['meta_info']


    class CiscoEntityQfp(object):
        """
        
        
        .. attribute:: ceqfpfiveminutesutilalgo
        
        	This objects represents the method used to calculate 5 Minutes interval utilization data. The enumerated values are described below.  unknown    (1) \- The calculation method is unknown fiveSecSMA (2) \- The value is calculated using Simple Moving                    Average of last 60 five seconds utilization                  data
        	**type**\: :py:class:`CeqfpFiveMinutesUtilAlgo_Enum <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.CiscoEntityQfp.CeqfpFiveMinutesUtilAlgo_Enum>`
        
        .. attribute:: ceqfpfivesecondutilalgo
        
        	This objects represents the method used to calculate 5 Second interval utilization data. The enumerated values are described below.  unknown       (1) \- The calculation method is unknown fiveSecSample (2) \- The value is calculated based on the last                     5 second sampling period of utilization                     data
        	**type**\: :py:class:`CeqfpFiveSecondUtilAlgo_Enum <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.CiscoEntityQfp.CeqfpFiveSecondUtilAlgo_Enum>`
        
        .. attribute:: ceqfponeminuteutilalgo
        
        	This objects represents the method used to calculate 1 Minute interval utilization data. The enumerated values are described below.  unknown    (1) \- The calculation method is unknown fiveSecSMA (2) \- The value is calculated using Simple Moving                    Average of last 12 five seconds utilization                  data
        	**type**\: :py:class:`CeqfpOneMinuteUtilAlgo_Enum <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.CiscoEntityQfp.CeqfpOneMinuteUtilAlgo_Enum>`
        
        .. attribute:: ceqfpsixtyminutesutilalgo
        
        	This objects represents the method used to calculate 60 Minutes interval utilization data. The enumerated values are described below.  unknown    (1) \- The calculation method is unknown fiveSecSMA (1) \- The value is calculated using Simple Moving                    Average of last 720 five seconds utilization                  data
        	**type**\: :py:class:`CeqfpSixtyMinutesUtilAlgo_Enum <ydk.models.entity.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.CiscoEntityQfp.CeqfpSixtyMinutesUtilAlgo_Enum>`
        
        

        """

        _prefix = 'cisco-entity'
        _revision = '2014-06-18'

        def __init__(self):
            self.parent = None
            self.ceqfpfiveminutesutilalgo = None
            self.ceqfpfivesecondutilalgo = None
            self.ceqfponeminuteutilalgo = None
            self.ceqfpsixtyminutesutilalgo = None

        class CeqfpFiveMinutesUtilAlgo_Enum(Enum):
            """
            CeqfpFiveMinutesUtilAlgo_Enum

            This objects represents the method used to calculate 5 Minutes
            interval utilization data. The enumerated values are described
            below.
            
            unknown    (1) \- The calculation method is unknown
            fiveSecSMA (2) \- The value is calculated using Simple Moving  
                             Average of last 60 five seconds utilization
                             data.

            """

            UNKNOWN = 1

            FIVESECSMA = 2


            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
                return meta._meta_table['CISCOENTITYQFPMIB.CiscoEntityQfp.CeqfpFiveMinutesUtilAlgo_Enum']


        class CeqfpFiveSecondUtilAlgo_Enum(Enum):
            """
            CeqfpFiveSecondUtilAlgo_Enum

            This objects represents the method used to calculate 5 Second
            interval utilization data. The enumerated values are described
            below.
            
            unknown       (1) \- The calculation method is unknown
            fiveSecSample (2) \- The value is calculated based on the last
                                5 second sampling period of utilization
                                data.

            """

            UNKNOWN = 1

            FIVESECSAMPLE = 2


            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
                return meta._meta_table['CISCOENTITYQFPMIB.CiscoEntityQfp.CeqfpFiveSecondUtilAlgo_Enum']


        class CeqfpOneMinuteUtilAlgo_Enum(Enum):
            """
            CeqfpOneMinuteUtilAlgo_Enum

            This objects represents the method used to calculate 1 Minute
            interval utilization data. The enumerated values are described
            below.
            
            unknown    (1) \- The calculation method is unknown
            fiveSecSMA (2) \- The value is calculated using Simple Moving  
                             Average of last 12 five seconds utilization
                             data.

            """

            UNKNOWN = 1

            FIVESECSMA = 2


            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
                return meta._meta_table['CISCOENTITYQFPMIB.CiscoEntityQfp.CeqfpOneMinuteUtilAlgo_Enum']


        class CeqfpSixtyMinutesUtilAlgo_Enum(Enum):
            """
            CeqfpSixtyMinutesUtilAlgo_Enum

            This objects represents the method used to calculate 60 Minutes
            interval utilization data. The enumerated values are described
            below.
            
            unknown    (1) \- The calculation method is unknown
            fiveSecSMA (1) \- The value is calculated using Simple Moving  
                             Average of last 720 five seconds utilization
                             data.

            """

            UNKNOWN = 1

            FIVESECSMA = 2


            @staticmethod
            def _meta_info():
                from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
                return meta._meta_table['CISCOENTITYQFPMIB.CiscoEntityQfp.CeqfpSixtyMinutesUtilAlgo_Enum']


        @property
        def _common_path(self):

            return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/CISCO-ENTITY-QFP-MIB:ciscoEntityQfp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ceqfpfiveminutesutilalgo is not None:
                return True

            if self.ceqfpfivesecondutilalgo is not None:
                return True

            if self.ceqfponeminuteutilalgo is not None:
                return True

            if self.ceqfpsixtyminutesutilalgo is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
            return meta._meta_table['CISCOENTITYQFPMIB.CiscoEntityQfp']['meta_info']


    class CiscoEntityQfpNotif(object):
        """
        
        
        .. attribute:: ceqfpmemoryresthreshnotifenabled
        
        	This object controls memory resource rising and falling threshold notification.  When this object contains a value 'true', then generation of memory resource threshold notification is enabled. If this object contains a value 'false', then generation of memory resource threshold notification is disabled
        	**type**\: bool
        
        .. attribute:: ceqfpthroughputnotifenabled
        
        	This object controls throughput rate notification.  When this object contains a value 'true', then generation of ceqfpThroughputNotif is enabled. If this object contains a value 'false', then generation of ceqfpThroughputNotif is disabled
        	**type**\: bool
        
        

        """

        _prefix = 'cisco-entity'
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
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ceqfpmemoryresthreshnotifenabled is not None:
                return True

            if self.ceqfpthroughputnotifenabled is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
            return meta._meta_table['CISCOENTITYQFPMIB.CiscoEntityQfpNotif']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ceqfpmemoryresourcetable is not None and self.ceqfpmemoryresourcetable._has_data():
            return True

        if self.ceqfpmemoryresourcetable is not None and self.ceqfpmemoryresourcetable.is_presence():
            return True

        if self.ceqfpsystemtable is not None and self.ceqfpsystemtable._has_data():
            return True

        if self.ceqfpsystemtable is not None and self.ceqfpsystemtable.is_presence():
            return True

        if self.ceqfpthroughputtable is not None and self.ceqfpthroughputtable._has_data():
            return True

        if self.ceqfpthroughputtable is not None and self.ceqfpthroughputtable.is_presence():
            return True

        if self.ceqfputilizationtable is not None and self.ceqfputilizationtable._has_data():
            return True

        if self.ceqfputilizationtable is not None and self.ceqfputilizationtable.is_presence():
            return True

        if self.ciscoentityqfp is not None and self.ciscoentityqfp._has_data():
            return True

        if self.ciscoentityqfp is not None and self.ciscoentityqfp.is_presence():
            return True

        if self.ciscoentityqfpnotif is not None and self.ciscoentityqfpnotif._has_data():
            return True

        if self.ciscoentityqfpnotif is not None and self.ciscoentityqfpnotif.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.entity._meta import _CISCO_ENTITY_QFP_MIB as meta
        return meta._meta_table['CISCOENTITYQFPMIB']['meta_info']


