""" CISCO_CEF_MIB 

Cisco Express Forwarding (CEF) describes a high speed 
switching mechanism that a router uses to forward packets
from the inbound to the outbound interface. 

CEF uses two sets of data structures
or tables, which it stores in router memory\:

Forwarding information base (FIB) \- Describes a database
of information used to make forwarding decisions. It is 
conceptually similar to a routing table or route\-cache, 
although its implementation is different.

Adjacency \- Two nodes in the network are said to be 
adjacent if they can reach each other via a single hop 
across a link layer.           

CEF path is a valid route to reach to a destination 
IP prefix. Multiple paths may exist out of a router to the 
same destination prefix. CEF Load balancing capability 
share the traffic to the destination IP prefix over all 
the active paths. 

After obtaining the prefix in the CEF table with the
longest match, output forwarding follows the chain of 
forwarding elements. 

Forwarding element (FE) may process the packet, forward 
the packet, drop or punt the packet or it may also
pass the packet to the next forwarding element in the 
chain for further processing.

Forwarding Elements are of various types
but this MIB only represents the forwarding elements of
adjacency and label types. Hence a forwarding element 
chain will be represented as a list of labels and
adjacency. The adjacency may point to a forwarding element
list again, if it is not the last forwarding element in this
chain. 

For the simplest IP forwarding case, the prefix entry will 
point at an adjacency forwarding element.
The IP adjacency processing function will apply the output
features, add the encapsulation (performing any required 
fixups), and may send the packet out.

If loadbalancing is configured, the prefix entry will point 
to lists of forwarding elements. One of these lists will be 
selected to forward the packet. 

Each forwarding element list dictates which of a set of 
possible packet transformations to apply on the way to 
the same neighbour. 

The following diagram represents relationship
between three of the core tables in this MIB module.

 cefPrefixTable             cefFESelectionTable

 +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+  points           +\-\-\-\-\-\-\-\-\-\-\-\-\-\-+   
 \|   \|     \|     \|  a set     +\-\-\-\-> \|   \|   \|   \|  \| 
 \|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|  of FE     \|      \|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|   
 \|   \|     \|     \|  Selection \|      \|   \|   \|   \|  \|
 \|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|  Entries   \|      \|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|    
 \|   \|     \|     \|\-\-\-\-\-\-\-\-\-\-\-\-+      \|              \|<\-\-\-\-+ 
 \|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|                   \|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|     \|
 \|               \|    +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|   \|   \|   \|  \|     \|
 +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+    \|              +\-\-\-\-\-\-\-\-\-\-\-\-\-\-+     \|
                      \|                                   \|
                points to an                              \|
                adjacency entry                           \|
                      \|                                   \|
                      \|   cefAdjTable                     \|
                      \|  +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+  may point     \|
                      +\->\|   \|     \|     \|  to a set      \|
                         \|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|  of FE         \|
                         \|   \|     \|     \|  Selection     \|
                         \|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\|  Entries       \| 
                         \|   \|     \|     \|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
                         \|\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\| 
                         \|               \| 
                         +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+ 

Some of the Cisco series routers (e.g. 7500 & 12000) 
support distributed CEF (dCEF), in which the line cards 
(LCs) make the packet forwarding decisions using locally 
stored copies of the same Forwarding information base (FIB)
and adjacency tables as the Routing Processor (RP).
          
Inter\-Process Communication (IPC) is the protocol used 
by routers that support distributed packet forwarding. 
CEF updates are encoded as external Data Representation 
(XDR) information elements inside IPC messages. 
         
This MIB reflects the distributed nature of CEF, e.g. CEF
has different instances running on the RP and the line cards.

There may be instances of inconsistency between the
CEF forwarding databases(i.e between CEF forwarding 
database on line cards and the CEF forwarding database
on the RP). CEF consistency checkers (CC) detects 
this inconsistency.

When two databases are compared by a consistency checker, 
a set of records from the first (master) database is 
looked up in the second (slave).

There are two types of consistency checkers, 
active and passive. Active consistency checkers 
are invoked in response to some stimulus, i.e. 
when a packet cannot be forwarded because the 
prefix is not in the forwarding table or 
in response to a Management Station request.

Passive consistency checkers operate in the background, 
scanning portions of the databases on a periodic basis.

The full\-scan checkers are active consistency checkers
which are invoked in response to a Management Station
Request.

If 64\-bit counter objects in this MIB are supported,
then their associated 32\-bit counter objects 
must also be supported. The 32\-bit counters will
report the low 32\-bits of the associated 64\-bit 
counter count (e.g., cefPrefixPkts will report the 
least significant 32 bits of cefPrefixHCPkts).
The same rule should be applied for the 64\-bit gauge
objects and their assocaited 32\-bit gauge objects.

If 64\-bit counters in this MIB are not supported,
then an agent MUST NOT instantiate the corresponding
objects with an incorrect value; rather, it MUST 
respond with the appropriate error/exception 
condition (e.g., noSuchInstance or noSuchName). 

Counters related to CEF accounting (e.g.,
cefPrefixPkts) MUST NOT be instantiated if the
corresponding accounting method has been disabled.  
 
This MIB allows configuration and monitoring of CEF 
related objects.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOCEFMIB(Entity):
    """
    
    
    .. attribute:: ceffib
    
    	
    	**type**\:  :py:class:`CefFIB <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefFIB>`
    
    	**config**\: False
    
    .. attribute:: cefcc
    
    	
    	**type**\:  :py:class:`CefCC <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefCC>`
    
    	**config**\: False
    
    .. attribute:: cefnotifcntl
    
    	
    	**type**\:  :py:class:`CefNotifCntl <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefNotifCntl>`
    
    	**config**\: False
    
    .. attribute:: ceffibsummarytable
    
    	This table contains the summary information for the cefPrefixTable
    	**type**\:  :py:class:`CefFIBSummaryTable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefFIBSummaryTable>`
    
    	**config**\: False
    
    .. attribute:: cefprefixtable
    
    	A list of CEF forwarding prefixes
    	**type**\:  :py:class:`CefPrefixTable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefPrefixTable>`
    
    	**config**\: False
    
    .. attribute:: ceflmprefixtable
    
    	A table of Longest Match Prefix Query requests.  Generator application should utilize the cefLMPrefixSpinLock to try to avoid collisions. See DESCRIPTION clause of cefLMPrefixSpinLock
    	**type**\:  :py:class:`CefLMPrefixTable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefLMPrefixTable>`
    
    	**config**\: False
    
    .. attribute:: cefpathtable
    
    	CEF prefix path is a valid route to reach to a  destination IP prefix. Multiple paths may exist  out of a router to the same destination prefix.  This table specify lists of CEF paths
    	**type**\:  :py:class:`CefPathTable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefPathTable>`
    
    	**config**\: False
    
    .. attribute:: cefadjsummarytable
    
    	This table contains the summary information for the cefAdjTable
    	**type**\:  :py:class:`CefAdjSummaryTable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefAdjSummaryTable>`
    
    	**config**\: False
    
    .. attribute:: cefadjtable
    
    	A list of CEF adjacencies
    	**type**\:  :py:class:`CefAdjTable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefAdjTable>`
    
    	**config**\: False
    
    .. attribute:: ceffeselectiontable
    
    	A list of forwarding element selection entries
    	**type**\:  :py:class:`CefFESelectionTable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefFESelectionTable>`
    
    	**config**\: False
    
    .. attribute:: cefcfgtable
    
    	This table contains global config parameter  of CEF on the Managed device
    	**type**\:  :py:class:`CefCfgTable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefCfgTable>`
    
    	**config**\: False
    
    .. attribute:: cefresourcetable
    
    	This table contains global resource  information of CEF on the Managed device
    	**type**\:  :py:class:`CefResourceTable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefResourceTable>`
    
    	**config**\: False
    
    .. attribute:: cefinttable
    
    	This Table contains interface specific information of CEF on the Managed device
    	**type**\:  :py:class:`CefIntTable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefIntTable>`
    
    	**config**\: False
    
    .. attribute:: cefpeertable
    
    	Entity acting as RP (Routing Processor) keeps the CEF states for the line card entities and communicates with the line card entities using XDR. This Table contains the CEF information  related to peer entities on the managed device
    	**type**\:  :py:class:`CefPeerTable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefPeerTable>`
    
    	**config**\: False
    
    .. attribute:: cefpeerfibtable
    
    	Entity acting as RP (Routing Processor) keep the CEF FIB states for the line card entities and communicate with the line card entities using XDR. This Table contains the CEF FIB State  related to peer entities on the managed device
    	**type**\:  :py:class:`CefPeerFIBTable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefPeerFIBTable>`
    
    	**config**\: False
    
    .. attribute:: cefccglobaltable
    
    	This table contains CEF consistency checker (CC) global parameters for the managed device
    	**type**\:  :py:class:`CefCCGlobalTable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefCCGlobalTable>`
    
    	**config**\: False
    
    .. attribute:: cefcctypetable
    
    	This table contains CEF consistency checker types specific parameters on the managed device.  All detected inconsistency are signaled to the Management Station via cefInconsistencyDetection notification
    	**type**\:  :py:class:`CefCCTypeTable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefCCTypeTable>`
    
    	**config**\: False
    
    .. attribute:: cefinconsistencyrecordtable
    
    	This table contains CEF inconsistency records
    	**type**\:  :py:class:`CefInconsistencyRecordTable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefInconsistencyRecordTable>`
    
    	**config**\: False
    
    .. attribute:: cefstatsprefixlentable
    
    	This table specifies the CEF stats based on the Prefix Length
    	**type**\:  :py:class:`CefStatsPrefixLenTable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefStatsPrefixLenTable>`
    
    	**config**\: False
    
    .. attribute:: cefswitchingstatstable
    
    	This table specifies the CEF switch stats
    	**type**\:  :py:class:`CefSwitchingStatsTable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefSwitchingStatsTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-CEF-MIB'
    _revision = '2006-01-30'

    def __init__(self):
        super(CISCOCEFMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-CEF-MIB"
        self.yang_parent_name = "CISCO-CEF-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cefFIB", ("ceffib", CISCOCEFMIB.CefFIB)), ("cefCC", ("cefcc", CISCOCEFMIB.CefCC)), ("cefNotifCntl", ("cefnotifcntl", CISCOCEFMIB.CefNotifCntl)), ("cefFIBSummaryTable", ("ceffibsummarytable", CISCOCEFMIB.CefFIBSummaryTable)), ("cefPrefixTable", ("cefprefixtable", CISCOCEFMIB.CefPrefixTable)), ("cefLMPrefixTable", ("ceflmprefixtable", CISCOCEFMIB.CefLMPrefixTable)), ("cefPathTable", ("cefpathtable", CISCOCEFMIB.CefPathTable)), ("cefAdjSummaryTable", ("cefadjsummarytable", CISCOCEFMIB.CefAdjSummaryTable)), ("cefAdjTable", ("cefadjtable", CISCOCEFMIB.CefAdjTable)), ("cefFESelectionTable", ("ceffeselectiontable", CISCOCEFMIB.CefFESelectionTable)), ("cefCfgTable", ("cefcfgtable", CISCOCEFMIB.CefCfgTable)), ("cefResourceTable", ("cefresourcetable", CISCOCEFMIB.CefResourceTable)), ("cefIntTable", ("cefinttable", CISCOCEFMIB.CefIntTable)), ("cefPeerTable", ("cefpeertable", CISCOCEFMIB.CefPeerTable)), ("cefPeerFIBTable", ("cefpeerfibtable", CISCOCEFMIB.CefPeerFIBTable)), ("cefCCGlobalTable", ("cefccglobaltable", CISCOCEFMIB.CefCCGlobalTable)), ("cefCCTypeTable", ("cefcctypetable", CISCOCEFMIB.CefCCTypeTable)), ("cefInconsistencyRecordTable", ("cefinconsistencyrecordtable", CISCOCEFMIB.CefInconsistencyRecordTable)), ("cefStatsPrefixLenTable", ("cefstatsprefixlentable", CISCOCEFMIB.CefStatsPrefixLenTable)), ("cefSwitchingStatsTable", ("cefswitchingstatstable", CISCOCEFMIB.CefSwitchingStatsTable))])
        self._leafs = OrderedDict()

        self.ceffib = CISCOCEFMIB.CefFIB()
        self.ceffib.parent = self
        self._children_name_map["ceffib"] = "cefFIB"

        self.cefcc = CISCOCEFMIB.CefCC()
        self.cefcc.parent = self
        self._children_name_map["cefcc"] = "cefCC"

        self.cefnotifcntl = CISCOCEFMIB.CefNotifCntl()
        self.cefnotifcntl.parent = self
        self._children_name_map["cefnotifcntl"] = "cefNotifCntl"

        self.ceffibsummarytable = CISCOCEFMIB.CefFIBSummaryTable()
        self.ceffibsummarytable.parent = self
        self._children_name_map["ceffibsummarytable"] = "cefFIBSummaryTable"

        self.cefprefixtable = CISCOCEFMIB.CefPrefixTable()
        self.cefprefixtable.parent = self
        self._children_name_map["cefprefixtable"] = "cefPrefixTable"

        self.ceflmprefixtable = CISCOCEFMIB.CefLMPrefixTable()
        self.ceflmprefixtable.parent = self
        self._children_name_map["ceflmprefixtable"] = "cefLMPrefixTable"

        self.cefpathtable = CISCOCEFMIB.CefPathTable()
        self.cefpathtable.parent = self
        self._children_name_map["cefpathtable"] = "cefPathTable"

        self.cefadjsummarytable = CISCOCEFMIB.CefAdjSummaryTable()
        self.cefadjsummarytable.parent = self
        self._children_name_map["cefadjsummarytable"] = "cefAdjSummaryTable"

        self.cefadjtable = CISCOCEFMIB.CefAdjTable()
        self.cefadjtable.parent = self
        self._children_name_map["cefadjtable"] = "cefAdjTable"

        self.ceffeselectiontable = CISCOCEFMIB.CefFESelectionTable()
        self.ceffeselectiontable.parent = self
        self._children_name_map["ceffeselectiontable"] = "cefFESelectionTable"

        self.cefcfgtable = CISCOCEFMIB.CefCfgTable()
        self.cefcfgtable.parent = self
        self._children_name_map["cefcfgtable"] = "cefCfgTable"

        self.cefresourcetable = CISCOCEFMIB.CefResourceTable()
        self.cefresourcetable.parent = self
        self._children_name_map["cefresourcetable"] = "cefResourceTable"

        self.cefinttable = CISCOCEFMIB.CefIntTable()
        self.cefinttable.parent = self
        self._children_name_map["cefinttable"] = "cefIntTable"

        self.cefpeertable = CISCOCEFMIB.CefPeerTable()
        self.cefpeertable.parent = self
        self._children_name_map["cefpeertable"] = "cefPeerTable"

        self.cefpeerfibtable = CISCOCEFMIB.CefPeerFIBTable()
        self.cefpeerfibtable.parent = self
        self._children_name_map["cefpeerfibtable"] = "cefPeerFIBTable"

        self.cefccglobaltable = CISCOCEFMIB.CefCCGlobalTable()
        self.cefccglobaltable.parent = self
        self._children_name_map["cefccglobaltable"] = "cefCCGlobalTable"

        self.cefcctypetable = CISCOCEFMIB.CefCCTypeTable()
        self.cefcctypetable.parent = self
        self._children_name_map["cefcctypetable"] = "cefCCTypeTable"

        self.cefinconsistencyrecordtable = CISCOCEFMIB.CefInconsistencyRecordTable()
        self.cefinconsistencyrecordtable.parent = self
        self._children_name_map["cefinconsistencyrecordtable"] = "cefInconsistencyRecordTable"

        self.cefstatsprefixlentable = CISCOCEFMIB.CefStatsPrefixLenTable()
        self.cefstatsprefixlentable.parent = self
        self._children_name_map["cefstatsprefixlentable"] = "cefStatsPrefixLenTable"

        self.cefswitchingstatstable = CISCOCEFMIB.CefSwitchingStatsTable()
        self.cefswitchingstatstable.parent = self
        self._children_name_map["cefswitchingstatstable"] = "cefSwitchingStatsTable"
        self._segment_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOCEFMIB, [], name, value)


    class CefFIB(Entity):
        """
        
        
        .. attribute:: ceflmprefixspinlock
        
        	An advisory lock used to allow cooperating SNMP Command Generator applications to coordinate their use of the Set operation in creating Longest Match Prefix Entries in cefLMPrefixTable.  When creating a new longest prefix match entry, the value of cefLMPrefixSpinLock should be retrieved.   The destination address should be determined to be unique by the SNMP Command Generator application by consulting the cefLMPrefixTable. Finally, the longest  prefix entry may be created (Set), including the advisory lock.         If another SNMP Command Generator application has altered the longest prefix entry in the meantime,  then the spin lock's value will have changed,  and so this creation will fail because it will specify the wrong value for the spin lock.  Since this is an advisory lock, the use of this lock is not enforced, but not using this lock may lead to conflict with the another SNMP command responder  application which may also be acting on the cefLMPrefixTable
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefFIB, self).__init__()

            self.yang_name = "cefFIB"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ceflmprefixspinlock', (YLeaf(YType.int32, 'cefLMPrefixSpinLock'), ['int'])),
            ])
            self.ceflmprefixspinlock = None
            self._segment_path = lambda: "cefFIB"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefFIB, ['ceflmprefixspinlock'], name, value)



    class CefCC(Entity):
        """
        
        
        .. attribute:: entlastinconsistencydetecttime
        
        	The value of sysUpTime at the time an inconsistency is detecetd
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: cefinconsistencyreset
        
        	Setting the value of this object to ccActionStart(1) will reset all the active consistency checkers.  The Management station should poll the  cefInconsistencyResetStatus object to get the  state of inconsistency reset operation.  This operation once started, cannot be aborted. Hence, the value of this object cannot be set to ccActionAbort(2).  The value of this object can't be set to ccActionStart(1),  if the value of object cefInconsistencyResetStatus is ccStatusRunning(2)
        	**type**\:  :py:class:`CefCCAction <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefCCAction>`
        
        	**config**\: False
        
        .. attribute:: cefinconsistencyresetstatus
        
        	Indicates the status of the consistency reset request
        	**type**\:  :py:class:`CefCCStatus <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefCCStatus>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefCC, self).__init__()

            self.yang_name = "cefCC"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('entlastinconsistencydetecttime', (YLeaf(YType.uint32, 'entLastInconsistencyDetectTime'), ['int'])),
                ('cefinconsistencyreset', (YLeaf(YType.enumeration, 'cefInconsistencyReset'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefCCAction', '')])),
                ('cefinconsistencyresetstatus', (YLeaf(YType.enumeration, 'cefInconsistencyResetStatus'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefCCStatus', '')])),
            ])
            self.entlastinconsistencydetecttime = None
            self.cefinconsistencyreset = None
            self.cefinconsistencyresetstatus = None
            self._segment_path = lambda: "cefCC"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefCC, ['entlastinconsistencydetecttime', 'cefinconsistencyreset', 'cefinconsistencyresetstatus'], name, value)



    class CefNotifCntl(Entity):
        """
        
        
        .. attribute:: cefresourcefailurenotifenable
        
        	Indicates whether or not a notification should be generated on the detection of CEF resource Failure
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: cefpeerstatechangenotifenable
        
        	Indicates whether or not a notification should be generated on the detection of CEF peer state change
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: cefpeerfibstatechangenotifenable
        
        	Indicates whether or not a notification should be generated on the detection of CEF FIB peer state change
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: cefnotifthrottlinginterval
        
        	This object controls the generation of the cefInconsistencyDetection notification.  If this object has a value of zero, then the throttle control is disabled.  If this object has a non\-zero value, then the agent must not generate more than one  cefInconsistencyDetection 'notification\-event' in the  indicated period, where a 'notification\-event' is the transmission of a single trap or inform PDU to a list of notification destinations.  If additional inconsistency is detected within the  throttling period, then notification\-events for these inconsistencies should be suppressed by the agent until the current throttling period expires.  At the end of a throttling period, one notification\-event should be generated if any inconsistency was detected since the start of the  throttling period. In such a case,  another throttling period is started right away.  An NMS should periodically poll cefInconsistencyRecordTable to detect any missed cefInconsistencyDetection notification\-events, e.g., due to throttling or transmission loss.   If cefNotifThrottlingInterval notification generation is enabled, the suggested default throttling period is 60 seconds, but generation of the cefInconsistencyDetection notification should be disabled by default.  If the agent is capable of storing non\-volatile configuration, then the value of this object must be restored after a re\-initialization of the management system.  The actual transmission of notifications is controlled via the MIB modules in RFC 3413
        	**type**\: int
        
        	**range:** 0..3600
        
        	**config**\: False
        
        	**units**\: seconds
        
        .. attribute:: cefinconsistencynotifenable
        
        	Indicates whether cefInconsistencyDetection notification should be generated for this managed device
        	**type**\: bool
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefNotifCntl, self).__init__()

            self.yang_name = "cefNotifCntl"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cefresourcefailurenotifenable', (YLeaf(YType.boolean, 'cefResourceFailureNotifEnable'), ['bool'])),
                ('cefpeerstatechangenotifenable', (YLeaf(YType.boolean, 'cefPeerStateChangeNotifEnable'), ['bool'])),
                ('cefpeerfibstatechangenotifenable', (YLeaf(YType.boolean, 'cefPeerFIBStateChangeNotifEnable'), ['bool'])),
                ('cefnotifthrottlinginterval', (YLeaf(YType.int32, 'cefNotifThrottlingInterval'), ['int'])),
                ('cefinconsistencynotifenable', (YLeaf(YType.boolean, 'cefInconsistencyNotifEnable'), ['bool'])),
            ])
            self.cefresourcefailurenotifenable = None
            self.cefpeerstatechangenotifenable = None
            self.cefpeerfibstatechangenotifenable = None
            self.cefnotifthrottlinginterval = None
            self.cefinconsistencynotifenable = None
            self._segment_path = lambda: "cefNotifCntl"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefNotifCntl, ['cefresourcefailurenotifenable', 'cefpeerstatechangenotifenable', 'cefpeerfibstatechangenotifenable', 'cefnotifthrottlinginterval', 'cefinconsistencynotifenable'], name, value)



    class CefFIBSummaryTable(Entity):
        """
        This table contains the summary information
        for the cefPrefixTable.
        
        .. attribute:: ceffibsummaryentry
        
        	If CEF is enabled on the Managed device, each entry contains the FIB summary related attributes for the managed entity.  A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`CefFIBSummaryEntry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefFIBSummaryTable.CefFIBSummaryEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefFIBSummaryTable, self).__init__()

            self.yang_name = "cefFIBSummaryTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefFIBSummaryEntry", ("ceffibsummaryentry", CISCOCEFMIB.CefFIBSummaryTable.CefFIBSummaryEntry))])
            self._leafs = OrderedDict()

            self.ceffibsummaryentry = YList(self)
            self._segment_path = lambda: "cefFIBSummaryTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefFIBSummaryTable, [], name, value)


        class CefFIBSummaryEntry(Entity):
            """
            If CEF is enabled on the Managed device,
            each entry contains the FIB summary related
            attributes for the managed entity.
            
            A row may exist for each IP version type
            (v4 and v6) depending upon the IP version
            supported on the device.
            
            entPhysicalIndex is also an index for this
            table which represents entities of
            'module' entPhysicalClass which are capable
            of running CEF.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: ceffibipversion  (key)
            
            	The version of IP forwarding
            	**type**\:  :py:class:`CefIpVersion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefIpVersion>`
            
            	**config**\: False
            
            .. attribute:: ceffibsummaryfwdprefixes
            
            	Total number of forwarding Prefixes in FIB for the IP version specified by cefFIBIpVersion object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.CefFIBSummaryTable.CefFIBSummaryEntry, self).__init__()

                self.yang_name = "cefFIBSummaryEntry"
                self.yang_parent_name = "cefFIBSummaryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','ceffibipversion']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('ceffibipversion', (YLeaf(YType.enumeration, 'cefFIBIpVersion'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefIpVersion', '')])),
                    ('ceffibsummaryfwdprefixes', (YLeaf(YType.uint32, 'cefFIBSummaryFwdPrefixes'), ['int'])),
                ])
                self.entphysicalindex = None
                self.ceffibipversion = None
                self.ceffibsummaryfwdprefixes = None
                self._segment_path = lambda: "cefFIBSummaryEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefFIBIpVersion='" + str(self.ceffibipversion) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefFIBSummaryTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.CefFIBSummaryTable.CefFIBSummaryEntry, ['entphysicalindex', 'ceffibipversion', 'ceffibsummaryfwdprefixes'], name, value)




    class CefPrefixTable(Entity):
        """
        A list of CEF forwarding prefixes.
        
        .. attribute:: cefprefixentry
        
        	If CEF is enabled on the Managed device, each entry contains the forwarding  prefix attributes.   CEF prefix based non\-recursive stats are maintained in internal and external buckets (depending upon the  value of cefIntNonrecursiveAccouting object in the  CefIntEntry).  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`CefPrefixEntry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefPrefixTable.CefPrefixEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefPrefixTable, self).__init__()

            self.yang_name = "cefPrefixTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefPrefixEntry", ("cefprefixentry", CISCOCEFMIB.CefPrefixTable.CefPrefixEntry))])
            self._leafs = OrderedDict()

            self.cefprefixentry = YList(self)
            self._segment_path = lambda: "cefPrefixTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefPrefixTable, [], name, value)


        class CefPrefixEntry(Entity):
            """
            If CEF is enabled on the Managed device,
            each entry contains the forwarding 
            prefix attributes. 
            
            CEF prefix based non\-recursive stats are maintained
            in internal and external buckets (depending upon the 
            value of cefIntNonrecursiveAccouting object in the 
            CefIntEntry).
            
            entPhysicalIndex is also an index for this
            table which represents entities of
            'module' entPhysicalClass which are capable
            of running CEF.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: cefprefixtype  (key)
            
            	The Network Prefix Type. This object specifies the address type used for cefPrefixAddr.  Prefix entries are only valid for the address type of ipv4(1) and ipv6(2)
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cefprefixaddr  (key)
            
            	The Network Prefix Address. The type of this address is determined by the value of the cefPrefixType object. This object is a Prefix Address containing the  prefix with length specified by cefPrefixLen.  Any bits beyond the length specified by cefPrefixLen are zeroed
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cefprefixlen  (key)
            
            	Length in bits of the FIB Address prefix
            	**type**\: int
            
            	**range:** 0..2040
            
            	**config**\: False
            
            .. attribute:: cefprefixforwardinginfo
            
            	This object indicates the associated forwarding element selection entries in cefFESelectionTable. The value of this object is index value (cefFESelectionName) of cefFESelectionTable
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cefprefixpkts
            
            	If CEF accounting is set to enable per prefix accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'perPrefix'  accounting), then this object represents the  number of packets switched to this prefix
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cefprefixhcpkts
            
            	If CEF accounting is set to enable per prefix accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'perPrefix'  accounting), then this object represents the  number of packets switched to this prefix.   This object is a 64\-bit version of  cefPrefixPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cefprefixbytes
            
            	If CEF accounting is set to enable per prefix accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'perPrefix'  accounting), then this object represents the  number of bytes switched to this prefix
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cefprefixhcbytes
            
            	If CEF accounting is set to enable per prefix accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'perPrefix'  accounting), then this object represents the  number of bytes switched to this prefix.  This object is a 64\-bit version of  cefPrefixBytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cefprefixinternalnrpkts
            
            	If CEF accounting is set to enable non\-recursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents the number of non\-recursive packets in the internal bucket switched using this prefix
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cefprefixinternalnrhcpkts
            
            	If CEF accounting is set to enable non\-recursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents the number of non\-recursive packets in the internal bucket switched using this prefix.  This object is a 64\-bit version of  cefPrefixInternalNRPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cefprefixinternalnrbytes
            
            	If CEF accounting is set to enable nonRecursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents  the number of non\-recursive bytes in the internal bucket switched using this prefix
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cefprefixinternalnrhcbytes
            
            	If CEF accounting is set to enable nonRecursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents  the number of non\-recursive bytes in the internal bucket switched using this prefix.  This object is a 64\-bit version of  cefPrefixInternalNRBytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cefprefixexternalnrpkts
            
            	If CEF accounting is set to enable non\-recursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents the number of non\-recursive packets in the external bucket switched using this prefix
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cefprefixexternalnrhcpkts
            
            	If CEF accounting is set to enable non\-recursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents the number of non\-recursive packets in the external bucket switched using this prefix.  This object is a 64\-bit version of  cefPrefixExternalNRPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cefprefixexternalnrbytes
            
            	If CEF accounting is set to enable nonRecursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents  the number of non\-recursive bytes in the external bucket switched using this prefix
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cefprefixexternalnrhcbytes
            
            	If CEF accounting is set to enable nonRecursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents  the number of non\-recursive bytes in the external bucket switched using this prefix.  This object is a 64\-bit version of  cefPrefixExternalNRBytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.CefPrefixTable.CefPrefixEntry, self).__init__()

                self.yang_name = "cefPrefixEntry"
                self.yang_parent_name = "cefPrefixTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cefprefixtype','cefprefixaddr','cefprefixlen']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefprefixtype', (YLeaf(YType.enumeration, 'cefPrefixType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cefprefixaddr', (YLeaf(YType.str, 'cefPrefixAddr'), ['str'])),
                    ('cefprefixlen', (YLeaf(YType.uint32, 'cefPrefixLen'), ['int'])),
                    ('cefprefixforwardinginfo', (YLeaf(YType.str, 'cefPrefixForwardingInfo'), ['str'])),
                    ('cefprefixpkts', (YLeaf(YType.uint32, 'cefPrefixPkts'), ['int'])),
                    ('cefprefixhcpkts', (YLeaf(YType.uint64, 'cefPrefixHCPkts'), ['int'])),
                    ('cefprefixbytes', (YLeaf(YType.uint32, 'cefPrefixBytes'), ['int'])),
                    ('cefprefixhcbytes', (YLeaf(YType.uint64, 'cefPrefixHCBytes'), ['int'])),
                    ('cefprefixinternalnrpkts', (YLeaf(YType.uint32, 'cefPrefixInternalNRPkts'), ['int'])),
                    ('cefprefixinternalnrhcpkts', (YLeaf(YType.uint64, 'cefPrefixInternalNRHCPkts'), ['int'])),
                    ('cefprefixinternalnrbytes', (YLeaf(YType.uint32, 'cefPrefixInternalNRBytes'), ['int'])),
                    ('cefprefixinternalnrhcbytes', (YLeaf(YType.uint64, 'cefPrefixInternalNRHCBytes'), ['int'])),
                    ('cefprefixexternalnrpkts', (YLeaf(YType.uint32, 'cefPrefixExternalNRPkts'), ['int'])),
                    ('cefprefixexternalnrhcpkts', (YLeaf(YType.uint64, 'cefPrefixExternalNRHCPkts'), ['int'])),
                    ('cefprefixexternalnrbytes', (YLeaf(YType.uint32, 'cefPrefixExternalNRBytes'), ['int'])),
                    ('cefprefixexternalnrhcbytes', (YLeaf(YType.uint64, 'cefPrefixExternalNRHCBytes'), ['int'])),
                ])
                self.entphysicalindex = None
                self.cefprefixtype = None
                self.cefprefixaddr = None
                self.cefprefixlen = None
                self.cefprefixforwardinginfo = None
                self.cefprefixpkts = None
                self.cefprefixhcpkts = None
                self.cefprefixbytes = None
                self.cefprefixhcbytes = None
                self.cefprefixinternalnrpkts = None
                self.cefprefixinternalnrhcpkts = None
                self.cefprefixinternalnrbytes = None
                self.cefprefixinternalnrhcbytes = None
                self.cefprefixexternalnrpkts = None
                self.cefprefixexternalnrhcpkts = None
                self.cefprefixexternalnrbytes = None
                self.cefprefixexternalnrhcbytes = None
                self._segment_path = lambda: "cefPrefixEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefPrefixType='" + str(self.cefprefixtype) + "']" + "[cefPrefixAddr='" + str(self.cefprefixaddr) + "']" + "[cefPrefixLen='" + str(self.cefprefixlen) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefPrefixTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.CefPrefixTable.CefPrefixEntry, ['entphysicalindex', 'cefprefixtype', 'cefprefixaddr', 'cefprefixlen', 'cefprefixforwardinginfo', 'cefprefixpkts', 'cefprefixhcpkts', 'cefprefixbytes', 'cefprefixhcbytes', 'cefprefixinternalnrpkts', 'cefprefixinternalnrhcpkts', 'cefprefixinternalnrbytes', 'cefprefixinternalnrhcbytes', 'cefprefixexternalnrpkts', 'cefprefixexternalnrhcpkts', 'cefprefixexternalnrbytes', 'cefprefixexternalnrhcbytes'], name, value)




    class CefLMPrefixTable(Entity):
        """
        A table of Longest Match Prefix Query requests.
        
        Generator application should utilize the
        cefLMPrefixSpinLock to try to avoid collisions.
        See DESCRIPTION clause of cefLMPrefixSpinLock.
        
        .. attribute:: ceflmprefixentry
        
        	If CEF is enabled on the managed device, then each entry represents a longest Match Prefix request.  A management station wishing to get the longest Match prefix for a given destination address should create the associate instance of the row status. The row status should be set to active(1) to initiate the request. Note that  this entire procedure may be initiated via a  single set request which specifies a row status  of createAndGo(4).  Once the request completes, the management station  should retrieve the values of the objects of  interest, and should then delete the entry.  In order  to prevent old entries from clogging the table,  entries will be aged out, but an entry will never be  deleted within 5 minutes of completion. Entries are lost after an agent restart.  I.e. to find out the longest prefix match for  destination address of A.B.C.D on entity whose entityPhysicalIndex is 1, the Management station will create an entry in cefLMPrefixTable with cefLMPrefixRowStatus.1(entPhysicalIndex).1(ipv4).A.B.C.D set to createAndGo(4). Management Station may query the value of objects cefLMPrefix and cefLMPrefixLen to find out the corresponding prefix entry from the cefPrefixTable once the value of cefLMPrefixState is set to matchFound(2).  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`CefLMPrefixEntry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefLMPrefixTable.CefLMPrefixEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefLMPrefixTable, self).__init__()

            self.yang_name = "cefLMPrefixTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefLMPrefixEntry", ("ceflmprefixentry", CISCOCEFMIB.CefLMPrefixTable.CefLMPrefixEntry))])
            self._leafs = OrderedDict()

            self.ceflmprefixentry = YList(self)
            self._segment_path = lambda: "cefLMPrefixTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefLMPrefixTable, [], name, value)


        class CefLMPrefixEntry(Entity):
            """
            If CEF is enabled on the managed device, then each
            entry represents a longest Match Prefix request.
            
            A management station wishing to get the longest
            Match prefix for a given destination address
            should create the associate instance of the
            row status. The row status should be set to
            active(1) to initiate the request. Note that 
            this entire procedure may be initiated via a 
            single set request which specifies a row status 
            of createAndGo(4).
            
            Once the request completes, the management station 
            should retrieve the values of the objects of 
            interest, and should then delete the entry.  In order 
            to prevent old entries from clogging the table, 
            entries will be aged out, but an entry will never be 
            deleted within 5 minutes of completion.
            Entries are lost after an agent restart.
            
            I.e. to find out the longest prefix match for 
            destination address of A.B.C.D on entity whose
            entityPhysicalIndex is 1, the Management station
            will create an entry in cefLMPrefixTable with
            cefLMPrefixRowStatus.1(entPhysicalIndex).1(ipv4).A.B.C.D
            set to createAndGo(4). Management Station may query the
            value of objects cefLMPrefix and cefLMPrefixLen
            to find out the corresponding prefix entry from the
            cefPrefixTable once the value of cefLMPrefixState
            is set to matchFound(2).
            
            entPhysicalIndex is also an index for this
            table which represents entities of
            'module' entPhysicalClass which are capable
            of running CEF.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: ceflmprefixdestaddrtype  (key)
            
            	The Destination Address Type. This object specifies the address type used for cefLMPrefixDestAddr.  Longest Match Prefix entries are only valid  for the address type of ipv4(1) and ipv6(2)
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: ceflmprefixdestaddr  (key)
            
            	The Destination Address. The type of this address is determined by the value of the cefLMPrefixDestAddrType object
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: ceflmprefixstate
            
            	Indicates the state of this prefix search request
            	**type**\:  :py:class:`CefPrefixSearchState <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefPrefixSearchState>`
            
            	**config**\: False
            
            .. attribute:: ceflmprefixaddr
            
            	The Network Prefix Address. Index to the cefPrefixTable. The type of this address is determined by the value of the cefLMPrefixDestAddrType object
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: ceflmprefixlen
            
            	The Network Prefix Length. Index to the cefPrefixTable
            	**type**\: int
            
            	**range:** 0..2040
            
            	**config**\: False
            
            .. attribute:: ceflmprefixrowstatus
            
            	The status of this table entry.  Once the entry  status is set to active(1), the associated entry  cannot be modified until the request completes (cefLMPrefixState transitions to matchFound(2)  or noMatchFound(3)).  Once the longest match request has been created (i.e. the cefLMPrefixRowStatus has been made active), the entry cannot be modified \- the only operation possible after this is to delete the row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.CefLMPrefixTable.CefLMPrefixEntry, self).__init__()

                self.yang_name = "cefLMPrefixEntry"
                self.yang_parent_name = "cefLMPrefixTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','ceflmprefixdestaddrtype','ceflmprefixdestaddr']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('ceflmprefixdestaddrtype', (YLeaf(YType.enumeration, 'cefLMPrefixDestAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('ceflmprefixdestaddr', (YLeaf(YType.str, 'cefLMPrefixDestAddr'), ['str'])),
                    ('ceflmprefixstate', (YLeaf(YType.enumeration, 'cefLMPrefixState'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefPrefixSearchState', '')])),
                    ('ceflmprefixaddr', (YLeaf(YType.str, 'cefLMPrefixAddr'), ['str'])),
                    ('ceflmprefixlen', (YLeaf(YType.uint32, 'cefLMPrefixLen'), ['int'])),
                    ('ceflmprefixrowstatus', (YLeaf(YType.enumeration, 'cefLMPrefixRowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.entphysicalindex = None
                self.ceflmprefixdestaddrtype = None
                self.ceflmprefixdestaddr = None
                self.ceflmprefixstate = None
                self.ceflmprefixaddr = None
                self.ceflmprefixlen = None
                self.ceflmprefixrowstatus = None
                self._segment_path = lambda: "cefLMPrefixEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefLMPrefixDestAddrType='" + str(self.ceflmprefixdestaddrtype) + "']" + "[cefLMPrefixDestAddr='" + str(self.ceflmprefixdestaddr) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefLMPrefixTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.CefLMPrefixTable.CefLMPrefixEntry, ['entphysicalindex', 'ceflmprefixdestaddrtype', 'ceflmprefixdestaddr', 'ceflmprefixstate', 'ceflmprefixaddr', 'ceflmprefixlen', 'ceflmprefixrowstatus'], name, value)




    class CefPathTable(Entity):
        """
        CEF prefix path is a valid route to reach to a 
        destination IP prefix. Multiple paths may exist 
        out of a router to the same destination prefix. 
        This table specify lists of CEF paths.
        
        .. attribute:: cefpathentry
        
        	If CEF is enabled on the Managed device, each entry contain a CEF prefix path.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`CefPathEntry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefPathTable.CefPathEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefPathTable, self).__init__()

            self.yang_name = "cefPathTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefPathEntry", ("cefpathentry", CISCOCEFMIB.CefPathTable.CefPathEntry))])
            self._leafs = OrderedDict()

            self.cefpathentry = YList(self)
            self._segment_path = lambda: "cefPathTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefPathTable, [], name, value)


        class CefPathEntry(Entity):
            """
            If CEF is enabled on the Managed device,
            each entry contain a CEF prefix path.
            
            entPhysicalIndex is also an index for this
            table which represents entities of
            'module' entPhysicalClass which are capable
            of running CEF.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: cefprefixtype  (key)
            
            	
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cefprefixaddr  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cefprefixaddr <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefPrefixTable.CefPrefixEntry>`
            
            	**config**\: False
            
            .. attribute:: cefprefixlen  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..2040
            
            	**refers to**\:  :py:class:`cefprefixlen <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefPrefixTable.CefPrefixEntry>`
            
            	**config**\: False
            
            .. attribute:: cefpathid  (key)
            
            	The locally arbitrary, but unique identifier associated with this prefix path entry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cefpathtype
            
            	Type for this CEF Path
            	**type**\:  :py:class:`CefPathType <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefPathType>`
            
            	**config**\: False
            
            .. attribute:: cefpathinterface
            
            	Interface associated with this CEF path.  A value of zero for this object will indicate that no interface is associated with this path  entry
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cefpathnexthopaddr
            
            	Next hop address associated with this CEF path.  The value of this object is only relevant for attached next hop and recursive next hop   path types (when the object cefPathType is set to attachedNexthop(4) or recursiveNexthop(5)). and will be set to zero for other path types.  The type of this address is determined by the value of the cefPrefixType object
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cefpathrecursevrfname
            
            	The recursive vrf name associated with this path.  The value of this object is only relevant for recursive next hop path types (when the  object cefPathType is set to recursiveNexthop(5)), and '0x00' will be returned for other path types
            	**type**\: str
            
            	**length:** 0..31
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.CefPathTable.CefPathEntry, self).__init__()

                self.yang_name = "cefPathEntry"
                self.yang_parent_name = "cefPathTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cefprefixtype','cefprefixaddr','cefprefixlen','cefpathid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefprefixtype', (YLeaf(YType.enumeration, 'cefPrefixType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cefprefixaddr', (YLeaf(YType.str, 'cefPrefixAddr'), ['str'])),
                    ('cefprefixlen', (YLeaf(YType.str, 'cefPrefixLen'), ['int'])),
                    ('cefpathid', (YLeaf(YType.int32, 'cefPathId'), ['int'])),
                    ('cefpathtype', (YLeaf(YType.enumeration, 'cefPathType'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefPathType', '')])),
                    ('cefpathinterface', (YLeaf(YType.int32, 'cefPathInterface'), ['int'])),
                    ('cefpathnexthopaddr', (YLeaf(YType.str, 'cefPathNextHopAddr'), ['str'])),
                    ('cefpathrecursevrfname', (YLeaf(YType.str, 'cefPathRecurseVrfName'), ['str'])),
                ])
                self.entphysicalindex = None
                self.cefprefixtype = None
                self.cefprefixaddr = None
                self.cefprefixlen = None
                self.cefpathid = None
                self.cefpathtype = None
                self.cefpathinterface = None
                self.cefpathnexthopaddr = None
                self.cefpathrecursevrfname = None
                self._segment_path = lambda: "cefPathEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefPrefixType='" + str(self.cefprefixtype) + "']" + "[cefPrefixAddr='" + str(self.cefprefixaddr) + "']" + "[cefPrefixLen='" + str(self.cefprefixlen) + "']" + "[cefPathId='" + str(self.cefpathid) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefPathTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.CefPathTable.CefPathEntry, ['entphysicalindex', 'cefprefixtype', 'cefprefixaddr', 'cefprefixlen', 'cefpathid', 'cefpathtype', 'cefpathinterface', 'cefpathnexthopaddr', 'cefpathrecursevrfname'], name, value)




    class CefAdjSummaryTable(Entity):
        """
        This table contains the summary information
        for the cefAdjTable.
        
        .. attribute:: cefadjsummaryentry
        
        	If CEF is enabled on the Managed device, each entry contains the CEF Adjacency   summary related attributes for the Managed entity. A row exists for each adjacency link type.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`CefAdjSummaryEntry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefAdjSummaryTable.CefAdjSummaryEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefAdjSummaryTable, self).__init__()

            self.yang_name = "cefAdjSummaryTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefAdjSummaryEntry", ("cefadjsummaryentry", CISCOCEFMIB.CefAdjSummaryTable.CefAdjSummaryEntry))])
            self._leafs = OrderedDict()

            self.cefadjsummaryentry = YList(self)
            self._segment_path = lambda: "cefAdjSummaryTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefAdjSummaryTable, [], name, value)


        class CefAdjSummaryEntry(Entity):
            """
            If CEF is enabled on the Managed device,
            each entry contains the CEF Adjacency  
            summary related attributes for the
            Managed entity. A row exists for
            each adjacency link type.
            
            entPhysicalIndex is also an index for this
            table which represents entities of
            'module' entPhysicalClass which are capable
            of running CEF.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: cefadjsummarylinktype  (key)
            
            	The link type of the adjacency
            	**type**\:  :py:class:`CefAdjLinkType <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefAdjLinkType>`
            
            	**config**\: False
            
            .. attribute:: cefadjsummarycomplete
            
            	The total number of complete adjacencies.  The total number of adjacencies which can be used  to switch traffic to a neighbour
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cefadjsummaryincomplete
            
            	The total number of incomplete adjacencies.  The total number of adjacencies which cannot be  used to switch traffic in their current state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cefadjsummaryfixup
            
            	The total number of adjacencies for which the Layer 2 encapsulation string (header) may be  updated (fixed up) at packet switch time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cefadjsummaryredirect
            
            	The total number of adjacencies for which  ip redirect (or icmp redirection) is enabled. The value of this object is only relevant for ipv4 and ipv6 link type (when the index object  cefAdjSummaryLinkType value is ipv4(1) or ipv6(2)) and will be set to zero for other link types
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.CefAdjSummaryTable.CefAdjSummaryEntry, self).__init__()

                self.yang_name = "cefAdjSummaryEntry"
                self.yang_parent_name = "cefAdjSummaryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cefadjsummarylinktype']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefadjsummarylinktype', (YLeaf(YType.enumeration, 'cefAdjSummaryLinkType'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefAdjLinkType', '')])),
                    ('cefadjsummarycomplete', (YLeaf(YType.uint32, 'cefAdjSummaryComplete'), ['int'])),
                    ('cefadjsummaryincomplete', (YLeaf(YType.uint32, 'cefAdjSummaryIncomplete'), ['int'])),
                    ('cefadjsummaryfixup', (YLeaf(YType.uint32, 'cefAdjSummaryFixup'), ['int'])),
                    ('cefadjsummaryredirect', (YLeaf(YType.uint32, 'cefAdjSummaryRedirect'), ['int'])),
                ])
                self.entphysicalindex = None
                self.cefadjsummarylinktype = None
                self.cefadjsummarycomplete = None
                self.cefadjsummaryincomplete = None
                self.cefadjsummaryfixup = None
                self.cefadjsummaryredirect = None
                self._segment_path = lambda: "cefAdjSummaryEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefAdjSummaryLinkType='" + str(self.cefadjsummarylinktype) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefAdjSummaryTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.CefAdjSummaryTable.CefAdjSummaryEntry, ['entphysicalindex', 'cefadjsummarylinktype', 'cefadjsummarycomplete', 'cefadjsummaryincomplete', 'cefadjsummaryfixup', 'cefadjsummaryredirect'], name, value)




    class CefAdjTable(Entity):
        """
        A list of CEF adjacencies.
        
        .. attribute:: cefadjentry
        
        	If CEF is enabled on the Managed device, each entry contains the adjacency  attributes. Adjacency entries may exist for all the interfaces on which packets can be switched out of the device. The interface is instantiated by ifIndex.   Therefore, the interface index must have been assigned, according to the applicable procedures, before it can be meaningfully used. Generally, this means that the interface must exist.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`CefAdjEntry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefAdjTable.CefAdjEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefAdjTable, self).__init__()

            self.yang_name = "cefAdjTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefAdjEntry", ("cefadjentry", CISCOCEFMIB.CefAdjTable.CefAdjEntry))])
            self._leafs = OrderedDict()

            self.cefadjentry = YList(self)
            self._segment_path = lambda: "cefAdjTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefAdjTable, [], name, value)


        class CefAdjEntry(Entity):
            """
            If CEF is enabled on the Managed device,
            each entry contains the adjacency 
            attributes. Adjacency entries may exist
            for all the interfaces on which packets
            can be switched out of the device.
            The interface is instantiated by ifIndex.  
            Therefore, the interface index must have been
            assigned, according to the applicable procedures,
            before it can be meaningfully used.
            Generally, this means that the interface must exist.
            
            entPhysicalIndex is also an index for this
            table which represents entities of
            'module' entPhysicalClass which are capable
            of running CEF.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cefadjnexthopaddrtype  (key)
            
            	Address type for the cefAdjNextHopAddr. This object specifies the address type used for cefAdjNextHopAddr.   Adjacency entries are only valid for the  address type of ipv4(1) and ipv6(2)
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cefadjnexthopaddr  (key)
            
            	The next Hop address for this adjacency. The type of this address is determined by the value of the cefAdjNextHopAddrType object
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cefadjconnid  (key)
            
            	In cases where cefLinkType, interface and the next hop address are not able to uniquely define an adjacency entry (e.g. ATM and Frame Relay Bundles), this object is a unique identifier to differentiate between these adjacency entries.   In all the other cases the value of this  index object will be 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cefadjsummarylinktype  (key)
            
            	
            	**type**\:  :py:class:`CefAdjLinkType <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefAdjLinkType>`
            
            	**config**\: False
            
            .. attribute:: cefadjsource
            
            	If the adjacency is created because some neighbour discovery mechanism has discovered a neighbour and all the information required to build a frame header to encapsulate traffic to the neighbour is available then the source of adjacency is set to the mechanism by which the adjacency is learned
            	**type**\:  :py:class:`CefAdjacencySource <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefAdjacencySource>`
            
            	**config**\: False
            
            .. attribute:: cefadjencap
            
            	The layer 2 encapsulation string to be used for sending the packet out using this adjacency
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cefadjfixup
            
            	For the cases, where the encapsulation string is decided at packet switch time, the adjacency  encapsulation string specified by object cefAdjEncap  require a fixup. I.e. for the adjacencies out of IP  Tunnels, the string prepended is an IP header which has  fields which can only be setup at packet switch time.  The value of this object represent the kind of fixup applied to the packet.  If the encapsulation string doesn't require any fixup, then the value of this object will be of zero length
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cefadjmtu
            
            	The Layer 3 MTU which can be transmitted using  this adjacency
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cefadjforwardinginfo
            
            	This object selects a forwarding info entry  defined in the cefFESelectionTable. The  selected target is defined by an entry in the cefFESelectionTable whose index value (cefFESelectionName)  is equal to this object.  The value of this object will be of zero length if this adjacency entry is the last forwarding  element in the forwarding path
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cefadjpkts
            
            	Number of pkts transmitted using this adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cefadjhcpkts
            
            	Number of pkts transmitted using this adjacency. This object is a 64\-bit version of cefAdjPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cefadjbytes
            
            	Number of bytes transmitted using this adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cefadjhcbytes
            
            	Number of bytes transmitted using this adjacency. This object is a 64\-bit version of cefAdjBytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.CefAdjTable.CefAdjEntry, self).__init__()

                self.yang_name = "cefAdjEntry"
                self.yang_parent_name = "cefAdjTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','ifindex','cefadjnexthopaddrtype','cefadjnexthopaddr','cefadjconnid','cefadjsummarylinktype']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cefadjnexthopaddrtype', (YLeaf(YType.enumeration, 'cefAdjNextHopAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cefadjnexthopaddr', (YLeaf(YType.str, 'cefAdjNextHopAddr'), ['str'])),
                    ('cefadjconnid', (YLeaf(YType.uint32, 'cefAdjConnId'), ['int'])),
                    ('cefadjsummarylinktype', (YLeaf(YType.enumeration, 'cefAdjSummaryLinkType'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefAdjLinkType', '')])),
                    ('cefadjsource', (YLeaf(YType.bits, 'cefAdjSource'), ['Bits'])),
                    ('cefadjencap', (YLeaf(YType.str, 'cefAdjEncap'), ['str'])),
                    ('cefadjfixup', (YLeaf(YType.str, 'cefAdjFixup'), ['str'])),
                    ('cefadjmtu', (YLeaf(YType.uint32, 'cefAdjMTU'), ['int'])),
                    ('cefadjforwardinginfo', (YLeaf(YType.str, 'cefAdjForwardingInfo'), ['str'])),
                    ('cefadjpkts', (YLeaf(YType.uint32, 'cefAdjPkts'), ['int'])),
                    ('cefadjhcpkts', (YLeaf(YType.uint64, 'cefAdjHCPkts'), ['int'])),
                    ('cefadjbytes', (YLeaf(YType.uint32, 'cefAdjBytes'), ['int'])),
                    ('cefadjhcbytes', (YLeaf(YType.uint64, 'cefAdjHCBytes'), ['int'])),
                ])
                self.entphysicalindex = None
                self.ifindex = None
                self.cefadjnexthopaddrtype = None
                self.cefadjnexthopaddr = None
                self.cefadjconnid = None
                self.cefadjsummarylinktype = None
                self.cefadjsource = Bits()
                self.cefadjencap = None
                self.cefadjfixup = None
                self.cefadjmtu = None
                self.cefadjforwardinginfo = None
                self.cefadjpkts = None
                self.cefadjhcpkts = None
                self.cefadjbytes = None
                self.cefadjhcbytes = None
                self._segment_path = lambda: "cefAdjEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[ifIndex='" + str(self.ifindex) + "']" + "[cefAdjNextHopAddrType='" + str(self.cefadjnexthopaddrtype) + "']" + "[cefAdjNextHopAddr='" + str(self.cefadjnexthopaddr) + "']" + "[cefAdjConnId='" + str(self.cefadjconnid) + "']" + "[cefAdjSummaryLinkType='" + str(self.cefadjsummarylinktype) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefAdjTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.CefAdjTable.CefAdjEntry, ['entphysicalindex', 'ifindex', 'cefadjnexthopaddrtype', 'cefadjnexthopaddr', 'cefadjconnid', 'cefadjsummarylinktype', 'cefadjsource', 'cefadjencap', 'cefadjfixup', 'cefadjmtu', 'cefadjforwardinginfo', 'cefadjpkts', 'cefadjhcpkts', 'cefadjbytes', 'cefadjhcbytes'], name, value)




    class CefFESelectionTable(Entity):
        """
        A list of forwarding element selection entries.
        
        .. attribute:: ceffeselectionentry
        
        	If CEF is enabled on the Managed device, each entry contain a CEF forwarding element selection list.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`CefFESelectionEntry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefFESelectionTable.CefFESelectionEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefFESelectionTable, self).__init__()

            self.yang_name = "cefFESelectionTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefFESelectionEntry", ("ceffeselectionentry", CISCOCEFMIB.CefFESelectionTable.CefFESelectionEntry))])
            self._leafs = OrderedDict()

            self.ceffeselectionentry = YList(self)
            self._segment_path = lambda: "cefFESelectionTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefFESelectionTable, [], name, value)


        class CefFESelectionEntry(Entity):
            """
            If CEF is enabled on the Managed device,
            each entry contain a CEF forwarding element
            selection list.
            
            entPhysicalIndex is also an index for this
            table which represents entities of
            'module' entPhysicalClass which are capable
            of running CEF.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: ceffeselectionname  (key)
            
            	The locally arbitrary, but unique identifier used to select a set of forwarding element lists
            	**type**\: str
            
            	**length:** 1..32
            
            	**config**\: False
            
            .. attribute:: ceffeselectionid  (key)
            
            	Secondary index to identify a forwarding elements List  in this Table
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: ceffeselectionspecial
            
            	Special processing for a destination is indicated through the use of special  forwarding element.   If the forwarding element list contains the  special forwarding element, then this object  represents the type of special forwarding element
            	**type**\:  :py:class:`CefForwardingElementSpecialType <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefForwardingElementSpecialType>`
            
            	**config**\: False
            
            .. attribute:: ceffeselectionlabels
            
            	This object represent the MPLS Labels  associated with this forwarding Element List.  The value of this object will be irrelevant and will be set to zero length if the forwarding element list  doesn't contain a label forwarding element. A zero  length label list will indicate that there is no label forwarding element associated with this selection entry
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: ceffeselectionadjlinktype
            
            	This object represent the link type for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to unknown(5) if the forwarding element list  doesn't contain an adjacency forwarding element
            	**type**\:  :py:class:`CefAdjLinkType <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefAdjLinkType>`
            
            	**config**\: False
            
            .. attribute:: ceffeselectionadjinterface
            
            	This object represent the interface for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to zero if the forwarding element list doesn't  contain an adjacency forwarding element
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: ceffeselectionadjnexthopaddrtype
            
            	This object represent the next hop address type for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to unknown(0) if the forwarding element list  doesn't contain an adjacency forwarding element
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: ceffeselectionadjnexthopaddr
            
            	This object represent the next hop address for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to zero if the forwarding element list doesn't  contain an adjacency forwarding element
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: ceffeselectionadjconnid
            
            	This object represent the connection id for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to zero if the forwarding element list doesn't  contain an adjacency forwarding element.   In cases where cefFESelectionAdjLinkType, interface  and the next hop address are not able to uniquely  define an adjacency entry (e.g. ATM and Frame Relay Bundles), this object is a unique identifier to differentiate between these adjacency entries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: ceffeselectionvrfname
            
            	This object represent the Vrf name for the lookup associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to a string containing the single octet 0x00 if the forwarding element list  doesn't contain a lookup forwarding element
            	**type**\: str
            
            	**length:** 0..31
            
            	**config**\: False
            
            .. attribute:: ceffeselectionweight
            
            	This object represent the weighting for  load balancing between multiple Forwarding Element Lists. The value of this object will be zero if load balancing is associated with this selection entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.CefFESelectionTable.CefFESelectionEntry, self).__init__()

                self.yang_name = "cefFESelectionEntry"
                self.yang_parent_name = "cefFESelectionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','ceffeselectionname','ceffeselectionid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('ceffeselectionname', (YLeaf(YType.str, 'cefFESelectionName'), ['str'])),
                    ('ceffeselectionid', (YLeaf(YType.int32, 'cefFESelectionId'), ['int'])),
                    ('ceffeselectionspecial', (YLeaf(YType.enumeration, 'cefFESelectionSpecial'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefForwardingElementSpecialType', '')])),
                    ('ceffeselectionlabels', (YLeaf(YType.str, 'cefFESelectionLabels'), ['str'])),
                    ('ceffeselectionadjlinktype', (YLeaf(YType.enumeration, 'cefFESelectionAdjLinkType'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefAdjLinkType', '')])),
                    ('ceffeselectionadjinterface', (YLeaf(YType.int32, 'cefFESelectionAdjInterface'), ['int'])),
                    ('ceffeselectionadjnexthopaddrtype', (YLeaf(YType.enumeration, 'cefFESelectionAdjNextHopAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('ceffeselectionadjnexthopaddr', (YLeaf(YType.str, 'cefFESelectionAdjNextHopAddr'), ['str'])),
                    ('ceffeselectionadjconnid', (YLeaf(YType.uint32, 'cefFESelectionAdjConnId'), ['int'])),
                    ('ceffeselectionvrfname', (YLeaf(YType.str, 'cefFESelectionVrfName'), ['str'])),
                    ('ceffeselectionweight', (YLeaf(YType.uint32, 'cefFESelectionWeight'), ['int'])),
                ])
                self.entphysicalindex = None
                self.ceffeselectionname = None
                self.ceffeselectionid = None
                self.ceffeselectionspecial = None
                self.ceffeselectionlabels = None
                self.ceffeselectionadjlinktype = None
                self.ceffeselectionadjinterface = None
                self.ceffeselectionadjnexthopaddrtype = None
                self.ceffeselectionadjnexthopaddr = None
                self.ceffeselectionadjconnid = None
                self.ceffeselectionvrfname = None
                self.ceffeselectionweight = None
                self._segment_path = lambda: "cefFESelectionEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefFESelectionName='" + str(self.ceffeselectionname) + "']" + "[cefFESelectionId='" + str(self.ceffeselectionid) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefFESelectionTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.CefFESelectionTable.CefFESelectionEntry, ['entphysicalindex', 'ceffeselectionname', 'ceffeselectionid', 'ceffeselectionspecial', 'ceffeselectionlabels', 'ceffeselectionadjlinktype', 'ceffeselectionadjinterface', 'ceffeselectionadjnexthopaddrtype', 'ceffeselectionadjnexthopaddr', 'ceffeselectionadjconnid', 'ceffeselectionvrfname', 'ceffeselectionweight'], name, value)




    class CefCfgTable(Entity):
        """
        This table contains global config parameter 
        of CEF on the Managed device.
        
        .. attribute:: cefcfgentry
        
        	If the Managed device supports CEF,  each entry contains the CEF config  parameter for the managed entity. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`CefCfgEntry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefCfgTable.CefCfgEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefCfgTable, self).__init__()

            self.yang_name = "cefCfgTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefCfgEntry", ("cefcfgentry", CISCOCEFMIB.CefCfgTable.CefCfgEntry))])
            self._leafs = OrderedDict()

            self.cefcfgentry = YList(self)
            self._segment_path = lambda: "cefCfgTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefCfgTable, [], name, value)


        class CefCfgEntry(Entity):
            """
            If the Managed device supports CEF, 
            each entry contains the CEF config 
            parameter for the managed entity.
            A row may exist for each IP version type
            (v4 and v6) depending upon the IP version
            supported on the device.
            
            entPhysicalIndex is also an index for this
            table which represents entities of
            'module' entPhysicalClass which are capable
            of running CEF.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: ceffibipversion  (key)
            
            	
            	**type**\:  :py:class:`CefIpVersion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefIpVersion>`
            
            	**config**\: False
            
            .. attribute:: cefcfgadminstate
            
            	The desired state of CEF
            	**type**\:  :py:class:`CefAdminStatus <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefAdminStatus>`
            
            	**config**\: False
            
            .. attribute:: cefcfgoperstate
            
            	The current operational state of CEF.  If the cefCfgAdminState is disabled(2), then cefOperState will eventually go to the down(2) state unless some error has occurred.   If cefCfgAdminState is changed to enabled(1) then  cefCfgOperState should change to up(1) only if the  CEF entity is ready to forward the packets using  Cisco Express Forwarding (CEF) else it should remain  in the down(2) state. The up(1) state for this object  indicates that CEF entity is forwarding the packet using Cisco Express Forwarding
            	**type**\:  :py:class:`CefOperStatus <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefOperStatus>`
            
            	**config**\: False
            
            .. attribute:: cefcfgdistributionadminstate
            
            	The desired state of CEF distribution
            	**type**\:  :py:class:`CefAdminStatus <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefAdminStatus>`
            
            	**config**\: False
            
            .. attribute:: cefcfgdistributionoperstate
            
            	The current operational state of CEF distribution.  If the cefCfgDistributionAdminState is disabled(2), then cefDistributionOperState will eventually go to the down(2) state unless some error has occurred.    If cefCfgDistributionAdminState is changed to enabled(1)  then cefCfgDistributionOperState should change to up(1)  only if the CEF entity is ready to forward the packets  using Distributed Cisco Express Forwarding (dCEF) else  it should remain in the down(2) state. The up(1) state  for this object indicates that CEF entity is forwarding the packet using Distributed Cisco Express Forwarding
            	**type**\:  :py:class:`CefOperStatus <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefOperStatus>`
            
            	**config**\: False
            
            .. attribute:: cefcfgaccountingmap
            
            	This object represents a bitmap of network accounting options.  CEF network accounting is disabled by default.  CEF network accounting can be enabled  by selecting one or more of the following CEF accounting option for the value of this object.    nonRecursive(0)\:  enables accounting through                     nonrecursive prefixes.   perPrefix(1)\:     enables the collection of the numbers                     of pkts and bytes express forwarded                    to a destination (prefix)   prefixLength(2)\:  enables accounting through                     prefixlength.           Once the accounting is enabled, the corresponding stats  can be retrieved from the cefPrefixTable and  cefStatsPrefixLenTable.  
            	**type**\:  :py:class:`CefCfgAccountingMap <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefCfgTable.CefCfgEntry.CefCfgAccountingMap>`
            
            	**config**\: False
            
            .. attribute:: cefcfgloadsharingalgorithm
            
            	Indicates the CEF Load balancing algorithm.  Setting this object to none(1) will disable the Load sharing for the specified entry.  CEF load balancing can be enabled by setting  this object to one of following Algorithms\:   original(2)  \: This algorithm is based on a                  source and destination hash    tunnel(3)    \: This algorithm is used in                  tunnels environments or in                 environments where there are                 only a few source                      universal(4)  \: This algorithm uses a source and                   destination and ID hash  If the value of this object is set to 'tunnel' or 'universal', then the FIXED ID for these algorithms may be specified by the managed  object cefLoadSharingID. 
            	**type**\:  :py:class:`CefCfgLoadSharingAlgorithm <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefCfgTable.CefCfgEntry.CefCfgLoadSharingAlgorithm>`
            
            	**config**\: False
            
            .. attribute:: cefcfgloadsharingid
            
            	The Fixed ID associated with the managed object cefCfgLoadSharingAlgorithm. The hash of this object value may be used by the Load Sharing Algorithm.  The value of this object is not relevant and will be set to zero if the value of managed object  cefCfgLoadSharingAlgorithm is set to none(1) or original(2). The default value of this object is calculated by the device at the time of initialization
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cefcfgtrafficstatsloadinterval
            
            	The interval time over which the CEF traffic statistics are collected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cefcfgtrafficstatsupdaterate
            
            	The frequency with which the line card sends the traffic load statistics to the Router Processor.  Setting the value of this object to 0 will disable the CEF traffic statistics collection
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            	**units**\: seconds
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.CefCfgTable.CefCfgEntry, self).__init__()

                self.yang_name = "cefCfgEntry"
                self.yang_parent_name = "cefCfgTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','ceffibipversion']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('ceffibipversion', (YLeaf(YType.enumeration, 'cefFIBIpVersion'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefIpVersion', '')])),
                    ('cefcfgadminstate', (YLeaf(YType.enumeration, 'cefCfgAdminState'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefAdminStatus', '')])),
                    ('cefcfgoperstate', (YLeaf(YType.enumeration, 'cefCfgOperState'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefOperStatus', '')])),
                    ('cefcfgdistributionadminstate', (YLeaf(YType.enumeration, 'cefCfgDistributionAdminState'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefAdminStatus', '')])),
                    ('cefcfgdistributionoperstate', (YLeaf(YType.enumeration, 'cefCfgDistributionOperState'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefOperStatus', '')])),
                    ('cefcfgaccountingmap', (YLeaf(YType.bits, 'cefCfgAccountingMap'), ['Bits'])),
                    ('cefcfgloadsharingalgorithm', (YLeaf(YType.enumeration, 'cefCfgLoadSharingAlgorithm'), [('ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CISCOCEFMIB', 'CefCfgTable.CefCfgEntry.CefCfgLoadSharingAlgorithm')])),
                    ('cefcfgloadsharingid', (YLeaf(YType.uint32, 'cefCfgLoadSharingID'), ['int'])),
                    ('cefcfgtrafficstatsloadinterval', (YLeaf(YType.uint32, 'cefCfgTrafficStatsLoadInterval'), ['int'])),
                    ('cefcfgtrafficstatsupdaterate', (YLeaf(YType.uint32, 'cefCfgTrafficStatsUpdateRate'), ['int'])),
                ])
                self.entphysicalindex = None
                self.ceffibipversion = None
                self.cefcfgadminstate = None
                self.cefcfgoperstate = None
                self.cefcfgdistributionadminstate = None
                self.cefcfgdistributionoperstate = None
                self.cefcfgaccountingmap = Bits()
                self.cefcfgloadsharingalgorithm = None
                self.cefcfgloadsharingid = None
                self.cefcfgtrafficstatsloadinterval = None
                self.cefcfgtrafficstatsupdaterate = None
                self._segment_path = lambda: "cefCfgEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefFIBIpVersion='" + str(self.ceffibipversion) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefCfgTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.CefCfgTable.CefCfgEntry, ['entphysicalindex', 'ceffibipversion', 'cefcfgadminstate', 'cefcfgoperstate', 'cefcfgdistributionadminstate', 'cefcfgdistributionoperstate', 'cefcfgaccountingmap', 'cefcfgloadsharingalgorithm', 'cefcfgloadsharingid', 'cefcfgtrafficstatsloadinterval', 'cefcfgtrafficstatsupdaterate'], name, value)

            class CefCfgLoadSharingAlgorithm(Enum):
                """
                CefCfgLoadSharingAlgorithm (Enum Class)

                Indicates the CEF Load balancing algorithm.

                Setting this object to none(1) will disable

                the Load sharing for the specified entry.

                CEF load balancing can be enabled by setting 

                this object to one of following Algorithms\:

                 original(2)  \: This algorithm is based on a 

                                source and destination hash 

                 tunnel(3)    \: This algorithm is used in 

                                tunnels environments or in

                                environments where there are

                                only a few source 

                 universal(4)  \: This algorithm uses a source and 

                                 destination and ID hash

                If the value of this object is set to 'tunnel'

                or 'universal', then the FIXED ID for these

                algorithms may be specified by the managed 

                object cefLoadSharingID. 

                .. data:: none = 1

                .. data:: original = 2

                .. data:: tunnel = 3

                .. data:: universal = 4

                """

                none = Enum.YLeaf(1, "none")

                original = Enum.YLeaf(2, "original")

                tunnel = Enum.YLeaf(3, "tunnel")

                universal = Enum.YLeaf(4, "universal")





    class CefResourceTable(Entity):
        """
        This table contains global resource 
        information of CEF on the Managed device.
        
        .. attribute:: cefresourceentry
        
        	If the Managed device supports CEF, each entry contains the CEF Resource  parameters for the managed entity.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`CefResourceEntry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefResourceTable.CefResourceEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefResourceTable, self).__init__()

            self.yang_name = "cefResourceTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefResourceEntry", ("cefresourceentry", CISCOCEFMIB.CefResourceTable.CefResourceEntry))])
            self._leafs = OrderedDict()

            self.cefresourceentry = YList(self)
            self._segment_path = lambda: "cefResourceTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefResourceTable, [], name, value)


        class CefResourceEntry(Entity):
            """
            If the Managed device supports CEF,
            each entry contains the CEF Resource 
            parameters for the managed entity.
            
            entPhysicalIndex is also an index for this
            table which represents entities of
            'module' entPhysicalClass which are capable
            of running CEF.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: cefresourcememoryused
            
            	Indicates the number of bytes from the Processor Memory Pool that are currently in use by CEF on the managed entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cefresourcefailurereason
            
            	The CEF resource failure reason which may lead to CEF being disabled on the managed entity
            	**type**\:  :py:class:`CefFailureReason <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefFailureReason>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.CefResourceTable.CefResourceEntry, self).__init__()

                self.yang_name = "cefResourceEntry"
                self.yang_parent_name = "cefResourceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cefresourcememoryused', (YLeaf(YType.uint32, 'cefResourceMemoryUsed'), ['int'])),
                    ('cefresourcefailurereason', (YLeaf(YType.enumeration, 'cefResourceFailureReason'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefFailureReason', '')])),
                ])
                self.entphysicalindex = None
                self.cefresourcememoryused = None
                self.cefresourcefailurereason = None
                self._segment_path = lambda: "cefResourceEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefResourceTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.CefResourceTable.CefResourceEntry, ['entphysicalindex', 'cefresourcememoryused', 'cefresourcefailurereason'], name, value)




    class CefIntTable(Entity):
        """
        This Table contains interface specific
        information of CEF on the Managed
        device.
        
        .. attribute:: cefintentry
        
        	If CEF is enabled on the Managed device,  each entry contains the CEF attributes  associated with an interface. The interface is instantiated by ifIndex.   Therefore, the interface index must have been assigned, according to the applicable procedures, before it can be meaningfully used. Generally, this means that the interface must exist.  A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`CefIntEntry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefIntTable.CefIntEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefIntTable, self).__init__()

            self.yang_name = "cefIntTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefIntEntry", ("cefintentry", CISCOCEFMIB.CefIntTable.CefIntEntry))])
            self._leafs = OrderedDict()

            self.cefintentry = YList(self)
            self._segment_path = lambda: "cefIntTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefIntTable, [], name, value)


        class CefIntEntry(Entity):
            """
            If CEF is enabled on the Managed device, 
            each entry contains the CEF attributes 
            associated with an interface.
            The interface is instantiated by ifIndex.  
            Therefore, the interface index must have been
            assigned, according to the applicable procedures,
            before it can be meaningfully used.
            Generally, this means that the interface must exist.
            
            A row may exist for each IP version type
            (v4 and v6) depending upon the IP version
            supported on the device.
            
            entPhysicalIndex is also an index for this
            table which represents entities of
            'module' entPhysicalClass which are capable
            of running CEF.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: ceffibipversion  (key)
            
            	
            	**type**\:  :py:class:`CefIpVersion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefIpVersion>`
            
            	**config**\: False
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: cefintswitchingstate
            
            	The CEF switching State for the interface.  If CEF is enabled but distributed CEF(dCEF) is disabled then CEF is in cefEnabled(1) state.  If distributed CEF is enabled, then CEF is in  distCefEnabled(2) state. The cefDisabled(3) state indicates that CEF is disabled.  The CEF switching state is only applicable to the received packet on the interface
            	**type**\:  :py:class:`CefIntSwitchingState <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefIntTable.CefIntEntry.CefIntSwitchingState>`
            
            	**config**\: False
            
            .. attribute:: cefintloadsharing
            
            	The status of load sharing on the interface.  perPacket(1) \: Router to send data packets                over successive equal\-cost paths                without regard to individual hosts                or user sessions.  perDestination(2) \: Router to use multiple, equal\-cost                     paths to achieve load sharing  Load sharing is enabled by default  for an interface when CEF is enabled
            	**type**\:  :py:class:`CefIntLoadSharing <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefIntTable.CefIntEntry.CefIntLoadSharing>`
            
            	**config**\: False
            
            .. attribute:: cefintnonrecursiveaccouting
            
            	The CEF accounting mode for the interface. CEF prefix based non\-recursive accounting  on an interface can be configured to store  the stats for non\-recursive prefixes in a internal  or external bucket.  internal(1)  \:  Count input traffic in the nonrecursive                 internal bucket  external(2)  \:  Count input traffic in the nonrecursive                 external bucket  The value of this object will only be effective if  value of the object cefAccountingMap is set to enable nonRecursive(1) accounting
            	**type**\:  :py:class:`CefIntNonrecursiveAccouting <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefIntTable.CefIntEntry.CefIntNonrecursiveAccouting>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.CefIntTable.CefIntEntry, self).__init__()

                self.yang_name = "cefIntEntry"
                self.yang_parent_name = "cefIntTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','ceffibipversion','ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('ceffibipversion', (YLeaf(YType.enumeration, 'cefFIBIpVersion'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefIpVersion', '')])),
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('cefintswitchingstate', (YLeaf(YType.enumeration, 'cefIntSwitchingState'), [('ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CISCOCEFMIB', 'CefIntTable.CefIntEntry.CefIntSwitchingState')])),
                    ('cefintloadsharing', (YLeaf(YType.enumeration, 'cefIntLoadSharing'), [('ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CISCOCEFMIB', 'CefIntTable.CefIntEntry.CefIntLoadSharing')])),
                    ('cefintnonrecursiveaccouting', (YLeaf(YType.enumeration, 'cefIntNonrecursiveAccouting'), [('ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CISCOCEFMIB', 'CefIntTable.CefIntEntry.CefIntNonrecursiveAccouting')])),
                ])
                self.entphysicalindex = None
                self.ceffibipversion = None
                self.ifindex = None
                self.cefintswitchingstate = None
                self.cefintloadsharing = None
                self.cefintnonrecursiveaccouting = None
                self._segment_path = lambda: "cefIntEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefFIBIpVersion='" + str(self.ceffibipversion) + "']" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefIntTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.CefIntTable.CefIntEntry, ['entphysicalindex', 'ceffibipversion', 'ifindex', 'cefintswitchingstate', 'cefintloadsharing', 'cefintnonrecursiveaccouting'], name, value)

            class CefIntLoadSharing(Enum):
                """
                CefIntLoadSharing (Enum Class)

                The status of load sharing on the

                interface.

                perPacket(1) \: Router to send data packets

                               over successive equal\-cost paths

                               without regard to individual hosts

                               or user sessions.

                perDestination(2) \: Router to use multiple, equal\-cost

                                    paths to achieve load sharing

                Load sharing is enabled by default 

                for an interface when CEF is enabled.

                .. data:: perPacket = 1

                .. data:: perDestination = 2

                """

                perPacket = Enum.YLeaf(1, "perPacket")

                perDestination = Enum.YLeaf(2, "perDestination")


            class CefIntNonrecursiveAccouting(Enum):
                """
                CefIntNonrecursiveAccouting (Enum Class)

                The CEF accounting mode for the interface.

                CEF prefix based non\-recursive accounting 

                on an interface can be configured to store 

                the stats for non\-recursive prefixes in a internal 

                or external bucket.

                internal(1)  \:  Count input traffic in the nonrecursive

                                internal bucket

                external(2)  \:  Count input traffic in the nonrecursive

                                external bucket

                The value of this object will only be effective if 

                value of the object cefAccountingMap is set to enable

                nonRecursive(1) accounting.

                .. data:: internal = 1

                .. data:: external = 2

                """

                internal = Enum.YLeaf(1, "internal")

                external = Enum.YLeaf(2, "external")


            class CefIntSwitchingState(Enum):
                """
                CefIntSwitchingState (Enum Class)

                The CEF switching State for the interface. 

                If CEF is enabled but distributed CEF(dCEF) is

                disabled then CEF is in cefEnabled(1) state.

                If distributed CEF is enabled, then CEF is in 

                distCefEnabled(2) state. The cefDisabled(3) state

                indicates that CEF is disabled.

                The CEF switching state is only applicable to the

                received packet on the interface.

                .. data:: cefEnabled = 1

                .. data:: distCefEnabled = 2

                .. data:: cefDisabled = 3

                """

                cefEnabled = Enum.YLeaf(1, "cefEnabled")

                distCefEnabled = Enum.YLeaf(2, "distCefEnabled")

                cefDisabled = Enum.YLeaf(3, "cefDisabled")





    class CefPeerTable(Entity):
        """
        Entity acting as RP (Routing Processor) keeps
        the CEF states for the line card entities and
        communicates with the line card entities using
        XDR. This Table contains the CEF information 
        related to peer entities on the managed device.
        
        .. attribute:: cefpeerentry
        
        	If CEF is enabled on the Managed device, each entry contains the CEF related attributes  associated with a CEF peer entity.  entPhysicalIndex and entPeerPhysicalIndex are also indexes for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`CefPeerEntry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefPeerTable.CefPeerEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefPeerTable, self).__init__()

            self.yang_name = "cefPeerTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefPeerEntry", ("cefpeerentry", CISCOCEFMIB.CefPeerTable.CefPeerEntry))])
            self._leafs = OrderedDict()

            self.cefpeerentry = YList(self)
            self._segment_path = lambda: "cefPeerTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefPeerTable, [], name, value)


        class CefPeerEntry(Entity):
            """
            If CEF is enabled on the Managed device,
            each entry contains the CEF related attributes 
            associated with a CEF peer entity.
            
            entPhysicalIndex and entPeerPhysicalIndex are
            also indexes for this table which represents
            entities of 'module' entPhysicalClass which are
            capable of running CEF.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: entpeerphysicalindex  (key)
            
            	The entity index for the CEF peer entity. Only the entities of 'module'  entPhysicalClass are included here
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cefpeeroperstate
            
            	The current CEF operational state of the CEF peer entity.  Cef peer entity oper state will be peerDisabled(1) in  the following condition\:     \: Cef Peer entity encounters fatal error i.e. resource      allocation failure, ipc failure etc     \: When a reload/delete request is received from the Cef       Peer Entity  Once the peer entity is up and no fatal error is encountered, then the value of this object will transits to the peerUp(3)  state.  If the Cef Peer entity is in held stage, then the value of this object will be peerHold(3). Cef peer entity can only transit to peerDisabled(1) state from the peerHold(3) state
            	**type**\:  :py:class:`CefPeerOperState <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefPeerTable.CefPeerEntry.CefPeerOperState>`
            
            	**config**\: False
            
            .. attribute:: cefpeernumberofresets
            
            	Number of times the session with CEF peer entity  has been reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.CefPeerTable.CefPeerEntry, self).__init__()

                self.yang_name = "cefPeerEntry"
                self.yang_parent_name = "cefPeerTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','entpeerphysicalindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('entpeerphysicalindex', (YLeaf(YType.int32, 'entPeerPhysicalIndex'), ['int'])),
                    ('cefpeeroperstate', (YLeaf(YType.enumeration, 'cefPeerOperState'), [('ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CISCOCEFMIB', 'CefPeerTable.CefPeerEntry.CefPeerOperState')])),
                    ('cefpeernumberofresets', (YLeaf(YType.uint32, 'cefPeerNumberOfResets'), ['int'])),
                ])
                self.entphysicalindex = None
                self.entpeerphysicalindex = None
                self.cefpeeroperstate = None
                self.cefpeernumberofresets = None
                self._segment_path = lambda: "cefPeerEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[entPeerPhysicalIndex='" + str(self.entpeerphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefPeerTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.CefPeerTable.CefPeerEntry, ['entphysicalindex', 'entpeerphysicalindex', 'cefpeeroperstate', 'cefpeernumberofresets'], name, value)

            class CefPeerOperState(Enum):
                """
                CefPeerOperState (Enum Class)

                The current CEF operational state of the CEF peer entity.

                Cef peer entity oper state will be peerDisabled(1) in 

                the following condition\:

                   \: Cef Peer entity encounters fatal error i.e. resource

                     allocation failure, ipc failure etc

                   \: When a reload/delete request is received from the Cef 

                     Peer Entity

                Once the peer entity is up and no fatal error is encountered,

                then the value of this object will transits to the peerUp(3) 

                state.

                If the Cef Peer entity is in held stage, then the value

                of this object will be peerHold(3). Cef peer entity can only

                transit to peerDisabled(1) state from the peerHold(3) state.

                .. data:: peerDisabled = 1

                .. data:: peerUp = 2

                .. data:: peerHold = 3

                """

                peerDisabled = Enum.YLeaf(1, "peerDisabled")

                peerUp = Enum.YLeaf(2, "peerUp")

                peerHold = Enum.YLeaf(3, "peerHold")





    class CefPeerFIBTable(Entity):
        """
        Entity acting as RP (Routing Processor) keep
        the CEF FIB states for the line card entities and
        communicate with the line card entities using
        XDR. This Table contains the CEF FIB State 
        related to peer entities on the managed device.
        
        .. attribute:: cefpeerfibentry
        
        	If CEF is enabled on the Managed device, each entry contains the CEF FIB State  associated a CEF peer entity.  entPhysicalIndex and entPeerPhysicalIndex are also indexes for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`CefPeerFIBEntry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefPeerFIBTable.CefPeerFIBEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefPeerFIBTable, self).__init__()

            self.yang_name = "cefPeerFIBTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefPeerFIBEntry", ("cefpeerfibentry", CISCOCEFMIB.CefPeerFIBTable.CefPeerFIBEntry))])
            self._leafs = OrderedDict()

            self.cefpeerfibentry = YList(self)
            self._segment_path = lambda: "cefPeerFIBTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefPeerFIBTable, [], name, value)


        class CefPeerFIBEntry(Entity):
            """
            If CEF is enabled on the Managed device,
            each entry contains the CEF FIB State 
            associated a CEF peer entity.
            
            entPhysicalIndex and entPeerPhysicalIndex are
            also indexes for this table which represents
            entities of 'module' entPhysicalClass which are
            capable of running CEF.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: entpeerphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entpeerphysicalindex <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefPeerTable.CefPeerEntry>`
            
            	**config**\: False
            
            .. attribute:: ceffibipversion  (key)
            
            	
            	**type**\:  :py:class:`CefIpVersion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefIpVersion>`
            
            	**config**\: False
            
            .. attribute:: cefpeerfiboperstate
            
            	The current CEF FIB Operational State for the  CEF peer entity
            	**type**\:  :py:class:`CefPeerFIBOperState <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefPeerFIBTable.CefPeerFIBEntry.CefPeerFIBOperState>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.CefPeerFIBTable.CefPeerFIBEntry, self).__init__()

                self.yang_name = "cefPeerFIBEntry"
                self.yang_parent_name = "cefPeerFIBTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','entpeerphysicalindex','ceffibipversion']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('entpeerphysicalindex', (YLeaf(YType.str, 'entPeerPhysicalIndex'), ['int'])),
                    ('ceffibipversion', (YLeaf(YType.enumeration, 'cefFIBIpVersion'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefIpVersion', '')])),
                    ('cefpeerfiboperstate', (YLeaf(YType.enumeration, 'cefPeerFIBOperState'), [('ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CISCOCEFMIB', 'CefPeerFIBTable.CefPeerFIBEntry.CefPeerFIBOperState')])),
                ])
                self.entphysicalindex = None
                self.entpeerphysicalindex = None
                self.ceffibipversion = None
                self.cefpeerfiboperstate = None
                self._segment_path = lambda: "cefPeerFIBEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[entPeerPhysicalIndex='" + str(self.entpeerphysicalindex) + "']" + "[cefFIBIpVersion='" + str(self.ceffibipversion) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefPeerFIBTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.CefPeerFIBTable.CefPeerFIBEntry, ['entphysicalindex', 'entpeerphysicalindex', 'ceffibipversion', 'cefpeerfiboperstate'], name, value)

            class CefPeerFIBOperState(Enum):
                """
                CefPeerFIBOperState (Enum Class)

                The current CEF FIB Operational State for the 

                CEF peer entity.

                .. data:: peerFIBDown = 1

                .. data:: peerFIBUp = 2

                .. data:: peerFIBReloadRequest = 3

                .. data:: peerFIBReloading = 4

                .. data:: peerFIBSynced = 5

                """

                peerFIBDown = Enum.YLeaf(1, "peerFIBDown")

                peerFIBUp = Enum.YLeaf(2, "peerFIBUp")

                peerFIBReloadRequest = Enum.YLeaf(3, "peerFIBReloadRequest")

                peerFIBReloading = Enum.YLeaf(4, "peerFIBReloading")

                peerFIBSynced = Enum.YLeaf(5, "peerFIBSynced")





    class CefCCGlobalTable(Entity):
        """
        This table contains CEF consistency checker
        (CC) global parameters for the managed device.
        
        .. attribute:: cefccglobalentry
        
        	If the managed device supports CEF, each entry contains the global consistency  checker parameter for the managed device. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device
        	**type**\: list of  		 :py:class:`CefCCGlobalEntry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefCCGlobalTable.CefCCGlobalEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefCCGlobalTable, self).__init__()

            self.yang_name = "cefCCGlobalTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefCCGlobalEntry", ("cefccglobalentry", CISCOCEFMIB.CefCCGlobalTable.CefCCGlobalEntry))])
            self._leafs = OrderedDict()

            self.cefccglobalentry = YList(self)
            self._segment_path = lambda: "cefCCGlobalTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefCCGlobalTable, [], name, value)


        class CefCCGlobalEntry(Entity):
            """
            If the managed device supports CEF,
            each entry contains the global consistency 
            checker parameter for the managed device.
            A row may exist for each IP version type
            (v4 and v6) depending upon the IP version
            supported on the device.
            
            .. attribute:: ceffibipversion  (key)
            
            	
            	**type**\:  :py:class:`CefIpVersion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefIpVersion>`
            
            	**config**\: False
            
            .. attribute:: cefccglobalautorepairenabled
            
            	Once an inconsistency has been detected,  CEF has the ability to repair the problem.  This object indicates the status of auto\-repair  function for the consistency checkers
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cefccglobalautorepairdelay
            
            	Indiactes how long the consistency checker  waits to fix an inconsistency.  The value of this object has no effect when the value of object cefCCGlobalAutoRepairEnabled is 'false'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cefccglobalautorepairholddown
            
            	Indicates how long the consistency checker waits to re\-enable auto\-repair after  auto\-repair runs.  The value of this object has no effect when the value of object cefCCGlobalAutoRepairEnabled is 'false'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cefccglobalerrormsgenabled
            
            	Enables the consistency checker to generate  an error message when it detects an inconsistency
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cefccglobalfullscanaction
            
            	Setting the value of this object to ccActionStart(1) will start the full scan consistency checkers.  The Management station should poll the  cefCCGlobalFullScanStatus object to get the  state of full\-scan operation.  Once the full\-scan operation completes (value of cefCCGlobalFullScanStatus object is ccStatusDone(3)),  the Management station should retrieve the values of the related stats object from the cefCCTypeTable.  Setting the value of this object to ccActionAbort(2) will  abort the full\-scan operation.  The value of this object can't be set to ccActionStart(1),  if the value of object cefCCGlobalFullScanStatus is ccStatusRunning(2).  The value of this object will be set to cefActionNone(1) when the full scan consistency checkers have never been activated.  A Management Station cannot set the value of this object to cefActionNone(1)
            	**type**\:  :py:class:`CefCCAction <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefCCAction>`
            
            	**config**\: False
            
            .. attribute:: cefccglobalfullscanstatus
            
            	Indicates the status of the full scan consistency checker request
            	**type**\:  :py:class:`CefCCStatus <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefCCStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.CefCCGlobalTable.CefCCGlobalEntry, self).__init__()

                self.yang_name = "cefCCGlobalEntry"
                self.yang_parent_name = "cefCCGlobalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ceffibipversion']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ceffibipversion', (YLeaf(YType.enumeration, 'cefFIBIpVersion'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefIpVersion', '')])),
                    ('cefccglobalautorepairenabled', (YLeaf(YType.boolean, 'cefCCGlobalAutoRepairEnabled'), ['bool'])),
                    ('cefccglobalautorepairdelay', (YLeaf(YType.uint32, 'cefCCGlobalAutoRepairDelay'), ['int'])),
                    ('cefccglobalautorepairholddown', (YLeaf(YType.uint32, 'cefCCGlobalAutoRepairHoldDown'), ['int'])),
                    ('cefccglobalerrormsgenabled', (YLeaf(YType.boolean, 'cefCCGlobalErrorMsgEnabled'), ['bool'])),
                    ('cefccglobalfullscanaction', (YLeaf(YType.enumeration, 'cefCCGlobalFullScanAction'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefCCAction', '')])),
                    ('cefccglobalfullscanstatus', (YLeaf(YType.enumeration, 'cefCCGlobalFullScanStatus'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefCCStatus', '')])),
                ])
                self.ceffibipversion = None
                self.cefccglobalautorepairenabled = None
                self.cefccglobalautorepairdelay = None
                self.cefccglobalautorepairholddown = None
                self.cefccglobalerrormsgenabled = None
                self.cefccglobalfullscanaction = None
                self.cefccglobalfullscanstatus = None
                self._segment_path = lambda: "cefCCGlobalEntry" + "[cefFIBIpVersion='" + str(self.ceffibipversion) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefCCGlobalTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.CefCCGlobalTable.CefCCGlobalEntry, ['ceffibipversion', 'cefccglobalautorepairenabled', 'cefccglobalautorepairdelay', 'cefccglobalautorepairholddown', 'cefccglobalerrormsgenabled', 'cefccglobalfullscanaction', 'cefccglobalfullscanstatus'], name, value)




    class CefCCTypeTable(Entity):
        """
        This table contains CEF consistency
        checker types specific parameters on the managed device.
        
        All detected inconsistency are signaled to the
        Management Station via cefInconsistencyDetection
        notification.
        
        .. attribute:: cefcctypeentry
        
        	If the managed device supports CEF, each entry contains the consistency  checker statistics for a consistency  checker type. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device
        	**type**\: list of  		 :py:class:`CefCCTypeEntry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefCCTypeTable.CefCCTypeEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefCCTypeTable, self).__init__()

            self.yang_name = "cefCCTypeTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefCCTypeEntry", ("cefcctypeentry", CISCOCEFMIB.CefCCTypeTable.CefCCTypeEntry))])
            self._leafs = OrderedDict()

            self.cefcctypeentry = YList(self)
            self._segment_path = lambda: "cefCCTypeTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefCCTypeTable, [], name, value)


        class CefCCTypeEntry(Entity):
            """
            If the managed device supports CEF,
            each entry contains the consistency 
            checker statistics for a consistency 
            checker type.
            A row may exist for each IP version type
            (v4 and v6) depending upon the IP version
            supported on the device.
            
            .. attribute:: ceffibipversion  (key)
            
            	
            	**type**\:  :py:class:`CefIpVersion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefIpVersion>`
            
            	**config**\: False
            
            .. attribute:: cefcctype  (key)
            
            	Type of the consistency checker
            	**type**\:  :py:class:`CefCCType <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefCCType>`
            
            	**config**\: False
            
            .. attribute:: cefccenabled
            
            	Enables the passive consistency checker. Passive consistency checkers are disabled by default.  Full\-scan consistency checkers are always enabled. An attempt to set this object to 'false' for an active consistency checker will result in 'wrongValue' error
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cefcccount
            
            	The maximum number of prefixes to check per scan.  The default value for this object  depends upon the consistency checker type.  The value of this object will be irrelevant  for some of the consistency checkers and will be set to 0.  A Management Station cannot set the value of this object to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cefccperiod
            
            	The period between scans for the consistency checker
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: cefccqueriessent
            
            	Number of prefix consistency queries sent to CEF forwarding databases by this consistency checker
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cefccqueriesignored
            
            	Number of prefix consistency queries for which the consistency checks were not performed by this  consistency checker. This may be because of some internal error or resource failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cefccquerieschecked
            
            	Number of prefix consistency queries processed by this  consistency checker
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cefccqueriesiterated
            
            	Number of prefix consistency queries iterated back to the master database by this consistency checker
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.CefCCTypeTable.CefCCTypeEntry, self).__init__()

                self.yang_name = "cefCCTypeEntry"
                self.yang_parent_name = "cefCCTypeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ceffibipversion','cefcctype']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ceffibipversion', (YLeaf(YType.enumeration, 'cefFIBIpVersion'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefIpVersion', '')])),
                    ('cefcctype', (YLeaf(YType.enumeration, 'cefCCType'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefCCType', '')])),
                    ('cefccenabled', (YLeaf(YType.boolean, 'cefCCEnabled'), ['bool'])),
                    ('cefcccount', (YLeaf(YType.uint32, 'cefCCCount'), ['int'])),
                    ('cefccperiod', (YLeaf(YType.uint32, 'cefCCPeriod'), ['int'])),
                    ('cefccqueriessent', (YLeaf(YType.uint32, 'cefCCQueriesSent'), ['int'])),
                    ('cefccqueriesignored', (YLeaf(YType.uint32, 'cefCCQueriesIgnored'), ['int'])),
                    ('cefccquerieschecked', (YLeaf(YType.uint32, 'cefCCQueriesChecked'), ['int'])),
                    ('cefccqueriesiterated', (YLeaf(YType.uint32, 'cefCCQueriesIterated'), ['int'])),
                ])
                self.ceffibipversion = None
                self.cefcctype = None
                self.cefccenabled = None
                self.cefcccount = None
                self.cefccperiod = None
                self.cefccqueriessent = None
                self.cefccqueriesignored = None
                self.cefccquerieschecked = None
                self.cefccqueriesiterated = None
                self._segment_path = lambda: "cefCCTypeEntry" + "[cefFIBIpVersion='" + str(self.ceffibipversion) + "']" + "[cefCCType='" + str(self.cefcctype) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefCCTypeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.CefCCTypeTable.CefCCTypeEntry, ['ceffibipversion', 'cefcctype', 'cefccenabled', 'cefcccount', 'cefccperiod', 'cefccqueriessent', 'cefccqueriesignored', 'cefccquerieschecked', 'cefccqueriesiterated'], name, value)




    class CefInconsistencyRecordTable(Entity):
        """
        This table contains CEF inconsistency
        records.
        
        .. attribute:: cefinconsistencyrecordentry
        
        	If the managed device supports CEF, each entry contains the inconsistency  record
        	**type**\: list of  		 :py:class:`CefInconsistencyRecordEntry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefInconsistencyRecordTable.CefInconsistencyRecordEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefInconsistencyRecordTable, self).__init__()

            self.yang_name = "cefInconsistencyRecordTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefInconsistencyRecordEntry", ("cefinconsistencyrecordentry", CISCOCEFMIB.CefInconsistencyRecordTable.CefInconsistencyRecordEntry))])
            self._leafs = OrderedDict()

            self.cefinconsistencyrecordentry = YList(self)
            self._segment_path = lambda: "cefInconsistencyRecordTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefInconsistencyRecordTable, [], name, value)


        class CefInconsistencyRecordEntry(Entity):
            """
            If the managed device supports CEF,
            each entry contains the inconsistency 
            record.
            
            .. attribute:: ceffibipversion  (key)
            
            	
            	**type**\:  :py:class:`CefIpVersion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefIpVersion>`
            
            	**config**\: False
            
            .. attribute:: cefinconsistencyrecid  (key)
            
            	The locally arbitrary, but unique identifier associated with this inconsistency record entry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cefinconsistencyprefixtype
            
            	The network prefix type associated with this inconsistency record
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: cefinconsistencyprefixaddr
            
            	The network prefix address associated with this  inconsistency record.  The type of this address is determined by the value of the cefInconsistencyPrefixType object
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: cefinconsistencyprefixlen
            
            	Length in bits of the inconsistency address prefix
            	**type**\: int
            
            	**range:** 0..2040
            
            	**config**\: False
            
            .. attribute:: cefinconsistencyvrfname
            
            	Vrf name associated with this inconsistency record
            	**type**\: str
            
            	**length:** 0..31
            
            	**config**\: False
            
            .. attribute:: cefinconsistencycctype
            
            	The type of consistency checker who generated this inconsistency record
            	**type**\:  :py:class:`CefCCType <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefCCType>`
            
            	**config**\: False
            
            .. attribute:: cefinconsistencyentity
            
            	The entity for which this inconsistency record was  generated. The value of this object will be  irrelevant and will be set to 0 when the inconsisency  record is applicable for all the entities
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cefinconsistencyreason
            
            	The reason for generating this inconsistency record.   missing(1)\:        the prefix is missing  checksumErr(2)\:    checksum error was found  unknown(3)\:        reason is unknown
            	**type**\:  :py:class:`CefInconsistencyReason <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefInconsistencyRecordTable.CefInconsistencyRecordEntry.CefInconsistencyReason>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.CefInconsistencyRecordTable.CefInconsistencyRecordEntry, self).__init__()

                self.yang_name = "cefInconsistencyRecordEntry"
                self.yang_parent_name = "cefInconsistencyRecordTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ceffibipversion','cefinconsistencyrecid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ceffibipversion', (YLeaf(YType.enumeration, 'cefFIBIpVersion'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefIpVersion', '')])),
                    ('cefinconsistencyrecid', (YLeaf(YType.int32, 'cefInconsistencyRecId'), ['int'])),
                    ('cefinconsistencyprefixtype', (YLeaf(YType.enumeration, 'cefInconsistencyPrefixType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('cefinconsistencyprefixaddr', (YLeaf(YType.str, 'cefInconsistencyPrefixAddr'), ['str'])),
                    ('cefinconsistencyprefixlen', (YLeaf(YType.uint32, 'cefInconsistencyPrefixLen'), ['int'])),
                    ('cefinconsistencyvrfname', (YLeaf(YType.str, 'cefInconsistencyVrfName'), ['str'])),
                    ('cefinconsistencycctype', (YLeaf(YType.enumeration, 'cefInconsistencyCCType'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefCCType', '')])),
                    ('cefinconsistencyentity', (YLeaf(YType.int32, 'cefInconsistencyEntity'), ['int'])),
                    ('cefinconsistencyreason', (YLeaf(YType.enumeration, 'cefInconsistencyReason'), [('ydk.models.cisco_ios_xe.CISCO_CEF_MIB', 'CISCOCEFMIB', 'CefInconsistencyRecordTable.CefInconsistencyRecordEntry.CefInconsistencyReason')])),
                ])
                self.ceffibipversion = None
                self.cefinconsistencyrecid = None
                self.cefinconsistencyprefixtype = None
                self.cefinconsistencyprefixaddr = None
                self.cefinconsistencyprefixlen = None
                self.cefinconsistencyvrfname = None
                self.cefinconsistencycctype = None
                self.cefinconsistencyentity = None
                self.cefinconsistencyreason = None
                self._segment_path = lambda: "cefInconsistencyRecordEntry" + "[cefFIBIpVersion='" + str(self.ceffibipversion) + "']" + "[cefInconsistencyRecId='" + str(self.cefinconsistencyrecid) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefInconsistencyRecordTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.CefInconsistencyRecordTable.CefInconsistencyRecordEntry, ['ceffibipversion', 'cefinconsistencyrecid', 'cefinconsistencyprefixtype', 'cefinconsistencyprefixaddr', 'cefinconsistencyprefixlen', 'cefinconsistencyvrfname', 'cefinconsistencycctype', 'cefinconsistencyentity', 'cefinconsistencyreason'], name, value)

            class CefInconsistencyReason(Enum):
                """
                CefInconsistencyReason (Enum Class)

                The reason for generating this inconsistency record. 

                missing(1)\:        the prefix is missing

                checksumErr(2)\:    checksum error was found

                unknown(3)\:        reason is unknown

                .. data:: missing = 1

                .. data:: checksumErr = 2

                .. data:: unknown = 3

                """

                missing = Enum.YLeaf(1, "missing")

                checksumErr = Enum.YLeaf(2, "checksumErr")

                unknown = Enum.YLeaf(3, "unknown")





    class CefStatsPrefixLenTable(Entity):
        """
        This table specifies the CEF stats based
        on the Prefix Length.
        
        .. attribute:: cefstatsprefixlenentry
        
        	If CEF is enabled on the Managed device and if CEF accounting is set to enable  prefix length based accounting (value of  cefCfgAccountingMap object in the  cefCfgEntry is set to enable 'prefixLength'  accounting), each entry contains the traffic  statistics for a prefix length. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`CefStatsPrefixLenEntry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefStatsPrefixLenTable.CefStatsPrefixLenEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefStatsPrefixLenTable, self).__init__()

            self.yang_name = "cefStatsPrefixLenTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefStatsPrefixLenEntry", ("cefstatsprefixlenentry", CISCOCEFMIB.CefStatsPrefixLenTable.CefStatsPrefixLenEntry))])
            self._leafs = OrderedDict()

            self.cefstatsprefixlenentry = YList(self)
            self._segment_path = lambda: "cefStatsPrefixLenTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefStatsPrefixLenTable, [], name, value)


        class CefStatsPrefixLenEntry(Entity):
            """
            If CEF is enabled on the Managed device
            and if CEF accounting is set to enable 
            prefix length based accounting (value of 
            cefCfgAccountingMap object in the 
            cefCfgEntry is set to enable 'prefixLength' 
            accounting), each entry contains the traffic 
            statistics for a prefix length.
            A row may exist for each IP version type
            (v4 and v6) depending upon the IP version
            supported on the device.
            
            entPhysicalIndex is also an index for this
            table which represents entities of
            'module' entPhysicalClass which are capable
            of running CEF.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: ceffibipversion  (key)
            
            	
            	**type**\:  :py:class:`CefIpVersion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefIpVersion>`
            
            	**config**\: False
            
            .. attribute:: cefstatsprefixlen  (key)
            
            	Length in bits of the Destination IP prefix. As 0.0.0.0/0 is a valid prefix, hence  0 is a valid prefix length
            	**type**\: int
            
            	**range:** 0..2040
            
            	**config**\: False
            
            .. attribute:: cefstatsprefixqueries
            
            	Number of queries received in the FIB database  for the specified IP prefix length
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cefstatsprefixhcqueries
            
            	Number of queries received in the FIB database for the specified IP prefix length. This object is a 64\-bit version of  cefStatsPrefixQueries
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: cefstatsprefixinserts
            
            	Number of insert operations performed to the FIB  database for the specified IP prefix length
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cefstatsprefixhcinserts
            
            	Number of insert operations performed to the FIB  database for the specified IP prefix length. This object is a 64\-bit version of  cefStatsPrefixInsert
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: cefstatsprefixdeletes
            
            	Number of delete operations performed to the FIB  database for the specified IP prefix length
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cefstatsprefixhcdeletes
            
            	Number of delete operations performed to the FIB  database for the specified IP prefix length. This object is a 64\-bit version of  cefStatsPrefixDelete
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            .. attribute:: cefstatsprefixelements
            
            	Total number of elements in the FIB database for the specified IP prefix length
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cefstatsprefixhcelements
            
            	Total number of elements in the FIB database for the specified IP prefix length. This object is a 64\-bit version of  cefStatsPrefixElements
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.CefStatsPrefixLenTable.CefStatsPrefixLenEntry, self).__init__()

                self.yang_name = "cefStatsPrefixLenEntry"
                self.yang_parent_name = "cefStatsPrefixLenTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','ceffibipversion','cefstatsprefixlen']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('ceffibipversion', (YLeaf(YType.enumeration, 'cefFIBIpVersion'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefIpVersion', '')])),
                    ('cefstatsprefixlen', (YLeaf(YType.uint32, 'cefStatsPrefixLen'), ['int'])),
                    ('cefstatsprefixqueries', (YLeaf(YType.uint32, 'cefStatsPrefixQueries'), ['int'])),
                    ('cefstatsprefixhcqueries', (YLeaf(YType.uint64, 'cefStatsPrefixHCQueries'), ['int'])),
                    ('cefstatsprefixinserts', (YLeaf(YType.uint32, 'cefStatsPrefixInserts'), ['int'])),
                    ('cefstatsprefixhcinserts', (YLeaf(YType.uint64, 'cefStatsPrefixHCInserts'), ['int'])),
                    ('cefstatsprefixdeletes', (YLeaf(YType.uint32, 'cefStatsPrefixDeletes'), ['int'])),
                    ('cefstatsprefixhcdeletes', (YLeaf(YType.uint64, 'cefStatsPrefixHCDeletes'), ['int'])),
                    ('cefstatsprefixelements', (YLeaf(YType.uint32, 'cefStatsPrefixElements'), ['int'])),
                    ('cefstatsprefixhcelements', (YLeaf(YType.uint64, 'cefStatsPrefixHCElements'), ['int'])),
                ])
                self.entphysicalindex = None
                self.ceffibipversion = None
                self.cefstatsprefixlen = None
                self.cefstatsprefixqueries = None
                self.cefstatsprefixhcqueries = None
                self.cefstatsprefixinserts = None
                self.cefstatsprefixhcinserts = None
                self.cefstatsprefixdeletes = None
                self.cefstatsprefixhcdeletes = None
                self.cefstatsprefixelements = None
                self.cefstatsprefixhcelements = None
                self._segment_path = lambda: "cefStatsPrefixLenEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefFIBIpVersion='" + str(self.ceffibipversion) + "']" + "[cefStatsPrefixLen='" + str(self.cefstatsprefixlen) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefStatsPrefixLenTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.CefStatsPrefixLenTable.CefStatsPrefixLenEntry, ['entphysicalindex', 'ceffibipversion', 'cefstatsprefixlen', 'cefstatsprefixqueries', 'cefstatsprefixhcqueries', 'cefstatsprefixinserts', 'cefstatsprefixhcinserts', 'cefstatsprefixdeletes', 'cefstatsprefixhcdeletes', 'cefstatsprefixelements', 'cefstatsprefixhcelements'], name, value)




    class CefSwitchingStatsTable(Entity):
        """
        This table specifies the CEF switch stats.
        
        .. attribute:: cefswitchingstatsentry
        
        	If CEF is enabled on the Managed device, each entry specifies the switching stats. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`CefSwitchingStatsEntry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.CefSwitchingStatsTable.CefSwitchingStatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.CefSwitchingStatsTable, self).__init__()

            self.yang_name = "cefSwitchingStatsTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cefSwitchingStatsEntry", ("cefswitchingstatsentry", CISCOCEFMIB.CefSwitchingStatsTable.CefSwitchingStatsEntry))])
            self._leafs = OrderedDict()

            self.cefswitchingstatsentry = YList(self)
            self._segment_path = lambda: "cefSwitchingStatsTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.CefSwitchingStatsTable, [], name, value)


        class CefSwitchingStatsEntry(Entity):
            """
            If CEF is enabled on the Managed device,
            each entry specifies the switching stats.
            A row may exist for each IP version type
            (v4 and v6) depending upon the IP version
            supported on the device.
            
            entPhysicalIndex is also an index for this
            table which represents entities of
            'module' entPhysicalClass which are capable
            of running CEF.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: ceffibipversion  (key)
            
            	
            	**type**\:  :py:class:`CefIpVersion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefIpVersion>`
            
            	**config**\: False
            
            .. attribute:: cefswitchingindex  (key)
            
            	The locally arbitrary, but unique identifier associated with this switching stats entry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cefswitchingpath
            
            	Switch path where the feature was executed. Available switch paths are platform\-dependent. Following are the examples of switching paths\:     RIB \: switching with CEF assistance     Low\-end switching (LES) \: CEF switch path     PAS \: CEF turbo switch path
            	**type**\: str
            
            	**length:** 1..32
            
            	**config**\: False
            
            .. attribute:: cefswitchingdrop
            
            	Number of packets dropped by CEF
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cefswitchinghcdrop
            
            	Number of packets dropped by CEF. This object is a 64\-bit version of cefSwitchingDrop
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cefswitchingpunt
            
            	Number of packets that could not be switched in the normal path and were punted to the next\-fastest switching vector
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cefswitchinghcpunt
            
            	Number of packets that could not be switched in the normal path and were punted to the next\-fastest switching vector. This object is a 64\-bit version of cefSwitchingPunt
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cefswitchingpunt2host
            
            	Number of packets that could not be switched in the normal path and were punted to the host (process switching path).  For most of the switching paths, the value of this object may be similar to cefSwitchingPunt
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: packets
            
            .. attribute:: cefswitchinghcpunt2host
            
            	Number of packets that could not be switched in the normal path and were punted to the host (process switching path).  For most of the switching paths, the value of this object may be similar to cefSwitchingPunt. This object is a 64\-bit version of cefSwitchingPunt2Host
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: packets
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.CefSwitchingStatsTable.CefSwitchingStatsEntry, self).__init__()

                self.yang_name = "cefSwitchingStatsEntry"
                self.yang_parent_name = "cefSwitchingStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','ceffibipversion','cefswitchingindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('ceffibipversion', (YLeaf(YType.enumeration, 'cefFIBIpVersion'), [('ydk.models.cisco_ios_xe.CISCO_CEF_TC', 'CefIpVersion', '')])),
                    ('cefswitchingindex', (YLeaf(YType.int32, 'cefSwitchingIndex'), ['int'])),
                    ('cefswitchingpath', (YLeaf(YType.str, 'cefSwitchingPath'), ['str'])),
                    ('cefswitchingdrop', (YLeaf(YType.uint32, 'cefSwitchingDrop'), ['int'])),
                    ('cefswitchinghcdrop', (YLeaf(YType.uint64, 'cefSwitchingHCDrop'), ['int'])),
                    ('cefswitchingpunt', (YLeaf(YType.uint32, 'cefSwitchingPunt'), ['int'])),
                    ('cefswitchinghcpunt', (YLeaf(YType.uint64, 'cefSwitchingHCPunt'), ['int'])),
                    ('cefswitchingpunt2host', (YLeaf(YType.uint32, 'cefSwitchingPunt2Host'), ['int'])),
                    ('cefswitchinghcpunt2host', (YLeaf(YType.uint64, 'cefSwitchingHCPunt2Host'), ['int'])),
                ])
                self.entphysicalindex = None
                self.ceffibipversion = None
                self.cefswitchingindex = None
                self.cefswitchingpath = None
                self.cefswitchingdrop = None
                self.cefswitchinghcdrop = None
                self.cefswitchingpunt = None
                self.cefswitchinghcpunt = None
                self.cefswitchingpunt2host = None
                self.cefswitchinghcpunt2host = None
                self._segment_path = lambda: "cefSwitchingStatsEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefFIBIpVersion='" + str(self.ceffibipversion) + "']" + "[cefSwitchingIndex='" + str(self.cefswitchingindex) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefSwitchingStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.CefSwitchingStatsTable.CefSwitchingStatsEntry, ['entphysicalindex', 'ceffibipversion', 'cefswitchingindex', 'cefswitchingpath', 'cefswitchingdrop', 'cefswitchinghcdrop', 'cefswitchingpunt', 'cefswitchinghcpunt', 'cefswitchingpunt2host', 'cefswitchinghcpunt2host'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOCEFMIB()
        return self._top_entity



