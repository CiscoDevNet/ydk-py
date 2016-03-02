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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.cef.CISCO_CEF_TC import CefAdjLinkType_Enum
from ydk.models.cef.CISCO_CEF_TC import CefAdjacencySource_Bits
from ydk.models.cef.CISCO_CEF_TC import CefAdminStatus_Enum
from ydk.models.cef.CISCO_CEF_TC import CefCCAction_Enum
from ydk.models.cef.CISCO_CEF_TC import CefCCStatus_Enum
from ydk.models.cef.CISCO_CEF_TC import CefCCType_Enum
from ydk.models.cef.CISCO_CEF_TC import CefFailureReason_Enum
from ydk.models.cef.CISCO_CEF_TC import CefForwardingElementSpecialType_Enum
from ydk.models.cef.CISCO_CEF_TC import CefIpVersion_Enum
from ydk.models.cef.CISCO_CEF_TC import CefOperStatus_Enum
from ydk.models.cef.CISCO_CEF_TC import CefPathType_Enum
from ydk.models.cef.CISCO_CEF_TC import CefPrefixSearchState_Enum
from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum


class CISCOCEFMIB(object):
    """
    
    
    .. attribute:: cefadjsummarytable
    
    	This table contains the summary information for the cefAdjTable
    	**type**\: :py:class:`CefAdjSummaryTable <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefAdjSummaryTable>`
    
    .. attribute:: cefadjtable
    
    	A list of CEF adjacencies
    	**type**\: :py:class:`CefAdjTable <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefAdjTable>`
    
    .. attribute:: cefcc
    
    	
    	**type**\: :py:class:`CefCC <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefCC>`
    
    .. attribute:: cefccglobaltable
    
    	This table contains CEF consistency checker (CC) global parameters for the managed device
    	**type**\: :py:class:`CefCCGlobalTable <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefCCGlobalTable>`
    
    .. attribute:: cefcctypetable
    
    	This table contains CEF consistency checker types specific parameters on the managed device.  All detected inconsistency are signaled to the Management Station via cefInconsistencyDetection notification
    	**type**\: :py:class:`CefCCTypeTable <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefCCTypeTable>`
    
    .. attribute:: cefcfgtable
    
    	This table contains global config parameter  of CEF on the Managed device
    	**type**\: :py:class:`CefCfgTable <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefCfgTable>`
    
    .. attribute:: ceffeselectiontable
    
    	A list of forwarding element selection entries
    	**type**\: :py:class:`CefFESelectionTable <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefFESelectionTable>`
    
    .. attribute:: ceffib
    
    	
    	**type**\: :py:class:`CefFIB <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefFIB>`
    
    .. attribute:: ceffibsummarytable
    
    	This table contains the summary information for the cefPrefixTable
    	**type**\: :py:class:`CefFIBSummaryTable <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefFIBSummaryTable>`
    
    .. attribute:: cefinconsistencyrecordtable
    
    	This table contains CEF inconsistency records
    	**type**\: :py:class:`CefInconsistencyRecordTable <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefInconsistencyRecordTable>`
    
    .. attribute:: cefinttable
    
    	This Table contains interface specific information of CEF on the Managed device
    	**type**\: :py:class:`CefIntTable <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefIntTable>`
    
    .. attribute:: ceflmprefixtable
    
    	A table of Longest Match Prefix Query requests.  Generator application should utilize the cefLMPrefixSpinLock to try to avoid collisions. See DESCRIPTION clause of cefLMPrefixSpinLock
    	**type**\: :py:class:`CefLMPrefixTable <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefLMPrefixTable>`
    
    .. attribute:: cefnotifcntl
    
    	
    	**type**\: :py:class:`CefNotifCntl <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefNotifCntl>`
    
    .. attribute:: cefpathtable
    
    	CEF prefix path is a valid route to reach to a  destination IP prefix. Multiple paths may exist  out of a router to the same destination prefix.  This table specify lists of CEF paths
    	**type**\: :py:class:`CefPathTable <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefPathTable>`
    
    .. attribute:: cefpeerfibtable
    
    	Entity acting as RP (Routing Processor) keep the CEF FIB states for the line card entities and communicate with the line card entities using XDR. This Table contains the CEF FIB State  related to peer entities on the managed device
    	**type**\: :py:class:`CefPeerFIBTable <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefPeerFIBTable>`
    
    .. attribute:: cefpeertable
    
    	Entity acting as RP (Routing Processor) keeps the CEF states for the line card entities and communicates with the line card entities using XDR. This Table contains the CEF information  related to peer entities on the managed device
    	**type**\: :py:class:`CefPeerTable <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefPeerTable>`
    
    .. attribute:: cefprefixtable
    
    	A list of CEF forwarding prefixes
    	**type**\: :py:class:`CefPrefixTable <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefPrefixTable>`
    
    .. attribute:: cefresourcetable
    
    	This table contains global resource  information of CEF on the Managed device
    	**type**\: :py:class:`CefResourceTable <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefResourceTable>`
    
    .. attribute:: cefstatsprefixlentable
    
    	This table specifies the CEF stats based on the Prefix Length
    	**type**\: :py:class:`CefStatsPrefixLenTable <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefStatsPrefixLenTable>`
    
    .. attribute:: cefswitchingstatstable
    
    	This table specifies the CEF switch stats
    	**type**\: :py:class:`CefSwitchingStatsTable <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefSwitchingStatsTable>`
    
    

    """

    _prefix = 'cisco-cef-mib'
    _revision = '2006-01-30'

    def __init__(self):
        self.cefadjsummarytable = CISCOCEFMIB.CefAdjSummaryTable()
        self.cefadjsummarytable.parent = self
        self.cefadjtable = CISCOCEFMIB.CefAdjTable()
        self.cefadjtable.parent = self
        self.cefcc = CISCOCEFMIB.CefCC()
        self.cefcc.parent = self
        self.cefccglobaltable = CISCOCEFMIB.CefCCGlobalTable()
        self.cefccglobaltable.parent = self
        self.cefcctypetable = CISCOCEFMIB.CefCCTypeTable()
        self.cefcctypetable.parent = self
        self.cefcfgtable = CISCOCEFMIB.CefCfgTable()
        self.cefcfgtable.parent = self
        self.ceffeselectiontable = CISCOCEFMIB.CefFESelectionTable()
        self.ceffeselectiontable.parent = self
        self.ceffib = CISCOCEFMIB.CefFIB()
        self.ceffib.parent = self
        self.ceffibsummarytable = CISCOCEFMIB.CefFIBSummaryTable()
        self.ceffibsummarytable.parent = self
        self.cefinconsistencyrecordtable = CISCOCEFMIB.CefInconsistencyRecordTable()
        self.cefinconsistencyrecordtable.parent = self
        self.cefinttable = CISCOCEFMIB.CefIntTable()
        self.cefinttable.parent = self
        self.ceflmprefixtable = CISCOCEFMIB.CefLMPrefixTable()
        self.ceflmprefixtable.parent = self
        self.cefnotifcntl = CISCOCEFMIB.CefNotifCntl()
        self.cefnotifcntl.parent = self
        self.cefpathtable = CISCOCEFMIB.CefPathTable()
        self.cefpathtable.parent = self
        self.cefpeerfibtable = CISCOCEFMIB.CefPeerFIBTable()
        self.cefpeerfibtable.parent = self
        self.cefpeertable = CISCOCEFMIB.CefPeerTable()
        self.cefpeertable.parent = self
        self.cefprefixtable = CISCOCEFMIB.CefPrefixTable()
        self.cefprefixtable.parent = self
        self.cefresourcetable = CISCOCEFMIB.CefResourceTable()
        self.cefresourcetable.parent = self
        self.cefstatsprefixlentable = CISCOCEFMIB.CefStatsPrefixLenTable()
        self.cefstatsprefixlentable.parent = self
        self.cefswitchingstatstable = CISCOCEFMIB.CefSwitchingStatsTable()
        self.cefswitchingstatstable.parent = self


    class CefAdjSummaryTable(object):
        """
        This table contains the summary information
        for the cefAdjTable.
        
        .. attribute:: cefadjsummaryentry
        
        	If CEF is enabled on the Managed device, each entry contains the CEF Adjacency   summary related attributes for the Managed entity. A row exists for each adjacency link type.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of :py:class:`CefAdjSummaryEntry <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefAdjSummaryTable.CefAdjSummaryEntry>`
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.cefadjsummaryentry = YList()
            self.cefadjsummaryentry.parent = self
            self.cefadjsummaryentry.name = 'cefadjsummaryentry'


        class CefAdjSummaryEntry(object):
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
            
            .. attribute:: cefadjsummarylinktype
            
            	The link type of the adjacency
            	**type**\: :py:class:`CefAdjLinkType_Enum <ydk.models.cef.CISCO_CEF_TC.CefAdjLinkType_Enum>`
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefadjsummarycomplete
            
            	The total number of complete adjacencies.  The total number of adjacencies which can be used  to switch traffic to a neighbour
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefadjsummaryfixup
            
            	The total number of adjacencies for which the Layer 2 encapsulation string (header) may be  updated (fixed up) at packet switch time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefadjsummaryincomplete
            
            	The total number of incomplete adjacencies.  The total number of adjacencies which cannot be  used to switch traffic in their current state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefadjsummaryredirect
            
            	The total number of adjacencies for which  ip redirect (or icmp redirection) is enabled. The value of this object is only relevant for ipv4 and ipv6 link type (when the index object  cefAdjSummaryLinkType value is ipv4(1) or ipv6(2)) and will be set to zero for other link types
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-cef-mib'
            _revision = '2006-01-30'

            def __init__(self):
                self.parent = None
                self.cefadjsummarylinktype = None
                self.entphysicalindex = None
                self.cefadjsummarycomplete = None
                self.cefadjsummaryfixup = None
                self.cefadjsummaryincomplete = None
                self.cefadjsummaryredirect = None

            @property
            def _common_path(self):
                if self.cefadjsummarylinktype is None:
                    raise YPYDataValidationError('Key property cefadjsummarylinktype is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefAdjSummaryTable/CISCO-CEF-MIB:cefAdjSummaryEntry[CISCO-CEF-MIB:cefAdjSummaryLinkType = ' + str(self.cefadjsummarylinktype) + '][CISCO-CEF-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cefadjsummarylinktype is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.cefadjsummarycomplete is not None:
                    return True

                if self.cefadjsummaryfixup is not None:
                    return True

                if self.cefadjsummaryincomplete is not None:
                    return True

                if self.cefadjsummaryredirect is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                return meta._meta_table['CISCOCEFMIB.CefAdjSummaryTable.CefAdjSummaryEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefAdjSummaryTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefadjsummaryentry is not None:
                for child_ref in self.cefadjsummaryentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefAdjSummaryTable']['meta_info']


    class CefAdjTable(object):
        """
        A list of CEF adjacencies.
        
        .. attribute:: cefadjentry
        
        	If CEF is enabled on the Managed device, each entry contains the adjacency  attributes. Adjacency entries may exist for all the interfaces on which packets can be switched out of the device. The interface is instantiated by ifIndex.   Therefore, the interface index must have been assigned, according to the applicable procedures, before it can be meaningfully used. Generally, this means that the interface must exist.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of :py:class:`CefAdjEntry <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefAdjTable.CefAdjEntry>`
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.cefadjentry = YList()
            self.cefadjentry.parent = self
            self.cefadjentry.name = 'cefadjentry'


        class CefAdjEntry(object):
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
            
            .. attribute:: cefadjconnid
            
            	In cases where cefLinkType, interface and the next hop address are not able to uniquely define an adjacency entry (e.g. ATM and Frame Relay Bundles), this object is a unique identifier to differentiate between these adjacency entries.   In all the other cases the value of this  index object will be 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefadjnexthopaddr
            
            	The next Hop address for this adjacency. The type of this address is determined by the value of the cefAdjNextHopAddrType object
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cefadjnexthopaddrtype
            
            	Address type for the cefAdjNextHopAddr. This object specifies the address type used for cefAdjNextHopAddr.   Adjacency entries are only valid for the  address type of ipv4(1) and ipv6(2)
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cefadjsummarylinktype
            
            	
            	**type**\: :py:class:`CefAdjLinkType_Enum <ydk.models.cef.CISCO_CEF_TC.CefAdjLinkType_Enum>`
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefadjbytes
            
            	Number of bytes transmitted using this adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefadjencap
            
            	The layer 2 encapsulation string to be used for sending the packet out using this adjacency
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cefadjfixup
            
            	For the cases, where the encapsulation string is decided at packet switch time, the adjacency  encapsulation string specified by object cefAdjEncap  require a fixup. I.e. for the adjacencies out of IP  Tunnels, the string prepended is an IP header which has  fields which can only be setup at packet switch time.  The value of this object represent the kind of fixup applied to the packet.  If the encapsulation string doesn't require any fixup, then the value of this object will be of zero length
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cefadjforwardinginfo
            
            	This object selects a forwarding info entry  defined in the cefFESelectionTable. The  selected target is defined by an entry in the cefFESelectionTable whose index value (cefFESelectionName)  is equal to this object.  The value of this object will be of zero length if this adjacency entry is the last forwarding  element in the forwarding path
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cefadjhcbytes
            
            	Number of bytes transmitted using this adjacency. This object is a 64\-bit version of cefAdjBytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefadjhcpkts
            
            	Number of pkts transmitted using this adjacency. This object is a 64\-bit version of cefAdjPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefadjmtu
            
            	The Layer 3 MTU which can be transmitted using  this adjacency
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: cefadjpkts
            
            	Number of pkts transmitted using this adjacency
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefadjsource
            
            	If the adjacency is created because some neighbour discovery mechanism has discovered a neighbour and all the information required to build a frame header to encapsulate traffic to the neighbour is available then the source of adjacency is set to the mechanism by which the adjacency is learned
            	**type**\: :py:class:`CefAdjacencySource_Bits <ydk.models.cef.CISCO_CEF_TC.CefAdjacencySource_Bits>`
            
            

            """

            _prefix = 'cisco-cef-mib'
            _revision = '2006-01-30'

            def __init__(self):
                self.parent = None
                self.cefadjconnid = None
                self.cefadjnexthopaddr = None
                self.cefadjnexthopaddrtype = None
                self.cefadjsummarylinktype = None
                self.entphysicalindex = None
                self.ifindex = None
                self.cefadjbytes = None
                self.cefadjencap = None
                self.cefadjfixup = None
                self.cefadjforwardinginfo = None
                self.cefadjhcbytes = None
                self.cefadjhcpkts = None
                self.cefadjmtu = None
                self.cefadjpkts = None
                self.cefadjsource = CefAdjacencySource_Bits()

            @property
            def _common_path(self):
                if self.cefadjconnid is None:
                    raise YPYDataValidationError('Key property cefadjconnid is None')
                if self.cefadjnexthopaddr is None:
                    raise YPYDataValidationError('Key property cefadjnexthopaddr is None')
                if self.cefadjnexthopaddrtype is None:
                    raise YPYDataValidationError('Key property cefadjnexthopaddrtype is None')
                if self.cefadjsummarylinktype is None:
                    raise YPYDataValidationError('Key property cefadjsummarylinktype is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefAdjTable/CISCO-CEF-MIB:cefAdjEntry[CISCO-CEF-MIB:cefAdjConnId = ' + str(self.cefadjconnid) + '][CISCO-CEF-MIB:cefAdjNextHopAddr = ' + str(self.cefadjnexthopaddr) + '][CISCO-CEF-MIB:cefAdjNextHopAddrType = ' + str(self.cefadjnexthopaddrtype) + '][CISCO-CEF-MIB:cefAdjSummaryLinkType = ' + str(self.cefadjsummarylinktype) + '][CISCO-CEF-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + '][CISCO-CEF-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cefadjconnid is not None:
                    return True

                if self.cefadjnexthopaddr is not None:
                    return True

                if self.cefadjnexthopaddrtype is not None:
                    return True

                if self.cefadjsummarylinktype is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.cefadjbytes is not None:
                    return True

                if self.cefadjencap is not None:
                    return True

                if self.cefadjfixup is not None:
                    return True

                if self.cefadjforwardinginfo is not None:
                    return True

                if self.cefadjhcbytes is not None:
                    return True

                if self.cefadjhcpkts is not None:
                    return True

                if self.cefadjmtu is not None:
                    return True

                if self.cefadjpkts is not None:
                    return True

                if self.cefadjsource is not None:
                    if self.cefadjsource._has_data():
                        return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                return meta._meta_table['CISCOCEFMIB.CefAdjTable.CefAdjEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefAdjTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefadjentry is not None:
                for child_ref in self.cefadjentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefAdjTable']['meta_info']


    class CefCC(object):
        """
        
        
        .. attribute:: cefinconsistencyreset
        
        	Setting the value of this object to ccActionStart(1) will reset all the active consistency checkers.  The Management station should poll the  cefInconsistencyResetStatus object to get the  state of inconsistency reset operation.  This operation once started, cannot be aborted. Hence, the value of this object cannot be set to ccActionAbort(2).  The value of this object can't be set to ccActionStart(1),  if the value of object cefInconsistencyResetStatus is ccStatusRunning(2)
        	**type**\: :py:class:`CefCCAction_Enum <ydk.models.cef.CISCO_CEF_TC.CefCCAction_Enum>`
        
        .. attribute:: cefinconsistencyresetstatus
        
        	Indicates the status of the consistency reset request
        	**type**\: :py:class:`CefCCStatus_Enum <ydk.models.cef.CISCO_CEF_TC.CefCCStatus_Enum>`
        
        .. attribute:: entlastinconsistencydetecttime
        
        	The value of sysUpTime at the time an inconsistency is detecetd
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.cefinconsistencyreset = None
            self.cefinconsistencyresetstatus = None
            self.entlastinconsistencydetecttime = None

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefCC'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefinconsistencyreset is not None:
                return True

            if self.cefinconsistencyresetstatus is not None:
                return True

            if self.entlastinconsistencydetecttime is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefCC']['meta_info']


    class CefCCGlobalTable(object):
        """
        This table contains CEF consistency checker
        (CC) global parameters for the managed device.
        
        .. attribute:: cefccglobalentry
        
        	If the managed device supports CEF, each entry contains the global consistency  checker parameter for the managed device. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device
        	**type**\: list of :py:class:`CefCCGlobalEntry <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefCCGlobalTable.CefCCGlobalEntry>`
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.cefccglobalentry = YList()
            self.cefccglobalentry.parent = self
            self.cefccglobalentry.name = 'cefccglobalentry'


        class CefCCGlobalEntry(object):
            """
            If the managed device supports CEF,
            each entry contains the global consistency 
            checker parameter for the managed device.
            A row may exist for each IP version type
            (v4 and v6) depending upon the IP version
            supported on the device.
            
            .. attribute:: ceffibipversion
            
            	
            	**type**\: :py:class:`CefIpVersion_Enum <ydk.models.cef.CISCO_CEF_TC.CefIpVersion_Enum>`
            
            .. attribute:: cefccglobalautorepairdelay
            
            	Indiactes how long the consistency checker  waits to fix an inconsistency.  The value of this object has no effect when the value of object cefCCGlobalAutoRepairEnabled is 'false'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefccglobalautorepairenabled
            
            	Once an inconsistency has been detected,  CEF has the ability to repair the problem.  This object indicates the status of auto\-repair  function for the consistency checkers
            	**type**\: bool
            
            .. attribute:: cefccglobalautorepairholddown
            
            	Indicates how long the consistency checker waits to re\-enable auto\-repair after  auto\-repair runs.  The value of this object has no effect when the value of object cefCCGlobalAutoRepairEnabled is 'false'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefccglobalerrormsgenabled
            
            	Enables the consistency checker to generate  an error message when it detects an inconsistency
            	**type**\: bool
            
            .. attribute:: cefccglobalfullscanaction
            
            	Setting the value of this object to ccActionStart(1) will start the full scan consistency checkers.  The Management station should poll the  cefCCGlobalFullScanStatus object to get the  state of full\-scan operation.  Once the full\-scan operation completes (value of cefCCGlobalFullScanStatus object is ccStatusDone(3)),  the Management station should retrieve the values of the related stats object from the cefCCTypeTable.  Setting the value of this object to ccActionAbort(2) will  abort the full\-scan operation.  The value of this object can't be set to ccActionStart(1),  if the value of object cefCCGlobalFullScanStatus is ccStatusRunning(2).  The value of this object will be set to cefActionNone(1) when the full scan consistency checkers have never been activated.  A Management Station cannot set the value of this object to cefActionNone(1)
            	**type**\: :py:class:`CefCCAction_Enum <ydk.models.cef.CISCO_CEF_TC.CefCCAction_Enum>`
            
            .. attribute:: cefccglobalfullscanstatus
            
            	Indicates the status of the full scan consistency checker request
            	**type**\: :py:class:`CefCCStatus_Enum <ydk.models.cef.CISCO_CEF_TC.CefCCStatus_Enum>`
            
            

            """

            _prefix = 'cisco-cef-mib'
            _revision = '2006-01-30'

            def __init__(self):
                self.parent = None
                self.ceffibipversion = None
                self.cefccglobalautorepairdelay = None
                self.cefccglobalautorepairenabled = None
                self.cefccglobalautorepairholddown = None
                self.cefccglobalerrormsgenabled = None
                self.cefccglobalfullscanaction = None
                self.cefccglobalfullscanstatus = None

            @property
            def _common_path(self):
                if self.ceffibipversion is None:
                    raise YPYDataValidationError('Key property ceffibipversion is None')

                return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefCCGlobalTable/CISCO-CEF-MIB:cefCCGlobalEntry[CISCO-CEF-MIB:cefFIBIpVersion = ' + str(self.ceffibipversion) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ceffibipversion is not None:
                    return True

                if self.cefccglobalautorepairdelay is not None:
                    return True

                if self.cefccglobalautorepairenabled is not None:
                    return True

                if self.cefccglobalautorepairholddown is not None:
                    return True

                if self.cefccglobalerrormsgenabled is not None:
                    return True

                if self.cefccglobalfullscanaction is not None:
                    return True

                if self.cefccglobalfullscanstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                return meta._meta_table['CISCOCEFMIB.CefCCGlobalTable.CefCCGlobalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefCCGlobalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefccglobalentry is not None:
                for child_ref in self.cefccglobalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefCCGlobalTable']['meta_info']


    class CefCCTypeTable(object):
        """
        This table contains CEF consistency
        checker types specific parameters on the managed device.
        
        All detected inconsistency are signaled to the
        Management Station via cefInconsistencyDetection
        notification.
        
        .. attribute:: cefcctypeentry
        
        	If the managed device supports CEF, each entry contains the consistency  checker statistics for a consistency  checker type. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device
        	**type**\: list of :py:class:`CefCCTypeEntry <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefCCTypeTable.CefCCTypeEntry>`
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.cefcctypeentry = YList()
            self.cefcctypeentry.parent = self
            self.cefcctypeentry.name = 'cefcctypeentry'


        class CefCCTypeEntry(object):
            """
            If the managed device supports CEF,
            each entry contains the consistency 
            checker statistics for a consistency 
            checker type.
            A row may exist for each IP version type
            (v4 and v6) depending upon the IP version
            supported on the device.
            
            .. attribute:: cefcctype
            
            	Type of the consistency checker
            	**type**\: :py:class:`CefCCType_Enum <ydk.models.cef.CISCO_CEF_TC.CefCCType_Enum>`
            
            .. attribute:: ceffibipversion
            
            	
            	**type**\: :py:class:`CefIpVersion_Enum <ydk.models.cef.CISCO_CEF_TC.CefIpVersion_Enum>`
            
            .. attribute:: cefcccount
            
            	The maximum number of prefixes to check per scan.  The default value for this object  depends upon the consistency checker type.  The value of this object will be irrelevant  for some of the consistency checkers and will be set to 0.  A Management Station cannot set the value of this object to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefccenabled
            
            	Enables the passive consistency checker. Passive consistency checkers are disabled by default.  Full\-scan consistency checkers are always enabled. An attempt to set this object to 'false' for an active consistency checker will result in 'wrongValue' error
            	**type**\: bool
            
            .. attribute:: cefccperiod
            
            	The period between scans for the consistency checker
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefccquerieschecked
            
            	Number of prefix consistency queries processed by this  consistency checker
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefccqueriesignored
            
            	Number of prefix consistency queries for which the consistency checks were not performed by this  consistency checker. This may be because of some internal error or resource failure
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefccqueriesiterated
            
            	Number of prefix consistency queries iterated back to the master database by this consistency checker
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefccqueriessent
            
            	Number of prefix consistency queries sent to CEF forwarding databases by this consistency checker
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-cef-mib'
            _revision = '2006-01-30'

            def __init__(self):
                self.parent = None
                self.cefcctype = None
                self.ceffibipversion = None
                self.cefcccount = None
                self.cefccenabled = None
                self.cefccperiod = None
                self.cefccquerieschecked = None
                self.cefccqueriesignored = None
                self.cefccqueriesiterated = None
                self.cefccqueriessent = None

            @property
            def _common_path(self):
                if self.cefcctype is None:
                    raise YPYDataValidationError('Key property cefcctype is None')
                if self.ceffibipversion is None:
                    raise YPYDataValidationError('Key property ceffibipversion is None')

                return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefCCTypeTable/CISCO-CEF-MIB:cefCCTypeEntry[CISCO-CEF-MIB:cefCCType = ' + str(self.cefcctype) + '][CISCO-CEF-MIB:cefFIBIpVersion = ' + str(self.ceffibipversion) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cefcctype is not None:
                    return True

                if self.ceffibipversion is not None:
                    return True

                if self.cefcccount is not None:
                    return True

                if self.cefccenabled is not None:
                    return True

                if self.cefccperiod is not None:
                    return True

                if self.cefccquerieschecked is not None:
                    return True

                if self.cefccqueriesignored is not None:
                    return True

                if self.cefccqueriesiterated is not None:
                    return True

                if self.cefccqueriessent is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                return meta._meta_table['CISCOCEFMIB.CefCCTypeTable.CefCCTypeEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefCCTypeTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcctypeentry is not None:
                for child_ref in self.cefcctypeentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefCCTypeTable']['meta_info']


    class CefCfgTable(object):
        """
        This table contains global config parameter 
        of CEF on the Managed device.
        
        .. attribute:: cefcfgentry
        
        	If the Managed device supports CEF,  each entry contains the CEF config  parameter for the managed entity. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of :py:class:`CefCfgEntry <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefCfgTable.CefCfgEntry>`
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.cefcfgentry = YList()
            self.cefcfgentry.parent = self
            self.cefcfgentry.name = 'cefcfgentry'


        class CefCfgEntry(object):
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
            
            .. attribute:: ceffibipversion
            
            	
            	**type**\: :py:class:`CefIpVersion_Enum <ydk.models.cef.CISCO_CEF_TC.CefIpVersion_Enum>`
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefcfgaccountingmap
            
            	This object represents a bitmap of network accounting options.  CEF network accounting is disabled by default.  CEF network accounting can be enabled  by selecting one or more of the following CEF accounting option for the value of this object.    nonRecursive(0)\:  enables accounting through                     nonrecursive prefixes.   perPrefix(1)\:     enables the collection of the numbers                     of pkts and bytes express forwarded                    to a destination (prefix)   prefixLength(2)\:  enables accounting through                     prefixlength.           Once the accounting is enabled, the corresponding stats  can be retrieved from the cefPrefixTable and  cefStatsPrefixLenTable.  
            	**type**\: :py:class:`CefCfgAccountingMap_Bits <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefCfgTable.CefCfgEntry.CefCfgAccountingMap_Bits>`
            
            .. attribute:: cefcfgadminstate
            
            	The desired state of CEF
            	**type**\: :py:class:`CefAdminStatus_Enum <ydk.models.cef.CISCO_CEF_TC.CefAdminStatus_Enum>`
            
            .. attribute:: cefcfgdistributionadminstate
            
            	The desired state of CEF distribution
            	**type**\: :py:class:`CefAdminStatus_Enum <ydk.models.cef.CISCO_CEF_TC.CefAdminStatus_Enum>`
            
            .. attribute:: cefcfgdistributionoperstate
            
            	The current operational state of CEF distribution.  If the cefCfgDistributionAdminState is disabled(2), then cefDistributionOperState will eventually go to the down(2) state unless some error has occurred.    If cefCfgDistributionAdminState is changed to enabled(1)  then cefCfgDistributionOperState should change to up(1)  only if the CEF entity is ready to forward the packets  using Distributed Cisco Express Forwarding (dCEF) else  it should remain in the down(2) state. The up(1) state  for this object indicates that CEF entity is forwarding the packet using Distributed Cisco Express Forwarding
            	**type**\: :py:class:`CefOperStatus_Enum <ydk.models.cef.CISCO_CEF_TC.CefOperStatus_Enum>`
            
            .. attribute:: cefcfgloadsharingalgorithm
            
            	Indicates the CEF Load balancing algorithm.  Setting this object to none(1) will disable the Load sharing for the specified entry.  CEF load balancing can be enabled by setting  this object to one of following Algorithms\:   original(2)  \: This algorithm is based on a                  source and destination hash    tunnel(3)    \: This algorithm is used in                  tunnels environments or in                 environments where there are                 only a few source                      universal(4)  \: This algorithm uses a source and                   destination and ID hash  If the value of this object is set to 'tunnel' or 'universal', then the FIXED ID for these algorithms may be specified by the managed  object cefLoadSharingID. 
            	**type**\: :py:class:`CefCfgLoadSharingAlgorithm_Enum <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefCfgTable.CefCfgEntry.CefCfgLoadSharingAlgorithm_Enum>`
            
            .. attribute:: cefcfgloadsharingid
            
            	The Fixed ID associated with the managed object cefCfgLoadSharingAlgorithm. The hash of this object value may be used by the Load Sharing Algorithm.  The value of this object is not relevant and will be set to zero if the value of managed object  cefCfgLoadSharingAlgorithm is set to none(1) or original(2). The default value of this object is calculated by the device at the time of initialization
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcfgoperstate
            
            	The current operational state of CEF.  If the cefCfgAdminState is disabled(2), then cefOperState will eventually go to the down(2) state unless some error has occurred.   If cefCfgAdminState is changed to enabled(1) then  cefCfgOperState should change to up(1) only if the  CEF entity is ready to forward the packets using  Cisco Express Forwarding (CEF) else it should remain  in the down(2) state. The up(1) state for this object  indicates that CEF entity is forwarding the packet using Cisco Express Forwarding
            	**type**\: :py:class:`CefOperStatus_Enum <ydk.models.cef.CISCO_CEF_TC.CefOperStatus_Enum>`
            
            .. attribute:: cefcfgtrafficstatsloadinterval
            
            	The interval time over which the CEF traffic statistics are collected
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefcfgtrafficstatsupdaterate
            
            	The frequency with which the line card sends the traffic load statistics to the Router Processor.  Setting the value of this object to 0 will disable the CEF traffic statistics collection
            	**type**\: int
            
            	**range:** 0..65535
            
            

            """

            _prefix = 'cisco-cef-mib'
            _revision = '2006-01-30'

            def __init__(self):
                self.parent = None
                self.ceffibipversion = None
                self.entphysicalindex = None
                self.cefcfgaccountingmap = CISCOCEFMIB.CefCfgTable.CefCfgEntry.CefCfgAccountingMap_Bits()
                self.cefcfgadminstate = None
                self.cefcfgdistributionadminstate = None
                self.cefcfgdistributionoperstate = None
                self.cefcfgloadsharingalgorithm = None
                self.cefcfgloadsharingid = None
                self.cefcfgoperstate = None
                self.cefcfgtrafficstatsloadinterval = None
                self.cefcfgtrafficstatsupdaterate = None

            class CefCfgLoadSharingAlgorithm_Enum(Enum):
                """
                CefCfgLoadSharingAlgorithm_Enum

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

                """

                NONE = 1

                ORIGINAL = 2

                TUNNEL = 3

                UNIVERSAL = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                    return meta._meta_table['CISCOCEFMIB.CefCfgTable.CefCfgEntry.CefCfgLoadSharingAlgorithm_Enum']


            class CefCfgAccountingMap_Bits(FixedBitsDict):
                """
                CefCfgAccountingMap_Bits

                This object represents a bitmap of network
                accounting options.
                
                CEF network accounting is disabled by default.
                
                CEF network accounting can be enabled 
                by selecting one or more of the following
                CEF accounting option for the value
                of this object.
                 
                 nonRecursive(0)\:  enables accounting through 
                                   nonrecursive prefixes.
                
                 perPrefix(1)\:     enables the collection of the numbers 
                                   of pkts and bytes express forwarded
                                   to a destination (prefix)
                
                 prefixLength(2)\:  enables accounting through 
                                   prefixlength.        
                
                 Once the accounting is enabled, the corresponding stats
                 can be retrieved from the cefPrefixTable and
                 cefStatsPrefixLenTable.
                 
                Keys are:- perPrefix , nonRecursive , prefixLength

                """

                def __init__(self):
                    self._dictionary = { 
                        'perPrefix':False,
                        'nonRecursive':False,
                        'prefixLength':False,
                    }
                    self._pos_map = { 
                        'perPrefix':1,
                        'nonRecursive':0,
                        'prefixLength':2,
                    }

            @property
            def _common_path(self):
                if self.ceffibipversion is None:
                    raise YPYDataValidationError('Key property ceffibipversion is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefCfgTable/CISCO-CEF-MIB:cefCfgEntry[CISCO-CEF-MIB:cefFIBIpVersion = ' + str(self.ceffibipversion) + '][CISCO-CEF-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ceffibipversion is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.cefcfgaccountingmap is not None:
                    if self.cefcfgaccountingmap._has_data():
                        return True

                if self.cefcfgadminstate is not None:
                    return True

                if self.cefcfgdistributionadminstate is not None:
                    return True

                if self.cefcfgdistributionoperstate is not None:
                    return True

                if self.cefcfgloadsharingalgorithm is not None:
                    return True

                if self.cefcfgloadsharingid is not None:
                    return True

                if self.cefcfgoperstate is not None:
                    return True

                if self.cefcfgtrafficstatsloadinterval is not None:
                    return True

                if self.cefcfgtrafficstatsupdaterate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                return meta._meta_table['CISCOCEFMIB.CefCfgTable.CefCfgEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefCfgTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefcfgentry is not None:
                for child_ref in self.cefcfgentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefCfgTable']['meta_info']


    class CefFESelectionTable(object):
        """
        A list of forwarding element selection entries.
        
        .. attribute:: ceffeselectionentry
        
        	If CEF is enabled on the Managed device, each entry contain a CEF forwarding element selection list.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of :py:class:`CefFESelectionEntry <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefFESelectionTable.CefFESelectionEntry>`
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.ceffeselectionentry = YList()
            self.ceffeselectionentry.parent = self
            self.ceffeselectionentry.name = 'ceffeselectionentry'


        class CefFESelectionEntry(object):
            """
            If CEF is enabled on the Managed device,
            each entry contain a CEF forwarding element
            selection list.
            
            entPhysicalIndex is also an index for this
            table which represents entities of
            'module' entPhysicalClass which are capable
            of running CEF.
            
            .. attribute:: ceffeselectionid
            
            	Secondary index to identify a forwarding elements List  in this Table
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ceffeselectionname
            
            	The locally arbitrary, but unique identifier used to select a set of forwarding element lists
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ceffeselectionadjconnid
            
            	This object represent the connection id for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to zero if the forwarding element list doesn't  contain an adjacency forwarding element.   In cases where cefFESelectionAdjLinkType, interface  and the next hop address are not able to uniquely  define an adjacency entry (e.g. ATM and Frame Relay Bundles), this object is a unique identifier to differentiate between these adjacency entries
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceffeselectionadjinterface
            
            	This object represent the interface for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to zero if the forwarding element list doesn't  contain an adjacency forwarding element
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ceffeselectionadjlinktype
            
            	This object represent the link type for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to unknown(5) if the forwarding element list  doesn't contain an adjacency forwarding element
            	**type**\: :py:class:`CefAdjLinkType_Enum <ydk.models.cef.CISCO_CEF_TC.CefAdjLinkType_Enum>`
            
            .. attribute:: ceffeselectionadjnexthopaddr
            
            	This object represent the next hop address for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to zero if the forwarding element list doesn't  contain an adjacency forwarding element
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ceffeselectionadjnexthopaddrtype
            
            	This object represent the next hop address type for the adjacency associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to unknown(0) if the forwarding element list  doesn't contain an adjacency forwarding element
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ceffeselectionlabels
            
            	This object represent the MPLS Labels  associated with this forwarding Element List.  The value of this object will be irrelevant and will be set to zero length if the forwarding element list  doesn't contain a label forwarding element. A zero  length label list will indicate that there is no label forwarding element associated with this selection entry
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ceffeselectionspecial
            
            	Special processing for a destination is indicated through the use of special  forwarding element.   If the forwarding element list contains the  special forwarding element, then this object  represents the type of special forwarding element
            	**type**\: :py:class:`CefForwardingElementSpecialType_Enum <ydk.models.cef.CISCO_CEF_TC.CefForwardingElementSpecialType_Enum>`
            
            .. attribute:: ceffeselectionvrfname
            
            	This object represent the Vrf name for the lookup associated with this forwarding  Element List.  The value of this object will be irrelevant and will be set to a string containing the single octet 0x00 if the forwarding element list  doesn't contain a lookup forwarding element
            	**type**\: str
            
            	**range:** 0..31
            
            .. attribute:: ceffeselectionweight
            
            	This object represent the weighting for  load balancing between multiple Forwarding Element Lists. The value of this object will be zero if load balancing is associated with this selection entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-cef-mib'
            _revision = '2006-01-30'

            def __init__(self):
                self.parent = None
                self.ceffeselectionid = None
                self.ceffeselectionname = None
                self.entphysicalindex = None
                self.ceffeselectionadjconnid = None
                self.ceffeselectionadjinterface = None
                self.ceffeselectionadjlinktype = None
                self.ceffeselectionadjnexthopaddr = None
                self.ceffeselectionadjnexthopaddrtype = None
                self.ceffeselectionlabels = None
                self.ceffeselectionspecial = None
                self.ceffeselectionvrfname = None
                self.ceffeselectionweight = None

            @property
            def _common_path(self):
                if self.ceffeselectionid is None:
                    raise YPYDataValidationError('Key property ceffeselectionid is None')
                if self.ceffeselectionname is None:
                    raise YPYDataValidationError('Key property ceffeselectionname is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefFESelectionTable/CISCO-CEF-MIB:cefFESelectionEntry[CISCO-CEF-MIB:cefFESelectionId = ' + str(self.ceffeselectionid) + '][CISCO-CEF-MIB:cefFESelectionName = ' + str(self.ceffeselectionname) + '][CISCO-CEF-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ceffeselectionid is not None:
                    return True

                if self.ceffeselectionname is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.ceffeselectionadjconnid is not None:
                    return True

                if self.ceffeselectionadjinterface is not None:
                    return True

                if self.ceffeselectionadjlinktype is not None:
                    return True

                if self.ceffeselectionadjnexthopaddr is not None:
                    return True

                if self.ceffeselectionadjnexthopaddrtype is not None:
                    return True

                if self.ceffeselectionlabels is not None:
                    return True

                if self.ceffeselectionspecial is not None:
                    return True

                if self.ceffeselectionvrfname is not None:
                    return True

                if self.ceffeselectionweight is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                return meta._meta_table['CISCOCEFMIB.CefFESelectionTable.CefFESelectionEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefFESelectionTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ceffeselectionentry is not None:
                for child_ref in self.ceffeselectionentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefFESelectionTable']['meta_info']


    class CefFIB(object):
        """
        
        
        .. attribute:: ceflmprefixspinlock
        
        	An advisory lock used to allow cooperating SNMP Command Generator applications to coordinate their use of the Set operation in creating Longest Match Prefix Entries in cefLMPrefixTable.  When creating a new longest prefix match entry, the value of cefLMPrefixSpinLock should be retrieved.   The destination address should be determined to be unique by the SNMP Command Generator application by consulting the cefLMPrefixTable. Finally, the longest  prefix entry may be created (Set), including the advisory lock.         If another SNMP Command Generator application has altered the longest prefix entry in the meantime,  then the spin lock's value will have changed,  and so this creation will fail because it will specify the wrong value for the spin lock.  Since this is an advisory lock, the use of this lock is not enforced, but not using this lock may lead to conflict with the another SNMP command responder  application which may also be acting on the cefLMPrefixTable
        	**type**\: int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.ceflmprefixspinlock = None

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefFIB'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ceflmprefixspinlock is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefFIB']['meta_info']


    class CefFIBSummaryTable(object):
        """
        This table contains the summary information
        for the cefPrefixTable.
        
        .. attribute:: ceffibsummaryentry
        
        	If CEF is enabled on the Managed device, each entry contains the FIB summary related attributes for the managed entity.  A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of :py:class:`CefFIBSummaryEntry <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefFIBSummaryTable.CefFIBSummaryEntry>`
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.ceffibsummaryentry = YList()
            self.ceffibsummaryentry.parent = self
            self.ceffibsummaryentry.name = 'ceffibsummaryentry'


        class CefFIBSummaryEntry(object):
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
            
            .. attribute:: ceffibipversion
            
            	The version of IP forwarding
            	**type**\: :py:class:`CefIpVersion_Enum <ydk.models.cef.CISCO_CEF_TC.CefIpVersion_Enum>`
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ceffibsummaryfwdprefixes
            
            	Total number of forwarding Prefixes in FIB for the IP version specified by cefFIBIpVersion object
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-cef-mib'
            _revision = '2006-01-30'

            def __init__(self):
                self.parent = None
                self.ceffibipversion = None
                self.entphysicalindex = None
                self.ceffibsummaryfwdprefixes = None

            @property
            def _common_path(self):
                if self.ceffibipversion is None:
                    raise YPYDataValidationError('Key property ceffibipversion is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefFIBSummaryTable/CISCO-CEF-MIB:cefFIBSummaryEntry[CISCO-CEF-MIB:cefFIBIpVersion = ' + str(self.ceffibipversion) + '][CISCO-CEF-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ceffibipversion is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.ceffibsummaryfwdprefixes is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                return meta._meta_table['CISCOCEFMIB.CefFIBSummaryTable.CefFIBSummaryEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefFIBSummaryTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ceffibsummaryentry is not None:
                for child_ref in self.ceffibsummaryentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefFIBSummaryTable']['meta_info']


    class CefInconsistencyRecordTable(object):
        """
        This table contains CEF inconsistency
        records.
        
        .. attribute:: cefinconsistencyrecordentry
        
        	If the managed device supports CEF, each entry contains the inconsistency  record
        	**type**\: list of :py:class:`CefInconsistencyRecordEntry <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefInconsistencyRecordTable.CefInconsistencyRecordEntry>`
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.cefinconsistencyrecordentry = YList()
            self.cefinconsistencyrecordentry.parent = self
            self.cefinconsistencyrecordentry.name = 'cefinconsistencyrecordentry'


        class CefInconsistencyRecordEntry(object):
            """
            If the managed device supports CEF,
            each entry contains the inconsistency 
            record.
            
            .. attribute:: ceffibipversion
            
            	
            	**type**\: :py:class:`CefIpVersion_Enum <ydk.models.cef.CISCO_CEF_TC.CefIpVersion_Enum>`
            
            .. attribute:: cefinconsistencyrecid
            
            	The locally arbitrary, but unique identifier associated with this inconsistency record entry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefinconsistencycctype
            
            	The type of consistency checker who generated this inconsistency record
            	**type**\: :py:class:`CefCCType_Enum <ydk.models.cef.CISCO_CEF_TC.CefCCType_Enum>`
            
            .. attribute:: cefinconsistencyentity
            
            	The entity for which this inconsistency record was  generated. The value of this object will be  irrelevant and will be set to 0 when the inconsisency  record is applicable for all the entities
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cefinconsistencyprefixaddr
            
            	The network prefix address associated with this  inconsistency record.  The type of this address is determined by the value of the cefInconsistencyPrefixType object
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cefinconsistencyprefixlen
            
            	Length in bits of the inconsistency address prefix
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: cefinconsistencyprefixtype
            
            	The network prefix type associated with this inconsistency record
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: cefinconsistencyreason
            
            	The reason for generating this inconsistency record.   missing(1)\:        the prefix is missing  checksumErr(2)\:    checksum error was found  unknown(3)\:        reason is unknown
            	**type**\: :py:class:`CefInconsistencyReason_Enum <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefInconsistencyRecordTable.CefInconsistencyRecordEntry.CefInconsistencyReason_Enum>`
            
            .. attribute:: cefinconsistencyvrfname
            
            	Vrf name associated with this inconsistency record
            	**type**\: str
            
            	**range:** 0..31
            
            

            """

            _prefix = 'cisco-cef-mib'
            _revision = '2006-01-30'

            def __init__(self):
                self.parent = None
                self.ceffibipversion = None
                self.cefinconsistencyrecid = None
                self.cefinconsistencycctype = None
                self.cefinconsistencyentity = None
                self.cefinconsistencyprefixaddr = None
                self.cefinconsistencyprefixlen = None
                self.cefinconsistencyprefixtype = None
                self.cefinconsistencyreason = None
                self.cefinconsistencyvrfname = None

            class CefInconsistencyReason_Enum(Enum):
                """
                CefInconsistencyReason_Enum

                The reason for generating this inconsistency record. 
                
                missing(1)\:        the prefix is missing
                
                checksumErr(2)\:    checksum error was found
                
                unknown(3)\:        reason is unknown

                """

                MISSING = 1

                CHECKSUMERR = 2

                UNKNOWN = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                    return meta._meta_table['CISCOCEFMIB.CefInconsistencyRecordTable.CefInconsistencyRecordEntry.CefInconsistencyReason_Enum']


            @property
            def _common_path(self):
                if self.ceffibipversion is None:
                    raise YPYDataValidationError('Key property ceffibipversion is None')
                if self.cefinconsistencyrecid is None:
                    raise YPYDataValidationError('Key property cefinconsistencyrecid is None')

                return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefInconsistencyRecordTable/CISCO-CEF-MIB:cefInconsistencyRecordEntry[CISCO-CEF-MIB:cefFIBIpVersion = ' + str(self.ceffibipversion) + '][CISCO-CEF-MIB:cefInconsistencyRecId = ' + str(self.cefinconsistencyrecid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ceffibipversion is not None:
                    return True

                if self.cefinconsistencyrecid is not None:
                    return True

                if self.cefinconsistencycctype is not None:
                    return True

                if self.cefinconsistencyentity is not None:
                    return True

                if self.cefinconsistencyprefixaddr is not None:
                    return True

                if self.cefinconsistencyprefixlen is not None:
                    return True

                if self.cefinconsistencyprefixtype is not None:
                    return True

                if self.cefinconsistencyreason is not None:
                    return True

                if self.cefinconsistencyvrfname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                return meta._meta_table['CISCOCEFMIB.CefInconsistencyRecordTable.CefInconsistencyRecordEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefInconsistencyRecordTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefinconsistencyrecordentry is not None:
                for child_ref in self.cefinconsistencyrecordentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefInconsistencyRecordTable']['meta_info']


    class CefIntTable(object):
        """
        This Table contains interface specific
        information of CEF on the Managed
        device.
        
        .. attribute:: cefintentry
        
        	If CEF is enabled on the Managed device,  each entry contains the CEF attributes  associated with an interface. The interface is instantiated by ifIndex.   Therefore, the interface index must have been assigned, according to the applicable procedures, before it can be meaningfully used. Generally, this means that the interface must exist.  A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of :py:class:`CefIntEntry <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefIntTable.CefIntEntry>`
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.cefintentry = YList()
            self.cefintentry.parent = self
            self.cefintentry.name = 'cefintentry'


        class CefIntEntry(object):
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
            
            .. attribute:: ceffibipversion
            
            	
            	**type**\: :py:class:`CefIpVersion_Enum <ydk.models.cef.CISCO_CEF_TC.CefIpVersion_Enum>`
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefintloadsharing
            
            	The status of load sharing on the interface.  perPacket(1) \: Router to send data packets                over successive equal\-cost paths                without regard to individual hosts                or user sessions.  perDestination(2) \: Router to use multiple, equal\-cost                     paths to achieve load sharing  Load sharing is enabled by default  for an interface when CEF is enabled
            	**type**\: :py:class:`CefIntLoadSharing_Enum <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefIntTable.CefIntEntry.CefIntLoadSharing_Enum>`
            
            .. attribute:: cefintnonrecursiveaccouting
            
            	The CEF accounting mode for the interface. CEF prefix based non\-recursive accounting  on an interface can be configured to store  the stats for non\-recursive prefixes in a internal  or external bucket.  internal(1)  \:  Count input traffic in the nonrecursive                 internal bucket  external(2)  \:  Count input traffic in the nonrecursive                 external bucket  The value of this object will only be effective if  value of the object cefAccountingMap is set to enable nonRecursive(1) accounting
            	**type**\: :py:class:`CefIntNonrecursiveAccouting_Enum <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefIntTable.CefIntEntry.CefIntNonrecursiveAccouting_Enum>`
            
            .. attribute:: cefintswitchingstate
            
            	The CEF switching State for the interface.  If CEF is enabled but distributed CEF(dCEF) is disabled then CEF is in cefEnabled(1) state.  If distributed CEF is enabled, then CEF is in  distCefEnabled(2) state. The cefDisabled(3) state indicates that CEF is disabled.  The CEF switching state is only applicable to the received packet on the interface
            	**type**\: :py:class:`CefIntSwitchingState_Enum <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefIntTable.CefIntEntry.CefIntSwitchingState_Enum>`
            
            

            """

            _prefix = 'cisco-cef-mib'
            _revision = '2006-01-30'

            def __init__(self):
                self.parent = None
                self.ceffibipversion = None
                self.entphysicalindex = None
                self.ifindex = None
                self.cefintloadsharing = None
                self.cefintnonrecursiveaccouting = None
                self.cefintswitchingstate = None

            class CefIntLoadSharing_Enum(Enum):
                """
                CefIntLoadSharing_Enum

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

                """

                PERPACKET = 1

                PERDESTINATION = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                    return meta._meta_table['CISCOCEFMIB.CefIntTable.CefIntEntry.CefIntLoadSharing_Enum']


            class CefIntNonrecursiveAccouting_Enum(Enum):
                """
                CefIntNonrecursiveAccouting_Enum

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

                """

                INTERNAL = 1

                EXTERNAL = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                    return meta._meta_table['CISCOCEFMIB.CefIntTable.CefIntEntry.CefIntNonrecursiveAccouting_Enum']


            class CefIntSwitchingState_Enum(Enum):
                """
                CefIntSwitchingState_Enum

                The CEF switching State for the interface. 
                If CEF is enabled but distributed CEF(dCEF) is
                disabled then CEF is in cefEnabled(1) state.
                
                If distributed CEF is enabled, then CEF is in 
                distCefEnabled(2) state. The cefDisabled(3) state
                indicates that CEF is disabled.
                
                The CEF switching state is only applicable to the
                received packet on the interface.

                """

                CEFENABLED = 1

                DISTCEFENABLED = 2

                CEFDISABLED = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                    return meta._meta_table['CISCOCEFMIB.CefIntTable.CefIntEntry.CefIntSwitchingState_Enum']


            @property
            def _common_path(self):
                if self.ceffibipversion is None:
                    raise YPYDataValidationError('Key property ceffibipversion is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')

                return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefIntTable/CISCO-CEF-MIB:cefIntEntry[CISCO-CEF-MIB:cefFIBIpVersion = ' + str(self.ceffibipversion) + '][CISCO-CEF-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + '][CISCO-CEF-MIB:ifIndex = ' + str(self.ifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ceffibipversion is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.ifindex is not None:
                    return True

                if self.cefintloadsharing is not None:
                    return True

                if self.cefintnonrecursiveaccouting is not None:
                    return True

                if self.cefintswitchingstate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                return meta._meta_table['CISCOCEFMIB.CefIntTable.CefIntEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefIntTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefintentry is not None:
                for child_ref in self.cefintentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefIntTable']['meta_info']


    class CefLMPrefixTable(object):
        """
        A table of Longest Match Prefix Query requests.
        
        Generator application should utilize the
        cefLMPrefixSpinLock to try to avoid collisions.
        See DESCRIPTION clause of cefLMPrefixSpinLock.
        
        .. attribute:: ceflmprefixentry
        
        	If CEF is enabled on the managed device, then each entry represents a longest Match Prefix request.  A management station wishing to get the longest Match prefix for a given destination address should create the associate instance of the row status. The row status should be set to active(1) to initiate the request. Note that  this entire procedure may be initiated via a  single set request which specifies a row status  of createAndGo(4).  Once the request completes, the management station  should retrieve the values of the objects of  interest, and should then delete the entry.  In order  to prevent old entries from clogging the table,  entries will be aged out, but an entry will never be  deleted within 5 minutes of completion. Entries are lost after an agent restart.  I.e. to find out the longest prefix match for  destination address of A.B.C.D on entity whose entityPhysicalIndex is 1, the Management station will create an entry in cefLMPrefixTable with cefLMPrefixRowStatus.1(entPhysicalIndex).1(ipv4).A.B.C.D set to createAndGo(4). Management Station may query the value of objects cefLMPrefix and cefLMPrefixLen to find out the corresponding prefix entry from the cefPrefixTable once the value of cefLMPrefixState is set to matchFound(2).  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of :py:class:`CefLMPrefixEntry <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefLMPrefixTable.CefLMPrefixEntry>`
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.ceflmprefixentry = YList()
            self.ceflmprefixentry.parent = self
            self.ceflmprefixentry.name = 'ceflmprefixentry'


        class CefLMPrefixEntry(object):
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
            
            .. attribute:: ceflmprefixdestaddr
            
            	The Destination Address. The type of this address is determined by the value of the cefLMPrefixDestAddrType object
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ceflmprefixdestaddrtype
            
            	The Destination Address Type. This object specifies the address type used for cefLMPrefixDestAddr.  Longest Match Prefix entries are only valid  for the address type of ipv4(1) and ipv6(2)
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ceflmprefixaddr
            
            	The Network Prefix Address. Index to the cefPrefixTable. The type of this address is determined by the value of the cefLMPrefixDestAddrType object
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ceflmprefixlen
            
            	The Network Prefix Length. Index to the cefPrefixTable
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: ceflmprefixrowstatus
            
            	The status of this table entry.  Once the entry  status is set to active(1), the associated entry  cannot be modified until the request completes (cefLMPrefixState transitions to matchFound(2)  or noMatchFound(3)).  Once the longest match request has been created (i.e. the cefLMPrefixRowStatus has been made active), the entry cannot be modified \- the only operation possible after this is to delete the row
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: ceflmprefixstate
            
            	Indicates the state of this prefix search request
            	**type**\: :py:class:`CefPrefixSearchState_Enum <ydk.models.cef.CISCO_CEF_TC.CefPrefixSearchState_Enum>`
            
            

            """

            _prefix = 'cisco-cef-mib'
            _revision = '2006-01-30'

            def __init__(self):
                self.parent = None
                self.ceflmprefixdestaddr = None
                self.ceflmprefixdestaddrtype = None
                self.entphysicalindex = None
                self.ceflmprefixaddr = None
                self.ceflmprefixlen = None
                self.ceflmprefixrowstatus = None
                self.ceflmprefixstate = None

            @property
            def _common_path(self):
                if self.ceflmprefixdestaddr is None:
                    raise YPYDataValidationError('Key property ceflmprefixdestaddr is None')
                if self.ceflmprefixdestaddrtype is None:
                    raise YPYDataValidationError('Key property ceflmprefixdestaddrtype is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefLMPrefixTable/CISCO-CEF-MIB:cefLMPrefixEntry[CISCO-CEF-MIB:cefLMPrefixDestAddr = ' + str(self.ceflmprefixdestaddr) + '][CISCO-CEF-MIB:cefLMPrefixDestAddrType = ' + str(self.ceflmprefixdestaddrtype) + '][CISCO-CEF-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ceflmprefixdestaddr is not None:
                    return True

                if self.ceflmprefixdestaddrtype is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.ceflmprefixaddr is not None:
                    return True

                if self.ceflmprefixlen is not None:
                    return True

                if self.ceflmprefixrowstatus is not None:
                    return True

                if self.ceflmprefixstate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                return meta._meta_table['CISCOCEFMIB.CefLMPrefixTable.CefLMPrefixEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefLMPrefixTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ceflmprefixentry is not None:
                for child_ref in self.ceflmprefixentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefLMPrefixTable']['meta_info']


    class CefNotifCntl(object):
        """
        
        
        .. attribute:: cefinconsistencynotifenable
        
        	Indicates whether cefInconsistencyDetection notification should be generated for this managed device
        	**type**\: bool
        
        .. attribute:: cefnotifthrottlinginterval
        
        	This object controls the generation of the cefInconsistencyDetection notification.  If this object has a value of zero, then the throttle control is disabled.  If this object has a non\-zero value, then the agent must not generate more than one  cefInconsistencyDetection 'notification\-event' in the  indicated period, where a 'notification\-event' is the transmission of a single trap or inform PDU to a list of notification destinations.  If additional inconsistency is detected within the  throttling period, then notification\-events for these inconsistencies should be suppressed by the agent until the current throttling period expires.  At the end of a throttling period, one notification\-event should be generated if any inconsistency was detected since the start of the  throttling period. In such a case,  another throttling period is started right away.  An NMS should periodically poll cefInconsistencyRecordTable to detect any missed cefInconsistencyDetection notification\-events, e.g., due to throttling or transmission loss.   If cefNotifThrottlingInterval notification generation is enabled, the suggested default throttling period is 60 seconds, but generation of the cefInconsistencyDetection notification should be disabled by default.  If the agent is capable of storing non\-volatile configuration, then the value of this object must be restored after a re\-initialization of the management system.  The actual transmission of notifications is controlled via the MIB modules in RFC 3413
        	**type**\: int
        
        	**range:** 0..3600
        
        .. attribute:: cefpeerfibstatechangenotifenable
        
        	Indicates whether or not a notification should be generated on the detection of CEF FIB peer state change
        	**type**\: bool
        
        .. attribute:: cefpeerstatechangenotifenable
        
        	Indicates whether or not a notification should be generated on the detection of CEF peer state change
        	**type**\: bool
        
        .. attribute:: cefresourcefailurenotifenable
        
        	Indicates whether or not a notification should be generated on the detection of CEF resource Failure
        	**type**\: bool
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.cefinconsistencynotifenable = None
            self.cefnotifthrottlinginterval = None
            self.cefpeerfibstatechangenotifenable = None
            self.cefpeerstatechangenotifenable = None
            self.cefresourcefailurenotifenable = None

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefNotifCntl'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefinconsistencynotifenable is not None:
                return True

            if self.cefnotifthrottlinginterval is not None:
                return True

            if self.cefpeerfibstatechangenotifenable is not None:
                return True

            if self.cefpeerstatechangenotifenable is not None:
                return True

            if self.cefresourcefailurenotifenable is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefNotifCntl']['meta_info']


    class CefPathTable(object):
        """
        CEF prefix path is a valid route to reach to a 
        destination IP prefix. Multiple paths may exist 
        out of a router to the same destination prefix. 
        This table specify lists of CEF paths.
        
        .. attribute:: cefpathentry
        
        	If CEF is enabled on the Managed device, each entry contain a CEF prefix path.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of :py:class:`CefPathEntry <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefPathTable.CefPathEntry>`
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.cefpathentry = YList()
            self.cefpathentry.parent = self
            self.cefpathentry.name = 'cefpathentry'


        class CefPathEntry(object):
            """
            If CEF is enabled on the Managed device,
            each entry contain a CEF prefix path.
            
            entPhysicalIndex is also an index for this
            table which represents entities of
            'module' entPhysicalClass which are capable
            of running CEF.
            
            .. attribute:: cefpathid
            
            	The locally arbitrary, but unique identifier associated with this prefix path entry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefprefixaddr
            
            	
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cefprefixlen
            
            	
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: cefprefixtype
            
            	
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefpathinterface
            
            	Interface associated with this CEF path.  A value of zero for this object will indicate that no interface is associated with this path  entry
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: cefpathnexthopaddr
            
            	Next hop address associated with this CEF path.  The value of this object is only relevant for attached next hop and recursive next hop   path types (when the object cefPathType is set to attachedNexthop(4) or recursiveNexthop(5)). and will be set to zero for other path types.  The type of this address is determined by the value of the cefPrefixType object
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cefpathrecursevrfname
            
            	The recursive vrf name associated with this path.  The value of this object is only relevant for recursive next hop path types (when the  object cefPathType is set to recursiveNexthop(5)), and '0x00' will be returned for other path types
            	**type**\: str
            
            	**range:** 0..31
            
            .. attribute:: cefpathtype
            
            	Type for this CEF Path
            	**type**\: :py:class:`CefPathType_Enum <ydk.models.cef.CISCO_CEF_TC.CefPathType_Enum>`
            
            

            """

            _prefix = 'cisco-cef-mib'
            _revision = '2006-01-30'

            def __init__(self):
                self.parent = None
                self.cefpathid = None
                self.cefprefixaddr = None
                self.cefprefixlen = None
                self.cefprefixtype = None
                self.entphysicalindex = None
                self.cefpathinterface = None
                self.cefpathnexthopaddr = None
                self.cefpathrecursevrfname = None
                self.cefpathtype = None

            @property
            def _common_path(self):
                if self.cefpathid is None:
                    raise YPYDataValidationError('Key property cefpathid is None')
                if self.cefprefixaddr is None:
                    raise YPYDataValidationError('Key property cefprefixaddr is None')
                if self.cefprefixlen is None:
                    raise YPYDataValidationError('Key property cefprefixlen is None')
                if self.cefprefixtype is None:
                    raise YPYDataValidationError('Key property cefprefixtype is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefPathTable/CISCO-CEF-MIB:cefPathEntry[CISCO-CEF-MIB:cefPathId = ' + str(self.cefpathid) + '][CISCO-CEF-MIB:cefPrefixAddr = ' + str(self.cefprefixaddr) + '][CISCO-CEF-MIB:cefPrefixLen = ' + str(self.cefprefixlen) + '][CISCO-CEF-MIB:cefPrefixType = ' + str(self.cefprefixtype) + '][CISCO-CEF-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cefpathid is not None:
                    return True

                if self.cefprefixaddr is not None:
                    return True

                if self.cefprefixlen is not None:
                    return True

                if self.cefprefixtype is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.cefpathinterface is not None:
                    return True

                if self.cefpathnexthopaddr is not None:
                    return True

                if self.cefpathrecursevrfname is not None:
                    return True

                if self.cefpathtype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                return meta._meta_table['CISCOCEFMIB.CefPathTable.CefPathEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefPathTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefpathentry is not None:
                for child_ref in self.cefpathentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefPathTable']['meta_info']


    class CefPeerFIBTable(object):
        """
        Entity acting as RP (Routing Processor) keep
        the CEF FIB states for the line card entities and
        communicate with the line card entities using
        XDR. This Table contains the CEF FIB State 
        related to peer entities on the managed device.
        
        .. attribute:: cefpeerfibentry
        
        	If CEF is enabled on the Managed device, each entry contains the CEF FIB State  associated a CEF peer entity.  entPhysicalIndex and entPeerPhysicalIndex are also indexes for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of :py:class:`CefPeerFIBEntry <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefPeerFIBTable.CefPeerFIBEntry>`
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.cefpeerfibentry = YList()
            self.cefpeerfibentry.parent = self
            self.cefpeerfibentry.name = 'cefpeerfibentry'


        class CefPeerFIBEntry(object):
            """
            If CEF is enabled on the Managed device,
            each entry contains the CEF FIB State 
            associated a CEF peer entity.
            
            entPhysicalIndex and entPeerPhysicalIndex are
            also indexes for this table which represents
            entities of 'module' entPhysicalClass which are
            capable of running CEF.
            
            .. attribute:: ceffibipversion
            
            	
            	**type**\: :py:class:`CefIpVersion_Enum <ydk.models.cef.CISCO_CEF_TC.CefIpVersion_Enum>`
            
            .. attribute:: entpeerphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefpeerfiboperstate
            
            	The current CEF FIB Operational State for the  CEF peer entity
            	**type**\: :py:class:`CefPeerFIBOperState_Enum <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefPeerFIBTable.CefPeerFIBEntry.CefPeerFIBOperState_Enum>`
            
            

            """

            _prefix = 'cisco-cef-mib'
            _revision = '2006-01-30'

            def __init__(self):
                self.parent = None
                self.ceffibipversion = None
                self.entpeerphysicalindex = None
                self.entphysicalindex = None
                self.cefpeerfiboperstate = None

            class CefPeerFIBOperState_Enum(Enum):
                """
                CefPeerFIBOperState_Enum

                The current CEF FIB Operational State for the 
                CEF peer entity.

                """

                PEERFIBDOWN = 1

                PEERFIBUP = 2

                PEERFIBRELOADREQUEST = 3

                PEERFIBRELOADING = 4

                PEERFIBSYNCED = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                    return meta._meta_table['CISCOCEFMIB.CefPeerFIBTable.CefPeerFIBEntry.CefPeerFIBOperState_Enum']


            @property
            def _common_path(self):
                if self.ceffibipversion is None:
                    raise YPYDataValidationError('Key property ceffibipversion is None')
                if self.entpeerphysicalindex is None:
                    raise YPYDataValidationError('Key property entpeerphysicalindex is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefPeerFIBTable/CISCO-CEF-MIB:cefPeerFIBEntry[CISCO-CEF-MIB:cefFIBIpVersion = ' + str(self.ceffibipversion) + '][CISCO-CEF-MIB:entPeerPhysicalIndex = ' + str(self.entpeerphysicalindex) + '][CISCO-CEF-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ceffibipversion is not None:
                    return True

                if self.entpeerphysicalindex is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.cefpeerfiboperstate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                return meta._meta_table['CISCOCEFMIB.CefPeerFIBTable.CefPeerFIBEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefPeerFIBTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefpeerfibentry is not None:
                for child_ref in self.cefpeerfibentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefPeerFIBTable']['meta_info']


    class CefPeerTable(object):
        """
        Entity acting as RP (Routing Processor) keeps
        the CEF states for the line card entities and
        communicates with the line card entities using
        XDR. This Table contains the CEF information 
        related to peer entities on the managed device.
        
        .. attribute:: cefpeerentry
        
        	If CEF is enabled on the Managed device, each entry contains the CEF related attributes  associated with a CEF peer entity.  entPhysicalIndex and entPeerPhysicalIndex are also indexes for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of :py:class:`CefPeerEntry <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefPeerTable.CefPeerEntry>`
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.cefpeerentry = YList()
            self.cefpeerentry.parent = self
            self.cefpeerentry.name = 'cefpeerentry'


        class CefPeerEntry(object):
            """
            If CEF is enabled on the Managed device,
            each entry contains the CEF related attributes 
            associated with a CEF peer entity.
            
            entPhysicalIndex and entPeerPhysicalIndex are
            also indexes for this table which represents
            entities of 'module' entPhysicalClass which are
            capable of running CEF.
            
            .. attribute:: entpeerphysicalindex
            
            	The entity index for the CEF peer entity. Only the entities of 'module'  entPhysicalClass are included here
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefpeernumberofresets
            
            	Number of times the session with CEF peer entity  has been reset
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefpeeroperstate
            
            	The current CEF operational state of the CEF peer entity.  Cef peer entity oper state will be peerDisabled(1) in  the following condition\:     \: Cef Peer entity encounters fatal error i.e. resource      allocation failure, ipc failure etc     \: When a reload/delete request is received from the Cef       Peer Entity  Once the peer entity is up and no fatal error is encountered, then the value of this object will transits to the peerUp(3)  state.  If the Cef Peer entity is in held stage, then the value of this object will be peerHold(3). Cef peer entity can only transit to peerDisabled(1) state from the peerHold(3) state
            	**type**\: :py:class:`CefPeerOperState_Enum <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefPeerTable.CefPeerEntry.CefPeerOperState_Enum>`
            
            

            """

            _prefix = 'cisco-cef-mib'
            _revision = '2006-01-30'

            def __init__(self):
                self.parent = None
                self.entpeerphysicalindex = None
                self.entphysicalindex = None
                self.cefpeernumberofresets = None
                self.cefpeeroperstate = None

            class CefPeerOperState_Enum(Enum):
                """
                CefPeerOperState_Enum

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

                """

                PEERDISABLED = 1

                PEERUP = 2

                PEERHOLD = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                    return meta._meta_table['CISCOCEFMIB.CefPeerTable.CefPeerEntry.CefPeerOperState_Enum']


            @property
            def _common_path(self):
                if self.entpeerphysicalindex is None:
                    raise YPYDataValidationError('Key property entpeerphysicalindex is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefPeerTable/CISCO-CEF-MIB:cefPeerEntry[CISCO-CEF-MIB:entPeerPhysicalIndex = ' + str(self.entpeerphysicalindex) + '][CISCO-CEF-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.entpeerphysicalindex is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.cefpeernumberofresets is not None:
                    return True

                if self.cefpeeroperstate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                return meta._meta_table['CISCOCEFMIB.CefPeerTable.CefPeerEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefPeerTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefpeerentry is not None:
                for child_ref in self.cefpeerentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefPeerTable']['meta_info']


    class CefPrefixTable(object):
        """
        A list of CEF forwarding prefixes.
        
        .. attribute:: cefprefixentry
        
        	If CEF is enabled on the Managed device, each entry contains the forwarding  prefix attributes.   CEF prefix based non\-recursive stats are maintained in internal and external buckets (depending upon the  value of cefIntNonrecursiveAccouting object in the  CefIntEntry).  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of :py:class:`CefPrefixEntry <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefPrefixTable.CefPrefixEntry>`
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.cefprefixentry = YList()
            self.cefprefixentry.parent = self
            self.cefprefixentry.name = 'cefprefixentry'


        class CefPrefixEntry(object):
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
            
            .. attribute:: cefprefixaddr
            
            	The Network Prefix Address. The type of this address is determined by the value of the cefPrefixType object. This object is a Prefix Address containing the  prefix with length specified by cefPrefixLen.  Any bits beyond the length specified by cefPrefixLen are zeroed
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cefprefixlen
            
            	Length in bits of the FIB Address prefix
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: cefprefixtype
            
            	The Network Prefix Type. This object specifies the address type used for cefPrefixAddr.  Prefix entries are only valid for the address type of ipv4(1) and ipv6(2)
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefprefixbytes
            
            	If CEF accounting is set to enable per prefix accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'perPrefix'  accounting), then this object represents the  number of bytes switched to this prefix
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefprefixexternalnrbytes
            
            	If CEF accounting is set to enable nonRecursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents  the number of non\-recursive bytes in the external bucket switched using this prefix
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefprefixexternalnrhcbytes
            
            	If CEF accounting is set to enable nonRecursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents  the number of non\-recursive bytes in the external bucket switched using this prefix.  This object is a 64\-bit version of  cefPrefixExternalNRBytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefprefixexternalnrhcpkts
            
            	If CEF accounting is set to enable non\-recursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents the number of non\-recursive packets in the external bucket switched using this prefix.  This object is a 64\-bit version of  cefPrefixExternalNRPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefprefixexternalnrpkts
            
            	If CEF accounting is set to enable non\-recursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents the number of non\-recursive packets in the external bucket switched using this prefix
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefprefixforwardinginfo
            
            	This object indicates the associated forwarding element selection entries in cefFESelectionTable. The value of this object is index value (cefFESelectionName) of cefFESelectionTable
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cefprefixhcbytes
            
            	If CEF accounting is set to enable per prefix accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'perPrefix'  accounting), then this object represents the  number of bytes switched to this prefix.  This object is a 64\-bit version of  cefPrefixBytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefprefixhcpkts
            
            	If CEF accounting is set to enable per prefix accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'perPrefix'  accounting), then this object represents the  number of packets switched to this prefix.   This object is a 64\-bit version of  cefPrefixPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefprefixinternalnrbytes
            
            	If CEF accounting is set to enable nonRecursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents  the number of non\-recursive bytes in the internal bucket switched using this prefix
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefprefixinternalnrhcbytes
            
            	If CEF accounting is set to enable nonRecursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents  the number of non\-recursive bytes in the internal bucket switched using this prefix.  This object is a 64\-bit version of  cefPrefixInternalNRBytes
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefprefixinternalnrhcpkts
            
            	If CEF accounting is set to enable non\-recursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents the number of non\-recursive packets in the internal bucket switched using this prefix.  This object is a 64\-bit version of  cefPrefixInternalNRPkts
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefprefixinternalnrpkts
            
            	If CEF accounting is set to enable non\-recursive accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'nonRecursive'  accounting), then this object represents the number of non\-recursive packets in the internal bucket switched using this prefix
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefprefixpkts
            
            	If CEF accounting is set to enable per prefix accounting (value of cefCfgAccountingMap object in  the cefCfgEntry is set to enable 'perPrefix'  accounting), then this object represents the  number of packets switched to this prefix
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-cef-mib'
            _revision = '2006-01-30'

            def __init__(self):
                self.parent = None
                self.cefprefixaddr = None
                self.cefprefixlen = None
                self.cefprefixtype = None
                self.entphysicalindex = None
                self.cefprefixbytes = None
                self.cefprefixexternalnrbytes = None
                self.cefprefixexternalnrhcbytes = None
                self.cefprefixexternalnrhcpkts = None
                self.cefprefixexternalnrpkts = None
                self.cefprefixforwardinginfo = None
                self.cefprefixhcbytes = None
                self.cefprefixhcpkts = None
                self.cefprefixinternalnrbytes = None
                self.cefprefixinternalnrhcbytes = None
                self.cefprefixinternalnrhcpkts = None
                self.cefprefixinternalnrpkts = None
                self.cefprefixpkts = None

            @property
            def _common_path(self):
                if self.cefprefixaddr is None:
                    raise YPYDataValidationError('Key property cefprefixaddr is None')
                if self.cefprefixlen is None:
                    raise YPYDataValidationError('Key property cefprefixlen is None')
                if self.cefprefixtype is None:
                    raise YPYDataValidationError('Key property cefprefixtype is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefPrefixTable/CISCO-CEF-MIB:cefPrefixEntry[CISCO-CEF-MIB:cefPrefixAddr = ' + str(self.cefprefixaddr) + '][CISCO-CEF-MIB:cefPrefixLen = ' + str(self.cefprefixlen) + '][CISCO-CEF-MIB:cefPrefixType = ' + str(self.cefprefixtype) + '][CISCO-CEF-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cefprefixaddr is not None:
                    return True

                if self.cefprefixlen is not None:
                    return True

                if self.cefprefixtype is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.cefprefixbytes is not None:
                    return True

                if self.cefprefixexternalnrbytes is not None:
                    return True

                if self.cefprefixexternalnrhcbytes is not None:
                    return True

                if self.cefprefixexternalnrhcpkts is not None:
                    return True

                if self.cefprefixexternalnrpkts is not None:
                    return True

                if self.cefprefixforwardinginfo is not None:
                    return True

                if self.cefprefixhcbytes is not None:
                    return True

                if self.cefprefixhcpkts is not None:
                    return True

                if self.cefprefixinternalnrbytes is not None:
                    return True

                if self.cefprefixinternalnrhcbytes is not None:
                    return True

                if self.cefprefixinternalnrhcpkts is not None:
                    return True

                if self.cefprefixinternalnrpkts is not None:
                    return True

                if self.cefprefixpkts is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                return meta._meta_table['CISCOCEFMIB.CefPrefixTable.CefPrefixEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefPrefixTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefprefixentry is not None:
                for child_ref in self.cefprefixentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefPrefixTable']['meta_info']


    class CefResourceTable(object):
        """
        This table contains global resource 
        information of CEF on the Managed device.
        
        .. attribute:: cefresourceentry
        
        	If the Managed device supports CEF, each entry contains the CEF Resource  parameters for the managed entity.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of :py:class:`CefResourceEntry <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefResourceTable.CefResourceEntry>`
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.cefresourceentry = YList()
            self.cefresourceentry.parent = self
            self.cefresourceentry.name = 'cefresourceentry'


        class CefResourceEntry(object):
            """
            If the Managed device supports CEF,
            each entry contains the CEF Resource 
            parameters for the managed entity.
            
            entPhysicalIndex is also an index for this
            table which represents entities of
            'module' entPhysicalClass which are capable
            of running CEF.
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefresourcefailurereason
            
            	The CEF resource failure reason which may lead to CEF being disabled on the managed entity
            	**type**\: :py:class:`CefFailureReason_Enum <ydk.models.cef.CISCO_CEF_TC.CefFailureReason_Enum>`
            
            .. attribute:: cefresourcememoryused
            
            	Indicates the number of bytes from the Processor Memory Pool that are currently in use by CEF on the managed entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-cef-mib'
            _revision = '2006-01-30'

            def __init__(self):
                self.parent = None
                self.entphysicalindex = None
                self.cefresourcefailurereason = None
                self.cefresourcememoryused = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefResourceTable/CISCO-CEF-MIB:cefResourceEntry[CISCO-CEF-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

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

                if self.cefresourcefailurereason is not None:
                    return True

                if self.cefresourcememoryused is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                return meta._meta_table['CISCOCEFMIB.CefResourceTable.CefResourceEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefResourceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefresourceentry is not None:
                for child_ref in self.cefresourceentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefResourceTable']['meta_info']


    class CefStatsPrefixLenTable(object):
        """
        This table specifies the CEF stats based
        on the Prefix Length.
        
        .. attribute:: cefstatsprefixlenentry
        
        	If CEF is enabled on the Managed device and if CEF accounting is set to enable  prefix length based accounting (value of  cefCfgAccountingMap object in the  cefCfgEntry is set to enable 'prefixLength'  accounting), each entry contains the traffic  statistics for a prefix length. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of :py:class:`CefStatsPrefixLenEntry <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefStatsPrefixLenTable.CefStatsPrefixLenEntry>`
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.cefstatsprefixlenentry = YList()
            self.cefstatsprefixlenentry.parent = self
            self.cefstatsprefixlenentry.name = 'cefstatsprefixlenentry'


        class CefStatsPrefixLenEntry(object):
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
            
            .. attribute:: ceffibipversion
            
            	
            	**type**\: :py:class:`CefIpVersion_Enum <ydk.models.cef.CISCO_CEF_TC.CefIpVersion_Enum>`
            
            .. attribute:: cefstatsprefixlen
            
            	Length in bits of the Destination IP prefix. As 0.0.0.0/0 is a valid prefix, hence  0 is a valid prefix length
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefstatsprefixdeletes
            
            	Number of delete operations performed to the FIB  database for the specified IP prefix length
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefstatsprefixelements
            
            	Total number of elements in the FIB database for the specified IP prefix length
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefstatsprefixhcdeletes
            
            	Number of delete operations performed to the FIB  database for the specified IP prefix length. This object is a 64\-bit version of  cefStatsPrefixDelete
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefstatsprefixhcelements
            
            	Total number of elements in the FIB database for the specified IP prefix length. This object is a 64\-bit version of  cefStatsPrefixElements
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefstatsprefixhcinserts
            
            	Number of insert operations performed to the FIB  database for the specified IP prefix length. This object is a 64\-bit version of  cefStatsPrefixInsert
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefstatsprefixhcqueries
            
            	Number of queries received in the FIB database for the specified IP prefix length. This object is a 64\-bit version of  cefStatsPrefixQueries
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefstatsprefixinserts
            
            	Number of insert operations performed to the FIB  database for the specified IP prefix length
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefstatsprefixqueries
            
            	Number of queries received in the FIB database  for the specified IP prefix length
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-cef-mib'
            _revision = '2006-01-30'

            def __init__(self):
                self.parent = None
                self.ceffibipversion = None
                self.cefstatsprefixlen = None
                self.entphysicalindex = None
                self.cefstatsprefixdeletes = None
                self.cefstatsprefixelements = None
                self.cefstatsprefixhcdeletes = None
                self.cefstatsprefixhcelements = None
                self.cefstatsprefixhcinserts = None
                self.cefstatsprefixhcqueries = None
                self.cefstatsprefixinserts = None
                self.cefstatsprefixqueries = None

            @property
            def _common_path(self):
                if self.ceffibipversion is None:
                    raise YPYDataValidationError('Key property ceffibipversion is None')
                if self.cefstatsprefixlen is None:
                    raise YPYDataValidationError('Key property cefstatsprefixlen is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefStatsPrefixLenTable/CISCO-CEF-MIB:cefStatsPrefixLenEntry[CISCO-CEF-MIB:cefFIBIpVersion = ' + str(self.ceffibipversion) + '][CISCO-CEF-MIB:cefStatsPrefixLen = ' + str(self.cefstatsprefixlen) + '][CISCO-CEF-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ceffibipversion is not None:
                    return True

                if self.cefstatsprefixlen is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.cefstatsprefixdeletes is not None:
                    return True

                if self.cefstatsprefixelements is not None:
                    return True

                if self.cefstatsprefixhcdeletes is not None:
                    return True

                if self.cefstatsprefixhcelements is not None:
                    return True

                if self.cefstatsprefixhcinserts is not None:
                    return True

                if self.cefstatsprefixhcqueries is not None:
                    return True

                if self.cefstatsprefixinserts is not None:
                    return True

                if self.cefstatsprefixqueries is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                return meta._meta_table['CISCOCEFMIB.CefStatsPrefixLenTable.CefStatsPrefixLenEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefStatsPrefixLenTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefstatsprefixlenentry is not None:
                for child_ref in self.cefstatsprefixlenentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefStatsPrefixLenTable']['meta_info']


    class CefSwitchingStatsTable(object):
        """
        This table specifies the CEF switch stats.
        
        .. attribute:: cefswitchingstatsentry
        
        	If CEF is enabled on the Managed device, each entry specifies the switching stats. A row may exist for each IP version type (v4 and v6) depending upon the IP version supported on the device.  entPhysicalIndex is also an index for this table which represents entities of 'module' entPhysicalClass which are capable of running CEF
        	**type**\: list of :py:class:`CefSwitchingStatsEntry <ydk.models.cef.CISCO_CEF_MIB.CISCOCEFMIB.CefSwitchingStatsTable.CefSwitchingStatsEntry>`
        
        

        """

        _prefix = 'cisco-cef-mib'
        _revision = '2006-01-30'

        def __init__(self):
            self.parent = None
            self.cefswitchingstatsentry = YList()
            self.cefswitchingstatsentry.parent = self
            self.cefswitchingstatsentry.name = 'cefswitchingstatsentry'


        class CefSwitchingStatsEntry(object):
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
            
            .. attribute:: ceffibipversion
            
            	
            	**type**\: :py:class:`CefIpVersion_Enum <ydk.models.cef.CISCO_CEF_TC.CefIpVersion_Enum>`
            
            .. attribute:: cefswitchingindex
            
            	The locally arbitrary, but unique identifier associated with this switching stats entry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: entphysicalindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cefswitchingdrop
            
            	Number of packets dropped by CEF
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefswitchinghcdrop
            
            	Number of packets dropped by CEF. This object is a 64\-bit version of cefSwitchingDrop
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefswitchinghcpunt
            
            	Number of packets that could not be switched in the normal path and were punted to the next\-fastest switching vector. This object is a 64\-bit version of cefSwitchingPunt
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefswitchinghcpunt2host
            
            	Number of packets that could not be switched in the normal path and were punted to the host (process switching path).  For most of the switching paths, the value of this object may be similar to cefSwitchingPunt. This object is a 64\-bit version of cefSwitchingPunt2Host
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cefswitchingpath
            
            	Switch path where the feature was executed. Available switch paths are platform\-dependent. Following are the examples of switching paths\:     RIB \: switching with CEF assistance     Low\-end switching (LES) \: CEF switch path     PAS \: CEF turbo switch path
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: cefswitchingpunt
            
            	Number of packets that could not be switched in the normal path and were punted to the next\-fastest switching vector
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cefswitchingpunt2host
            
            	Number of packets that could not be switched in the normal path and were punted to the host (process switching path).  For most of the switching paths, the value of this object may be similar to cefSwitchingPunt
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-cef-mib'
            _revision = '2006-01-30'

            def __init__(self):
                self.parent = None
                self.ceffibipversion = None
                self.cefswitchingindex = None
                self.entphysicalindex = None
                self.cefswitchingdrop = None
                self.cefswitchinghcdrop = None
                self.cefswitchinghcpunt = None
                self.cefswitchinghcpunt2host = None
                self.cefswitchingpath = None
                self.cefswitchingpunt = None
                self.cefswitchingpunt2host = None

            @property
            def _common_path(self):
                if self.ceffibipversion is None:
                    raise YPYDataValidationError('Key property ceffibipversion is None')
                if self.cefswitchingindex is None:
                    raise YPYDataValidationError('Key property cefswitchingindex is None')
                if self.entphysicalindex is None:
                    raise YPYDataValidationError('Key property entphysicalindex is None')

                return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefSwitchingStatsTable/CISCO-CEF-MIB:cefSwitchingStatsEntry[CISCO-CEF-MIB:cefFIBIpVersion = ' + str(self.ceffibipversion) + '][CISCO-CEF-MIB:cefSwitchingIndex = ' + str(self.cefswitchingindex) + '][CISCO-CEF-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ceffibipversion is not None:
                    return True

                if self.cefswitchingindex is not None:
                    return True

                if self.entphysicalindex is not None:
                    return True

                if self.cefswitchingdrop is not None:
                    return True

                if self.cefswitchinghcdrop is not None:
                    return True

                if self.cefswitchinghcpunt is not None:
                    return True

                if self.cefswitchinghcpunt2host is not None:
                    return True

                if self.cefswitchingpath is not None:
                    return True

                if self.cefswitchingpunt is not None:
                    return True

                if self.cefswitchingpunt2host is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
                return meta._meta_table['CISCOCEFMIB.CefSwitchingStatsTable.CefSwitchingStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-CEF-MIB:CISCO-CEF-MIB/CISCO-CEF-MIB:cefSwitchingStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cefswitchingstatsentry is not None:
                for child_ref in self.cefswitchingstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
            return meta._meta_table['CISCOCEFMIB.CefSwitchingStatsTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-CEF-MIB:CISCO-CEF-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cefadjsummarytable is not None and self.cefadjsummarytable._has_data():
            return True

        if self.cefadjsummarytable is not None and self.cefadjsummarytable.is_presence():
            return True

        if self.cefadjtable is not None and self.cefadjtable._has_data():
            return True

        if self.cefadjtable is not None and self.cefadjtable.is_presence():
            return True

        if self.cefcc is not None and self.cefcc._has_data():
            return True

        if self.cefcc is not None and self.cefcc.is_presence():
            return True

        if self.cefccglobaltable is not None and self.cefccglobaltable._has_data():
            return True

        if self.cefccglobaltable is not None and self.cefccglobaltable.is_presence():
            return True

        if self.cefcctypetable is not None and self.cefcctypetable._has_data():
            return True

        if self.cefcctypetable is not None and self.cefcctypetable.is_presence():
            return True

        if self.cefcfgtable is not None and self.cefcfgtable._has_data():
            return True

        if self.cefcfgtable is not None and self.cefcfgtable.is_presence():
            return True

        if self.ceffeselectiontable is not None and self.ceffeselectiontable._has_data():
            return True

        if self.ceffeselectiontable is not None and self.ceffeselectiontable.is_presence():
            return True

        if self.ceffib is not None and self.ceffib._has_data():
            return True

        if self.ceffib is not None and self.ceffib.is_presence():
            return True

        if self.ceffibsummarytable is not None and self.ceffibsummarytable._has_data():
            return True

        if self.ceffibsummarytable is not None and self.ceffibsummarytable.is_presence():
            return True

        if self.cefinconsistencyrecordtable is not None and self.cefinconsistencyrecordtable._has_data():
            return True

        if self.cefinconsistencyrecordtable is not None and self.cefinconsistencyrecordtable.is_presence():
            return True

        if self.cefinttable is not None and self.cefinttable._has_data():
            return True

        if self.cefinttable is not None and self.cefinttable.is_presence():
            return True

        if self.ceflmprefixtable is not None and self.ceflmprefixtable._has_data():
            return True

        if self.ceflmprefixtable is not None and self.ceflmprefixtable.is_presence():
            return True

        if self.cefnotifcntl is not None and self.cefnotifcntl._has_data():
            return True

        if self.cefnotifcntl is not None and self.cefnotifcntl.is_presence():
            return True

        if self.cefpathtable is not None and self.cefpathtable._has_data():
            return True

        if self.cefpathtable is not None and self.cefpathtable.is_presence():
            return True

        if self.cefpeerfibtable is not None and self.cefpeerfibtable._has_data():
            return True

        if self.cefpeerfibtable is not None and self.cefpeerfibtable.is_presence():
            return True

        if self.cefpeertable is not None and self.cefpeertable._has_data():
            return True

        if self.cefpeertable is not None and self.cefpeertable.is_presence():
            return True

        if self.cefprefixtable is not None and self.cefprefixtable._has_data():
            return True

        if self.cefprefixtable is not None and self.cefprefixtable.is_presence():
            return True

        if self.cefresourcetable is not None and self.cefresourcetable._has_data():
            return True

        if self.cefresourcetable is not None and self.cefresourcetable.is_presence():
            return True

        if self.cefstatsprefixlentable is not None and self.cefstatsprefixlentable._has_data():
            return True

        if self.cefstatsprefixlentable is not None and self.cefstatsprefixlentable.is_presence():
            return True

        if self.cefswitchingstatstable is not None and self.cefswitchingstatstable._has_data():
            return True

        if self.cefswitchingstatstable is not None and self.cefswitchingstatstable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cef._meta import _CISCO_CEF_MIB as meta
        return meta._meta_table['CISCOCEFMIB']['meta_info']


