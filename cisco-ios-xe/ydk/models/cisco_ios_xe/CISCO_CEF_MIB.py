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
    
    	
    	**type**\:  :py:class:`Ceffib <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Ceffib>`
    
    .. attribute:: cefcc
    
    	
    	**type**\:  :py:class:`Cefcc <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefcc>`
    
    .. attribute:: cefnotifcntl
    
    	
    	**type**\:  :py:class:`Cefnotifcntl <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefnotifcntl>`
    
    .. attribute:: ceffibsummarytable
    
    	This table contains the summary information for the cefPrefixTable
    	**type**\:  :py:class:`Ceffibsummarytable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Ceffibsummarytable>`
    
    .. attribute:: cefprefixtable
    
    	A list of CEF forwarding prefixes
    	**type**\:  :py:class:`Cefprefixtable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefprefixtable>`
    
    .. attribute:: ceflmprefixtable
    
    	A table of Longest Match Prefix Query requests.  Generator application should utilize the cefLMPrefixSpinLock to try to avoid collisions. See DESCRIPTION clause of cefLMPrefixSpinLock
    	**type**\:  :py:class:`Ceflmprefixtable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Ceflmprefixtable>`
    
    .. attribute:: cefpathtable
    
    	CEF prefix path is a valid route to reach to a  destination IP prefix. Multiple paths may exist  out of a router to the same destination prefix.  This table specify lists of CEF paths
    	**type**\:  :py:class:`Cefpathtable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefpathtable>`
    
    .. attribute:: cefadjsummarytable
    
    	This table contains the summary information for the cefAdjTable
    	**type**\:  :py:class:`Cefadjsummarytable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefadjsummarytable>`
    
    .. attribute:: cefadjtable
    
    	A list of CEF adjacencies
    	**type**\:  :py:class:`Cefadjtable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefadjtable>`
    
    .. attribute:: ceffeselectiontable
    
    	A list of forwarding element selection entries
    	**type**\:  :py:class:`Ceffeselectiontable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Ceffeselectiontable>`
    
    .. attribute:: cefcfgtable
    
    	This table contains global config parameter  of CEF on the Managed device
    	**type**\:  :py:class:`Cefcfgtable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefcfgtable>`
    
    .. attribute:: cefresourcetable
    
    	This table contains global resource  information of CEF on the Managed device
    	**type**\:  :py:class:`Cefresourcetable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefresourcetable>`
    
    .. attribute:: cefinttable
    
    	This Table contains interface specific information of CEF on the Managed device
    	**type**\:  :py:class:`Cefinttable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefinttable>`
    
    .. attribute:: cefpeertable
    
    	Entity acting as RP (Routing Processor) keeps the CEF states for the line card entities and communicates with the line card entities using XDR. This Table contains the CEF information  related to peer entities on the managed device
    	**type**\:  :py:class:`Cefpeertable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefpeertable>`
    
    .. attribute:: cefpeerfibtable
    
    	Entity acting as RP (Routing Processor) keep the CEF FIB states for the line card entities and communicate with the line card entities using XDR. This Table contains the CEF FIB State  related to peer entities on the managed device
    	**type**\:  :py:class:`Cefpeerfibtable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefpeerfibtable>`
    
    .. attribute:: cefccglobaltable
    
    	This table contains CEF consistency checker (CC) global parameters for the managed device
    	**type**\:  :py:class:`Cefccglobaltable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefccglobaltable>`
    
    .. attribute:: cefcctypetable
    
    	This table contains CEF consistency checker types specific parameters on the managed device.  All detected inconsistency are signaled to the Management Station via cefInconsistencyDetection notification
    	**type**\:  :py:class:`Cefcctypetable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefcctypetable>`
    
    .. attribute:: cefinconsistencyrecordtable
    
    	This table contains CEF inconsistency records
    	**type**\:  :py:class:`Cefinconsistencyrecordtable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefinconsistencyrecordtable>`
    
    .. attribute:: cefstatsprefixlentable
    
    	This table specifies the CEF stats based on the Prefix Length
    	**type**\:  :py:class:`Cefstatsprefixlentable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefstatsprefixlentable>`
    
    .. attribute:: cefswitchingstatstable
    
    	This table specifies the CEF switch stats
    	**type**\:  :py:class:`Cefswitchingstatstable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefswitchingstatstable>`
    
    

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
        self._child_container_classes = OrderedDict([("cefFIB", ("ceffib", CISCOCEFMIB.Ceffib)), ("cefCC", ("cefcc", CISCOCEFMIB.Cefcc)), ("cefNotifCntl", ("cefnotifcntl", CISCOCEFMIB.Cefnotifcntl)), ("cefFIBSummaryTable", ("ceffibsummarytable", CISCOCEFMIB.Ceffibsummarytable)), ("cefPrefixTable", ("cefprefixtable", CISCOCEFMIB.Cefprefixtable)), ("cefLMPrefixTable", ("ceflmprefixtable", CISCOCEFMIB.Ceflmprefixtable)), ("cefPathTable", ("cefpathtable", CISCOCEFMIB.Cefpathtable)), ("cefAdjSummaryTable", ("cefadjsummarytable", CISCOCEFMIB.Cefadjsummarytable)), ("cefAdjTable", ("cefadjtable", CISCOCEFMIB.Cefadjtable)), ("cefFESelectionTable", ("ceffeselectiontable", CISCOCEFMIB.Ceffeselectiontable)), ("cefCfgTable", ("cefcfgtable", CISCOCEFMIB.Cefcfgtable)), ("cefResourceTable", ("cefresourcetable", CISCOCEFMIB.Cefresourcetable)), ("cefIntTable", ("cefinttable", CISCOCEFMIB.Cefinttable)), ("cefPeerTable", ("cefpeertable", CISCOCEFMIB.Cefpeertable)), ("cefPeerFIBTable", ("cefpeerfibtable", CISCOCEFMIB.Cefpeerfibtable)), ("cefCCGlobalTable", ("cefccglobaltable", CISCOCEFMIB.Cefccglobaltable)), ("cefCCTypeTable", ("cefcctypetable", CISCOCEFMIB.Cefcctypetable)), ("cefInconsistencyRecordTable", ("cefinconsistencyrecordtable", CISCOCEFMIB.Cefinconsistencyrecordtable)), ("cefStatsPrefixLenTable", ("cefstatsprefixlentable", CISCOCEFMIB.Cefstatsprefixlentable)), ("cefSwitchingStatsTable", ("cefswitchingstatstable", CISCOCEFMIB.Cefswitchingstatstable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ceffib = CISCOCEFMIB.Ceffib()
        self.ceffib.parent = self
        self._children_name_map["ceffib"] = "cefFIB"
        self._children_yang_names.add("cefFIB")

        self.cefcc = CISCOCEFMIB.Cefcc()
        self.cefcc.parent = self
        self._children_name_map["cefcc"] = "cefCC"
        self._children_yang_names.add("cefCC")

        self.cefnotifcntl = CISCOCEFMIB.Cefnotifcntl()
        self.cefnotifcntl.parent = self
        self._children_name_map["cefnotifcntl"] = "cefNotifCntl"
        self._children_yang_names.add("cefNotifCntl")

        self.ceffibsummarytable = CISCOCEFMIB.Ceffibsummarytable()
        self.ceffibsummarytable.parent = self
        self._children_name_map["ceffibsummarytable"] = "cefFIBSummaryTable"
        self._children_yang_names.add("cefFIBSummaryTable")

        self.cefprefixtable = CISCOCEFMIB.Cefprefixtable()
        self.cefprefixtable.parent = self
        self._children_name_map["cefprefixtable"] = "cefPrefixTable"
        self._children_yang_names.add("cefPrefixTable")

        self.ceflmprefixtable = CISCOCEFMIB.Ceflmprefixtable()
        self.ceflmprefixtable.parent = self
        self._children_name_map["ceflmprefixtable"] = "cefLMPrefixTable"
        self._children_yang_names.add("cefLMPrefixTable")

        self.cefpathtable = CISCOCEFMIB.Cefpathtable()
        self.cefpathtable.parent = self
        self._children_name_map["cefpathtable"] = "cefPathTable"
        self._children_yang_names.add("cefPathTable")

        self.cefadjsummarytable = CISCOCEFMIB.Cefadjsummarytable()
        self.cefadjsummarytable.parent = self
        self._children_name_map["cefadjsummarytable"] = "cefAdjSummaryTable"
        self._children_yang_names.add("cefAdjSummaryTable")

        self.cefadjtable = CISCOCEFMIB.Cefadjtable()
        self.cefadjtable.parent = self
        self._children_name_map["cefadjtable"] = "cefAdjTable"
        self._children_yang_names.add("cefAdjTable")

        self.ceffeselectiontable = CISCOCEFMIB.Ceffeselectiontable()
        self.ceffeselectiontable.parent = self
        self._children_name_map["ceffeselectiontable"] = "cefFESelectionTable"
        self._children_yang_names.add("cefFESelectionTable")

        self.cefcfgtable = CISCOCEFMIB.Cefcfgtable()
        self.cefcfgtable.parent = self
        self._children_name_map["cefcfgtable"] = "cefCfgTable"
        self._children_yang_names.add("cefCfgTable")

        self.cefresourcetable = CISCOCEFMIB.Cefresourcetable()
        self.cefresourcetable.parent = self
        self._children_name_map["cefresourcetable"] = "cefResourceTable"
        self._children_yang_names.add("cefResourceTable")

        self.cefinttable = CISCOCEFMIB.Cefinttable()
        self.cefinttable.parent = self
        self._children_name_map["cefinttable"] = "cefIntTable"
        self._children_yang_names.add("cefIntTable")

        self.cefpeertable = CISCOCEFMIB.Cefpeertable()
        self.cefpeertable.parent = self
        self._children_name_map["cefpeertable"] = "cefPeerTable"
        self._children_yang_names.add("cefPeerTable")

        self.cefpeerfibtable = CISCOCEFMIB.Cefpeerfibtable()
        self.cefpeerfibtable.parent = self
        self._children_name_map["cefpeerfibtable"] = "cefPeerFIBTable"
        self._children_yang_names.add("cefPeerFIBTable")

        self.cefccglobaltable = CISCOCEFMIB.Cefccglobaltable()
        self.cefccglobaltable.parent = self
        self._children_name_map["cefccglobaltable"] = "cefCCGlobalTable"
        self._children_yang_names.add("cefCCGlobalTable")

        self.cefcctypetable = CISCOCEFMIB.Cefcctypetable()
        self.cefcctypetable.parent = self
        self._children_name_map["cefcctypetable"] = "cefCCTypeTable"
        self._children_yang_names.add("cefCCTypeTable")

        self.cefinconsistencyrecordtable = CISCOCEFMIB.Cefinconsistencyrecordtable()
        self.cefinconsistencyrecordtable.parent = self
        self._children_name_map["cefinconsistencyrecordtable"] = "cefInconsistencyRecordTable"
        self._children_yang_names.add("cefInconsistencyRecordTable")

        self.cefstatsprefixlentable = CISCOCEFMIB.Cefstatsprefixlentable()
        self.cefstatsprefixlentable.parent = self
        self._children_name_map["cefstatsprefixlentable"] = "cefStatsPrefixLenTable"
        self._children_yang_names.add("cefStatsPrefixLenTable")

        self.cefswitchingstatstable = CISCOCEFMIB.Cefswitchingstatstable()
        self.cefswitchingstatstable.parent = self
        self._children_name_map["cefswitchingstatstable"] = "cefSwitchingStatsTable"
        self._children_yang_names.add("cefSwitchingStatsTable")
        self._segment_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB"


    class Ceffib(Entity):
        """
        
        
        .. attribute:: ceflmprefixspinlock
        
        	An advisory lock used to allow cooperating SNMP Command Generator applications to coordinate their use of the Set operation in creating Longest Match Prefix Entries in cefLMPrefixTable.  When creating a new longest prefix match entry, the value of cefLMPrefixSpinLock should be retrieved.   The destination address should be determined to be unique by the SNMP Command Generator application by consulting the cefLMPrefixTable. Finally, the longest  prefix entry may be created (Set), including the advisory lock.         If another SNMP Command Generator application has altered the longest prefix entry in the meantime,  then the spin lock's value will have changed,  and so this creation will fail because it will specify the wrong value for the spin lock.  Since this is an advisory lock, the use of this lock is not enforced, but not using this lock may lead to conflict with the another SNMP command responder  application which may also be acting on the cefLMPrefixTable
        	**type**\: int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Ceffib, self).__init__()

            self.yang_name = "cefFIB"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ceflmprefixspinlock', YLeaf(YType.int32, 'cefLMPrefixSpinLock')),
            ])
            self.ceflmprefixspinlock = None
            self._segment_path = lambda: "cefFIB"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Ceffib, ['ceflmprefixspinlock'], name, value)


    class Cefcc(Entity):
        """
        
        
        .. attribute:: entlastinconsistencydetecttime
        
        	The value of sysUpTime at the time an inconsistency is detecetd
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: cefinconsistencyreset
        
        	Setting the value of this object to ccActionStart(1) will reset all the active consistency checkers.  The Management station should poll the  cefInconsistencyResetStatus object to get the  state of inconsistency reset operation.  This operation once started, cannot be aborted. Hence, the value of this object cannot be set to ccActionAbort(2).  The value of this object can't be set to ccActionStart(1),  if the value of object cefInconsistencyResetStatus is ccStatusRunning(2)
        	**type**\:  :py:class:`CefCCAction <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefCCAction>`
        
        .. attribute:: cefinconsistencyresetstatus
        
        	Indicates the status of the consistency reset request
        	**type**\:  :py:class:`CefCCStatus <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefCCStatus>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Cefcc, self).__init__()

            self.yang_name = "cefCC"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('entlastinconsistencydetecttime', YLeaf(YType.uint32, 'entLastInconsistencyDetectTime')),
                ('cefinconsistencyreset', YLeaf(YType.enumeration, 'cefInconsistencyReset')),
                ('cefinconsistencyresetstatus', YLeaf(YType.enumeration, 'cefInconsistencyResetStatus')),
            ])
            self.entlastinconsistencydetecttime = None
            self.cefinconsistencyreset = None
            self.cefinconsistencyresetstatus = None
            self._segment_path = lambda: "cefCC"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Cefcc, ['entlastinconsistencydetecttime', 'cefinconsistencyreset', 'cefinconsistencyresetstatus'], name, value)


    class Cefnotifcntl(Entity):
        """
        
        
        .. attribute:: cefresourcefailurenotifenable
        
        	Indicates whether or not a notification should be generated on the detection of CEF resource Failure
        	**type**\: bool
        
        .. attribute:: cefpeerstatechangenotifenable
        
        	Indicates whether or not a notification should be generated on the detection of CEF peer state change
        	**type**\: bool
        
        .. attribute:: cefpeerfibstatechangenotifenable
        
        	Indicates whether or not a notification should be generated on the detection of CEF FIB peer state change
        	**type**\: bool
        
        .. attribute:: cefnotifthrottlinginterval
        
        	This object controls the generation of the cefInconsistencyDetection notification.  If this object has a value of zero, then the throttle control is disabled.  If this object has a non\-zero value, then the agent must not generate more than one  cefInconsistencyDetection 'notification\-event' in the  indicated period, where a 'notification\-event' is the transmission of a single trap or inform PDU to a list of notification destinations.  If additional inconsistency is detected within the  throttling period, then notification\-events for these inconsistencies should be suppressed by the agent until the current throttling period expires.  At the end of a throttling period, one notification\-event should be generated if any inconsistency was detected since the start of the  throttling period. In such a case,  another throttling period is started right away.  An NMS should periodically poll cefInconsistencyRecordTable to detect any missed cefInconsistencyDetection notification\-events, e.g., due to throttling or transmission loss.   If cefNotifThrottlingInterval notification generation is enabled, the suggested default throttling period is 60 seconds, but generation of the cefInconsistencyDetection notification should be disabled by default.  If the agent is capable of storing non\-volatile configuration, then the value of this object must be restored after a re\-initialization of the management system.  The actual transmission of notifications is controlled via the MIB modules in RFC 3413
        	**type**\: int
        
        	**range:** 0..3600
        
        	**units**\: seconds
        
        .. attribute:: cefinconsistencynotifenable
        
        	Indicates whether cefInconsistencyDetection notification should be generated for this managed device
        	**type**\: bool
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Cefnotifcntl, self).__init__()

            self.yang_name = "cefNotifCntl"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cefresourcefailurenotifenable', YLeaf(YType.boolean, 'cefResourceFailureNotifEnable')),
                ('cefpeerstatechangenotifenable', YLeaf(YType.boolean, 'cefPeerStateChangeNotifEnable')),
                ('cefpeerfibstatechangenotifenable', YLeaf(YType.boolean, 'cefPeerFIBStateChangeNotifEnable')),
                ('cefnotifthrottlinginterval', YLeaf(YType.int32, 'cefNotifThrottlingInterval')),
                ('cefinconsistencynotifenable', YLeaf(YType.boolean, 'cefInconsistencyNotifEnable')),
            ])
            self.cefresourcefailurenotifenable = None
            self.cefpeerstatechangenotifenable = None
            self.cefpeerfibstatechangenotifenable = None
            self.cefnotifthrottlinginterval = None
            self.cefinconsistencynotifenable = None
            self._segment_path = lambda: "cefNotifCntl"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Cefnotifcntl, ['cefresourcefailurenotifenable', 'cefpeerstatechangenotifenable', 'cefpeerfibstatechangenotifenable', 'cefnotifthrottlinginterval', 'cefinconsistencynotifenable'], name, value)


    class Ceffibsummarytable(Entity):
        """
        This table contains the summary information
        for the cefPrefixTable.
        
        .. attribute:: ceffibsummaryentry
        
        	If CEF is enabled on the Managed device, each entry contains the FIB summary related attributes for the managed entity.  A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`Ceffibsummaryentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Ceffibsummarytable.Ceffibsummaryentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Ceffibsummarytable, self).__init__()

            self.yang_name = "cefFIBSummaryTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefFIBSummaryEntry", ("ceffibsummaryentry", CISCOCEFMIB.Ceffibsummarytable.Ceffibsummaryentry))])
            self._leafs = OrderedDict()

            self.ceffibsummaryentry = YList(self)
            self._segment_path = lambda: "cefFIBSummaryTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Ceffibsummarytable, [], name, value)


        class Ceffibsummaryentry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceffibipversion  (key)
            
            	The version of IP forwarding
            	**type**\:  :py:class:`CefIpVersion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefIpVersion>`
            
            .. attribute:: ceffibsummaryfwdprefixes
            
            	Total number of forwarding Prefixes in FIB for the IP version specified by cefFIBIpVersion object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.Ceffibsummarytable.Ceffibsummaryentry, self).__init__()

                self.yang_name = "cefFIBSummaryEntry"
                self.yang_parent_name = "cefFIBSummaryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','ceffibipversion']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('ceffibipversion', YLeaf(YType.enumeration, 'cefFIBIpVersion')),
                    ('ceffibsummaryfwdprefixes', YLeaf(YType.uint32, 'cefFIBSummaryFwdPrefixes')),
                ])
                self.entphysicalindex = None
                self.ceffibipversion = None
                self.ceffibsummaryfwdprefixes = None
                self._segment_path = lambda: "cefFIBSummaryEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefFIBIpVersion='" + str(self.ceffibipversion) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefFIBSummaryTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.Ceffibsummarytable.Ceffibsummaryentry, ['entphysicalindex', 'ceffibipversion', 'ceffibsummaryfwdprefixes'], name, value)


    class Cefprefixtable(Entity):
        """
        A list of CEF forwarding prefixes.
        
        .. attribute:: cefprefixentry
        
        	If CEF is enabled on the Managed device, each entry contains the forwarding  prefix attributes.   CEF prefix based non\-recursive stats are maintained in internal and external buckets (depending upon the  value of cefIntNonrecursiveAccouting object in the  CefIntEntry).  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`Cefprefixentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefprefixtable.Cefprefixentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Cefprefixtable, self).__init__()

            self.yang_name = "cefPrefixTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefPrefixEntry", ("cefprefixentry", CISCOCEFMIB.Cefprefixtable.Cefprefixentry))])
            self._leafs = OrderedDict()

            self.cefprefixentry = YList(self)
            self._segment_path = lambda: "cefPrefixTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Cefprefixtable, [], name, value)


        class Cefprefixentry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefprefixtype  (key)
            
            	The Network Prefix Type. This object specifies the address type used for cefPrefixAddr.  Prefix entries are only valid for the address type of ipv4(1) and ipv6(2)
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cefprefixaddr  (key)
            
            	The Network Prefix Address. The type of this address is determined by the value of the cefPrefixType object. This object is a Prefix Address containing the  prefix with length specified by cefPrefixLen.  Any bits beyond the length specified by cefPrefixLen are zeroed
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cefprefixlen  (key)
            
            	Length in bits of the FIB Address prefix
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: cefprefixforwardinginfo
            
            	This object indicates the associated forwarding element selection entries in cefFESelectionTable. The value of this object is index value (cefFESelectionName) of cefFESelectionTable
            	**type**\: str
            
            .. attribute:: cefprefixpkts
            
            	If CEF accounting is set to enable per prefix accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'perPrefix'  accounting), then this object represents the  number of packets switched to this prefix
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cefprefixhcpkts
            
            	If CEF accounting is set to enable per prefix accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'perPrefix'  accounting), then this object represents the  number of packets switched to this prefix.   This object is a 64\-bit version of  cefPrefixPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cefprefixbytes
            
            	If CEF accounting is set to enable per prefix accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'perPrefix'  accounting), then this object represents the  number of bytes switched to this prefix
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cefprefixhcbytes
            
            	If CEF accounting is set to enable per prefix accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'perPrefix'  accounting), then this object represents the  number of bytes switched to this prefix.  This object is a 64\-bit version of  cefPrefixBytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cefprefixinternalnrpkts
            
            	If CEF accounting is set to enable non\-recursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents the number of non\-recursive packets in the internal bucket switched using this prefix
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cefprefixinternalnrhcpkts
            
            	If CEF accounting is set to enable non\-recursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents the number of non\-recursive packets in the internal bucket switched using this prefix.  This object is a 64\-bit version of  cefPrefixInternalNRPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cefprefixinternalnrbytes
            
            	If CEF accounting is set to enable nonRecursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents  the number of non\-recursive bytes in the internal bucket switched using this prefix
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cefprefixinternalnrhcbytes
            
            	If CEF accounting is set to enable nonRecursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents  the number of non\-recursive bytes in the internal bucket switched using this prefix.  This object is a 64\-bit version of  cefPrefixInternalNRBytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cefprefixexternalnrpkts
            
            	If CEF accounting is set to enable non\-recursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents the number of non\-recursive packets in the external bucket switched using this prefix
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cefprefixexternalnrhcpkts
            
            	If CEF accounting is set to enable non\-recursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents the number of non\-recursive packets in the external bucket switched using this prefix.  This object is a 64\-bit version of  cefPrefixExternalNRPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cefprefixexternalnrbytes
            
            	If CEF accounting is set to enable nonRecursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents  the number of non\-recursive bytes in the external bucket switched using this prefix
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cefprefixexternalnrhcbytes
            
            	If CEF accounting is set to enable nonRecursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents  the number of non\-recursive bytes in the external bucket switched using this prefix.  This object is a 64\-bit version of  cefPrefixExternalNRBytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.Cefprefixtable.Cefprefixentry, self).__init__()

                self.yang_name = "cefPrefixEntry"
                self.yang_parent_name = "cefPrefixTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cefprefixtype','cefprefixaddr','cefprefixlen']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefprefixtype', YLeaf(YType.enumeration, 'cefPrefixType')),
                    ('cefprefixaddr', YLeaf(YType.str, 'cefPrefixAddr')),
                    ('cefprefixlen', YLeaf(YType.uint32, 'cefPrefixLen')),
                    ('cefprefixforwardinginfo', YLeaf(YType.str, 'cefPrefixForwardingInfo')),
                    ('cefprefixpkts', YLeaf(YType.uint32, 'cefPrefixPkts')),
                    ('cefprefixhcpkts', YLeaf(YType.uint64, 'cefPrefixHCPkts')),
                    ('cefprefixbytes', YLeaf(YType.uint32, 'cefPrefixBytes')),
                    ('cefprefixhcbytes', YLeaf(YType.uint64, 'cefPrefixHCBytes')),
                    ('cefprefixinternalnrpkts', YLeaf(YType.uint32, 'cefPrefixInternalNRPkts')),
                    ('cefprefixinternalnrhcpkts', YLeaf(YType.uint64, 'cefPrefixInternalNRHCPkts')),
                    ('cefprefixinternalnrbytes', YLeaf(YType.uint32, 'cefPrefixInternalNRBytes')),
                    ('cefprefixinternalnrhcbytes', YLeaf(YType.uint64, 'cefPrefixInternalNRHCBytes')),
                    ('cefprefixexternalnrpkts', YLeaf(YType.uint32, 'cefPrefixExternalNRPkts')),
                    ('cefprefixexternalnrhcpkts', YLeaf(YType.uint64, 'cefPrefixExternalNRHCPkts')),
                    ('cefprefixexternalnrbytes', YLeaf(YType.uint32, 'cefPrefixExternalNRBytes')),
                    ('cefprefixexternalnrhcbytes', YLeaf(YType.uint64, 'cefPrefixExternalNRHCBytes')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.Cefprefixtable.Cefprefixentry, ['entphysicalindex', 'cefprefixtype', 'cefprefixaddr', 'cefprefixlen', 'cefprefixforwardinginfo', 'cefprefixpkts', 'cefprefixhcpkts', 'cefprefixbytes', 'cefprefixhcbytes', 'cefprefixinternalnrpkts', 'cefprefixinternalnrhcpkts', 'cefprefixinternalnrbytes', 'cefprefixinternalnrhcbytes', 'cefprefixexternalnrpkts', 'cefprefixexternalnrhcpkts', 'cefprefixexternalnrbytes', 'cefprefixexternalnrhcbytes'], name, value)


    class Ceflmprefixtable(Entity):
        """
        A table of Longest Match Prefix Query requests.
        
        Generator application should utilize the
        cefLMPrefixSpinLock to try to avoid collisions.
        See DESCRIPTION clause of cefLMPrefixSpinLock.
        
        .. attribute:: ceflmprefixentry
        
        	If CEF is enabled on the managed device, then each entry represents a longest Match Prefix request.  A management station wishing to get the longest Match prefix for a given destination address should create the associate instance of the row status. The row status should be set to active(1) to initiate the request. Note that  this entire procedure may be initiated via a  single set request which specifies a row status  of createAndGo(4).  Once the request completes, the management station  should retrieve the values of the objects of  interest, and should then delete the entry.  In order  to prevent old entries from clogging the table,  entries will be aged out, but an entry will never be  deleted within 5 minutes of completion. Entries are lost after an agent restart.  I.e. to find out the longest prefix match for  destination address of A.B.C.D on entity whose entityPhysicalIndex is 1, the Management station will create an entry in cefLMPrefixTable with cefLMPrefixRowStatus.1(entPhysicalIndex).1(ipv4).A.B.C.D set to createAndGo(4). Management Station may query the value of objects cefLMPrefix and cefLMPrefixLen to find out the corresponding prefix entry from the cefPrefixTable once the value of cefLMPrefixState is set to matchFound(2).  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`Ceflmprefixentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Ceflmprefixtable.Ceflmprefixentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Ceflmprefixtable, self).__init__()

            self.yang_name = "cefLMPrefixTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefLMPrefixEntry", ("ceflmprefixentry", CISCOCEFMIB.Ceflmprefixtable.Ceflmprefixentry))])
            self._leafs = OrderedDict()

            self.ceflmprefixentry = YList(self)
            self._segment_path = lambda: "cefLMPrefixTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Ceflmprefixtable, [], name, value)


        class Ceflmprefixentry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceflmprefixdestaddrtype  (key)
            
            	The Destination Address Type. This object specifies the address type used for cefLMPrefixDestAddr.  Longest Match Prefix entries are only valid  for the address type of ipv4(1) and ipv6(2)
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: ceflmprefixdestaddr  (key)
            
            	The Destination Address. The type of this address is determined by the value of the cefLMPrefixDestAddrType object
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: ceflmprefixstate
            
            	Indicates the state of this prefix search request
            	**type**\:  :py:class:`CefPrefixSearchState <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefPrefixSearchState>`
            
            .. attribute:: ceflmprefixaddr
            
            	The Network Prefix Address. Index to the cefPrefixTable. The type of this address is determined by the value of the cefLMPrefixDestAddrType object
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: ceflmprefixlen
            
            	The Network Prefix Length. Index to the cefPrefixTable
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: ceflmprefixrowstatus
            
            	The status of this table entry.  Once the entry  status is set to active(1), the associated entry  cannot be modified until the request completes (cefLMPrefixState transitions to matchFound(2)  or noMatchFound(3)).  Once the longest match request has been created (i.e. the cefLMPrefixRowStatus has been made active), the entry cannot be modified \- the only operation possible after this is to delete the row
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.Ceflmprefixtable.Ceflmprefixentry, self).__init__()

                self.yang_name = "cefLMPrefixEntry"
                self.yang_parent_name = "cefLMPrefixTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','ceflmprefixdestaddrtype','ceflmprefixdestaddr']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('ceflmprefixdestaddrtype', YLeaf(YType.enumeration, 'cefLMPrefixDestAddrType')),
                    ('ceflmprefixdestaddr', YLeaf(YType.str, 'cefLMPrefixDestAddr')),
                    ('ceflmprefixstate', YLeaf(YType.enumeration, 'cefLMPrefixState')),
                    ('ceflmprefixaddr', YLeaf(YType.str, 'cefLMPrefixAddr')),
                    ('ceflmprefixlen', YLeaf(YType.uint32, 'cefLMPrefixLen')),
                    ('ceflmprefixrowstatus', YLeaf(YType.enumeration, 'cefLMPrefixRowStatus')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.Ceflmprefixtable.Ceflmprefixentry, ['entphysicalindex', 'ceflmprefixdestaddrtype', 'ceflmprefixdestaddr', 'ceflmprefixstate', 'ceflmprefixaddr', 'ceflmprefixlen', 'ceflmprefixrowstatus'], name, value)


    class Cefpathtable(Entity):
        """
        CEF prefix path is a valid route to reach to a 
        destination IP prefix. Multiple paths may exist 
        out of a router to the same destination prefix. 
        This table specify lists of CEF paths.
        
        .. attribute:: cefpathentry
        
        	If CEF is enabled on the Managed device, each entry contain a CEF prefix path.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`Cefpathentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefpathtable.Cefpathentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Cefpathtable, self).__init__()

            self.yang_name = "cefPathTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefPathEntry", ("cefpathentry", CISCOCEFMIB.Cefpathtable.Cefpathentry))])
            self._leafs = OrderedDict()

            self.cefpathentry = YList(self)
            self._segment_path = lambda: "cefPathTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Cefpathtable, [], name, value)


        class Cefpathentry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefprefixtype  (key)
            
            	
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cefprefixaddr  (key)
            
            	
            	**type**\: str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cefprefixaddr <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefprefixtable.Cefprefixentry>`
            
            .. attribute:: cefprefixlen  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..2040
            
            	**refers to**\:  :py:class:`cefprefixlen <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefprefixtable.Cefprefixentry>`
            
            .. attribute:: cefpathid  (key)
            
            	The locally arbitrary, but unique identifier associated with this prefix path entry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefpathtype
            
            	Type for this CEF Path
            	**type**\:  :py:class:`CefPathType <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefPathType>`
            
            .. attribute:: cefpathinterface
            
            	Interface associated with this CEF path.  A value of zero for this object will indicate that no interface is associated with this path  entry
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cefpathnexthopaddr
            
            	Next hop address associated with this CEF path.  The value of this object is only relevant for attached next hop and recursive next hop   path types (when the object cefPathType is set to attachedNexthop(4) or recursiveNexthop(5)). and will be set to zero for other path types.  The type of this address is determined by the value of the cefPrefixType object
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cefpathrecursevrfname
            
            	The recursive vrf name associated with this path.  The value of this object is only relevant for recursive next hop path types (when the  object cefPathType is set to recursiveNexthop(5)), and '0x00' will be returned for other path types
            	**type**\: str
            
            	**length:** 0..31
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.Cefpathtable.Cefpathentry, self).__init__()

                self.yang_name = "cefPathEntry"
                self.yang_parent_name = "cefPathTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cefprefixtype','cefprefixaddr','cefprefixlen','cefpathid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefprefixtype', YLeaf(YType.enumeration, 'cefPrefixType')),
                    ('cefprefixaddr', YLeaf(YType.str, 'cefPrefixAddr')),
                    ('cefprefixlen', YLeaf(YType.str, 'cefPrefixLen')),
                    ('cefpathid', YLeaf(YType.int32, 'cefPathId')),
                    ('cefpathtype', YLeaf(YType.enumeration, 'cefPathType')),
                    ('cefpathinterface', YLeaf(YType.int32, 'cefPathInterface')),
                    ('cefpathnexthopaddr', YLeaf(YType.str, 'cefPathNextHopAddr')),
                    ('cefpathrecursevrfname', YLeaf(YType.str, 'cefPathRecurseVrfName')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.Cefpathtable.Cefpathentry, ['entphysicalindex', 'cefprefixtype', 'cefprefixaddr', 'cefprefixlen', 'cefpathid', 'cefpathtype', 'cefpathinterface', 'cefpathnexthopaddr', 'cefpathrecursevrfname'], name, value)


    class Cefadjsummarytable(Entity):
        """
        This table contains the summary information
        for the cefAdjTable.
        
        .. attribute:: cefadjsummaryentry
        
        	If CEF is enabled on the Managed device, each entry contains the CEF Adjacency   summary related attributes for the Managed entity. A row exists for each adjacency link type.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`Cefadjsummaryentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefadjsummarytable.Cefadjsummaryentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Cefadjsummarytable, self).__init__()

            self.yang_name = "cefAdjSummaryTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefAdjSummaryEntry", ("cefadjsummaryentry", CISCOCEFMIB.Cefadjsummarytable.Cefadjsummaryentry))])
            self._leafs = OrderedDict()

            self.cefadjsummaryentry = YList(self)
            self._segment_path = lambda: "cefAdjSummaryTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Cefadjsummarytable, [], name, value)


        class Cefadjsummaryentry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefadjsummarylinktype  (key)
            
            	The link type of the adjacency
            	**type**\:  :py:class:`CefAdjLinkType <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefAdjLinkType>`
            
            .. attribute:: cefadjsummarycomplete
            
            	The total number of complete adjacencies.  The total number of adjacencies which can be used  to switch traffic to a neighbour
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefadjsummaryincomplete
            
            	The total number of incomplete adjacencies.  The total number of adjacencies which cannot be  used to switch traffic in their current state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefadjsummaryfixup
            
            	The total number of adjacencies for which the Layer 2 encapsulation string (header) may be  updated (fixed up) at packet switch time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefadjsummaryredirect
            
            	The total number of adjacencies for which  ip redirect (or icmp redirection) is enabled. The value of this object is only relevant for ipv4 and ipv6 link type (when the index object  cefAdjSummaryLinkType value is ipv4(1) or ipv6(2)) and will be set to zero for other link types
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.Cefadjsummarytable.Cefadjsummaryentry, self).__init__()

                self.yang_name = "cefAdjSummaryEntry"
                self.yang_parent_name = "cefAdjSummaryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cefadjsummarylinktype']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefadjsummarylinktype', YLeaf(YType.enumeration, 'cefAdjSummaryLinkType')),
                    ('cefadjsummarycomplete', YLeaf(YType.uint32, 'cefAdjSummaryComplete')),
                    ('cefadjsummaryincomplete', YLeaf(YType.uint32, 'cefAdjSummaryIncomplete')),
                    ('cefadjsummaryfixup', YLeaf(YType.uint32, 'cefAdjSummaryFixup')),
                    ('cefadjsummaryredirect', YLeaf(YType.uint32, 'cefAdjSummaryRedirect')),
                ])
                self.entphysicalindex = None
                self.cefadjsummarylinktype = None
                self.cefadjsummarycomplete = None
                self.cefadjsummaryincomplete = None
                self.cefadjsummaryfixup = None
                self.cefadjsummaryredirect = None
                self._segment_path = lambda: "cefAdjSummaryEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefAdjSummaryLinkType='" + str(self.cefadjsummarylinktype) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefAdjSummaryTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.Cefadjsummarytable.Cefadjsummaryentry, ['entphysicalindex', 'cefadjsummarylinktype', 'cefadjsummarycomplete', 'cefadjsummaryincomplete', 'cefadjsummaryfixup', 'cefadjsummaryredirect'], name, value)


    class Cefadjtable(Entity):
        """
        A list of CEF adjacencies.
        
        .. attribute:: cefadjentry
        
        	If CEF is enabled on the Managed device, each entry contains the adjacency  attributes. Adjacency entries may exist for all the interfaces on which packets can be switched out of the device. The interface is instantiated by ifIndex.   Therefore, the interface index must have been assigned, according to the applicable procedures, before it can be meaningfully used. Generally, this means that the interface must exist.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`Cefadjentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefadjtable.Cefadjentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Cefadjtable, self).__init__()

            self.yang_name = "cefAdjTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefAdjEntry", ("cefadjentry", CISCOCEFMIB.Cefadjtable.Cefadjentry))])
            self._leafs = OrderedDict()

            self.cefadjentry = YList(self)
            self._segment_path = lambda: "cefAdjTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Cefadjtable, [], name, value)


        class Cefadjentry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cefadjnexthopaddrtype  (key)
            
            	Address type for the cefAdjNextHopAddr. This object specifies the address type used for cefAdjNextHopAddr.   Adjacency entries are only valid for the  address type of ipv4(1) and ipv6(2)
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cefadjnexthopaddr  (key)
            
            	The next Hop address for this adjacency. The type of this address is determined by the value of the cefAdjNextHopAddrType object
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cefadjconnid  (key)
            
            	In cases where cefLinkType, interface and the next hop address are not able to uniquely define an adjacency entry (e.g. ATM and Frame Relay Bundles), this object is a unique identifier to differentiate between these adjacency entries.   In all the other cases the value of this  index object will be 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefadjsummarylinktype  (key)
            
            	
            	**type**\:  :py:class:`CefAdjLinkType <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefAdjLinkType>`
            
            .. attribute:: cefadjsource
            
            	If the adjacency is created because some neighbour discovery mechanism has discovered a neighbour and all the information required to build a frame header to encapsulate traffic to the neighbour is available then the source of adjacency is set to the mechanism by which the adjacency is learned
            	**type**\:  :py:class:`CefAdjacencySource <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefAdjacencySource>`
            
            .. attribute:: cefadjencap
            
            	The layer 2 encapsulation string to be used for sending the packet out using this adjacency
            	**type**\: str
            
            .. attribute:: cefadjfixup
            
            	For the cases, where the encapsulation string is decided at packet switch time, the adjacency  encapsulation string specified by object cefAdjEncap  require a fixup. I.e. for the adjacencies out of IP  Tunnels, the string prepended is an IP header which has  fields which can only be setup at packet switch time.  The value of this object represent the kind of fixup applied to the packet.  If the encapsulation string doesn't require any fixup, then the value of this object will be of zero length
            	**type**\: str
            
            .. attribute:: cefadjmtu
            
            	The Layer 3 MTU which can be transmitted using  this adjacency
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: bytes
            
            .. attribute:: cefadjforwardinginfo
            
            	This object selects a forwarding info entry  defined in the cefFESelectionTable. The  selected target is defined by an entry in the cefFESelectionTable whose index value (cefFESelectionName)  is equal to this object.  The value of this object will be of zero length if this adjacency entry is the last forwarding  element in the forwarding path
            	**type**\: str
            
            .. attribute:: cefadjpkts
            
            	Number of pkts transmitted using this adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cefadjhcpkts
            
            	Number of pkts transmitted using this adjacency. This object is a 64\-bit version of cefAdjPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cefadjbytes
            
            	Number of bytes transmitted using this adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cefadjhcbytes
            
            	Number of bytes transmitted using this adjacency. This object is a 64\-bit version of cefAdjBytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.Cefadjtable.Cefadjentry, self).__init__()

                self.yang_name = "cefAdjEntry"
                self.yang_parent_name = "cefAdjTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','ifindex','cefadjnexthopaddrtype','cefadjnexthopaddr','cefadjconnid','cefadjsummarylinktype']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cefadjnexthopaddrtype', YLeaf(YType.enumeration, 'cefAdjNextHopAddrType')),
                    ('cefadjnexthopaddr', YLeaf(YType.str, 'cefAdjNextHopAddr')),
                    ('cefadjconnid', YLeaf(YType.uint32, 'cefAdjConnId')),
                    ('cefadjsummarylinktype', YLeaf(YType.enumeration, 'cefAdjSummaryLinkType')),
                    ('cefadjsource', YLeaf(YType.bits, 'cefAdjSource')),
                    ('cefadjencap', YLeaf(YType.str, 'cefAdjEncap')),
                    ('cefadjfixup', YLeaf(YType.str, 'cefAdjFixup')),
                    ('cefadjmtu', YLeaf(YType.uint32, 'cefAdjMTU')),
                    ('cefadjforwardinginfo', YLeaf(YType.str, 'cefAdjForwardingInfo')),
                    ('cefadjpkts', YLeaf(YType.uint32, 'cefAdjPkts')),
                    ('cefadjhcpkts', YLeaf(YType.uint64, 'cefAdjHCPkts')),
                    ('cefadjbytes', YLeaf(YType.uint32, 'cefAdjBytes')),
                    ('cefadjhcbytes', YLeaf(YType.uint64, 'cefAdjHCBytes')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.Cefadjtable.Cefadjentry, ['entphysicalindex', 'ifindex', 'cefadjnexthopaddrtype', 'cefadjnexthopaddr', 'cefadjconnid', 'cefadjsummarylinktype', 'cefadjsource', 'cefadjencap', 'cefadjfixup', 'cefadjmtu', 'cefadjforwardinginfo', 'cefadjpkts', 'cefadjhcpkts', 'cefadjbytes', 'cefadjhcbytes'], name, value)


    class Ceffeselectiontable(Entity):
        """
        A list of forwarding element selection entries.
        
        .. attribute:: ceffeselectionentry
        
        	If CEF is enabled on the Managed device, each entry contain a CEF forwarding element selection list.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`Ceffeselectionentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Ceffeselectiontable.Ceffeselectionentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Ceffeselectiontable, self).__init__()

            self.yang_name = "cefFESelectionTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefFESelectionEntry", ("ceffeselectionentry", CISCOCEFMIB.Ceffeselectiontable.Ceffeselectionentry))])
            self._leafs = OrderedDict()

            self.ceffeselectionentry = YList(self)
            self._segment_path = lambda: "cefFESelectionTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Ceffeselectiontable, [], name, value)


        class Ceffeselectionentry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceffeselectionname  (key)
            
            	The locally arbitrary, but unique identifier used to select a set of forwarding element lists
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: ceffeselectionid  (key)
            
            	Secondary index to identify a forwarding elements List  in this Table
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ceffeselectionspecial
            
            	Special processing for a destination is indicated through the use of special  forwarding element.   If the forwarding element list contains the  special forwarding element, then this object  represents the type of special forwarding element
            	**type**\:  :py:class:`CefForwardingElementSpecialType <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefForwardingElementSpecialType>`
            
            .. attribute:: ceffeselectionlabels
            
            	This object represent the MPLS Labels  associated with this forwarding Element List.  The value of this object will be irrelevant and will be set to zero length if the forwarding element list  doesn't contain a label forwarding element. A zero  length label list will indicate that there is no label forwarding element associated with this selection entry
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: ceffeselectionadjlinktype
            
            	This object represent the link type for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to unknown(5) if the forwarding element list  doesn't contain an adjacency forwarding element
            	**type**\:  :py:class:`CefAdjLinkType <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefAdjLinkType>`
            
            .. attribute:: ceffeselectionadjinterface
            
            	This object represent the interface for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to zero if the forwarding element list doesn't  contain an adjacency forwarding element
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ceffeselectionadjnexthopaddrtype
            
            	This object represent the next hop address type for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to unknown(0) if the forwarding element list  doesn't contain an adjacency forwarding element
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: ceffeselectionadjnexthopaddr
            
            	This object represent the next hop address for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to zero if the forwarding element list doesn't  contain an adjacency forwarding element
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: ceffeselectionadjconnid
            
            	This object represent the connection id for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to zero if the forwarding element list doesn't  contain an adjacency forwarding element.   In cases where cefFESelectionAdjLinkType, interface  and the next hop address are not able to uniquely  define an adjacency entry (e.g. ATM and Frame Relay Bundles), this object is a unique identifier to differentiate between these adjacency entries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceffeselectionvrfname
            
            	This object represent the Vrf name for the lookup associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to a string containing the single octet 0x00 if the forwarding element list  doesn't contain a lookup forwarding element
            	**type**\: str
            
            	**length:** 0..31
            
            .. attribute:: ceffeselectionweight
            
            	This object represent the weighting for  load balancing between multiple Forwarding Element Lists. The value of this object will be zero if load balancing is associated with this selection entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.Ceffeselectiontable.Ceffeselectionentry, self).__init__()

                self.yang_name = "cefFESelectionEntry"
                self.yang_parent_name = "cefFESelectionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','ceffeselectionname','ceffeselectionid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('ceffeselectionname', YLeaf(YType.str, 'cefFESelectionName')),
                    ('ceffeselectionid', YLeaf(YType.int32, 'cefFESelectionId')),
                    ('ceffeselectionspecial', YLeaf(YType.enumeration, 'cefFESelectionSpecial')),
                    ('ceffeselectionlabels', YLeaf(YType.str, 'cefFESelectionLabels')),
                    ('ceffeselectionadjlinktype', YLeaf(YType.enumeration, 'cefFESelectionAdjLinkType')),
                    ('ceffeselectionadjinterface', YLeaf(YType.int32, 'cefFESelectionAdjInterface')),
                    ('ceffeselectionadjnexthopaddrtype', YLeaf(YType.enumeration, 'cefFESelectionAdjNextHopAddrType')),
                    ('ceffeselectionadjnexthopaddr', YLeaf(YType.str, 'cefFESelectionAdjNextHopAddr')),
                    ('ceffeselectionadjconnid', YLeaf(YType.uint32, 'cefFESelectionAdjConnId')),
                    ('ceffeselectionvrfname', YLeaf(YType.str, 'cefFESelectionVrfName')),
                    ('ceffeselectionweight', YLeaf(YType.uint32, 'cefFESelectionWeight')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.Ceffeselectiontable.Ceffeselectionentry, ['entphysicalindex', 'ceffeselectionname', 'ceffeselectionid', 'ceffeselectionspecial', 'ceffeselectionlabels', 'ceffeselectionadjlinktype', 'ceffeselectionadjinterface', 'ceffeselectionadjnexthopaddrtype', 'ceffeselectionadjnexthopaddr', 'ceffeselectionadjconnid', 'ceffeselectionvrfname', 'ceffeselectionweight'], name, value)


    class Cefcfgtable(Entity):
        """
        This table contains global config parameter 
        of CEF on the Managed device.
        
        .. attribute:: cefcfgentry
        
        	If the Managed device supports CEF,  each entry contains the CEF config  parameter for the managed entity. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`Cefcfgentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefcfgtable.Cefcfgentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Cefcfgtable, self).__init__()

            self.yang_name = "cefCfgTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefCfgEntry", ("cefcfgentry", CISCOCEFMIB.Cefcfgtable.Cefcfgentry))])
            self._leafs = OrderedDict()

            self.cefcfgentry = YList(self)
            self._segment_path = lambda: "cefCfgTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Cefcfgtable, [], name, value)


        class Cefcfgentry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceffibipversion  (key)
            
            	
            	**type**\:  :py:class:`CefIpVersion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefIpVersion>`
            
            .. attribute:: cefcfgadminstate
            
            	The desired state of CEF
            	**type**\:  :py:class:`CefAdminStatus <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefAdminStatus>`
            
            .. attribute:: cefcfgoperstate
            
            	The current operational state of CEF.  If the cefCfgAdminState is disabled(2), then cefOperState will eventually go to the down(2) state unless some error has occurred.   If cefCfgAdminState is changed to enabled(1) then  cefCfgOperState should change to up(1) only if the  CEF entity is ready to forward the packets using  Cisco Express Forwarding (CEF) else it should remain  in the down(2) state. The up(1) state for this object  indicates that CEF entity is forwarding the packet using Cisco Express Forwarding
            	**type**\:  :py:class:`CefOperStatus <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefOperStatus>`
            
            .. attribute:: cefcfgdistributionadminstate
            
            	The desired state of CEF distribution
            	**type**\:  :py:class:`CefAdminStatus <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefAdminStatus>`
            
            .. attribute:: cefcfgdistributionoperstate
            
            	The current operational state of CEF distribution.  If the cefCfgDistributionAdminState is disabled(2), then cefDistributionOperState will eventually go to the down(2) state unless some error has occurred.    If cefCfgDistributionAdminState is changed to enabled(1)  then cefCfgDistributionOperState should change to up(1)  only if the CEF entity is ready to forward the packets  using Distributed Cisco Express Forwarding (dCEF) else  it should remain in the down(2) state. The up(1) state  for this object indicates that CEF entity is forwarding the packet using Distributed Cisco Express Forwarding
            	**type**\:  :py:class:`CefOperStatus <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefOperStatus>`
            
            .. attribute:: cefcfgaccountingmap
            
            	This object represents a bitmap of network accounting options.  CEF network accounting is disabled by default.  CEF network accounting can be enabled  by selecting one or more of the following CEF accounting option for the value of this object.    nonRecursive(0)\:  enables accounting through                     nonrecursive prefixes.   perPrefix(1)\:     enables the collection of the numbers                     of pkts and bytes express forwarded                    to a destination (prefix)   prefixLength(2)\:  enables accounting through                     prefixlength.           Once the accounting is enabled, the corresponding stats  can be retrieved from the cefPrefixTable and  cefStatsPrefixLenTable.  
            	**type**\:  :py:class:`Cefcfgaccountingmap <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefcfgtable.Cefcfgentry.Cefcfgaccountingmap>`
            
            .. attribute:: cefcfgloadsharingalgorithm
            
            	Indicates the CEF Load balancing algorithm.  Setting this object to none(1) will disable the Load sharing for the specified entry.  CEF load balancing can be enabled by setting  this object to one of following Algorithms\:   original(2)  \: This algorithm is based on a                  source and destination hash    tunnel(3)    \: This algorithm is used in                  tunnels environments or in                 environments where there are                 only a few source                      universal(4)  \: This algorithm uses a source and                   destination and ID hash  If the value of this object is set to 'tunnel' or 'universal', then the FIXED ID for these algorithms may be specified by the managed  object cefLoadSharingID. 
            	**type**\:  :py:class:`Cefcfgloadsharingalgorithm <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefcfgtable.Cefcfgentry.Cefcfgloadsharingalgorithm>`
            
            .. attribute:: cefcfgloadsharingid
            
            	The Fixed ID associated with the managed object cefCfgLoadSharingAlgorithm. The hash of this object value may be used by the Load Sharing Algorithm.  The value of this object is not relevant and will be set to zero if the value of managed object  cefCfgLoadSharingAlgorithm is set to none(1) or original(2). The default value of this object is calculated by the device at the time of initialization
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcfgtrafficstatsloadinterval
            
            	The interval time over which the CEF traffic statistics are collected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cefcfgtrafficstatsupdaterate
            
            	The frequency with which the line card sends the traffic load statistics to the Router Processor.  Setting the value of this object to 0 will disable the CEF traffic statistics collection
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: seconds
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.Cefcfgtable.Cefcfgentry, self).__init__()

                self.yang_name = "cefCfgEntry"
                self.yang_parent_name = "cefCfgTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','ceffibipversion']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('ceffibipversion', YLeaf(YType.enumeration, 'cefFIBIpVersion')),
                    ('cefcfgadminstate', YLeaf(YType.enumeration, 'cefCfgAdminState')),
                    ('cefcfgoperstate', YLeaf(YType.enumeration, 'cefCfgOperState')),
                    ('cefcfgdistributionadminstate', YLeaf(YType.enumeration, 'cefCfgDistributionAdminState')),
                    ('cefcfgdistributionoperstate', YLeaf(YType.enumeration, 'cefCfgDistributionOperState')),
                    ('cefcfgaccountingmap', YLeaf(YType.bits, 'cefCfgAccountingMap')),
                    ('cefcfgloadsharingalgorithm', YLeaf(YType.enumeration, 'cefCfgLoadSharingAlgorithm')),
                    ('cefcfgloadsharingid', YLeaf(YType.uint32, 'cefCfgLoadSharingID')),
                    ('cefcfgtrafficstatsloadinterval', YLeaf(YType.uint32, 'cefCfgTrafficStatsLoadInterval')),
                    ('cefcfgtrafficstatsupdaterate', YLeaf(YType.uint32, 'cefCfgTrafficStatsUpdateRate')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.Cefcfgtable.Cefcfgentry, ['entphysicalindex', 'ceffibipversion', 'cefcfgadminstate', 'cefcfgoperstate', 'cefcfgdistributionadminstate', 'cefcfgdistributionoperstate', 'cefcfgaccountingmap', 'cefcfgloadsharingalgorithm', 'cefcfgloadsharingid', 'cefcfgtrafficstatsloadinterval', 'cefcfgtrafficstatsupdaterate'], name, value)

            class Cefcfgloadsharingalgorithm(Enum):
                """
                Cefcfgloadsharingalgorithm (Enum Class)

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



    class Cefresourcetable(Entity):
        """
        This table contains global resource 
        information of CEF on the Managed device.
        
        .. attribute:: cefresourceentry
        
        	If the Managed device supports CEF, each entry contains the CEF Resource  parameters for the managed entity.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`Cefresourceentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefresourcetable.Cefresourceentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Cefresourcetable, self).__init__()

            self.yang_name = "cefResourceTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefResourceEntry", ("cefresourceentry", CISCOCEFMIB.Cefresourcetable.Cefresourceentry))])
            self._leafs = OrderedDict()

            self.cefresourceentry = YList(self)
            self._segment_path = lambda: "cefResourceTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Cefresourcetable, [], name, value)


        class Cefresourceentry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefresourcememoryused
            
            	Indicates the number of bytes from the Processor Memory Pool that are currently in use by CEF on the managed entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cefresourcefailurereason
            
            	The CEF resource failure reason which may lead to CEF being disabled on the managed entity
            	**type**\:  :py:class:`CefFailureReason <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefFailureReason>`
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.Cefresourcetable.Cefresourceentry, self).__init__()

                self.yang_name = "cefResourceEntry"
                self.yang_parent_name = "cefResourceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('cefresourcememoryused', YLeaf(YType.uint32, 'cefResourceMemoryUsed')),
                    ('cefresourcefailurereason', YLeaf(YType.enumeration, 'cefResourceFailureReason')),
                ])
                self.entphysicalindex = None
                self.cefresourcememoryused = None
                self.cefresourcefailurereason = None
                self._segment_path = lambda: "cefResourceEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefResourceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.Cefresourcetable.Cefresourceentry, ['entphysicalindex', 'cefresourcememoryused', 'cefresourcefailurereason'], name, value)


    class Cefinttable(Entity):
        """
        This Table contains interface specific
        information of CEF on the Managed
        device.
        
        .. attribute:: cefintentry
        
        	If CEF is enabled on the Managed device,  each entry contains the CEF attributes  associated with an interface. The interface is instantiated by ifIndex.   Therefore, the interface index must have been assigned, according to the applicable procedures, before it can be meaningfully used. Generally, this means that the interface must exist.  A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`Cefintentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefinttable.Cefintentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Cefinttable, self).__init__()

            self.yang_name = "cefIntTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefIntEntry", ("cefintentry", CISCOCEFMIB.Cefinttable.Cefintentry))])
            self._leafs = OrderedDict()

            self.cefintentry = YList(self)
            self._segment_path = lambda: "cefIntTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Cefinttable, [], name, value)


        class Cefintentry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceffibipversion  (key)
            
            	
            	**type**\:  :py:class:`CefIpVersion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefIpVersion>`
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: cefintswitchingstate
            
            	The CEF switching State for the interface.  If CEF is enabled but distributed CEF(dCEF) is disabled then CEF is in cefEnabled(1) state.  If distributed CEF is enabled, then CEF is in  distCefEnabled(2) state. The cefDisabled(3) state indicates that CEF is disabled.  The CEF switching state is only applicable to the received packet on the interface
            	**type**\:  :py:class:`Cefintswitchingstate <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefinttable.Cefintentry.Cefintswitchingstate>`
            
            .. attribute:: cefintloadsharing
            
            	The status of load sharing on the interface.  perPacket(1) \: Router to send data packets                over successive equal\-cost paths                without regard to individual hosts                or user sessions.  perDestination(2) \: Router to use multiple, equal\-cost                     paths to achieve load sharing  Load sharing is enabled by default  for an interface when CEF is enabled
            	**type**\:  :py:class:`Cefintloadsharing <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefinttable.Cefintentry.Cefintloadsharing>`
            
            .. attribute:: cefintnonrecursiveaccouting
            
            	The CEF accounting mode for the interface. CEF prefix based non\-recursive accounting  on an interface can be configured to store  the stats for non\-recursive prefixes in a internal  or external bucket.  internal(1)  \:  Count input traffic in the nonrecursive                 internal bucket  external(2)  \:  Count input traffic in the nonrecursive                 external bucket  The value of this object will only be effective if  value of the object cefAccountingMap is set to enable nonRecursive(1) accounting
            	**type**\:  :py:class:`Cefintnonrecursiveaccouting <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefinttable.Cefintentry.Cefintnonrecursiveaccouting>`
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.Cefinttable.Cefintentry, self).__init__()

                self.yang_name = "cefIntEntry"
                self.yang_parent_name = "cefIntTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','ceffibipversion','ifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('ceffibipversion', YLeaf(YType.enumeration, 'cefFIBIpVersion')),
                    ('ifindex', YLeaf(YType.str, 'ifIndex')),
                    ('cefintswitchingstate', YLeaf(YType.enumeration, 'cefIntSwitchingState')),
                    ('cefintloadsharing', YLeaf(YType.enumeration, 'cefIntLoadSharing')),
                    ('cefintnonrecursiveaccouting', YLeaf(YType.enumeration, 'cefIntNonrecursiveAccouting')),
                ])
                self.entphysicalindex = None
                self.ceffibipversion = None
                self.ifindex = None
                self.cefintswitchingstate = None
                self.cefintloadsharing = None
                self.cefintnonrecursiveaccouting = None
                self._segment_path = lambda: "cefIntEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cefFIBIpVersion='" + str(self.ceffibipversion) + "']" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefIntTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.Cefinttable.Cefintentry, ['entphysicalindex', 'ceffibipversion', 'ifindex', 'cefintswitchingstate', 'cefintloadsharing', 'cefintnonrecursiveaccouting'], name, value)

            class Cefintloadsharing(Enum):
                """
                Cefintloadsharing (Enum Class)

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


            class Cefintnonrecursiveaccouting(Enum):
                """
                Cefintnonrecursiveaccouting (Enum Class)

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


            class Cefintswitchingstate(Enum):
                """
                Cefintswitchingstate (Enum Class)

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



    class Cefpeertable(Entity):
        """
        Entity acting as RP (Routing Processor) keeps
        the CEF states for the line card entities and
        communicates with the line card entities using
        XDR. This Table contains the CEF information 
        related to peer entities on the managed device.
        
        .. attribute:: cefpeerentry
        
        	If CEF is enabled on the Managed device, each entry contains the CEF related attributes  associated with a CEF peer entity.  entPhysicalIndex and entPeerPhysicalIndex are also indexes for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`Cefpeerentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefpeertable.Cefpeerentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Cefpeertable, self).__init__()

            self.yang_name = "cefPeerTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefPeerEntry", ("cefpeerentry", CISCOCEFMIB.Cefpeertable.Cefpeerentry))])
            self._leafs = OrderedDict()

            self.cefpeerentry = YList(self)
            self._segment_path = lambda: "cefPeerTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Cefpeertable, [], name, value)


        class Cefpeerentry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: entpeerphysicalindex  (key)
            
            	The entity index for the CEF peer entity. Only the entities of 'module'  entPhysicalClass are included here
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefpeeroperstate
            
            	The current CEF operational state of the CEF peer entity.  Cef peer entity oper state will be peerDisabled(1) in  the following condition\:     \: Cef Peer entity encounters fatal error i.e. resource      allocation failure, ipc failure etc     \: When a reload/delete request is received from the Cef       Peer Entity  Once the peer entity is up and no fatal error is encountered, then the value of this object will transits to the peerUp(3)  state.  If the Cef Peer entity is in held stage, then the value of this object will be peerHold(3). Cef peer entity can only transit to peerDisabled(1) state from the peerHold(3) state
            	**type**\:  :py:class:`Cefpeeroperstate <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefpeertable.Cefpeerentry.Cefpeeroperstate>`
            
            .. attribute:: cefpeernumberofresets
            
            	Number of times the session with CEF peer entity  has been reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.Cefpeertable.Cefpeerentry, self).__init__()

                self.yang_name = "cefPeerEntry"
                self.yang_parent_name = "cefPeerTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','entpeerphysicalindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('entpeerphysicalindex', YLeaf(YType.int32, 'entPeerPhysicalIndex')),
                    ('cefpeeroperstate', YLeaf(YType.enumeration, 'cefPeerOperState')),
                    ('cefpeernumberofresets', YLeaf(YType.uint32, 'cefPeerNumberOfResets')),
                ])
                self.entphysicalindex = None
                self.entpeerphysicalindex = None
                self.cefpeeroperstate = None
                self.cefpeernumberofresets = None
                self._segment_path = lambda: "cefPeerEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[entPeerPhysicalIndex='" + str(self.entpeerphysicalindex) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefPeerTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.Cefpeertable.Cefpeerentry, ['entphysicalindex', 'entpeerphysicalindex', 'cefpeeroperstate', 'cefpeernumberofresets'], name, value)

            class Cefpeeroperstate(Enum):
                """
                Cefpeeroperstate (Enum Class)

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



    class Cefpeerfibtable(Entity):
        """
        Entity acting as RP (Routing Processor) keep
        the CEF FIB states for the line card entities and
        communicate with the line card entities using
        XDR. This Table contains the CEF FIB State 
        related to peer entities on the managed device.
        
        .. attribute:: cefpeerfibentry
        
        	If CEF is enabled on the Managed device, each entry contains the CEF FIB State  associated a CEF peer entity.  entPhysicalIndex and entPeerPhysicalIndex are also indexes for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`Cefpeerfibentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefpeerfibtable.Cefpeerfibentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Cefpeerfibtable, self).__init__()

            self.yang_name = "cefPeerFIBTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefPeerFIBEntry", ("cefpeerfibentry", CISCOCEFMIB.Cefpeerfibtable.Cefpeerfibentry))])
            self._leafs = OrderedDict()

            self.cefpeerfibentry = YList(self)
            self._segment_path = lambda: "cefPeerFIBTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Cefpeerfibtable, [], name, value)


        class Cefpeerfibentry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: entpeerphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entpeerphysicalindex <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefpeertable.Cefpeerentry>`
            
            .. attribute:: ceffibipversion  (key)
            
            	
            	**type**\:  :py:class:`CefIpVersion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefIpVersion>`
            
            .. attribute:: cefpeerfiboperstate
            
            	The current CEF FIB Operational State for the  CEF peer entity
            	**type**\:  :py:class:`Cefpeerfiboperstate <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefpeerfibtable.Cefpeerfibentry.Cefpeerfiboperstate>`
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.Cefpeerfibtable.Cefpeerfibentry, self).__init__()

                self.yang_name = "cefPeerFIBEntry"
                self.yang_parent_name = "cefPeerFIBTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','entpeerphysicalindex','ceffibipversion']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('entpeerphysicalindex', YLeaf(YType.str, 'entPeerPhysicalIndex')),
                    ('ceffibipversion', YLeaf(YType.enumeration, 'cefFIBIpVersion')),
                    ('cefpeerfiboperstate', YLeaf(YType.enumeration, 'cefPeerFIBOperState')),
                ])
                self.entphysicalindex = None
                self.entpeerphysicalindex = None
                self.ceffibipversion = None
                self.cefpeerfiboperstate = None
                self._segment_path = lambda: "cefPeerFIBEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[entPeerPhysicalIndex='" + str(self.entpeerphysicalindex) + "']" + "[cefFIBIpVersion='" + str(self.ceffibipversion) + "']"
                self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/cefPeerFIBTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.Cefpeerfibtable.Cefpeerfibentry, ['entphysicalindex', 'entpeerphysicalindex', 'ceffibipversion', 'cefpeerfiboperstate'], name, value)

            class Cefpeerfiboperstate(Enum):
                """
                Cefpeerfiboperstate (Enum Class)

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



    class Cefccglobaltable(Entity):
        """
        This table contains CEF consistency checker
        (CC) global parameters for the managed device.
        
        .. attribute:: cefccglobalentry
        
        	If the managed device supports CEF, each entry contains the global consistency  checker parameter for the managed device. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device
        	**type**\: list of  		 :py:class:`Cefccglobalentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefccglobaltable.Cefccglobalentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Cefccglobaltable, self).__init__()

            self.yang_name = "cefCCGlobalTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefCCGlobalEntry", ("cefccglobalentry", CISCOCEFMIB.Cefccglobaltable.Cefccglobalentry))])
            self._leafs = OrderedDict()

            self.cefccglobalentry = YList(self)
            self._segment_path = lambda: "cefCCGlobalTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Cefccglobaltable, [], name, value)


        class Cefccglobalentry(Entity):
            """
            If the managed device supports CEF,
            each entry contains the global consistency 
            checker parameter for the managed device.
            A row may exist for each IP version type
            (v4 and v6) depending upon the IP version
            supported on the device.
            
            .. attribute:: ceffibipversion  (key)
            
            	
            	**type**\:  :py:class:`CefIpVersion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefIpVersion>`
            
            .. attribute:: cefccglobalautorepairenabled
            
            	Once an inconsistency has been detected,  CEF has the ability to repair the problem.  This object indicates the status of auto\-repair  function for the consistency checkers
            	**type**\: bool
            
            .. attribute:: cefccglobalautorepairdelay
            
            	Indiactes how long the consistency checker  waits to fix an inconsistency.  The value of this object has no effect when the value of object cefCCGlobalAutoRepairEnabled is 'false'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cefccglobalautorepairholddown
            
            	Indicates how long the consistency checker waits to re\-enable auto\-repair after  auto\-repair runs.  The value of this object has no effect when the value of object cefCCGlobalAutoRepairEnabled is 'false'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cefccglobalerrormsgenabled
            
            	Enables the consistency checker to generate  an error message when it detects an inconsistency
            	**type**\: bool
            
            .. attribute:: cefccglobalfullscanaction
            
            	Setting the value of this object to ccActionStart(1) will start the full scan consistency checkers.  The Management station should poll the  cefCCGlobalFullScanStatus object to get the  state of full\-scan operation.  Once the full\-scan operation completes (value of cefCCGlobalFullScanStatus object is ccStatusDone(3)),  the Management station should retrieve the values of the related stats object from the cefCCTypeTable.  Setting the value of this object to ccActionAbort(2) will  abort the full\-scan operation.  The value of this object can't be set to ccActionStart(1),  if the value of object cefCCGlobalFullScanStatus is ccStatusRunning(2).  The value of this object will be set to cefActionNone(1) when the full scan consistency checkers have never been activated.  A Management Station cannot set the value of this object to cefActionNone(1)
            	**type**\:  :py:class:`CefCCAction <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefCCAction>`
            
            .. attribute:: cefccglobalfullscanstatus
            
            	Indicates the status of the full scan consistency checker request
            	**type**\:  :py:class:`CefCCStatus <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefCCStatus>`
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.Cefccglobaltable.Cefccglobalentry, self).__init__()

                self.yang_name = "cefCCGlobalEntry"
                self.yang_parent_name = "cefCCGlobalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ceffibipversion']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ceffibipversion', YLeaf(YType.enumeration, 'cefFIBIpVersion')),
                    ('cefccglobalautorepairenabled', YLeaf(YType.boolean, 'cefCCGlobalAutoRepairEnabled')),
                    ('cefccglobalautorepairdelay', YLeaf(YType.uint32, 'cefCCGlobalAutoRepairDelay')),
                    ('cefccglobalautorepairholddown', YLeaf(YType.uint32, 'cefCCGlobalAutoRepairHoldDown')),
                    ('cefccglobalerrormsgenabled', YLeaf(YType.boolean, 'cefCCGlobalErrorMsgEnabled')),
                    ('cefccglobalfullscanaction', YLeaf(YType.enumeration, 'cefCCGlobalFullScanAction')),
                    ('cefccglobalfullscanstatus', YLeaf(YType.enumeration, 'cefCCGlobalFullScanStatus')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.Cefccglobaltable.Cefccglobalentry, ['ceffibipversion', 'cefccglobalautorepairenabled', 'cefccglobalautorepairdelay', 'cefccglobalautorepairholddown', 'cefccglobalerrormsgenabled', 'cefccglobalfullscanaction', 'cefccglobalfullscanstatus'], name, value)


    class Cefcctypetable(Entity):
        """
        This table contains CEF consistency
        checker types specific parameters on the managed device.
        
        All detected inconsistency are signaled to the
        Management Station via cefInconsistencyDetection
        notification.
        
        .. attribute:: cefcctypeentry
        
        	If the managed device supports CEF, each entry contains the consistency  checker statistics for a consistency  checker type. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device
        	**type**\: list of  		 :py:class:`Cefcctypeentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefcctypetable.Cefcctypeentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Cefcctypetable, self).__init__()

            self.yang_name = "cefCCTypeTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefCCTypeEntry", ("cefcctypeentry", CISCOCEFMIB.Cefcctypetable.Cefcctypeentry))])
            self._leafs = OrderedDict()

            self.cefcctypeentry = YList(self)
            self._segment_path = lambda: "cefCCTypeTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Cefcctypetable, [], name, value)


        class Cefcctypeentry(Entity):
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
            
            .. attribute:: cefcctype  (key)
            
            	Type of the consistency checker
            	**type**\:  :py:class:`CefCCType <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefCCType>`
            
            .. attribute:: cefccenabled
            
            	Enables the passive consistency checker. Passive consistency checkers are disabled by default.  Full\-scan consistency checkers are always enabled. An attempt to set this object to 'false' for an active consistency checker will result in 'wrongValue' error
            	**type**\: bool
            
            .. attribute:: cefcccount
            
            	The maximum number of prefixes to check per scan.  The default value for this object  depends upon the consistency checker type.  The value of this object will be irrelevant  for some of the consistency checkers and will be set to 0.  A Management Station cannot set the value of this object to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefccperiod
            
            	The period between scans for the consistency checker
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cefccqueriessent
            
            	Number of prefix consistency queries sent to CEF forwarding databases by this consistency checker
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefccqueriesignored
            
            	Number of prefix consistency queries for which the consistency checks were not performed by this  consistency checker. This may be because of some internal error or resource failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefccquerieschecked
            
            	Number of prefix consistency queries processed by this  consistency checker
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefccqueriesiterated
            
            	Number of prefix consistency queries iterated back to the master database by this consistency checker
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.Cefcctypetable.Cefcctypeentry, self).__init__()

                self.yang_name = "cefCCTypeEntry"
                self.yang_parent_name = "cefCCTypeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ceffibipversion','cefcctype']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ceffibipversion', YLeaf(YType.enumeration, 'cefFIBIpVersion')),
                    ('cefcctype', YLeaf(YType.enumeration, 'cefCCType')),
                    ('cefccenabled', YLeaf(YType.boolean, 'cefCCEnabled')),
                    ('cefcccount', YLeaf(YType.uint32, 'cefCCCount')),
                    ('cefccperiod', YLeaf(YType.uint32, 'cefCCPeriod')),
                    ('cefccqueriessent', YLeaf(YType.uint32, 'cefCCQueriesSent')),
                    ('cefccqueriesignored', YLeaf(YType.uint32, 'cefCCQueriesIgnored')),
                    ('cefccquerieschecked', YLeaf(YType.uint32, 'cefCCQueriesChecked')),
                    ('cefccqueriesiterated', YLeaf(YType.uint32, 'cefCCQueriesIterated')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.Cefcctypetable.Cefcctypeentry, ['ceffibipversion', 'cefcctype', 'cefccenabled', 'cefcccount', 'cefccperiod', 'cefccqueriessent', 'cefccqueriesignored', 'cefccquerieschecked', 'cefccqueriesiterated'], name, value)


    class Cefinconsistencyrecordtable(Entity):
        """
        This table contains CEF inconsistency
        records.
        
        .. attribute:: cefinconsistencyrecordentry
        
        	If the managed device supports CEF, each entry contains the inconsistency  record
        	**type**\: list of  		 :py:class:`Cefinconsistencyrecordentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefinconsistencyrecordtable.Cefinconsistencyrecordentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Cefinconsistencyrecordtable, self).__init__()

            self.yang_name = "cefInconsistencyRecordTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefInconsistencyRecordEntry", ("cefinconsistencyrecordentry", CISCOCEFMIB.Cefinconsistencyrecordtable.Cefinconsistencyrecordentry))])
            self._leafs = OrderedDict()

            self.cefinconsistencyrecordentry = YList(self)
            self._segment_path = lambda: "cefInconsistencyRecordTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Cefinconsistencyrecordtable, [], name, value)


        class Cefinconsistencyrecordentry(Entity):
            """
            If the managed device supports CEF,
            each entry contains the inconsistency 
            record.
            
            .. attribute:: ceffibipversion  (key)
            
            	
            	**type**\:  :py:class:`CefIpVersion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefIpVersion>`
            
            .. attribute:: cefinconsistencyrecid  (key)
            
            	The locally arbitrary, but unique identifier associated with this inconsistency record entry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefinconsistencyprefixtype
            
            	The network prefix type associated with this inconsistency record
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: cefinconsistencyprefixaddr
            
            	The network prefix address associated with this  inconsistency record.  The type of this address is determined by the value of the cefInconsistencyPrefixType object
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: cefinconsistencyprefixlen
            
            	Length in bits of the inconsistency address prefix
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: cefinconsistencyvrfname
            
            	Vrf name associated with this inconsistency record
            	**type**\: str
            
            	**length:** 0..31
            
            .. attribute:: cefinconsistencycctype
            
            	The type of consistency checker who generated this inconsistency record
            	**type**\:  :py:class:`CefCCType <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefCCType>`
            
            .. attribute:: cefinconsistencyentity
            
            	The entity for which this inconsistency record was  generated. The value of this object will be  irrelevant and will be set to 0 when the inconsisency  record is applicable for all the entities
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cefinconsistencyreason
            
            	The reason for generating this inconsistency record.   missing(1)\:        the prefix is missing  checksumErr(2)\:    checksum error was found  unknown(3)\:        reason is unknown
            	**type**\:  :py:class:`Cefinconsistencyreason <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefinconsistencyrecordtable.Cefinconsistencyrecordentry.Cefinconsistencyreason>`
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.Cefinconsistencyrecordtable.Cefinconsistencyrecordentry, self).__init__()

                self.yang_name = "cefInconsistencyRecordEntry"
                self.yang_parent_name = "cefInconsistencyRecordTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ceffibipversion','cefinconsistencyrecid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ceffibipversion', YLeaf(YType.enumeration, 'cefFIBIpVersion')),
                    ('cefinconsistencyrecid', YLeaf(YType.int32, 'cefInconsistencyRecId')),
                    ('cefinconsistencyprefixtype', YLeaf(YType.enumeration, 'cefInconsistencyPrefixType')),
                    ('cefinconsistencyprefixaddr', YLeaf(YType.str, 'cefInconsistencyPrefixAddr')),
                    ('cefinconsistencyprefixlen', YLeaf(YType.uint32, 'cefInconsistencyPrefixLen')),
                    ('cefinconsistencyvrfname', YLeaf(YType.str, 'cefInconsistencyVrfName')),
                    ('cefinconsistencycctype', YLeaf(YType.enumeration, 'cefInconsistencyCCType')),
                    ('cefinconsistencyentity', YLeaf(YType.int32, 'cefInconsistencyEntity')),
                    ('cefinconsistencyreason', YLeaf(YType.enumeration, 'cefInconsistencyReason')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.Cefinconsistencyrecordtable.Cefinconsistencyrecordentry, ['ceffibipversion', 'cefinconsistencyrecid', 'cefinconsistencyprefixtype', 'cefinconsistencyprefixaddr', 'cefinconsistencyprefixlen', 'cefinconsistencyvrfname', 'cefinconsistencycctype', 'cefinconsistencyentity', 'cefinconsistencyreason'], name, value)

            class Cefinconsistencyreason(Enum):
                """
                Cefinconsistencyreason (Enum Class)

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



    class Cefstatsprefixlentable(Entity):
        """
        This table specifies the CEF stats based
        on the Prefix Length.
        
        .. attribute:: cefstatsprefixlenentry
        
        	If CEF is enabled on the Managed device and if CEF accounting is set to enable  prefix length based accounting (value of  cefCfgAccountingMap object in the  cefCfgEntry is set to enable 'prefixLength'  accounting), each entry contains the traffic  statistics for a prefix length. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`Cefstatsprefixlenentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefstatsprefixlentable.Cefstatsprefixlenentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Cefstatsprefixlentable, self).__init__()

            self.yang_name = "cefStatsPrefixLenTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefStatsPrefixLenEntry", ("cefstatsprefixlenentry", CISCOCEFMIB.Cefstatsprefixlentable.Cefstatsprefixlenentry))])
            self._leafs = OrderedDict()

            self.cefstatsprefixlenentry = YList(self)
            self._segment_path = lambda: "cefStatsPrefixLenTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Cefstatsprefixlentable, [], name, value)


        class Cefstatsprefixlenentry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceffibipversion  (key)
            
            	
            	**type**\:  :py:class:`CefIpVersion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefIpVersion>`
            
            .. attribute:: cefstatsprefixlen  (key)
            
            	Length in bits of the Destination IP prefix. As 0.0.0.0/0 is a valid prefix, hence  0 is a valid prefix length
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: cefstatsprefixqueries
            
            	Number of queries received in the FIB database  for the specified IP prefix length
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefstatsprefixhcqueries
            
            	Number of queries received in the FIB database for the specified IP prefix length. This object is a 64\-bit version of  cefStatsPrefixQueries
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefstatsprefixinserts
            
            	Number of insert operations performed to the FIB  database for the specified IP prefix length
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefstatsprefixhcinserts
            
            	Number of insert operations performed to the FIB  database for the specified IP prefix length. This object is a 64\-bit version of  cefStatsPrefixInsert
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefstatsprefixdeletes
            
            	Number of delete operations performed to the FIB  database for the specified IP prefix length
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefstatsprefixhcdeletes
            
            	Number of delete operations performed to the FIB  database for the specified IP prefix length. This object is a 64\-bit version of  cefStatsPrefixDelete
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefstatsprefixelements
            
            	Total number of elements in the FIB database for the specified IP prefix length
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefstatsprefixhcelements
            
            	Total number of elements in the FIB database for the specified IP prefix length. This object is a 64\-bit version of  cefStatsPrefixElements
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.Cefstatsprefixlentable.Cefstatsprefixlenentry, self).__init__()

                self.yang_name = "cefStatsPrefixLenEntry"
                self.yang_parent_name = "cefStatsPrefixLenTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','ceffibipversion','cefstatsprefixlen']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('ceffibipversion', YLeaf(YType.enumeration, 'cefFIBIpVersion')),
                    ('cefstatsprefixlen', YLeaf(YType.uint32, 'cefStatsPrefixLen')),
                    ('cefstatsprefixqueries', YLeaf(YType.uint32, 'cefStatsPrefixQueries')),
                    ('cefstatsprefixhcqueries', YLeaf(YType.uint64, 'cefStatsPrefixHCQueries')),
                    ('cefstatsprefixinserts', YLeaf(YType.uint32, 'cefStatsPrefixInserts')),
                    ('cefstatsprefixhcinserts', YLeaf(YType.uint64, 'cefStatsPrefixHCInserts')),
                    ('cefstatsprefixdeletes', YLeaf(YType.uint32, 'cefStatsPrefixDeletes')),
                    ('cefstatsprefixhcdeletes', YLeaf(YType.uint64, 'cefStatsPrefixHCDeletes')),
                    ('cefstatsprefixelements', YLeaf(YType.uint32, 'cefStatsPrefixElements')),
                    ('cefstatsprefixhcelements', YLeaf(YType.uint64, 'cefStatsPrefixHCElements')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.Cefstatsprefixlentable.Cefstatsprefixlenentry, ['entphysicalindex', 'ceffibipversion', 'cefstatsprefixlen', 'cefstatsprefixqueries', 'cefstatsprefixhcqueries', 'cefstatsprefixinserts', 'cefstatsprefixhcinserts', 'cefstatsprefixdeletes', 'cefstatsprefixhcdeletes', 'cefstatsprefixelements', 'cefstatsprefixhcelements'], name, value)


    class Cefswitchingstatstable(Entity):
        """
        This table specifies the CEF switch stats.
        
        .. attribute:: cefswitchingstatsentry
        
        	If CEF is enabled on the Managed device, each entry specifies the switching stats. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of  		 :py:class:`Cefswitchingstatsentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CISCOCEFMIB.Cefswitchingstatstable.Cefswitchingstatsentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CISCOCEFMIB.Cefswitchingstatstable, self).__init__()

            self.yang_name = "cefSwitchingStatsTable"
            self.yang_parent_name = "CISCO-CEF-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("cefSwitchingStatsEntry", ("cefswitchingstatsentry", CISCOCEFMIB.Cefswitchingstatstable.Cefswitchingstatsentry))])
            self._leafs = OrderedDict()

            self.cefswitchingstatsentry = YList(self)
            self._segment_path = lambda: "cefSwitchingStatsTable"
            self._absolute_path = lambda: "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOCEFMIB.Cefswitchingstatstable, [], name, value)


        class Cefswitchingstatsentry(Entity):
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
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceffibipversion  (key)
            
            	
            	**type**\:  :py:class:`CefIpVersion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.CefIpVersion>`
            
            .. attribute:: cefswitchingindex  (key)
            
            	The locally arbitrary, but unique identifier associated with this switching stats entry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefswitchingpath
            
            	Switch path where the feature was executed. Available switch paths are platform\-dependent. Following are the examples of switching paths\:     RIB \: switching with CEF assistance     Low\-end switching (LES) \: CEF switch path     PAS \: CEF turbo switch path
            	**type**\: str
            
            	**length:** 1..32
            
            .. attribute:: cefswitchingdrop
            
            	Number of packets dropped by CEF
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cefswitchinghcdrop
            
            	Number of packets dropped by CEF. This object is a 64\-bit version of cefSwitchingDrop
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cefswitchingpunt
            
            	Number of packets that could not be switched in the normal path and were punted to the next\-fastest switching vector
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cefswitchinghcpunt
            
            	Number of packets that could not be switched in the normal path and were punted to the next\-fastest switching vector. This object is a 64\-bit version of cefSwitchingPunt
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cefswitchingpunt2host
            
            	Number of packets that could not be switched in the normal path and were punted to the host (process switching path).  For most of the switching paths, the value of this object may be similar to cefSwitchingPunt
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cefswitchinghcpunt2host
            
            	Number of packets that could not be switched in the normal path and were punted to the host (process switching path).  For most of the switching paths, the value of this object may be similar to cefSwitchingPunt. This object is a 64\-bit version of cefSwitchingPunt2Host
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CISCOCEFMIB.Cefswitchingstatstable.Cefswitchingstatsentry, self).__init__()

                self.yang_name = "cefSwitchingStatsEntry"
                self.yang_parent_name = "cefSwitchingStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','ceffibipversion','cefswitchingindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', YLeaf(YType.str, 'entPhysicalIndex')),
                    ('ceffibipversion', YLeaf(YType.enumeration, 'cefFIBIpVersion')),
                    ('cefswitchingindex', YLeaf(YType.int32, 'cefSwitchingIndex')),
                    ('cefswitchingpath', YLeaf(YType.str, 'cefSwitchingPath')),
                    ('cefswitchingdrop', YLeaf(YType.uint32, 'cefSwitchingDrop')),
                    ('cefswitchinghcdrop', YLeaf(YType.uint64, 'cefSwitchingHCDrop')),
                    ('cefswitchingpunt', YLeaf(YType.uint32, 'cefSwitchingPunt')),
                    ('cefswitchinghcpunt', YLeaf(YType.uint64, 'cefSwitchingHCPunt')),
                    ('cefswitchingpunt2host', YLeaf(YType.uint32, 'cefSwitchingPunt2Host')),
                    ('cefswitchinghcpunt2host', YLeaf(YType.uint64, 'cefSwitchingHCPunt2Host')),
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

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOCEFMIB.Cefswitchingstatstable.Cefswitchingstatsentry, ['entphysicalindex', 'ceffibipversion', 'cefswitchingindex', 'cefswitchingpath', 'cefswitchingdrop', 'cefswitchinghcdrop', 'cefswitchingpunt', 'cefswitchinghcpunt', 'cefswitchingpunt2host', 'cefswitchinghcpunt2host'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOCEFMIB()
        return self._top_entity

