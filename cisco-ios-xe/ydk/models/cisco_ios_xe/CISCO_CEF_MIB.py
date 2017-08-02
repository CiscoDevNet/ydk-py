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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoCefMib(Entity):
    """
    
    
    .. attribute:: cefadjsummarytable
    
    	This table contains the summary information for the cefAdjTable
    	**type**\:   :py:class:`Cefadjsummarytable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefadjsummarytable>`
    
    .. attribute:: cefadjtable
    
    	A list of CEF adjacencies
    	**type**\:   :py:class:`Cefadjtable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefadjtable>`
    
    .. attribute:: cefcc
    
    	
    	**type**\:   :py:class:`Cefcc <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefcc>`
    
    .. attribute:: cefccglobaltable
    
    	This table contains CEF consistency checker (CC) global parameters for the managed device
    	**type**\:   :py:class:`Cefccglobaltable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefccglobaltable>`
    
    .. attribute:: cefcctypetable
    
    	This table contains CEF consistency checker types specific parameters on the managed device.  All detected inconsistency are signaled to the Management Station via cefInconsistencyDetection notification
    	**type**\:   :py:class:`Cefcctypetable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefcctypetable>`
    
    .. attribute:: cefcfgtable
    
    	This table contains global config parameter  of CEF on the Managed device
    	**type**\:   :py:class:`Cefcfgtable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefcfgtable>`
    
    .. attribute:: ceffeselectiontable
    
    	A list of forwarding element selection entries
    	**type**\:   :py:class:`Ceffeselectiontable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Ceffeselectiontable>`
    
    .. attribute:: ceffib
    
    	
    	**type**\:   :py:class:`Ceffib <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Ceffib>`
    
    .. attribute:: ceffibsummarytable
    
    	This table contains the summary information for the cefPrefixTable
    	**type**\:   :py:class:`Ceffibsummarytable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Ceffibsummarytable>`
    
    .. attribute:: cefinconsistencyrecordtable
    
    	This table contains CEF inconsistency records
    	**type**\:   :py:class:`Cefinconsistencyrecordtable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefinconsistencyrecordtable>`
    
    .. attribute:: cefinttable
    
    	This Table contains interface specific information of CEF on the Managed device
    	**type**\:   :py:class:`Cefinttable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefinttable>`
    
    .. attribute:: ceflmprefixtable
    
    	A table of Longest Match Prefix Query requests.  Generator application should utilize the cefLMPrefixSpinLock to try to avoid collisions. See DESCRIPTION clause of cefLMPrefixSpinLock
    	**type**\:   :py:class:`Ceflmprefixtable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Ceflmprefixtable>`
    
    .. attribute:: cefnotifcntl
    
    	
    	**type**\:   :py:class:`Cefnotifcntl <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefnotifcntl>`
    
    .. attribute:: cefpathtable
    
    	CEF prefix path is a valid route to reach to a  destination IP prefix. Multiple paths may exist  out of a router to the same destination prefix.  This table specify lists of CEF paths
    	**type**\:   :py:class:`Cefpathtable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefpathtable>`
    
    .. attribute:: cefpeerfibtable
    
    	Entity acting as RP (Routing Processor) keep the CEF FIB states for the line card entities and communicate with the line card entities using XDR. This Table contains the CEF FIB State  related to peer entities on the managed device
    	**type**\:   :py:class:`Cefpeerfibtable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefpeerfibtable>`
    
    .. attribute:: cefpeertable
    
    	Entity acting as RP (Routing Processor) keeps the CEF states for the line card entities and communicates with the line card entities using XDR. This Table contains the CEF information  related to peer entities on the managed device
    	**type**\:   :py:class:`Cefpeertable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefpeertable>`
    
    .. attribute:: cefprefixtable
    
    	A list of CEF forwarding prefixes
    	**type**\:   :py:class:`Cefprefixtable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefprefixtable>`
    
    .. attribute:: cefresourcetable
    
    	This table contains global resource  information of CEF on the Managed device
    	**type**\:   :py:class:`Cefresourcetable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefresourcetable>`
    
    .. attribute:: cefstatsprefixlentable
    
    	This table specifies the CEF stats based on the Prefix Length
    	**type**\:   :py:class:`Cefstatsprefixlentable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefstatsprefixlentable>`
    
    .. attribute:: cefswitchingstatstable
    
    	This table specifies the CEF switch stats
    	**type**\:   :py:class:`Cefswitchingstatstable <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefswitchingstatstable>`
    
    

    """

    _prefix = 'CISCO-CEF-MIB'
    _revision = '2006-01-30'

    def __init__(self):
        super(CiscoCefMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-CEF-MIB"
        self.yang_parent_name = "CISCO-CEF-MIB"

        self.cefadjsummarytable = CiscoCefMib.Cefadjsummarytable()
        self.cefadjsummarytable.parent = self
        self._children_name_map["cefadjsummarytable"] = "cefAdjSummaryTable"
        self._children_yang_names.add("cefAdjSummaryTable")

        self.cefadjtable = CiscoCefMib.Cefadjtable()
        self.cefadjtable.parent = self
        self._children_name_map["cefadjtable"] = "cefAdjTable"
        self._children_yang_names.add("cefAdjTable")

        self.cefcc = CiscoCefMib.Cefcc()
        self.cefcc.parent = self
        self._children_name_map["cefcc"] = "cefCC"
        self._children_yang_names.add("cefCC")

        self.cefccglobaltable = CiscoCefMib.Cefccglobaltable()
        self.cefccglobaltable.parent = self
        self._children_name_map["cefccglobaltable"] = "cefCCGlobalTable"
        self._children_yang_names.add("cefCCGlobalTable")

        self.cefcctypetable = CiscoCefMib.Cefcctypetable()
        self.cefcctypetable.parent = self
        self._children_name_map["cefcctypetable"] = "cefCCTypeTable"
        self._children_yang_names.add("cefCCTypeTable")

        self.cefcfgtable = CiscoCefMib.Cefcfgtable()
        self.cefcfgtable.parent = self
        self._children_name_map["cefcfgtable"] = "cefCfgTable"
        self._children_yang_names.add("cefCfgTable")

        self.ceffeselectiontable = CiscoCefMib.Ceffeselectiontable()
        self.ceffeselectiontable.parent = self
        self._children_name_map["ceffeselectiontable"] = "cefFESelectionTable"
        self._children_yang_names.add("cefFESelectionTable")

        self.ceffib = CiscoCefMib.Ceffib()
        self.ceffib.parent = self
        self._children_name_map["ceffib"] = "cefFIB"
        self._children_yang_names.add("cefFIB")

        self.ceffibsummarytable = CiscoCefMib.Ceffibsummarytable()
        self.ceffibsummarytable.parent = self
        self._children_name_map["ceffibsummarytable"] = "cefFIBSummaryTable"
        self._children_yang_names.add("cefFIBSummaryTable")

        self.cefinconsistencyrecordtable = CiscoCefMib.Cefinconsistencyrecordtable()
        self.cefinconsistencyrecordtable.parent = self
        self._children_name_map["cefinconsistencyrecordtable"] = "cefInconsistencyRecordTable"
        self._children_yang_names.add("cefInconsistencyRecordTable")

        self.cefinttable = CiscoCefMib.Cefinttable()
        self.cefinttable.parent = self
        self._children_name_map["cefinttable"] = "cefIntTable"
        self._children_yang_names.add("cefIntTable")

        self.ceflmprefixtable = CiscoCefMib.Ceflmprefixtable()
        self.ceflmprefixtable.parent = self
        self._children_name_map["ceflmprefixtable"] = "cefLMPrefixTable"
        self._children_yang_names.add("cefLMPrefixTable")

        self.cefnotifcntl = CiscoCefMib.Cefnotifcntl()
        self.cefnotifcntl.parent = self
        self._children_name_map["cefnotifcntl"] = "cefNotifCntl"
        self._children_yang_names.add("cefNotifCntl")

        self.cefpathtable = CiscoCefMib.Cefpathtable()
        self.cefpathtable.parent = self
        self._children_name_map["cefpathtable"] = "cefPathTable"
        self._children_yang_names.add("cefPathTable")

        self.cefpeerfibtable = CiscoCefMib.Cefpeerfibtable()
        self.cefpeerfibtable.parent = self
        self._children_name_map["cefpeerfibtable"] = "cefPeerFIBTable"
        self._children_yang_names.add("cefPeerFIBTable")

        self.cefpeertable = CiscoCefMib.Cefpeertable()
        self.cefpeertable.parent = self
        self._children_name_map["cefpeertable"] = "cefPeerTable"
        self._children_yang_names.add("cefPeerTable")

        self.cefprefixtable = CiscoCefMib.Cefprefixtable()
        self.cefprefixtable.parent = self
        self._children_name_map["cefprefixtable"] = "cefPrefixTable"
        self._children_yang_names.add("cefPrefixTable")

        self.cefresourcetable = CiscoCefMib.Cefresourcetable()
        self.cefresourcetable.parent = self
        self._children_name_map["cefresourcetable"] = "cefResourceTable"
        self._children_yang_names.add("cefResourceTable")

        self.cefstatsprefixlentable = CiscoCefMib.Cefstatsprefixlentable()
        self.cefstatsprefixlentable.parent = self
        self._children_name_map["cefstatsprefixlentable"] = "cefStatsPrefixLenTable"
        self._children_yang_names.add("cefStatsPrefixLenTable")

        self.cefswitchingstatstable = CiscoCefMib.Cefswitchingstatstable()
        self.cefswitchingstatstable.parent = self
        self._children_name_map["cefswitchingstatstable"] = "cefSwitchingStatsTable"
        self._children_yang_names.add("cefSwitchingStatsTable")


    class Ceffib(Entity):
        """
        
        
        .. attribute:: ceflmprefixspinlock
        
        	An advisory lock used to allow cooperating SNMP Command Generator applications to coordinate their use of the Set operation in creating Longest Match Prefix Entries in cefLMPrefixTable.  When creating a new longest prefix match entry, the value of cefLMPrefixSpinLock should be retrieved.   The destination address should be determined to be unique by the SNMP Command Generator application by consulting the cefLMPrefixTable. Finally, the longest  prefix entry may be created (Set), including the advisory lock.         If another SNMP Command Generator application has altered the longest prefix entry in the meantime,  then the spin lock's value will have changed,  and so this creation will fail because it will specify the wrong value for the spin lock.  Since this is an advisory lock, the use of this lock is not enforced, but not using this lock may lead to conflict with the another SNMP command responder  application which may also be acting on the cefLMPrefixTable
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Ceffib, self).__init__()

            self.yang_name = "cefFIB"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.ceflmprefixspinlock = YLeaf(YType.int32, "cefLMPrefixSpinLock")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ceflmprefixspinlock") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Ceffib, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Ceffib, self).__setattr__(name, value)

        def has_data(self):
            return self.ceflmprefixspinlock.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ceflmprefixspinlock.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefFIB" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ceflmprefixspinlock.is_set or self.ceflmprefixspinlock.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ceflmprefixspinlock.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefLMPrefixSpinLock"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cefLMPrefixSpinLock"):
                self.ceflmprefixspinlock = value
                self.ceflmprefixspinlock.value_namespace = name_space
                self.ceflmprefixspinlock.value_namespace_prefix = name_space_prefix


    class Cefcc(Entity):
        """
        
        
        .. attribute:: cefinconsistencyreset
        
        	Setting the value of this object to ccActionStart(1) will reset all the active consistency checkers.  The Management station should poll the  cefInconsistencyResetStatus object to get the  state of inconsistency reset operation.  This operation once started, cannot be aborted. Hence, the value of this object cannot be set to ccActionAbort(2).  The value of this object can't be set to ccActionStart(1),  if the value of object cefInconsistencyResetStatus is ccStatusRunning(2)
        	**type**\:   :py:class:`Cefccaction <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefccaction>`
        
        .. attribute:: cefinconsistencyresetstatus
        
        	Indicates the status of the consistency reset request
        	**type**\:   :py:class:`Cefccstatus <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefccstatus>`
        
        .. attribute:: entlastinconsistencydetecttime
        
        	The value of sysUpTime at the time an inconsistency is detecetd
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Cefcc, self).__init__()

            self.yang_name = "cefCC"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.cefinconsistencyreset = YLeaf(YType.enumeration, "cefInconsistencyReset")

            self.cefinconsistencyresetstatus = YLeaf(YType.enumeration, "cefInconsistencyResetStatus")

            self.entlastinconsistencydetecttime = YLeaf(YType.uint32, "entLastInconsistencyDetectTime")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cefinconsistencyreset",
                            "cefinconsistencyresetstatus",
                            "entlastinconsistencydetecttime") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Cefcc, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Cefcc, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cefinconsistencyreset.is_set or
                self.cefinconsistencyresetstatus.is_set or
                self.entlastinconsistencydetecttime.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cefinconsistencyreset.yfilter != YFilter.not_set or
                self.cefinconsistencyresetstatus.yfilter != YFilter.not_set or
                self.entlastinconsistencydetecttime.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefCC" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cefinconsistencyreset.is_set or self.cefinconsistencyreset.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cefinconsistencyreset.get_name_leafdata())
            if (self.cefinconsistencyresetstatus.is_set or self.cefinconsistencyresetstatus.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cefinconsistencyresetstatus.get_name_leafdata())
            if (self.entlastinconsistencydetecttime.is_set or self.entlastinconsistencydetecttime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.entlastinconsistencydetecttime.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefInconsistencyReset" or name == "cefInconsistencyResetStatus" or name == "entLastInconsistencyDetectTime"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cefInconsistencyReset"):
                self.cefinconsistencyreset = value
                self.cefinconsistencyreset.value_namespace = name_space
                self.cefinconsistencyreset.value_namespace_prefix = name_space_prefix
            if(value_path == "cefInconsistencyResetStatus"):
                self.cefinconsistencyresetstatus = value
                self.cefinconsistencyresetstatus.value_namespace = name_space
                self.cefinconsistencyresetstatus.value_namespace_prefix = name_space_prefix
            if(value_path == "entLastInconsistencyDetectTime"):
                self.entlastinconsistencydetecttime = value
                self.entlastinconsistencydetecttime.value_namespace = name_space
                self.entlastinconsistencydetecttime.value_namespace_prefix = name_space_prefix


    class Cefnotifcntl(Entity):
        """
        
        
        .. attribute:: cefinconsistencynotifenable
        
        	Indicates whether cefInconsistencyDetection notification should be generated for this managed device
        	**type**\:  bool
        
        .. attribute:: cefnotifthrottlinginterval
        
        	This object controls the generation of the cefInconsistencyDetection notification.  If this object has a value of zero, then the throttle control is disabled.  If this object has a non\-zero value, then the agent must not generate more than one  cefInconsistencyDetection 'notification\-event' in the  indicated period, where a 'notification\-event' is the transmission of a single trap or inform PDU to a list of notification destinations.  If additional inconsistency is detected within the  throttling period, then notification\-events for these inconsistencies should be suppressed by the agent until the current throttling period expires.  At the end of a throttling period, one notification\-event should be generated if any inconsistency was detected since the start of the  throttling period. In such a case,  another throttling period is started right away.  An NMS should periodically poll cefInconsistencyRecordTable to detect any missed cefInconsistencyDetection notification\-events, e.g., due to throttling or transmission loss.   If cefNotifThrottlingInterval notification generation is enabled, the suggested default throttling period is 60 seconds, but generation of the cefInconsistencyDetection notification should be disabled by default.  If the agent is capable of storing non\-volatile configuration, then the value of this object must be restored after a re\-initialization of the management system.  The actual transmission of notifications is controlled via the MIB modules in RFC 3413
        	**type**\:  int
        
        	**range:** 0..3600
        
        	**units**\: seconds
        
        .. attribute:: cefpeerfibstatechangenotifenable
        
        	Indicates whether or not a notification should be generated on the detection of CEF FIB peer state change
        	**type**\:  bool
        
        .. attribute:: cefpeerstatechangenotifenable
        
        	Indicates whether or not a notification should be generated on the detection of CEF peer state change
        	**type**\:  bool
        
        .. attribute:: cefresourcefailurenotifenable
        
        	Indicates whether or not a notification should be generated on the detection of CEF resource Failure
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Cefnotifcntl, self).__init__()

            self.yang_name = "cefNotifCntl"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.cefinconsistencynotifenable = YLeaf(YType.boolean, "cefInconsistencyNotifEnable")

            self.cefnotifthrottlinginterval = YLeaf(YType.int32, "cefNotifThrottlingInterval")

            self.cefpeerfibstatechangenotifenable = YLeaf(YType.boolean, "cefPeerFIBStateChangeNotifEnable")

            self.cefpeerstatechangenotifenable = YLeaf(YType.boolean, "cefPeerStateChangeNotifEnable")

            self.cefresourcefailurenotifenable = YLeaf(YType.boolean, "cefResourceFailureNotifEnable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cefinconsistencynotifenable",
                            "cefnotifthrottlinginterval",
                            "cefpeerfibstatechangenotifenable",
                            "cefpeerstatechangenotifenable",
                            "cefresourcefailurenotifenable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Cefnotifcntl, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Cefnotifcntl, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cefinconsistencynotifenable.is_set or
                self.cefnotifthrottlinginterval.is_set or
                self.cefpeerfibstatechangenotifenable.is_set or
                self.cefpeerstatechangenotifenable.is_set or
                self.cefresourcefailurenotifenable.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cefinconsistencynotifenable.yfilter != YFilter.not_set or
                self.cefnotifthrottlinginterval.yfilter != YFilter.not_set or
                self.cefpeerfibstatechangenotifenable.yfilter != YFilter.not_set or
                self.cefpeerstatechangenotifenable.yfilter != YFilter.not_set or
                self.cefresourcefailurenotifenable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefNotifCntl" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cefinconsistencynotifenable.is_set or self.cefinconsistencynotifenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cefinconsistencynotifenable.get_name_leafdata())
            if (self.cefnotifthrottlinginterval.is_set or self.cefnotifthrottlinginterval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cefnotifthrottlinginterval.get_name_leafdata())
            if (self.cefpeerfibstatechangenotifenable.is_set or self.cefpeerfibstatechangenotifenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cefpeerfibstatechangenotifenable.get_name_leafdata())
            if (self.cefpeerstatechangenotifenable.is_set or self.cefpeerstatechangenotifenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cefpeerstatechangenotifenable.get_name_leafdata())
            if (self.cefresourcefailurenotifenable.is_set or self.cefresourcefailurenotifenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cefresourcefailurenotifenable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefInconsistencyNotifEnable" or name == "cefNotifThrottlingInterval" or name == "cefPeerFIBStateChangeNotifEnable" or name == "cefPeerStateChangeNotifEnable" or name == "cefResourceFailureNotifEnable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cefInconsistencyNotifEnable"):
                self.cefinconsistencynotifenable = value
                self.cefinconsistencynotifenable.value_namespace = name_space
                self.cefinconsistencynotifenable.value_namespace_prefix = name_space_prefix
            if(value_path == "cefNotifThrottlingInterval"):
                self.cefnotifthrottlinginterval = value
                self.cefnotifthrottlinginterval.value_namespace = name_space
                self.cefnotifthrottlinginterval.value_namespace_prefix = name_space_prefix
            if(value_path == "cefPeerFIBStateChangeNotifEnable"):
                self.cefpeerfibstatechangenotifenable = value
                self.cefpeerfibstatechangenotifenable.value_namespace = name_space
                self.cefpeerfibstatechangenotifenable.value_namespace_prefix = name_space_prefix
            if(value_path == "cefPeerStateChangeNotifEnable"):
                self.cefpeerstatechangenotifenable = value
                self.cefpeerstatechangenotifenable.value_namespace = name_space
                self.cefpeerstatechangenotifenable.value_namespace_prefix = name_space_prefix
            if(value_path == "cefResourceFailureNotifEnable"):
                self.cefresourcefailurenotifenable = value
                self.cefresourcefailurenotifenable.value_namespace = name_space
                self.cefresourcefailurenotifenable.value_namespace_prefix = name_space_prefix


    class Ceffibsummarytable(Entity):
        """
        This table contains the summary information
        for the cefPrefixTable.
        
        .. attribute:: ceffibsummaryentry
        
        	If CEF is enabled on the Managed device, each entry contains the FIB summary related attributes for the managed entity.  A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of    :py:class:`Ceffibsummaryentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Ceffibsummarytable.Ceffibsummaryentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Ceffibsummarytable, self).__init__()

            self.yang_name = "cefFIBSummaryTable"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.ceffibsummaryentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Ceffibsummarytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Ceffibsummarytable, self).__setattr__(name, value)


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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceffibipversion  <key>
            
            	The version of IP forwarding
            	**type**\:   :py:class:`Cefipversion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefipversion>`
            
            .. attribute:: ceffibsummaryfwdprefixes
            
            	Total number of forwarding Prefixes in FIB for the IP version specified by cefFIBIpVersion object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CiscoCefMib.Ceffibsummarytable.Ceffibsummaryentry, self).__init__()

                self.yang_name = "cefFIBSummaryEntry"
                self.yang_parent_name = "cefFIBSummaryTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ceffibipversion = YLeaf(YType.enumeration, "cefFIBIpVersion")

                self.ceffibsummaryfwdprefixes = YLeaf(YType.uint32, "cefFIBSummaryFwdPrefixes")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "ceffibipversion",
                                "ceffibsummaryfwdprefixes") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCefMib.Ceffibsummarytable.Ceffibsummaryentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCefMib.Ceffibsummarytable.Ceffibsummaryentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.ceffibipversion.is_set or
                    self.ceffibsummaryfwdprefixes.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.ceffibipversion.yfilter != YFilter.not_set or
                    self.ceffibsummaryfwdprefixes.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefFIBSummaryEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cefFIBIpVersion='" + self.ceffibipversion.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/cefFIBSummaryTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.ceffibipversion.is_set or self.ceffibipversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffibipversion.get_name_leafdata())
                if (self.ceffibsummaryfwdprefixes.is_set or self.ceffibsummaryfwdprefixes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffibsummaryfwdprefixes.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefFIBIpVersion" or name == "cefFIBSummaryFwdPrefixes"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefFIBIpVersion"):
                    self.ceffibipversion = value
                    self.ceffibipversion.value_namespace = name_space
                    self.ceffibipversion.value_namespace_prefix = name_space_prefix
                if(value_path == "cefFIBSummaryFwdPrefixes"):
                    self.ceffibsummaryfwdprefixes = value
                    self.ceffibsummaryfwdprefixes.value_namespace = name_space
                    self.ceffibsummaryfwdprefixes.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ceffibsummaryentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ceffibsummaryentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefFIBSummaryTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefFIBSummaryEntry"):
                for c in self.ceffibsummaryentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCefMib.Ceffibsummarytable.Ceffibsummaryentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ceffibsummaryentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefFIBSummaryEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefprefixtable(Entity):
        """
        A list of CEF forwarding prefixes.
        
        .. attribute:: cefprefixentry
        
        	If CEF is enabled on the Managed device, each entry contains the forwarding  prefix attributes.   CEF prefix based non\-recursive stats are maintained in internal and external buckets (depending upon the  value of cefIntNonrecursiveAccouting object in the  CefIntEntry).  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of    :py:class:`Cefprefixentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefprefixtable.Cefprefixentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Cefprefixtable, self).__init__()

            self.yang_name = "cefPrefixTable"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.cefprefixentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Cefprefixtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Cefprefixtable, self).__setattr__(name, value)


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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefprefixtype  <key>
            
            	The Network Prefix Type. This object specifies the address type used for cefPrefixAddr.  Prefix entries are only valid for the address type of ipv4(1) and ipv6(2)
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cefprefixaddr  <key>
            
            	The Network Prefix Address. The type of this address is determined by the value of the cefPrefixType object. This object is a Prefix Address containing the  prefix with length specified by cefPrefixLen.  Any bits beyond the length specified by cefPrefixLen are zeroed
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cefprefixlen  <key>
            
            	Length in bits of the FIB Address prefix
            	**type**\:  int
            
            	**range:** 0..2040
            
            .. attribute:: cefprefixbytes
            
            	If CEF accounting is set to enable per prefix accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'perPrefix'  accounting), then this object represents the  number of bytes switched to this prefix
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cefprefixexternalnrbytes
            
            	If CEF accounting is set to enable nonRecursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents  the number of non\-recursive bytes in the external bucket switched using this prefix
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cefprefixexternalnrhcbytes
            
            	If CEF accounting is set to enable nonRecursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents  the number of non\-recursive bytes in the external bucket switched using this prefix.  This object is a 64\-bit version of  cefPrefixExternalNRBytes
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cefprefixexternalnrhcpkts
            
            	If CEF accounting is set to enable non\-recursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents the number of non\-recursive packets in the external bucket switched using this prefix.  This object is a 64\-bit version of  cefPrefixExternalNRPkts
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cefprefixexternalnrpkts
            
            	If CEF accounting is set to enable non\-recursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents the number of non\-recursive packets in the external bucket switched using this prefix
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cefprefixforwardinginfo
            
            	This object indicates the associated forwarding element selection entries in cefFESelectionTable. The value of this object is index value (cefFESelectionName) of cefFESelectionTable
            	**type**\:  str
            
            .. attribute:: cefprefixhcbytes
            
            	If CEF accounting is set to enable per prefix accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'perPrefix'  accounting), then this object represents the  number of bytes switched to this prefix.  This object is a 64\-bit version of  cefPrefixBytes
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cefprefixhcpkts
            
            	If CEF accounting is set to enable per prefix accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'perPrefix'  accounting), then this object represents the  number of packets switched to this prefix.   This object is a 64\-bit version of  cefPrefixPkts
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cefprefixinternalnrbytes
            
            	If CEF accounting is set to enable nonRecursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents  the number of non\-recursive bytes in the internal bucket switched using this prefix
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cefprefixinternalnrhcbytes
            
            	If CEF accounting is set to enable nonRecursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents  the number of non\-recursive bytes in the internal bucket switched using this prefix.  This object is a 64\-bit version of  cefPrefixInternalNRBytes
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cefprefixinternalnrhcpkts
            
            	If CEF accounting is set to enable non\-recursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents the number of non\-recursive packets in the internal bucket switched using this prefix.  This object is a 64\-bit version of  cefPrefixInternalNRPkts
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cefprefixinternalnrpkts
            
            	If CEF accounting is set to enable non\-recursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents the number of non\-recursive packets in the internal bucket switched using this prefix
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cefprefixpkts
            
            	If CEF accounting is set to enable per prefix accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'perPrefix'  accounting), then this object represents the  number of packets switched to this prefix
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CiscoCefMib.Cefprefixtable.Cefprefixentry, self).__init__()

                self.yang_name = "cefPrefixEntry"
                self.yang_parent_name = "cefPrefixTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefprefixtype = YLeaf(YType.enumeration, "cefPrefixType")

                self.cefprefixaddr = YLeaf(YType.str, "cefPrefixAddr")

                self.cefprefixlen = YLeaf(YType.uint32, "cefPrefixLen")

                self.cefprefixbytes = YLeaf(YType.uint32, "cefPrefixBytes")

                self.cefprefixexternalnrbytes = YLeaf(YType.uint32, "cefPrefixExternalNRBytes")

                self.cefprefixexternalnrhcbytes = YLeaf(YType.uint64, "cefPrefixExternalNRHCBytes")

                self.cefprefixexternalnrhcpkts = YLeaf(YType.uint64, "cefPrefixExternalNRHCPkts")

                self.cefprefixexternalnrpkts = YLeaf(YType.uint32, "cefPrefixExternalNRPkts")

                self.cefprefixforwardinginfo = YLeaf(YType.str, "cefPrefixForwardingInfo")

                self.cefprefixhcbytes = YLeaf(YType.uint64, "cefPrefixHCBytes")

                self.cefprefixhcpkts = YLeaf(YType.uint64, "cefPrefixHCPkts")

                self.cefprefixinternalnrbytes = YLeaf(YType.uint32, "cefPrefixInternalNRBytes")

                self.cefprefixinternalnrhcbytes = YLeaf(YType.uint64, "cefPrefixInternalNRHCBytes")

                self.cefprefixinternalnrhcpkts = YLeaf(YType.uint64, "cefPrefixInternalNRHCPkts")

                self.cefprefixinternalnrpkts = YLeaf(YType.uint32, "cefPrefixInternalNRPkts")

                self.cefprefixpkts = YLeaf(YType.uint32, "cefPrefixPkts")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefprefixtype",
                                "cefprefixaddr",
                                "cefprefixlen",
                                "cefprefixbytes",
                                "cefprefixexternalnrbytes",
                                "cefprefixexternalnrhcbytes",
                                "cefprefixexternalnrhcpkts",
                                "cefprefixexternalnrpkts",
                                "cefprefixforwardinginfo",
                                "cefprefixhcbytes",
                                "cefprefixhcpkts",
                                "cefprefixinternalnrbytes",
                                "cefprefixinternalnrhcbytes",
                                "cefprefixinternalnrhcpkts",
                                "cefprefixinternalnrpkts",
                                "cefprefixpkts") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCefMib.Cefprefixtable.Cefprefixentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCefMib.Cefprefixtable.Cefprefixentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefprefixtype.is_set or
                    self.cefprefixaddr.is_set or
                    self.cefprefixlen.is_set or
                    self.cefprefixbytes.is_set or
                    self.cefprefixexternalnrbytes.is_set or
                    self.cefprefixexternalnrhcbytes.is_set or
                    self.cefprefixexternalnrhcpkts.is_set or
                    self.cefprefixexternalnrpkts.is_set or
                    self.cefprefixforwardinginfo.is_set or
                    self.cefprefixhcbytes.is_set or
                    self.cefprefixhcpkts.is_set or
                    self.cefprefixinternalnrbytes.is_set or
                    self.cefprefixinternalnrhcbytes.is_set or
                    self.cefprefixinternalnrhcpkts.is_set or
                    self.cefprefixinternalnrpkts.is_set or
                    self.cefprefixpkts.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefprefixtype.yfilter != YFilter.not_set or
                    self.cefprefixaddr.yfilter != YFilter.not_set or
                    self.cefprefixlen.yfilter != YFilter.not_set or
                    self.cefprefixbytes.yfilter != YFilter.not_set or
                    self.cefprefixexternalnrbytes.yfilter != YFilter.not_set or
                    self.cefprefixexternalnrhcbytes.yfilter != YFilter.not_set or
                    self.cefprefixexternalnrhcpkts.yfilter != YFilter.not_set or
                    self.cefprefixexternalnrpkts.yfilter != YFilter.not_set or
                    self.cefprefixforwardinginfo.yfilter != YFilter.not_set or
                    self.cefprefixhcbytes.yfilter != YFilter.not_set or
                    self.cefprefixhcpkts.yfilter != YFilter.not_set or
                    self.cefprefixinternalnrbytes.yfilter != YFilter.not_set or
                    self.cefprefixinternalnrhcbytes.yfilter != YFilter.not_set or
                    self.cefprefixinternalnrhcpkts.yfilter != YFilter.not_set or
                    self.cefprefixinternalnrpkts.yfilter != YFilter.not_set or
                    self.cefprefixpkts.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefPrefixEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cefPrefixType='" + self.cefprefixtype.get() + "']" + "[cefPrefixAddr='" + self.cefprefixaddr.get() + "']" + "[cefPrefixLen='" + self.cefprefixlen.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/cefPrefixTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefprefixtype.is_set or self.cefprefixtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixtype.get_name_leafdata())
                if (self.cefprefixaddr.is_set or self.cefprefixaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixaddr.get_name_leafdata())
                if (self.cefprefixlen.is_set or self.cefprefixlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixlen.get_name_leafdata())
                if (self.cefprefixbytes.is_set or self.cefprefixbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixbytes.get_name_leafdata())
                if (self.cefprefixexternalnrbytes.is_set or self.cefprefixexternalnrbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixexternalnrbytes.get_name_leafdata())
                if (self.cefprefixexternalnrhcbytes.is_set or self.cefprefixexternalnrhcbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixexternalnrhcbytes.get_name_leafdata())
                if (self.cefprefixexternalnrhcpkts.is_set or self.cefprefixexternalnrhcpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixexternalnrhcpkts.get_name_leafdata())
                if (self.cefprefixexternalnrpkts.is_set or self.cefprefixexternalnrpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixexternalnrpkts.get_name_leafdata())
                if (self.cefprefixforwardinginfo.is_set or self.cefprefixforwardinginfo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixforwardinginfo.get_name_leafdata())
                if (self.cefprefixhcbytes.is_set or self.cefprefixhcbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixhcbytes.get_name_leafdata())
                if (self.cefprefixhcpkts.is_set or self.cefprefixhcpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixhcpkts.get_name_leafdata())
                if (self.cefprefixinternalnrbytes.is_set or self.cefprefixinternalnrbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixinternalnrbytes.get_name_leafdata())
                if (self.cefprefixinternalnrhcbytes.is_set or self.cefprefixinternalnrhcbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixinternalnrhcbytes.get_name_leafdata())
                if (self.cefprefixinternalnrhcpkts.is_set or self.cefprefixinternalnrhcpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixinternalnrhcpkts.get_name_leafdata())
                if (self.cefprefixinternalnrpkts.is_set or self.cefprefixinternalnrpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixinternalnrpkts.get_name_leafdata())
                if (self.cefprefixpkts.is_set or self.cefprefixpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixpkts.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefPrefixType" or name == "cefPrefixAddr" or name == "cefPrefixLen" or name == "cefPrefixBytes" or name == "cefPrefixExternalNRBytes" or name == "cefPrefixExternalNRHCBytes" or name == "cefPrefixExternalNRHCPkts" or name == "cefPrefixExternalNRPkts" or name == "cefPrefixForwardingInfo" or name == "cefPrefixHCBytes" or name == "cefPrefixHCPkts" or name == "cefPrefixInternalNRBytes" or name == "cefPrefixInternalNRHCBytes" or name == "cefPrefixInternalNRHCPkts" or name == "cefPrefixInternalNRPkts" or name == "cefPrefixPkts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixType"):
                    self.cefprefixtype = value
                    self.cefprefixtype.value_namespace = name_space
                    self.cefprefixtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixAddr"):
                    self.cefprefixaddr = value
                    self.cefprefixaddr.value_namespace = name_space
                    self.cefprefixaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixLen"):
                    self.cefprefixlen = value
                    self.cefprefixlen.value_namespace = name_space
                    self.cefprefixlen.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixBytes"):
                    self.cefprefixbytes = value
                    self.cefprefixbytes.value_namespace = name_space
                    self.cefprefixbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixExternalNRBytes"):
                    self.cefprefixexternalnrbytes = value
                    self.cefprefixexternalnrbytes.value_namespace = name_space
                    self.cefprefixexternalnrbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixExternalNRHCBytes"):
                    self.cefprefixexternalnrhcbytes = value
                    self.cefprefixexternalnrhcbytes.value_namespace = name_space
                    self.cefprefixexternalnrhcbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixExternalNRHCPkts"):
                    self.cefprefixexternalnrhcpkts = value
                    self.cefprefixexternalnrhcpkts.value_namespace = name_space
                    self.cefprefixexternalnrhcpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixExternalNRPkts"):
                    self.cefprefixexternalnrpkts = value
                    self.cefprefixexternalnrpkts.value_namespace = name_space
                    self.cefprefixexternalnrpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixForwardingInfo"):
                    self.cefprefixforwardinginfo = value
                    self.cefprefixforwardinginfo.value_namespace = name_space
                    self.cefprefixforwardinginfo.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixHCBytes"):
                    self.cefprefixhcbytes = value
                    self.cefprefixhcbytes.value_namespace = name_space
                    self.cefprefixhcbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixHCPkts"):
                    self.cefprefixhcpkts = value
                    self.cefprefixhcpkts.value_namespace = name_space
                    self.cefprefixhcpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixInternalNRBytes"):
                    self.cefprefixinternalnrbytes = value
                    self.cefprefixinternalnrbytes.value_namespace = name_space
                    self.cefprefixinternalnrbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixInternalNRHCBytes"):
                    self.cefprefixinternalnrhcbytes = value
                    self.cefprefixinternalnrhcbytes.value_namespace = name_space
                    self.cefprefixinternalnrhcbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixInternalNRHCPkts"):
                    self.cefprefixinternalnrhcpkts = value
                    self.cefprefixinternalnrhcpkts.value_namespace = name_space
                    self.cefprefixinternalnrhcpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixInternalNRPkts"):
                    self.cefprefixinternalnrpkts = value
                    self.cefprefixinternalnrpkts.value_namespace = name_space
                    self.cefprefixinternalnrpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixPkts"):
                    self.cefprefixpkts = value
                    self.cefprefixpkts.value_namespace = name_space
                    self.cefprefixpkts.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefprefixentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefprefixentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefPrefixTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefPrefixEntry"):
                for c in self.cefprefixentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCefMib.Cefprefixtable.Cefprefixentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefprefixentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefPrefixEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ceflmprefixtable(Entity):
        """
        A table of Longest Match Prefix Query requests.
        
        Generator application should utilize the
        cefLMPrefixSpinLock to try to avoid collisions.
        See DESCRIPTION clause of cefLMPrefixSpinLock.
        
        .. attribute:: ceflmprefixentry
        
        	If CEF is enabled on the managed device, then each entry represents a longest Match Prefix request.  A management station wishing to get the longest Match prefix for a given destination address should create the associate instance of the row status. The row status should be set to active(1) to initiate the request. Note that  this entire procedure may be initiated via a  single set request which specifies a row status  of createAndGo(4).  Once the request completes, the management station  should retrieve the values of the objects of  interest, and should then delete the entry.  In order  to prevent old entries from clogging the table,  entries will be aged out, but an entry will never be  deleted within 5 minutes of completion. Entries are lost after an agent restart.  I.e. to find out the longest prefix match for  destination address of A.B.C.D on entity whose entityPhysicalIndex is 1, the Management station will create an entry in cefLMPrefixTable with cefLMPrefixRowStatus.1(entPhysicalIndex).1(ipv4).A.B.C.D set to createAndGo(4). Management Station may query the value of objects cefLMPrefix and cefLMPrefixLen to find out the corresponding prefix entry from the cefPrefixTable once the value of cefLMPrefixState is set to matchFound(2).  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of    :py:class:`Ceflmprefixentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Ceflmprefixtable.Ceflmprefixentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Ceflmprefixtable, self).__init__()

            self.yang_name = "cefLMPrefixTable"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.ceflmprefixentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Ceflmprefixtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Ceflmprefixtable, self).__setattr__(name, value)


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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceflmprefixdestaddrtype  <key>
            
            	The Destination Address Type. This object specifies the address type used for cefLMPrefixDestAddr.  Longest Match Prefix entries are only valid  for the address type of ipv4(1) and ipv6(2)
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ceflmprefixdestaddr  <key>
            
            	The Destination Address. The type of this address is determined by the value of the cefLMPrefixDestAddrType object
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ceflmprefixaddr
            
            	The Network Prefix Address. Index to the cefPrefixTable. The type of this address is determined by the value of the cefLMPrefixDestAddrType object
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ceflmprefixlen
            
            	The Network Prefix Length. Index to the cefPrefixTable
            	**type**\:  int
            
            	**range:** 0..2040
            
            .. attribute:: ceflmprefixrowstatus
            
            	The status of this table entry.  Once the entry  status is set to active(1), the associated entry  cannot be modified until the request completes (cefLMPrefixState transitions to matchFound(2)  or noMatchFound(3)).  Once the longest match request has been created (i.e. the cefLMPrefixRowStatus has been made active), the entry cannot be modified \- the only operation possible after this is to delete the row
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ceflmprefixstate
            
            	Indicates the state of this prefix search request
            	**type**\:   :py:class:`Cefprefixsearchstate <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefprefixsearchstate>`
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CiscoCefMib.Ceflmprefixtable.Ceflmprefixentry, self).__init__()

                self.yang_name = "cefLMPrefixEntry"
                self.yang_parent_name = "cefLMPrefixTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ceflmprefixdestaddrtype = YLeaf(YType.enumeration, "cefLMPrefixDestAddrType")

                self.ceflmprefixdestaddr = YLeaf(YType.str, "cefLMPrefixDestAddr")

                self.ceflmprefixaddr = YLeaf(YType.str, "cefLMPrefixAddr")

                self.ceflmprefixlen = YLeaf(YType.uint32, "cefLMPrefixLen")

                self.ceflmprefixrowstatus = YLeaf(YType.enumeration, "cefLMPrefixRowStatus")

                self.ceflmprefixstate = YLeaf(YType.enumeration, "cefLMPrefixState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "ceflmprefixdestaddrtype",
                                "ceflmprefixdestaddr",
                                "ceflmprefixaddr",
                                "ceflmprefixlen",
                                "ceflmprefixrowstatus",
                                "ceflmprefixstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCefMib.Ceflmprefixtable.Ceflmprefixentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCefMib.Ceflmprefixtable.Ceflmprefixentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.ceflmprefixdestaddrtype.is_set or
                    self.ceflmprefixdestaddr.is_set or
                    self.ceflmprefixaddr.is_set or
                    self.ceflmprefixlen.is_set or
                    self.ceflmprefixrowstatus.is_set or
                    self.ceflmprefixstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.ceflmprefixdestaddrtype.yfilter != YFilter.not_set or
                    self.ceflmprefixdestaddr.yfilter != YFilter.not_set or
                    self.ceflmprefixaddr.yfilter != YFilter.not_set or
                    self.ceflmprefixlen.yfilter != YFilter.not_set or
                    self.ceflmprefixrowstatus.yfilter != YFilter.not_set or
                    self.ceflmprefixstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefLMPrefixEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cefLMPrefixDestAddrType='" + self.ceflmprefixdestaddrtype.get() + "']" + "[cefLMPrefixDestAddr='" + self.ceflmprefixdestaddr.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/cefLMPrefixTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.ceflmprefixdestaddrtype.is_set or self.ceflmprefixdestaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceflmprefixdestaddrtype.get_name_leafdata())
                if (self.ceflmprefixdestaddr.is_set or self.ceflmprefixdestaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceflmprefixdestaddr.get_name_leafdata())
                if (self.ceflmprefixaddr.is_set or self.ceflmprefixaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceflmprefixaddr.get_name_leafdata())
                if (self.ceflmprefixlen.is_set or self.ceflmprefixlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceflmprefixlen.get_name_leafdata())
                if (self.ceflmprefixrowstatus.is_set or self.ceflmprefixrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceflmprefixrowstatus.get_name_leafdata())
                if (self.ceflmprefixstate.is_set or self.ceflmprefixstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceflmprefixstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefLMPrefixDestAddrType" or name == "cefLMPrefixDestAddr" or name == "cefLMPrefixAddr" or name == "cefLMPrefixLen" or name == "cefLMPrefixRowStatus" or name == "cefLMPrefixState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefLMPrefixDestAddrType"):
                    self.ceflmprefixdestaddrtype = value
                    self.ceflmprefixdestaddrtype.value_namespace = name_space
                    self.ceflmprefixdestaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cefLMPrefixDestAddr"):
                    self.ceflmprefixdestaddr = value
                    self.ceflmprefixdestaddr.value_namespace = name_space
                    self.ceflmprefixdestaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cefLMPrefixAddr"):
                    self.ceflmprefixaddr = value
                    self.ceflmprefixaddr.value_namespace = name_space
                    self.ceflmprefixaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cefLMPrefixLen"):
                    self.ceflmprefixlen = value
                    self.ceflmprefixlen.value_namespace = name_space
                    self.ceflmprefixlen.value_namespace_prefix = name_space_prefix
                if(value_path == "cefLMPrefixRowStatus"):
                    self.ceflmprefixrowstatus = value
                    self.ceflmprefixrowstatus.value_namespace = name_space
                    self.ceflmprefixrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cefLMPrefixState"):
                    self.ceflmprefixstate = value
                    self.ceflmprefixstate.value_namespace = name_space
                    self.ceflmprefixstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ceflmprefixentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ceflmprefixentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefLMPrefixTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefLMPrefixEntry"):
                for c in self.ceflmprefixentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCefMib.Ceflmprefixtable.Ceflmprefixentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ceflmprefixentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefLMPrefixEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefpathtable(Entity):
        """
        CEF prefix path is a valid route to reach to a 
        destination IP prefix. Multiple paths may exist 
        out of a router to the same destination prefix. 
        This table specify lists of CEF paths.
        
        .. attribute:: cefpathentry
        
        	If CEF is enabled on the Managed device, each entry contain a CEF prefix path.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of    :py:class:`Cefpathentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefpathtable.Cefpathentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Cefpathtable, self).__init__()

            self.yang_name = "cefPathTable"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.cefpathentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Cefpathtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Cefpathtable, self).__setattr__(name, value)


        class Cefpathentry(Entity):
            """
            If CEF is enabled on the Managed device,
            each entry contain a CEF prefix path.
            
            entPhysicalIndex is also an index for this
            table which represents entities of
            'module' entPhysicalClass which are capable
            of running CEF.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefprefixtype  <key>
            
            	
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cefprefixaddr  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..255
            
            	**refers to**\:  :py:class:`cefprefixaddr <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefprefixtable.Cefprefixentry>`
            
            .. attribute:: cefprefixlen  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..2040
            
            	**refers to**\:  :py:class:`cefprefixlen <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefprefixtable.Cefprefixentry>`
            
            .. attribute:: cefpathid  <key>
            
            	The locally arbitrary, but unique identifier associated with this prefix path entry
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefpathinterface
            
            	Interface associated with this CEF path.  A value of zero for this object will indicate that no interface is associated with this path  entry
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cefpathnexthopaddr
            
            	Next hop address associated with this CEF path.  The value of this object is only relevant for attached next hop and recursive next hop   path types (when the object cefPathType is set to attachedNexthop(4) or recursiveNexthop(5)). and will be set to zero for other path types.  The type of this address is determined by the value of the cefPrefixType object
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cefpathrecursevrfname
            
            	The recursive vrf name associated with this path.  The value of this object is only relevant for recursive next hop path types (when the  object cefPathType is set to recursiveNexthop(5)), and '0x00' will be returned for other path types
            	**type**\:  str
            
            	**length:** 0..31
            
            .. attribute:: cefpathtype
            
            	Type for this CEF Path
            	**type**\:   :py:class:`Cefpathtype <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefpathtype>`
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CiscoCefMib.Cefpathtable.Cefpathentry, self).__init__()

                self.yang_name = "cefPathEntry"
                self.yang_parent_name = "cefPathTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefprefixtype = YLeaf(YType.enumeration, "cefPrefixType")

                self.cefprefixaddr = YLeaf(YType.str, "cefPrefixAddr")

                self.cefprefixlen = YLeaf(YType.str, "cefPrefixLen")

                self.cefpathid = YLeaf(YType.int32, "cefPathId")

                self.cefpathinterface = YLeaf(YType.int32, "cefPathInterface")

                self.cefpathnexthopaddr = YLeaf(YType.str, "cefPathNextHopAddr")

                self.cefpathrecursevrfname = YLeaf(YType.str, "cefPathRecurseVrfName")

                self.cefpathtype = YLeaf(YType.enumeration, "cefPathType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefprefixtype",
                                "cefprefixaddr",
                                "cefprefixlen",
                                "cefpathid",
                                "cefpathinterface",
                                "cefpathnexthopaddr",
                                "cefpathrecursevrfname",
                                "cefpathtype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCefMib.Cefpathtable.Cefpathentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCefMib.Cefpathtable.Cefpathentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefprefixtype.is_set or
                    self.cefprefixaddr.is_set or
                    self.cefprefixlen.is_set or
                    self.cefpathid.is_set or
                    self.cefpathinterface.is_set or
                    self.cefpathnexthopaddr.is_set or
                    self.cefpathrecursevrfname.is_set or
                    self.cefpathtype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefprefixtype.yfilter != YFilter.not_set or
                    self.cefprefixaddr.yfilter != YFilter.not_set or
                    self.cefprefixlen.yfilter != YFilter.not_set or
                    self.cefpathid.yfilter != YFilter.not_set or
                    self.cefpathinterface.yfilter != YFilter.not_set or
                    self.cefpathnexthopaddr.yfilter != YFilter.not_set or
                    self.cefpathrecursevrfname.yfilter != YFilter.not_set or
                    self.cefpathtype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefPathEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cefPrefixType='" + self.cefprefixtype.get() + "']" + "[cefPrefixAddr='" + self.cefprefixaddr.get() + "']" + "[cefPrefixLen='" + self.cefprefixlen.get() + "']" + "[cefPathId='" + self.cefpathid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/cefPathTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefprefixtype.is_set or self.cefprefixtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixtype.get_name_leafdata())
                if (self.cefprefixaddr.is_set or self.cefprefixaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixaddr.get_name_leafdata())
                if (self.cefprefixlen.is_set or self.cefprefixlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefprefixlen.get_name_leafdata())
                if (self.cefpathid.is_set or self.cefpathid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefpathid.get_name_leafdata())
                if (self.cefpathinterface.is_set or self.cefpathinterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefpathinterface.get_name_leafdata())
                if (self.cefpathnexthopaddr.is_set or self.cefpathnexthopaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefpathnexthopaddr.get_name_leafdata())
                if (self.cefpathrecursevrfname.is_set or self.cefpathrecursevrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefpathrecursevrfname.get_name_leafdata())
                if (self.cefpathtype.is_set or self.cefpathtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefpathtype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefPrefixType" or name == "cefPrefixAddr" or name == "cefPrefixLen" or name == "cefPathId" or name == "cefPathInterface" or name == "cefPathNextHopAddr" or name == "cefPathRecurseVrfName" or name == "cefPathType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixType"):
                    self.cefprefixtype = value
                    self.cefprefixtype.value_namespace = name_space
                    self.cefprefixtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixAddr"):
                    self.cefprefixaddr = value
                    self.cefprefixaddr.value_namespace = name_space
                    self.cefprefixaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPrefixLen"):
                    self.cefprefixlen = value
                    self.cefprefixlen.value_namespace = name_space
                    self.cefprefixlen.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPathId"):
                    self.cefpathid = value
                    self.cefpathid.value_namespace = name_space
                    self.cefpathid.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPathInterface"):
                    self.cefpathinterface = value
                    self.cefpathinterface.value_namespace = name_space
                    self.cefpathinterface.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPathNextHopAddr"):
                    self.cefpathnexthopaddr = value
                    self.cefpathnexthopaddr.value_namespace = name_space
                    self.cefpathnexthopaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPathRecurseVrfName"):
                    self.cefpathrecursevrfname = value
                    self.cefpathrecursevrfname.value_namespace = name_space
                    self.cefpathrecursevrfname.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPathType"):
                    self.cefpathtype = value
                    self.cefpathtype.value_namespace = name_space
                    self.cefpathtype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefpathentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefpathentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefPathTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefPathEntry"):
                for c in self.cefpathentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCefMib.Cefpathtable.Cefpathentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefpathentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefPathEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefadjsummarytable(Entity):
        """
        This table contains the summary information
        for the cefAdjTable.
        
        .. attribute:: cefadjsummaryentry
        
        	If CEF is enabled on the Managed device, each entry contains the CEF Adjacency   summary related attributes for the Managed entity. A row exists for each adjacency link type.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of    :py:class:`Cefadjsummaryentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefadjsummarytable.Cefadjsummaryentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Cefadjsummarytable, self).__init__()

            self.yang_name = "cefAdjSummaryTable"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.cefadjsummaryentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Cefadjsummarytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Cefadjsummarytable, self).__setattr__(name, value)


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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefadjsummarylinktype  <key>
            
            	The link type of the adjacency
            	**type**\:   :py:class:`Cefadjlinktype <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefadjlinktype>`
            
            .. attribute:: cefadjsummarycomplete
            
            	The total number of complete adjacencies.  The total number of adjacencies which can be used  to switch traffic to a neighbour
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefadjsummaryfixup
            
            	The total number of adjacencies for which the Layer 2 encapsulation string (header) may be  updated (fixed up) at packet switch time
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefadjsummaryincomplete
            
            	The total number of incomplete adjacencies.  The total number of adjacencies which cannot be  used to switch traffic in their current state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefadjsummaryredirect
            
            	The total number of adjacencies for which  ip redirect (or icmp redirection) is enabled. The value of this object is only relevant for ipv4 and ipv6 link type (when the index object  cefAdjSummaryLinkType value is ipv4(1) or ipv6(2)) and will be set to zero for other link types
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CiscoCefMib.Cefadjsummarytable.Cefadjsummaryentry, self).__init__()

                self.yang_name = "cefAdjSummaryEntry"
                self.yang_parent_name = "cefAdjSummaryTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefadjsummarylinktype = YLeaf(YType.enumeration, "cefAdjSummaryLinkType")

                self.cefadjsummarycomplete = YLeaf(YType.uint32, "cefAdjSummaryComplete")

                self.cefadjsummaryfixup = YLeaf(YType.uint32, "cefAdjSummaryFixup")

                self.cefadjsummaryincomplete = YLeaf(YType.uint32, "cefAdjSummaryIncomplete")

                self.cefadjsummaryredirect = YLeaf(YType.uint32, "cefAdjSummaryRedirect")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefadjsummarylinktype",
                                "cefadjsummarycomplete",
                                "cefadjsummaryfixup",
                                "cefadjsummaryincomplete",
                                "cefadjsummaryredirect") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCefMib.Cefadjsummarytable.Cefadjsummaryentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCefMib.Cefadjsummarytable.Cefadjsummaryentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefadjsummarylinktype.is_set or
                    self.cefadjsummarycomplete.is_set or
                    self.cefadjsummaryfixup.is_set or
                    self.cefadjsummaryincomplete.is_set or
                    self.cefadjsummaryredirect.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefadjsummarylinktype.yfilter != YFilter.not_set or
                    self.cefadjsummarycomplete.yfilter != YFilter.not_set or
                    self.cefadjsummaryfixup.yfilter != YFilter.not_set or
                    self.cefadjsummaryincomplete.yfilter != YFilter.not_set or
                    self.cefadjsummaryredirect.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefAdjSummaryEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cefAdjSummaryLinkType='" + self.cefadjsummarylinktype.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/cefAdjSummaryTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefadjsummarylinktype.is_set or self.cefadjsummarylinktype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefadjsummarylinktype.get_name_leafdata())
                if (self.cefadjsummarycomplete.is_set or self.cefadjsummarycomplete.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefadjsummarycomplete.get_name_leafdata())
                if (self.cefadjsummaryfixup.is_set or self.cefadjsummaryfixup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefadjsummaryfixup.get_name_leafdata())
                if (self.cefadjsummaryincomplete.is_set or self.cefadjsummaryincomplete.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefadjsummaryincomplete.get_name_leafdata())
                if (self.cefadjsummaryredirect.is_set or self.cefadjsummaryredirect.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefadjsummaryredirect.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefAdjSummaryLinkType" or name == "cefAdjSummaryComplete" or name == "cefAdjSummaryFixup" or name == "cefAdjSummaryIncomplete" or name == "cefAdjSummaryRedirect"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefAdjSummaryLinkType"):
                    self.cefadjsummarylinktype = value
                    self.cefadjsummarylinktype.value_namespace = name_space
                    self.cefadjsummarylinktype.value_namespace_prefix = name_space_prefix
                if(value_path == "cefAdjSummaryComplete"):
                    self.cefadjsummarycomplete = value
                    self.cefadjsummarycomplete.value_namespace = name_space
                    self.cefadjsummarycomplete.value_namespace_prefix = name_space_prefix
                if(value_path == "cefAdjSummaryFixup"):
                    self.cefadjsummaryfixup = value
                    self.cefadjsummaryfixup.value_namespace = name_space
                    self.cefadjsummaryfixup.value_namespace_prefix = name_space_prefix
                if(value_path == "cefAdjSummaryIncomplete"):
                    self.cefadjsummaryincomplete = value
                    self.cefadjsummaryincomplete.value_namespace = name_space
                    self.cefadjsummaryincomplete.value_namespace_prefix = name_space_prefix
                if(value_path == "cefAdjSummaryRedirect"):
                    self.cefadjsummaryredirect = value
                    self.cefadjsummaryredirect.value_namespace = name_space
                    self.cefadjsummaryredirect.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefadjsummaryentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefadjsummaryentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefAdjSummaryTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefAdjSummaryEntry"):
                for c in self.cefadjsummaryentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCefMib.Cefadjsummarytable.Cefadjsummaryentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefadjsummaryentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefAdjSummaryEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefadjtable(Entity):
        """
        A list of CEF adjacencies.
        
        .. attribute:: cefadjentry
        
        	If CEF is enabled on the Managed device, each entry contains the adjacency  attributes. Adjacency entries may exist for all the interfaces on which packets can be switched out of the device. The interface is instantiated by ifIndex.   Therefore, the interface index must have been assigned, according to the applicable procedures, before it can be meaningfully used. Generally, this means that the interface must exist.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of    :py:class:`Cefadjentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefadjtable.Cefadjentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Cefadjtable, self).__init__()

            self.yang_name = "cefAdjTable"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.cefadjentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Cefadjtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Cefadjtable, self).__setattr__(name, value)


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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cefadjnexthopaddrtype  <key>
            
            	Address type for the cefAdjNextHopAddr. This object specifies the address type used for cefAdjNextHopAddr.   Adjacency entries are only valid for the  address type of ipv4(1) and ipv6(2)
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cefadjnexthopaddr  <key>
            
            	The next Hop address for this adjacency. The type of this address is determined by the value of the cefAdjNextHopAddrType object
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cefadjconnid  <key>
            
            	In cases where cefLinkType, interface and the next hop address are not able to uniquely define an adjacency entry (e.g. ATM and Frame Relay Bundles), this object is a unique identifier to differentiate between these adjacency entries.   In all the other cases the value of this  index object will be 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefadjsummarylinktype  <key>
            
            	
            	**type**\:   :py:class:`Cefadjlinktype <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefadjlinktype>`
            
            .. attribute:: cefadjbytes
            
            	Number of bytes transmitted using this adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cefadjencap
            
            	The layer 2 encapsulation string to be used for sending the packet out using this adjacency
            	**type**\:  str
            
            .. attribute:: cefadjfixup
            
            	For the cases, where the encapsulation string is decided at packet switch time, the adjacency  encapsulation string specified by object cefAdjEncap  require a fixup. I.e. for the adjacencies out of IP  Tunnels, the string prepended is an IP header which has  fields which can only be setup at packet switch time.  The value of this object represent the kind of fixup applied to the packet.  If the encapsulation string doesn't require any fixup, then the value of this object will be of zero length
            	**type**\:  str
            
            .. attribute:: cefadjforwardinginfo
            
            	This object selects a forwarding info entry  defined in the cefFESelectionTable. The  selected target is defined by an entry in the cefFESelectionTable whose index value (cefFESelectionName)  is equal to this object.  The value of this object will be of zero length if this adjacency entry is the last forwarding  element in the forwarding path
            	**type**\:  str
            
            .. attribute:: cefadjhcbytes
            
            	Number of bytes transmitted using this adjacency. This object is a 64\-bit version of cefAdjBytes
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cefadjhcpkts
            
            	Number of pkts transmitted using this adjacency. This object is a 64\-bit version of cefAdjPkts
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cefadjmtu
            
            	The Layer 3 MTU which can be transmitted using  this adjacency
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: bytes
            
            .. attribute:: cefadjpkts
            
            	Number of pkts transmitted using this adjacency
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cefadjsource
            
            	If the adjacency is created because some neighbour discovery mechanism has discovered a neighbour and all the information required to build a frame header to encapsulate traffic to the neighbour is available then the source of adjacency is set to the mechanism by which the adjacency is learned
            	**type**\:   :py:class:`Cefadjacencysource <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefadjacencysource>`
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CiscoCefMib.Cefadjtable.Cefadjentry, self).__init__()

                self.yang_name = "cefAdjEntry"
                self.yang_parent_name = "cefAdjTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cefadjnexthopaddrtype = YLeaf(YType.enumeration, "cefAdjNextHopAddrType")

                self.cefadjnexthopaddr = YLeaf(YType.str, "cefAdjNextHopAddr")

                self.cefadjconnid = YLeaf(YType.uint32, "cefAdjConnId")

                self.cefadjsummarylinktype = YLeaf(YType.enumeration, "cefAdjSummaryLinkType")

                self.cefadjbytes = YLeaf(YType.uint32, "cefAdjBytes")

                self.cefadjencap = YLeaf(YType.str, "cefAdjEncap")

                self.cefadjfixup = YLeaf(YType.str, "cefAdjFixup")

                self.cefadjforwardinginfo = YLeaf(YType.str, "cefAdjForwardingInfo")

                self.cefadjhcbytes = YLeaf(YType.uint64, "cefAdjHCBytes")

                self.cefadjhcpkts = YLeaf(YType.uint64, "cefAdjHCPkts")

                self.cefadjmtu = YLeaf(YType.uint32, "cefAdjMTU")

                self.cefadjpkts = YLeaf(YType.uint32, "cefAdjPkts")

                self.cefadjsource = YLeaf(YType.bits, "cefAdjSource")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "ifindex",
                                "cefadjnexthopaddrtype",
                                "cefadjnexthopaddr",
                                "cefadjconnid",
                                "cefadjsummarylinktype",
                                "cefadjbytes",
                                "cefadjencap",
                                "cefadjfixup",
                                "cefadjforwardinginfo",
                                "cefadjhcbytes",
                                "cefadjhcpkts",
                                "cefadjmtu",
                                "cefadjpkts",
                                "cefadjsource") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCefMib.Cefadjtable.Cefadjentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCefMib.Cefadjtable.Cefadjentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.ifindex.is_set or
                    self.cefadjnexthopaddrtype.is_set or
                    self.cefadjnexthopaddr.is_set or
                    self.cefadjconnid.is_set or
                    self.cefadjsummarylinktype.is_set or
                    self.cefadjbytes.is_set or
                    self.cefadjencap.is_set or
                    self.cefadjfixup.is_set or
                    self.cefadjforwardinginfo.is_set or
                    self.cefadjhcbytes.is_set or
                    self.cefadjhcpkts.is_set or
                    self.cefadjmtu.is_set or
                    self.cefadjpkts.is_set or
                    self.cefadjsource.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cefadjnexthopaddrtype.yfilter != YFilter.not_set or
                    self.cefadjnexthopaddr.yfilter != YFilter.not_set or
                    self.cefadjconnid.yfilter != YFilter.not_set or
                    self.cefadjsummarylinktype.yfilter != YFilter.not_set or
                    self.cefadjbytes.yfilter != YFilter.not_set or
                    self.cefadjencap.yfilter != YFilter.not_set or
                    self.cefadjfixup.yfilter != YFilter.not_set or
                    self.cefadjforwardinginfo.yfilter != YFilter.not_set or
                    self.cefadjhcbytes.yfilter != YFilter.not_set or
                    self.cefadjhcpkts.yfilter != YFilter.not_set or
                    self.cefadjmtu.yfilter != YFilter.not_set or
                    self.cefadjpkts.yfilter != YFilter.not_set or
                    self.cefadjsource.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefAdjEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[ifIndex='" + self.ifindex.get() + "']" + "[cefAdjNextHopAddrType='" + self.cefadjnexthopaddrtype.get() + "']" + "[cefAdjNextHopAddr='" + self.cefadjnexthopaddr.get() + "']" + "[cefAdjConnId='" + self.cefadjconnid.get() + "']" + "[cefAdjSummaryLinkType='" + self.cefadjsummarylinktype.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/cefAdjTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cefadjnexthopaddrtype.is_set or self.cefadjnexthopaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefadjnexthopaddrtype.get_name_leafdata())
                if (self.cefadjnexthopaddr.is_set or self.cefadjnexthopaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefadjnexthopaddr.get_name_leafdata())
                if (self.cefadjconnid.is_set or self.cefadjconnid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefadjconnid.get_name_leafdata())
                if (self.cefadjsummarylinktype.is_set or self.cefadjsummarylinktype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefadjsummarylinktype.get_name_leafdata())
                if (self.cefadjbytes.is_set or self.cefadjbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefadjbytes.get_name_leafdata())
                if (self.cefadjencap.is_set or self.cefadjencap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefadjencap.get_name_leafdata())
                if (self.cefadjfixup.is_set or self.cefadjfixup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefadjfixup.get_name_leafdata())
                if (self.cefadjforwardinginfo.is_set or self.cefadjforwardinginfo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefadjforwardinginfo.get_name_leafdata())
                if (self.cefadjhcbytes.is_set or self.cefadjhcbytes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefadjhcbytes.get_name_leafdata())
                if (self.cefadjhcpkts.is_set or self.cefadjhcpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefadjhcpkts.get_name_leafdata())
                if (self.cefadjmtu.is_set or self.cefadjmtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefadjmtu.get_name_leafdata())
                if (self.cefadjpkts.is_set or self.cefadjpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefadjpkts.get_name_leafdata())
                if (self.cefadjsource.is_set or self.cefadjsource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefadjsource.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "ifIndex" or name == "cefAdjNextHopAddrType" or name == "cefAdjNextHopAddr" or name == "cefAdjConnId" or name == "cefAdjSummaryLinkType" or name == "cefAdjBytes" or name == "cefAdjEncap" or name == "cefAdjFixup" or name == "cefAdjForwardingInfo" or name == "cefAdjHCBytes" or name == "cefAdjHCPkts" or name == "cefAdjMTU" or name == "cefAdjPkts" or name == "cefAdjSource"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefAdjNextHopAddrType"):
                    self.cefadjnexthopaddrtype = value
                    self.cefadjnexthopaddrtype.value_namespace = name_space
                    self.cefadjnexthopaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cefAdjNextHopAddr"):
                    self.cefadjnexthopaddr = value
                    self.cefadjnexthopaddr.value_namespace = name_space
                    self.cefadjnexthopaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cefAdjConnId"):
                    self.cefadjconnid = value
                    self.cefadjconnid.value_namespace = name_space
                    self.cefadjconnid.value_namespace_prefix = name_space_prefix
                if(value_path == "cefAdjSummaryLinkType"):
                    self.cefadjsummarylinktype = value
                    self.cefadjsummarylinktype.value_namespace = name_space
                    self.cefadjsummarylinktype.value_namespace_prefix = name_space_prefix
                if(value_path == "cefAdjBytes"):
                    self.cefadjbytes = value
                    self.cefadjbytes.value_namespace = name_space
                    self.cefadjbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cefAdjEncap"):
                    self.cefadjencap = value
                    self.cefadjencap.value_namespace = name_space
                    self.cefadjencap.value_namespace_prefix = name_space_prefix
                if(value_path == "cefAdjFixup"):
                    self.cefadjfixup = value
                    self.cefadjfixup.value_namespace = name_space
                    self.cefadjfixup.value_namespace_prefix = name_space_prefix
                if(value_path == "cefAdjForwardingInfo"):
                    self.cefadjforwardinginfo = value
                    self.cefadjforwardinginfo.value_namespace = name_space
                    self.cefadjforwardinginfo.value_namespace_prefix = name_space_prefix
                if(value_path == "cefAdjHCBytes"):
                    self.cefadjhcbytes = value
                    self.cefadjhcbytes.value_namespace = name_space
                    self.cefadjhcbytes.value_namespace_prefix = name_space_prefix
                if(value_path == "cefAdjHCPkts"):
                    self.cefadjhcpkts = value
                    self.cefadjhcpkts.value_namespace = name_space
                    self.cefadjhcpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cefAdjMTU"):
                    self.cefadjmtu = value
                    self.cefadjmtu.value_namespace = name_space
                    self.cefadjmtu.value_namespace_prefix = name_space_prefix
                if(value_path == "cefAdjPkts"):
                    self.cefadjpkts = value
                    self.cefadjpkts.value_namespace = name_space
                    self.cefadjpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cefAdjSource"):
                    self.cefadjsource[value] = True

        def has_data(self):
            for c in self.cefadjentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefadjentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefAdjTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefAdjEntry"):
                for c in self.cefadjentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCefMib.Cefadjtable.Cefadjentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefadjentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefAdjEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ceffeselectiontable(Entity):
        """
        A list of forwarding element selection entries.
        
        .. attribute:: ceffeselectionentry
        
        	If CEF is enabled on the Managed device, each entry contain a CEF forwarding element selection list.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of    :py:class:`Ceffeselectionentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Ceffeselectiontable.Ceffeselectionentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Ceffeselectiontable, self).__init__()

            self.yang_name = "cefFESelectionTable"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.ceffeselectionentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Ceffeselectiontable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Ceffeselectiontable, self).__setattr__(name, value)


        class Ceffeselectionentry(Entity):
            """
            If CEF is enabled on the Managed device,
            each entry contain a CEF forwarding element
            selection list.
            
            entPhysicalIndex is also an index for this
            table which represents entities of
            'module' entPhysicalClass which are capable
            of running CEF.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceffeselectionname  <key>
            
            	The locally arbitrary, but unique identifier used to select a set of forwarding element lists
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: ceffeselectionid  <key>
            
            	Secondary index to identify a forwarding elements List  in this Table
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ceffeselectionadjconnid
            
            	This object represent the connection id for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to zero if the forwarding element list doesn't  contain an adjacency forwarding element.   In cases where cefFESelectionAdjLinkType, interface  and the next hop address are not able to uniquely  define an adjacency entry (e.g. ATM and Frame Relay Bundles), this object is a unique identifier to differentiate between these adjacency entries
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceffeselectionadjinterface
            
            	This object represent the interface for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to zero if the forwarding element list doesn't  contain an adjacency forwarding element
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ceffeselectionadjlinktype
            
            	This object represent the link type for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to unknown(5) if the forwarding element list  doesn't contain an adjacency forwarding element
            	**type**\:   :py:class:`Cefadjlinktype <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefadjlinktype>`
            
            .. attribute:: ceffeselectionadjnexthopaddr
            
            	This object represent the next hop address for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to zero if the forwarding element list doesn't  contain an adjacency forwarding element
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ceffeselectionadjnexthopaddrtype
            
            	This object represent the next hop address type for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to unknown(0) if the forwarding element list  doesn't contain an adjacency forwarding element
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ceffeselectionlabels
            
            	This object represent the MPLS Labels  associated with this forwarding Element List.  The value of this object will be irrelevant and will be set to zero length if the forwarding element list  doesn't contain a label forwarding element. A zero  length label list will indicate that there is no label forwarding element associated with this selection entry
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ceffeselectionspecial
            
            	Special processing for a destination is indicated through the use of special  forwarding element.   If the forwarding element list contains the  special forwarding element, then this object  represents the type of special forwarding element
            	**type**\:   :py:class:`Cefforwardingelementspecialtype <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefforwardingelementspecialtype>`
            
            .. attribute:: ceffeselectionvrfname
            
            	This object represent the Vrf name for the lookup associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to a string containing the single octet 0x00 if the forwarding element list  doesn't contain a lookup forwarding element
            	**type**\:  str
            
            	**length:** 0..31
            
            .. attribute:: ceffeselectionweight
            
            	This object represent the weighting for  load balancing between multiple Forwarding Element Lists. The value of this object will be zero if load balancing is associated with this selection entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CiscoCefMib.Ceffeselectiontable.Ceffeselectionentry, self).__init__()

                self.yang_name = "cefFESelectionEntry"
                self.yang_parent_name = "cefFESelectionTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ceffeselectionname = YLeaf(YType.str, "cefFESelectionName")

                self.ceffeselectionid = YLeaf(YType.int32, "cefFESelectionId")

                self.ceffeselectionadjconnid = YLeaf(YType.uint32, "cefFESelectionAdjConnId")

                self.ceffeselectionadjinterface = YLeaf(YType.int32, "cefFESelectionAdjInterface")

                self.ceffeselectionadjlinktype = YLeaf(YType.enumeration, "cefFESelectionAdjLinkType")

                self.ceffeselectionadjnexthopaddr = YLeaf(YType.str, "cefFESelectionAdjNextHopAddr")

                self.ceffeselectionadjnexthopaddrtype = YLeaf(YType.enumeration, "cefFESelectionAdjNextHopAddrType")

                self.ceffeselectionlabels = YLeaf(YType.str, "cefFESelectionLabels")

                self.ceffeselectionspecial = YLeaf(YType.enumeration, "cefFESelectionSpecial")

                self.ceffeselectionvrfname = YLeaf(YType.str, "cefFESelectionVrfName")

                self.ceffeselectionweight = YLeaf(YType.uint32, "cefFESelectionWeight")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "ceffeselectionname",
                                "ceffeselectionid",
                                "ceffeselectionadjconnid",
                                "ceffeselectionadjinterface",
                                "ceffeselectionadjlinktype",
                                "ceffeselectionadjnexthopaddr",
                                "ceffeselectionadjnexthopaddrtype",
                                "ceffeselectionlabels",
                                "ceffeselectionspecial",
                                "ceffeselectionvrfname",
                                "ceffeselectionweight") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCefMib.Ceffeselectiontable.Ceffeselectionentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCefMib.Ceffeselectiontable.Ceffeselectionentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.ceffeselectionname.is_set or
                    self.ceffeselectionid.is_set or
                    self.ceffeselectionadjconnid.is_set or
                    self.ceffeselectionadjinterface.is_set or
                    self.ceffeselectionadjlinktype.is_set or
                    self.ceffeselectionadjnexthopaddr.is_set or
                    self.ceffeselectionadjnexthopaddrtype.is_set or
                    self.ceffeselectionlabels.is_set or
                    self.ceffeselectionspecial.is_set or
                    self.ceffeselectionvrfname.is_set or
                    self.ceffeselectionweight.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.ceffeselectionname.yfilter != YFilter.not_set or
                    self.ceffeselectionid.yfilter != YFilter.not_set or
                    self.ceffeselectionadjconnid.yfilter != YFilter.not_set or
                    self.ceffeselectionadjinterface.yfilter != YFilter.not_set or
                    self.ceffeselectionadjlinktype.yfilter != YFilter.not_set or
                    self.ceffeselectionadjnexthopaddr.yfilter != YFilter.not_set or
                    self.ceffeselectionadjnexthopaddrtype.yfilter != YFilter.not_set or
                    self.ceffeselectionlabels.yfilter != YFilter.not_set or
                    self.ceffeselectionspecial.yfilter != YFilter.not_set or
                    self.ceffeselectionvrfname.yfilter != YFilter.not_set or
                    self.ceffeselectionweight.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefFESelectionEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cefFESelectionName='" + self.ceffeselectionname.get() + "']" + "[cefFESelectionId='" + self.ceffeselectionid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/cefFESelectionTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.ceffeselectionname.is_set or self.ceffeselectionname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffeselectionname.get_name_leafdata())
                if (self.ceffeselectionid.is_set or self.ceffeselectionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffeselectionid.get_name_leafdata())
                if (self.ceffeselectionadjconnid.is_set or self.ceffeselectionadjconnid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffeselectionadjconnid.get_name_leafdata())
                if (self.ceffeselectionadjinterface.is_set or self.ceffeselectionadjinterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffeselectionadjinterface.get_name_leafdata())
                if (self.ceffeselectionadjlinktype.is_set or self.ceffeselectionadjlinktype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffeselectionadjlinktype.get_name_leafdata())
                if (self.ceffeselectionadjnexthopaddr.is_set or self.ceffeselectionadjnexthopaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffeselectionadjnexthopaddr.get_name_leafdata())
                if (self.ceffeselectionadjnexthopaddrtype.is_set or self.ceffeselectionadjnexthopaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffeselectionadjnexthopaddrtype.get_name_leafdata())
                if (self.ceffeselectionlabels.is_set or self.ceffeselectionlabels.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffeselectionlabels.get_name_leafdata())
                if (self.ceffeselectionspecial.is_set or self.ceffeselectionspecial.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffeselectionspecial.get_name_leafdata())
                if (self.ceffeselectionvrfname.is_set or self.ceffeselectionvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffeselectionvrfname.get_name_leafdata())
                if (self.ceffeselectionweight.is_set or self.ceffeselectionweight.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffeselectionweight.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefFESelectionName" or name == "cefFESelectionId" or name == "cefFESelectionAdjConnId" or name == "cefFESelectionAdjInterface" or name == "cefFESelectionAdjLinkType" or name == "cefFESelectionAdjNextHopAddr" or name == "cefFESelectionAdjNextHopAddrType" or name == "cefFESelectionLabels" or name == "cefFESelectionSpecial" or name == "cefFESelectionVrfName" or name == "cefFESelectionWeight"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefFESelectionName"):
                    self.ceffeselectionname = value
                    self.ceffeselectionname.value_namespace = name_space
                    self.ceffeselectionname.value_namespace_prefix = name_space_prefix
                if(value_path == "cefFESelectionId"):
                    self.ceffeselectionid = value
                    self.ceffeselectionid.value_namespace = name_space
                    self.ceffeselectionid.value_namespace_prefix = name_space_prefix
                if(value_path == "cefFESelectionAdjConnId"):
                    self.ceffeselectionadjconnid = value
                    self.ceffeselectionadjconnid.value_namespace = name_space
                    self.ceffeselectionadjconnid.value_namespace_prefix = name_space_prefix
                if(value_path == "cefFESelectionAdjInterface"):
                    self.ceffeselectionadjinterface = value
                    self.ceffeselectionadjinterface.value_namespace = name_space
                    self.ceffeselectionadjinterface.value_namespace_prefix = name_space_prefix
                if(value_path == "cefFESelectionAdjLinkType"):
                    self.ceffeselectionadjlinktype = value
                    self.ceffeselectionadjlinktype.value_namespace = name_space
                    self.ceffeselectionadjlinktype.value_namespace_prefix = name_space_prefix
                if(value_path == "cefFESelectionAdjNextHopAddr"):
                    self.ceffeselectionadjnexthopaddr = value
                    self.ceffeselectionadjnexthopaddr.value_namespace = name_space
                    self.ceffeselectionadjnexthopaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cefFESelectionAdjNextHopAddrType"):
                    self.ceffeselectionadjnexthopaddrtype = value
                    self.ceffeselectionadjnexthopaddrtype.value_namespace = name_space
                    self.ceffeselectionadjnexthopaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cefFESelectionLabels"):
                    self.ceffeselectionlabels = value
                    self.ceffeselectionlabels.value_namespace = name_space
                    self.ceffeselectionlabels.value_namespace_prefix = name_space_prefix
                if(value_path == "cefFESelectionSpecial"):
                    self.ceffeselectionspecial = value
                    self.ceffeselectionspecial.value_namespace = name_space
                    self.ceffeselectionspecial.value_namespace_prefix = name_space_prefix
                if(value_path == "cefFESelectionVrfName"):
                    self.ceffeselectionvrfname = value
                    self.ceffeselectionvrfname.value_namespace = name_space
                    self.ceffeselectionvrfname.value_namespace_prefix = name_space_prefix
                if(value_path == "cefFESelectionWeight"):
                    self.ceffeselectionweight = value
                    self.ceffeselectionweight.value_namespace = name_space
                    self.ceffeselectionweight.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ceffeselectionentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ceffeselectionentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefFESelectionTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefFESelectionEntry"):
                for c in self.ceffeselectionentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCefMib.Ceffeselectiontable.Ceffeselectionentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ceffeselectionentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefFESelectionEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefcfgtable(Entity):
        """
        This table contains global config parameter 
        of CEF on the Managed device.
        
        .. attribute:: cefcfgentry
        
        	If the Managed device supports CEF,  each entry contains the CEF config  parameter for the managed entity. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of    :py:class:`Cefcfgentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefcfgtable.Cefcfgentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Cefcfgtable, self).__init__()

            self.yang_name = "cefCfgTable"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.cefcfgentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Cefcfgtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Cefcfgtable, self).__setattr__(name, value)


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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceffibipversion  <key>
            
            	
            	**type**\:   :py:class:`Cefipversion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefipversion>`
            
            .. attribute:: cefcfgaccountingmap
            
            	This object represents a bitmap of network accounting options.  CEF network accounting is disabled by default.  CEF network accounting can be enabled  by selecting one or more of the following CEF accounting option for the value of this object.    nonRecursive(0)\:  enables accounting through                     nonrecursive prefixes.   perPrefix(1)\:     enables the collection of the numbers                     of pkts and bytes express forwarded                    to a destination (prefix)   prefixLength(2)\:  enables accounting through                     prefixlength.           Once the accounting is enabled, the corresponding stats  can be retrieved from the cefPrefixTable and  cefStatsPrefixLenTable.  
            	**type**\:   :py:class:`Cefcfgaccountingmap <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefcfgtable.Cefcfgentry.Cefcfgaccountingmap>`
            
            .. attribute:: cefcfgadminstate
            
            	The desired state of CEF
            	**type**\:   :py:class:`Cefadminstatus <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefadminstatus>`
            
            .. attribute:: cefcfgdistributionadminstate
            
            	The desired state of CEF distribution
            	**type**\:   :py:class:`Cefadminstatus <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefadminstatus>`
            
            .. attribute:: cefcfgdistributionoperstate
            
            	The current operational state of CEF distribution.  If the cefCfgDistributionAdminState is disabled(2), then cefDistributionOperState will eventually go to the down(2) state unless some error has occurred.    If cefCfgDistributionAdminState is changed to enabled(1)  then cefCfgDistributionOperState should change to up(1)  only if the CEF entity is ready to forward the packets  using Distributed Cisco Express Forwarding (dCEF) else  it should remain in the down(2) state. The up(1) state  for this object indicates that CEF entity is forwarding the packet using Distributed Cisco Express Forwarding
            	**type**\:   :py:class:`Cefoperstatus <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefoperstatus>`
            
            .. attribute:: cefcfgloadsharingalgorithm
            
            	Indicates the CEF Load balancing algorithm.  Setting this object to none(1) will disable the Load sharing for the specified entry.  CEF load balancing can be enabled by setting  this object to one of following Algorithms\:   original(2)  \: This algorithm is based on a                  source and destination hash    tunnel(3)    \: This algorithm is used in                  tunnels environments or in                 environments where there are                 only a few source                      universal(4)  \: This algorithm uses a source and                   destination and ID hash  If the value of this object is set to 'tunnel' or 'universal', then the FIXED ID for these algorithms may be specified by the managed  object cefLoadSharingID. 
            	**type**\:   :py:class:`Cefcfgloadsharingalgorithm <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefcfgtable.Cefcfgentry.Cefcfgloadsharingalgorithm>`
            
            .. attribute:: cefcfgloadsharingid
            
            	The Fixed ID associated with the managed object cefCfgLoadSharingAlgorithm. The hash of this object value may be used by the Load Sharing Algorithm.  The value of this object is not relevant and will be set to zero if the value of managed object  cefCfgLoadSharingAlgorithm is set to none(1) or original(2). The default value of this object is calculated by the device at the time of initialization
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcfgoperstate
            
            	The current operational state of CEF.  If the cefCfgAdminState is disabled(2), then cefOperState will eventually go to the down(2) state unless some error has occurred.   If cefCfgAdminState is changed to enabled(1) then  cefCfgOperState should change to up(1) only if the  CEF entity is ready to forward the packets using  Cisco Express Forwarding (CEF) else it should remain  in the down(2) state. The up(1) state for this object  indicates that CEF entity is forwarding the packet using Cisco Express Forwarding
            	**type**\:   :py:class:`Cefoperstatus <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefoperstatus>`
            
            .. attribute:: cefcfgtrafficstatsloadinterval
            
            	The interval time over which the CEF traffic statistics are collected
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cefcfgtrafficstatsupdaterate
            
            	The frequency with which the line card sends the traffic load statistics to the Router Processor.  Setting the value of this object to 0 will disable the CEF traffic statistics collection
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: seconds
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CiscoCefMib.Cefcfgtable.Cefcfgentry, self).__init__()

                self.yang_name = "cefCfgEntry"
                self.yang_parent_name = "cefCfgTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ceffibipversion = YLeaf(YType.enumeration, "cefFIBIpVersion")

                self.cefcfgaccountingmap = YLeaf(YType.bits, "cefCfgAccountingMap")

                self.cefcfgadminstate = YLeaf(YType.enumeration, "cefCfgAdminState")

                self.cefcfgdistributionadminstate = YLeaf(YType.enumeration, "cefCfgDistributionAdminState")

                self.cefcfgdistributionoperstate = YLeaf(YType.enumeration, "cefCfgDistributionOperState")

                self.cefcfgloadsharingalgorithm = YLeaf(YType.enumeration, "cefCfgLoadSharingAlgorithm")

                self.cefcfgloadsharingid = YLeaf(YType.uint32, "cefCfgLoadSharingID")

                self.cefcfgoperstate = YLeaf(YType.enumeration, "cefCfgOperState")

                self.cefcfgtrafficstatsloadinterval = YLeaf(YType.uint32, "cefCfgTrafficStatsLoadInterval")

                self.cefcfgtrafficstatsupdaterate = YLeaf(YType.uint32, "cefCfgTrafficStatsUpdateRate")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "ceffibipversion",
                                "cefcfgaccountingmap",
                                "cefcfgadminstate",
                                "cefcfgdistributionadminstate",
                                "cefcfgdistributionoperstate",
                                "cefcfgloadsharingalgorithm",
                                "cefcfgloadsharingid",
                                "cefcfgoperstate",
                                "cefcfgtrafficstatsloadinterval",
                                "cefcfgtrafficstatsupdaterate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCefMib.Cefcfgtable.Cefcfgentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCefMib.Cefcfgtable.Cefcfgentry, self).__setattr__(name, value)

            class Cefcfgloadsharingalgorithm(Enum):
                """
                Cefcfgloadsharingalgorithm

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


            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.ceffibipversion.is_set or
                    self.cefcfgaccountingmap.is_set or
                    self.cefcfgadminstate.is_set or
                    self.cefcfgdistributionadminstate.is_set or
                    self.cefcfgdistributionoperstate.is_set or
                    self.cefcfgloadsharingalgorithm.is_set or
                    self.cefcfgloadsharingid.is_set or
                    self.cefcfgoperstate.is_set or
                    self.cefcfgtrafficstatsloadinterval.is_set or
                    self.cefcfgtrafficstatsupdaterate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.ceffibipversion.yfilter != YFilter.not_set or
                    self.cefcfgaccountingmap.yfilter != YFilter.not_set or
                    self.cefcfgadminstate.yfilter != YFilter.not_set or
                    self.cefcfgdistributionadminstate.yfilter != YFilter.not_set or
                    self.cefcfgdistributionoperstate.yfilter != YFilter.not_set or
                    self.cefcfgloadsharingalgorithm.yfilter != YFilter.not_set or
                    self.cefcfgloadsharingid.yfilter != YFilter.not_set or
                    self.cefcfgoperstate.yfilter != YFilter.not_set or
                    self.cefcfgtrafficstatsloadinterval.yfilter != YFilter.not_set or
                    self.cefcfgtrafficstatsupdaterate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefCfgEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cefFIBIpVersion='" + self.ceffibipversion.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/cefCfgTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.ceffibipversion.is_set or self.ceffibipversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffibipversion.get_name_leafdata())
                if (self.cefcfgaccountingmap.is_set or self.cefcfgaccountingmap.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfgaccountingmap.get_name_leafdata())
                if (self.cefcfgadminstate.is_set or self.cefcfgadminstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfgadminstate.get_name_leafdata())
                if (self.cefcfgdistributionadminstate.is_set or self.cefcfgdistributionadminstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfgdistributionadminstate.get_name_leafdata())
                if (self.cefcfgdistributionoperstate.is_set or self.cefcfgdistributionoperstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfgdistributionoperstate.get_name_leafdata())
                if (self.cefcfgloadsharingalgorithm.is_set or self.cefcfgloadsharingalgorithm.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfgloadsharingalgorithm.get_name_leafdata())
                if (self.cefcfgloadsharingid.is_set or self.cefcfgloadsharingid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfgloadsharingid.get_name_leafdata())
                if (self.cefcfgoperstate.is_set or self.cefcfgoperstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfgoperstate.get_name_leafdata())
                if (self.cefcfgtrafficstatsloadinterval.is_set or self.cefcfgtrafficstatsloadinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfgtrafficstatsloadinterval.get_name_leafdata())
                if (self.cefcfgtrafficstatsupdaterate.is_set or self.cefcfgtrafficstatsupdaterate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcfgtrafficstatsupdaterate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefFIBIpVersion" or name == "cefCfgAccountingMap" or name == "cefCfgAdminState" or name == "cefCfgDistributionAdminState" or name == "cefCfgDistributionOperState" or name == "cefCfgLoadSharingAlgorithm" or name == "cefCfgLoadSharingID" or name == "cefCfgOperState" or name == "cefCfgTrafficStatsLoadInterval" or name == "cefCfgTrafficStatsUpdateRate"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefFIBIpVersion"):
                    self.ceffibipversion = value
                    self.ceffibipversion.value_namespace = name_space
                    self.ceffibipversion.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCfgAccountingMap"):
                    self.cefcfgaccountingmap[value] = True
                if(value_path == "cefCfgAdminState"):
                    self.cefcfgadminstate = value
                    self.cefcfgadminstate.value_namespace = name_space
                    self.cefcfgadminstate.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCfgDistributionAdminState"):
                    self.cefcfgdistributionadminstate = value
                    self.cefcfgdistributionadminstate.value_namespace = name_space
                    self.cefcfgdistributionadminstate.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCfgDistributionOperState"):
                    self.cefcfgdistributionoperstate = value
                    self.cefcfgdistributionoperstate.value_namespace = name_space
                    self.cefcfgdistributionoperstate.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCfgLoadSharingAlgorithm"):
                    self.cefcfgloadsharingalgorithm = value
                    self.cefcfgloadsharingalgorithm.value_namespace = name_space
                    self.cefcfgloadsharingalgorithm.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCfgLoadSharingID"):
                    self.cefcfgloadsharingid = value
                    self.cefcfgloadsharingid.value_namespace = name_space
                    self.cefcfgloadsharingid.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCfgOperState"):
                    self.cefcfgoperstate = value
                    self.cefcfgoperstate.value_namespace = name_space
                    self.cefcfgoperstate.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCfgTrafficStatsLoadInterval"):
                    self.cefcfgtrafficstatsloadinterval = value
                    self.cefcfgtrafficstatsloadinterval.value_namespace = name_space
                    self.cefcfgtrafficstatsloadinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCfgTrafficStatsUpdateRate"):
                    self.cefcfgtrafficstatsupdaterate = value
                    self.cefcfgtrafficstatsupdaterate.value_namespace = name_space
                    self.cefcfgtrafficstatsupdaterate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefcfgentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefcfgentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefCfgTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefCfgEntry"):
                for c in self.cefcfgentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCefMib.Cefcfgtable.Cefcfgentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefcfgentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefCfgEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefresourcetable(Entity):
        """
        This table contains global resource 
        information of CEF on the Managed device.
        
        .. attribute:: cefresourceentry
        
        	If the Managed device supports CEF, each entry contains the CEF Resource  parameters for the managed entity.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of    :py:class:`Cefresourceentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefresourcetable.Cefresourceentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Cefresourcetable, self).__init__()

            self.yang_name = "cefResourceTable"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.cefresourceentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Cefresourcetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Cefresourcetable, self).__setattr__(name, value)


        class Cefresourceentry(Entity):
            """
            If the Managed device supports CEF,
            each entry contains the CEF Resource 
            parameters for the managed entity.
            
            entPhysicalIndex is also an index for this
            table which represents entities of
            'module' entPhysicalClass which are capable
            of running CEF.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cefresourcefailurereason
            
            	The CEF resource failure reason which may lead to CEF being disabled on the managed entity
            	**type**\:   :py:class:`Ceffailurereason <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Ceffailurereason>`
            
            .. attribute:: cefresourcememoryused
            
            	Indicates the number of bytes from the Processor Memory Pool that are currently in use by CEF on the managed entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CiscoCefMib.Cefresourcetable.Cefresourceentry, self).__init__()

                self.yang_name = "cefResourceEntry"
                self.yang_parent_name = "cefResourceTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cefresourcefailurereason = YLeaf(YType.enumeration, "cefResourceFailureReason")

                self.cefresourcememoryused = YLeaf(YType.uint32, "cefResourceMemoryUsed")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cefresourcefailurereason",
                                "cefresourcememoryused") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCefMib.Cefresourcetable.Cefresourceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCefMib.Cefresourcetable.Cefresourceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cefresourcefailurereason.is_set or
                    self.cefresourcememoryused.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cefresourcefailurereason.yfilter != YFilter.not_set or
                    self.cefresourcememoryused.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefResourceEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/cefResourceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cefresourcefailurereason.is_set or self.cefresourcefailurereason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefresourcefailurereason.get_name_leafdata())
                if (self.cefresourcememoryused.is_set or self.cefresourcememoryused.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefresourcememoryused.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefResourceFailureReason" or name == "cefResourceMemoryUsed"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefResourceFailureReason"):
                    self.cefresourcefailurereason = value
                    self.cefresourcefailurereason.value_namespace = name_space
                    self.cefresourcefailurereason.value_namespace_prefix = name_space_prefix
                if(value_path == "cefResourceMemoryUsed"):
                    self.cefresourcememoryused = value
                    self.cefresourcememoryused.value_namespace = name_space
                    self.cefresourcememoryused.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefresourceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefresourceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefResourceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefResourceEntry"):
                for c in self.cefresourceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCefMib.Cefresourcetable.Cefresourceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefresourceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefResourceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefinttable(Entity):
        """
        This Table contains interface specific
        information of CEF on the Managed
        device.
        
        .. attribute:: cefintentry
        
        	If CEF is enabled on the Managed device,  each entry contains the CEF attributes  associated with an interface. The interface is instantiated by ifIndex.   Therefore, the interface index must have been assigned, according to the applicable procedures, before it can be meaningfully used. Generally, this means that the interface must exist.  A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of    :py:class:`Cefintentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefinttable.Cefintentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Cefinttable, self).__init__()

            self.yang_name = "cefIntTable"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.cefintentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Cefinttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Cefinttable, self).__setattr__(name, value)


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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceffibipversion  <key>
            
            	
            	**type**\:   :py:class:`Cefipversion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefipversion>`
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: cefintloadsharing
            
            	The status of load sharing on the interface.  perPacket(1) \: Router to send data packets                over successive equal\-cost paths                without regard to individual hosts                or user sessions.  perDestination(2) \: Router to use multiple, equal\-cost                     paths to achieve load sharing  Load sharing is enabled by default  for an interface when CEF is enabled
            	**type**\:   :py:class:`Cefintloadsharing <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefinttable.Cefintentry.Cefintloadsharing>`
            
            .. attribute:: cefintnonrecursiveaccouting
            
            	The CEF accounting mode for the interface. CEF prefix based non\-recursive accounting  on an interface can be configured to store  the stats for non\-recursive prefixes in a internal  or external bucket.  internal(1)  \:  Count input traffic in the nonrecursive                 internal bucket  external(2)  \:  Count input traffic in the nonrecursive                 external bucket  The value of this object will only be effective if  value of the object cefAccountingMap is set to enable nonRecursive(1) accounting
            	**type**\:   :py:class:`Cefintnonrecursiveaccouting <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefinttable.Cefintentry.Cefintnonrecursiveaccouting>`
            
            .. attribute:: cefintswitchingstate
            
            	The CEF switching State for the interface.  If CEF is enabled but distributed CEF(dCEF) is disabled then CEF is in cefEnabled(1) state.  If distributed CEF is enabled, then CEF is in  distCefEnabled(2) state. The cefDisabled(3) state indicates that CEF is disabled.  The CEF switching state is only applicable to the received packet on the interface
            	**type**\:   :py:class:`Cefintswitchingstate <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefinttable.Cefintentry.Cefintswitchingstate>`
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CiscoCefMib.Cefinttable.Cefintentry, self).__init__()

                self.yang_name = "cefIntEntry"
                self.yang_parent_name = "cefIntTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ceffibipversion = YLeaf(YType.enumeration, "cefFIBIpVersion")

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.cefintloadsharing = YLeaf(YType.enumeration, "cefIntLoadSharing")

                self.cefintnonrecursiveaccouting = YLeaf(YType.enumeration, "cefIntNonrecursiveAccouting")

                self.cefintswitchingstate = YLeaf(YType.enumeration, "cefIntSwitchingState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "ceffibipversion",
                                "ifindex",
                                "cefintloadsharing",
                                "cefintnonrecursiveaccouting",
                                "cefintswitchingstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCefMib.Cefinttable.Cefintentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCefMib.Cefinttable.Cefintentry, self).__setattr__(name, value)

            class Cefintloadsharing(Enum):
                """
                Cefintloadsharing

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
                Cefintnonrecursiveaccouting

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
                Cefintswitchingstate

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


            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.ceffibipversion.is_set or
                    self.ifindex.is_set or
                    self.cefintloadsharing.is_set or
                    self.cefintnonrecursiveaccouting.is_set or
                    self.cefintswitchingstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.ceffibipversion.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.cefintloadsharing.yfilter != YFilter.not_set or
                    self.cefintnonrecursiveaccouting.yfilter != YFilter.not_set or
                    self.cefintswitchingstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefIntEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cefFIBIpVersion='" + self.ceffibipversion.get() + "']" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/cefIntTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.ceffibipversion.is_set or self.ceffibipversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffibipversion.get_name_leafdata())
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.cefintloadsharing.is_set or self.cefintloadsharing.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefintloadsharing.get_name_leafdata())
                if (self.cefintnonrecursiveaccouting.is_set or self.cefintnonrecursiveaccouting.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefintnonrecursiveaccouting.get_name_leafdata())
                if (self.cefintswitchingstate.is_set or self.cefintswitchingstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefintswitchingstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefFIBIpVersion" or name == "ifIndex" or name == "cefIntLoadSharing" or name == "cefIntNonrecursiveAccouting" or name == "cefIntSwitchingState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefFIBIpVersion"):
                    self.ceffibipversion = value
                    self.ceffibipversion.value_namespace = name_space
                    self.ceffibipversion.value_namespace_prefix = name_space_prefix
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefIntLoadSharing"):
                    self.cefintloadsharing = value
                    self.cefintloadsharing.value_namespace = name_space
                    self.cefintloadsharing.value_namespace_prefix = name_space_prefix
                if(value_path == "cefIntNonrecursiveAccouting"):
                    self.cefintnonrecursiveaccouting = value
                    self.cefintnonrecursiveaccouting.value_namespace = name_space
                    self.cefintnonrecursiveaccouting.value_namespace_prefix = name_space_prefix
                if(value_path == "cefIntSwitchingState"):
                    self.cefintswitchingstate = value
                    self.cefintswitchingstate.value_namespace = name_space
                    self.cefintswitchingstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefintentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefintentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefIntTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefIntEntry"):
                for c in self.cefintentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCefMib.Cefinttable.Cefintentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefintentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefIntEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefpeertable(Entity):
        """
        Entity acting as RP (Routing Processor) keeps
        the CEF states for the line card entities and
        communicates with the line card entities using
        XDR. This Table contains the CEF information 
        related to peer entities on the managed device.
        
        .. attribute:: cefpeerentry
        
        	If CEF is enabled on the Managed device, each entry contains the CEF related attributes  associated with a CEF peer entity.  entPhysicalIndex and entPeerPhysicalIndex are also indexes for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of    :py:class:`Cefpeerentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefpeertable.Cefpeerentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Cefpeertable, self).__init__()

            self.yang_name = "cefPeerTable"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.cefpeerentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Cefpeertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Cefpeertable, self).__setattr__(name, value)


        class Cefpeerentry(Entity):
            """
            If CEF is enabled on the Managed device,
            each entry contains the CEF related attributes 
            associated with a CEF peer entity.
            
            entPhysicalIndex and entPeerPhysicalIndex are
            also indexes for this table which represents
            entities of 'module' entPhysicalClass which are
            capable of running CEF.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: entpeerphysicalindex  <key>
            
            	The entity index for the CEF peer entity. Only the entities of 'module'  entPhysicalClass are included here
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefpeernumberofresets
            
            	Number of times the session with CEF peer entity  has been reset
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefpeeroperstate
            
            	The current CEF operational state of the CEF peer entity.  Cef peer entity oper state will be peerDisabled(1) in  the following condition\:     \: Cef Peer entity encounters fatal error i.e. resource      allocation failure, ipc failure etc     \: When a reload/delete request is received from the Cef       Peer Entity  Once the peer entity is up and no fatal error is encountered, then the value of this object will transits to the peerUp(3)  state.  If the Cef Peer entity is in held stage, then the value of this object will be peerHold(3). Cef peer entity can only transit to peerDisabled(1) state from the peerHold(3) state
            	**type**\:   :py:class:`Cefpeeroperstate <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefpeertable.Cefpeerentry.Cefpeeroperstate>`
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CiscoCefMib.Cefpeertable.Cefpeerentry, self).__init__()

                self.yang_name = "cefPeerEntry"
                self.yang_parent_name = "cefPeerTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.entpeerphysicalindex = YLeaf(YType.int32, "entPeerPhysicalIndex")

                self.cefpeernumberofresets = YLeaf(YType.uint32, "cefPeerNumberOfResets")

                self.cefpeeroperstate = YLeaf(YType.enumeration, "cefPeerOperState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "entpeerphysicalindex",
                                "cefpeernumberofresets",
                                "cefpeeroperstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCefMib.Cefpeertable.Cefpeerentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCefMib.Cefpeertable.Cefpeerentry, self).__setattr__(name, value)

            class Cefpeeroperstate(Enum):
                """
                Cefpeeroperstate

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


            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.entpeerphysicalindex.is_set or
                    self.cefpeernumberofresets.is_set or
                    self.cefpeeroperstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.entpeerphysicalindex.yfilter != YFilter.not_set or
                    self.cefpeernumberofresets.yfilter != YFilter.not_set or
                    self.cefpeeroperstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefPeerEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[entPeerPhysicalIndex='" + self.entpeerphysicalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/cefPeerTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.entpeerphysicalindex.is_set or self.entpeerphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entpeerphysicalindex.get_name_leafdata())
                if (self.cefpeernumberofresets.is_set or self.cefpeernumberofresets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefpeernumberofresets.get_name_leafdata())
                if (self.cefpeeroperstate.is_set or self.cefpeeroperstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefpeeroperstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "entPeerPhysicalIndex" or name == "cefPeerNumberOfResets" or name == "cefPeerOperState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "entPeerPhysicalIndex"):
                    self.entpeerphysicalindex = value
                    self.entpeerphysicalindex.value_namespace = name_space
                    self.entpeerphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPeerNumberOfResets"):
                    self.cefpeernumberofresets = value
                    self.cefpeernumberofresets.value_namespace = name_space
                    self.cefpeernumberofresets.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPeerOperState"):
                    self.cefpeeroperstate = value
                    self.cefpeeroperstate.value_namespace = name_space
                    self.cefpeeroperstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefpeerentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefpeerentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefPeerTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefPeerEntry"):
                for c in self.cefpeerentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCefMib.Cefpeertable.Cefpeerentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefpeerentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefPeerEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefpeerfibtable(Entity):
        """
        Entity acting as RP (Routing Processor) keep
        the CEF FIB states for the line card entities and
        communicate with the line card entities using
        XDR. This Table contains the CEF FIB State 
        related to peer entities on the managed device.
        
        .. attribute:: cefpeerfibentry
        
        	If CEF is enabled on the Managed device, each entry contains the CEF FIB State  associated a CEF peer entity.  entPhysicalIndex and entPeerPhysicalIndex are also indexes for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of    :py:class:`Cefpeerfibentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefpeerfibtable.Cefpeerfibentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Cefpeerfibtable, self).__init__()

            self.yang_name = "cefPeerFIBTable"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.cefpeerfibentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Cefpeerfibtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Cefpeerfibtable, self).__setattr__(name, value)


        class Cefpeerfibentry(Entity):
            """
            If CEF is enabled on the Managed device,
            each entry contains the CEF FIB State 
            associated a CEF peer entity.
            
            entPhysicalIndex and entPeerPhysicalIndex are
            also indexes for this table which represents
            entities of 'module' entPhysicalClass which are
            capable of running CEF.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: entpeerphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entpeerphysicalindex <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefpeertable.Cefpeerentry>`
            
            .. attribute:: ceffibipversion  <key>
            
            	
            	**type**\:   :py:class:`Cefipversion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefipversion>`
            
            .. attribute:: cefpeerfiboperstate
            
            	The current CEF FIB Operational State for the  CEF peer entity
            	**type**\:   :py:class:`Cefpeerfiboperstate <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefpeerfibtable.Cefpeerfibentry.Cefpeerfiboperstate>`
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CiscoCefMib.Cefpeerfibtable.Cefpeerfibentry, self).__init__()

                self.yang_name = "cefPeerFIBEntry"
                self.yang_parent_name = "cefPeerFIBTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.entpeerphysicalindex = YLeaf(YType.str, "entPeerPhysicalIndex")

                self.ceffibipversion = YLeaf(YType.enumeration, "cefFIBIpVersion")

                self.cefpeerfiboperstate = YLeaf(YType.enumeration, "cefPeerFIBOperState")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "entpeerphysicalindex",
                                "ceffibipversion",
                                "cefpeerfiboperstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCefMib.Cefpeerfibtable.Cefpeerfibentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCefMib.Cefpeerfibtable.Cefpeerfibentry, self).__setattr__(name, value)

            class Cefpeerfiboperstate(Enum):
                """
                Cefpeerfiboperstate

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


            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.entpeerphysicalindex.is_set or
                    self.ceffibipversion.is_set or
                    self.cefpeerfiboperstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.entpeerphysicalindex.yfilter != YFilter.not_set or
                    self.ceffibipversion.yfilter != YFilter.not_set or
                    self.cefpeerfiboperstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefPeerFIBEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[entPeerPhysicalIndex='" + self.entpeerphysicalindex.get() + "']" + "[cefFIBIpVersion='" + self.ceffibipversion.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/cefPeerFIBTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.entpeerphysicalindex.is_set or self.entpeerphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entpeerphysicalindex.get_name_leafdata())
                if (self.ceffibipversion.is_set or self.ceffibipversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffibipversion.get_name_leafdata())
                if (self.cefpeerfiboperstate.is_set or self.cefpeerfiboperstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefpeerfiboperstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "entPeerPhysicalIndex" or name == "cefFIBIpVersion" or name == "cefPeerFIBOperState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "entPeerPhysicalIndex"):
                    self.entpeerphysicalindex = value
                    self.entpeerphysicalindex.value_namespace = name_space
                    self.entpeerphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefFIBIpVersion"):
                    self.ceffibipversion = value
                    self.ceffibipversion.value_namespace = name_space
                    self.ceffibipversion.value_namespace_prefix = name_space_prefix
                if(value_path == "cefPeerFIBOperState"):
                    self.cefpeerfiboperstate = value
                    self.cefpeerfiboperstate.value_namespace = name_space
                    self.cefpeerfiboperstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefpeerfibentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefpeerfibentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefPeerFIBTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefPeerFIBEntry"):
                for c in self.cefpeerfibentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCefMib.Cefpeerfibtable.Cefpeerfibentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefpeerfibentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefPeerFIBEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefccglobaltable(Entity):
        """
        This table contains CEF consistency checker
        (CC) global parameters for the managed device.
        
        .. attribute:: cefccglobalentry
        
        	If the managed device supports CEF, each entry contains the global consistency  checker parameter for the managed device. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device
        	**type**\: list of    :py:class:`Cefccglobalentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefccglobaltable.Cefccglobalentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Cefccglobaltable, self).__init__()

            self.yang_name = "cefCCGlobalTable"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.cefccglobalentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Cefccglobaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Cefccglobaltable, self).__setattr__(name, value)


        class Cefccglobalentry(Entity):
            """
            If the managed device supports CEF,
            each entry contains the global consistency 
            checker parameter for the managed device.
            A row may exist for each IP version type
            (v4 and v6) depending upon the IP version
            supported on the device.
            
            .. attribute:: ceffibipversion  <key>
            
            	
            	**type**\:   :py:class:`Cefipversion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefipversion>`
            
            .. attribute:: cefccglobalautorepairdelay
            
            	Indiactes how long the consistency checker  waits to fix an inconsistency.  The value of this object has no effect when the value of object cefCCGlobalAutoRepairEnabled is 'false'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cefccglobalautorepairenabled
            
            	Once an inconsistency has been detected,  CEF has the ability to repair the problem.  This object indicates the status of auto\-repair  function for the consistency checkers
            	**type**\:  bool
            
            .. attribute:: cefccglobalautorepairholddown
            
            	Indicates how long the consistency checker waits to re\-enable auto\-repair after  auto\-repair runs.  The value of this object has no effect when the value of object cefCCGlobalAutoRepairEnabled is 'false'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cefccglobalerrormsgenabled
            
            	Enables the consistency checker to generate  an error message when it detects an inconsistency
            	**type**\:  bool
            
            .. attribute:: cefccglobalfullscanaction
            
            	Setting the value of this object to ccActionStart(1) will start the full scan consistency checkers.  The Management station should poll the  cefCCGlobalFullScanStatus object to get the  state of full\-scan operation.  Once the full\-scan operation completes (value of cefCCGlobalFullScanStatus object is ccStatusDone(3)),  the Management station should retrieve the values of the related stats object from the cefCCTypeTable.  Setting the value of this object to ccActionAbort(2) will  abort the full\-scan operation.  The value of this object can't be set to ccActionStart(1),  if the value of object cefCCGlobalFullScanStatus is ccStatusRunning(2).  The value of this object will be set to cefActionNone(1) when the full scan consistency checkers have never been activated.  A Management Station cannot set the value of this object to cefActionNone(1)
            	**type**\:   :py:class:`Cefccaction <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefccaction>`
            
            .. attribute:: cefccglobalfullscanstatus
            
            	Indicates the status of the full scan consistency checker request
            	**type**\:   :py:class:`Cefccstatus <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefccstatus>`
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CiscoCefMib.Cefccglobaltable.Cefccglobalentry, self).__init__()

                self.yang_name = "cefCCGlobalEntry"
                self.yang_parent_name = "cefCCGlobalTable"

                self.ceffibipversion = YLeaf(YType.enumeration, "cefFIBIpVersion")

                self.cefccglobalautorepairdelay = YLeaf(YType.uint32, "cefCCGlobalAutoRepairDelay")

                self.cefccglobalautorepairenabled = YLeaf(YType.boolean, "cefCCGlobalAutoRepairEnabled")

                self.cefccglobalautorepairholddown = YLeaf(YType.uint32, "cefCCGlobalAutoRepairHoldDown")

                self.cefccglobalerrormsgenabled = YLeaf(YType.boolean, "cefCCGlobalErrorMsgEnabled")

                self.cefccglobalfullscanaction = YLeaf(YType.enumeration, "cefCCGlobalFullScanAction")

                self.cefccglobalfullscanstatus = YLeaf(YType.enumeration, "cefCCGlobalFullScanStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ceffibipversion",
                                "cefccglobalautorepairdelay",
                                "cefccglobalautorepairenabled",
                                "cefccglobalautorepairholddown",
                                "cefccglobalerrormsgenabled",
                                "cefccglobalfullscanaction",
                                "cefccglobalfullscanstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCefMib.Cefccglobaltable.Cefccglobalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCefMib.Cefccglobaltable.Cefccglobalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ceffibipversion.is_set or
                    self.cefccglobalautorepairdelay.is_set or
                    self.cefccglobalautorepairenabled.is_set or
                    self.cefccglobalautorepairholddown.is_set or
                    self.cefccglobalerrormsgenabled.is_set or
                    self.cefccglobalfullscanaction.is_set or
                    self.cefccglobalfullscanstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ceffibipversion.yfilter != YFilter.not_set or
                    self.cefccglobalautorepairdelay.yfilter != YFilter.not_set or
                    self.cefccglobalautorepairenabled.yfilter != YFilter.not_set or
                    self.cefccglobalautorepairholddown.yfilter != YFilter.not_set or
                    self.cefccglobalerrormsgenabled.yfilter != YFilter.not_set or
                    self.cefccglobalfullscanaction.yfilter != YFilter.not_set or
                    self.cefccglobalfullscanstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefCCGlobalEntry" + "[cefFIBIpVersion='" + self.ceffibipversion.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/cefCCGlobalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ceffibipversion.is_set or self.ceffibipversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffibipversion.get_name_leafdata())
                if (self.cefccglobalautorepairdelay.is_set or self.cefccglobalautorepairdelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefccglobalautorepairdelay.get_name_leafdata())
                if (self.cefccglobalautorepairenabled.is_set or self.cefccglobalautorepairenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefccglobalautorepairenabled.get_name_leafdata())
                if (self.cefccglobalautorepairholddown.is_set or self.cefccglobalautorepairholddown.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefccglobalautorepairholddown.get_name_leafdata())
                if (self.cefccglobalerrormsgenabled.is_set or self.cefccglobalerrormsgenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefccglobalerrormsgenabled.get_name_leafdata())
                if (self.cefccglobalfullscanaction.is_set or self.cefccglobalfullscanaction.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefccglobalfullscanaction.get_name_leafdata())
                if (self.cefccglobalfullscanstatus.is_set or self.cefccglobalfullscanstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefccglobalfullscanstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cefFIBIpVersion" or name == "cefCCGlobalAutoRepairDelay" or name == "cefCCGlobalAutoRepairEnabled" or name == "cefCCGlobalAutoRepairHoldDown" or name == "cefCCGlobalErrorMsgEnabled" or name == "cefCCGlobalFullScanAction" or name == "cefCCGlobalFullScanStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cefFIBIpVersion"):
                    self.ceffibipversion = value
                    self.ceffibipversion.value_namespace = name_space
                    self.ceffibipversion.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCCGlobalAutoRepairDelay"):
                    self.cefccglobalautorepairdelay = value
                    self.cefccglobalautorepairdelay.value_namespace = name_space
                    self.cefccglobalautorepairdelay.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCCGlobalAutoRepairEnabled"):
                    self.cefccglobalautorepairenabled = value
                    self.cefccglobalautorepairenabled.value_namespace = name_space
                    self.cefccglobalautorepairenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCCGlobalAutoRepairHoldDown"):
                    self.cefccglobalautorepairholddown = value
                    self.cefccglobalautorepairholddown.value_namespace = name_space
                    self.cefccglobalautorepairholddown.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCCGlobalErrorMsgEnabled"):
                    self.cefccglobalerrormsgenabled = value
                    self.cefccglobalerrormsgenabled.value_namespace = name_space
                    self.cefccglobalerrormsgenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCCGlobalFullScanAction"):
                    self.cefccglobalfullscanaction = value
                    self.cefccglobalfullscanaction.value_namespace = name_space
                    self.cefccglobalfullscanaction.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCCGlobalFullScanStatus"):
                    self.cefccglobalfullscanstatus = value
                    self.cefccglobalfullscanstatus.value_namespace = name_space
                    self.cefccglobalfullscanstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefccglobalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefccglobalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefCCGlobalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefCCGlobalEntry"):
                for c in self.cefccglobalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCefMib.Cefccglobaltable.Cefccglobalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefccglobalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefCCGlobalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefcctypetable(Entity):
        """
        This table contains CEF consistency
        checker types specific parameters on the managed device.
        
        All detected inconsistency are signaled to the
        Management Station via cefInconsistencyDetection
        notification.
        
        .. attribute:: cefcctypeentry
        
        	If the managed device supports CEF, each entry contains the consistency  checker statistics for a consistency  checker type. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device
        	**type**\: list of    :py:class:`Cefcctypeentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefcctypetable.Cefcctypeentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Cefcctypetable, self).__init__()

            self.yang_name = "cefCCTypeTable"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.cefcctypeentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Cefcctypetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Cefcctypetable, self).__setattr__(name, value)


        class Cefcctypeentry(Entity):
            """
            If the managed device supports CEF,
            each entry contains the consistency 
            checker statistics for a consistency 
            checker type.
            A row may exist for each IP version type
            (v4 and v6) depending upon the IP version
            supported on the device.
            
            .. attribute:: ceffibipversion  <key>
            
            	
            	**type**\:   :py:class:`Cefipversion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefipversion>`
            
            .. attribute:: cefcctype  <key>
            
            	Type of the consistency checker
            	**type**\:   :py:class:`Cefcctype <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefcctype>`
            
            .. attribute:: cefcccount
            
            	The maximum number of prefixes to check per scan.  The default value for this object  depends upon the consistency checker type.  The value of this object will be irrelevant  for some of the consistency checkers and will be set to 0.  A Management Station cannot set the value of this object to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefccenabled
            
            	Enables the passive consistency checker. Passive consistency checkers are disabled by default.  Full\-scan consistency checkers are always enabled. An attempt to set this object to 'false' for an active consistency checker will result in 'wrongValue' error
            	**type**\:  bool
            
            .. attribute:: cefccperiod
            
            	The period between scans for the consistency checker
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cefccquerieschecked
            
            	Number of prefix consistency queries processed by this  consistency checker
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefccqueriesignored
            
            	Number of prefix consistency queries for which the consistency checks were not performed by this  consistency checker. This may be because of some internal error or resource failure
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefccqueriesiterated
            
            	Number of prefix consistency queries iterated back to the master database by this consistency checker
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefccqueriessent
            
            	Number of prefix consistency queries sent to CEF forwarding databases by this consistency checker
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CiscoCefMib.Cefcctypetable.Cefcctypeentry, self).__init__()

                self.yang_name = "cefCCTypeEntry"
                self.yang_parent_name = "cefCCTypeTable"

                self.ceffibipversion = YLeaf(YType.enumeration, "cefFIBIpVersion")

                self.cefcctype = YLeaf(YType.enumeration, "cefCCType")

                self.cefcccount = YLeaf(YType.uint32, "cefCCCount")

                self.cefccenabled = YLeaf(YType.boolean, "cefCCEnabled")

                self.cefccperiod = YLeaf(YType.uint32, "cefCCPeriod")

                self.cefccquerieschecked = YLeaf(YType.uint32, "cefCCQueriesChecked")

                self.cefccqueriesignored = YLeaf(YType.uint32, "cefCCQueriesIgnored")

                self.cefccqueriesiterated = YLeaf(YType.uint32, "cefCCQueriesIterated")

                self.cefccqueriessent = YLeaf(YType.uint32, "cefCCQueriesSent")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ceffibipversion",
                                "cefcctype",
                                "cefcccount",
                                "cefccenabled",
                                "cefccperiod",
                                "cefccquerieschecked",
                                "cefccqueriesignored",
                                "cefccqueriesiterated",
                                "cefccqueriessent") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCefMib.Cefcctypetable.Cefcctypeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCefMib.Cefcctypetable.Cefcctypeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ceffibipversion.is_set or
                    self.cefcctype.is_set or
                    self.cefcccount.is_set or
                    self.cefccenabled.is_set or
                    self.cefccperiod.is_set or
                    self.cefccquerieschecked.is_set or
                    self.cefccqueriesignored.is_set or
                    self.cefccqueriesiterated.is_set or
                    self.cefccqueriessent.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ceffibipversion.yfilter != YFilter.not_set or
                    self.cefcctype.yfilter != YFilter.not_set or
                    self.cefcccount.yfilter != YFilter.not_set or
                    self.cefccenabled.yfilter != YFilter.not_set or
                    self.cefccperiod.yfilter != YFilter.not_set or
                    self.cefccquerieschecked.yfilter != YFilter.not_set or
                    self.cefccqueriesignored.yfilter != YFilter.not_set or
                    self.cefccqueriesiterated.yfilter != YFilter.not_set or
                    self.cefccqueriessent.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefCCTypeEntry" + "[cefFIBIpVersion='" + self.ceffibipversion.get() + "']" + "[cefCCType='" + self.cefcctype.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/cefCCTypeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ceffibipversion.is_set or self.ceffibipversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffibipversion.get_name_leafdata())
                if (self.cefcctype.is_set or self.cefcctype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcctype.get_name_leafdata())
                if (self.cefcccount.is_set or self.cefcccount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefcccount.get_name_leafdata())
                if (self.cefccenabled.is_set or self.cefccenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefccenabled.get_name_leafdata())
                if (self.cefccperiod.is_set or self.cefccperiod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefccperiod.get_name_leafdata())
                if (self.cefccquerieschecked.is_set or self.cefccquerieschecked.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefccquerieschecked.get_name_leafdata())
                if (self.cefccqueriesignored.is_set or self.cefccqueriesignored.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefccqueriesignored.get_name_leafdata())
                if (self.cefccqueriesiterated.is_set or self.cefccqueriesiterated.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefccqueriesiterated.get_name_leafdata())
                if (self.cefccqueriessent.is_set or self.cefccqueriessent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefccqueriessent.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cefFIBIpVersion" or name == "cefCCType" or name == "cefCCCount" or name == "cefCCEnabled" or name == "cefCCPeriod" or name == "cefCCQueriesChecked" or name == "cefCCQueriesIgnored" or name == "cefCCQueriesIterated" or name == "cefCCQueriesSent"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cefFIBIpVersion"):
                    self.ceffibipversion = value
                    self.ceffibipversion.value_namespace = name_space
                    self.ceffibipversion.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCCType"):
                    self.cefcctype = value
                    self.cefcctype.value_namespace = name_space
                    self.cefcctype.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCCCount"):
                    self.cefcccount = value
                    self.cefcccount.value_namespace = name_space
                    self.cefcccount.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCCEnabled"):
                    self.cefccenabled = value
                    self.cefccenabled.value_namespace = name_space
                    self.cefccenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCCPeriod"):
                    self.cefccperiod = value
                    self.cefccperiod.value_namespace = name_space
                    self.cefccperiod.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCCQueriesChecked"):
                    self.cefccquerieschecked = value
                    self.cefccquerieschecked.value_namespace = name_space
                    self.cefccquerieschecked.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCCQueriesIgnored"):
                    self.cefccqueriesignored = value
                    self.cefccqueriesignored.value_namespace = name_space
                    self.cefccqueriesignored.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCCQueriesIterated"):
                    self.cefccqueriesiterated = value
                    self.cefccqueriesiterated.value_namespace = name_space
                    self.cefccqueriesiterated.value_namespace_prefix = name_space_prefix
                if(value_path == "cefCCQueriesSent"):
                    self.cefccqueriessent = value
                    self.cefccqueriessent.value_namespace = name_space
                    self.cefccqueriessent.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefcctypeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefcctypeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefCCTypeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefCCTypeEntry"):
                for c in self.cefcctypeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCefMib.Cefcctypetable.Cefcctypeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefcctypeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefCCTypeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefinconsistencyrecordtable(Entity):
        """
        This table contains CEF inconsistency
        records.
        
        .. attribute:: cefinconsistencyrecordentry
        
        	If the managed device supports CEF, each entry contains the inconsistency  record
        	**type**\: list of    :py:class:`Cefinconsistencyrecordentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefinconsistencyrecordtable.Cefinconsistencyrecordentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Cefinconsistencyrecordtable, self).__init__()

            self.yang_name = "cefInconsistencyRecordTable"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.cefinconsistencyrecordentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Cefinconsistencyrecordtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Cefinconsistencyrecordtable, self).__setattr__(name, value)


        class Cefinconsistencyrecordentry(Entity):
            """
            If the managed device supports CEF,
            each entry contains the inconsistency 
            record.
            
            .. attribute:: ceffibipversion  <key>
            
            	
            	**type**\:   :py:class:`Cefipversion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefipversion>`
            
            .. attribute:: cefinconsistencyrecid  <key>
            
            	The locally arbitrary, but unique identifier associated with this inconsistency record entry
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefinconsistencycctype
            
            	The type of consistency checker who generated this inconsistency record
            	**type**\:   :py:class:`Cefcctype <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefcctype>`
            
            .. attribute:: cefinconsistencyentity
            
            	The entity for which this inconsistency record was  generated. The value of this object will be  irrelevant and will be set to 0 when the inconsisency  record is applicable for all the entities
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cefinconsistencyprefixaddr
            
            	The network prefix address associated with this  inconsistency record.  The type of this address is determined by the value of the cefInconsistencyPrefixType object
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: cefinconsistencyprefixlen
            
            	Length in bits of the inconsistency address prefix
            	**type**\:  int
            
            	**range:** 0..2040
            
            .. attribute:: cefinconsistencyprefixtype
            
            	The network prefix type associated with this inconsistency record
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: cefinconsistencyreason
            
            	The reason for generating this inconsistency record.   missing(1)\:        the prefix is missing  checksumErr(2)\:    checksum error was found  unknown(3)\:        reason is unknown
            	**type**\:   :py:class:`Cefinconsistencyreason <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefinconsistencyrecordtable.Cefinconsistencyrecordentry.Cefinconsistencyreason>`
            
            .. attribute:: cefinconsistencyvrfname
            
            	Vrf name associated with this inconsistency record
            	**type**\:  str
            
            	**length:** 0..31
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CiscoCefMib.Cefinconsistencyrecordtable.Cefinconsistencyrecordentry, self).__init__()

                self.yang_name = "cefInconsistencyRecordEntry"
                self.yang_parent_name = "cefInconsistencyRecordTable"

                self.ceffibipversion = YLeaf(YType.enumeration, "cefFIBIpVersion")

                self.cefinconsistencyrecid = YLeaf(YType.int32, "cefInconsistencyRecId")

                self.cefinconsistencycctype = YLeaf(YType.enumeration, "cefInconsistencyCCType")

                self.cefinconsistencyentity = YLeaf(YType.int32, "cefInconsistencyEntity")

                self.cefinconsistencyprefixaddr = YLeaf(YType.str, "cefInconsistencyPrefixAddr")

                self.cefinconsistencyprefixlen = YLeaf(YType.uint32, "cefInconsistencyPrefixLen")

                self.cefinconsistencyprefixtype = YLeaf(YType.enumeration, "cefInconsistencyPrefixType")

                self.cefinconsistencyreason = YLeaf(YType.enumeration, "cefInconsistencyReason")

                self.cefinconsistencyvrfname = YLeaf(YType.str, "cefInconsistencyVrfName")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ceffibipversion",
                                "cefinconsistencyrecid",
                                "cefinconsistencycctype",
                                "cefinconsistencyentity",
                                "cefinconsistencyprefixaddr",
                                "cefinconsistencyprefixlen",
                                "cefinconsistencyprefixtype",
                                "cefinconsistencyreason",
                                "cefinconsistencyvrfname") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCefMib.Cefinconsistencyrecordtable.Cefinconsistencyrecordentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCefMib.Cefinconsistencyrecordtable.Cefinconsistencyrecordentry, self).__setattr__(name, value)

            class Cefinconsistencyreason(Enum):
                """
                Cefinconsistencyreason

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


            def has_data(self):
                return (
                    self.ceffibipversion.is_set or
                    self.cefinconsistencyrecid.is_set or
                    self.cefinconsistencycctype.is_set or
                    self.cefinconsistencyentity.is_set or
                    self.cefinconsistencyprefixaddr.is_set or
                    self.cefinconsistencyprefixlen.is_set or
                    self.cefinconsistencyprefixtype.is_set or
                    self.cefinconsistencyreason.is_set or
                    self.cefinconsistencyvrfname.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ceffibipversion.yfilter != YFilter.not_set or
                    self.cefinconsistencyrecid.yfilter != YFilter.not_set or
                    self.cefinconsistencycctype.yfilter != YFilter.not_set or
                    self.cefinconsistencyentity.yfilter != YFilter.not_set or
                    self.cefinconsistencyprefixaddr.yfilter != YFilter.not_set or
                    self.cefinconsistencyprefixlen.yfilter != YFilter.not_set or
                    self.cefinconsistencyprefixtype.yfilter != YFilter.not_set or
                    self.cefinconsistencyreason.yfilter != YFilter.not_set or
                    self.cefinconsistencyvrfname.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefInconsistencyRecordEntry" + "[cefFIBIpVersion='" + self.ceffibipversion.get() + "']" + "[cefInconsistencyRecId='" + self.cefinconsistencyrecid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/cefInconsistencyRecordTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ceffibipversion.is_set or self.ceffibipversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffibipversion.get_name_leafdata())
                if (self.cefinconsistencyrecid.is_set or self.cefinconsistencyrecid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefinconsistencyrecid.get_name_leafdata())
                if (self.cefinconsistencycctype.is_set or self.cefinconsistencycctype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefinconsistencycctype.get_name_leafdata())
                if (self.cefinconsistencyentity.is_set or self.cefinconsistencyentity.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefinconsistencyentity.get_name_leafdata())
                if (self.cefinconsistencyprefixaddr.is_set or self.cefinconsistencyprefixaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefinconsistencyprefixaddr.get_name_leafdata())
                if (self.cefinconsistencyprefixlen.is_set or self.cefinconsistencyprefixlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefinconsistencyprefixlen.get_name_leafdata())
                if (self.cefinconsistencyprefixtype.is_set or self.cefinconsistencyprefixtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefinconsistencyprefixtype.get_name_leafdata())
                if (self.cefinconsistencyreason.is_set or self.cefinconsistencyreason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefinconsistencyreason.get_name_leafdata())
                if (self.cefinconsistencyvrfname.is_set or self.cefinconsistencyvrfname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefinconsistencyvrfname.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cefFIBIpVersion" or name == "cefInconsistencyRecId" or name == "cefInconsistencyCCType" or name == "cefInconsistencyEntity" or name == "cefInconsistencyPrefixAddr" or name == "cefInconsistencyPrefixLen" or name == "cefInconsistencyPrefixType" or name == "cefInconsistencyReason" or name == "cefInconsistencyVrfName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cefFIBIpVersion"):
                    self.ceffibipversion = value
                    self.ceffibipversion.value_namespace = name_space
                    self.ceffibipversion.value_namespace_prefix = name_space_prefix
                if(value_path == "cefInconsistencyRecId"):
                    self.cefinconsistencyrecid = value
                    self.cefinconsistencyrecid.value_namespace = name_space
                    self.cefinconsistencyrecid.value_namespace_prefix = name_space_prefix
                if(value_path == "cefInconsistencyCCType"):
                    self.cefinconsistencycctype = value
                    self.cefinconsistencycctype.value_namespace = name_space
                    self.cefinconsistencycctype.value_namespace_prefix = name_space_prefix
                if(value_path == "cefInconsistencyEntity"):
                    self.cefinconsistencyentity = value
                    self.cefinconsistencyentity.value_namespace = name_space
                    self.cefinconsistencyentity.value_namespace_prefix = name_space_prefix
                if(value_path == "cefInconsistencyPrefixAddr"):
                    self.cefinconsistencyprefixaddr = value
                    self.cefinconsistencyprefixaddr.value_namespace = name_space
                    self.cefinconsistencyprefixaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cefInconsistencyPrefixLen"):
                    self.cefinconsistencyprefixlen = value
                    self.cefinconsistencyprefixlen.value_namespace = name_space
                    self.cefinconsistencyprefixlen.value_namespace_prefix = name_space_prefix
                if(value_path == "cefInconsistencyPrefixType"):
                    self.cefinconsistencyprefixtype = value
                    self.cefinconsistencyprefixtype.value_namespace = name_space
                    self.cefinconsistencyprefixtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cefInconsistencyReason"):
                    self.cefinconsistencyreason = value
                    self.cefinconsistencyreason.value_namespace = name_space
                    self.cefinconsistencyreason.value_namespace_prefix = name_space_prefix
                if(value_path == "cefInconsistencyVrfName"):
                    self.cefinconsistencyvrfname = value
                    self.cefinconsistencyvrfname.value_namespace = name_space
                    self.cefinconsistencyvrfname.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefinconsistencyrecordentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefinconsistencyrecordentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefInconsistencyRecordTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefInconsistencyRecordEntry"):
                for c in self.cefinconsistencyrecordentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCefMib.Cefinconsistencyrecordtable.Cefinconsistencyrecordentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefinconsistencyrecordentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefInconsistencyRecordEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefstatsprefixlentable(Entity):
        """
        This table specifies the CEF stats based
        on the Prefix Length.
        
        .. attribute:: cefstatsprefixlenentry
        
        	If CEF is enabled on the Managed device and if CEF accounting is set to enable  prefix length based accounting (value of  cefCfgAccountingMap object in the  cefCfgEntry is set to enable 'prefixLength'  accounting), each entry contains the traffic  statistics for a prefix length. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of    :py:class:`Cefstatsprefixlenentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefstatsprefixlentable.Cefstatsprefixlenentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Cefstatsprefixlentable, self).__init__()

            self.yang_name = "cefStatsPrefixLenTable"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.cefstatsprefixlenentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Cefstatsprefixlentable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Cefstatsprefixlentable, self).__setattr__(name, value)


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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceffibipversion  <key>
            
            	
            	**type**\:   :py:class:`Cefipversion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefipversion>`
            
            .. attribute:: cefstatsprefixlen  <key>
            
            	Length in bits of the Destination IP prefix. As 0.0.0.0/0 is a valid prefix, hence  0 is a valid prefix length
            	**type**\:  int
            
            	**range:** 0..2040
            
            .. attribute:: cefstatsprefixdeletes
            
            	Number of delete operations performed to the FIB  database for the specified IP prefix length
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefstatsprefixelements
            
            	Total number of elements in the FIB database for the specified IP prefix length
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefstatsprefixhcdeletes
            
            	Number of delete operations performed to the FIB  database for the specified IP prefix length. This object is a 64\-bit version of  cefStatsPrefixDelete
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefstatsprefixhcelements
            
            	Total number of elements in the FIB database for the specified IP prefix length. This object is a 64\-bit version of  cefStatsPrefixElements
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefstatsprefixhcinserts
            
            	Number of insert operations performed to the FIB  database for the specified IP prefix length. This object is a 64\-bit version of  cefStatsPrefixInsert
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefstatsprefixhcqueries
            
            	Number of queries received in the FIB database for the specified IP prefix length. This object is a 64\-bit version of  cefStatsPrefixQueries
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefstatsprefixinserts
            
            	Number of insert operations performed to the FIB  database for the specified IP prefix length
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefstatsprefixqueries
            
            	Number of queries received in the FIB database  for the specified IP prefix length
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CiscoCefMib.Cefstatsprefixlentable.Cefstatsprefixlenentry, self).__init__()

                self.yang_name = "cefStatsPrefixLenEntry"
                self.yang_parent_name = "cefStatsPrefixLenTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ceffibipversion = YLeaf(YType.enumeration, "cefFIBIpVersion")

                self.cefstatsprefixlen = YLeaf(YType.uint32, "cefStatsPrefixLen")

                self.cefstatsprefixdeletes = YLeaf(YType.uint32, "cefStatsPrefixDeletes")

                self.cefstatsprefixelements = YLeaf(YType.uint32, "cefStatsPrefixElements")

                self.cefstatsprefixhcdeletes = YLeaf(YType.uint64, "cefStatsPrefixHCDeletes")

                self.cefstatsprefixhcelements = YLeaf(YType.uint64, "cefStatsPrefixHCElements")

                self.cefstatsprefixhcinserts = YLeaf(YType.uint64, "cefStatsPrefixHCInserts")

                self.cefstatsprefixhcqueries = YLeaf(YType.uint64, "cefStatsPrefixHCQueries")

                self.cefstatsprefixinserts = YLeaf(YType.uint32, "cefStatsPrefixInserts")

                self.cefstatsprefixqueries = YLeaf(YType.uint32, "cefStatsPrefixQueries")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "ceffibipversion",
                                "cefstatsprefixlen",
                                "cefstatsprefixdeletes",
                                "cefstatsprefixelements",
                                "cefstatsprefixhcdeletes",
                                "cefstatsprefixhcelements",
                                "cefstatsprefixhcinserts",
                                "cefstatsprefixhcqueries",
                                "cefstatsprefixinserts",
                                "cefstatsprefixqueries") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCefMib.Cefstatsprefixlentable.Cefstatsprefixlenentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCefMib.Cefstatsprefixlentable.Cefstatsprefixlenentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.ceffibipversion.is_set or
                    self.cefstatsprefixlen.is_set or
                    self.cefstatsprefixdeletes.is_set or
                    self.cefstatsprefixelements.is_set or
                    self.cefstatsprefixhcdeletes.is_set or
                    self.cefstatsprefixhcelements.is_set or
                    self.cefstatsprefixhcinserts.is_set or
                    self.cefstatsprefixhcqueries.is_set or
                    self.cefstatsprefixinserts.is_set or
                    self.cefstatsprefixqueries.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.ceffibipversion.yfilter != YFilter.not_set or
                    self.cefstatsprefixlen.yfilter != YFilter.not_set or
                    self.cefstatsprefixdeletes.yfilter != YFilter.not_set or
                    self.cefstatsprefixelements.yfilter != YFilter.not_set or
                    self.cefstatsprefixhcdeletes.yfilter != YFilter.not_set or
                    self.cefstatsprefixhcelements.yfilter != YFilter.not_set or
                    self.cefstatsprefixhcinserts.yfilter != YFilter.not_set or
                    self.cefstatsprefixhcqueries.yfilter != YFilter.not_set or
                    self.cefstatsprefixinserts.yfilter != YFilter.not_set or
                    self.cefstatsprefixqueries.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefStatsPrefixLenEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cefFIBIpVersion='" + self.ceffibipversion.get() + "']" + "[cefStatsPrefixLen='" + self.cefstatsprefixlen.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/cefStatsPrefixLenTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.ceffibipversion.is_set or self.ceffibipversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffibipversion.get_name_leafdata())
                if (self.cefstatsprefixlen.is_set or self.cefstatsprefixlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefstatsprefixlen.get_name_leafdata())
                if (self.cefstatsprefixdeletes.is_set or self.cefstatsprefixdeletes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefstatsprefixdeletes.get_name_leafdata())
                if (self.cefstatsprefixelements.is_set or self.cefstatsprefixelements.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefstatsprefixelements.get_name_leafdata())
                if (self.cefstatsprefixhcdeletes.is_set or self.cefstatsprefixhcdeletes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefstatsprefixhcdeletes.get_name_leafdata())
                if (self.cefstatsprefixhcelements.is_set or self.cefstatsprefixhcelements.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefstatsprefixhcelements.get_name_leafdata())
                if (self.cefstatsprefixhcinserts.is_set or self.cefstatsprefixhcinserts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefstatsprefixhcinserts.get_name_leafdata())
                if (self.cefstatsprefixhcqueries.is_set or self.cefstatsprefixhcqueries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefstatsprefixhcqueries.get_name_leafdata())
                if (self.cefstatsprefixinserts.is_set or self.cefstatsprefixinserts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefstatsprefixinserts.get_name_leafdata())
                if (self.cefstatsprefixqueries.is_set or self.cefstatsprefixqueries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefstatsprefixqueries.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefFIBIpVersion" or name == "cefStatsPrefixLen" or name == "cefStatsPrefixDeletes" or name == "cefStatsPrefixElements" or name == "cefStatsPrefixHCDeletes" or name == "cefStatsPrefixHCElements" or name == "cefStatsPrefixHCInserts" or name == "cefStatsPrefixHCQueries" or name == "cefStatsPrefixInserts" or name == "cefStatsPrefixQueries"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefFIBIpVersion"):
                    self.ceffibipversion = value
                    self.ceffibipversion.value_namespace = name_space
                    self.ceffibipversion.value_namespace_prefix = name_space_prefix
                if(value_path == "cefStatsPrefixLen"):
                    self.cefstatsprefixlen = value
                    self.cefstatsprefixlen.value_namespace = name_space
                    self.cefstatsprefixlen.value_namespace_prefix = name_space_prefix
                if(value_path == "cefStatsPrefixDeletes"):
                    self.cefstatsprefixdeletes = value
                    self.cefstatsprefixdeletes.value_namespace = name_space
                    self.cefstatsprefixdeletes.value_namespace_prefix = name_space_prefix
                if(value_path == "cefStatsPrefixElements"):
                    self.cefstatsprefixelements = value
                    self.cefstatsprefixelements.value_namespace = name_space
                    self.cefstatsprefixelements.value_namespace_prefix = name_space_prefix
                if(value_path == "cefStatsPrefixHCDeletes"):
                    self.cefstatsprefixhcdeletes = value
                    self.cefstatsprefixhcdeletes.value_namespace = name_space
                    self.cefstatsprefixhcdeletes.value_namespace_prefix = name_space_prefix
                if(value_path == "cefStatsPrefixHCElements"):
                    self.cefstatsprefixhcelements = value
                    self.cefstatsprefixhcelements.value_namespace = name_space
                    self.cefstatsprefixhcelements.value_namespace_prefix = name_space_prefix
                if(value_path == "cefStatsPrefixHCInserts"):
                    self.cefstatsprefixhcinserts = value
                    self.cefstatsprefixhcinserts.value_namespace = name_space
                    self.cefstatsprefixhcinserts.value_namespace_prefix = name_space_prefix
                if(value_path == "cefStatsPrefixHCQueries"):
                    self.cefstatsprefixhcqueries = value
                    self.cefstatsprefixhcqueries.value_namespace = name_space
                    self.cefstatsprefixhcqueries.value_namespace_prefix = name_space_prefix
                if(value_path == "cefStatsPrefixInserts"):
                    self.cefstatsprefixinserts = value
                    self.cefstatsprefixinserts.value_namespace = name_space
                    self.cefstatsprefixinserts.value_namespace_prefix = name_space_prefix
                if(value_path == "cefStatsPrefixQueries"):
                    self.cefstatsprefixqueries = value
                    self.cefstatsprefixqueries.value_namespace = name_space
                    self.cefstatsprefixqueries.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefstatsprefixlenentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefstatsprefixlenentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefStatsPrefixLenTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefStatsPrefixLenEntry"):
                for c in self.cefstatsprefixlenentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCefMib.Cefstatsprefixlentable.Cefstatsprefixlenentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefstatsprefixlenentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefStatsPrefixLenEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cefswitchingstatstable(Entity):
        """
        This table specifies the CEF switch stats.
        
        .. attribute:: cefswitchingstatsentry
        
        	If CEF is enabled on the Managed device, each entry specifies the switching stats. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of    :py:class:`Cefswitchingstatsentry <ydk.models.cisco_ios_xe.CISCO_CEF_MIB.CiscoCefMib.Cefswitchingstatstable.Cefswitchingstatsentry>`
        
        

        """

        _prefix = 'CISCO-CEF-MIB'
        _revision = '2006-01-30'

        def __init__(self):
            super(CiscoCefMib.Cefswitchingstatstable, self).__init__()

            self.yang_name = "cefSwitchingStatsTable"
            self.yang_parent_name = "CISCO-CEF-MIB"

            self.cefswitchingstatsentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoCefMib.Cefswitchingstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoCefMib.Cefswitchingstatstable, self).__setattr__(name, value)


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
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: ceffibipversion  <key>
            
            	
            	**type**\:   :py:class:`Cefipversion <ydk.models.cisco_ios_xe.CISCO_CEF_TC.Cefipversion>`
            
            .. attribute:: cefswitchingindex  <key>
            
            	The locally arbitrary, but unique identifier associated with this switching stats entry
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefswitchingdrop
            
            	Number of packets dropped by CEF
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cefswitchinghcdrop
            
            	Number of packets dropped by CEF. This object is a 64\-bit version of cefSwitchingDrop
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cefswitchinghcpunt
            
            	Number of packets that could not be switched in the normal path and were punted to the next\-fastest switching vector. This object is a 64\-bit version of cefSwitchingPunt
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cefswitchinghcpunt2host
            
            	Number of packets that could not be switched in the normal path and were punted to the host (process switching path).  For most of the switching paths, the value of this object may be similar to cefSwitchingPunt. This object is a 64\-bit version of cefSwitchingPunt2Host
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: packets
            
            .. attribute:: cefswitchingpath
            
            	Switch path where the feature was executed. Available switch paths are platform\-dependent. Following are the examples of switching paths\:     RIB \: switching with CEF assistance     Low\-end switching (LES) \: CEF switch path     PAS \: CEF turbo switch path
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: cefswitchingpunt
            
            	Number of packets that could not be switched in the normal path and were punted to the next\-fastest switching vector
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            .. attribute:: cefswitchingpunt2host
            
            	Number of packets that could not be switched in the normal path and were punted to the host (process switching path).  For most of the switching paths, the value of this object may be similar to cefSwitchingPunt
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: packets
            
            

            """

            _prefix = 'CISCO-CEF-MIB'
            _revision = '2006-01-30'

            def __init__(self):
                super(CiscoCefMib.Cefswitchingstatstable.Cefswitchingstatsentry, self).__init__()

                self.yang_name = "cefSwitchingStatsEntry"
                self.yang_parent_name = "cefSwitchingStatsTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.ceffibipversion = YLeaf(YType.enumeration, "cefFIBIpVersion")

                self.cefswitchingindex = YLeaf(YType.int32, "cefSwitchingIndex")

                self.cefswitchingdrop = YLeaf(YType.uint32, "cefSwitchingDrop")

                self.cefswitchinghcdrop = YLeaf(YType.uint64, "cefSwitchingHCDrop")

                self.cefswitchinghcpunt = YLeaf(YType.uint64, "cefSwitchingHCPunt")

                self.cefswitchinghcpunt2host = YLeaf(YType.uint64, "cefSwitchingHCPunt2Host")

                self.cefswitchingpath = YLeaf(YType.str, "cefSwitchingPath")

                self.cefswitchingpunt = YLeaf(YType.uint32, "cefSwitchingPunt")

                self.cefswitchingpunt2host = YLeaf(YType.uint32, "cefSwitchingPunt2Host")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "ceffibipversion",
                                "cefswitchingindex",
                                "cefswitchingdrop",
                                "cefswitchinghcdrop",
                                "cefswitchinghcpunt",
                                "cefswitchinghcpunt2host",
                                "cefswitchingpath",
                                "cefswitchingpunt",
                                "cefswitchingpunt2host") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoCefMib.Cefswitchingstatstable.Cefswitchingstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoCefMib.Cefswitchingstatstable.Cefswitchingstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.ceffibipversion.is_set or
                    self.cefswitchingindex.is_set or
                    self.cefswitchingdrop.is_set or
                    self.cefswitchinghcdrop.is_set or
                    self.cefswitchinghcpunt.is_set or
                    self.cefswitchinghcpunt2host.is_set or
                    self.cefswitchingpath.is_set or
                    self.cefswitchingpunt.is_set or
                    self.cefswitchingpunt2host.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.ceffibipversion.yfilter != YFilter.not_set or
                    self.cefswitchingindex.yfilter != YFilter.not_set or
                    self.cefswitchingdrop.yfilter != YFilter.not_set or
                    self.cefswitchinghcdrop.yfilter != YFilter.not_set or
                    self.cefswitchinghcpunt.yfilter != YFilter.not_set or
                    self.cefswitchinghcpunt2host.yfilter != YFilter.not_set or
                    self.cefswitchingpath.yfilter != YFilter.not_set or
                    self.cefswitchingpunt.yfilter != YFilter.not_set or
                    self.cefswitchingpunt2host.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cefSwitchingStatsEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cefFIBIpVersion='" + self.ceffibipversion.get() + "']" + "[cefSwitchingIndex='" + self.cefswitchingindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/cefSwitchingStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.ceffibipversion.is_set or self.ceffibipversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceffibipversion.get_name_leafdata())
                if (self.cefswitchingindex.is_set or self.cefswitchingindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefswitchingindex.get_name_leafdata())
                if (self.cefswitchingdrop.is_set or self.cefswitchingdrop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefswitchingdrop.get_name_leafdata())
                if (self.cefswitchinghcdrop.is_set or self.cefswitchinghcdrop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefswitchinghcdrop.get_name_leafdata())
                if (self.cefswitchinghcpunt.is_set or self.cefswitchinghcpunt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefswitchinghcpunt.get_name_leafdata())
                if (self.cefswitchinghcpunt2host.is_set or self.cefswitchinghcpunt2host.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefswitchinghcpunt2host.get_name_leafdata())
                if (self.cefswitchingpath.is_set or self.cefswitchingpath.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefswitchingpath.get_name_leafdata())
                if (self.cefswitchingpunt.is_set or self.cefswitchingpunt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefswitchingpunt.get_name_leafdata())
                if (self.cefswitchingpunt2host.is_set or self.cefswitchingpunt2host.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cefswitchingpunt2host.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cefFIBIpVersion" or name == "cefSwitchingIndex" or name == "cefSwitchingDrop" or name == "cefSwitchingHCDrop" or name == "cefSwitchingHCPunt" or name == "cefSwitchingHCPunt2Host" or name == "cefSwitchingPath" or name == "cefSwitchingPunt" or name == "cefSwitchingPunt2Host"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefFIBIpVersion"):
                    self.ceffibipversion = value
                    self.ceffibipversion.value_namespace = name_space
                    self.ceffibipversion.value_namespace_prefix = name_space_prefix
                if(value_path == "cefSwitchingIndex"):
                    self.cefswitchingindex = value
                    self.cefswitchingindex.value_namespace = name_space
                    self.cefswitchingindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cefSwitchingDrop"):
                    self.cefswitchingdrop = value
                    self.cefswitchingdrop.value_namespace = name_space
                    self.cefswitchingdrop.value_namespace_prefix = name_space_prefix
                if(value_path == "cefSwitchingHCDrop"):
                    self.cefswitchinghcdrop = value
                    self.cefswitchinghcdrop.value_namespace = name_space
                    self.cefswitchinghcdrop.value_namespace_prefix = name_space_prefix
                if(value_path == "cefSwitchingHCPunt"):
                    self.cefswitchinghcpunt = value
                    self.cefswitchinghcpunt.value_namespace = name_space
                    self.cefswitchinghcpunt.value_namespace_prefix = name_space_prefix
                if(value_path == "cefSwitchingHCPunt2Host"):
                    self.cefswitchinghcpunt2host = value
                    self.cefswitchinghcpunt2host.value_namespace = name_space
                    self.cefswitchinghcpunt2host.value_namespace_prefix = name_space_prefix
                if(value_path == "cefSwitchingPath"):
                    self.cefswitchingpath = value
                    self.cefswitchingpath.value_namespace = name_space
                    self.cefswitchingpath.value_namespace_prefix = name_space_prefix
                if(value_path == "cefSwitchingPunt"):
                    self.cefswitchingpunt = value
                    self.cefswitchingpunt.value_namespace = name_space
                    self.cefswitchingpunt.value_namespace_prefix = name_space_prefix
                if(value_path == "cefSwitchingPunt2Host"):
                    self.cefswitchingpunt2host = value
                    self.cefswitchingpunt2host.value_namespace = name_space
                    self.cefswitchingpunt2host.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cefswitchingstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cefswitchingstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cefSwitchingStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cefSwitchingStatsEntry"):
                for c in self.cefswitchingstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoCefMib.Cefswitchingstatstable.Cefswitchingstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cefswitchingstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cefSwitchingStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cefadjsummarytable is not None and self.cefadjsummarytable.has_data()) or
            (self.cefadjtable is not None and self.cefadjtable.has_data()) or
            (self.cefcc is not None and self.cefcc.has_data()) or
            (self.cefccglobaltable is not None and self.cefccglobaltable.has_data()) or
            (self.cefcctypetable is not None and self.cefcctypetable.has_data()) or
            (self.cefcfgtable is not None and self.cefcfgtable.has_data()) or
            (self.ceffeselectiontable is not None and self.ceffeselectiontable.has_data()) or
            (self.ceffib is not None and self.ceffib.has_data()) or
            (self.ceffibsummarytable is not None and self.ceffibsummarytable.has_data()) or
            (self.cefinconsistencyrecordtable is not None and self.cefinconsistencyrecordtable.has_data()) or
            (self.cefinttable is not None and self.cefinttable.has_data()) or
            (self.ceflmprefixtable is not None and self.ceflmprefixtable.has_data()) or
            (self.cefnotifcntl is not None and self.cefnotifcntl.has_data()) or
            (self.cefpathtable is not None and self.cefpathtable.has_data()) or
            (self.cefpeerfibtable is not None and self.cefpeerfibtable.has_data()) or
            (self.cefpeertable is not None and self.cefpeertable.has_data()) or
            (self.cefprefixtable is not None and self.cefprefixtable.has_data()) or
            (self.cefresourcetable is not None and self.cefresourcetable.has_data()) or
            (self.cefstatsprefixlentable is not None and self.cefstatsprefixlentable.has_data()) or
            (self.cefswitchingstatstable is not None and self.cefswitchingstatstable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cefadjsummarytable is not None and self.cefadjsummarytable.has_operation()) or
            (self.cefadjtable is not None and self.cefadjtable.has_operation()) or
            (self.cefcc is not None and self.cefcc.has_operation()) or
            (self.cefccglobaltable is not None and self.cefccglobaltable.has_operation()) or
            (self.cefcctypetable is not None and self.cefcctypetable.has_operation()) or
            (self.cefcfgtable is not None and self.cefcfgtable.has_operation()) or
            (self.ceffeselectiontable is not None and self.ceffeselectiontable.has_operation()) or
            (self.ceffib is not None and self.ceffib.has_operation()) or
            (self.ceffibsummarytable is not None and self.ceffibsummarytable.has_operation()) or
            (self.cefinconsistencyrecordtable is not None and self.cefinconsistencyrecordtable.has_operation()) or
            (self.cefinttable is not None and self.cefinttable.has_operation()) or
            (self.ceflmprefixtable is not None and self.ceflmprefixtable.has_operation()) or
            (self.cefnotifcntl is not None and self.cefnotifcntl.has_operation()) or
            (self.cefpathtable is not None and self.cefpathtable.has_operation()) or
            (self.cefpeerfibtable is not None and self.cefpeerfibtable.has_operation()) or
            (self.cefpeertable is not None and self.cefpeertable.has_operation()) or
            (self.cefprefixtable is not None and self.cefprefixtable.has_operation()) or
            (self.cefresourcetable is not None and self.cefresourcetable.has_operation()) or
            (self.cefstatsprefixlentable is not None and self.cefstatsprefixlentable.has_operation()) or
            (self.cefswitchingstatstable is not None and self.cefswitchingstatstable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-CEF-MIB:CISCO-CEF-MIB" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "cefAdjSummaryTable"):
            if (self.cefadjsummarytable is None):
                self.cefadjsummarytable = CiscoCefMib.Cefadjsummarytable()
                self.cefadjsummarytable.parent = self
                self._children_name_map["cefadjsummarytable"] = "cefAdjSummaryTable"
            return self.cefadjsummarytable

        if (child_yang_name == "cefAdjTable"):
            if (self.cefadjtable is None):
                self.cefadjtable = CiscoCefMib.Cefadjtable()
                self.cefadjtable.parent = self
                self._children_name_map["cefadjtable"] = "cefAdjTable"
            return self.cefadjtable

        if (child_yang_name == "cefCC"):
            if (self.cefcc is None):
                self.cefcc = CiscoCefMib.Cefcc()
                self.cefcc.parent = self
                self._children_name_map["cefcc"] = "cefCC"
            return self.cefcc

        if (child_yang_name == "cefCCGlobalTable"):
            if (self.cefccglobaltable is None):
                self.cefccglobaltable = CiscoCefMib.Cefccglobaltable()
                self.cefccglobaltable.parent = self
                self._children_name_map["cefccglobaltable"] = "cefCCGlobalTable"
            return self.cefccglobaltable

        if (child_yang_name == "cefCCTypeTable"):
            if (self.cefcctypetable is None):
                self.cefcctypetable = CiscoCefMib.Cefcctypetable()
                self.cefcctypetable.parent = self
                self._children_name_map["cefcctypetable"] = "cefCCTypeTable"
            return self.cefcctypetable

        if (child_yang_name == "cefCfgTable"):
            if (self.cefcfgtable is None):
                self.cefcfgtable = CiscoCefMib.Cefcfgtable()
                self.cefcfgtable.parent = self
                self._children_name_map["cefcfgtable"] = "cefCfgTable"
            return self.cefcfgtable

        if (child_yang_name == "cefFESelectionTable"):
            if (self.ceffeselectiontable is None):
                self.ceffeselectiontable = CiscoCefMib.Ceffeselectiontable()
                self.ceffeselectiontable.parent = self
                self._children_name_map["ceffeselectiontable"] = "cefFESelectionTable"
            return self.ceffeselectiontable

        if (child_yang_name == "cefFIB"):
            if (self.ceffib is None):
                self.ceffib = CiscoCefMib.Ceffib()
                self.ceffib.parent = self
                self._children_name_map["ceffib"] = "cefFIB"
            return self.ceffib

        if (child_yang_name == "cefFIBSummaryTable"):
            if (self.ceffibsummarytable is None):
                self.ceffibsummarytable = CiscoCefMib.Ceffibsummarytable()
                self.ceffibsummarytable.parent = self
                self._children_name_map["ceffibsummarytable"] = "cefFIBSummaryTable"
            return self.ceffibsummarytable

        if (child_yang_name == "cefInconsistencyRecordTable"):
            if (self.cefinconsistencyrecordtable is None):
                self.cefinconsistencyrecordtable = CiscoCefMib.Cefinconsistencyrecordtable()
                self.cefinconsistencyrecordtable.parent = self
                self._children_name_map["cefinconsistencyrecordtable"] = "cefInconsistencyRecordTable"
            return self.cefinconsistencyrecordtable

        if (child_yang_name == "cefIntTable"):
            if (self.cefinttable is None):
                self.cefinttable = CiscoCefMib.Cefinttable()
                self.cefinttable.parent = self
                self._children_name_map["cefinttable"] = "cefIntTable"
            return self.cefinttable

        if (child_yang_name == "cefLMPrefixTable"):
            if (self.ceflmprefixtable is None):
                self.ceflmprefixtable = CiscoCefMib.Ceflmprefixtable()
                self.ceflmprefixtable.parent = self
                self._children_name_map["ceflmprefixtable"] = "cefLMPrefixTable"
            return self.ceflmprefixtable

        if (child_yang_name == "cefNotifCntl"):
            if (self.cefnotifcntl is None):
                self.cefnotifcntl = CiscoCefMib.Cefnotifcntl()
                self.cefnotifcntl.parent = self
                self._children_name_map["cefnotifcntl"] = "cefNotifCntl"
            return self.cefnotifcntl

        if (child_yang_name == "cefPathTable"):
            if (self.cefpathtable is None):
                self.cefpathtable = CiscoCefMib.Cefpathtable()
                self.cefpathtable.parent = self
                self._children_name_map["cefpathtable"] = "cefPathTable"
            return self.cefpathtable

        if (child_yang_name == "cefPeerFIBTable"):
            if (self.cefpeerfibtable is None):
                self.cefpeerfibtable = CiscoCefMib.Cefpeerfibtable()
                self.cefpeerfibtable.parent = self
                self._children_name_map["cefpeerfibtable"] = "cefPeerFIBTable"
            return self.cefpeerfibtable

        if (child_yang_name == "cefPeerTable"):
            if (self.cefpeertable is None):
                self.cefpeertable = CiscoCefMib.Cefpeertable()
                self.cefpeertable.parent = self
                self._children_name_map["cefpeertable"] = "cefPeerTable"
            return self.cefpeertable

        if (child_yang_name == "cefPrefixTable"):
            if (self.cefprefixtable is None):
                self.cefprefixtable = CiscoCefMib.Cefprefixtable()
                self.cefprefixtable.parent = self
                self._children_name_map["cefprefixtable"] = "cefPrefixTable"
            return self.cefprefixtable

        if (child_yang_name == "cefResourceTable"):
            if (self.cefresourcetable is None):
                self.cefresourcetable = CiscoCefMib.Cefresourcetable()
                self.cefresourcetable.parent = self
                self._children_name_map["cefresourcetable"] = "cefResourceTable"
            return self.cefresourcetable

        if (child_yang_name == "cefStatsPrefixLenTable"):
            if (self.cefstatsprefixlentable is None):
                self.cefstatsprefixlentable = CiscoCefMib.Cefstatsprefixlentable()
                self.cefstatsprefixlentable.parent = self
                self._children_name_map["cefstatsprefixlentable"] = "cefStatsPrefixLenTable"
            return self.cefstatsprefixlentable

        if (child_yang_name == "cefSwitchingStatsTable"):
            if (self.cefswitchingstatstable is None):
                self.cefswitchingstatstable = CiscoCefMib.Cefswitchingstatstable()
                self.cefswitchingstatstable.parent = self
                self._children_name_map["cefswitchingstatstable"] = "cefSwitchingStatsTable"
            return self.cefswitchingstatstable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cefAdjSummaryTable" or name == "cefAdjTable" or name == "cefCC" or name == "cefCCGlobalTable" or name == "cefCCTypeTable" or name == "cefCfgTable" or name == "cefFESelectionTable" or name == "cefFIB" or name == "cefFIBSummaryTable" or name == "cefInconsistencyRecordTable" or name == "cefIntTable" or name == "cefLMPrefixTable" or name == "cefNotifCntl" or name == "cefPathTable" or name == "cefPeerFIBTable" or name == "cefPeerTable" or name == "cefPrefixTable" or name == "cefResourceTable" or name == "cefStatsPrefixLenTable" or name == "cefSwitchingStatsTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoCefMib()
        return self._top_entity

