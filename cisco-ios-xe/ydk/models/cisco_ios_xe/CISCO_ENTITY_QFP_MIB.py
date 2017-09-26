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
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class CiscoQfpMemoryResource(Enum):
    """
    CiscoQfpMemoryResource

    An enumerated integer\-value describing various memory resources

    used by the QFP.

    dram (1) \- Dynamic Random Access Memory (DRAM) memory resource

    .. data:: dram = 1

    """

    dram = Enum.YLeaf(1, "dram")


class CiscoQfpTimeInterval(Enum):
    """
    CiscoQfpTimeInterval

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

    fiveSeconds = Enum.YLeaf(1, "fiveSeconds")

    oneMinute = Enum.YLeaf(2, "oneMinute")

    fiveMinutes = Enum.YLeaf(3, "fiveMinutes")

    sixtyMinutes = Enum.YLeaf(4, "sixtyMinutes")



class CISCOENTITYQFPMIB(Entity):
    """
    
    
    .. attribute:: ceqfpmemoryresourcetable
    
    	This table maintains the memory resources statistics for each QFP physical entity.  An agent creates a conceptual row to this table corresponding to a QFP physical entity and its supported memory resource type upon detection of a physical entity supporting the memory  resource statistics for a memory resource type.  An agent destroys a conceptual row from this table        corresponding to a QFP physical entity and its supported memory resource type upon removal of the QFP host physical entity or it does not receive memory resource statistics update for a certain time period. The time period to wait before deleting an entry from this table would be the discretion of the supporting device
    	**type**\:   :py:class:`Ceqfpmemoryresourcetable <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.Ceqfpmemoryresourcetable>`
    
    .. attribute:: ceqfpsystemtable
    
    	This table maintains the QFP system information for each QFP physical entity.  An agent creates a conceptual row to this table corresponding to a QFP physical entity upon detection of a physical entity supporting the QFP system information.  An agent destroys a conceptual row from this table        corresponding to a QFP physical entity upon removal of the QFP host physical entity
    	**type**\:   :py:class:`Ceqfpsystemtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.Ceqfpsystemtable>`
    
    .. attribute:: ceqfpthroughputtable
    
    	This table maintains the throughput information for each QFP physical entity.          An agent creates a conceptual row to this table corresponding to a QFP physical entity upon detection of a physical entity supporting the QFP throughput information.          An agent destroys a conceptual row from this table       corresponding to a QFP physical entity upon removal of the QFP host physical entity
    	**type**\:   :py:class:`Ceqfpthroughputtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.Ceqfpthroughputtable>`
    
    .. attribute:: ceqfputilizationtable
    
    	This table maintains the utilization statistics collected by each QFP physical entity at various time interval such as last 5 seconds, 1 minute, etc.  An agent creates a conceptual row to this table corresponding to a QFP physical entity for a time interval upon detection of a physical entity supporting the utilization statistics for a time interval.  The agent destroys a conceptual row from this table        corresponding to a QFP physical entity for a time interval upon removal of the QFP host physical entity or it does not receive the utilization statistics update for a certain time period. The time period to wait before deleting an entry from this table would be the discretion of the supporting device
    	**type**\:   :py:class:`Ceqfputilizationtable <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.Ceqfputilizationtable>`
    
    .. attribute:: ciscoentityqfp
    
    	
    	**type**\:   :py:class:`Ciscoentityqfp <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.Ciscoentityqfp>`
    
    .. attribute:: ciscoentityqfpnotif
    
    	
    	**type**\:   :py:class:`Ciscoentityqfpnotif <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.Ciscoentityqfpnotif>`
    
    

    """

    _prefix = 'CISCO-ENTITY-QFP-MIB'
    _revision = '2014-06-18'

    def __init__(self):
        super(CISCOENTITYQFPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ENTITY-QFP-MIB"
        self.yang_parent_name = "CISCO-ENTITY-QFP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"ceqfpMemoryResourceTable" : ("ceqfpmemoryresourcetable", CISCOENTITYQFPMIB.Ceqfpmemoryresourcetable), "ceqfpSystemTable" : ("ceqfpsystemtable", CISCOENTITYQFPMIB.Ceqfpsystemtable), "ceqfpThroughputTable" : ("ceqfpthroughputtable", CISCOENTITYQFPMIB.Ceqfpthroughputtable), "ceqfpUtilizationTable" : ("ceqfputilizationtable", CISCOENTITYQFPMIB.Ceqfputilizationtable), "ciscoEntityQfp" : ("ciscoentityqfp", CISCOENTITYQFPMIB.Ciscoentityqfp), "ciscoEntityQfpNotif" : ("ciscoentityqfpnotif", CISCOENTITYQFPMIB.Ciscoentityqfpnotif)}
        self._child_list_classes = {}

        self.ceqfpmemoryresourcetable = CISCOENTITYQFPMIB.Ceqfpmemoryresourcetable()
        self.ceqfpmemoryresourcetable.parent = self
        self._children_name_map["ceqfpmemoryresourcetable"] = "ceqfpMemoryResourceTable"
        self._children_yang_names.add("ceqfpMemoryResourceTable")

        self.ceqfpsystemtable = CISCOENTITYQFPMIB.Ceqfpsystemtable()
        self.ceqfpsystemtable.parent = self
        self._children_name_map["ceqfpsystemtable"] = "ceqfpSystemTable"
        self._children_yang_names.add("ceqfpSystemTable")

        self.ceqfpthroughputtable = CISCOENTITYQFPMIB.Ceqfpthroughputtable()
        self.ceqfpthroughputtable.parent = self
        self._children_name_map["ceqfpthroughputtable"] = "ceqfpThroughputTable"
        self._children_yang_names.add("ceqfpThroughputTable")

        self.ceqfputilizationtable = CISCOENTITYQFPMIB.Ceqfputilizationtable()
        self.ceqfputilizationtable.parent = self
        self._children_name_map["ceqfputilizationtable"] = "ceqfpUtilizationTable"
        self._children_yang_names.add("ceqfpUtilizationTable")

        self.ciscoentityqfp = CISCOENTITYQFPMIB.Ciscoentityqfp()
        self.ciscoentityqfp.parent = self
        self._children_name_map["ciscoentityqfp"] = "ciscoEntityQfp"
        self._children_yang_names.add("ciscoEntityQfp")

        self.ciscoentityqfpnotif = CISCOENTITYQFPMIB.Ciscoentityqfpnotif()
        self.ciscoentityqfpnotif.parent = self
        self._children_name_map["ciscoentityqfpnotif"] = "ciscoEntityQfpNotif"
        self._children_yang_names.add("ciscoEntityQfpNotif")
        self._segment_path = lambda: "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB"


    class Ceqfpmemoryresourcetable(Entity):
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
        	**type**\: list of    :py:class:`Ceqfpmemoryresourceentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.Ceqfpmemoryresourcetable.Ceqfpmemoryresourceentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-QFP-MIB'
        _revision = '2014-06-18'

        def __init__(self):
            super(CISCOENTITYQFPMIB.Ceqfpmemoryresourcetable, self).__init__()

            self.yang_name = "ceqfpMemoryResourceTable"
            self.yang_parent_name = "CISCO-ENTITY-QFP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"ceqfpMemoryResourceEntry" : ("ceqfpmemoryresourceentry", CISCOENTITYQFPMIB.Ceqfpmemoryresourcetable.Ceqfpmemoryresourceentry)}

            self.ceqfpmemoryresourceentry = YList(self)
            self._segment_path = lambda: "ceqfpMemoryResourceTable"
            self._absolute_path = lambda: "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYQFPMIB.Ceqfpmemoryresourcetable, [], name, value)


        class Ceqfpmemoryresourceentry(Entity):
            """
            A conceptual row in the ceqfpMemoryResourceTable. There
            is an entry in this table for each QFP entity by a value 
            of entPhysicalIndex and the supported memory resource type 
            by a value of ceqfpMemoryResType.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceqfpmemoryrestype  <key>
            
            	This object indicates the type of the memory resource used by the QFP. This object is one of the indices to uniquely identify the QFP memory resource type
            	**type**\:   :py:class:`CiscoQfpMemoryResource <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoQfpMemoryResource>`
            
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
                super(CISCOENTITYQFPMIB.Ceqfpmemoryresourcetable.Ceqfpmemoryresourceentry, self).__init__()

                self.yang_name = "ceqfpMemoryResourceEntry"
                self.yang_parent_name = "ceqfpMemoryResourceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ceqfpmemoryrestype = YLeaf(YType.enumeration, "ceqfpMemoryResType")

                self.ceqfpmemoryhcresfree = YLeaf(YType.uint64, "ceqfpMemoryHCResFree")

                self.ceqfpmemoryhcresinuse = YLeaf(YType.uint64, "ceqfpMemoryHCResInUse")

                self.ceqfpmemoryhcreslowfreewatermark = YLeaf(YType.uint64, "ceqfpMemoryHCResLowFreeWatermark")

                self.ceqfpmemoryhcrestotal = YLeaf(YType.uint64, "ceqfpMemoryHCResTotal")

                self.ceqfpmemoryresfallingthreshold = YLeaf(YType.uint32, "ceqfpMemoryResFallingThreshold")

                self.ceqfpmemoryresfree = YLeaf(YType.uint32, "ceqfpMemoryResFree")

                self.ceqfpmemoryresfreeovrflw = YLeaf(YType.uint32, "ceqfpMemoryResFreeOvrflw")

                self.ceqfpmemoryresinuse = YLeaf(YType.uint32, "ceqfpMemoryResInUse")

                self.ceqfpmemoryresinuseovrflw = YLeaf(YType.uint32, "ceqfpMemoryResInUseOvrflw")

                self.ceqfpmemoryreslowfreewatermark = YLeaf(YType.uint32, "ceqfpMemoryResLowFreeWatermark")

                self.ceqfpmemoryreslowfreewatermarkovrflw = YLeaf(YType.uint32, "ceqfpMemoryResLowFreeWatermarkOvrflw")

                self.ceqfpmemoryresrisingthreshold = YLeaf(YType.uint32, "ceqfpMemoryResRisingThreshold")

                self.ceqfpmemoryrestotal = YLeaf(YType.uint32, "ceqfpMemoryResTotal")

                self.ceqfpmemoryrestotalovrflw = YLeaf(YType.uint32, "ceqfpMemoryResTotalOvrflw")
                self._segment_path = lambda: "ceqfpMemoryResourceEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[ceqfpMemoryResType='" + self.ceqfpmemoryrestype.get() + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/ceqfpMemoryResourceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYQFPMIB.Ceqfpmemoryresourcetable.Ceqfpmemoryresourceentry, ['entphysicalindex', 'ceqfpmemoryrestype', 'ceqfpmemoryhcresfree', 'ceqfpmemoryhcresinuse', 'ceqfpmemoryhcreslowfreewatermark', 'ceqfpmemoryhcrestotal', 'ceqfpmemoryresfallingthreshold', 'ceqfpmemoryresfree', 'ceqfpmemoryresfreeovrflw', 'ceqfpmemoryresinuse', 'ceqfpmemoryresinuseovrflw', 'ceqfpmemoryreslowfreewatermark', 'ceqfpmemoryreslowfreewatermarkovrflw', 'ceqfpmemoryresrisingthreshold', 'ceqfpmemoryrestotal', 'ceqfpmemoryrestotalovrflw'], name, value)


    class Ceqfpsystemtable(Entity):
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
        	**type**\: list of    :py:class:`Ceqfpsystementry <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.Ceqfpsystemtable.Ceqfpsystementry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-QFP-MIB'
        _revision = '2014-06-18'

        def __init__(self):
            super(CISCOENTITYQFPMIB.Ceqfpsystemtable, self).__init__()

            self.yang_name = "ceqfpSystemTable"
            self.yang_parent_name = "CISCO-ENTITY-QFP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"ceqfpSystemEntry" : ("ceqfpsystementry", CISCOENTITYQFPMIB.Ceqfpsystemtable.Ceqfpsystementry)}

            self.ceqfpsystementry = YList(self)
            self._segment_path = lambda: "ceqfpSystemTable"
            self._absolute_path = lambda: "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYQFPMIB.Ceqfpsystemtable, [], name, value)


        class Ceqfpsystementry(Entity):
            """
            A conceptual row in the ceqfpSystemTable. There is an entry
            in this table for each QFP entity, as defined by a value of
            entPhysicalIndex.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceqfpnumbersystemloads
            
            	This object represents the number of times the QFP is loaded, since the QFP host is up
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceqfpsystemlastloadtime
            
            	This object represents the QFP last load time
            	**type**\:  str
            
            .. attribute:: ceqfpsystemstate
            
            	This object represents the current QFP state. The enumerated values are described below.  unknown (1)    \- The state of the QFP is unknown reset (2)      \- The QFP is reset init (3)       \- The QFP is being initialized active (4)     \- The QFP is active in a system with redundant                  QFP activeSolo (5) \- The QFP is active and there is no redundant                  QFP in the system standby (6)    \- The QFP is standby in a redundant system. hotStandby (7) \- The QFP is standby and synchronized with                  active, so that a switchover in this state                  will preserve state of the active. Stateful                   datapath features are synchronized between the                  active QFP and standby QFP
            	**type**\:   :py:class:`Ceqfpsystemstate <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.Ceqfpsystemtable.Ceqfpsystementry.Ceqfpsystemstate>`
            
            .. attribute:: ceqfpsystemtrafficdirection
            
            	This object represents the traffic direction that this QFP is assigned to process. The enumerated values are described below.  none (1)    \- The QFP is not assigned to processes any traffic               yet ingress (2) \- The QFP processes inbound traffic egress (3)  \- The QFP processes outbound traffic both (4)    \- The QFP processes both inbound and outbound               traffic
            	**type**\:   :py:class:`Ceqfpsystemtrafficdirection <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.Ceqfpsystemtable.Ceqfpsystementry.Ceqfpsystemtrafficdirection>`
            
            

            """

            _prefix = 'CISCO-ENTITY-QFP-MIB'
            _revision = '2014-06-18'

            def __init__(self):
                super(CISCOENTITYQFPMIB.Ceqfpsystemtable.Ceqfpsystementry, self).__init__()

                self.yang_name = "ceqfpSystemEntry"
                self.yang_parent_name = "ceqfpSystemTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ceqfpnumbersystemloads = YLeaf(YType.uint32, "ceqfpNumberSystemLoads")

                self.ceqfpsystemlastloadtime = YLeaf(YType.str, "ceqfpSystemLastLoadTime")

                self.ceqfpsystemstate = YLeaf(YType.enumeration, "ceqfpSystemState")

                self.ceqfpsystemtrafficdirection = YLeaf(YType.enumeration, "ceqfpSystemTrafficDirection")
                self._segment_path = lambda: "ceqfpSystemEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/ceqfpSystemTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYQFPMIB.Ceqfpsystemtable.Ceqfpsystementry, ['entphysicalindex', 'ceqfpnumbersystemloads', 'ceqfpsystemlastloadtime', 'ceqfpsystemstate', 'ceqfpsystemtrafficdirection'], name, value)

            class Ceqfpsystemstate(Enum):
                """
                Ceqfpsystemstate

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

                unknown = Enum.YLeaf(1, "unknown")

                reset = Enum.YLeaf(2, "reset")

                init = Enum.YLeaf(3, "init")

                active = Enum.YLeaf(4, "active")

                activeSolo = Enum.YLeaf(5, "activeSolo")

                standby = Enum.YLeaf(6, "standby")

                hotStandby = Enum.YLeaf(7, "hotStandby")


            class Ceqfpsystemtrafficdirection(Enum):
                """
                Ceqfpsystemtrafficdirection

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

                none = Enum.YLeaf(1, "none")

                ingress = Enum.YLeaf(2, "ingress")

                egress = Enum.YLeaf(3, "egress")

                both = Enum.YLeaf(4, "both")



    class Ceqfpthroughputtable(Entity):
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
        	**type**\: list of    :py:class:`Ceqfpthroughputentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.Ceqfpthroughputtable.Ceqfpthroughputentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-QFP-MIB'
        _revision = '2014-06-18'

        def __init__(self):
            super(CISCOENTITYQFPMIB.Ceqfpthroughputtable, self).__init__()

            self.yang_name = "ceqfpThroughputTable"
            self.yang_parent_name = "CISCO-ENTITY-QFP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"ceqfpThroughputEntry" : ("ceqfpthroughputentry", CISCOENTITYQFPMIB.Ceqfpthroughputtable.Ceqfpthroughputentry)}

            self.ceqfpthroughputentry = YList(self)
            self._segment_path = lambda: "ceqfpThroughputTable"
            self._absolute_path = lambda: "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYQFPMIB.Ceqfpthroughputtable, [], name, value)


        class Ceqfpthroughputentry(Entity):
            """
            A conceptual row in the ceqfpThroughputTable. There is an entry
            in this table for each QFP entity, as defined by a value of
            entPhysicalIndex.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
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
            	**type**\:   :py:class:`Ceqfpthroughputlevel <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.Ceqfpthroughputtable.Ceqfpthroughputentry.Ceqfpthroughputlevel>`
            
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
                super(CISCOENTITYQFPMIB.Ceqfpthroughputtable.Ceqfpthroughputentry, self).__init__()

                self.yang_name = "ceqfpThroughputEntry"
                self.yang_parent_name = "ceqfpThroughputTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ceqfpthroughputavgrate = YLeaf(YType.uint64, "ceqfpThroughputAvgRate")

                self.ceqfpthroughputinterval = YLeaf(YType.int32, "ceqfpThroughputInterval")

                self.ceqfpthroughputlevel = YLeaf(YType.enumeration, "ceqfpThroughputLevel")

                self.ceqfpthroughputlicensedbw = YLeaf(YType.uint64, "ceqfpThroughputLicensedBW")

                self.ceqfpthroughputthreshold = YLeaf(YType.int32, "ceqfpThroughputThreshold")
                self._segment_path = lambda: "ceqfpThroughputEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/ceqfpThroughputTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYQFPMIB.Ceqfpthroughputtable.Ceqfpthroughputentry, ['entphysicalindex', 'ceqfpthroughputavgrate', 'ceqfpthroughputinterval', 'ceqfpthroughputlevel', 'ceqfpthroughputlicensedbw', 'ceqfpthroughputthreshold'], name, value)

            class Ceqfpthroughputlevel(Enum):
                """
                Ceqfpthroughputlevel

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

                normal = Enum.YLeaf(1, "normal")

                warning = Enum.YLeaf(2, "warning")

                exceed = Enum.YLeaf(3, "exceed")



    class Ceqfputilizationtable(Entity):
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
        	**type**\: list of    :py:class:`Ceqfputilizationentry <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.Ceqfputilizationtable.Ceqfputilizationentry>`
        
        

        """

        _prefix = 'CISCO-ENTITY-QFP-MIB'
        _revision = '2014-06-18'

        def __init__(self):
            super(CISCOENTITYQFPMIB.Ceqfputilizationtable, self).__init__()

            self.yang_name = "ceqfpUtilizationTable"
            self.yang_parent_name = "CISCO-ENTITY-QFP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"ceqfpUtilizationEntry" : ("ceqfputilizationentry", CISCOENTITYQFPMIB.Ceqfputilizationtable.Ceqfputilizationentry)}

            self.ceqfputilizationentry = YList(self)
            self._segment_path = lambda: "ceqfpUtilizationTable"
            self._absolute_path = lambda: "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYQFPMIB.Ceqfputilizationtable, [], name, value)


        class Ceqfputilizationentry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceqfputiltimeinterval  <key>
            
            	This object identifies the time interval for which the utilization statistics being collected. The interval  values can be 5 second, 1 minute, etc. as specified in  the CiscoQfpTimeInterval
            	**type**\:   :py:class:`CiscoQfpTimeInterval <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CiscoQfpTimeInterval>`
            
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
                super(CISCOENTITYQFPMIB.Ceqfputilizationtable.Ceqfputilizationentry, self).__init__()

                self.yang_name = "ceqfpUtilizationEntry"
                self.yang_parent_name = "ceqfpUtilizationTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ceqfputiltimeinterval = YLeaf(YType.enumeration, "ceqfpUtilTimeInterval")

                self.ceqfputilinputnonprioritybitrate = YLeaf(YType.uint64, "ceqfpUtilInputNonPriorityBitRate")

                self.ceqfputilinputnonprioritypktrate = YLeaf(YType.uint64, "ceqfpUtilInputNonPriorityPktRate")

                self.ceqfputilinputprioritybitrate = YLeaf(YType.uint64, "ceqfpUtilInputPriorityBitRate")

                self.ceqfputilinputprioritypktrate = YLeaf(YType.uint64, "ceqfpUtilInputPriorityPktRate")

                self.ceqfputilinputtotalbitrate = YLeaf(YType.uint64, "ceqfpUtilInputTotalBitRate")

                self.ceqfputilinputtotalpktrate = YLeaf(YType.uint64, "ceqfpUtilInputTotalPktRate")

                self.ceqfputiloutputnonprioritybitrate = YLeaf(YType.uint64, "ceqfpUtilOutputNonPriorityBitRate")

                self.ceqfputiloutputnonprioritypktrate = YLeaf(YType.uint64, "ceqfpUtilOutputNonPriorityPktRate")

                self.ceqfputiloutputprioritybitrate = YLeaf(YType.uint64, "ceqfpUtilOutputPriorityBitRate")

                self.ceqfputiloutputprioritypktrate = YLeaf(YType.uint64, "ceqfpUtilOutputPriorityPktRate")

                self.ceqfputiloutputtotalbitrate = YLeaf(YType.uint64, "ceqfpUtilOutputTotalBitRate")

                self.ceqfputiloutputtotalpktrate = YLeaf(YType.uint64, "ceqfpUtilOutputTotalPktRate")

                self.ceqfputilprocessingload = YLeaf(YType.uint32, "ceqfpUtilProcessingLoad")
                self._segment_path = lambda: "ceqfpUtilizationEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[ceqfpUtilTimeInterval='" + self.ceqfputiltimeinterval.get() + "']"
                self._absolute_path = lambda: "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/ceqfpUtilizationTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENTITYQFPMIB.Ceqfputilizationtable.Ceqfputilizationentry, ['entphysicalindex', 'ceqfputiltimeinterval', 'ceqfputilinputnonprioritybitrate', 'ceqfputilinputnonprioritypktrate', 'ceqfputilinputprioritybitrate', 'ceqfputilinputprioritypktrate', 'ceqfputilinputtotalbitrate', 'ceqfputilinputtotalpktrate', 'ceqfputiloutputnonprioritybitrate', 'ceqfputiloutputnonprioritypktrate', 'ceqfputiloutputprioritybitrate', 'ceqfputiloutputprioritypktrate', 'ceqfputiloutputtotalbitrate', 'ceqfputiloutputtotalpktrate', 'ceqfputilprocessingload'], name, value)


    class Ciscoentityqfp(Entity):
        """
        
        
        .. attribute:: ceqfpfiveminutesutilalgo
        
        	This objects represents the method used to calculate 5 Minutes interval utilization data. The enumerated values are described below.  unknown    (1) \- The calculation method is unknown fiveSecSMA (2) \- The value is calculated using Simple Moving                    Average of last 60 five seconds utilization                  data
        	**type**\:   :py:class:`Ceqfpfiveminutesutilalgo <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.Ciscoentityqfp.Ceqfpfiveminutesutilalgo>`
        
        .. attribute:: ceqfpfivesecondutilalgo
        
        	This objects represents the method used to calculate 5 Second interval utilization data. The enumerated values are described below.  unknown       (1) \- The calculation method is unknown fiveSecSample (2) \- The value is calculated based on the last                     5 second sampling period of utilization                     data
        	**type**\:   :py:class:`Ceqfpfivesecondutilalgo <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.Ciscoentityqfp.Ceqfpfivesecondutilalgo>`
        
        .. attribute:: ceqfponeminuteutilalgo
        
        	This objects represents the method used to calculate 1 Minute interval utilization data. The enumerated values are described below.  unknown    (1) \- The calculation method is unknown fiveSecSMA (2) \- The value is calculated using Simple Moving                    Average of last 12 five seconds utilization                  data
        	**type**\:   :py:class:`Ceqfponeminuteutilalgo <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.Ciscoentityqfp.Ceqfponeminuteutilalgo>`
        
        .. attribute:: ceqfpsixtyminutesutilalgo
        
        	This objects represents the method used to calculate 60 Minutes interval utilization data. The enumerated values are described below.  unknown    (1) \- The calculation method is unknown fiveSecSMA (1) \- The value is calculated using Simple Moving                    Average of last 720 five seconds utilization                  data
        	**type**\:   :py:class:`Ceqfpsixtyminutesutilalgo <ydk.models.cisco_ios_xe.CISCO_ENTITY_QFP_MIB.CISCOENTITYQFPMIB.Ciscoentityqfp.Ceqfpsixtyminutesutilalgo>`
        
        

        """

        _prefix = 'CISCO-ENTITY-QFP-MIB'
        _revision = '2014-06-18'

        def __init__(self):
            super(CISCOENTITYQFPMIB.Ciscoentityqfp, self).__init__()

            self.yang_name = "ciscoEntityQfp"
            self.yang_parent_name = "CISCO-ENTITY-QFP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.ceqfpfiveminutesutilalgo = YLeaf(YType.enumeration, "ceqfpFiveMinutesUtilAlgo")

            self.ceqfpfivesecondutilalgo = YLeaf(YType.enumeration, "ceqfpFiveSecondUtilAlgo")

            self.ceqfponeminuteutilalgo = YLeaf(YType.enumeration, "ceqfpOneMinuteUtilAlgo")

            self.ceqfpsixtyminutesutilalgo = YLeaf(YType.enumeration, "ceqfpSixtyMinutesUtilAlgo")
            self._segment_path = lambda: "ciscoEntityQfp"
            self._absolute_path = lambda: "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYQFPMIB.Ciscoentityqfp, ['ceqfpfiveminutesutilalgo', 'ceqfpfivesecondutilalgo', 'ceqfponeminuteutilalgo', 'ceqfpsixtyminutesutilalgo'], name, value)

        class Ceqfpfiveminutesutilalgo(Enum):
            """
            Ceqfpfiveminutesutilalgo

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

            unknown = Enum.YLeaf(1, "unknown")

            fiveSecSMA = Enum.YLeaf(2, "fiveSecSMA")


        class Ceqfpfivesecondutilalgo(Enum):
            """
            Ceqfpfivesecondutilalgo

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

            unknown = Enum.YLeaf(1, "unknown")

            fiveSecSample = Enum.YLeaf(2, "fiveSecSample")


        class Ceqfponeminuteutilalgo(Enum):
            """
            Ceqfponeminuteutilalgo

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

            unknown = Enum.YLeaf(1, "unknown")

            fiveSecSMA = Enum.YLeaf(2, "fiveSecSMA")


        class Ceqfpsixtyminutesutilalgo(Enum):
            """
            Ceqfpsixtyminutesutilalgo

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

            unknown = Enum.YLeaf(1, "unknown")

            fiveSecSMA = Enum.YLeaf(2, "fiveSecSMA")



    class Ciscoentityqfpnotif(Entity):
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
            super(CISCOENTITYQFPMIB.Ciscoentityqfpnotif, self).__init__()

            self.yang_name = "ciscoEntityQfpNotif"
            self.yang_parent_name = "CISCO-ENTITY-QFP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.ceqfpmemoryresthreshnotifenabled = YLeaf(YType.boolean, "ceqfpMemoryResThreshNotifEnabled")

            self.ceqfpthroughputnotifenabled = YLeaf(YType.uint32, "ceqfpThroughputNotifEnabled")
            self._segment_path = lambda: "ciscoEntityQfpNotif"
            self._absolute_path = lambda: "CISCO-ENTITY-QFP-MIB:CISCO-ENTITY-QFP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENTITYQFPMIB.Ciscoentityqfpnotif, ['ceqfpmemoryresthreshnotifenabled', 'ceqfpthroughputnotifenabled'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOENTITYQFPMIB()
        return self._top_entity

