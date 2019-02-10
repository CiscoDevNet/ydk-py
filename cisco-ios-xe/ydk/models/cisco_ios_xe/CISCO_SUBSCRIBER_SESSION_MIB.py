""" CISCO_SUBSCRIBER_SESSION_MIB 

This MIB defines objects describing subscriber sessions, or
more specifically, subscriber sessions terminated by a RAS.  A
subscriber session consists of the traffic between a CPE and a
NAS, as illustrated in the diagram below.

                                   Service
                   Access          Provider
                   Network         Network
+\-\-+  +\-\-\-+  +\-\-+   {   }   +\-\-\-+   {   }
\|PC+\-\-+CPE+\-\-+AN+\-\-{     }\-\-+NAS+\-\-{     }
+\-\-+  +\-\-\-+  +\-\-+   {   }   +\-\-\-+   {   }
          \|                 \|
          \|<\-\-\-\-\-\-\-\-\-\-\-\-\-\-\->\|
               subscriber
                session

A subscriber session behaves according to the FSM illustrated
below.

      +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+
 +\-\-\->\|  DISCONNECTED   \|<\-\-\-\-\-\-\-+
 \|    +\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-+        \|
 \|             \|                 \|
 \| failed      \| initiated       \| disconnect
 \|             V                 \|
 \|    +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+        \|
 +\-\-\-\-+     PENDING     +\-\-\-\-\-\-\-\-+
      +\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-+        \|
               \|                 \|
               \| established     \|
               V                 \|
+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+   \|
\|             UP             \|   \|
\|                            +\-\-\-+
\|  +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \|
\|  \| UNAUTHENTICATED \|       \|
\|  +\-\-\-\-\-\-\-\-+\-\-\-\-\-\-\-\-+       \|
\|           \|                \|
\|           \| authenticated  \|
\|           V                \|
\|  +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \|
\|  \|  AUTHENTICATED  \|       \|
\|  +\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+       \|
\|                            \|
+\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+

A subscriber session in the DISCONNECTED state technically
doesn't exist; that is, the system does not maintain a context
to describe a disconnected subscriber session.

Once the system detects the initiation of a subscriber session,
then it creates a context and places the subscriber session in
the PENDING state.  The initiation of a subscriber session can
occur either through provisioning or the reception of a packet.
In the PENDING state, a system does not forward subscriber
traffic.

A pending subscriber session can become DISCONNECTED if
it fails to come up (e.g., a timeout) or if the system or the
subscriber explicitly terminates the subscriber session.

A pending subscriber session can become UP if the system
successfully configures and applies any relevant policies.
Once in the UP state, a system forwards subscriber traffic.

A operationally UP subscriber session can become DISCONNECTED if
either system or the subscriber terminates it.

A operationally UP subscriber session can either be
UNAUTHENTICATED or AUTHENTICATED.  When the system is in the
process of checking a the credentials associated with a
subscriber session, it is in the UNAUTHENTICATED state.  When
the system successfully completes this process, it transitions
the subscriber session to the AUTHENTICATED state.  If the
process fails, then the system terminates the subscriber
session.

Besides describing individual subscriber sessions, this MIB
module provides an EMS/NMS with the means to perform the
following functions\:

1)  Enumerate subscriber sessions by ifIndex.

2)  Enumerate subscriber sessions by subscriber session type and
    ifIndex.

3)  Monitor aggregated statistics relating to subscriber
    sessions\:

    a.  System\-wide
    b.  System\-wide by subscriber session type
    c.  Per node
    d.  Per node by subscriber session type

4)  Collect 15\-minute aggregated performance data history
    relating to subscriber sessions\:

    a.  System\-wide
    b.  System\-wide by subscriber session type
    c.  Per node
    d.  Per node by subscriber session type

5)  Submit a query for a report containing those subscriber
    sessions that match a specified identity match criteria.

6)  Terminate those subscriber session that match a
    specified identify match criteria.

GLOSSARY
========

Access Concentrator
    See NAS.

Access Network
    The network that provides connectivity between a AN and NAS.
    An access network may provide L2 or L3 connectivity. If the
    access network provide L2 connectivity, it may switch
    traffic or tunnel it through a MPLS or IP network.

AN (Access Node)
    A device (e.g., a DSLAM) that multiplexes or switches
    traffic between many CPEs and an access network.

BRAS (Broadband Remote Access Server)
    See NAS.

CPE (Customer Premise Equipment)
    A device (e.g., a DSL modem) that connects a customer's
    network to an AN.

DHCP (Dynamic Host Configuration Protocol)
    The protocol that provides a framework for transacting
    configuration information to devices on an IP network, as
    specified by RFC\-2131.

NAS (Network Access Server)
    A device that switches or routes traffic between subscriber
    sessions and service provider networks.

Network Service
    Access to the Internet backbone, voice, video, or other
    content.

Node
    A physical entity capable of maintaining a subscriber
    session within a distributed system.  The notion of a node
    is not applicable to a centralized system.

PADI (PPPoE Active Discovery Initiation)
    A subscriber broadcasts a PADI packet to start the process
    of discovering access concentrators capable of serving it.

PADO (PPPoE Active Discovery Offer)
    The packet sent by an access concentrator to a subscriber
    indicating that it can serve the subscriber.

PADR (PPPoE Active Discovery Request)
    The packet sent by a subscriber to an access concentrator
    requesting a PPPoE connection.

PADS (PPPoE Active Discovery Session\-confirmation)
    The packet sent by an access concentrator to a subscriber
    confirming the request for a PPPoE connection.  Once this
    packet has been sent, then the PPP can proceed as specified
    by RFC\-1661.

PADT (PPPoE Active Discovery Terminate)
    The packet indicating that a PPPoE connection has been
    terminated.  Either the subscriber or the access
    concentrator can send this packet.

PPP (Point\-to\-Point Protocol)
    The standard method for transporting multi\-protocol
    datagrams over point\-to\-point links, as defined by RFC\-1661.
    The PPP specifies the encapsulation for these datagrams and
    the protocols necessary for establishing, configuring, and
    maintaining connectivity.

PPPoE (Point\-to\-Point Protocol over Ethernet)
    The protocol and encapsulation necessary to support a PPP
    connection over an Ethernet connection, as defined by IETF
    RFC\-2516.

Service Provider Network
    The network that provides connectivity between a NAS and a
    network service.

Subscriber
    A customer of a network service.

Subscriber Session
    A context maintained by a NAS for the purpose of classifying
    a subscriber's traffic, maintaining a subscriber's identity,
    applying configuration and policies, and maintaining
    statistics.  For more information on the types of subscriber
    sessions, see the CISCO\-SUBSCRIBER\-SESSION\-TC\-MIB.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error




class CISCOSUBSCRIBERSESSIONMIB(Entity):
    """
    
    
    .. attribute:: csubjob
    
    	
    	**type**\:  :py:class:`CsubJob <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJob>`
    
    	**config**\: False
    
    .. attribute:: csubaggthresh
    
    	
    	**type**\:  :py:class:`CsubAggThresh <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubAggThresh>`
    
    	**config**\: False
    
    .. attribute:: csubsessiontable
    
    	This table describes a list of subscriber sessions currently maintained by the system.  This table has a sparse dependent relationship on the ifTable, containing a row for each interface having an interface type describing a subscriber session
    	**type**\:  :py:class:`CsubSessionTable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubSessionTable>`
    
    	**config**\: False
    
    .. attribute:: csubsessionbytypetable
    
    	This table describes a list of subscriber sessions currently maintained by the system.  The tables sorts the subscriber sessions first by the subscriber session's type and second by the ifIndex assigned to the subscriber session
    	**type**\:  :py:class:`CsubSessionByTypeTable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubSessionByTypeTable>`
    
    	**config**\: False
    
    .. attribute:: csubaggstatstable
    
    	This table contains sets of aggregated statistics relating to subscriber sessions, where each set has a unique scope of aggregation
    	**type**\:  :py:class:`CsubAggStatsTable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsTable>`
    
    	**config**\: False
    
    .. attribute:: csubaggstatsinttable
    
    	This table contains aggregated subscriber session performance data collected for as much as a day's worth of 15\-minute measurement intervals.  This table has an expansion dependent relationship on the csubAggStatsTable, containing zero or more rows for each row contained by the csubAggStatsTable.  Observe that the collection and maintenance of aggregated subscriber performance data is OPTIONAL for all scopes of aggregation.  However, an implementation should maintain at least one interval for the 'scope of aggregation' that contains all subscriber sessions maintained by the system
    	**type**\:  :py:class:`CsubAggStatsIntTable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsIntTable>`
    
    	**config**\: False
    
    .. attribute:: csubaggstatsthreshtable
    
    	Please enter the Table Description here
    	**type**\:  :py:class:`CsubAggStatsThreshTable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsThreshTable>`
    
    	**config**\: False
    
    .. attribute:: csubjobtable
    
    	This table contains the subscriber session jobs submitted by the EMS/NMS
    	**type**\:  :py:class:`CsubJobTable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJobTable>`
    
    	**config**\: False
    
    .. attribute:: csubjobmatchparamstable
    
    	This table contains subscriber session job parameters describing match criteria.  This table has a sparse\-dependent relationship on the csubJobTable, containing a row for each job having a csubJobType of 'query' or 'clear'
    	**type**\:  :py:class:`CsubJobMatchParamsTable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJobMatchParamsTable>`
    
    	**config**\: False
    
    .. attribute:: csubjobqueryparamstable
    
    	This table contains subscriber session job parameters describing query parameters.  This table has a sparse\-dependent relationship on the csubJobTable, containing a row for each job having a csubJobType of 'query'
    	**type**\:  :py:class:`CsubJobQueryParamsTable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJobQueryParamsTable>`
    
    	**config**\: False
    
    .. attribute:: csubjobqueuetable
    
    	This table lists the subscriber session jobs currently pending in the subscriber session job queue
    	**type**\:  :py:class:`CsubJobQueueTable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJobQueueTable>`
    
    	**config**\: False
    
    .. attribute:: csubjobreporttable
    
    	This table contains the reports corresponding to subscriber session jobs that have a csubJobType of 'query' and csubJobState of 'finished'.  This table has an expansion dependent relationship on the csubJobTable, containing zero or more rows for each job
    	**type**\:  :py:class:`CsubJobReportTable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJobReportTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
    _revision = '2012-08-08'

    def __init__(self):
        super(CISCOSUBSCRIBERSESSIONMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-SUBSCRIBER-SESSION-MIB"
        self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("csubJob", ("csubjob", CISCOSUBSCRIBERSESSIONMIB.CsubJob)), ("csubAggThresh", ("csubaggthresh", CISCOSUBSCRIBERSESSIONMIB.CsubAggThresh)), ("csubSessionTable", ("csubsessiontable", CISCOSUBSCRIBERSESSIONMIB.CsubSessionTable)), ("csubSessionByTypeTable", ("csubsessionbytypetable", CISCOSUBSCRIBERSESSIONMIB.CsubSessionByTypeTable)), ("csubAggStatsTable", ("csubaggstatstable", CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsTable)), ("csubAggStatsIntTable", ("csubaggstatsinttable", CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsIntTable)), ("csubAggStatsThreshTable", ("csubaggstatsthreshtable", CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsThreshTable)), ("csubJobTable", ("csubjobtable", CISCOSUBSCRIBERSESSIONMIB.CsubJobTable)), ("csubJobMatchParamsTable", ("csubjobmatchparamstable", CISCOSUBSCRIBERSESSIONMIB.CsubJobMatchParamsTable)), ("csubJobQueryParamsTable", ("csubjobqueryparamstable", CISCOSUBSCRIBERSESSIONMIB.CsubJobQueryParamsTable)), ("csubJobQueueTable", ("csubjobqueuetable", CISCOSUBSCRIBERSESSIONMIB.CsubJobQueueTable)), ("csubJobReportTable", ("csubjobreporttable", CISCOSUBSCRIBERSESSIONMIB.CsubJobReportTable))])
        self._leafs = OrderedDict()

        self.csubjob = CISCOSUBSCRIBERSESSIONMIB.CsubJob()
        self.csubjob.parent = self
        self._children_name_map["csubjob"] = "csubJob"

        self.csubaggthresh = CISCOSUBSCRIBERSESSIONMIB.CsubAggThresh()
        self.csubaggthresh.parent = self
        self._children_name_map["csubaggthresh"] = "csubAggThresh"

        self.csubsessiontable = CISCOSUBSCRIBERSESSIONMIB.CsubSessionTable()
        self.csubsessiontable.parent = self
        self._children_name_map["csubsessiontable"] = "csubSessionTable"

        self.csubsessionbytypetable = CISCOSUBSCRIBERSESSIONMIB.CsubSessionByTypeTable()
        self.csubsessionbytypetable.parent = self
        self._children_name_map["csubsessionbytypetable"] = "csubSessionByTypeTable"

        self.csubaggstatstable = CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsTable()
        self.csubaggstatstable.parent = self
        self._children_name_map["csubaggstatstable"] = "csubAggStatsTable"

        self.csubaggstatsinttable = CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsIntTable()
        self.csubaggstatsinttable.parent = self
        self._children_name_map["csubaggstatsinttable"] = "csubAggStatsIntTable"

        self.csubaggstatsthreshtable = CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsThreshTable()
        self.csubaggstatsthreshtable.parent = self
        self._children_name_map["csubaggstatsthreshtable"] = "csubAggStatsThreshTable"

        self.csubjobtable = CISCOSUBSCRIBERSESSIONMIB.CsubJobTable()
        self.csubjobtable.parent = self
        self._children_name_map["csubjobtable"] = "csubJobTable"

        self.csubjobmatchparamstable = CISCOSUBSCRIBERSESSIONMIB.CsubJobMatchParamsTable()
        self.csubjobmatchparamstable.parent = self
        self._children_name_map["csubjobmatchparamstable"] = "csubJobMatchParamsTable"

        self.csubjobqueryparamstable = CISCOSUBSCRIBERSESSIONMIB.CsubJobQueryParamsTable()
        self.csubjobqueryparamstable.parent = self
        self._children_name_map["csubjobqueryparamstable"] = "csubJobQueryParamsTable"

        self.csubjobqueuetable = CISCOSUBSCRIBERSESSIONMIB.CsubJobQueueTable()
        self.csubjobqueuetable.parent = self
        self._children_name_map["csubjobqueuetable"] = "csubJobQueueTable"

        self.csubjobreporttable = CISCOSUBSCRIBERSESSIONMIB.CsubJobReportTable()
        self.csubjobreporttable.parent = self
        self._children_name_map["csubjobreporttable"] = "csubJobReportTable"
        self._segment_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB, [], name, value)


    class CsubJob(Entity):
        """
        
        
        .. attribute:: csubjobfinishednotifyenable
        
        	This object specifies whether the system generates a csubJobFinishedNotify notification when the system finishes processing a subscriber session job
        	**type**\: bool
        
        	**config**\: False
        
        .. attribute:: csubjobindexedattributes
        
        	This object indicates which subscriber session identities the system maintains as searchable keys.  This value serves the EMS/NMS in configuring a subscriber session query, as at least one match criteria must be an 'indexed attribute'
        	**type**\:  :py:class:`SubSessionIdentities <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.SubSessionIdentities>`
        
        	**config**\: False
        
        .. attribute:: csubjobidnext
        
        	This object indicates the next available identifier for the creation of a new row in the csubJobTable.  If no available identifier exists, then this object has the value '0'
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: csubjobmaxnumber
        
        	This object indicates the maximum number of outstanding subscriber session jobs the system can support.  If the csubJobTable contains a number of rows (i.e., the value of csubJobCount) equal to this value, then any attempt to create a new row will result in a response with an error\-status of 'resourceUnavailable'
        	**type**\: int
        
        	**range:** 1..4294967295
        
        	**config**\: False
        
        	**units**\: jobs
        
        .. attribute:: csubjobmaxlife
        
        	This object specifies the maximum life a subscriber session report corresponding to a subscriber session job having a csubJobType of 'query'.  The system tracks the time elapsed after it finishes processing a query.  When the time elapsed reaches the value specified by this column, the system automatically  destroys the report.  A value of '0' disables the automatic destruction of reports
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: seconds
        
        .. attribute:: csubjobcount
        
        	This object indicates the number of subscriber session jobs currently maintained by the csubJobTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        	**units**\: jobs
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CISCOSUBSCRIBERSESSIONMIB.CsubJob, self).__init__()

            self.yang_name = "csubJob"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csubjobfinishednotifyenable', (YLeaf(YType.boolean, 'csubJobFinishedNotifyEnable'), ['bool'])),
                ('csubjobindexedattributes', (YLeaf(YType.bits, 'csubJobIndexedAttributes'), ['Bits'])),
                ('csubjobidnext', (YLeaf(YType.uint32, 'csubJobIdNext'), ['int'])),
                ('csubjobmaxnumber', (YLeaf(YType.uint32, 'csubJobMaxNumber'), ['int'])),
                ('csubjobmaxlife', (YLeaf(YType.uint32, 'csubJobMaxLife'), ['int'])),
                ('csubjobcount', (YLeaf(YType.uint32, 'csubJobCount'), ['int'])),
            ])
            self.csubjobfinishednotifyenable = None
            self.csubjobindexedattributes = Bits()
            self.csubjobidnext = None
            self.csubjobmaxnumber = None
            self.csubjobmaxlife = None
            self.csubjobcount = None
            self._segment_path = lambda: "csubJob"
            self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubJob, ['csubjobfinishednotifyenable', 'csubjobindexedattributes', 'csubjobidnext', 'csubjobmaxnumber', 'csubjobmaxlife', 'csubjobcount'], name, value)



    class CsubAggThresh(Entity):
        """
        
        
        .. attribute:: csubaggstatsthreshnotifenable
        
        	This object enables or disables the generation of any of the csubAggStats\* threshold notifications
        	**type**\: bool
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CISCOSUBSCRIBERSESSIONMIB.CsubAggThresh, self).__init__()

            self.yang_name = "csubAggThresh"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('csubaggstatsthreshnotifenable', (YLeaf(YType.boolean, 'csubAggStatsThreshNotifEnable'), ['bool'])),
            ])
            self.csubaggstatsthreshnotifenable = None
            self._segment_path = lambda: "csubAggThresh"
            self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubAggThresh, ['csubaggstatsthreshnotifenable'], name, value)



    class CsubSessionTable(Entity):
        """
        This table describes a list of subscriber sessions currently
        maintained by the system.
        
        This table has a sparse dependent relationship on the ifTable,
        containing a row for each interface having an interface type
        describing a subscriber session.
        
        .. attribute:: csubsessionentry
        
        	This entry contains data describing a subscriber sessions, including its state, configuration, and collected identities.  An entry exists for a corresponding entry in the ifTable describing a subscriber session.  Currently, subscriber sessions must have one of the following ifType values\:      'ppp'     'ipSubscriberSession'     'l2SubscriberSession'  The system creates an entry when it establishes a subscriber session.  Likewise, the system destroys an entry when it terminates the corresponding subscriber session
        	**type**\: list of  		 :py:class:`CsubSessionEntry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubSessionTable.CsubSessionEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CISCOSUBSCRIBERSESSIONMIB.CsubSessionTable, self).__init__()

            self.yang_name = "csubSessionTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("csubSessionEntry", ("csubsessionentry", CISCOSUBSCRIBERSESSIONMIB.CsubSessionTable.CsubSessionEntry))])
            self._leafs = OrderedDict()

            self.csubsessionentry = YList(self)
            self._segment_path = lambda: "csubSessionTable"
            self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubSessionTable, [], name, value)


        class CsubSessionEntry(Entity):
            """
            This entry contains data describing a subscriber sessions,
            including its state, configuration, and collected identities.
            
            An entry exists for a corresponding entry in the ifTable
            describing a subscriber session.  Currently, subscriber
            sessions must have one of the following ifType values\:
            
                'ppp'
                'ipSubscriberSession'
                'l2SubscriberSession'
            
            The system creates an entry when it establishes a subscriber
            session.  Likewise, the system destroys an entry when it
            terminates the corresponding subscriber session.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: csubsessiontype
            
            	This object indicates the type of subscriber session
            	**type**\:  :py:class:`SubSessionType <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB.SubSessionType>`
            
            	**config**\: False
            
            .. attribute:: csubsessionipaddrassignment
            
            	This object indicates how the system assigns IP addresses to the subscriber\:      'none'         The system does not an involvement in (or is it aware         of) the assignment an subscriber IP addresses.  For         example, a system does not have an involvement in the         assignment of subscriber IP addresses for IP interface         subscriber sessions.      'other'         The system assigns subscriber IP addresses using a         method not recognized by this MIB module.      'static'         Subscriber IP addresses have been configured correctly         for the service domain.  The system does not have an         involvement in the assignment of the IP address.      'localPool'         The system assigns subscriber IP addresses from a         locally configured pool of IP addresses.      'dhcpv4'         The system assigns subscriber IP addresses are using the         DHCPv4.      'dhcpv6'         The system assigns subscriber IP addresses using the         DHCPv6.      'userProfileIpAddr'         The system assigns subscriber IP addresses from a user         profile.      'userProfileIpSubnet'         The system assigns the subscriber an IP subnet from a         user profile.      'userProfileNamedPool'         The system assigns subscriber IP addresses from a         locally configured named pool specified by a user         profile
            	**type**\:  :py:class:`CsubSessionIpAddrAssignment <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubSessionTable.CsubSessionEntry.CsubSessionIpAddrAssignment>`
            
            	**config**\: False
            
            .. attribute:: csubsessionstate
            
            	This object indicates the operational state of the subscriber session
            	**type**\:  :py:class:`SubSessionState <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB.SubSessionState>`
            
            	**config**\: False
            
            .. attribute:: csubsessionauthenticated
            
            	This object indicates whether the system has successfully authenticated the subscriber session.      'false'         The subscriber session is operationally up, but in the         UNAUTHENTICATED state.      'true'         The subscriber session is operationally up, but in the         AUTHENTICATED state
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: csubsessionredundancymode
            
            	This object indicates the redundancy mode in which the subscriber session is operating
            	**type**\:  :py:class:`SubSessionRedundancyMode <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB.SubSessionRedundancyMode>`
            
            	**config**\: False
            
            .. attribute:: csubsessioncreationtime
            
            	This object indicates when the subscriber session was created (i.e., when the subscriber session was initiated)
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubsessionderivedcfg
            
            	This object indicates the row in the cdtTemplateTable (defined by the CISCO\-DYNAMIC\-TEMPLATE\-MIB) describing the derived configuration for the subscriber session.  Observe that the value of cdtTemplateType corresponding to the referenced row must be 'derived'
            	**type**\: str
            
            	**length:** 1..64
            
            	**config**\: False
            
            .. attribute:: csubsessionavailableidentities
            
            	This object indicates the subscriber identities that the system has successfully collected for the subscriber session.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is invalid.  If the bit is '1', then the value of the corresponding column represents the value of the subscriber identity collected by the system.  The following list specifies the mappings between the bits and the columns\:      'subscriberLabel' => csubSessionSubscriberLabel     'macAddress'      => csubSessionMacAddress     'nativeVrf'       => csubSessionNativeVrf     'nativeIpAddress' => csubSessionNativeIpAddrType,                          csubSessionNativeIpAddr,                          csubSessionNativeIpMask     'nativeIpAddress2'=> csubSessionNativeIpAddrType2,                          csubSessionNativeIpAddr2,                          csubSessionNativeIpMask2                                      'domainVrf'       => csubSessionDomainVrf     'domainIpAddress' => csubSessionDomainIpAddrType,                          csubSessionDomainIpAddr,                          csubSessionDomainIpMask     'pbhk'            => csubSessionPbhk     'remoteId'        => csubSessionRemoteId     'circuitId'       => csubSessionCircuitId     'nasPort'         => csubSessionNasPort     'domain'          => csubSessionDomain     'username'        => csubSessionUsername     'acctSessionId'   => csubSessionAcctSessionId     'dnis'            => csubSessionDnis     'media'           => csubSessionMedia     'mlpNegotiated'   => csubSessionMlpNegotiated     'protocol'        => csubSessionProtocol     'dhcpClass'       => csubSessionDhcpClass     'tunnelName'      => csubSessionTunnelName  Observe that the bit 'ifIndex' should always be '1'.  This identity maps to the ifIndex assigned to the subscriber session.  Observe that the bit 'serviceName' maps to one or more instance of ccbptPolicyMap (defined by the CISCO\-CBP\-TARGET\-MIB)
            	**type**\:  :py:class:`SubSessionIdentities <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.SubSessionIdentities>`
            
            	**config**\: False
            
            .. attribute:: csubsessionsubscriberlabel
            
            	This object indicates a positive integer\-value uniquely identifying the subscriber session within the scope of the system.  This column is valid only if the 'subscriberLabel' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: csubsessionmacaddress
            
            	This object indicates the MAC address of the subscriber.  This column is valid only if the 'macAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: csubsessionnativevrf
            
            	This object indicates the VRF originating the subscriber session.  This column is valid only if the 'nativeVrf' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubsessionnativeipaddrtype
            
            	This object indicates the type of IP address assigned to the subscriber on the customer\-facing side of the system.  This column is valid only if the 'nativeIpAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: csubsessionnativeipaddr
            
            	This object indicates the IP address assigned to the subscriber on the customer\-facing side of the system.  This column is valid only if the 'nativeIpAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: csubsessionnativeipmask
            
            	This object indicates the corresponding mask for the IP address assigned to the subscriber on the customer\-facing side of the system.  This column is valid only if the 'nativeIpAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: csubsessiondomainvrf
            
            	This object indicates the VRF to which the system transfers the subscriber session's traffic.  This column is valid only if the 'domainVrf' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubsessiondomainipaddrtype
            
            	This object indicates the type of IP address assigned to the subscriber on the service\-facing side of the system.  This column is valid only if the 'domainIpAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: csubsessiondomainipaddr
            
            	This object indicates the IP address assigned to the subscriber on the service\-facing side of the system.  This column is valid only if the 'domainIpAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: csubsessiondomainipmask
            
            	This object indicates the corresponding mask for the IP address assigned to the subscriber on the service\-facing side of the system.  This column is valid only if the 'domainIpAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: csubsessionpbhk
            
            	This object indicates the PBHK identifying the subscriber.  This column is valid only if the 'pbhk' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubsessionremoteid
            
            	This object indicates the Remote\-Id identifying the 'calling station' or AN supporting the circuit that provides access to the subscriber.  This column is valid only if the 'remoteId' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubsessioncircuitid
            
            	This object indicates the Circuit\-Id identifying the circuit supported by the 'calling station' or AN providing access to the subscriber.  This column is valid only if the 'circuitId' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubsessionnasport
            
            	This object indicates the NAS port\-identifier identifying the port on the NAS providing access to the subscriber.  This column is valid only if the 'nasPort' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubsessiondomain
            
            	This object indicates the domain associated with the subscriber.  This column is valid only if the 'domain' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubsessionusername
            
            	This object indicates the username identifying the subscriber.  This column is valid only if the 'username' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubsessionacctsessionid
            
            	This object indicates the accounting session identifier assigned to the subscriber session.  This column is valid only if the 'accountingSid' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: csubsessiondnis
            
            	This object indicates the DNIS number dialed by the subscriber to access the 'calling station' or AN.  This column is valid only if the 'dnis' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubsessionmedia
            
            	This object indicates the type of media providing access to the subscriber.  This column is valid only if the 'media' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  :py:class:`SubscriberMediaType <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.SubscriberMediaType>`
            
            	**config**\: False
            
            .. attribute:: csubsessionmlpnegotiated
            
            	This object indicates whether the subscriber session was established using multi\-link PPP negotiation.  This column is valid only if the 'mlpNegotiated' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: csubsessionprotocol
            
            	This object indicates the type of protocol providing access to the subscriber.  This column is valid only if the 'protocol' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  :py:class:`SubscriberProtocolType <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.SubscriberProtocolType>`
            
            	**config**\: False
            
            .. attribute:: csubsessiondhcpclass
            
            	This object indicates the name of the class matching the DHCP DISCOVER message received from the subscriber.  This column is valid only if the 'dhcpClass' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubsessiontunnelname
            
            	This object indicates the name of the VPDN used to carry the subscriber session to the system.  This column is valid only if the 'tunnelName' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubsessionlocationidentifier
            
            	This object indicates the location of the subscriber
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubsessionserviceidentifier
            
            	This object indicates the name used to identify the services subscribed by a particular session
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubsessionlastchanged
            
            	This object indicates when the subscriber session is updated with new policy information
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubsessionnativeipaddrtype2
            
            	This object indicates the type of IP address assigned to the subscriber on the customer\-facing side of the system.  This column is valid only if the 'nativeIpAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'.  In Dual stack scenarios both 'csubSessionNativeIpAddrType' and  'csubSessionNativeIpAddrType2' will be valid
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: csubsessionnativeipaddr2
            
            	This object indicates the IP address assigned to the subscriber on the customer\-facing side of the system.  This column is valid only if the 'nativeIpAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: csubsessionnativeipmask2
            
            	This object indicates the corresponding mask for the IP address assigned to the subscriber on the customer\-facing side of the system.  This column is valid only if the 'nativeIpAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CISCOSUBSCRIBERSESSIONMIB.CsubSessionTable.CsubSessionEntry, self).__init__()

                self.yang_name = "csubSessionEntry"
                self.yang_parent_name = "csubSessionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('csubsessiontype', (YLeaf(YType.enumeration, 'csubSessionType'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB', 'SubSessionType', '')])),
                    ('csubsessionipaddrassignment', (YLeaf(YType.enumeration, 'csubSessionIpAddrAssignment'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CISCOSUBSCRIBERSESSIONMIB', 'CsubSessionTable.CsubSessionEntry.CsubSessionIpAddrAssignment')])),
                    ('csubsessionstate', (YLeaf(YType.enumeration, 'csubSessionState'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB', 'SubSessionState', '')])),
                    ('csubsessionauthenticated', (YLeaf(YType.boolean, 'csubSessionAuthenticated'), ['bool'])),
                    ('csubsessionredundancymode', (YLeaf(YType.enumeration, 'csubSessionRedundancyMode'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB', 'SubSessionRedundancyMode', '')])),
                    ('csubsessioncreationtime', (YLeaf(YType.str, 'csubSessionCreationTime'), ['str'])),
                    ('csubsessionderivedcfg', (YLeaf(YType.str, 'csubSessionDerivedCfg'), ['str'])),
                    ('csubsessionavailableidentities', (YLeaf(YType.bits, 'csubSessionAvailableIdentities'), ['Bits'])),
                    ('csubsessionsubscriberlabel', (YLeaf(YType.uint32, 'csubSessionSubscriberLabel'), ['int'])),
                    ('csubsessionmacaddress', (YLeaf(YType.str, 'csubSessionMacAddress'), ['str'])),
                    ('csubsessionnativevrf', (YLeaf(YType.str, 'csubSessionNativeVrf'), ['str'])),
                    ('csubsessionnativeipaddrtype', (YLeaf(YType.enumeration, 'csubSessionNativeIpAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('csubsessionnativeipaddr', (YLeaf(YType.str, 'csubSessionNativeIpAddr'), ['str'])),
                    ('csubsessionnativeipmask', (YLeaf(YType.str, 'csubSessionNativeIpMask'), ['str'])),
                    ('csubsessiondomainvrf', (YLeaf(YType.str, 'csubSessionDomainVrf'), ['str'])),
                    ('csubsessiondomainipaddrtype', (YLeaf(YType.enumeration, 'csubSessionDomainIpAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('csubsessiondomainipaddr', (YLeaf(YType.str, 'csubSessionDomainIpAddr'), ['str'])),
                    ('csubsessiondomainipmask', (YLeaf(YType.str, 'csubSessionDomainIpMask'), ['str'])),
                    ('csubsessionpbhk', (YLeaf(YType.str, 'csubSessionPbhk'), ['str'])),
                    ('csubsessionremoteid', (YLeaf(YType.str, 'csubSessionRemoteId'), ['str'])),
                    ('csubsessioncircuitid', (YLeaf(YType.str, 'csubSessionCircuitId'), ['str'])),
                    ('csubsessionnasport', (YLeaf(YType.str, 'csubSessionNasPort'), ['str'])),
                    ('csubsessiondomain', (YLeaf(YType.str, 'csubSessionDomain'), ['str'])),
                    ('csubsessionusername', (YLeaf(YType.str, 'csubSessionUsername'), ['str'])),
                    ('csubsessionacctsessionid', (YLeaf(YType.uint32, 'csubSessionAcctSessionId'), ['int'])),
                    ('csubsessiondnis', (YLeaf(YType.str, 'csubSessionDnis'), ['str'])),
                    ('csubsessionmedia', (YLeaf(YType.enumeration, 'csubSessionMedia'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB', 'SubscriberMediaType', '')])),
                    ('csubsessionmlpnegotiated', (YLeaf(YType.boolean, 'csubSessionMlpNegotiated'), ['bool'])),
                    ('csubsessionprotocol', (YLeaf(YType.enumeration, 'csubSessionProtocol'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB', 'SubscriberProtocolType', '')])),
                    ('csubsessiondhcpclass', (YLeaf(YType.str, 'csubSessionDhcpClass'), ['str'])),
                    ('csubsessiontunnelname', (YLeaf(YType.str, 'csubSessionTunnelName'), ['str'])),
                    ('csubsessionlocationidentifier', (YLeaf(YType.str, 'csubSessionLocationIdentifier'), ['str'])),
                    ('csubsessionserviceidentifier', (YLeaf(YType.str, 'csubSessionServiceIdentifier'), ['str'])),
                    ('csubsessionlastchanged', (YLeaf(YType.str, 'csubSessionLastChanged'), ['str'])),
                    ('csubsessionnativeipaddrtype2', (YLeaf(YType.enumeration, 'csubSessionNativeIpAddrType2'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('csubsessionnativeipaddr2', (YLeaf(YType.str, 'csubSessionNativeIpAddr2'), ['str'])),
                    ('csubsessionnativeipmask2', (YLeaf(YType.str, 'csubSessionNativeIpMask2'), ['str'])),
                ])
                self.ifindex = None
                self.csubsessiontype = None
                self.csubsessionipaddrassignment = None
                self.csubsessionstate = None
                self.csubsessionauthenticated = None
                self.csubsessionredundancymode = None
                self.csubsessioncreationtime = None
                self.csubsessionderivedcfg = None
                self.csubsessionavailableidentities = Bits()
                self.csubsessionsubscriberlabel = None
                self.csubsessionmacaddress = None
                self.csubsessionnativevrf = None
                self.csubsessionnativeipaddrtype = None
                self.csubsessionnativeipaddr = None
                self.csubsessionnativeipmask = None
                self.csubsessiondomainvrf = None
                self.csubsessiondomainipaddrtype = None
                self.csubsessiondomainipaddr = None
                self.csubsessiondomainipmask = None
                self.csubsessionpbhk = None
                self.csubsessionremoteid = None
                self.csubsessioncircuitid = None
                self.csubsessionnasport = None
                self.csubsessiondomain = None
                self.csubsessionusername = None
                self.csubsessionacctsessionid = None
                self.csubsessiondnis = None
                self.csubsessionmedia = None
                self.csubsessionmlpnegotiated = None
                self.csubsessionprotocol = None
                self.csubsessiondhcpclass = None
                self.csubsessiontunnelname = None
                self.csubsessionlocationidentifier = None
                self.csubsessionserviceidentifier = None
                self.csubsessionlastchanged = None
                self.csubsessionnativeipaddrtype2 = None
                self.csubsessionnativeipaddr2 = None
                self.csubsessionnativeipmask2 = None
                self._segment_path = lambda: "csubSessionEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubSessionTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubSessionTable.CsubSessionEntry, ['ifindex', 'csubsessiontype', 'csubsessionipaddrassignment', 'csubsessionstate', 'csubsessionauthenticated', 'csubsessionredundancymode', 'csubsessioncreationtime', 'csubsessionderivedcfg', 'csubsessionavailableidentities', 'csubsessionsubscriberlabel', 'csubsessionmacaddress', 'csubsessionnativevrf', 'csubsessionnativeipaddrtype', 'csubsessionnativeipaddr', 'csubsessionnativeipmask', 'csubsessiondomainvrf', 'csubsessiondomainipaddrtype', 'csubsessiondomainipaddr', 'csubsessiondomainipmask', 'csubsessionpbhk', 'csubsessionremoteid', 'csubsessioncircuitid', 'csubsessionnasport', 'csubsessiondomain', 'csubsessionusername', 'csubsessionacctsessionid', 'csubsessiondnis', 'csubsessionmedia', 'csubsessionmlpnegotiated', 'csubsessionprotocol', 'csubsessiondhcpclass', 'csubsessiontunnelname', 'csubsessionlocationidentifier', 'csubsessionserviceidentifier', 'csubsessionlastchanged', 'csubsessionnativeipaddrtype2', 'csubsessionnativeipaddr2', 'csubsessionnativeipmask2'], name, value)

            class CsubSessionIpAddrAssignment(Enum):
                """
                CsubSessionIpAddrAssignment (Enum Class)

                This object indicates how the system assigns IP addresses to

                the subscriber\:

                    'none'

                        The system does not an involvement in (or is it aware

                        of) the assignment an subscriber IP addresses.  For

                        example, a system does not have an involvement in the

                        assignment of subscriber IP addresses for IP interface

                        subscriber sessions.

                    'other'

                        The system assigns subscriber IP addresses using a

                        method not recognized by this MIB module.

                    'static'

                        Subscriber IP addresses have been configured correctly

                        for the service domain.  The system does not have an

                        involvement in the assignment of the IP address.

                    'localPool'

                        The system assigns subscriber IP addresses from a

                        locally configured pool of IP addresses.

                    'dhcpv4'

                        The system assigns subscriber IP addresses are using the

                        DHCPv4.

                    'dhcpv6'

                        The system assigns subscriber IP addresses using the

                        DHCPv6.

                    'userProfileIpAddr'

                        The system assigns subscriber IP addresses from a user

                        profile.

                    'userProfileIpSubnet'

                        The system assigns the subscriber an IP subnet from a

                        user profile.

                    'userProfileNamedPool'

                        The system assigns subscriber IP addresses from a

                        locally configured named pool specified by a user

                        profile.

                .. data:: none = 1

                .. data:: other = 2

                .. data:: static = 3

                .. data:: localPool = 4

                .. data:: dhcpv4 = 5

                .. data:: dhcpv6 = 6

                .. data:: userProfileIpAddr = 7

                .. data:: userProfileIpSubnet = 8

                .. data:: userProfileNamedPool = 9

                """

                none = Enum.YLeaf(1, "none")

                other = Enum.YLeaf(2, "other")

                static = Enum.YLeaf(3, "static")

                localPool = Enum.YLeaf(4, "localPool")

                dhcpv4 = Enum.YLeaf(5, "dhcpv4")

                dhcpv6 = Enum.YLeaf(6, "dhcpv6")

                userProfileIpAddr = Enum.YLeaf(7, "userProfileIpAddr")

                userProfileIpSubnet = Enum.YLeaf(8, "userProfileIpSubnet")

                userProfileNamedPool = Enum.YLeaf(9, "userProfileNamedPool")





    class CsubSessionByTypeTable(Entity):
        """
        This table describes a list of subscriber sessions currently
        maintained by the system.  The tables sorts the subscriber
        sessions first by the subscriber session's type and second by
        the ifIndex assigned to the subscriber session.
        
        .. attribute:: csubsessionbytypeentry
        
        	This entry identifies a subscriber session.  An entry exists for a corresponding entry in the ifTable describing a subscriber session.  Currently, subscriber sessions must have one of the following ifType values\:      'ppp'     'ipSubscriberSession'     'l2SubscriberSession'  The system creates an entry when it establishes a subscriber session.  Likewise, the system destroys an entry when it terminates the corresponding subscriber session
        	**type**\: list of  		 :py:class:`CsubSessionByTypeEntry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubSessionByTypeTable.CsubSessionByTypeEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CISCOSUBSCRIBERSESSIONMIB.CsubSessionByTypeTable, self).__init__()

            self.yang_name = "csubSessionByTypeTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("csubSessionByTypeEntry", ("csubsessionbytypeentry", CISCOSUBSCRIBERSESSIONMIB.CsubSessionByTypeTable.CsubSessionByTypeEntry))])
            self._leafs = OrderedDict()

            self.csubsessionbytypeentry = YList(self)
            self._segment_path = lambda: "csubSessionByTypeTable"
            self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubSessionByTypeTable, [], name, value)


        class CsubSessionByTypeEntry(Entity):
            """
            This entry identifies a subscriber session.
            
            An entry exists for a corresponding entry in the ifTable
            describing a subscriber session.  Currently, subscriber
            sessions must have one of the following ifType values\:
            
                'ppp'
                'ipSubscriberSession'
                'l2SubscriberSession'
            
            The system creates an entry when it establishes a subscriber
            session.  Likewise, the system destroys an entry when it
            terminates the corresponding subscriber session.
            
            .. attribute:: csubsessionbytype  (key)
            
            	This object indicates the type of the subscriber session
            	**type**\:  :py:class:`SubSessionType <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB.SubSessionType>`
            
            	**config**\: False
            
            .. attribute:: csubsessionifindex  (key)
            
            	This object indicates the ifIndex assigned to the subscriber session
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CISCOSUBSCRIBERSESSIONMIB.CsubSessionByTypeTable.CsubSessionByTypeEntry, self).__init__()

                self.yang_name = "csubSessionByTypeEntry"
                self.yang_parent_name = "csubSessionByTypeTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csubsessionbytype','csubsessionifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csubsessionbytype', (YLeaf(YType.enumeration, 'csubSessionByType'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB', 'SubSessionType', '')])),
                    ('csubsessionifindex', (YLeaf(YType.int32, 'csubSessionIfIndex'), ['int'])),
                ])
                self.csubsessionbytype = None
                self.csubsessionifindex = None
                self._segment_path = lambda: "csubSessionByTypeEntry" + "[csubSessionByType='" + str(self.csubsessionbytype) + "']" + "[csubSessionIfIndex='" + str(self.csubsessionifindex) + "']"
                self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubSessionByTypeTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubSessionByTypeTable.CsubSessionByTypeEntry, ['csubsessionbytype', 'csubsessionifindex'], name, value)




    class CsubAggStatsTable(Entity):
        """
        This table contains sets of aggregated statistics relating to
        subscriber sessions, where each set has a unique scope of
        aggregation.
        
        .. attribute:: csubaggstatsentry
        
        	An entry contains a set of aggregated statistics relating to those subscriber sessions that fall into a 'scope of  aggregation'.   A 'scope of aggregation' is the set of subscriber sessions  that meet specified criteria.  For example, a 'scope of  aggregation' may be the set of all PPPoE subscriber sessions  maintained by the system.  The following criteria define the  'scope of aggregation'\:   1)  Aggregation Point type          Aggregation point type identifies the format of the          csubAggStatsPoint for this entry.   2)  Aggregation Point          'Physical' Aggregation Point type case\:          In a distributed system, a 'node' represents a physical          entity capable of maintaining the context representing          a subscriber session.           If the 'scope of aggregation' specifies a physical          entity having an entPhysicalClass of 'chassis', then          the set of subscriber sessions in the 'scope of          aggregation' may contain the subscriber sessions maintained by all          the nodes contained in the system.           If the 'scope of aggregation' specifies a physical          entity having an entPhysicalClass of 'module' (e.g., a          line card), then the set of subscriber sessions in the          'scope of aggregation' may contain the subscriber          sessions maintained by the nodes contained by the          module.           If the 'scope of aggregation' specifies a physical          entity having an entPhysicalClass of 'cpu', then the          set of subscriber sessions in the 'scope of aggregation'          may contain the subscriber sessions maintained by the node          running on that processor.           Observe that a centralized system (i.e., a system          that essentially contains a single node) can only          support a 'scope of aggregation' that specifies a          physical entity classified as a 'chassis'.           If the scope of aggregation specifies 'interface',          then the scope is the set of subscriber sessions carried          by the interface identified the ifIndex value          represented in the csubAggStatsPoint value.   2)  Subscriber Session Type          If the 'scope of aggregation' specifies the value 'all'          for the subscriber session type, then the set of          subscriber sessions in the 'scope of aggregation' may          contain all subscriber sessions, regardless of type.           If the 'scope of aggregation' specifies a value other          than 'all' for the subscriber session type, then the          set of subscriber sessions in the 'scope of aggregation may          contain only those subscriber sessions of the specified          type.   Implementation Guidance  =======================  A system MUST maintain a set of statistics with a 'scope of  aggregation' that contains all subscriber sessions maintained  by the system.  The system creates this entry during the  initialization of the SNMP entity.   A system SHOULD maintain a set of statistics for each 'scope of  aggregation' containing subscriber sessions of each subscriber  session type the system is capable of providing access.  If the  system supports these sets of statistics, then it creates these  entries during the initialization of the SNMP entity.   A system MAY maintain sets of node\-specific statistics.  if the  system supports sets of node\-specific statistics, then it  creates the appropriate entries upon detection of a physical  entity (resulting from system restart or insertion) containing  those nodes.  Likewise, the system destroys these entries  upon removal of the physical entity
        	**type**\: list of  		 :py:class:`CsubAggStatsEntry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsTable.CsubAggStatsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsTable, self).__init__()

            self.yang_name = "csubAggStatsTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("csubAggStatsEntry", ("csubaggstatsentry", CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsTable.CsubAggStatsEntry))])
            self._leafs = OrderedDict()

            self.csubaggstatsentry = YList(self)
            self._segment_path = lambda: "csubAggStatsTable"
            self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsTable, [], name, value)


        class CsubAggStatsEntry(Entity):
            """
            An entry contains a set of aggregated statistics relating to
            those subscriber sessions that fall into a 'scope of 
            aggregation'. 
            
            A 'scope of aggregation' is the set of subscriber sessions 
            that meet specified criteria.  For example, a 'scope of 
            aggregation' may be the set of all PPPoE subscriber sessions 
            maintained by the system.  The following criteria define the 
            'scope of aggregation'\: 
            
            1)  Aggregation Point type 
                    Aggregation point type identifies the format of the 
                    csubAggStatsPoint for this entry. 
            
            2)  Aggregation Point 
                    'Physical' Aggregation Point type case\: 
                    In a distributed system, a 'node' represents a physical 
                    entity capable of maintaining the context representing 
                    a subscriber session. 
            
                    If the 'scope of aggregation' specifies a physical 
                    entity having an entPhysicalClass of 'chassis', then 
                    the set of subscriber sessions in the 'scope of 
                    aggregation' may contain the subscriber sessions maintained by all 
                    the nodes contained in the system. 
            
                    If the 'scope of aggregation' specifies a physical 
                    entity having an entPhysicalClass of 'module' (e.g., a 
                    line card), then the set of subscriber sessions in the 
                    'scope of aggregation' may contain the subscriber 
                    sessions maintained by the nodes contained by the 
                    module. 
            
                    If the 'scope of aggregation' specifies a physical 
                    entity having an entPhysicalClass of 'cpu', then the 
                    set of subscriber sessions in the 'scope of aggregation' 
                    may contain the subscriber sessions maintained by the node 
                    running on that processor. 
            
                    Observe that a centralized system (i.e., a system 
                    that essentially contains a single node) can only 
                    support a 'scope of aggregation' that specifies a 
                    physical entity classified as a 'chassis'. 
            
                    If the scope of aggregation specifies 'interface', 
                    then the scope is the set of subscriber sessions carried 
                    by the interface identified the ifIndex value 
                    represented in the csubAggStatsPoint value. 
            
            2)  Subscriber Session Type 
                    If the 'scope of aggregation' specifies the value 'all' 
                    for the subscriber session type, then the set of 
                    subscriber sessions in the 'scope of aggregation' may 
                    contain all subscriber sessions, regardless of type. 
            
                    If the 'scope of aggregation' specifies a value other 
                    than 'all' for the subscriber session type, then the 
                    set of subscriber sessions in the 'scope of aggregation may 
                    contain only those subscriber sessions of the specified 
                    type. 
            
            Implementation Guidance 
            ======================= 
            A system MUST maintain a set of statistics with a 'scope of 
            aggregation' that contains all subscriber sessions maintained 
            by the system.  The system creates this entry during the 
            initialization of the SNMP entity. 
            
            A system SHOULD maintain a set of statistics for each 'scope of 
            aggregation' containing subscriber sessions of each subscriber 
            session type the system is capable of providing access.  If the 
            system supports these sets of statistics, then it creates these 
            entries during the initialization of the SNMP entity. 
            
            A system MAY maintain sets of node\-specific statistics.  if the 
            system supports sets of node\-specific statistics, then it 
            creates the appropriate entries upon detection of a physical 
            entity (resulting from system restart or insertion) containing 
            those nodes.  Likewise, the system destroys these entries 
            upon removal of the physical entity.
            
            .. attribute:: csubaggstatspointtype  (key)
            
            	This object indicates format of the csubAggStatsPoint for this entry.   The format for the csubAggStatsPoint is as follows\:   csubAggStatsPointType      csubAggStatsPoint  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-     \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-      'physical'                 PhysicalIndex      'interface'                InterfaceIndex
            	**type**\:  :py:class:`CsubAggStatsPointType <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsTable.CsubAggStatsEntry.CsubAggStatsPointType>`
            
            	**config**\: False
            
            .. attribute:: csubaggstatspoint  (key)
            
            	This object should be read with csubAggStatsPointType always.  This object indicates one of the determining factors affecting  the 'scope of aggregation' for the set of statistics contained  by the row.   The value indicated by this object should be interpreted as the  identifier for the point type specific base table.   For point types of 'physical', the type specific base table is  the entPhysicalTable and this value is a PhysicalIndex.  For  point types of 'interface', the type specific base table is  the ifTable and this value is an InterfaceIndex.   If this column indicates a physical entity which has an  entPhysicalClass of 'chassis', then the 'scope of aggregation'  may includes those subscriber sessions maintained by all nodes  contained by the system.   If this column indicates a physical entity which has an  entPhysicalClass of  'module' (e.g., a line card), then the  'scope of aggregation' may include those subscriber sessions  maintained by the nodes contained by the module.   If this column indicates a physical entity which has an  entPhysicalClass of 'cpu', then the 'scope of aggregation' may  include those subscriber sessions maintained by the node  running on the processor.   Aggregation points with entPhysicalTable / ifTable overlap\:  For interfaces which map directly to physical 'port' class  entities in the entPhysicalTable, the preferred representation  as aggregation points is the 'physical' point type and  PhysicalIndex identifier
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: csubaggstatssessiontype  (key)
            
            	This object indicates one of the determining factors affecting the 'scope of aggregation' for the statistics contained by the row.  If the value of this column is 'all', then the 'scope of aggregation' may include all subscriber sessions, regardless of type.  If the value of this column is not 'all', then the 'scope of aggregation' may include subscriber sessions of the indicated subscriber session type
            	**type**\:  :py:class:`SubSessionType <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB.SubSessionType>`
            
            	**config**\: False
            
            .. attribute:: csubaggstatspendingsessions
            
            	This object indicates the current number of subscriber sessions within the 'scope of aggregation' that are in the PENDING state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsupsessions
            
            	This object indicates the current number of subscriber sessions within the 'scope of aggregation' that are in the UP state
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsauthsessions
            
            	This object indicates the current number of subscriber session within the 'scope of aggregation' that have been authenticated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsunauthsessions
            
            	This object indicates the current number of subscriber session within the 'scope of aggregation' that have not been authenticated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatslightweightsessions
            
            	This object indicates the current number of subscriber sessions within the 'scope of aggregation' that are less resource intensive
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsredsessions
            
            	This object indicates the current number of subscriber sessions within the 'scope of aggregation' that are redundant (i.e.,  sessions with a csubSessionRedundancyMode of 'standby')
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatshighupsessions
            
            	This object indicates the highest number of subscriber sessions within the 'scope of aggregation' observed simultaneously in the UP state since the last discontinuity time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsavgsessionuptime
            
            	This object indicates the average time subscriber sessions within the 'scope of aggregation' spent in the UP state.  The system calculates this average over all subscriber sessions maintained by all nodes contained by the 'scope of aggregation' since the last discontinuity time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: csubaggstatsavgsessionrpm
            
            	This object indicates the average rate (per minute) at which the nodes contained by the 'scope of aggregation' have established new subscriber sessions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions per minute
            
            .. attribute:: csubaggstatsavgsessionrph
            
            	This object indicates the average rate (per hour) at which the nodes contained by the 'scope of aggregation' have established new subscriber sessions
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions per hour
            
            .. attribute:: csubaggstatsthrottleengagements
            
            	This object indicates the number of times that nodes contained within the 'scope of aggregation' have engaged the subscriber session throttle since the last discontinuity time.  The mechanics of a subscriber session throttle vary with subscriber session type and implementation.  However, the general concept of the throttle prevents a node from having to deal with more than a configured number of requests to establish subscriber sessions from the same CPE within the a configured interval of time.  When the number of requests exceeds the configured threshold within the configured interval, then the node processing the requests engages the throttle. Typically, when a node engages a throttle, it drops requests from the CPE for some period of time, after which the node disengages the throttle.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of csubAggStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: engagements
            
            .. attribute:: csubaggstatstotalcreatedsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' created since the discontinuity time.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of csubAggStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatstotalfailedsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that were in the PENDING state and terminated for reasons other than disconnect since the last discontinuity time.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of csubAggStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatstotalupsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that transitioned to the UP state since the last discontinuity time.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of csubAggStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatstotalauthsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that transitioned from the UNAUTHENTICATED to the AUTHENTICATED state since the last discontinuity time.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of csubAggStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatstotaldiscsessions
            
            	This object indicates the total number of subscriber sessions terminated due to a disconnect event since the last discontinuity time.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of csubAggStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatstotallightweightsessions
            
            	This object indicates the total number of subscriber sessions that are less resource intensive
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatstotalflowsup
            
            	This object indicates the total number of differential traffic classes on subscriber sessions. IP ACLs are used to create differential flows(Traffic Classes).  Each Traffic Class can have a different set of features applied
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsdaycreatedsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' created during the last 24 hours.  The system calculates the value of this column by summing the values of all instances of csubAggStatsIntCreatedSessions that expand this row and have a corresponding csubAggStatsIntValid of 'true'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsdayfailedsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that were in the PENDING state and terminated for reasons other than disconnect during the last 24 hours.  The system calculates the value of this column by summing the values of all instances of csubAggStatsIntFailedSessions that expand this row and have a corresponding csubAggStatsIntValid of 'true'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsdayupsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that transitioned to the UP state during the last 24 hours.  The system calculates the value of this column by summing the values of all instances of csubAggStatsIntUpSessions that expand this row and have a corresponding csubAggStatsIntValid of 'true'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsdayauthsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that transitioned from the UNAUTHENTICATED to the AUTHENTICATED state during the last 24 hours.  The system calculates the value of this column by summing the values of all instances of csubAggStatsIntAuthSessions that expand this row and have a corresponding csubAggStatsIntValid of 'true'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsdaydiscsessions
            
            	This object indicates the total number of subscriber sessions terminated due to a disconnect event during the last 24 hours.  The system calculates the value of this column by summing the values of all instances of csubAggStatsIntDiscSessions that expand this row and have a corresponding csubAggStatsIntValid of 'true'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatscurrtimeelapsed
            
            	This object indicates the time that has elapsed since the beginning of the current 15\-minute measurement interval.  If, for some reason, such as an adjustment in the system's time\-of\-day clock, the current interval exceeds the maximum value, then the value of this column will be the maximum value
            	**type**\: int
            
            	**range:** 0..899
            
            	**config**\: False
            
            	**units**\: seconds
            
            .. attribute:: csubaggstatscurrvalidintervals
            
            	This object indicates the number of intervals for which data was collected.  The value of this column will be '96' unless the measurement was started (or restarted) within 1,440 minutes, in which case the value will be the number of complete 15\-minute intervals for which the system has at least some data.  In certain cases it is possible that some intervals are unavailable, in which case the value of this column will be maximum interval number for which data is available
            	**type**\: int
            
            	**range:** 0..96
            
            	**config**\: False
            
            	**units**\: intervals
            
            .. attribute:: csubaggstatscurrinvalidintervals
            
            	This object indicates the number of intervals in the range from 0 to csubCurrValidIntervals for which no data is available.  This object will typically be '0' except in certain circumstances when some intervals are unavailable
            	**type**\: int
            
            	**range:** 0..96
            
            	**config**\: False
            
            	**units**\: intervals
            
            .. attribute:: csubaggstatscurrflowsup
            
            	This object indicates the current number of differential traffic classes on subscriber sessions currently UP. IP ACLs are used to create differential flows (Traffic Classes).Each Traffic Class can have a different set of features applied
            	**type**\: int
            
            	**range:** 0..96
            
            	**config**\: False
            
            	**units**\: intervals
            
            .. attribute:: csubaggstatscurrcreatedsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' created during the current 15\-minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatscurrfailedsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that were in the PENDING state and terminated for reasons other than disconnect during the current 15\-minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatscurrupsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that transitioned to the UP state during the current 15\-minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatscurrauthsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that transitioned from the UNAUTHENTICATED to the AUTHENTICATED state during the current 15\-minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatscurrdiscsessions
            
            	This object indicates the total number of subscriber sessions terminated due to a disconnect event during the current 15\-minute interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsdiscontinuitytime
            
            	The date and time (as determined by the system's clock) of the most recent occurrence of an event affecting the  continuity of the aggregation statistics for this aggregation  point
            	**type**\: str
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsTable.CsubAggStatsEntry, self).__init__()

                self.yang_name = "csubAggStatsEntry"
                self.yang_parent_name = "csubAggStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csubaggstatspointtype','csubaggstatspoint','csubaggstatssessiontype']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csubaggstatspointtype', (YLeaf(YType.enumeration, 'csubAggStatsPointType'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CISCOSUBSCRIBERSESSIONMIB', 'CsubAggStatsTable.CsubAggStatsEntry.CsubAggStatsPointType')])),
                    ('csubaggstatspoint', (YLeaf(YType.uint32, 'csubAggStatsPoint'), ['int'])),
                    ('csubaggstatssessiontype', (YLeaf(YType.enumeration, 'csubAggStatsSessionType'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB', 'SubSessionType', '')])),
                    ('csubaggstatspendingsessions', (YLeaf(YType.uint32, 'csubAggStatsPendingSessions'), ['int'])),
                    ('csubaggstatsupsessions', (YLeaf(YType.uint32, 'csubAggStatsUpSessions'), ['int'])),
                    ('csubaggstatsauthsessions', (YLeaf(YType.uint32, 'csubAggStatsAuthSessions'), ['int'])),
                    ('csubaggstatsunauthsessions', (YLeaf(YType.uint32, 'csubAggStatsUnAuthSessions'), ['int'])),
                    ('csubaggstatslightweightsessions', (YLeaf(YType.uint32, 'csubAggStatsLightWeightSessions'), ['int'])),
                    ('csubaggstatsredsessions', (YLeaf(YType.uint32, 'csubAggStatsRedSessions'), ['int'])),
                    ('csubaggstatshighupsessions', (YLeaf(YType.uint32, 'csubAggStatsHighUpSessions'), ['int'])),
                    ('csubaggstatsavgsessionuptime', (YLeaf(YType.uint32, 'csubAggStatsAvgSessionUptime'), ['int'])),
                    ('csubaggstatsavgsessionrpm', (YLeaf(YType.uint32, 'csubAggStatsAvgSessionRPM'), ['int'])),
                    ('csubaggstatsavgsessionrph', (YLeaf(YType.uint32, 'csubAggStatsAvgSessionRPH'), ['int'])),
                    ('csubaggstatsthrottleengagements', (YLeaf(YType.uint64, 'csubAggStatsThrottleEngagements'), ['int'])),
                    ('csubaggstatstotalcreatedsessions', (YLeaf(YType.uint64, 'csubAggStatsTotalCreatedSessions'), ['int'])),
                    ('csubaggstatstotalfailedsessions', (YLeaf(YType.uint64, 'csubAggStatsTotalFailedSessions'), ['int'])),
                    ('csubaggstatstotalupsessions', (YLeaf(YType.uint64, 'csubAggStatsTotalUpSessions'), ['int'])),
                    ('csubaggstatstotalauthsessions', (YLeaf(YType.uint64, 'csubAggStatsTotalAuthSessions'), ['int'])),
                    ('csubaggstatstotaldiscsessions', (YLeaf(YType.uint64, 'csubAggStatsTotalDiscSessions'), ['int'])),
                    ('csubaggstatstotallightweightsessions', (YLeaf(YType.uint64, 'csubAggStatsTotalLightWeightSessions'), ['int'])),
                    ('csubaggstatstotalflowsup', (YLeaf(YType.uint64, 'csubAggStatsTotalFlowsUp'), ['int'])),
                    ('csubaggstatsdaycreatedsessions', (YLeaf(YType.uint32, 'csubAggStatsDayCreatedSessions'), ['int'])),
                    ('csubaggstatsdayfailedsessions', (YLeaf(YType.uint32, 'csubAggStatsDayFailedSessions'), ['int'])),
                    ('csubaggstatsdayupsessions', (YLeaf(YType.uint32, 'csubAggStatsDayUpSessions'), ['int'])),
                    ('csubaggstatsdayauthsessions', (YLeaf(YType.uint32, 'csubAggStatsDayAuthSessions'), ['int'])),
                    ('csubaggstatsdaydiscsessions', (YLeaf(YType.uint32, 'csubAggStatsDayDiscSessions'), ['int'])),
                    ('csubaggstatscurrtimeelapsed', (YLeaf(YType.uint32, 'csubAggStatsCurrTimeElapsed'), ['int'])),
                    ('csubaggstatscurrvalidintervals', (YLeaf(YType.uint32, 'csubAggStatsCurrValidIntervals'), ['int'])),
                    ('csubaggstatscurrinvalidintervals', (YLeaf(YType.uint32, 'csubAggStatsCurrInvalidIntervals'), ['int'])),
                    ('csubaggstatscurrflowsup', (YLeaf(YType.uint32, 'csubAggStatsCurrFlowsUp'), ['int'])),
                    ('csubaggstatscurrcreatedsessions', (YLeaf(YType.uint32, 'csubAggStatsCurrCreatedSessions'), ['int'])),
                    ('csubaggstatscurrfailedsessions', (YLeaf(YType.uint32, 'csubAggStatsCurrFailedSessions'), ['int'])),
                    ('csubaggstatscurrupsessions', (YLeaf(YType.uint32, 'csubAggStatsCurrUpSessions'), ['int'])),
                    ('csubaggstatscurrauthsessions', (YLeaf(YType.uint32, 'csubAggStatsCurrAuthSessions'), ['int'])),
                    ('csubaggstatscurrdiscsessions', (YLeaf(YType.uint32, 'csubAggStatsCurrDiscSessions'), ['int'])),
                    ('csubaggstatsdiscontinuitytime', (YLeaf(YType.str, 'csubAggStatsDiscontinuityTime'), ['str'])),
                ])
                self.csubaggstatspointtype = None
                self.csubaggstatspoint = None
                self.csubaggstatssessiontype = None
                self.csubaggstatspendingsessions = None
                self.csubaggstatsupsessions = None
                self.csubaggstatsauthsessions = None
                self.csubaggstatsunauthsessions = None
                self.csubaggstatslightweightsessions = None
                self.csubaggstatsredsessions = None
                self.csubaggstatshighupsessions = None
                self.csubaggstatsavgsessionuptime = None
                self.csubaggstatsavgsessionrpm = None
                self.csubaggstatsavgsessionrph = None
                self.csubaggstatsthrottleengagements = None
                self.csubaggstatstotalcreatedsessions = None
                self.csubaggstatstotalfailedsessions = None
                self.csubaggstatstotalupsessions = None
                self.csubaggstatstotalauthsessions = None
                self.csubaggstatstotaldiscsessions = None
                self.csubaggstatstotallightweightsessions = None
                self.csubaggstatstotalflowsup = None
                self.csubaggstatsdaycreatedsessions = None
                self.csubaggstatsdayfailedsessions = None
                self.csubaggstatsdayupsessions = None
                self.csubaggstatsdayauthsessions = None
                self.csubaggstatsdaydiscsessions = None
                self.csubaggstatscurrtimeelapsed = None
                self.csubaggstatscurrvalidintervals = None
                self.csubaggstatscurrinvalidintervals = None
                self.csubaggstatscurrflowsup = None
                self.csubaggstatscurrcreatedsessions = None
                self.csubaggstatscurrfailedsessions = None
                self.csubaggstatscurrupsessions = None
                self.csubaggstatscurrauthsessions = None
                self.csubaggstatscurrdiscsessions = None
                self.csubaggstatsdiscontinuitytime = None
                self._segment_path = lambda: "csubAggStatsEntry" + "[csubAggStatsPointType='" + str(self.csubaggstatspointtype) + "']" + "[csubAggStatsPoint='" + str(self.csubaggstatspoint) + "']" + "[csubAggStatsSessionType='" + str(self.csubaggstatssessiontype) + "']"
                self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubAggStatsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsTable.CsubAggStatsEntry, ['csubaggstatspointtype', 'csubaggstatspoint', 'csubaggstatssessiontype', 'csubaggstatspendingsessions', 'csubaggstatsupsessions', 'csubaggstatsauthsessions', 'csubaggstatsunauthsessions', 'csubaggstatslightweightsessions', 'csubaggstatsredsessions', 'csubaggstatshighupsessions', 'csubaggstatsavgsessionuptime', 'csubaggstatsavgsessionrpm', 'csubaggstatsavgsessionrph', 'csubaggstatsthrottleengagements', 'csubaggstatstotalcreatedsessions', 'csubaggstatstotalfailedsessions', 'csubaggstatstotalupsessions', 'csubaggstatstotalauthsessions', 'csubaggstatstotaldiscsessions', 'csubaggstatstotallightweightsessions', 'csubaggstatstotalflowsup', 'csubaggstatsdaycreatedsessions', 'csubaggstatsdayfailedsessions', 'csubaggstatsdayupsessions', 'csubaggstatsdayauthsessions', 'csubaggstatsdaydiscsessions', 'csubaggstatscurrtimeelapsed', 'csubaggstatscurrvalidintervals', 'csubaggstatscurrinvalidintervals', 'csubaggstatscurrflowsup', 'csubaggstatscurrcreatedsessions', 'csubaggstatscurrfailedsessions', 'csubaggstatscurrupsessions', 'csubaggstatscurrauthsessions', 'csubaggstatscurrdiscsessions', 'csubaggstatsdiscontinuitytime'], name, value)

            class CsubAggStatsPointType(Enum):
                """
                CsubAggStatsPointType (Enum Class)

                This object indicates format of the csubAggStatsPoint

                for this entry. 

                The format for the csubAggStatsPoint is as follows\: 

                csubAggStatsPointType      csubAggStatsPoint 

                \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-     \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\- 

                    'physical'                 PhysicalIndex 

                    'interface'                InterfaceIndex

                .. data:: physical = 1

                .. data:: interface = 2

                """

                physical = Enum.YLeaf(1, "physical")

                interface = Enum.YLeaf(2, "interface")





    class CsubAggStatsIntTable(Entity):
        """
        This table contains aggregated subscriber session performance
        data collected for as much as a day's worth of 15\-minute
        measurement intervals.
        
        This table has an expansion dependent relationship on the
        csubAggStatsTable, containing zero or more rows for each row
        contained by the csubAggStatsTable.
        
        Observe that the collection and maintenance of aggregated
        subscriber performance data is OPTIONAL for all scopes of
        aggregation.  However, an implementation should maintain at
        least one interval for the 'scope of aggregation' that contains
        all subscriber sessions maintained by the system.
        
        .. attribute:: csubaggstatsintentry
        
        	An entry contains the aggregated subscriber session performance data collected over a single 15\-minute measurement interval within a 'scope of aggregation'.  For further details regarding 'scope of aggregation', see the descriptive text associated with the csubAggStatsEntry
        	**type**\: list of  		 :py:class:`CsubAggStatsIntEntry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsIntTable.CsubAggStatsIntEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsIntTable, self).__init__()

            self.yang_name = "csubAggStatsIntTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("csubAggStatsIntEntry", ("csubaggstatsintentry", CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsIntTable.CsubAggStatsIntEntry))])
            self._leafs = OrderedDict()

            self.csubaggstatsintentry = YList(self)
            self._segment_path = lambda: "csubAggStatsIntTable"
            self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsIntTable, [], name, value)


        class CsubAggStatsIntEntry(Entity):
            """
            An entry contains the aggregated subscriber session performance
            data collected over a single 15\-minute measurement interval
            within a 'scope of aggregation'.  For further details regarding
            'scope of aggregation', see the descriptive text associated with
            the csubAggStatsEntry.
            
            .. attribute:: csubaggstatspointtype  (key)
            
            	
            	**type**\:  :py:class:`CsubAggStatsPointType <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsTable.CsubAggStatsEntry.CsubAggStatsPointType>`
            
            	**config**\: False
            
            .. attribute:: csubaggstatspoint  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`csubaggstatspoint <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsTable.CsubAggStatsEntry>`
            
            	**config**\: False
            
            .. attribute:: csubaggstatssessiontype  (key)
            
            	
            	**type**\:  :py:class:`SubSessionType <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB.SubSessionType>`
            
            	**config**\: False
            
            .. attribute:: csubaggstatsintnumber  (key)
            
            	This object indicates the interval number identifying the 15\-minute measurement interval for which aggregated subscriber session performance data was successfully collected by the system.  The interval identified by the value '1' represents the most recent 15\-minute measurement interval, and the interval identified by the value (n) represents the interval immediately preceding the interval identified by the value (n\-1)
            	**type**\: int
            
            	**range:** 1..96
            
            	**config**\: False
            
            .. attribute:: csubaggstatsintvalid
            
            	This object indicates whether the data for the 15\-minute measurement interval is valid
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: csubaggstatsintcreatedsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' created during the 15\-minute measurement interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsintfailedsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that were in the PENDING state and terminated for reasons other than disconnect during the 15\-minute measurement interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsintupsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that transitioned to the UP state during the 15\-minute measurement interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsintauthsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that transitioned from the UNAUTHENTICATED to the AUTHENTICATED state during the 15\-minute measurement interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsintdiscsessions
            
            	This object indicates the total number of subscriber sessions terminated due to a disconnect event during the 15\-minute measurement interval
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: sessions
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsIntTable.CsubAggStatsIntEntry, self).__init__()

                self.yang_name = "csubAggStatsIntEntry"
                self.yang_parent_name = "csubAggStatsIntTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csubaggstatspointtype','csubaggstatspoint','csubaggstatssessiontype','csubaggstatsintnumber']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csubaggstatspointtype', (YLeaf(YType.enumeration, 'csubAggStatsPointType'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CISCOSUBSCRIBERSESSIONMIB', 'CsubAggStatsTable.CsubAggStatsEntry.CsubAggStatsPointType')])),
                    ('csubaggstatspoint', (YLeaf(YType.str, 'csubAggStatsPoint'), ['int'])),
                    ('csubaggstatssessiontype', (YLeaf(YType.enumeration, 'csubAggStatsSessionType'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB', 'SubSessionType', '')])),
                    ('csubaggstatsintnumber', (YLeaf(YType.uint32, 'csubAggStatsIntNumber'), ['int'])),
                    ('csubaggstatsintvalid', (YLeaf(YType.boolean, 'csubAggStatsIntValid'), ['bool'])),
                    ('csubaggstatsintcreatedsessions', (YLeaf(YType.uint32, 'csubAggStatsIntCreatedSessions'), ['int'])),
                    ('csubaggstatsintfailedsessions', (YLeaf(YType.uint32, 'csubAggStatsIntFailedSessions'), ['int'])),
                    ('csubaggstatsintupsessions', (YLeaf(YType.uint32, 'csubAggStatsIntUpSessions'), ['int'])),
                    ('csubaggstatsintauthsessions', (YLeaf(YType.uint32, 'csubAggStatsIntAuthSessions'), ['int'])),
                    ('csubaggstatsintdiscsessions', (YLeaf(YType.uint32, 'csubAggStatsIntDiscSessions'), ['int'])),
                ])
                self.csubaggstatspointtype = None
                self.csubaggstatspoint = None
                self.csubaggstatssessiontype = None
                self.csubaggstatsintnumber = None
                self.csubaggstatsintvalid = None
                self.csubaggstatsintcreatedsessions = None
                self.csubaggstatsintfailedsessions = None
                self.csubaggstatsintupsessions = None
                self.csubaggstatsintauthsessions = None
                self.csubaggstatsintdiscsessions = None
                self._segment_path = lambda: "csubAggStatsIntEntry" + "[csubAggStatsPointType='" + str(self.csubaggstatspointtype) + "']" + "[csubAggStatsPoint='" + str(self.csubaggstatspoint) + "']" + "[csubAggStatsSessionType='" + str(self.csubaggstatssessiontype) + "']" + "[csubAggStatsIntNumber='" + str(self.csubaggstatsintnumber) + "']"
                self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubAggStatsIntTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsIntTable.CsubAggStatsIntEntry, ['csubaggstatspointtype', 'csubaggstatspoint', 'csubaggstatssessiontype', 'csubaggstatsintnumber', 'csubaggstatsintvalid', 'csubaggstatsintcreatedsessions', 'csubaggstatsintfailedsessions', 'csubaggstatsintupsessions', 'csubaggstatsintauthsessions', 'csubaggstatsintdiscsessions'], name, value)




    class CsubAggStatsThreshTable(Entity):
        """
        Please enter the Table Description here.
        
        .. attribute:: csubaggstatsthreshentry
        
        	A row in this table exists for each row in the csubAggStatsTable. Each row defines the set of thresholds and evaluation attributes for an aggregation point
        	**type**\: list of  		 :py:class:`CsubAggStatsThreshEntry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsThreshTable.CsubAggStatsThreshEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsThreshTable, self).__init__()

            self.yang_name = "csubAggStatsThreshTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("csubAggStatsThreshEntry", ("csubaggstatsthreshentry", CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsThreshTable.CsubAggStatsThreshEntry))])
            self._leafs = OrderedDict()

            self.csubaggstatsthreshentry = YList(self)
            self._segment_path = lambda: "csubAggStatsThreshTable"
            self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsThreshTable, [], name, value)


        class CsubAggStatsThreshEntry(Entity):
            """
            A row in this table exists for each row in the
            csubAggStatsTable.
            Each row defines the set of thresholds and evaluation attributes
            for an aggregation point.
            
            .. attribute:: csubsessionrisingthresh  (key)
            
            	This threshold, if non\-zero, indicates the rising threshold for the value of csubAggStatsUpSessions for the aggregation point, When the current sample of csubAggStatsUpSessions is greater than or equal to this threshold, and the value of csubAggStatsUpSessions for the last sample interval was less than this thershold, the csubSessionRisingNotif is triggered.           If the value of this threshold is 0, the threshold is not evaluated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: csubsessionfallingthresh
            
            	This threshold, if non\-zero, indicates the falling threshold for the value of csubAggStatsUpSessions for the aggregation point, When the current sample of csubAggStatsUpSessions is less than or equal to this threshold, and the value of csubAggStatsUpSessions for the last sample interval was greater than this thershold, the csubSessionFallingNotif is triggered.           If the value of this threshold is 0, the threshold is not evaluated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: csubsessiondeltapercentfallingthresh
            
            	This threshold, if non\-zero, indicates the delta falling threshold as a percentage of the value of csubAggStatsUpSessions for the aggregation point, The delta as a percentage of csubAggStatsUpSessions (delta\_percent) is calculated as follows\:       current value of csubAggStatsUpSessions = value(n)              previous sampled value of csubAggStatsUpSessions = value(n\-1)               delta\_percent = ((value(n\-1) \- value(n)) / value(n\-1)) \* 100           If the delta\_percent value of the current evaluation interval is          greater than the value of this threshold, a          csubSessionDeltaPercentLossNotif is triggered.           If the value of this threshold is 0, the threshold is not evaluated
            	**type**\: int
            
            	**range:** 0..100
            
            	**config**\: False
            
            .. attribute:: csubsessionthreshevalinterval
            
            	The value of this object sets the number of seconds between samples for threshold evaluation. For implementations capable of per\-session event evaluation of thresholds this object represents the maximum number of seconds between samples
            	**type**\: int
            
            	**range:** 0..900
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsThreshTable.CsubAggStatsThreshEntry, self).__init__()

                self.yang_name = "csubAggStatsThreshEntry"
                self.yang_parent_name = "csubAggStatsThreshTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csubsessionrisingthresh']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csubsessionrisingthresh', (YLeaf(YType.uint32, 'csubSessionRisingThresh'), ['int'])),
                    ('csubsessionfallingthresh', (YLeaf(YType.uint32, 'csubSessionFallingThresh'), ['int'])),
                    ('csubsessiondeltapercentfallingthresh', (YLeaf(YType.uint32, 'csubSessionDeltaPercentFallingThresh'), ['int'])),
                    ('csubsessionthreshevalinterval', (YLeaf(YType.uint32, 'csubSessionThreshEvalInterval'), ['int'])),
                ])
                self.csubsessionrisingthresh = None
                self.csubsessionfallingthresh = None
                self.csubsessiondeltapercentfallingthresh = None
                self.csubsessionthreshevalinterval = None
                self._segment_path = lambda: "csubAggStatsThreshEntry" + "[csubSessionRisingThresh='" + str(self.csubsessionrisingthresh) + "']"
                self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubAggStatsThreshTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubAggStatsThreshTable.CsubAggStatsThreshEntry, ['csubsessionrisingthresh', 'csubsessionfallingthresh', 'csubsessiondeltapercentfallingthresh', 'csubsessionthreshevalinterval'], name, value)




    class CsubJobTable(Entity):
        """
        This table contains the subscriber session jobs submitted by
        the EMS/NMS.
        
        .. attribute:: csubjobentry
        
        	An entry describing a subscriber session job.  At this time, subscriber session jobs can perform one of two tasks\:  \- Subscriber Session Query     This type of job invokes the report generator, which builds     a list of subscriber sessions matching criteria specified by     the corresponding row in the csubJobMatchParamsTable.  The     list built by the report generator must conform to     parameters specified by the corresponding row in     csubJobQueryParamsTable, which at this time only affects     sorting order.  \- Subscriber Session Clear     This type of job causes the system to terminate those     subscriber sessions matching criteria specified by the     corresponding row in the csubJobMatchParamsTable.  The following procedure summarizes how the EMS/NMS can start and monitor a subscriber session job\:  1)  The EMS/NMS must start by reading csubJobIdNext.  If it is     zero, continue polling csubJobIdNext until it is non\-zero.  2)  The EMS/NMS creates a row in the csubJobTable using the     instance identifier retrieved in the last step.  Since every     object contained by the entry with a MAX\-ACCESS of      'read\-create' specifies a default value, it makes little     difference whether the EMS/NMS employs create\-and\-wait or     create\-and\-go semantics.  3)  The EMS/NMS sets the type of subscriber session job by     setting the corresponding instance of csubJobType.  4a) If the job is a 'query', then the EMS/NMS must configure     the query before starting it by setting columns contained     by the corresponding rows in the csubJobMatchParamsTable and     csubJobQueryParamsTable.  4b) If job is a 'clear', then the EMS/NMS must configure     the job before starting it by setting columns contained by     the corresponding row in the csubJobMatchParamsTable.  5)  The EMS/NMS can now start the job by setting the      corresponding instance of csubJobControl to 'start'.  6)  The EMS/NMS can monitor the progress of the job by polling     the corresponding instance of csubJobState.  It can also     wait for a csubJobFinishedNotify notification.  When the     state of the job transitions to 'finished', then the system     has finished executing the job.  7)  The EMS/NMS can determine the final status of the job by     reading the corresponding instance of csubJobFinishedReason.     If job is a 'query' and the corresponding instance of     csubJobFinishedReason is 'normal', then the EMS/NMS can     safely read the report by retrieving the corresponding     rows from the csubJobReportTable.  8a) After a job has finished, the EMS/NMS has the option of     destroying it.  It can do this by simply setting the     corresponding instance of  csubJobStatus to 'destroy'.     Alternatively, the EMS/NMS may retain the job and execute it     again in the future (by returning to step 5).  Additionally,     nothing would prevent the EMS/NMS from changing the job's     type, which causes the automatic destruction of the     corresponding report.  8b) If the job is a 'query' and the EMS/NMS opts to retain the     job, then it may consider releasing the corresponding report     after reading it.  It can do this by setting the     corresponding instance of csubJobControl to 'release'
        	**type**\: list of  		 :py:class:`CsubJobEntry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJobTable.CsubJobEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CISCOSUBSCRIBERSESSIONMIB.CsubJobTable, self).__init__()

            self.yang_name = "csubJobTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("csubJobEntry", ("csubjobentry", CISCOSUBSCRIBERSESSIONMIB.CsubJobTable.CsubJobEntry))])
            self._leafs = OrderedDict()

            self.csubjobentry = YList(self)
            self._segment_path = lambda: "csubJobTable"
            self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubJobTable, [], name, value)


        class CsubJobEntry(Entity):
            """
            An entry describing a subscriber session job.  At this time,
            subscriber session jobs can perform one of two tasks\:
            
            \- Subscriber Session Query
                This type of job invokes the report generator, which builds
                a list of subscriber sessions matching criteria specified by
                the corresponding row in the csubJobMatchParamsTable.  The
                list built by the report generator must conform to
                parameters specified by the corresponding row in
                csubJobQueryParamsTable, which at this time only affects
                sorting order.
            
            \- Subscriber Session Clear
                This type of job causes the system to terminate those
                subscriber sessions matching criteria specified by the
                corresponding row in the csubJobMatchParamsTable.
            
            The following procedure summarizes how the EMS/NMS can start and
            monitor a subscriber session job\:
            
            1)  The EMS/NMS must start by reading csubJobIdNext.  If it is
                zero, continue polling csubJobIdNext until it is non\-zero.
            
            2)  The EMS/NMS creates a row in the csubJobTable using the
                instance identifier retrieved in the last step.  Since every
                object contained by the entry with a MAX\-ACCESS of 
                'read\-create' specifies a default value, it makes little
                difference whether the EMS/NMS employs create\-and\-wait or
                create\-and\-go semantics.
            
            3)  The EMS/NMS sets the type of subscriber session job by
                setting the corresponding instance of csubJobType.
            
            4a) If the job is a 'query', then the EMS/NMS must configure
                the query before starting it by setting columns contained
                by the corresponding rows in the csubJobMatchParamsTable and
                csubJobQueryParamsTable.
            
            4b) If job is a 'clear', then the EMS/NMS must configure
                the job before starting it by setting columns contained by
                the corresponding row in the csubJobMatchParamsTable.
            
            5)  The EMS/NMS can now start the job by setting the 
                corresponding instance of csubJobControl to 'start'.
            
            6)  The EMS/NMS can monitor the progress of the job by polling
                the corresponding instance of csubJobState.  It can also
                wait for a csubJobFinishedNotify notification.  When the
                state of the job transitions to 'finished', then the system
                has finished executing the job.
            
            7)  The EMS/NMS can determine the final status of the job by
                reading the corresponding instance of csubJobFinishedReason.
                If job is a 'query' and the corresponding instance of
                csubJobFinishedReason is 'normal', then the EMS/NMS can
                safely read the report by retrieving the corresponding
                rows from the csubJobReportTable.
            
            8a) After a job has finished, the EMS/NMS has the option of
                destroying it.  It can do this by simply setting the
                corresponding instance of  csubJobStatus to 'destroy'.
                Alternatively, the EMS/NMS may retain the job and execute it
                again in the future (by returning to step 5).  Additionally,
                nothing would prevent the EMS/NMS from changing the job's
                type, which causes the automatic destruction of the
                corresponding report.
            
            8b) If the job is a 'query' and the EMS/NMS opts to retain the
                job, then it may consider releasing the corresponding report
                after reading it.  It can do this by setting the
                corresponding instance of csubJobControl to 'release'.
            
            .. attribute:: csubjobid  (key)
            
            	This object indicates an arbitrary, positive integer\-value uniquely identifying the subscriber session job
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: csubjobstatus
            
            	This object specifies the status of the subscriber session job.  The following columns must be valid before activating a subscriber session job\:      \- csubJobStorage     \- csubJobType     \- csubJobControl  However, these objects specify a default value.  Thus, it is possible to use create\-and\-go semantics without setting any additional columns.  An implementation must allow the EMS/NMS to modify any column when this column is 'active', including columns defined in tables that have a one\-to\-one or sparse dependent relationship on this table
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: csubjobstorage
            
            	This object specifies what happens to the subscriber session job upon restart
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            	**config**\: False
            
            .. attribute:: csubjobtype
            
            	This object specifies the type of subscriber session job\:  'noop'     This type of job does nothing and simply serves as a     convenient default value for newly created jobs, thereby     allowing create\-and\-go row creation without having to     specify the type of job.  'query'     This type of job starts a subscriber session query.  The     system searches for any subscriber sessions matching the     configured criteria and sorts them into a resulting     report.      Upon activation of a subscriber session with this value,     the system automatically creates corresponding rows in     the csubJobMatchParamsTable and csubQueryParamsTable.  'clear'     This type of job causes the system to terminated all     subscriber sessions matching configured criteria.      Upon activation of a subscriber session with this value,     the system automatically creates a corresponding row in     the csubJobMatchParamsTable
            	**type**\:  :py:class:`CsubJobType <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJobTable.CsubJobEntry.CsubJobType>`
            
            	**config**\: False
            
            .. attribute:: csubjobcontrol
            
            	This object specifies an action relating to the subscriber session job\:      'noop'         This action does nothing.      'start'         If the corresponding instance of csubJobType is 'noop',         then this action simply causes the system to set the         corresponding instances of csubJobState and         csubJobFinishedReason to 'finished' and 'normal',         respectively.          If the corresponding instance of csubJobType is not         'noop' and the system is not executing a subscriber         session job, then this action causes the system         immediately execute the subscriber session job.          If the corresponding instance of csubJobType is not         'noop' and the system is already executing a subscriber         session job, then this action causes the system to put         the job on the subscriber session job queue.      'abort'         If the subscriber session job is in the subscriber         session job queue, then this action causes the system to         remove the job from the queue.          If the system is executing the subscriber session job,         then this action causes the system to stop the job.      'release'         This action causes the system to destroy any         corresponding rows in the csubJobReportTable.          The system only accepts this action for a previously         executed subscriber session job having a corresponding         instance of csubJobType set to 'query'.  Any attempt to         issue this action under other circumstances will result         in a response indicating an  error\-status of         'inconsistentValue'.  When read, this column is always 'noop'
            	**type**\:  :py:class:`CsubJobControl <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJobTable.CsubJobEntry.CsubJobControl>`
            
            	**config**\: False
            
            .. attribute:: csubjobstate
            
            	This object indicates the current state of the subscriber session job\:      'idle'         This state indicates that the system has not executed         the subscriber session job since it was created.      'pending'         This state indicates that the subscriber session job is         waiting in the subscriber session job queue.      'inProgress'         This state indicates that the system is executing the         subscriber session job.  Observe that the system may         execute more than one subscriber session job at a time.      'finished'         This state indicates that the system has executed the         subscriber session job and it has finished.  The         corresponding instance of csubJobFinishedReason         indicates further details regarding the reason why the         job finished
            	**type**\:  :py:class:`CsubJobState <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJobTable.CsubJobEntry.CsubJobState>`
            
            	**config**\: False
            
            .. attribute:: csubjobstartedtime
            
            	This object indicates the value of sysUpTime when the system started executing the subscriber session job.  This value will be '0' when the corresponding instance of csubJobState is 'idle' or 'pending'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: csubjobfinishedtime
            
            	This object indicates the value of sysUpTime when the system finished executing the subscriber session job, for whatever reason.  This value will be '0' when the corresponding instance of csubJobState is 'idle', 'pending', or 'inProgress'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: csubjobfinishedreason
            
            	This object indicates the reason why the system finished executing the subscriber session job\:      'invalid'         Indicates that the corresponding instance of         csubJobState is either 'idle', 'pending', or         'inProgress'.      'other'         Indicates that the system finished executing the         subscriber session job abnormally for a reason not         recognized by this MIB module.      'normal'         Indicates that the system finished executing the         subscriber session job with no problems.      'aborted'         Indicates that the system finished executing the         subscriber session job as the result of the EMS/NMS         writing 'abort' to the corresponding instance of         csubJobControl.      'insufficientResources'         Indicates that the system finished executing the         subscriber session job abnormally due to insufficient         resources to continue.      'error'         Indicates that the system encountered an error that         prevented it from completing the job
            	**type**\:  :py:class:`CsubJobFinishedReason <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJobTable.CsubJobEntry.CsubJobFinishedReason>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CISCOSUBSCRIBERSESSIONMIB.CsubJobTable.CsubJobEntry, self).__init__()

                self.yang_name = "csubJobEntry"
                self.yang_parent_name = "csubJobTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csubjobid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csubjobid', (YLeaf(YType.uint32, 'csubJobId'), ['int'])),
                    ('csubjobstatus', (YLeaf(YType.enumeration, 'csubJobStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('csubjobstorage', (YLeaf(YType.enumeration, 'csubJobStorage'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'StorageType', '')])),
                    ('csubjobtype', (YLeaf(YType.enumeration, 'csubJobType'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CISCOSUBSCRIBERSESSIONMIB', 'CsubJobTable.CsubJobEntry.CsubJobType')])),
                    ('csubjobcontrol', (YLeaf(YType.enumeration, 'csubJobControl'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CISCOSUBSCRIBERSESSIONMIB', 'CsubJobTable.CsubJobEntry.CsubJobControl')])),
                    ('csubjobstate', (YLeaf(YType.enumeration, 'csubJobState'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CISCOSUBSCRIBERSESSIONMIB', 'CsubJobTable.CsubJobEntry.CsubJobState')])),
                    ('csubjobstartedtime', (YLeaf(YType.uint32, 'csubJobStartedTime'), ['int'])),
                    ('csubjobfinishedtime', (YLeaf(YType.uint32, 'csubJobFinishedTime'), ['int'])),
                    ('csubjobfinishedreason', (YLeaf(YType.enumeration, 'csubJobFinishedReason'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB', 'CISCOSUBSCRIBERSESSIONMIB', 'CsubJobTable.CsubJobEntry.CsubJobFinishedReason')])),
                ])
                self.csubjobid = None
                self.csubjobstatus = None
                self.csubjobstorage = None
                self.csubjobtype = None
                self.csubjobcontrol = None
                self.csubjobstate = None
                self.csubjobstartedtime = None
                self.csubjobfinishedtime = None
                self.csubjobfinishedreason = None
                self._segment_path = lambda: "csubJobEntry" + "[csubJobId='" + str(self.csubjobid) + "']"
                self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubJobTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubJobTable.CsubJobEntry, ['csubjobid', 'csubjobstatus', 'csubjobstorage', 'csubjobtype', 'csubjobcontrol', 'csubjobstate', 'csubjobstartedtime', 'csubjobfinishedtime', 'csubjobfinishedreason'], name, value)

            class CsubJobControl(Enum):
                """
                CsubJobControl (Enum Class)

                This object specifies an action relating to the subscriber

                session job\:

                    'noop'

                        This action does nothing.

                    'start'

                        If the corresponding instance of csubJobType is 'noop',

                        then this action simply causes the system to set the

                        corresponding instances of csubJobState and

                        csubJobFinishedReason to 'finished' and 'normal',

                        respectively.

                        If the corresponding instance of csubJobType is not

                        'noop' and the system is not executing a subscriber

                        session job, then this action causes the system

                        immediately execute the subscriber session job.

                        If the corresponding instance of csubJobType is not

                        'noop' and the system is already executing a subscriber

                        session job, then this action causes the system to put

                        the job on the subscriber session job queue.

                    'abort'

                        If the subscriber session job is in the subscriber

                        session job queue, then this action causes the system to

                        remove the job from the queue.

                        If the system is executing the subscriber session job,

                        then this action causes the system to stop the job.

                    'release'

                        This action causes the system to destroy any

                        corresponding rows in the csubJobReportTable.

                        The system only accepts this action for a previously

                        executed subscriber session job having a corresponding

                        instance of csubJobType set to 'query'.  Any attempt to

                        issue this action under other circumstances will result

                        in a response indicating an  error\-status of

                        'inconsistentValue'.

                When read, this column is always 'noop'.

                .. data:: noop = 1

                .. data:: start = 2

                .. data:: abort = 3

                .. data:: release = 4

                """

                noop = Enum.YLeaf(1, "noop")

                start = Enum.YLeaf(2, "start")

                abort = Enum.YLeaf(3, "abort")

                release = Enum.YLeaf(4, "release")


            class CsubJobFinishedReason(Enum):
                """
                CsubJobFinishedReason (Enum Class)

                This object indicates the reason why the system finished

                executing the subscriber session job\:

                    'invalid'

                        Indicates that the corresponding instance of

                        csubJobState is either 'idle', 'pending', or

                        'inProgress'.

                    'other'

                        Indicates that the system finished executing the

                        subscriber session job abnormally for a reason not

                        recognized by this MIB module.

                    'normal'

                        Indicates that the system finished executing the

                        subscriber session job with no problems.

                    'aborted'

                        Indicates that the system finished executing the

                        subscriber session job as the result of the EMS/NMS

                        writing 'abort' to the corresponding instance of

                        csubJobControl.

                    'insufficientResources'

                        Indicates that the system finished executing the

                        subscriber session job abnormally due to insufficient

                        resources to continue.

                    'error'

                        Indicates that the system encountered an error that

                        prevented it from completing the job.

                .. data:: invalid = 1

                .. data:: other = 2

                .. data:: normal = 3

                .. data:: aborted = 4

                .. data:: insufficientResources = 5

                .. data:: error = 6

                """

                invalid = Enum.YLeaf(1, "invalid")

                other = Enum.YLeaf(2, "other")

                normal = Enum.YLeaf(3, "normal")

                aborted = Enum.YLeaf(4, "aborted")

                insufficientResources = Enum.YLeaf(5, "insufficientResources")

                error = Enum.YLeaf(6, "error")


            class CsubJobState(Enum):
                """
                CsubJobState (Enum Class)

                This object indicates the current state of the subscriber

                session job\:

                    'idle'

                        This state indicates that the system has not executed

                        the subscriber session job since it was created.

                    'pending'

                        This state indicates that the subscriber session job is

                        waiting in the subscriber session job queue.

                    'inProgress'

                        This state indicates that the system is executing the

                        subscriber session job.  Observe that the system may

                        execute more than one subscriber session job at a time.

                    'finished'

                        This state indicates that the system has executed the

                        subscriber session job and it has finished.  The

                        corresponding instance of csubJobFinishedReason

                        indicates further details regarding the reason why the

                        job finished.

                .. data:: idle = 1

                .. data:: pending = 2

                .. data:: inProgress = 3

                .. data:: finished = 4

                """

                idle = Enum.YLeaf(1, "idle")

                pending = Enum.YLeaf(2, "pending")

                inProgress = Enum.YLeaf(3, "inProgress")

                finished = Enum.YLeaf(4, "finished")


            class CsubJobType(Enum):
                """
                CsubJobType (Enum Class)

                This object specifies the type of subscriber session job\:

                'noop'

                    This type of job does nothing and simply serves as a

                    convenient default value for newly created jobs, thereby

                    allowing create\-and\-go row creation without having to

                    specify the type of job.

                'query'

                    This type of job starts a subscriber session query.  The

                    system searches for any subscriber sessions matching the

                    configured criteria and sorts them into a resulting

                    report.

                    Upon activation of a subscriber session with this value,

                    the system automatically creates corresponding rows in

                    the csubJobMatchParamsTable and csubQueryParamsTable.

                'clear'

                    This type of job causes the system to terminated all

                    subscriber sessions matching configured criteria.

                    Upon activation of a subscriber session with this value,

                    the system automatically creates a corresponding row in

                    the csubJobMatchParamsTable.

                .. data:: noop = 1

                .. data:: query = 2

                .. data:: clear = 3

                """

                noop = Enum.YLeaf(1, "noop")

                query = Enum.YLeaf(2, "query")

                clear = Enum.YLeaf(3, "clear")





    class CsubJobMatchParamsTable(Entity):
        """
        This table contains subscriber session job parameters
        describing match criteria.
        
        This table has a sparse\-dependent relationship on the
        csubJobTable, containing a row for each job having a
        csubJobType of 'query' or 'clear'.
        
        .. attribute:: csubjobmatchparamsentry
        
        	An entry describes a set of subscriber session match criteria. The set contains those subscriber session identities specified by csubJobMatchIdentities.  If the corresponding row in the csubJobTable has a csubJobType of 'query', then the system builds a report containing those subscriber sessions matching these criteria.  If the corresponding row in the csubJobTable has a csubJobType of 'clear', then the system terminates those subscriber sessions matching these criteria.  The system automatically creates an entry when the EMS/NMS sets the corresponding instance of csubJobType to 'query' or 'clear'. Likewise, the system automatically destroys an entry under the following circumstances\:  1)  The EMS/NMS destroys the corresponding row in the     csubJobTable.  2)  The EMS/NMS sets the corresponding instance of csubJobType     to 'noop'
        	**type**\: list of  		 :py:class:`CsubJobMatchParamsEntry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJobMatchParamsTable.CsubJobMatchParamsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CISCOSUBSCRIBERSESSIONMIB.CsubJobMatchParamsTable, self).__init__()

            self.yang_name = "csubJobMatchParamsTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("csubJobMatchParamsEntry", ("csubjobmatchparamsentry", CISCOSUBSCRIBERSESSIONMIB.CsubJobMatchParamsTable.CsubJobMatchParamsEntry))])
            self._leafs = OrderedDict()

            self.csubjobmatchparamsentry = YList(self)
            self._segment_path = lambda: "csubJobMatchParamsTable"
            self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubJobMatchParamsTable, [], name, value)


        class CsubJobMatchParamsEntry(Entity):
            """
            An entry describes a set of subscriber session match criteria.
            The set contains those subscriber session identities specified
            by csubJobMatchIdentities.
            
            If the corresponding row in the csubJobTable has a csubJobType
            of 'query', then the system builds a report containing those
            subscriber sessions matching these criteria.
            
            If the corresponding row in the csubJobTable has a csubJobType
            of 'clear', then the system terminates those subscriber
            sessions matching these criteria.
            
            The system automatically creates an entry when the EMS/NMS sets
            the corresponding instance of csubJobType to 'query' or 'clear'.
            Likewise, the system automatically destroys an entry under the
            following circumstances\:
            
            1)  The EMS/NMS destroys the corresponding row in the
                csubJobTable.
            
            2)  The EMS/NMS sets the corresponding instance of csubJobType
                to 'noop'.
            
            .. attribute:: csubjobid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`csubjobid <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJobTable.CsubJobEntry>`
            
            	**config**\: False
            
            .. attribute:: csubjobmatchidentities
            
            	This object specifies the subscriber identities that the system uses to determine the subscriber sessions the job executes on.  Each bit in this bit string corresponds to one or more columns in this table.  If the bit is '0', then the value of the corresponding columns are invalid.  If the bit is '1', then the value of corresponding columns are valid.  The following list specifies the mappings between the bits and the columns\:      'subscriberLabel' => csubJobMatchSubscriberLabel     'macAddress'      => csubJobMatchMacAddress     'nativeVrf'       => csubJobMatchNativeVrf     'nativeIpAddress' => csubJobMatchNativeIpAddrType,                          csubJobMatchNativeIpAddr,                          csubJobMatchNativeIpMask,     'domainVrf'       => csubJobMatchDomainVrf     'domainIpAddress' => csubJobMatchDomainIpAddrType,                          csubJobMatchDomainIpAddr,                          csubJobMatchDomainIpMask     'pbhk'            => csubJobMatchPbhk     'remoteId'        => csubJobMatchRemoteId     'circuitId'       => csubJobMatchCircuitId     'nasPort'         => csubJobMatchNasPort     'domain'          => csubJobMatchDomain     'username'        => csubJobMatchUsername     'acctSessionId'   => csubJobMatchAcctSessionId     'dnis'            => csubJobMatchDnis     'media'           => csubJobMatchMedia     'mlpNegotiated'   => csubJobMatchMlpNegotiated     'protocol'        => csubJobMatchProtocol     'serviceName'     => csubJobMatchServiceName     'dhcpClass'       => csubJobMatchDhcpClass     'tunnelName'      => csubJobMatchTunnelName  Observe that the bit 'ifIndex' has no meaning, as subscriber session jobs do not match against this subscriber session identity
            	**type**\:  :py:class:`SubSessionIdentities <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.SubSessionIdentities>`
            
            	**config**\: False
            
            .. attribute:: csubjobmatchotherparams
            
            	This object specifies other parameters relating to subscriber sessions a subscriber session job may match against.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is invalid.  If the bit is '1', then the value of the corresponding column represents the value of the parameter identity the system should match against for the corresponding subscriber session job.  The following list specifies the mappings between bits and the columns\:      'danglingDuration' => csubJobMatchDanglingDuration     'state'            => csubJobMatchState     'authenticated'    => csubJobMatchAuthenticated     'redundancyMode'   => csubJobMatchRedundancyMode
            	**type**\:  :py:class:`CsubJobMatchOtherParams <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJobMatchParamsTable.CsubJobMatchParamsEntry.CsubJobMatchOtherParams>`
            
            	**config**\: False
            
            .. attribute:: csubjobmatchsubscriberlabel
            
            	This object specifies the subscriber label that the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'subscriberLabel' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: csubjobmatchmacaddress
            
            	This object specifies the MAC address that the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'macAddress' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            	**config**\: False
            
            .. attribute:: csubjobmatchnativevrf
            
            	This object specifies the native VRF the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'nativeVrf' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubjobmatchnativeipaddrtype
            
            	This object specifies the type of Internet address specified by csubJobMatchNativeIpAddr and csubJobMatchNativeIpMask.  This value is valid only if the 'nativeIpAddress' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: csubjobmatchnativeipaddr
            
            	This object specifies the native IP address that the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'nativeIpAddress' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: csubjobmatchnativeipmask
            
            	This object specifies the mask used when matching the native IP address against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'nativeIpAddress' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: csubjobmatchdomainvrf
            
            	This object specifies the domain VRF the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'domainVrf' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubjobmatchdomainipaddrtype
            
            	This object specifies the type of Internet address specified by csubJobMatchDomainIpAddr and csubJobMatchDomainIpMask.  This value is valid only if the 'domainIpAddress' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            	**config**\: False
            
            .. attribute:: csubjobmatchdomainipaddr
            
            	This object specifies the domain IP address that the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'domainIpAddress' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: csubjobmatchdomainipmask
            
            	This object specifies the mask used when matching the domain IP address against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'domainIpAddress' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: str
            
            	**length:** 0..255
            
            	**config**\: False
            
            .. attribute:: csubjobmatchpbhk
            
            	This object specifies the PBHK that the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'pbhk' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubjobmatchremoteid
            
            	This object specifies the Remote\-Id the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'remoteId' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubjobmatchcircuitid
            
            	This object specifies the Circuit\-Id the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'circuitId' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubjobmatchnasport
            
            	This object specifies the NAS port\-identifier the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'nasPort' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubjobmatchdomain
            
            	This object specifies the domain the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'domain' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubjobmatchusername
            
            	This object specifies the username the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'username' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubjobmatchacctsessionid
            
            	This object specifies the accounting session identifier the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'accountingSid' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: csubjobmatchdnis
            
            	This object specifies the DNIS number the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'dnis' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubjobmatchmedia
            
            	This object specifies the media type the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'media' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  :py:class:`SubscriberMediaType <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.SubscriberMediaType>`
            
            	**config**\: False
            
            .. attribute:: csubjobmatchmlpnegotiated
            
            	This object specifies the MLP negotiated flag the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'mlpNegotiated' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: csubjobmatchprotocol
            
            	This object specifies the protocol type the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'protocol' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  :py:class:`SubscriberProtocolType <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.SubscriberProtocolType>`
            
            	**config**\: False
            
            .. attribute:: csubjobmatchservicename
            
            	This object specifies the service name the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'serviceName' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubjobmatchdhcpclass
            
            	This object specifies the DHCP class name the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'dhcpClass' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubjobmatchtunnelname
            
            	This object specifies the tunnel name the system matches against subscriber session in the process of executing a subscriber session job.  This value is valid only if the 'tunnelName' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: csubjobmatchdanglingduration
            
            	This object specifies the minimum interval of time a subscriber session can remain dangling in order for the system to consider it a match in the process of executing a subscriber session job. A 'dangling' subscriber session is one in the PENDING state.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This value is valid only if the 'danglingDuration' bit of the corresponding instance of csubJobMatchOtherParams is '1'
            	**type**\: int
            
            	**range:** 0..3600
            
            	**config**\: False
            
            .. attribute:: csubjobmatchstate
            
            	This object specifies the state of a subscriber session in order for the system to consider a match in the process of executing a subscriber session job.  The value 'other' is not valid and an implementation should not allow it to be written to this column.  This value is valid only if the 'state' bit of the corresponding instance of csubJobMatchOtherParams is '1'
            	**type**\:  :py:class:`SubSessionState <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB.SubSessionState>`
            
            	**config**\: False
            
            .. attribute:: csubjobmatchauthenticated
            
            	This object specifies whether a subscriber session should be unauthenticated for the system to consider a match in the process of executing a subscriber session job.  If this column is 'false', then the subscriber session job matches subscriber sessions that are unauthenticated.  If this column is 'true', then the subscriber session job matches subscriber session that are authenticated.  This value is valid only if the 'authenticated' bit of the corresponding instance of csubJobMatchParams is '1'
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: csubjobmatchredundancymode
            
            	This object specifies the redudancy mode of the subscriber session in order for the system to consider a match in the process of executing a subscriber session job.  The value 'other' is not valid and an implementation should not allow it to be written to this column.  This value is valid only if the 'redundancyMode' bit of the corresponding instance of csubJobMatchOtherParams is '1'
            	**type**\:  :py:class:`SubSessionRedundancyMode <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB.SubSessionRedundancyMode>`
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CISCOSUBSCRIBERSESSIONMIB.CsubJobMatchParamsTable.CsubJobMatchParamsEntry, self).__init__()

                self.yang_name = "csubJobMatchParamsEntry"
                self.yang_parent_name = "csubJobMatchParamsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csubjobid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csubjobid', (YLeaf(YType.str, 'csubJobId'), ['int'])),
                    ('csubjobmatchidentities', (YLeaf(YType.bits, 'csubJobMatchIdentities'), ['Bits'])),
                    ('csubjobmatchotherparams', (YLeaf(YType.bits, 'csubJobMatchOtherParams'), ['Bits'])),
                    ('csubjobmatchsubscriberlabel', (YLeaf(YType.uint32, 'csubJobMatchSubscriberLabel'), ['int'])),
                    ('csubjobmatchmacaddress', (YLeaf(YType.str, 'csubJobMatchMacAddress'), ['str'])),
                    ('csubjobmatchnativevrf', (YLeaf(YType.str, 'csubJobMatchNativeVrf'), ['str'])),
                    ('csubjobmatchnativeipaddrtype', (YLeaf(YType.enumeration, 'csubJobMatchNativeIpAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('csubjobmatchnativeipaddr', (YLeaf(YType.str, 'csubJobMatchNativeIpAddr'), ['str'])),
                    ('csubjobmatchnativeipmask', (YLeaf(YType.str, 'csubJobMatchNativeIpMask'), ['str'])),
                    ('csubjobmatchdomainvrf', (YLeaf(YType.str, 'csubJobMatchDomainVrf'), ['str'])),
                    ('csubjobmatchdomainipaddrtype', (YLeaf(YType.enumeration, 'csubJobMatchDomainIpAddrType'), [('ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetAddressType', '')])),
                    ('csubjobmatchdomainipaddr', (YLeaf(YType.str, 'csubJobMatchDomainIpAddr'), ['str'])),
                    ('csubjobmatchdomainipmask', (YLeaf(YType.str, 'csubJobMatchDomainIpMask'), ['str'])),
                    ('csubjobmatchpbhk', (YLeaf(YType.str, 'csubJobMatchPbhk'), ['str'])),
                    ('csubjobmatchremoteid', (YLeaf(YType.str, 'csubJobMatchRemoteId'), ['str'])),
                    ('csubjobmatchcircuitid', (YLeaf(YType.str, 'csubJobMatchCircuitId'), ['str'])),
                    ('csubjobmatchnasport', (YLeaf(YType.str, 'csubJobMatchNasPort'), ['str'])),
                    ('csubjobmatchdomain', (YLeaf(YType.str, 'csubJobMatchDomain'), ['str'])),
                    ('csubjobmatchusername', (YLeaf(YType.str, 'csubJobMatchUsername'), ['str'])),
                    ('csubjobmatchacctsessionid', (YLeaf(YType.uint32, 'csubJobMatchAcctSessionId'), ['int'])),
                    ('csubjobmatchdnis', (YLeaf(YType.str, 'csubJobMatchDnis'), ['str'])),
                    ('csubjobmatchmedia', (YLeaf(YType.enumeration, 'csubJobMatchMedia'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB', 'SubscriberMediaType', '')])),
                    ('csubjobmatchmlpnegotiated', (YLeaf(YType.boolean, 'csubJobMatchMlpNegotiated'), ['bool'])),
                    ('csubjobmatchprotocol', (YLeaf(YType.enumeration, 'csubJobMatchProtocol'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB', 'SubscriberProtocolType', '')])),
                    ('csubjobmatchservicename', (YLeaf(YType.str, 'csubJobMatchServiceName'), ['str'])),
                    ('csubjobmatchdhcpclass', (YLeaf(YType.str, 'csubJobMatchDhcpClass'), ['str'])),
                    ('csubjobmatchtunnelname', (YLeaf(YType.str, 'csubJobMatchTunnelName'), ['str'])),
                    ('csubjobmatchdanglingduration', (YLeaf(YType.uint32, 'csubJobMatchDanglingDuration'), ['int'])),
                    ('csubjobmatchstate', (YLeaf(YType.enumeration, 'csubJobMatchState'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB', 'SubSessionState', '')])),
                    ('csubjobmatchauthenticated', (YLeaf(YType.boolean, 'csubJobMatchAuthenticated'), ['bool'])),
                    ('csubjobmatchredundancymode', (YLeaf(YType.enumeration, 'csubJobMatchRedundancyMode'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB', 'SubSessionRedundancyMode', '')])),
                ])
                self.csubjobid = None
                self.csubjobmatchidentities = Bits()
                self.csubjobmatchotherparams = Bits()
                self.csubjobmatchsubscriberlabel = None
                self.csubjobmatchmacaddress = None
                self.csubjobmatchnativevrf = None
                self.csubjobmatchnativeipaddrtype = None
                self.csubjobmatchnativeipaddr = None
                self.csubjobmatchnativeipmask = None
                self.csubjobmatchdomainvrf = None
                self.csubjobmatchdomainipaddrtype = None
                self.csubjobmatchdomainipaddr = None
                self.csubjobmatchdomainipmask = None
                self.csubjobmatchpbhk = None
                self.csubjobmatchremoteid = None
                self.csubjobmatchcircuitid = None
                self.csubjobmatchnasport = None
                self.csubjobmatchdomain = None
                self.csubjobmatchusername = None
                self.csubjobmatchacctsessionid = None
                self.csubjobmatchdnis = None
                self.csubjobmatchmedia = None
                self.csubjobmatchmlpnegotiated = None
                self.csubjobmatchprotocol = None
                self.csubjobmatchservicename = None
                self.csubjobmatchdhcpclass = None
                self.csubjobmatchtunnelname = None
                self.csubjobmatchdanglingduration = None
                self.csubjobmatchstate = None
                self.csubjobmatchauthenticated = None
                self.csubjobmatchredundancymode = None
                self._segment_path = lambda: "csubJobMatchParamsEntry" + "[csubJobId='" + str(self.csubjobid) + "']"
                self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubJobMatchParamsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubJobMatchParamsTable.CsubJobMatchParamsEntry, ['csubjobid', 'csubjobmatchidentities', 'csubjobmatchotherparams', 'csubjobmatchsubscriberlabel', 'csubjobmatchmacaddress', 'csubjobmatchnativevrf', 'csubjobmatchnativeipaddrtype', 'csubjobmatchnativeipaddr', 'csubjobmatchnativeipmask', 'csubjobmatchdomainvrf', 'csubjobmatchdomainipaddrtype', 'csubjobmatchdomainipaddr', 'csubjobmatchdomainipmask', 'csubjobmatchpbhk', 'csubjobmatchremoteid', 'csubjobmatchcircuitid', 'csubjobmatchnasport', 'csubjobmatchdomain', 'csubjobmatchusername', 'csubjobmatchacctsessionid', 'csubjobmatchdnis', 'csubjobmatchmedia', 'csubjobmatchmlpnegotiated', 'csubjobmatchprotocol', 'csubjobmatchservicename', 'csubjobmatchdhcpclass', 'csubjobmatchtunnelname', 'csubjobmatchdanglingduration', 'csubjobmatchstate', 'csubjobmatchauthenticated', 'csubjobmatchredundancymode'], name, value)




    class CsubJobQueryParamsTable(Entity):
        """
        This table contains subscriber session job parameters
        describing query parameters.
        
        This table has a sparse\-dependent relationship on the
        csubJobTable, containing a row for each job having a
        csubJobType of 'query'.
        
        .. attribute:: csubjobqueryparamsentry
        
        	An entry describes a set of subscriber session query parameters.  The system automatically creates an entry when the EMS/NMS sets the corresponding instance of csubJobType to 'query'.  Likewise, the system automatically destroys an entry under the following circumstances\:  1)  The EMS/NMS destroys the corresponding row in the csubJobTable.  2)  The EMS/NMS sets the corresponding instance of csubJobType to     'noop' or 'clear'
        	**type**\: list of  		 :py:class:`CsubJobQueryParamsEntry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJobQueryParamsTable.CsubJobQueryParamsEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CISCOSUBSCRIBERSESSIONMIB.CsubJobQueryParamsTable, self).__init__()

            self.yang_name = "csubJobQueryParamsTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("csubJobQueryParamsEntry", ("csubjobqueryparamsentry", CISCOSUBSCRIBERSESSIONMIB.CsubJobQueryParamsTable.CsubJobQueryParamsEntry))])
            self._leafs = OrderedDict()

            self.csubjobqueryparamsentry = YList(self)
            self._segment_path = lambda: "csubJobQueryParamsTable"
            self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubJobQueryParamsTable, [], name, value)


        class CsubJobQueryParamsEntry(Entity):
            """
            An entry describes a set of subscriber session query
            parameters.
            
            The system automatically creates an entry when the EMS/NMS sets
            the corresponding instance of csubJobType to 'query'.  Likewise,
            the system automatically destroys an entry under the following
            circumstances\:
            
            1)  The EMS/NMS destroys the corresponding row in the csubJobTable.
            
            2)  The EMS/NMS sets the corresponding instance of csubJobType to
                'noop' or 'clear'.
            
            .. attribute:: csubjobid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`csubjobid <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJobTable.CsubJobEntry>`
            
            	**config**\: False
            
            .. attribute:: csubjobquerysortkey1
            
            	This object specifies the first subscriber identity that the system uses when sorting subscriber sessions into the final report corresponding to a subscriber session query.  It is not valid to set this column to 'other' or 'ifIndex'
            	**type**\:  :py:class:`SubSessionIdentity <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.SubSessionIdentity>`
            
            	**config**\: False
            
            .. attribute:: csubjobquerysortkey2
            
            	This object specifies the second subscriber identity that the system uses when sorting subscriber sessions into the final report corresponding to a subscriber session query.  If it is the desire to have the final report sorted on a single subscriber identity, then this column should be 'other'
            	**type**\:  :py:class:`SubSessionIdentity <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.SubSessionIdentity>`
            
            	**config**\: False
            
            .. attribute:: csubjobquerysortkey3
            
            	This object specifies the third subscriber identity that the system uses when sorting subscriber sessions into the final report corresponding to a subscriber session query.  If it is the desire to have the final report sorted on one or two subscriber identities, then this column should be 'other'
            	**type**\:  :py:class:`SubSessionIdentity <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.SubSessionIdentity>`
            
            	**config**\: False
            
            .. attribute:: csubjobqueryresultingreportsize
            
            	This object indicates the number of subscriber sessions that matched the corresponding subscriber session query.  The value of this column should be '0' unless the corresponding value of csubJobState is 'finished'.  The value of this column should be '0' after the EMS/NMS sets the corresponding csubJobControl to 'release'
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CISCOSUBSCRIBERSESSIONMIB.CsubJobQueryParamsTable.CsubJobQueryParamsEntry, self).__init__()

                self.yang_name = "csubJobQueryParamsEntry"
                self.yang_parent_name = "csubJobQueryParamsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csubjobid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csubjobid', (YLeaf(YType.str, 'csubJobId'), ['int'])),
                    ('csubjobquerysortkey1', (YLeaf(YType.enumeration, 'csubJobQuerySortKey1'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB', 'SubSessionIdentity', '')])),
                    ('csubjobquerysortkey2', (YLeaf(YType.enumeration, 'csubJobQuerySortKey2'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB', 'SubSessionIdentity', '')])),
                    ('csubjobquerysortkey3', (YLeaf(YType.enumeration, 'csubJobQuerySortKey3'), [('ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB', 'SubSessionIdentity', '')])),
                    ('csubjobqueryresultingreportsize', (YLeaf(YType.uint32, 'csubJobQueryResultingReportSize'), ['int'])),
                ])
                self.csubjobid = None
                self.csubjobquerysortkey1 = None
                self.csubjobquerysortkey2 = None
                self.csubjobquerysortkey3 = None
                self.csubjobqueryresultingreportsize = None
                self._segment_path = lambda: "csubJobQueryParamsEntry" + "[csubJobId='" + str(self.csubjobid) + "']"
                self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubJobQueryParamsTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubJobQueryParamsTable.CsubJobQueryParamsEntry, ['csubjobid', 'csubjobquerysortkey1', 'csubjobquerysortkey2', 'csubjobquerysortkey3', 'csubjobqueryresultingreportsize'], name, value)




    class CsubJobQueueTable(Entity):
        """
        This table lists the subscriber session jobs currently pending
        in the subscriber session job queue.
        
        .. attribute:: csubjobqueueentry
        
        	An entry describing an subscriber session job in the subscriber session job queue.  The system creates an entry in this table when it places a subscriber session job on the subscriber session job queue.  It does this when the EMS/NMS sets an instance of csubJobControl to 'start' and the system is already executing a subscriber session job.  Likewise, the system destroys an entry when it removes it from the queue.  This occurs under the following circumstances\:  1)  The system has finished executing a job, for whatever     reason, and is ready to start executing the job at the head     of the queue.  2)  The EMS/NMS has set an instance of csubJobControl to 'abort'     for a job that was on the queue
        	**type**\: list of  		 :py:class:`CsubJobQueueEntry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJobQueueTable.CsubJobQueueEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CISCOSUBSCRIBERSESSIONMIB.CsubJobQueueTable, self).__init__()

            self.yang_name = "csubJobQueueTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("csubJobQueueEntry", ("csubjobqueueentry", CISCOSUBSCRIBERSESSIONMIB.CsubJobQueueTable.CsubJobQueueEntry))])
            self._leafs = OrderedDict()

            self.csubjobqueueentry = YList(self)
            self._segment_path = lambda: "csubJobQueueTable"
            self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubJobQueueTable, [], name, value)


        class CsubJobQueueEntry(Entity):
            """
            An entry describing an subscriber session job in the
            subscriber session job queue.
            
            The system creates an entry in this table when it places a
            subscriber session job on the subscriber session job queue.  It
            does this when the EMS/NMS sets an instance of csubJobControl to
            'start' and the system is already executing a subscriber session
            job.  Likewise, the system destroys an entry when it removes it
            from the queue.  This occurs under the following circumstances\:
            
            1)  The system has finished executing a job, for whatever
                reason, and is ready to start executing the job at the head
                of the queue.
            
            2)  The EMS/NMS has set an instance of csubJobControl to 'abort'
                for a job that was on the queue.
            
            .. attribute:: csubjobqueuenumber  (key)
            
            	This object indicates an positive, integer\-value that uniquely identifies the entry in the table. The value of this object starts at '1' and monotonically increases for each subscriber session job inserted into the subscriber session job queue.  If the value of this object is '4294967295', the system will reset it to '1' when it inserts the next subscriber session job into the subscriber session job queue
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: csubjobqueuejobid
            
            	This object indicates the identifier associated with the subscriber session job
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CISCOSUBSCRIBERSESSIONMIB.CsubJobQueueTable.CsubJobQueueEntry, self).__init__()

                self.yang_name = "csubJobQueueEntry"
                self.yang_parent_name = "csubJobQueueTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csubjobqueuenumber']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csubjobqueuenumber', (YLeaf(YType.uint32, 'csubJobQueueNumber'), ['int'])),
                    ('csubjobqueuejobid', (YLeaf(YType.uint32, 'csubJobQueueJobId'), ['int'])),
                ])
                self.csubjobqueuenumber = None
                self.csubjobqueuejobid = None
                self._segment_path = lambda: "csubJobQueueEntry" + "[csubJobQueueNumber='" + str(self.csubjobqueuenumber) + "']"
                self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubJobQueueTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubJobQueueTable.CsubJobQueueEntry, ['csubjobqueuenumber', 'csubjobqueuejobid'], name, value)




    class CsubJobReportTable(Entity):
        """
        This table contains the reports corresponding to subscriber
        session jobs that have a csubJobType of 'query' and
        csubJobState of 'finished'.
        
        This table has an expansion dependent relationship on the
        csubJobTable, containing zero or more rows for each job.
        
        .. attribute:: csubjobreportentry
        
        	An entry describes a subscriber session that satisfied the match criteria specified by the corresponding job.  The system creates an entry for each subscriber session that satisfied the specified match criteria of a subscriber session job having a csubJobType of 'query'.  However, it does not create these entries until after the system has successfully executed the subscriber session job.  The system destroys an entry under the following circumstances\:  1)  The corresponding subscriber session job has been destroyed     by the EMS/NMS.  2)  The value of csubJobMaxLife is non\-zero and the age of the     report has reached the specified maximum life.  3)  The EMS/NMS has set the corresponding instance of     csubJobControl to 'release'.  4)  The EMS/NMS has restarted the corresponding subscriber     session job (i.e., has set the corresponding instance of     csubJobControl to 'start')
        	**type**\: list of  		 :py:class:`CsubJobReportEntry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJobReportTable.CsubJobReportEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CISCOSUBSCRIBERSESSIONMIB.CsubJobReportTable, self).__init__()

            self.yang_name = "csubJobReportTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("csubJobReportEntry", ("csubjobreportentry", CISCOSUBSCRIBERSESSIONMIB.CsubJobReportTable.CsubJobReportEntry))])
            self._leafs = OrderedDict()

            self.csubjobreportentry = YList(self)
            self._segment_path = lambda: "csubJobReportTable"
            self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubJobReportTable, [], name, value)


        class CsubJobReportEntry(Entity):
            """
            An entry describes a subscriber session that satisfied the
            match criteria specified by the corresponding job.
            
            The system creates an entry for each subscriber session that
            satisfied the specified match criteria of a subscriber session
            job having a csubJobType of 'query'.  However, it does not
            create these entries until after the system has successfully
            executed the subscriber session job.
            
            The system destroys an entry under the following circumstances\:
            
            1)  The corresponding subscriber session job has been destroyed
                by the EMS/NMS.
            
            2)  The value of csubJobMaxLife is non\-zero and the age of the
                report has reached the specified maximum life.
            
            3)  The EMS/NMS has set the corresponding instance of
                csubJobControl to 'release'.
            
            4)  The EMS/NMS has restarted the corresponding subscriber
                session job (i.e., has set the corresponding instance of
                csubJobControl to 'start').
            
            .. attribute:: csubjobid  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`csubjobid <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CISCOSUBSCRIBERSESSIONMIB.CsubJobTable.CsubJobEntry>`
            
            	**config**\: False
            
            .. attribute:: csubjobreportid  (key)
            
            	This object indicates an arbitrary, positive, integer\-value that uniquely identifies this entry in a report.  This auxiliary value is necessary, as the corresponding subscriber session job can specify up to three subscriber identities on which to sort the subscriber sessions that end up in the final report
            	**type**\: int
            
            	**range:** 1..4294967295
            
            	**config**\: False
            
            .. attribute:: csubjobreportsession
            
            	This object indicates the ifIndex\-value assigned to the subscriber session that satisfied the match criteria specified by the corresponding subscriber session job having a csubJobType of 'query'
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CISCOSUBSCRIBERSESSIONMIB.CsubJobReportTable.CsubJobReportEntry, self).__init__()

                self.yang_name = "csubJobReportEntry"
                self.yang_parent_name = "csubJobReportTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['csubjobid','csubjobreportid']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('csubjobid', (YLeaf(YType.str, 'csubJobId'), ['int'])),
                    ('csubjobreportid', (YLeaf(YType.uint32, 'csubJobReportId'), ['int'])),
                    ('csubjobreportsession', (YLeaf(YType.int32, 'csubJobReportSession'), ['int'])),
                ])
                self.csubjobid = None
                self.csubjobreportid = None
                self.csubjobreportsession = None
                self._segment_path = lambda: "csubJobReportEntry" + "[csubJobId='" + str(self.csubjobid) + "']" + "[csubJobReportId='" + str(self.csubjobreportid) + "']"
                self._absolute_path = lambda: "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubJobReportTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOSUBSCRIBERSESSIONMIB.CsubJobReportTable.CsubJobReportEntry, ['csubjobid', 'csubjobreportid', 'csubjobreportsession'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOSUBSCRIBERSESSIONMIB()
        return self._top_entity



