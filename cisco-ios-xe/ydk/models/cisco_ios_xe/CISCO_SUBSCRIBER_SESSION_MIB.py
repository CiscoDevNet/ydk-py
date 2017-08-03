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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoSubscriberSessionMib(Entity):
    """
    
    
    .. attribute:: csubaggstatsinttable
    
    	This table contains aggregated subscriber session performance data collected for as much as a day's worth of 15\-minute measurement intervals.  This table has an expansion dependent relationship on the csubAggStatsTable, containing zero or more rows for each row contained by the csubAggStatsTable.  Observe that the collection and maintenance of aggregated subscriber performance data is OPTIONAL for all scopes of aggregation.  However, an implementation should maintain at least one interval for the 'scope of aggregation' that contains all subscriber sessions maintained by the system
    	**type**\:   :py:class:`Csubaggstatsinttable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubaggstatsinttable>`
    
    .. attribute:: csubaggstatstable
    
    	This table contains sets of aggregated statistics relating to subscriber sessions, where each set has a unique scope of aggregation
    	**type**\:   :py:class:`Csubaggstatstable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubaggstatstable>`
    
    .. attribute:: csubaggstatsthreshtable
    
    	Please enter the Table Description here
    	**type**\:   :py:class:`Csubaggstatsthreshtable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubaggstatsthreshtable>`
    
    .. attribute:: csubaggthresh
    
    	
    	**type**\:   :py:class:`Csubaggthresh <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubaggthresh>`
    
    .. attribute:: csubjob
    
    	
    	**type**\:   :py:class:`Csubjob <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjob>`
    
    .. attribute:: csubjobmatchparamstable
    
    	This table contains subscriber session job parameters describing match criteria.  This table has a sparse\-dependent relationship on the csubJobTable, containing a row for each job having a csubJobType of 'query' or 'clear'
    	**type**\:   :py:class:`Csubjobmatchparamstable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjobmatchparamstable>`
    
    .. attribute:: csubjobqueryparamstable
    
    	This table contains subscriber session job parameters describing query parameters.  This table has a sparse\-dependent relationship on the csubJobTable, containing a row for each job having a csubJobType of 'query'
    	**type**\:   :py:class:`Csubjobqueryparamstable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjobqueryparamstable>`
    
    .. attribute:: csubjobqueuetable
    
    	This table lists the subscriber session jobs currently pending in the subscriber session job queue
    	**type**\:   :py:class:`Csubjobqueuetable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjobqueuetable>`
    
    .. attribute:: csubjobreporttable
    
    	This table contains the reports corresponding to subscriber session jobs that have a csubJobType of 'query' and csubJobState of 'finished'.  This table has an expansion dependent relationship on the csubJobTable, containing zero or more rows for each job
    	**type**\:   :py:class:`Csubjobreporttable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjobreporttable>`
    
    .. attribute:: csubjobtable
    
    	This table contains the subscriber session jobs submitted by the EMS/NMS
    	**type**\:   :py:class:`Csubjobtable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjobtable>`
    
    .. attribute:: csubsessionbytypetable
    
    	This table describes a list of subscriber sessions currently maintained by the system.  The tables sorts the subscriber sessions first by the subscriber session's type and second by the ifIndex assigned to the subscriber session
    	**type**\:   :py:class:`Csubsessionbytypetable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubsessionbytypetable>`
    
    .. attribute:: csubsessiontable
    
    	This table describes a list of subscriber sessions currently maintained by the system.  This table has a sparse dependent relationship on the ifTable, containing a row for each interface having an interface type describing a subscriber session
    	**type**\:   :py:class:`Csubsessiontable <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubsessiontable>`
    
    

    """

    _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
    _revision = '2012-08-08'

    def __init__(self):
        super(CiscoSubscriberSessionMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-SUBSCRIBER-SESSION-MIB"
        self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"

        self.csubaggstatsinttable = CiscoSubscriberSessionMib.Csubaggstatsinttable()
        self.csubaggstatsinttable.parent = self
        self._children_name_map["csubaggstatsinttable"] = "csubAggStatsIntTable"
        self._children_yang_names.add("csubAggStatsIntTable")

        self.csubaggstatstable = CiscoSubscriberSessionMib.Csubaggstatstable()
        self.csubaggstatstable.parent = self
        self._children_name_map["csubaggstatstable"] = "csubAggStatsTable"
        self._children_yang_names.add("csubAggStatsTable")

        self.csubaggstatsthreshtable = CiscoSubscriberSessionMib.Csubaggstatsthreshtable()
        self.csubaggstatsthreshtable.parent = self
        self._children_name_map["csubaggstatsthreshtable"] = "csubAggStatsThreshTable"
        self._children_yang_names.add("csubAggStatsThreshTable")

        self.csubaggthresh = CiscoSubscriberSessionMib.Csubaggthresh()
        self.csubaggthresh.parent = self
        self._children_name_map["csubaggthresh"] = "csubAggThresh"
        self._children_yang_names.add("csubAggThresh")

        self.csubjob = CiscoSubscriberSessionMib.Csubjob()
        self.csubjob.parent = self
        self._children_name_map["csubjob"] = "csubJob"
        self._children_yang_names.add("csubJob")

        self.csubjobmatchparamstable = CiscoSubscriberSessionMib.Csubjobmatchparamstable()
        self.csubjobmatchparamstable.parent = self
        self._children_name_map["csubjobmatchparamstable"] = "csubJobMatchParamsTable"
        self._children_yang_names.add("csubJobMatchParamsTable")

        self.csubjobqueryparamstable = CiscoSubscriberSessionMib.Csubjobqueryparamstable()
        self.csubjobqueryparamstable.parent = self
        self._children_name_map["csubjobqueryparamstable"] = "csubJobQueryParamsTable"
        self._children_yang_names.add("csubJobQueryParamsTable")

        self.csubjobqueuetable = CiscoSubscriberSessionMib.Csubjobqueuetable()
        self.csubjobqueuetable.parent = self
        self._children_name_map["csubjobqueuetable"] = "csubJobQueueTable"
        self._children_yang_names.add("csubJobQueueTable")

        self.csubjobreporttable = CiscoSubscriberSessionMib.Csubjobreporttable()
        self.csubjobreporttable.parent = self
        self._children_name_map["csubjobreporttable"] = "csubJobReportTable"
        self._children_yang_names.add("csubJobReportTable")

        self.csubjobtable = CiscoSubscriberSessionMib.Csubjobtable()
        self.csubjobtable.parent = self
        self._children_name_map["csubjobtable"] = "csubJobTable"
        self._children_yang_names.add("csubJobTable")

        self.csubsessionbytypetable = CiscoSubscriberSessionMib.Csubsessionbytypetable()
        self.csubsessionbytypetable.parent = self
        self._children_name_map["csubsessionbytypetable"] = "csubSessionByTypeTable"
        self._children_yang_names.add("csubSessionByTypeTable")

        self.csubsessiontable = CiscoSubscriberSessionMib.Csubsessiontable()
        self.csubsessiontable.parent = self
        self._children_name_map["csubsessiontable"] = "csubSessionTable"
        self._children_yang_names.add("csubSessionTable")


    class Csubjob(Entity):
        """
        
        
        .. attribute:: csubjobcount
        
        	This object indicates the number of subscriber session jobs currently maintained by the csubJobTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: jobs
        
        .. attribute:: csubjobfinishednotifyenable
        
        	This object specifies whether the system generates a csubJobFinishedNotify notification when the system finishes processing a subscriber session job
        	**type**\:  bool
        
        .. attribute:: csubjobidnext
        
        	This object indicates the next available identifier for the creation of a new row in the csubJobTable.  If no available identifier exists, then this object has the value '0'
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: csubjobindexedattributes
        
        	This object indicates which subscriber session identities the system maintains as searchable keys.  This value serves the EMS/NMS in configuring a subscriber session query, as at least one match criteria must be an 'indexed attribute'
        	**type**\:   :py:class:`Subsessionidentities <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.Subsessionidentities>`
        
        .. attribute:: csubjobmaxlife
        
        	This object specifies the maximum life a subscriber session report corresponding to a subscriber session job having a csubJobType of 'query'.  The system tracks the time elapsed after it finishes processing a query.  When the time elapsed reaches the value specified by this column, the system automatically  destroys the report.  A value of '0' disables the automatic destruction of reports
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**units**\: seconds
        
        .. attribute:: csubjobmaxnumber
        
        	This object indicates the maximum number of outstanding subscriber session jobs the system can support.  If the csubJobTable contains a number of rows (i.e., the value of csubJobCount) equal to this value, then any attempt to create a new row will result in a response with an error\-status of 'resourceUnavailable'
        	**type**\:  int
        
        	**range:** 1..4294967295
        
        	**units**\: jobs
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CiscoSubscriberSessionMib.Csubjob, self).__init__()

            self.yang_name = "csubJob"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"

            self.csubjobcount = YLeaf(YType.uint32, "csubJobCount")

            self.csubjobfinishednotifyenable = YLeaf(YType.boolean, "csubJobFinishedNotifyEnable")

            self.csubjobidnext = YLeaf(YType.uint32, "csubJobIdNext")

            self.csubjobindexedattributes = YLeaf(YType.bits, "csubJobIndexedAttributes")

            self.csubjobmaxlife = YLeaf(YType.uint32, "csubJobMaxLife")

            self.csubjobmaxnumber = YLeaf(YType.uint32, "csubJobMaxNumber")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csubjobcount",
                            "csubjobfinishednotifyenable",
                            "csubjobidnext",
                            "csubjobindexedattributes",
                            "csubjobmaxlife",
                            "csubjobmaxnumber") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSubscriberSessionMib.Csubjob, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSubscriberSessionMib.Csubjob, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.csubjobcount.is_set or
                self.csubjobfinishednotifyenable.is_set or
                self.csubjobidnext.is_set or
                self.csubjobindexedattributes.is_set or
                self.csubjobmaxlife.is_set or
                self.csubjobmaxnumber.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csubjobcount.yfilter != YFilter.not_set or
                self.csubjobfinishednotifyenable.yfilter != YFilter.not_set or
                self.csubjobidnext.yfilter != YFilter.not_set or
                self.csubjobindexedattributes.yfilter != YFilter.not_set or
                self.csubjobmaxlife.yfilter != YFilter.not_set or
                self.csubjobmaxnumber.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csubJob" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csubjobcount.is_set or self.csubjobcount.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csubjobcount.get_name_leafdata())
            if (self.csubjobfinishednotifyenable.is_set or self.csubjobfinishednotifyenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csubjobfinishednotifyenable.get_name_leafdata())
            if (self.csubjobidnext.is_set or self.csubjobidnext.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csubjobidnext.get_name_leafdata())
            if (self.csubjobindexedattributes.is_set or self.csubjobindexedattributes.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csubjobindexedattributes.get_name_leafdata())
            if (self.csubjobmaxlife.is_set or self.csubjobmaxlife.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csubjobmaxlife.get_name_leafdata())
            if (self.csubjobmaxnumber.is_set or self.csubjobmaxnumber.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csubjobmaxnumber.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csubJobCount" or name == "csubJobFinishedNotifyEnable" or name == "csubJobIdNext" or name == "csubJobIndexedAttributes" or name == "csubJobMaxLife" or name == "csubJobMaxNumber"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "csubJobCount"):
                self.csubjobcount = value
                self.csubjobcount.value_namespace = name_space
                self.csubjobcount.value_namespace_prefix = name_space_prefix
            if(value_path == "csubJobFinishedNotifyEnable"):
                self.csubjobfinishednotifyenable = value
                self.csubjobfinishednotifyenable.value_namespace = name_space
                self.csubjobfinishednotifyenable.value_namespace_prefix = name_space_prefix
            if(value_path == "csubJobIdNext"):
                self.csubjobidnext = value
                self.csubjobidnext.value_namespace = name_space
                self.csubjobidnext.value_namespace_prefix = name_space_prefix
            if(value_path == "csubJobIndexedAttributes"):
                self.csubjobindexedattributes[value] = True
            if(value_path == "csubJobMaxLife"):
                self.csubjobmaxlife = value
                self.csubjobmaxlife.value_namespace = name_space
                self.csubjobmaxlife.value_namespace_prefix = name_space_prefix
            if(value_path == "csubJobMaxNumber"):
                self.csubjobmaxnumber = value
                self.csubjobmaxnumber.value_namespace = name_space
                self.csubjobmaxnumber.value_namespace_prefix = name_space_prefix


    class Csubaggthresh(Entity):
        """
        
        
        .. attribute:: csubaggstatsthreshnotifenable
        
        	This object enables or disables the generation of any of the csubAggStats\* threshold notifications
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CiscoSubscriberSessionMib.Csubaggthresh, self).__init__()

            self.yang_name = "csubAggThresh"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"

            self.csubaggstatsthreshnotifenable = YLeaf(YType.boolean, "csubAggStatsThreshNotifEnable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("csubaggstatsthreshnotifenable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoSubscriberSessionMib.Csubaggthresh, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSubscriberSessionMib.Csubaggthresh, self).__setattr__(name, value)

        def has_data(self):
            return self.csubaggstatsthreshnotifenable.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.csubaggstatsthreshnotifenable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csubAggThresh" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.csubaggstatsthreshnotifenable.is_set or self.csubaggstatsthreshnotifenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.csubaggstatsthreshnotifenable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csubAggStatsThreshNotifEnable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "csubAggStatsThreshNotifEnable"):
                self.csubaggstatsthreshnotifenable = value
                self.csubaggstatsthreshnotifenable.value_namespace = name_space
                self.csubaggstatsthreshnotifenable.value_namespace_prefix = name_space_prefix


    class Csubsessiontable(Entity):
        """
        This table describes a list of subscriber sessions currently
        maintained by the system.
        
        This table has a sparse dependent relationship on the ifTable,
        containing a row for each interface having an interface type
        describing a subscriber session.
        
        .. attribute:: csubsessionentry
        
        	This entry contains data describing a subscriber sessions, including its state, configuration, and collected identities.  An entry exists for a corresponding entry in the ifTable describing a subscriber session.  Currently, subscriber sessions must have one of the following ifType values\:      'ppp'     'ipSubscriberSession'     'l2SubscriberSession'  The system creates an entry when it establishes a subscriber session.  Likewise, the system destroys an entry when it terminates the corresponding subscriber session
        	**type**\: list of    :py:class:`Csubsessionentry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubsessiontable.Csubsessionentry>`
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CiscoSubscriberSessionMib.Csubsessiontable, self).__init__()

            self.yang_name = "csubSessionTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"

            self.csubsessionentry = YList(self)

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
                        super(CiscoSubscriberSessionMib.Csubsessiontable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSubscriberSessionMib.Csubsessiontable, self).__setattr__(name, value)


        class Csubsessionentry(Entity):
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
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: csubsessionacctsessionid
            
            	This object indicates the accounting session identifier assigned to the subscriber session.  This column is valid only if the 'accountingSid' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csubsessionauthenticated
            
            	This object indicates whether the system has successfully authenticated the subscriber session.      'false'         The subscriber session is operationally up, but in the         UNAUTHENTICATED state.      'true'         The subscriber session is operationally up, but in the         AUTHENTICATED state
            	**type**\:  bool
            
            .. attribute:: csubsessionavailableidentities
            
            	This object indicates the subscriber identities that the system has successfully collected for the subscriber session.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is invalid.  If the bit is '1', then the value of the corresponding column represents the value of the subscriber identity collected by the system.  The following list specifies the mappings between the bits and the columns\:      'subscriberLabel' => csubSessionSubscriberLabel     'macAddress'      => csubSessionMacAddress     'nativeVrf'       => csubSessionNativeVrf     'nativeIpAddress' => csubSessionNativeIpAddrType,                          csubSessionNativeIpAddr,                          csubSessionNativeIpMask     'nativeIpAddress2'=> csubSessionNativeIpAddrType2,                          csubSessionNativeIpAddr2,                          csubSessionNativeIpMask2                                      'domainVrf'       => csubSessionDomainVrf     'domainIpAddress' => csubSessionDomainIpAddrType,                          csubSessionDomainIpAddr,                          csubSessionDomainIpMask     'pbhk'            => csubSessionPbhk     'remoteId'        => csubSessionRemoteId     'circuitId'       => csubSessionCircuitId     'nasPort'         => csubSessionNasPort     'domain'          => csubSessionDomain     'username'        => csubSessionUsername     'acctSessionId'   => csubSessionAcctSessionId     'dnis'            => csubSessionDnis     'media'           => csubSessionMedia     'mlpNegotiated'   => csubSessionMlpNegotiated     'protocol'        => csubSessionProtocol     'dhcpClass'       => csubSessionDhcpClass     'tunnelName'      => csubSessionTunnelName  Observe that the bit 'ifIndex' should always be '1'.  This identity maps to the ifIndex assigned to the subscriber session.  Observe that the bit 'serviceName' maps to one or more instance of ccbptPolicyMap (defined by the CISCO\-CBP\-TARGET\-MIB)
            	**type**\:   :py:class:`Subsessionidentities <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.Subsessionidentities>`
            
            .. attribute:: csubsessioncircuitid
            
            	This object indicates the Circuit\-Id identifying the circuit supported by the 'calling station' or AN providing access to the subscriber.  This column is valid only if the 'circuitId' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubsessioncreationtime
            
            	This object indicates when the subscriber session was created (i.e., when the subscriber session was initiated)
            	**type**\:  str
            
            .. attribute:: csubsessionderivedcfg
            
            	This object indicates the row in the cdtTemplateTable (defined by the CISCO\-DYNAMIC\-TEMPLATE\-MIB) describing the derived configuration for the subscriber session.  Observe that the value of cdtTemplateType corresponding to the referenced row must be 'derived'
            	**type**\:  str
            
            	**length:** 1..64
            
            .. attribute:: csubsessiondhcpclass
            
            	This object indicates the name of the class matching the DHCP DISCOVER message received from the subscriber.  This column is valid only if the 'dhcpClass' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubsessiondnis
            
            	This object indicates the DNIS number dialed by the subscriber to access the 'calling station' or AN.  This column is valid only if the 'dnis' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubsessiondomain
            
            	This object indicates the domain associated with the subscriber.  This column is valid only if the 'domain' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubsessiondomainipaddr
            
            	This object indicates the IP address assigned to the subscriber on the service\-facing side of the system.  This column is valid only if the 'domainIpAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: csubsessiondomainipaddrtype
            
            	This object indicates the type of IP address assigned to the subscriber on the service\-facing side of the system.  This column is valid only if the 'domainIpAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: csubsessiondomainipmask
            
            	This object indicates the corresponding mask for the IP address assigned to the subscriber on the service\-facing side of the system.  This column is valid only if the 'domainIpAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: csubsessiondomainvrf
            
            	This object indicates the VRF to which the system transfers the subscriber session's traffic.  This column is valid only if the 'domainVrf' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubsessionipaddrassignment
            
            	This object indicates how the system assigns IP addresses to the subscriber\:      'none'         The system does not an involvement in (or is it aware         of) the assignment an subscriber IP addresses.  For         example, a system does not have an involvement in the         assignment of subscriber IP addresses for IP interface         subscriber sessions.      'other'         The system assigns subscriber IP addresses using a         method not recognized by this MIB module.      'static'         Subscriber IP addresses have been configured correctly         for the service domain.  The system does not have an         involvement in the assignment of the IP address.      'localPool'         The system assigns subscriber IP addresses from a         locally configured pool of IP addresses.      'dhcpv4'         The system assigns subscriber IP addresses are using the         DHCPv4.      'dhcpv6'         The system assigns subscriber IP addresses using the         DHCPv6.      'userProfileIpAddr'         The system assigns subscriber IP addresses from a user         profile.      'userProfileIpSubnet'         The system assigns the subscriber an IP subnet from a         user profile.      'userProfileNamedPool'         The system assigns subscriber IP addresses from a         locally configured named pool specified by a user         profile
            	**type**\:   :py:class:`Csubsessionipaddrassignment <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubsessiontable.Csubsessionentry.Csubsessionipaddrassignment>`
            
            .. attribute:: csubsessionlastchanged
            
            	This object indicates when the subscriber session is updated with new policy information
            	**type**\:  str
            
            .. attribute:: csubsessionlocationidentifier
            
            	This object indicates the location of the subscriber
            	**type**\:  str
            
            .. attribute:: csubsessionmacaddress
            
            	This object indicates the MAC address of the subscriber.  This column is valid only if the 'macAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: csubsessionmedia
            
            	This object indicates the type of media providing access to the subscriber.  This column is valid only if the 'media' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:   :py:class:`Subscribermediatype <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.Subscribermediatype>`
            
            .. attribute:: csubsessionmlpnegotiated
            
            	This object indicates whether the subscriber session was established using multi\-link PPP negotiation.  This column is valid only if the 'mlpNegotiated' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  bool
            
            .. attribute:: csubsessionnasport
            
            	This object indicates the NAS port\-identifier identifying the port on the NAS providing access to the subscriber.  This column is valid only if the 'nasPort' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubsessionnativeipaddr
            
            	This object indicates the IP address assigned to the subscriber on the customer\-facing side of the system.  This column is valid only if the 'nativeIpAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: csubsessionnativeipaddr2
            
            	This object indicates the IP address assigned to the subscriber on the customer\-facing side of the system.  This column is valid only if the 'nativeIpAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: csubsessionnativeipaddrtype
            
            	This object indicates the type of IP address assigned to the subscriber on the customer\-facing side of the system.  This column is valid only if the 'nativeIpAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: csubsessionnativeipaddrtype2
            
            	This object indicates the type of IP address assigned to the subscriber on the customer\-facing side of the system.  This column is valid only if the 'nativeIpAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'.  In Dual stack scenarios both 'csubSessionNativeIpAddrType' and  'csubSessionNativeIpAddrType2' will be valid
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: csubsessionnativeipmask
            
            	This object indicates the corresponding mask for the IP address assigned to the subscriber on the customer\-facing side of the system.  This column is valid only if the 'nativeIpAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: csubsessionnativeipmask2
            
            	This object indicates the corresponding mask for the IP address assigned to the subscriber on the customer\-facing side of the system.  This column is valid only if the 'nativeIpAddress' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: csubsessionnativevrf
            
            	This object indicates the VRF originating the subscriber session.  This column is valid only if the 'nativeVrf' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubsessionpbhk
            
            	This object indicates the PBHK identifying the subscriber.  This column is valid only if the 'pbhk' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubsessionprotocol
            
            	This object indicates the type of protocol providing access to the subscriber.  This column is valid only if the 'protocol' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:   :py:class:`Subscriberprotocoltype <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.Subscriberprotocoltype>`
            
            .. attribute:: csubsessionredundancymode
            
            	This object indicates the redundancy mode in which the subscriber session is operating
            	**type**\:   :py:class:`Subsessionredundancymode <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB.Subsessionredundancymode>`
            
            .. attribute:: csubsessionremoteid
            
            	This object indicates the Remote\-Id identifying the 'calling station' or AN supporting the circuit that provides access to the subscriber.  This column is valid only if the 'remoteId' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubsessionserviceidentifier
            
            	This object indicates the name used to identify the services subscribed by a particular session
            	**type**\:  str
            
            .. attribute:: csubsessionstate
            
            	This object indicates the operational state of the subscriber session
            	**type**\:   :py:class:`Subsessionstate <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB.Subsessionstate>`
            
            .. attribute:: csubsessionsubscriberlabel
            
            	This object indicates a positive integer\-value uniquely identifying the subscriber session within the scope of the system.  This column is valid only if the 'subscriberLabel' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csubsessiontunnelname
            
            	This object indicates the name of the VPDN used to carry the subscriber session to the system.  This column is valid only if the 'tunnelName' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubsessiontype
            
            	This object indicates the type of subscriber session
            	**type**\:   :py:class:`Subsessiontype <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB.Subsessiontype>`
            
            .. attribute:: csubsessionusername
            
            	This object indicates the username identifying the subscriber.  This column is valid only if the 'username' bit of the corresponding instance of csubSessionAvailableIdentities is '1'
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CiscoSubscriberSessionMib.Csubsessiontable.Csubsessionentry, self).__init__()

                self.yang_name = "csubSessionEntry"
                self.yang_parent_name = "csubSessionTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.csubsessionacctsessionid = YLeaf(YType.uint32, "csubSessionAcctSessionId")

                self.csubsessionauthenticated = YLeaf(YType.boolean, "csubSessionAuthenticated")

                self.csubsessionavailableidentities = YLeaf(YType.bits, "csubSessionAvailableIdentities")

                self.csubsessioncircuitid = YLeaf(YType.str, "csubSessionCircuitId")

                self.csubsessioncreationtime = YLeaf(YType.str, "csubSessionCreationTime")

                self.csubsessionderivedcfg = YLeaf(YType.str, "csubSessionDerivedCfg")

                self.csubsessiondhcpclass = YLeaf(YType.str, "csubSessionDhcpClass")

                self.csubsessiondnis = YLeaf(YType.str, "csubSessionDnis")

                self.csubsessiondomain = YLeaf(YType.str, "csubSessionDomain")

                self.csubsessiondomainipaddr = YLeaf(YType.str, "csubSessionDomainIpAddr")

                self.csubsessiondomainipaddrtype = YLeaf(YType.enumeration, "csubSessionDomainIpAddrType")

                self.csubsessiondomainipmask = YLeaf(YType.str, "csubSessionDomainIpMask")

                self.csubsessiondomainvrf = YLeaf(YType.str, "csubSessionDomainVrf")

                self.csubsessionipaddrassignment = YLeaf(YType.enumeration, "csubSessionIpAddrAssignment")

                self.csubsessionlastchanged = YLeaf(YType.str, "csubSessionLastChanged")

                self.csubsessionlocationidentifier = YLeaf(YType.str, "csubSessionLocationIdentifier")

                self.csubsessionmacaddress = YLeaf(YType.str, "csubSessionMacAddress")

                self.csubsessionmedia = YLeaf(YType.enumeration, "csubSessionMedia")

                self.csubsessionmlpnegotiated = YLeaf(YType.boolean, "csubSessionMlpNegotiated")

                self.csubsessionnasport = YLeaf(YType.str, "csubSessionNasPort")

                self.csubsessionnativeipaddr = YLeaf(YType.str, "csubSessionNativeIpAddr")

                self.csubsessionnativeipaddr2 = YLeaf(YType.str, "csubSessionNativeIpAddr2")

                self.csubsessionnativeipaddrtype = YLeaf(YType.enumeration, "csubSessionNativeIpAddrType")

                self.csubsessionnativeipaddrtype2 = YLeaf(YType.enumeration, "csubSessionNativeIpAddrType2")

                self.csubsessionnativeipmask = YLeaf(YType.str, "csubSessionNativeIpMask")

                self.csubsessionnativeipmask2 = YLeaf(YType.str, "csubSessionNativeIpMask2")

                self.csubsessionnativevrf = YLeaf(YType.str, "csubSessionNativeVrf")

                self.csubsessionpbhk = YLeaf(YType.str, "csubSessionPbhk")

                self.csubsessionprotocol = YLeaf(YType.enumeration, "csubSessionProtocol")

                self.csubsessionredundancymode = YLeaf(YType.enumeration, "csubSessionRedundancyMode")

                self.csubsessionremoteid = YLeaf(YType.str, "csubSessionRemoteId")

                self.csubsessionserviceidentifier = YLeaf(YType.str, "csubSessionServiceIdentifier")

                self.csubsessionstate = YLeaf(YType.enumeration, "csubSessionState")

                self.csubsessionsubscriberlabel = YLeaf(YType.uint32, "csubSessionSubscriberLabel")

                self.csubsessiontunnelname = YLeaf(YType.str, "csubSessionTunnelName")

                self.csubsessiontype = YLeaf(YType.enumeration, "csubSessionType")

                self.csubsessionusername = YLeaf(YType.str, "csubSessionUsername")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ifindex",
                                "csubsessionacctsessionid",
                                "csubsessionauthenticated",
                                "csubsessionavailableidentities",
                                "csubsessioncircuitid",
                                "csubsessioncreationtime",
                                "csubsessionderivedcfg",
                                "csubsessiondhcpclass",
                                "csubsessiondnis",
                                "csubsessiondomain",
                                "csubsessiondomainipaddr",
                                "csubsessiondomainipaddrtype",
                                "csubsessiondomainipmask",
                                "csubsessiondomainvrf",
                                "csubsessionipaddrassignment",
                                "csubsessionlastchanged",
                                "csubsessionlocationidentifier",
                                "csubsessionmacaddress",
                                "csubsessionmedia",
                                "csubsessionmlpnegotiated",
                                "csubsessionnasport",
                                "csubsessionnativeipaddr",
                                "csubsessionnativeipaddr2",
                                "csubsessionnativeipaddrtype",
                                "csubsessionnativeipaddrtype2",
                                "csubsessionnativeipmask",
                                "csubsessionnativeipmask2",
                                "csubsessionnativevrf",
                                "csubsessionpbhk",
                                "csubsessionprotocol",
                                "csubsessionredundancymode",
                                "csubsessionremoteid",
                                "csubsessionserviceidentifier",
                                "csubsessionstate",
                                "csubsessionsubscriberlabel",
                                "csubsessiontunnelname",
                                "csubsessiontype",
                                "csubsessionusername") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSubscriberSessionMib.Csubsessiontable.Csubsessionentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSubscriberSessionMib.Csubsessiontable.Csubsessionentry, self).__setattr__(name, value)

            class Csubsessionipaddrassignment(Enum):
                """
                Csubsessionipaddrassignment

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


            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.csubsessionacctsessionid.is_set or
                    self.csubsessionauthenticated.is_set or
                    self.csubsessionavailableidentities.is_set or
                    self.csubsessioncircuitid.is_set or
                    self.csubsessioncreationtime.is_set or
                    self.csubsessionderivedcfg.is_set or
                    self.csubsessiondhcpclass.is_set or
                    self.csubsessiondnis.is_set or
                    self.csubsessiondomain.is_set or
                    self.csubsessiondomainipaddr.is_set or
                    self.csubsessiondomainipaddrtype.is_set or
                    self.csubsessiondomainipmask.is_set or
                    self.csubsessiondomainvrf.is_set or
                    self.csubsessionipaddrassignment.is_set or
                    self.csubsessionlastchanged.is_set or
                    self.csubsessionlocationidentifier.is_set or
                    self.csubsessionmacaddress.is_set or
                    self.csubsessionmedia.is_set or
                    self.csubsessionmlpnegotiated.is_set or
                    self.csubsessionnasport.is_set or
                    self.csubsessionnativeipaddr.is_set or
                    self.csubsessionnativeipaddr2.is_set or
                    self.csubsessionnativeipaddrtype.is_set or
                    self.csubsessionnativeipaddrtype2.is_set or
                    self.csubsessionnativeipmask.is_set or
                    self.csubsessionnativeipmask2.is_set or
                    self.csubsessionnativevrf.is_set or
                    self.csubsessionpbhk.is_set or
                    self.csubsessionprotocol.is_set or
                    self.csubsessionredundancymode.is_set or
                    self.csubsessionremoteid.is_set or
                    self.csubsessionserviceidentifier.is_set or
                    self.csubsessionstate.is_set or
                    self.csubsessionsubscriberlabel.is_set or
                    self.csubsessiontunnelname.is_set or
                    self.csubsessiontype.is_set or
                    self.csubsessionusername.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.csubsessionacctsessionid.yfilter != YFilter.not_set or
                    self.csubsessionauthenticated.yfilter != YFilter.not_set or
                    self.csubsessionavailableidentities.yfilter != YFilter.not_set or
                    self.csubsessioncircuitid.yfilter != YFilter.not_set or
                    self.csubsessioncreationtime.yfilter != YFilter.not_set or
                    self.csubsessionderivedcfg.yfilter != YFilter.not_set or
                    self.csubsessiondhcpclass.yfilter != YFilter.not_set or
                    self.csubsessiondnis.yfilter != YFilter.not_set or
                    self.csubsessiondomain.yfilter != YFilter.not_set or
                    self.csubsessiondomainipaddr.yfilter != YFilter.not_set or
                    self.csubsessiondomainipaddrtype.yfilter != YFilter.not_set or
                    self.csubsessiondomainipmask.yfilter != YFilter.not_set or
                    self.csubsessiondomainvrf.yfilter != YFilter.not_set or
                    self.csubsessionipaddrassignment.yfilter != YFilter.not_set or
                    self.csubsessionlastchanged.yfilter != YFilter.not_set or
                    self.csubsessionlocationidentifier.yfilter != YFilter.not_set or
                    self.csubsessionmacaddress.yfilter != YFilter.not_set or
                    self.csubsessionmedia.yfilter != YFilter.not_set or
                    self.csubsessionmlpnegotiated.yfilter != YFilter.not_set or
                    self.csubsessionnasport.yfilter != YFilter.not_set or
                    self.csubsessionnativeipaddr.yfilter != YFilter.not_set or
                    self.csubsessionnativeipaddr2.yfilter != YFilter.not_set or
                    self.csubsessionnativeipaddrtype.yfilter != YFilter.not_set or
                    self.csubsessionnativeipaddrtype2.yfilter != YFilter.not_set or
                    self.csubsessionnativeipmask.yfilter != YFilter.not_set or
                    self.csubsessionnativeipmask2.yfilter != YFilter.not_set or
                    self.csubsessionnativevrf.yfilter != YFilter.not_set or
                    self.csubsessionpbhk.yfilter != YFilter.not_set or
                    self.csubsessionprotocol.yfilter != YFilter.not_set or
                    self.csubsessionredundancymode.yfilter != YFilter.not_set or
                    self.csubsessionremoteid.yfilter != YFilter.not_set or
                    self.csubsessionserviceidentifier.yfilter != YFilter.not_set or
                    self.csubsessionstate.yfilter != YFilter.not_set or
                    self.csubsessionsubscriberlabel.yfilter != YFilter.not_set or
                    self.csubsessiontunnelname.yfilter != YFilter.not_set or
                    self.csubsessiontype.yfilter != YFilter.not_set or
                    self.csubsessionusername.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csubSessionEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubSessionTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.csubsessionacctsessionid.is_set or self.csubsessionacctsessionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionacctsessionid.get_name_leafdata())
                if (self.csubsessionauthenticated.is_set or self.csubsessionauthenticated.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionauthenticated.get_name_leafdata())
                if (self.csubsessionavailableidentities.is_set or self.csubsessionavailableidentities.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionavailableidentities.get_name_leafdata())
                if (self.csubsessioncircuitid.is_set or self.csubsessioncircuitid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessioncircuitid.get_name_leafdata())
                if (self.csubsessioncreationtime.is_set or self.csubsessioncreationtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessioncreationtime.get_name_leafdata())
                if (self.csubsessionderivedcfg.is_set or self.csubsessionderivedcfg.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionderivedcfg.get_name_leafdata())
                if (self.csubsessiondhcpclass.is_set or self.csubsessiondhcpclass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessiondhcpclass.get_name_leafdata())
                if (self.csubsessiondnis.is_set or self.csubsessiondnis.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessiondnis.get_name_leafdata())
                if (self.csubsessiondomain.is_set or self.csubsessiondomain.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessiondomain.get_name_leafdata())
                if (self.csubsessiondomainipaddr.is_set or self.csubsessiondomainipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessiondomainipaddr.get_name_leafdata())
                if (self.csubsessiondomainipaddrtype.is_set or self.csubsessiondomainipaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessiondomainipaddrtype.get_name_leafdata())
                if (self.csubsessiondomainipmask.is_set or self.csubsessiondomainipmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessiondomainipmask.get_name_leafdata())
                if (self.csubsessiondomainvrf.is_set or self.csubsessiondomainvrf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessiondomainvrf.get_name_leafdata())
                if (self.csubsessionipaddrassignment.is_set or self.csubsessionipaddrassignment.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionipaddrassignment.get_name_leafdata())
                if (self.csubsessionlastchanged.is_set or self.csubsessionlastchanged.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionlastchanged.get_name_leafdata())
                if (self.csubsessionlocationidentifier.is_set or self.csubsessionlocationidentifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionlocationidentifier.get_name_leafdata())
                if (self.csubsessionmacaddress.is_set or self.csubsessionmacaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionmacaddress.get_name_leafdata())
                if (self.csubsessionmedia.is_set or self.csubsessionmedia.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionmedia.get_name_leafdata())
                if (self.csubsessionmlpnegotiated.is_set or self.csubsessionmlpnegotiated.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionmlpnegotiated.get_name_leafdata())
                if (self.csubsessionnasport.is_set or self.csubsessionnasport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionnasport.get_name_leafdata())
                if (self.csubsessionnativeipaddr.is_set or self.csubsessionnativeipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionnativeipaddr.get_name_leafdata())
                if (self.csubsessionnativeipaddr2.is_set or self.csubsessionnativeipaddr2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionnativeipaddr2.get_name_leafdata())
                if (self.csubsessionnativeipaddrtype.is_set or self.csubsessionnativeipaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionnativeipaddrtype.get_name_leafdata())
                if (self.csubsessionnativeipaddrtype2.is_set or self.csubsessionnativeipaddrtype2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionnativeipaddrtype2.get_name_leafdata())
                if (self.csubsessionnativeipmask.is_set or self.csubsessionnativeipmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionnativeipmask.get_name_leafdata())
                if (self.csubsessionnativeipmask2.is_set or self.csubsessionnativeipmask2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionnativeipmask2.get_name_leafdata())
                if (self.csubsessionnativevrf.is_set or self.csubsessionnativevrf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionnativevrf.get_name_leafdata())
                if (self.csubsessionpbhk.is_set or self.csubsessionpbhk.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionpbhk.get_name_leafdata())
                if (self.csubsessionprotocol.is_set or self.csubsessionprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionprotocol.get_name_leafdata())
                if (self.csubsessionredundancymode.is_set or self.csubsessionredundancymode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionredundancymode.get_name_leafdata())
                if (self.csubsessionremoteid.is_set or self.csubsessionremoteid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionremoteid.get_name_leafdata())
                if (self.csubsessionserviceidentifier.is_set or self.csubsessionserviceidentifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionserviceidentifier.get_name_leafdata())
                if (self.csubsessionstate.is_set or self.csubsessionstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionstate.get_name_leafdata())
                if (self.csubsessionsubscriberlabel.is_set or self.csubsessionsubscriberlabel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionsubscriberlabel.get_name_leafdata())
                if (self.csubsessiontunnelname.is_set or self.csubsessiontunnelname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessiontunnelname.get_name_leafdata())
                if (self.csubsessiontype.is_set or self.csubsessiontype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessiontype.get_name_leafdata())
                if (self.csubsessionusername.is_set or self.csubsessionusername.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionusername.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "csubSessionAcctSessionId" or name == "csubSessionAuthenticated" or name == "csubSessionAvailableIdentities" or name == "csubSessionCircuitId" or name == "csubSessionCreationTime" or name == "csubSessionDerivedCfg" or name == "csubSessionDhcpClass" or name == "csubSessionDnis" or name == "csubSessionDomain" or name == "csubSessionDomainIpAddr" or name == "csubSessionDomainIpAddrType" or name == "csubSessionDomainIpMask" or name == "csubSessionDomainVrf" or name == "csubSessionIpAddrAssignment" or name == "csubSessionLastChanged" or name == "csubSessionLocationIdentifier" or name == "csubSessionMacAddress" or name == "csubSessionMedia" or name == "csubSessionMlpNegotiated" or name == "csubSessionNasPort" or name == "csubSessionNativeIpAddr" or name == "csubSessionNativeIpAddr2" or name == "csubSessionNativeIpAddrType" or name == "csubSessionNativeIpAddrType2" or name == "csubSessionNativeIpMask" or name == "csubSessionNativeIpMask2" or name == "csubSessionNativeVrf" or name == "csubSessionPbhk" or name == "csubSessionProtocol" or name == "csubSessionRedundancyMode" or name == "csubSessionRemoteId" or name == "csubSessionServiceIdentifier" or name == "csubSessionState" or name == "csubSessionSubscriberLabel" or name == "csubSessionTunnelName" or name == "csubSessionType" or name == "csubSessionUsername"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionAcctSessionId"):
                    self.csubsessionacctsessionid = value
                    self.csubsessionacctsessionid.value_namespace = name_space
                    self.csubsessionacctsessionid.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionAuthenticated"):
                    self.csubsessionauthenticated = value
                    self.csubsessionauthenticated.value_namespace = name_space
                    self.csubsessionauthenticated.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionAvailableIdentities"):
                    self.csubsessionavailableidentities[value] = True
                if(value_path == "csubSessionCircuitId"):
                    self.csubsessioncircuitid = value
                    self.csubsessioncircuitid.value_namespace = name_space
                    self.csubsessioncircuitid.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionCreationTime"):
                    self.csubsessioncreationtime = value
                    self.csubsessioncreationtime.value_namespace = name_space
                    self.csubsessioncreationtime.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionDerivedCfg"):
                    self.csubsessionderivedcfg = value
                    self.csubsessionderivedcfg.value_namespace = name_space
                    self.csubsessionderivedcfg.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionDhcpClass"):
                    self.csubsessiondhcpclass = value
                    self.csubsessiondhcpclass.value_namespace = name_space
                    self.csubsessiondhcpclass.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionDnis"):
                    self.csubsessiondnis = value
                    self.csubsessiondnis.value_namespace = name_space
                    self.csubsessiondnis.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionDomain"):
                    self.csubsessiondomain = value
                    self.csubsessiondomain.value_namespace = name_space
                    self.csubsessiondomain.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionDomainIpAddr"):
                    self.csubsessiondomainipaddr = value
                    self.csubsessiondomainipaddr.value_namespace = name_space
                    self.csubsessiondomainipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionDomainIpAddrType"):
                    self.csubsessiondomainipaddrtype = value
                    self.csubsessiondomainipaddrtype.value_namespace = name_space
                    self.csubsessiondomainipaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionDomainIpMask"):
                    self.csubsessiondomainipmask = value
                    self.csubsessiondomainipmask.value_namespace = name_space
                    self.csubsessiondomainipmask.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionDomainVrf"):
                    self.csubsessiondomainvrf = value
                    self.csubsessiondomainvrf.value_namespace = name_space
                    self.csubsessiondomainvrf.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionIpAddrAssignment"):
                    self.csubsessionipaddrassignment = value
                    self.csubsessionipaddrassignment.value_namespace = name_space
                    self.csubsessionipaddrassignment.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionLastChanged"):
                    self.csubsessionlastchanged = value
                    self.csubsessionlastchanged.value_namespace = name_space
                    self.csubsessionlastchanged.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionLocationIdentifier"):
                    self.csubsessionlocationidentifier = value
                    self.csubsessionlocationidentifier.value_namespace = name_space
                    self.csubsessionlocationidentifier.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionMacAddress"):
                    self.csubsessionmacaddress = value
                    self.csubsessionmacaddress.value_namespace = name_space
                    self.csubsessionmacaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionMedia"):
                    self.csubsessionmedia = value
                    self.csubsessionmedia.value_namespace = name_space
                    self.csubsessionmedia.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionMlpNegotiated"):
                    self.csubsessionmlpnegotiated = value
                    self.csubsessionmlpnegotiated.value_namespace = name_space
                    self.csubsessionmlpnegotiated.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionNasPort"):
                    self.csubsessionnasport = value
                    self.csubsessionnasport.value_namespace = name_space
                    self.csubsessionnasport.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionNativeIpAddr"):
                    self.csubsessionnativeipaddr = value
                    self.csubsessionnativeipaddr.value_namespace = name_space
                    self.csubsessionnativeipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionNativeIpAddr2"):
                    self.csubsessionnativeipaddr2 = value
                    self.csubsessionnativeipaddr2.value_namespace = name_space
                    self.csubsessionnativeipaddr2.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionNativeIpAddrType"):
                    self.csubsessionnativeipaddrtype = value
                    self.csubsessionnativeipaddrtype.value_namespace = name_space
                    self.csubsessionnativeipaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionNativeIpAddrType2"):
                    self.csubsessionnativeipaddrtype2 = value
                    self.csubsessionnativeipaddrtype2.value_namespace = name_space
                    self.csubsessionnativeipaddrtype2.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionNativeIpMask"):
                    self.csubsessionnativeipmask = value
                    self.csubsessionnativeipmask.value_namespace = name_space
                    self.csubsessionnativeipmask.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionNativeIpMask2"):
                    self.csubsessionnativeipmask2 = value
                    self.csubsessionnativeipmask2.value_namespace = name_space
                    self.csubsessionnativeipmask2.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionNativeVrf"):
                    self.csubsessionnativevrf = value
                    self.csubsessionnativevrf.value_namespace = name_space
                    self.csubsessionnativevrf.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionPbhk"):
                    self.csubsessionpbhk = value
                    self.csubsessionpbhk.value_namespace = name_space
                    self.csubsessionpbhk.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionProtocol"):
                    self.csubsessionprotocol = value
                    self.csubsessionprotocol.value_namespace = name_space
                    self.csubsessionprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionRedundancyMode"):
                    self.csubsessionredundancymode = value
                    self.csubsessionredundancymode.value_namespace = name_space
                    self.csubsessionredundancymode.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionRemoteId"):
                    self.csubsessionremoteid = value
                    self.csubsessionremoteid.value_namespace = name_space
                    self.csubsessionremoteid.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionServiceIdentifier"):
                    self.csubsessionserviceidentifier = value
                    self.csubsessionserviceidentifier.value_namespace = name_space
                    self.csubsessionserviceidentifier.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionState"):
                    self.csubsessionstate = value
                    self.csubsessionstate.value_namespace = name_space
                    self.csubsessionstate.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionSubscriberLabel"):
                    self.csubsessionsubscriberlabel = value
                    self.csubsessionsubscriberlabel.value_namespace = name_space
                    self.csubsessionsubscriberlabel.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionTunnelName"):
                    self.csubsessiontunnelname = value
                    self.csubsessiontunnelname.value_namespace = name_space
                    self.csubsessiontunnelname.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionType"):
                    self.csubsessiontype = value
                    self.csubsessiontype.value_namespace = name_space
                    self.csubsessiontype.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionUsername"):
                    self.csubsessionusername = value
                    self.csubsessionusername.value_namespace = name_space
                    self.csubsessionusername.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csubsessionentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csubsessionentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csubSessionTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csubSessionEntry"):
                for c in self.csubsessionentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSubscriberSessionMib.Csubsessiontable.Csubsessionentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csubsessionentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csubSessionEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csubsessionbytypetable(Entity):
        """
        This table describes a list of subscriber sessions currently
        maintained by the system.  The tables sorts the subscriber
        sessions first by the subscriber session's type and second by
        the ifIndex assigned to the subscriber session.
        
        .. attribute:: csubsessionbytypeentry
        
        	This entry identifies a subscriber session.  An entry exists for a corresponding entry in the ifTable describing a subscriber session.  Currently, subscriber sessions must have one of the following ifType values\:      'ppp'     'ipSubscriberSession'     'l2SubscriberSession'  The system creates an entry when it establishes a subscriber session.  Likewise, the system destroys an entry when it terminates the corresponding subscriber session
        	**type**\: list of    :py:class:`Csubsessionbytypeentry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubsessionbytypetable.Csubsessionbytypeentry>`
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CiscoSubscriberSessionMib.Csubsessionbytypetable, self).__init__()

            self.yang_name = "csubSessionByTypeTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"

            self.csubsessionbytypeentry = YList(self)

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
                        super(CiscoSubscriberSessionMib.Csubsessionbytypetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSubscriberSessionMib.Csubsessionbytypetable, self).__setattr__(name, value)


        class Csubsessionbytypeentry(Entity):
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
            
            .. attribute:: csubsessionbytype  <key>
            
            	This object indicates the type of the subscriber session
            	**type**\:   :py:class:`Subsessiontype <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB.Subsessiontype>`
            
            .. attribute:: csubsessionifindex  <key>
            
            	This object indicates the ifIndex assigned to the subscriber session
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CiscoSubscriberSessionMib.Csubsessionbytypetable.Csubsessionbytypeentry, self).__init__()

                self.yang_name = "csubSessionByTypeEntry"
                self.yang_parent_name = "csubSessionByTypeTable"

                self.csubsessionbytype = YLeaf(YType.enumeration, "csubSessionByType")

                self.csubsessionifindex = YLeaf(YType.int32, "csubSessionIfIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csubsessionbytype",
                                "csubsessionifindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSubscriberSessionMib.Csubsessionbytypetable.Csubsessionbytypeentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSubscriberSessionMib.Csubsessionbytypetable.Csubsessionbytypeentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csubsessionbytype.is_set or
                    self.csubsessionifindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csubsessionbytype.yfilter != YFilter.not_set or
                    self.csubsessionifindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csubSessionByTypeEntry" + "[csubSessionByType='" + self.csubsessionbytype.get() + "']" + "[csubSessionIfIndex='" + self.csubsessionifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubSessionByTypeTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csubsessionbytype.is_set or self.csubsessionbytype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionbytype.get_name_leafdata())
                if (self.csubsessionifindex.is_set or self.csubsessionifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionifindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csubSessionByType" or name == "csubSessionIfIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "csubSessionByType"):
                    self.csubsessionbytype = value
                    self.csubsessionbytype.value_namespace = name_space
                    self.csubsessionbytype.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionIfIndex"):
                    self.csubsessionifindex = value
                    self.csubsessionifindex.value_namespace = name_space
                    self.csubsessionifindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csubsessionbytypeentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csubsessionbytypeentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csubSessionByTypeTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csubSessionByTypeEntry"):
                for c in self.csubsessionbytypeentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSubscriberSessionMib.Csubsessionbytypetable.Csubsessionbytypeentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csubsessionbytypeentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csubSessionByTypeEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csubaggstatstable(Entity):
        """
        This table contains sets of aggregated statistics relating to
        subscriber sessions, where each set has a unique scope of
        aggregation.
        
        .. attribute:: csubaggstatsentry
        
        	An entry contains a set of aggregated statistics relating to those subscriber sessions that fall into a 'scope of  aggregation'.   A 'scope of aggregation' is the set of subscriber sessions  that meet specified criteria.  For example, a 'scope of  aggregation' may be the set of all PPPoE subscriber sessions  maintained by the system.  The following criteria define the  'scope of aggregation'\:   1)  Aggregation Point type          Aggregation point type identifies the format of the          csubAggStatsPoint for this entry.   2)  Aggregation Point          'Physical' Aggregation Point type case\:          In a distributed system, a 'node' represents a physical          entity capable of maintaining the context representing          a subscriber session.           If the 'scope of aggregation' specifies a physical          entity having an entPhysicalClass of 'chassis', then          the set of subscriber sessions in the 'scope of          aggregation' may contain the subscriber sessions maintained by all          the nodes contained in the system.           If the 'scope of aggregation' specifies a physical          entity having an entPhysicalClass of 'module' (e.g., a          line card), then the set of subscriber sessions in the          'scope of aggregation' may contain the subscriber          sessions maintained by the nodes contained by the          module.           If the 'scope of aggregation' specifies a physical          entity having an entPhysicalClass of 'cpu', then the          set of subscriber sessions in the 'scope of aggregation'          may contain the subscriber sessions maintained by the node          running on that processor.           Observe that a centralized system (i.e., a system          that essentially contains a single node) can only          support a 'scope of aggregation' that specifies a          physical entity classified as a 'chassis'.           If the scope of aggregation specifies 'interface',          then the scope is the set of subscriber sessions carried          by the interface identified the ifIndex value          represented in the csubAggStatsPoint value.   2)  Subscriber Session Type          If the 'scope of aggregation' specifies the value 'all'          for the subscriber session type, then the set of          subscriber sessions in the 'scope of aggregation' may          contain all subscriber sessions, regardless of type.           If the 'scope of aggregation' specifies a value other          than 'all' for the subscriber session type, then the          set of subscriber sessions in the 'scope of aggregation may          contain only those subscriber sessions of the specified          type.   Implementation Guidance  =======================  A system MUST maintain a set of statistics with a 'scope of  aggregation' that contains all subscriber sessions maintained  by the system.  The system creates this entry during the  initialization of the SNMP entity.   A system SHOULD maintain a set of statistics for each 'scope of  aggregation' containing subscriber sessions of each subscriber  session type the system is capable of providing access.  If the  system supports these sets of statistics, then it creates these  entries during the initialization of the SNMP entity.   A system MAY maintain sets of node\-specific statistics.  if the  system supports sets of node\-specific statistics, then it  creates the appropriate entries upon detection of a physical  entity (resulting from system restart or insertion) containing  those nodes.  Likewise, the system destroys these entries  upon removal of the physical entity
        	**type**\: list of    :py:class:`Csubaggstatsentry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubaggstatstable.Csubaggstatsentry>`
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CiscoSubscriberSessionMib.Csubaggstatstable, self).__init__()

            self.yang_name = "csubAggStatsTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"

            self.csubaggstatsentry = YList(self)

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
                        super(CiscoSubscriberSessionMib.Csubaggstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSubscriberSessionMib.Csubaggstatstable, self).__setattr__(name, value)


        class Csubaggstatsentry(Entity):
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
            
            .. attribute:: csubaggstatspointtype  <key>
            
            	This object indicates format of the csubAggStatsPoint for this entry.   The format for the csubAggStatsPoint is as follows\:   csubAggStatsPointType      csubAggStatsPoint  \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-     \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-      'physical'                 PhysicalIndex      'interface'                InterfaceIndex
            	**type**\:   :py:class:`Csubaggstatspointtype <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubaggstatstable.Csubaggstatsentry.Csubaggstatspointtype>`
            
            .. attribute:: csubaggstatspoint  <key>
            
            	This object should be read with csubAggStatsPointType always.  This object indicates one of the determining factors affecting  the 'scope of aggregation' for the set of statistics contained  by the row.   The value indicated by this object should be interpreted as the  identifier for the point type specific base table.   For point types of 'physical', the type specific base table is  the entPhysicalTable and this value is a PhysicalIndex.  For  point types of 'interface', the type specific base table is  the ifTable and this value is an InterfaceIndex.   If this column indicates a physical entity which has an  entPhysicalClass of 'chassis', then the 'scope of aggregation'  may includes those subscriber sessions maintained by all nodes  contained by the system.   If this column indicates a physical entity which has an  entPhysicalClass of  'module' (e.g., a line card), then the  'scope of aggregation' may include those subscriber sessions  maintained by the nodes contained by the module.   If this column indicates a physical entity which has an  entPhysicalClass of 'cpu', then the 'scope of aggregation' may  include those subscriber sessions maintained by the node  running on the processor.   Aggregation points with entPhysicalTable / ifTable overlap\:  For interfaces which map directly to physical 'port' class  entities in the entPhysicalTable, the preferred representation  as aggregation points is the 'physical' point type and  PhysicalIndex identifier
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: csubaggstatssessiontype  <key>
            
            	This object indicates one of the determining factors affecting the 'scope of aggregation' for the statistics contained by the row.  If the value of this column is 'all', then the 'scope of aggregation' may include all subscriber sessions, regardless of type.  If the value of this column is not 'all', then the 'scope of aggregation' may include subscriber sessions of the indicated subscriber session type
            	**type**\:   :py:class:`Subsessiontype <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB.Subsessiontype>`
            
            .. attribute:: csubaggstatsauthsessions
            
            	This object indicates the current number of subscriber session within the 'scope of aggregation' that have been authenticated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsavgsessionrph
            
            	This object indicates the average rate (per hour) at which the nodes contained by the 'scope of aggregation' have established new subscriber sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions per hour
            
            .. attribute:: csubaggstatsavgsessionrpm
            
            	This object indicates the average rate (per minute) at which the nodes contained by the 'scope of aggregation' have established new subscriber sessions
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions per minute
            
            .. attribute:: csubaggstatsavgsessionuptime
            
            	This object indicates the average time subscriber sessions within the 'scope of aggregation' spent in the UP state.  The system calculates this average over all subscriber sessions maintained by all nodes contained by the 'scope of aggregation' since the last discontinuity time
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: csubaggstatscurrauthsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that transitioned from the UNAUTHENTICATED to the AUTHENTICATED state during the current 15\-minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatscurrcreatedsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' created during the current 15\-minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatscurrdiscsessions
            
            	This object indicates the total number of subscriber sessions terminated due to a disconnect event during the current 15\-minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatscurrfailedsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that were in the PENDING state and terminated for reasons other than disconnect during the current 15\-minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatscurrflowsup
            
            	This object indicates the current number of differential traffic classes on subscriber sessions currently UP. IP ACLs are used to create differential flows (Traffic Classes).Each Traffic Class can have a different set of features applied
            	**type**\:  int
            
            	**range:** 0..96
            
            	**units**\: intervals
            
            .. attribute:: csubaggstatscurrinvalidintervals
            
            	This object indicates the number of intervals in the range from 0 to csubCurrValidIntervals for which no data is available.  This object will typically be '0' except in certain circumstances when some intervals are unavailable
            	**type**\:  int
            
            	**range:** 0..96
            
            	**units**\: intervals
            
            .. attribute:: csubaggstatscurrtimeelapsed
            
            	This object indicates the time that has elapsed since the beginning of the current 15\-minute measurement interval.  If, for some reason, such as an adjustment in the system's time\-of\-day clock, the current interval exceeds the maximum value, then the value of this column will be the maximum value
            	**type**\:  int
            
            	**range:** 0..899
            
            	**units**\: seconds
            
            .. attribute:: csubaggstatscurrupsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that transitioned to the UP state during the current 15\-minute interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatscurrvalidintervals
            
            	This object indicates the number of intervals for which data was collected.  The value of this column will be '96' unless the measurement was started (or restarted) within 1,440 minutes, in which case the value will be the number of complete 15\-minute intervals for which the system has at least some data.  In certain cases it is possible that some intervals are unavailable, in which case the value of this column will be maximum interval number for which data is available
            	**type**\:  int
            
            	**range:** 0..96
            
            	**units**\: intervals
            
            .. attribute:: csubaggstatsdayauthsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that transitioned from the UNAUTHENTICATED to the AUTHENTICATED state during the last 24 hours.  The system calculates the value of this column by summing the values of all instances of csubAggStatsIntAuthSessions that expand this row and have a corresponding csubAggStatsIntValid of 'true'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsdaycreatedsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' created during the last 24 hours.  The system calculates the value of this column by summing the values of all instances of csubAggStatsIntCreatedSessions that expand this row and have a corresponding csubAggStatsIntValid of 'true'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsdaydiscsessions
            
            	This object indicates the total number of subscriber sessions terminated due to a disconnect event during the last 24 hours.  The system calculates the value of this column by summing the values of all instances of csubAggStatsIntDiscSessions that expand this row and have a corresponding csubAggStatsIntValid of 'true'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsdayfailedsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that were in the PENDING state and terminated for reasons other than disconnect during the last 24 hours.  The system calculates the value of this column by summing the values of all instances of csubAggStatsIntFailedSessions that expand this row and have a corresponding csubAggStatsIntValid of 'true'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsdayupsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that transitioned to the UP state during the last 24 hours.  The system calculates the value of this column by summing the values of all instances of csubAggStatsIntUpSessions that expand this row and have a corresponding csubAggStatsIntValid of 'true'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsdiscontinuitytime
            
            	The date and time (as determined by the system's clock) of the most recent occurrence of an event affecting the  continuity of the aggregation statistics for this aggregation  point
            	**type**\:  str
            
            .. attribute:: csubaggstatshighupsessions
            
            	This object indicates the highest number of subscriber sessions within the 'scope of aggregation' observed simultaneously in the UP state since the last discontinuity time
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatslightweightsessions
            
            	This object indicates the current number of subscriber sessions within the 'scope of aggregation' that are less resource intensive
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatspendingsessions
            
            	This object indicates the current number of subscriber sessions within the 'scope of aggregation' that are in the PENDING state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsredsessions
            
            	This object indicates the current number of subscriber sessions within the 'scope of aggregation' that are redundant (i.e.,  sessions with a csubSessionRedundancyMode of 'standby')
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsthrottleengagements
            
            	This object indicates the number of times that nodes contained within the 'scope of aggregation' have engaged the subscriber session throttle since the last discontinuity time.  The mechanics of a subscriber session throttle vary with subscriber session type and implementation.  However, the general concept of the throttle prevents a node from having to deal with more than a configured number of requests to establish subscriber sessions from the same CPE within the a configured interval of time.  When the number of requests exceeds the configured threshold within the configured interval, then the node processing the requests engages the throttle. Typically, when a node engages a throttle, it drops requests from the CPE for some period of time, after which the node disengages the throttle.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of csubAggStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: engagements
            
            .. attribute:: csubaggstatstotalauthsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that transitioned from the UNAUTHENTICATED to the AUTHENTICATED state since the last discontinuity time.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of csubAggStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatstotalcreatedsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' created since the discontinuity time.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of csubAggStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatstotaldiscsessions
            
            	This object indicates the total number of subscriber sessions terminated due to a disconnect event since the last discontinuity time.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of csubAggStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatstotalfailedsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that were in the PENDING state and terminated for reasons other than disconnect since the last discontinuity time.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of csubAggStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatstotalflowsup
            
            	This object indicates the total number of differential traffic classes on subscriber sessions. IP ACLs are used to create differential flows(Traffic Classes).  Each Traffic Class can have a different set of features applied
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatstotallightweightsessions
            
            	This object indicates the total number of subscriber sessions that are less resource intensive
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatstotalupsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that transitioned to the UP state since the last discontinuity time.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of csubAggStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsunauthsessions
            
            	This object indicates the current number of subscriber session within the 'scope of aggregation' that have not been authenticated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsupsessions
            
            	This object indicates the current number of subscriber sessions within the 'scope of aggregation' that are in the UP state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CiscoSubscriberSessionMib.Csubaggstatstable.Csubaggstatsentry, self).__init__()

                self.yang_name = "csubAggStatsEntry"
                self.yang_parent_name = "csubAggStatsTable"

                self.csubaggstatspointtype = YLeaf(YType.enumeration, "csubAggStatsPointType")

                self.csubaggstatspoint = YLeaf(YType.uint32, "csubAggStatsPoint")

                self.csubaggstatssessiontype = YLeaf(YType.enumeration, "csubAggStatsSessionType")

                self.csubaggstatsauthsessions = YLeaf(YType.uint32, "csubAggStatsAuthSessions")

                self.csubaggstatsavgsessionrph = YLeaf(YType.uint32, "csubAggStatsAvgSessionRPH")

                self.csubaggstatsavgsessionrpm = YLeaf(YType.uint32, "csubAggStatsAvgSessionRPM")

                self.csubaggstatsavgsessionuptime = YLeaf(YType.uint32, "csubAggStatsAvgSessionUptime")

                self.csubaggstatscurrauthsessions = YLeaf(YType.uint32, "csubAggStatsCurrAuthSessions")

                self.csubaggstatscurrcreatedsessions = YLeaf(YType.uint32, "csubAggStatsCurrCreatedSessions")

                self.csubaggstatscurrdiscsessions = YLeaf(YType.uint32, "csubAggStatsCurrDiscSessions")

                self.csubaggstatscurrfailedsessions = YLeaf(YType.uint32, "csubAggStatsCurrFailedSessions")

                self.csubaggstatscurrflowsup = YLeaf(YType.uint32, "csubAggStatsCurrFlowsUp")

                self.csubaggstatscurrinvalidintervals = YLeaf(YType.uint32, "csubAggStatsCurrInvalidIntervals")

                self.csubaggstatscurrtimeelapsed = YLeaf(YType.uint32, "csubAggStatsCurrTimeElapsed")

                self.csubaggstatscurrupsessions = YLeaf(YType.uint32, "csubAggStatsCurrUpSessions")

                self.csubaggstatscurrvalidintervals = YLeaf(YType.uint32, "csubAggStatsCurrValidIntervals")

                self.csubaggstatsdayauthsessions = YLeaf(YType.uint32, "csubAggStatsDayAuthSessions")

                self.csubaggstatsdaycreatedsessions = YLeaf(YType.uint32, "csubAggStatsDayCreatedSessions")

                self.csubaggstatsdaydiscsessions = YLeaf(YType.uint32, "csubAggStatsDayDiscSessions")

                self.csubaggstatsdayfailedsessions = YLeaf(YType.uint32, "csubAggStatsDayFailedSessions")

                self.csubaggstatsdayupsessions = YLeaf(YType.uint32, "csubAggStatsDayUpSessions")

                self.csubaggstatsdiscontinuitytime = YLeaf(YType.str, "csubAggStatsDiscontinuityTime")

                self.csubaggstatshighupsessions = YLeaf(YType.uint32, "csubAggStatsHighUpSessions")

                self.csubaggstatslightweightsessions = YLeaf(YType.uint32, "csubAggStatsLightWeightSessions")

                self.csubaggstatspendingsessions = YLeaf(YType.uint32, "csubAggStatsPendingSessions")

                self.csubaggstatsredsessions = YLeaf(YType.uint32, "csubAggStatsRedSessions")

                self.csubaggstatsthrottleengagements = YLeaf(YType.uint64, "csubAggStatsThrottleEngagements")

                self.csubaggstatstotalauthsessions = YLeaf(YType.uint64, "csubAggStatsTotalAuthSessions")

                self.csubaggstatstotalcreatedsessions = YLeaf(YType.uint64, "csubAggStatsTotalCreatedSessions")

                self.csubaggstatstotaldiscsessions = YLeaf(YType.uint64, "csubAggStatsTotalDiscSessions")

                self.csubaggstatstotalfailedsessions = YLeaf(YType.uint64, "csubAggStatsTotalFailedSessions")

                self.csubaggstatstotalflowsup = YLeaf(YType.uint64, "csubAggStatsTotalFlowsUp")

                self.csubaggstatstotallightweightsessions = YLeaf(YType.uint64, "csubAggStatsTotalLightWeightSessions")

                self.csubaggstatstotalupsessions = YLeaf(YType.uint64, "csubAggStatsTotalUpSessions")

                self.csubaggstatsunauthsessions = YLeaf(YType.uint32, "csubAggStatsUnAuthSessions")

                self.csubaggstatsupsessions = YLeaf(YType.uint32, "csubAggStatsUpSessions")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csubaggstatspointtype",
                                "csubaggstatspoint",
                                "csubaggstatssessiontype",
                                "csubaggstatsauthsessions",
                                "csubaggstatsavgsessionrph",
                                "csubaggstatsavgsessionrpm",
                                "csubaggstatsavgsessionuptime",
                                "csubaggstatscurrauthsessions",
                                "csubaggstatscurrcreatedsessions",
                                "csubaggstatscurrdiscsessions",
                                "csubaggstatscurrfailedsessions",
                                "csubaggstatscurrflowsup",
                                "csubaggstatscurrinvalidintervals",
                                "csubaggstatscurrtimeelapsed",
                                "csubaggstatscurrupsessions",
                                "csubaggstatscurrvalidintervals",
                                "csubaggstatsdayauthsessions",
                                "csubaggstatsdaycreatedsessions",
                                "csubaggstatsdaydiscsessions",
                                "csubaggstatsdayfailedsessions",
                                "csubaggstatsdayupsessions",
                                "csubaggstatsdiscontinuitytime",
                                "csubaggstatshighupsessions",
                                "csubaggstatslightweightsessions",
                                "csubaggstatspendingsessions",
                                "csubaggstatsredsessions",
                                "csubaggstatsthrottleengagements",
                                "csubaggstatstotalauthsessions",
                                "csubaggstatstotalcreatedsessions",
                                "csubaggstatstotaldiscsessions",
                                "csubaggstatstotalfailedsessions",
                                "csubaggstatstotalflowsup",
                                "csubaggstatstotallightweightsessions",
                                "csubaggstatstotalupsessions",
                                "csubaggstatsunauthsessions",
                                "csubaggstatsupsessions") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSubscriberSessionMib.Csubaggstatstable.Csubaggstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSubscriberSessionMib.Csubaggstatstable.Csubaggstatsentry, self).__setattr__(name, value)

            class Csubaggstatspointtype(Enum):
                """
                Csubaggstatspointtype

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


            def has_data(self):
                return (
                    self.csubaggstatspointtype.is_set or
                    self.csubaggstatspoint.is_set or
                    self.csubaggstatssessiontype.is_set or
                    self.csubaggstatsauthsessions.is_set or
                    self.csubaggstatsavgsessionrph.is_set or
                    self.csubaggstatsavgsessionrpm.is_set or
                    self.csubaggstatsavgsessionuptime.is_set or
                    self.csubaggstatscurrauthsessions.is_set or
                    self.csubaggstatscurrcreatedsessions.is_set or
                    self.csubaggstatscurrdiscsessions.is_set or
                    self.csubaggstatscurrfailedsessions.is_set or
                    self.csubaggstatscurrflowsup.is_set or
                    self.csubaggstatscurrinvalidintervals.is_set or
                    self.csubaggstatscurrtimeelapsed.is_set or
                    self.csubaggstatscurrupsessions.is_set or
                    self.csubaggstatscurrvalidintervals.is_set or
                    self.csubaggstatsdayauthsessions.is_set or
                    self.csubaggstatsdaycreatedsessions.is_set or
                    self.csubaggstatsdaydiscsessions.is_set or
                    self.csubaggstatsdayfailedsessions.is_set or
                    self.csubaggstatsdayupsessions.is_set or
                    self.csubaggstatsdiscontinuitytime.is_set or
                    self.csubaggstatshighupsessions.is_set or
                    self.csubaggstatslightweightsessions.is_set or
                    self.csubaggstatspendingsessions.is_set or
                    self.csubaggstatsredsessions.is_set or
                    self.csubaggstatsthrottleengagements.is_set or
                    self.csubaggstatstotalauthsessions.is_set or
                    self.csubaggstatstotalcreatedsessions.is_set or
                    self.csubaggstatstotaldiscsessions.is_set or
                    self.csubaggstatstotalfailedsessions.is_set or
                    self.csubaggstatstotalflowsup.is_set or
                    self.csubaggstatstotallightweightsessions.is_set or
                    self.csubaggstatstotalupsessions.is_set or
                    self.csubaggstatsunauthsessions.is_set or
                    self.csubaggstatsupsessions.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csubaggstatspointtype.yfilter != YFilter.not_set or
                    self.csubaggstatspoint.yfilter != YFilter.not_set or
                    self.csubaggstatssessiontype.yfilter != YFilter.not_set or
                    self.csubaggstatsauthsessions.yfilter != YFilter.not_set or
                    self.csubaggstatsavgsessionrph.yfilter != YFilter.not_set or
                    self.csubaggstatsavgsessionrpm.yfilter != YFilter.not_set or
                    self.csubaggstatsavgsessionuptime.yfilter != YFilter.not_set or
                    self.csubaggstatscurrauthsessions.yfilter != YFilter.not_set or
                    self.csubaggstatscurrcreatedsessions.yfilter != YFilter.not_set or
                    self.csubaggstatscurrdiscsessions.yfilter != YFilter.not_set or
                    self.csubaggstatscurrfailedsessions.yfilter != YFilter.not_set or
                    self.csubaggstatscurrflowsup.yfilter != YFilter.not_set or
                    self.csubaggstatscurrinvalidintervals.yfilter != YFilter.not_set or
                    self.csubaggstatscurrtimeelapsed.yfilter != YFilter.not_set or
                    self.csubaggstatscurrupsessions.yfilter != YFilter.not_set or
                    self.csubaggstatscurrvalidintervals.yfilter != YFilter.not_set or
                    self.csubaggstatsdayauthsessions.yfilter != YFilter.not_set or
                    self.csubaggstatsdaycreatedsessions.yfilter != YFilter.not_set or
                    self.csubaggstatsdaydiscsessions.yfilter != YFilter.not_set or
                    self.csubaggstatsdayfailedsessions.yfilter != YFilter.not_set or
                    self.csubaggstatsdayupsessions.yfilter != YFilter.not_set or
                    self.csubaggstatsdiscontinuitytime.yfilter != YFilter.not_set or
                    self.csubaggstatshighupsessions.yfilter != YFilter.not_set or
                    self.csubaggstatslightweightsessions.yfilter != YFilter.not_set or
                    self.csubaggstatspendingsessions.yfilter != YFilter.not_set or
                    self.csubaggstatsredsessions.yfilter != YFilter.not_set or
                    self.csubaggstatsthrottleengagements.yfilter != YFilter.not_set or
                    self.csubaggstatstotalauthsessions.yfilter != YFilter.not_set or
                    self.csubaggstatstotalcreatedsessions.yfilter != YFilter.not_set or
                    self.csubaggstatstotaldiscsessions.yfilter != YFilter.not_set or
                    self.csubaggstatstotalfailedsessions.yfilter != YFilter.not_set or
                    self.csubaggstatstotalflowsup.yfilter != YFilter.not_set or
                    self.csubaggstatstotallightweightsessions.yfilter != YFilter.not_set or
                    self.csubaggstatstotalupsessions.yfilter != YFilter.not_set or
                    self.csubaggstatsunauthsessions.yfilter != YFilter.not_set or
                    self.csubaggstatsupsessions.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csubAggStatsEntry" + "[csubAggStatsPointType='" + self.csubaggstatspointtype.get() + "']" + "[csubAggStatsPoint='" + self.csubaggstatspoint.get() + "']" + "[csubAggStatsSessionType='" + self.csubaggstatssessiontype.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubAggStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csubaggstatspointtype.is_set or self.csubaggstatspointtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatspointtype.get_name_leafdata())
                if (self.csubaggstatspoint.is_set or self.csubaggstatspoint.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatspoint.get_name_leafdata())
                if (self.csubaggstatssessiontype.is_set or self.csubaggstatssessiontype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatssessiontype.get_name_leafdata())
                if (self.csubaggstatsauthsessions.is_set or self.csubaggstatsauthsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsauthsessions.get_name_leafdata())
                if (self.csubaggstatsavgsessionrph.is_set or self.csubaggstatsavgsessionrph.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsavgsessionrph.get_name_leafdata())
                if (self.csubaggstatsavgsessionrpm.is_set or self.csubaggstatsavgsessionrpm.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsavgsessionrpm.get_name_leafdata())
                if (self.csubaggstatsavgsessionuptime.is_set or self.csubaggstatsavgsessionuptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsavgsessionuptime.get_name_leafdata())
                if (self.csubaggstatscurrauthsessions.is_set or self.csubaggstatscurrauthsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatscurrauthsessions.get_name_leafdata())
                if (self.csubaggstatscurrcreatedsessions.is_set or self.csubaggstatscurrcreatedsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatscurrcreatedsessions.get_name_leafdata())
                if (self.csubaggstatscurrdiscsessions.is_set or self.csubaggstatscurrdiscsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatscurrdiscsessions.get_name_leafdata())
                if (self.csubaggstatscurrfailedsessions.is_set or self.csubaggstatscurrfailedsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatscurrfailedsessions.get_name_leafdata())
                if (self.csubaggstatscurrflowsup.is_set or self.csubaggstatscurrflowsup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatscurrflowsup.get_name_leafdata())
                if (self.csubaggstatscurrinvalidintervals.is_set or self.csubaggstatscurrinvalidintervals.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatscurrinvalidintervals.get_name_leafdata())
                if (self.csubaggstatscurrtimeelapsed.is_set or self.csubaggstatscurrtimeelapsed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatscurrtimeelapsed.get_name_leafdata())
                if (self.csubaggstatscurrupsessions.is_set or self.csubaggstatscurrupsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatscurrupsessions.get_name_leafdata())
                if (self.csubaggstatscurrvalidintervals.is_set or self.csubaggstatscurrvalidintervals.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatscurrvalidintervals.get_name_leafdata())
                if (self.csubaggstatsdayauthsessions.is_set or self.csubaggstatsdayauthsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsdayauthsessions.get_name_leafdata())
                if (self.csubaggstatsdaycreatedsessions.is_set or self.csubaggstatsdaycreatedsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsdaycreatedsessions.get_name_leafdata())
                if (self.csubaggstatsdaydiscsessions.is_set or self.csubaggstatsdaydiscsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsdaydiscsessions.get_name_leafdata())
                if (self.csubaggstatsdayfailedsessions.is_set or self.csubaggstatsdayfailedsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsdayfailedsessions.get_name_leafdata())
                if (self.csubaggstatsdayupsessions.is_set or self.csubaggstatsdayupsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsdayupsessions.get_name_leafdata())
                if (self.csubaggstatsdiscontinuitytime.is_set or self.csubaggstatsdiscontinuitytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsdiscontinuitytime.get_name_leafdata())
                if (self.csubaggstatshighupsessions.is_set or self.csubaggstatshighupsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatshighupsessions.get_name_leafdata())
                if (self.csubaggstatslightweightsessions.is_set or self.csubaggstatslightweightsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatslightweightsessions.get_name_leafdata())
                if (self.csubaggstatspendingsessions.is_set or self.csubaggstatspendingsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatspendingsessions.get_name_leafdata())
                if (self.csubaggstatsredsessions.is_set or self.csubaggstatsredsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsredsessions.get_name_leafdata())
                if (self.csubaggstatsthrottleengagements.is_set or self.csubaggstatsthrottleengagements.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsthrottleengagements.get_name_leafdata())
                if (self.csubaggstatstotalauthsessions.is_set or self.csubaggstatstotalauthsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatstotalauthsessions.get_name_leafdata())
                if (self.csubaggstatstotalcreatedsessions.is_set or self.csubaggstatstotalcreatedsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatstotalcreatedsessions.get_name_leafdata())
                if (self.csubaggstatstotaldiscsessions.is_set or self.csubaggstatstotaldiscsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatstotaldiscsessions.get_name_leafdata())
                if (self.csubaggstatstotalfailedsessions.is_set or self.csubaggstatstotalfailedsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatstotalfailedsessions.get_name_leafdata())
                if (self.csubaggstatstotalflowsup.is_set or self.csubaggstatstotalflowsup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatstotalflowsup.get_name_leafdata())
                if (self.csubaggstatstotallightweightsessions.is_set or self.csubaggstatstotallightweightsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatstotallightweightsessions.get_name_leafdata())
                if (self.csubaggstatstotalupsessions.is_set or self.csubaggstatstotalupsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatstotalupsessions.get_name_leafdata())
                if (self.csubaggstatsunauthsessions.is_set or self.csubaggstatsunauthsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsunauthsessions.get_name_leafdata())
                if (self.csubaggstatsupsessions.is_set or self.csubaggstatsupsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsupsessions.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csubAggStatsPointType" or name == "csubAggStatsPoint" or name == "csubAggStatsSessionType" or name == "csubAggStatsAuthSessions" or name == "csubAggStatsAvgSessionRPH" or name == "csubAggStatsAvgSessionRPM" or name == "csubAggStatsAvgSessionUptime" or name == "csubAggStatsCurrAuthSessions" or name == "csubAggStatsCurrCreatedSessions" or name == "csubAggStatsCurrDiscSessions" or name == "csubAggStatsCurrFailedSessions" or name == "csubAggStatsCurrFlowsUp" or name == "csubAggStatsCurrInvalidIntervals" or name == "csubAggStatsCurrTimeElapsed" or name == "csubAggStatsCurrUpSessions" or name == "csubAggStatsCurrValidIntervals" or name == "csubAggStatsDayAuthSessions" or name == "csubAggStatsDayCreatedSessions" or name == "csubAggStatsDayDiscSessions" or name == "csubAggStatsDayFailedSessions" or name == "csubAggStatsDayUpSessions" or name == "csubAggStatsDiscontinuityTime" or name == "csubAggStatsHighUpSessions" or name == "csubAggStatsLightWeightSessions" or name == "csubAggStatsPendingSessions" or name == "csubAggStatsRedSessions" or name == "csubAggStatsThrottleEngagements" or name == "csubAggStatsTotalAuthSessions" or name == "csubAggStatsTotalCreatedSessions" or name == "csubAggStatsTotalDiscSessions" or name == "csubAggStatsTotalFailedSessions" or name == "csubAggStatsTotalFlowsUp" or name == "csubAggStatsTotalLightWeightSessions" or name == "csubAggStatsTotalUpSessions" or name == "csubAggStatsUnAuthSessions" or name == "csubAggStatsUpSessions"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "csubAggStatsPointType"):
                    self.csubaggstatspointtype = value
                    self.csubaggstatspointtype.value_namespace = name_space
                    self.csubaggstatspointtype.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsPoint"):
                    self.csubaggstatspoint = value
                    self.csubaggstatspoint.value_namespace = name_space
                    self.csubaggstatspoint.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsSessionType"):
                    self.csubaggstatssessiontype = value
                    self.csubaggstatssessiontype.value_namespace = name_space
                    self.csubaggstatssessiontype.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsAuthSessions"):
                    self.csubaggstatsauthsessions = value
                    self.csubaggstatsauthsessions.value_namespace = name_space
                    self.csubaggstatsauthsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsAvgSessionRPH"):
                    self.csubaggstatsavgsessionrph = value
                    self.csubaggstatsavgsessionrph.value_namespace = name_space
                    self.csubaggstatsavgsessionrph.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsAvgSessionRPM"):
                    self.csubaggstatsavgsessionrpm = value
                    self.csubaggstatsavgsessionrpm.value_namespace = name_space
                    self.csubaggstatsavgsessionrpm.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsAvgSessionUptime"):
                    self.csubaggstatsavgsessionuptime = value
                    self.csubaggstatsavgsessionuptime.value_namespace = name_space
                    self.csubaggstatsavgsessionuptime.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsCurrAuthSessions"):
                    self.csubaggstatscurrauthsessions = value
                    self.csubaggstatscurrauthsessions.value_namespace = name_space
                    self.csubaggstatscurrauthsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsCurrCreatedSessions"):
                    self.csubaggstatscurrcreatedsessions = value
                    self.csubaggstatscurrcreatedsessions.value_namespace = name_space
                    self.csubaggstatscurrcreatedsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsCurrDiscSessions"):
                    self.csubaggstatscurrdiscsessions = value
                    self.csubaggstatscurrdiscsessions.value_namespace = name_space
                    self.csubaggstatscurrdiscsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsCurrFailedSessions"):
                    self.csubaggstatscurrfailedsessions = value
                    self.csubaggstatscurrfailedsessions.value_namespace = name_space
                    self.csubaggstatscurrfailedsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsCurrFlowsUp"):
                    self.csubaggstatscurrflowsup = value
                    self.csubaggstatscurrflowsup.value_namespace = name_space
                    self.csubaggstatscurrflowsup.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsCurrInvalidIntervals"):
                    self.csubaggstatscurrinvalidintervals = value
                    self.csubaggstatscurrinvalidintervals.value_namespace = name_space
                    self.csubaggstatscurrinvalidintervals.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsCurrTimeElapsed"):
                    self.csubaggstatscurrtimeelapsed = value
                    self.csubaggstatscurrtimeelapsed.value_namespace = name_space
                    self.csubaggstatscurrtimeelapsed.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsCurrUpSessions"):
                    self.csubaggstatscurrupsessions = value
                    self.csubaggstatscurrupsessions.value_namespace = name_space
                    self.csubaggstatscurrupsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsCurrValidIntervals"):
                    self.csubaggstatscurrvalidintervals = value
                    self.csubaggstatscurrvalidintervals.value_namespace = name_space
                    self.csubaggstatscurrvalidintervals.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsDayAuthSessions"):
                    self.csubaggstatsdayauthsessions = value
                    self.csubaggstatsdayauthsessions.value_namespace = name_space
                    self.csubaggstatsdayauthsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsDayCreatedSessions"):
                    self.csubaggstatsdaycreatedsessions = value
                    self.csubaggstatsdaycreatedsessions.value_namespace = name_space
                    self.csubaggstatsdaycreatedsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsDayDiscSessions"):
                    self.csubaggstatsdaydiscsessions = value
                    self.csubaggstatsdaydiscsessions.value_namespace = name_space
                    self.csubaggstatsdaydiscsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsDayFailedSessions"):
                    self.csubaggstatsdayfailedsessions = value
                    self.csubaggstatsdayfailedsessions.value_namespace = name_space
                    self.csubaggstatsdayfailedsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsDayUpSessions"):
                    self.csubaggstatsdayupsessions = value
                    self.csubaggstatsdayupsessions.value_namespace = name_space
                    self.csubaggstatsdayupsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsDiscontinuityTime"):
                    self.csubaggstatsdiscontinuitytime = value
                    self.csubaggstatsdiscontinuitytime.value_namespace = name_space
                    self.csubaggstatsdiscontinuitytime.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsHighUpSessions"):
                    self.csubaggstatshighupsessions = value
                    self.csubaggstatshighupsessions.value_namespace = name_space
                    self.csubaggstatshighupsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsLightWeightSessions"):
                    self.csubaggstatslightweightsessions = value
                    self.csubaggstatslightweightsessions.value_namespace = name_space
                    self.csubaggstatslightweightsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsPendingSessions"):
                    self.csubaggstatspendingsessions = value
                    self.csubaggstatspendingsessions.value_namespace = name_space
                    self.csubaggstatspendingsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsRedSessions"):
                    self.csubaggstatsredsessions = value
                    self.csubaggstatsredsessions.value_namespace = name_space
                    self.csubaggstatsredsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsThrottleEngagements"):
                    self.csubaggstatsthrottleengagements = value
                    self.csubaggstatsthrottleengagements.value_namespace = name_space
                    self.csubaggstatsthrottleengagements.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsTotalAuthSessions"):
                    self.csubaggstatstotalauthsessions = value
                    self.csubaggstatstotalauthsessions.value_namespace = name_space
                    self.csubaggstatstotalauthsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsTotalCreatedSessions"):
                    self.csubaggstatstotalcreatedsessions = value
                    self.csubaggstatstotalcreatedsessions.value_namespace = name_space
                    self.csubaggstatstotalcreatedsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsTotalDiscSessions"):
                    self.csubaggstatstotaldiscsessions = value
                    self.csubaggstatstotaldiscsessions.value_namespace = name_space
                    self.csubaggstatstotaldiscsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsTotalFailedSessions"):
                    self.csubaggstatstotalfailedsessions = value
                    self.csubaggstatstotalfailedsessions.value_namespace = name_space
                    self.csubaggstatstotalfailedsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsTotalFlowsUp"):
                    self.csubaggstatstotalflowsup = value
                    self.csubaggstatstotalflowsup.value_namespace = name_space
                    self.csubaggstatstotalflowsup.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsTotalLightWeightSessions"):
                    self.csubaggstatstotallightweightsessions = value
                    self.csubaggstatstotallightweightsessions.value_namespace = name_space
                    self.csubaggstatstotallightweightsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsTotalUpSessions"):
                    self.csubaggstatstotalupsessions = value
                    self.csubaggstatstotalupsessions.value_namespace = name_space
                    self.csubaggstatstotalupsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsUnAuthSessions"):
                    self.csubaggstatsunauthsessions = value
                    self.csubaggstatsunauthsessions.value_namespace = name_space
                    self.csubaggstatsunauthsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsUpSessions"):
                    self.csubaggstatsupsessions = value
                    self.csubaggstatsupsessions.value_namespace = name_space
                    self.csubaggstatsupsessions.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csubaggstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csubaggstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csubAggStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csubAggStatsEntry"):
                for c in self.csubaggstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSubscriberSessionMib.Csubaggstatstable.Csubaggstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csubaggstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csubAggStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csubaggstatsinttable(Entity):
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
        	**type**\: list of    :py:class:`Csubaggstatsintentry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubaggstatsinttable.Csubaggstatsintentry>`
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CiscoSubscriberSessionMib.Csubaggstatsinttable, self).__init__()

            self.yang_name = "csubAggStatsIntTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"

            self.csubaggstatsintentry = YList(self)

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
                        super(CiscoSubscriberSessionMib.Csubaggstatsinttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSubscriberSessionMib.Csubaggstatsinttable, self).__setattr__(name, value)


        class Csubaggstatsintentry(Entity):
            """
            An entry contains the aggregated subscriber session performance
            data collected over a single 15\-minute measurement interval
            within a 'scope of aggregation'.  For further details regarding
            'scope of aggregation', see the descriptive text associated with
            the csubAggStatsEntry.
            
            .. attribute:: csubaggstatspointtype  <key>
            
            	
            	**type**\:   :py:class:`Csubaggstatspointtype <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubaggstatstable.Csubaggstatsentry.Csubaggstatspointtype>`
            
            .. attribute:: csubaggstatspoint  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`csubaggstatspoint <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubaggstatstable.Csubaggstatsentry>`
            
            .. attribute:: csubaggstatssessiontype  <key>
            
            	
            	**type**\:   :py:class:`Subsessiontype <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB.Subsessiontype>`
            
            .. attribute:: csubaggstatsintnumber  <key>
            
            	This object indicates the interval number identifying the 15\-minute measurement interval for which aggregated subscriber session performance data was successfully collected by the system.  The interval identified by the value '1' represents the most recent 15\-minute measurement interval, and the interval identified by the value (n) represents the interval immediately preceding the interval identified by the value (n\-1)
            	**type**\:  int
            
            	**range:** 1..96
            
            .. attribute:: csubaggstatsintauthsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that transitioned from the UNAUTHENTICATED to the AUTHENTICATED state during the 15\-minute measurement interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsintcreatedsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' created during the 15\-minute measurement interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsintdiscsessions
            
            	This object indicates the total number of subscriber sessions terminated due to a disconnect event during the 15\-minute measurement interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsintfailedsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that were in the PENDING state and terminated for reasons other than disconnect during the 15\-minute measurement interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsintupsessions
            
            	This object indicates the total number of subscriber sessions within the 'scope of aggregation' that transitioned to the UP state during the 15\-minute measurement interval
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: sessions
            
            .. attribute:: csubaggstatsintvalid
            
            	This object indicates whether the data for the 15\-minute measurement interval is valid
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CiscoSubscriberSessionMib.Csubaggstatsinttable.Csubaggstatsintentry, self).__init__()

                self.yang_name = "csubAggStatsIntEntry"
                self.yang_parent_name = "csubAggStatsIntTable"

                self.csubaggstatspointtype = YLeaf(YType.enumeration, "csubAggStatsPointType")

                self.csubaggstatspoint = YLeaf(YType.str, "csubAggStatsPoint")

                self.csubaggstatssessiontype = YLeaf(YType.enumeration, "csubAggStatsSessionType")

                self.csubaggstatsintnumber = YLeaf(YType.uint32, "csubAggStatsIntNumber")

                self.csubaggstatsintauthsessions = YLeaf(YType.uint32, "csubAggStatsIntAuthSessions")

                self.csubaggstatsintcreatedsessions = YLeaf(YType.uint32, "csubAggStatsIntCreatedSessions")

                self.csubaggstatsintdiscsessions = YLeaf(YType.uint32, "csubAggStatsIntDiscSessions")

                self.csubaggstatsintfailedsessions = YLeaf(YType.uint32, "csubAggStatsIntFailedSessions")

                self.csubaggstatsintupsessions = YLeaf(YType.uint32, "csubAggStatsIntUpSessions")

                self.csubaggstatsintvalid = YLeaf(YType.boolean, "csubAggStatsIntValid")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csubaggstatspointtype",
                                "csubaggstatspoint",
                                "csubaggstatssessiontype",
                                "csubaggstatsintnumber",
                                "csubaggstatsintauthsessions",
                                "csubaggstatsintcreatedsessions",
                                "csubaggstatsintdiscsessions",
                                "csubaggstatsintfailedsessions",
                                "csubaggstatsintupsessions",
                                "csubaggstatsintvalid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSubscriberSessionMib.Csubaggstatsinttable.Csubaggstatsintentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSubscriberSessionMib.Csubaggstatsinttable.Csubaggstatsintentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csubaggstatspointtype.is_set or
                    self.csubaggstatspoint.is_set or
                    self.csubaggstatssessiontype.is_set or
                    self.csubaggstatsintnumber.is_set or
                    self.csubaggstatsintauthsessions.is_set or
                    self.csubaggstatsintcreatedsessions.is_set or
                    self.csubaggstatsintdiscsessions.is_set or
                    self.csubaggstatsintfailedsessions.is_set or
                    self.csubaggstatsintupsessions.is_set or
                    self.csubaggstatsintvalid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csubaggstatspointtype.yfilter != YFilter.not_set or
                    self.csubaggstatspoint.yfilter != YFilter.not_set or
                    self.csubaggstatssessiontype.yfilter != YFilter.not_set or
                    self.csubaggstatsintnumber.yfilter != YFilter.not_set or
                    self.csubaggstatsintauthsessions.yfilter != YFilter.not_set or
                    self.csubaggstatsintcreatedsessions.yfilter != YFilter.not_set or
                    self.csubaggstatsintdiscsessions.yfilter != YFilter.not_set or
                    self.csubaggstatsintfailedsessions.yfilter != YFilter.not_set or
                    self.csubaggstatsintupsessions.yfilter != YFilter.not_set or
                    self.csubaggstatsintvalid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csubAggStatsIntEntry" + "[csubAggStatsPointType='" + self.csubaggstatspointtype.get() + "']" + "[csubAggStatsPoint='" + self.csubaggstatspoint.get() + "']" + "[csubAggStatsSessionType='" + self.csubaggstatssessiontype.get() + "']" + "[csubAggStatsIntNumber='" + self.csubaggstatsintnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubAggStatsIntTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csubaggstatspointtype.is_set or self.csubaggstatspointtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatspointtype.get_name_leafdata())
                if (self.csubaggstatspoint.is_set or self.csubaggstatspoint.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatspoint.get_name_leafdata())
                if (self.csubaggstatssessiontype.is_set or self.csubaggstatssessiontype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatssessiontype.get_name_leafdata())
                if (self.csubaggstatsintnumber.is_set or self.csubaggstatsintnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsintnumber.get_name_leafdata())
                if (self.csubaggstatsintauthsessions.is_set or self.csubaggstatsintauthsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsintauthsessions.get_name_leafdata())
                if (self.csubaggstatsintcreatedsessions.is_set or self.csubaggstatsintcreatedsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsintcreatedsessions.get_name_leafdata())
                if (self.csubaggstatsintdiscsessions.is_set or self.csubaggstatsintdiscsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsintdiscsessions.get_name_leafdata())
                if (self.csubaggstatsintfailedsessions.is_set or self.csubaggstatsintfailedsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsintfailedsessions.get_name_leafdata())
                if (self.csubaggstatsintupsessions.is_set or self.csubaggstatsintupsessions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsintupsessions.get_name_leafdata())
                if (self.csubaggstatsintvalid.is_set or self.csubaggstatsintvalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubaggstatsintvalid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csubAggStatsPointType" or name == "csubAggStatsPoint" or name == "csubAggStatsSessionType" or name == "csubAggStatsIntNumber" or name == "csubAggStatsIntAuthSessions" or name == "csubAggStatsIntCreatedSessions" or name == "csubAggStatsIntDiscSessions" or name == "csubAggStatsIntFailedSessions" or name == "csubAggStatsIntUpSessions" or name == "csubAggStatsIntValid"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "csubAggStatsPointType"):
                    self.csubaggstatspointtype = value
                    self.csubaggstatspointtype.value_namespace = name_space
                    self.csubaggstatspointtype.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsPoint"):
                    self.csubaggstatspoint = value
                    self.csubaggstatspoint.value_namespace = name_space
                    self.csubaggstatspoint.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsSessionType"):
                    self.csubaggstatssessiontype = value
                    self.csubaggstatssessiontype.value_namespace = name_space
                    self.csubaggstatssessiontype.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsIntNumber"):
                    self.csubaggstatsintnumber = value
                    self.csubaggstatsintnumber.value_namespace = name_space
                    self.csubaggstatsintnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsIntAuthSessions"):
                    self.csubaggstatsintauthsessions = value
                    self.csubaggstatsintauthsessions.value_namespace = name_space
                    self.csubaggstatsintauthsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsIntCreatedSessions"):
                    self.csubaggstatsintcreatedsessions = value
                    self.csubaggstatsintcreatedsessions.value_namespace = name_space
                    self.csubaggstatsintcreatedsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsIntDiscSessions"):
                    self.csubaggstatsintdiscsessions = value
                    self.csubaggstatsintdiscsessions.value_namespace = name_space
                    self.csubaggstatsintdiscsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsIntFailedSessions"):
                    self.csubaggstatsintfailedsessions = value
                    self.csubaggstatsintfailedsessions.value_namespace = name_space
                    self.csubaggstatsintfailedsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsIntUpSessions"):
                    self.csubaggstatsintupsessions = value
                    self.csubaggstatsintupsessions.value_namespace = name_space
                    self.csubaggstatsintupsessions.value_namespace_prefix = name_space_prefix
                if(value_path == "csubAggStatsIntValid"):
                    self.csubaggstatsintvalid = value
                    self.csubaggstatsintvalid.value_namespace = name_space
                    self.csubaggstatsintvalid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csubaggstatsintentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csubaggstatsintentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csubAggStatsIntTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csubAggStatsIntEntry"):
                for c in self.csubaggstatsintentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSubscriberSessionMib.Csubaggstatsinttable.Csubaggstatsintentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csubaggstatsintentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csubAggStatsIntEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csubaggstatsthreshtable(Entity):
        """
        Please enter the Table Description here.
        
        .. attribute:: csubaggstatsthreshentry
        
        	A row in this table exists for each row in the csubAggStatsTable. Each row defines the set of thresholds and evaluation attributes for an aggregation point
        	**type**\: list of    :py:class:`Csubaggstatsthreshentry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubaggstatsthreshtable.Csubaggstatsthreshentry>`
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CiscoSubscriberSessionMib.Csubaggstatsthreshtable, self).__init__()

            self.yang_name = "csubAggStatsThreshTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"

            self.csubaggstatsthreshentry = YList(self)

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
                        super(CiscoSubscriberSessionMib.Csubaggstatsthreshtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSubscriberSessionMib.Csubaggstatsthreshtable, self).__setattr__(name, value)


        class Csubaggstatsthreshentry(Entity):
            """
            A row in this table exists for each row in the
            csubAggStatsTable.
            Each row defines the set of thresholds and evaluation attributes
            for an aggregation point.
            
            .. attribute:: csubsessionrisingthresh  <key>
            
            	This threshold, if non\-zero, indicates the rising threshold for the value of csubAggStatsUpSessions for the aggregation point, When the current sample of csubAggStatsUpSessions is greater than or equal to this threshold, and the value of csubAggStatsUpSessions for the last sample interval was less than this thershold, the csubSessionRisingNotif is triggered.           If the value of this threshold is 0, the threshold is not evaluated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csubsessiondeltapercentfallingthresh
            
            	This threshold, if non\-zero, indicates the delta falling threshold as a percentage of the value of csubAggStatsUpSessions for the aggregation point, The delta as a percentage of csubAggStatsUpSessions (delta\_percent) is calculated as follows\:       current value of csubAggStatsUpSessions = value(n)              previous sampled value of csubAggStatsUpSessions = value(n\-1)               delta\_percent = ((value(n\-1) \- value(n)) / value(n\-1)) \* 100           If the delta\_percent value of the current evaluation interval is          greater than the value of this threshold, a          csubSessionDeltaPercentLossNotif is triggered.           If the value of this threshold is 0, the threshold is not evaluated
            	**type**\:  int
            
            	**range:** 0..100
            
            .. attribute:: csubsessionfallingthresh
            
            	This threshold, if non\-zero, indicates the falling threshold for the value of csubAggStatsUpSessions for the aggregation point, When the current sample of csubAggStatsUpSessions is less than or equal to this threshold, and the value of csubAggStatsUpSessions for the last sample interval was greater than this thershold, the csubSessionFallingNotif is triggered.           If the value of this threshold is 0, the threshold is not evaluated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csubsessionthreshevalinterval
            
            	The value of this object sets the number of seconds between samples for threshold evaluation. For implementations capable of per\-session event evaluation of thresholds this object represents the maximum number of seconds between samples
            	**type**\:  int
            
            	**range:** 0..900
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CiscoSubscriberSessionMib.Csubaggstatsthreshtable.Csubaggstatsthreshentry, self).__init__()

                self.yang_name = "csubAggStatsThreshEntry"
                self.yang_parent_name = "csubAggStatsThreshTable"

                self.csubsessionrisingthresh = YLeaf(YType.uint32, "csubSessionRisingThresh")

                self.csubsessiondeltapercentfallingthresh = YLeaf(YType.uint32, "csubSessionDeltaPercentFallingThresh")

                self.csubsessionfallingthresh = YLeaf(YType.uint32, "csubSessionFallingThresh")

                self.csubsessionthreshevalinterval = YLeaf(YType.uint32, "csubSessionThreshEvalInterval")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csubsessionrisingthresh",
                                "csubsessiondeltapercentfallingthresh",
                                "csubsessionfallingthresh",
                                "csubsessionthreshevalinterval") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSubscriberSessionMib.Csubaggstatsthreshtable.Csubaggstatsthreshentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSubscriberSessionMib.Csubaggstatsthreshtable.Csubaggstatsthreshentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csubsessionrisingthresh.is_set or
                    self.csubsessiondeltapercentfallingthresh.is_set or
                    self.csubsessionfallingthresh.is_set or
                    self.csubsessionthreshevalinterval.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csubsessionrisingthresh.yfilter != YFilter.not_set or
                    self.csubsessiondeltapercentfallingthresh.yfilter != YFilter.not_set or
                    self.csubsessionfallingthresh.yfilter != YFilter.not_set or
                    self.csubsessionthreshevalinterval.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csubAggStatsThreshEntry" + "[csubSessionRisingThresh='" + self.csubsessionrisingthresh.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubAggStatsThreshTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csubsessionrisingthresh.is_set or self.csubsessionrisingthresh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionrisingthresh.get_name_leafdata())
                if (self.csubsessiondeltapercentfallingthresh.is_set or self.csubsessiondeltapercentfallingthresh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessiondeltapercentfallingthresh.get_name_leafdata())
                if (self.csubsessionfallingthresh.is_set or self.csubsessionfallingthresh.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionfallingthresh.get_name_leafdata())
                if (self.csubsessionthreshevalinterval.is_set or self.csubsessionthreshevalinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubsessionthreshevalinterval.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csubSessionRisingThresh" or name == "csubSessionDeltaPercentFallingThresh" or name == "csubSessionFallingThresh" or name == "csubSessionThreshEvalInterval"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "csubSessionRisingThresh"):
                    self.csubsessionrisingthresh = value
                    self.csubsessionrisingthresh.value_namespace = name_space
                    self.csubsessionrisingthresh.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionDeltaPercentFallingThresh"):
                    self.csubsessiondeltapercentfallingthresh = value
                    self.csubsessiondeltapercentfallingthresh.value_namespace = name_space
                    self.csubsessiondeltapercentfallingthresh.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionFallingThresh"):
                    self.csubsessionfallingthresh = value
                    self.csubsessionfallingthresh.value_namespace = name_space
                    self.csubsessionfallingthresh.value_namespace_prefix = name_space_prefix
                if(value_path == "csubSessionThreshEvalInterval"):
                    self.csubsessionthreshevalinterval = value
                    self.csubsessionthreshevalinterval.value_namespace = name_space
                    self.csubsessionthreshevalinterval.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csubaggstatsthreshentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csubaggstatsthreshentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csubAggStatsThreshTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csubAggStatsThreshEntry"):
                for c in self.csubaggstatsthreshentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSubscriberSessionMib.Csubaggstatsthreshtable.Csubaggstatsthreshentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csubaggstatsthreshentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csubAggStatsThreshEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csubjobtable(Entity):
        """
        This table contains the subscriber session jobs submitted by
        the EMS/NMS.
        
        .. attribute:: csubjobentry
        
        	An entry describing a subscriber session job.  At this time, subscriber session jobs can perform one of two tasks\:  \- Subscriber Session Query     This type of job invokes the report generator, which builds     a list of subscriber sessions matching criteria specified by     the corresponding row in the csubJobMatchParamsTable.  The     list built by the report generator must conform to     parameters specified by the corresponding row in     csubJobQueryParamsTable, which at this time only affects     sorting order.  \- Subscriber Session Clear     This type of job causes the system to terminate those     subscriber sessions matching criteria specified by the     corresponding row in the csubJobMatchParamsTable.  The following procedure summarizes how the EMS/NMS can start and monitor a subscriber session job\:  1)  The EMS/NMS must start by reading csubJobIdNext.  If it is     zero, continue polling csubJobIdNext until it is non\-zero.  2)  The EMS/NMS creates a row in the csubJobTable using the     instance identifier retrieved in the last step.  Since every     object contained by the entry with a MAX\-ACCESS of      'read\-create' specifies a default value, it makes little     difference whether the EMS/NMS employs create\-and\-wait or     create\-and\-go semantics.  3)  The EMS/NMS sets the type of subscriber session job by     setting the corresponding instance of csubJobType.  4a) If the job is a 'query', then the EMS/NMS must configure     the query before starting it by setting columns contained     by the corresponding rows in the csubJobMatchParamsTable and     csubJobQueryParamsTable.  4b) If job is a 'clear', then the EMS/NMS must configure     the job before starting it by setting columns contained by     the corresponding row in the csubJobMatchParamsTable.  5)  The EMS/NMS can now start the job by setting the      corresponding instance of csubJobControl to 'start'.  6)  The EMS/NMS can monitor the progress of the job by polling     the corresponding instance of csubJobState.  It can also     wait for a csubJobFinishedNotify notification.  When the     state of the job transitions to 'finished', then the system     has finished executing the job.  7)  The EMS/NMS can determine the final status of the job by     reading the corresponding instance of csubJobFinishedReason.     If job is a 'query' and the corresponding instance of     csubJobFinishedReason is 'normal', then the EMS/NMS can     safely read the report by retrieving the corresponding     rows from the csubJobReportTable.  8a) After a job has finished, the EMS/NMS has the option of     destroying it.  It can do this by simply setting the     corresponding instance of  csubJobStatus to 'destroy'.     Alternatively, the EMS/NMS may retain the job and execute it     again in the future (by returning to step 5).  Additionally,     nothing would prevent the EMS/NMS from changing the job's     type, which causes the automatic destruction of the     corresponding report.  8b) If the job is a 'query' and the EMS/NMS opts to retain the     job, then it may consider releasing the corresponding report     after reading it.  It can do this by setting the     corresponding instance of csubJobControl to 'release'
        	**type**\: list of    :py:class:`Csubjobentry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry>`
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CiscoSubscriberSessionMib.Csubjobtable, self).__init__()

            self.yang_name = "csubJobTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"

            self.csubjobentry = YList(self)

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
                        super(CiscoSubscriberSessionMib.Csubjobtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSubscriberSessionMib.Csubjobtable, self).__setattr__(name, value)


        class Csubjobentry(Entity):
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
            
            .. attribute:: csubjobid  <key>
            
            	This object indicates an arbitrary, positive integer\-value uniquely identifying the subscriber session job
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: csubjobcontrol
            
            	This object specifies an action relating to the subscriber session job\:      'noop'         This action does nothing.      'start'         If the corresponding instance of csubJobType is 'noop',         then this action simply causes the system to set the         corresponding instances of csubJobState and         csubJobFinishedReason to 'finished' and 'normal',         respectively.          If the corresponding instance of csubJobType is not         'noop' and the system is not executing a subscriber         session job, then this action causes the system         immediately execute the subscriber session job.          If the corresponding instance of csubJobType is not         'noop' and the system is already executing a subscriber         session job, then this action causes the system to put         the job on the subscriber session job queue.      'abort'         If the subscriber session job is in the subscriber         session job queue, then this action causes the system to         remove the job from the queue.          If the system is executing the subscriber session job,         then this action causes the system to stop the job.      'release'         This action causes the system to destroy any         corresponding rows in the csubJobReportTable.          The system only accepts this action for a previously         executed subscriber session job having a corresponding         instance of csubJobType set to 'query'.  Any attempt to         issue this action under other circumstances will result         in a response indicating an  error\-status of         'inconsistentValue'.  When read, this column is always 'noop'
            	**type**\:   :py:class:`Csubjobcontrol <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry.Csubjobcontrol>`
            
            .. attribute:: csubjobfinishedreason
            
            	This object indicates the reason why the system finished executing the subscriber session job\:      'invalid'         Indicates that the corresponding instance of         csubJobState is either 'idle', 'pending', or         'inProgress'.      'other'         Indicates that the system finished executing the         subscriber session job abnormally for a reason not         recognized by this MIB module.      'normal'         Indicates that the system finished executing the         subscriber session job with no problems.      'aborted'         Indicates that the system finished executing the         subscriber session job as the result of the EMS/NMS         writing 'abort' to the corresponding instance of         csubJobControl.      'insufficientResources'         Indicates that the system finished executing the         subscriber session job abnormally due to insufficient         resources to continue.      'error'         Indicates that the system encountered an error that         prevented it from completing the job
            	**type**\:   :py:class:`Csubjobfinishedreason <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry.Csubjobfinishedreason>`
            
            .. attribute:: csubjobfinishedtime
            
            	This object indicates the value of sysUpTime when the system finished executing the subscriber session job, for whatever reason.  This value will be '0' when the corresponding instance of csubJobState is 'idle', 'pending', or 'inProgress'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csubjobstartedtime
            
            	This object indicates the value of sysUpTime when the system started executing the subscriber session job.  This value will be '0' when the corresponding instance of csubJobState is 'idle' or 'pending'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csubjobstate
            
            	This object indicates the current state of the subscriber session job\:      'idle'         This state indicates that the system has not executed         the subscriber session job since it was created.      'pending'         This state indicates that the subscriber session job is         waiting in the subscriber session job queue.      'inProgress'         This state indicates that the system is executing the         subscriber session job.  Observe that the system may         execute more than one subscriber session job at a time.      'finished'         This state indicates that the system has executed the         subscriber session job and it has finished.  The         corresponding instance of csubJobFinishedReason         indicates further details regarding the reason why the         job finished
            	**type**\:   :py:class:`Csubjobstate <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry.Csubjobstate>`
            
            .. attribute:: csubjobstatus
            
            	This object specifies the status of the subscriber session job.  The following columns must be valid before activating a subscriber session job\:      \- csubJobStorage     \- csubJobType     \- csubJobControl  However, these objects specify a default value.  Thus, it is possible to use create\-and\-go semantics without setting any additional columns.  An implementation must allow the EMS/NMS to modify any column when this column is 'active', including columns defined in tables that have a one\-to\-one or sparse dependent relationship on this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: csubjobstorage
            
            	This object specifies what happens to the subscriber session job upon restart
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: csubjobtype
            
            	This object specifies the type of subscriber session job\:  'noop'     This type of job does nothing and simply serves as a     convenient default value for newly created jobs, thereby     allowing create\-and\-go row creation without having to     specify the type of job.  'query'     This type of job starts a subscriber session query.  The     system searches for any subscriber sessions matching the     configured criteria and sorts them into a resulting     report.      Upon activation of a subscriber session with this value,     the system automatically creates corresponding rows in     the csubJobMatchParamsTable and csubQueryParamsTable.  'clear'     This type of job causes the system to terminated all     subscriber sessions matching configured criteria.      Upon activation of a subscriber session with this value,     the system automatically creates a corresponding row in     the csubJobMatchParamsTable
            	**type**\:   :py:class:`Csubjobtype <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry.Csubjobtype>`
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry, self).__init__()

                self.yang_name = "csubJobEntry"
                self.yang_parent_name = "csubJobTable"

                self.csubjobid = YLeaf(YType.uint32, "csubJobId")

                self.csubjobcontrol = YLeaf(YType.enumeration, "csubJobControl")

                self.csubjobfinishedreason = YLeaf(YType.enumeration, "csubJobFinishedReason")

                self.csubjobfinishedtime = YLeaf(YType.uint32, "csubJobFinishedTime")

                self.csubjobstartedtime = YLeaf(YType.uint32, "csubJobStartedTime")

                self.csubjobstate = YLeaf(YType.enumeration, "csubJobState")

                self.csubjobstatus = YLeaf(YType.enumeration, "csubJobStatus")

                self.csubjobstorage = YLeaf(YType.enumeration, "csubJobStorage")

                self.csubjobtype = YLeaf(YType.enumeration, "csubJobType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csubjobid",
                                "csubjobcontrol",
                                "csubjobfinishedreason",
                                "csubjobfinishedtime",
                                "csubjobstartedtime",
                                "csubjobstate",
                                "csubjobstatus",
                                "csubjobstorage",
                                "csubjobtype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry, self).__setattr__(name, value)

            class Csubjobcontrol(Enum):
                """
                Csubjobcontrol

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


            class Csubjobfinishedreason(Enum):
                """
                Csubjobfinishedreason

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


            class Csubjobstate(Enum):
                """
                Csubjobstate

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


            class Csubjobtype(Enum):
                """
                Csubjobtype

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


            def has_data(self):
                return (
                    self.csubjobid.is_set or
                    self.csubjobcontrol.is_set or
                    self.csubjobfinishedreason.is_set or
                    self.csubjobfinishedtime.is_set or
                    self.csubjobstartedtime.is_set or
                    self.csubjobstate.is_set or
                    self.csubjobstatus.is_set or
                    self.csubjobstorage.is_set or
                    self.csubjobtype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csubjobid.yfilter != YFilter.not_set or
                    self.csubjobcontrol.yfilter != YFilter.not_set or
                    self.csubjobfinishedreason.yfilter != YFilter.not_set or
                    self.csubjobfinishedtime.yfilter != YFilter.not_set or
                    self.csubjobstartedtime.yfilter != YFilter.not_set or
                    self.csubjobstate.yfilter != YFilter.not_set or
                    self.csubjobstatus.yfilter != YFilter.not_set or
                    self.csubjobstorage.yfilter != YFilter.not_set or
                    self.csubjobtype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csubJobEntry" + "[csubJobId='" + self.csubjobid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubJobTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csubjobid.is_set or self.csubjobid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobid.get_name_leafdata())
                if (self.csubjobcontrol.is_set or self.csubjobcontrol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobcontrol.get_name_leafdata())
                if (self.csubjobfinishedreason.is_set or self.csubjobfinishedreason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobfinishedreason.get_name_leafdata())
                if (self.csubjobfinishedtime.is_set or self.csubjobfinishedtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobfinishedtime.get_name_leafdata())
                if (self.csubjobstartedtime.is_set or self.csubjobstartedtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobstartedtime.get_name_leafdata())
                if (self.csubjobstate.is_set or self.csubjobstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobstate.get_name_leafdata())
                if (self.csubjobstatus.is_set or self.csubjobstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobstatus.get_name_leafdata())
                if (self.csubjobstorage.is_set or self.csubjobstorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobstorage.get_name_leafdata())
                if (self.csubjobtype.is_set or self.csubjobtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobtype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csubJobId" or name == "csubJobControl" or name == "csubJobFinishedReason" or name == "csubJobFinishedTime" or name == "csubJobStartedTime" or name == "csubJobState" or name == "csubJobStatus" or name == "csubJobStorage" or name == "csubJobType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "csubJobId"):
                    self.csubjobid = value
                    self.csubjobid.value_namespace = name_space
                    self.csubjobid.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobControl"):
                    self.csubjobcontrol = value
                    self.csubjobcontrol.value_namespace = name_space
                    self.csubjobcontrol.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobFinishedReason"):
                    self.csubjobfinishedreason = value
                    self.csubjobfinishedreason.value_namespace = name_space
                    self.csubjobfinishedreason.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobFinishedTime"):
                    self.csubjobfinishedtime = value
                    self.csubjobfinishedtime.value_namespace = name_space
                    self.csubjobfinishedtime.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobStartedTime"):
                    self.csubjobstartedtime = value
                    self.csubjobstartedtime.value_namespace = name_space
                    self.csubjobstartedtime.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobState"):
                    self.csubjobstate = value
                    self.csubjobstate.value_namespace = name_space
                    self.csubjobstate.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobStatus"):
                    self.csubjobstatus = value
                    self.csubjobstatus.value_namespace = name_space
                    self.csubjobstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobStorage"):
                    self.csubjobstorage = value
                    self.csubjobstorage.value_namespace = name_space
                    self.csubjobstorage.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobType"):
                    self.csubjobtype = value
                    self.csubjobtype.value_namespace = name_space
                    self.csubjobtype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csubjobentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csubjobentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csubJobTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csubJobEntry"):
                for c in self.csubjobentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csubjobentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csubJobEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csubjobmatchparamstable(Entity):
        """
        This table contains subscriber session job parameters
        describing match criteria.
        
        This table has a sparse\-dependent relationship on the
        csubJobTable, containing a row for each job having a
        csubJobType of 'query' or 'clear'.
        
        .. attribute:: csubjobmatchparamsentry
        
        	An entry describes a set of subscriber session match criteria. The set contains those subscriber session identities specified by csubJobMatchIdentities.  If the corresponding row in the csubJobTable has a csubJobType of 'query', then the system builds a report containing those subscriber sessions matching these criteria.  If the corresponding row in the csubJobTable has a csubJobType of 'clear', then the system terminates those subscriber sessions matching these criteria.  The system automatically creates an entry when the EMS/NMS sets the corresponding instance of csubJobType to 'query' or 'clear'. Likewise, the system automatically destroys an entry under the following circumstances\:  1)  The EMS/NMS destroys the corresponding row in the     csubJobTable.  2)  The EMS/NMS sets the corresponding instance of csubJobType     to 'noop'
        	**type**\: list of    :py:class:`Csubjobmatchparamsentry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjobmatchparamstable.Csubjobmatchparamsentry>`
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CiscoSubscriberSessionMib.Csubjobmatchparamstable, self).__init__()

            self.yang_name = "csubJobMatchParamsTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"

            self.csubjobmatchparamsentry = YList(self)

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
                        super(CiscoSubscriberSessionMib.Csubjobmatchparamstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSubscriberSessionMib.Csubjobmatchparamstable, self).__setattr__(name, value)


        class Csubjobmatchparamsentry(Entity):
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
            
            .. attribute:: csubjobid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`csubjobid <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry>`
            
            .. attribute:: csubjobmatchacctsessionid
            
            	This object specifies the accounting session identifier the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'accountingSid' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csubjobmatchauthenticated
            
            	This object specifies whether a subscriber session should be unauthenticated for the system to consider a match in the process of executing a subscriber session job.  If this column is 'false', then the subscriber session job matches subscriber sessions that are unauthenticated.  If this column is 'true', then the subscriber session job matches subscriber session that are authenticated.  This value is valid only if the 'authenticated' bit of the corresponding instance of csubJobMatchParams is '1'
            	**type**\:  bool
            
            .. attribute:: csubjobmatchcircuitid
            
            	This object specifies the Circuit\-Id the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'circuitId' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubjobmatchdanglingduration
            
            	This object specifies the minimum interval of time a subscriber session can remain dangling in order for the system to consider it a match in the process of executing a subscriber session job. A 'dangling' subscriber session is one in the PENDING state.  The value '0' cannot be written to an instance of this object. However, it serves as a convenient value when the column is not valid.  This value is valid only if the 'danglingDuration' bit of the corresponding instance of csubJobMatchOtherParams is '1'
            	**type**\:  int
            
            	**range:** 0..3600
            
            .. attribute:: csubjobmatchdhcpclass
            
            	This object specifies the DHCP class name the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'dhcpClass' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubjobmatchdnis
            
            	This object specifies the DNIS number the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'dnis' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubjobmatchdomain
            
            	This object specifies the domain the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'domain' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubjobmatchdomainipaddr
            
            	This object specifies the domain IP address that the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'domainIpAddress' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: csubjobmatchdomainipaddrtype
            
            	This object specifies the type of Internet address specified by csubJobMatchDomainIpAddr and csubJobMatchDomainIpMask.  This value is valid only if the 'domainIpAddress' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: csubjobmatchdomainipmask
            
            	This object specifies the mask used when matching the domain IP address against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'domainIpAddress' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: csubjobmatchdomainvrf
            
            	This object specifies the domain VRF the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'domainVrf' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubjobmatchidentities
            
            	This object specifies the subscriber identities that the system uses to determine the subscriber sessions the job executes on.  Each bit in this bit string corresponds to one or more columns in this table.  If the bit is '0', then the value of the corresponding columns are invalid.  If the bit is '1', then the value of corresponding columns are valid.  The following list specifies the mappings between the bits and the columns\:      'subscriberLabel' => csubJobMatchSubscriberLabel     'macAddress'      => csubJobMatchMacAddress     'nativeVrf'       => csubJobMatchNativeVrf     'nativeIpAddress' => csubJobMatchNativeIpAddrType,                          csubJobMatchNativeIpAddr,                          csubJobMatchNativeIpMask,     'domainVrf'       => csubJobMatchDomainVrf     'domainIpAddress' => csubJobMatchDomainIpAddrType,                          csubJobMatchDomainIpAddr,                          csubJobMatchDomainIpMask     'pbhk'            => csubJobMatchPbhk     'remoteId'        => csubJobMatchRemoteId     'circuitId'       => csubJobMatchCircuitId     'nasPort'         => csubJobMatchNasPort     'domain'          => csubJobMatchDomain     'username'        => csubJobMatchUsername     'acctSessionId'   => csubJobMatchAcctSessionId     'dnis'            => csubJobMatchDnis     'media'           => csubJobMatchMedia     'mlpNegotiated'   => csubJobMatchMlpNegotiated     'protocol'        => csubJobMatchProtocol     'serviceName'     => csubJobMatchServiceName     'dhcpClass'       => csubJobMatchDhcpClass     'tunnelName'      => csubJobMatchTunnelName  Observe that the bit 'ifIndex' has no meaning, as subscriber session jobs do not match against this subscriber session identity
            	**type**\:   :py:class:`Subsessionidentities <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.Subsessionidentities>`
            
            .. attribute:: csubjobmatchmacaddress
            
            	This object specifies the MAC address that the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'macAddress' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: csubjobmatchmedia
            
            	This object specifies the media type the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'media' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:   :py:class:`Subscribermediatype <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.Subscribermediatype>`
            
            .. attribute:: csubjobmatchmlpnegotiated
            
            	This object specifies the MLP negotiated flag the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'mlpNegotiated' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  bool
            
            .. attribute:: csubjobmatchnasport
            
            	This object specifies the NAS port\-identifier the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'nasPort' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubjobmatchnativeipaddr
            
            	This object specifies the native IP address that the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'nativeIpAddress' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: csubjobmatchnativeipaddrtype
            
            	This object specifies the type of Internet address specified by csubJobMatchNativeIpAddr and csubJobMatchNativeIpMask.  This value is valid only if the 'nativeIpAddress' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: csubjobmatchnativeipmask
            
            	This object specifies the mask used when matching the native IP address against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'nativeIpAddress' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: csubjobmatchnativevrf
            
            	This object specifies the native VRF the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'nativeVrf' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubjobmatchotherparams
            
            	This object specifies other parameters relating to subscriber sessions a subscriber session job may match against.  Each bit in this bit string corresponds to a column in this table.  If the bit is '0', then the value of the corresponding column is invalid.  If the bit is '1', then the value of the corresponding column represents the value of the parameter identity the system should match against for the corresponding subscriber session job.  The following list specifies the mappings between bits and the columns\:      'danglingDuration' => csubJobMatchDanglingDuration     'state'            => csubJobMatchState     'authenticated'    => csubJobMatchAuthenticated     'redundancyMode'   => csubJobMatchRedundancyMode
            	**type**\:   :py:class:`Csubjobmatchotherparams <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjobmatchparamstable.Csubjobmatchparamsentry.Csubjobmatchotherparams>`
            
            .. attribute:: csubjobmatchpbhk
            
            	This object specifies the PBHK that the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'pbhk' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubjobmatchprotocol
            
            	This object specifies the protocol type the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'protocol' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:   :py:class:`Subscriberprotocoltype <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.Subscriberprotocoltype>`
            
            .. attribute:: csubjobmatchredundancymode
            
            	This object specifies the redudancy mode of the subscriber session in order for the system to consider a match in the process of executing a subscriber session job.  The value 'other' is not valid and an implementation should not allow it to be written to this column.  This value is valid only if the 'redundancyMode' bit of the corresponding instance of csubJobMatchOtherParams is '1'
            	**type**\:   :py:class:`Subsessionredundancymode <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB.Subsessionredundancymode>`
            
            .. attribute:: csubjobmatchremoteid
            
            	This object specifies the Remote\-Id the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'remoteId' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubjobmatchservicename
            
            	This object specifies the service name the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'serviceName' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubjobmatchstate
            
            	This object specifies the state of a subscriber session in order for the system to consider a match in the process of executing a subscriber session job.  The value 'other' is not valid and an implementation should not allow it to be written to this column.  This value is valid only if the 'state' bit of the corresponding instance of csubJobMatchOtherParams is '1'
            	**type**\:   :py:class:`Subsessionstate <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_TC_MIB.Subsessionstate>`
            
            .. attribute:: csubjobmatchsubscriberlabel
            
            	This object specifies the subscriber label that the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'subscriberLabel' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csubjobmatchtunnelname
            
            	This object specifies the tunnel name the system matches against subscriber session in the process of executing a subscriber session job.  This value is valid only if the 'tunnelName' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  str
            
            .. attribute:: csubjobmatchusername
            
            	This object specifies the username the system matches against subscriber sessions in the process of executing a subscriber session job.  This value is valid only if the 'username' bit of the corresponding instance of csubJobMatchIdentities is '1'
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CiscoSubscriberSessionMib.Csubjobmatchparamstable.Csubjobmatchparamsentry, self).__init__()

                self.yang_name = "csubJobMatchParamsEntry"
                self.yang_parent_name = "csubJobMatchParamsTable"

                self.csubjobid = YLeaf(YType.str, "csubJobId")

                self.csubjobmatchacctsessionid = YLeaf(YType.uint32, "csubJobMatchAcctSessionId")

                self.csubjobmatchauthenticated = YLeaf(YType.boolean, "csubJobMatchAuthenticated")

                self.csubjobmatchcircuitid = YLeaf(YType.str, "csubJobMatchCircuitId")

                self.csubjobmatchdanglingduration = YLeaf(YType.uint32, "csubJobMatchDanglingDuration")

                self.csubjobmatchdhcpclass = YLeaf(YType.str, "csubJobMatchDhcpClass")

                self.csubjobmatchdnis = YLeaf(YType.str, "csubJobMatchDnis")

                self.csubjobmatchdomain = YLeaf(YType.str, "csubJobMatchDomain")

                self.csubjobmatchdomainipaddr = YLeaf(YType.str, "csubJobMatchDomainIpAddr")

                self.csubjobmatchdomainipaddrtype = YLeaf(YType.enumeration, "csubJobMatchDomainIpAddrType")

                self.csubjobmatchdomainipmask = YLeaf(YType.str, "csubJobMatchDomainIpMask")

                self.csubjobmatchdomainvrf = YLeaf(YType.str, "csubJobMatchDomainVrf")

                self.csubjobmatchidentities = YLeaf(YType.bits, "csubJobMatchIdentities")

                self.csubjobmatchmacaddress = YLeaf(YType.str, "csubJobMatchMacAddress")

                self.csubjobmatchmedia = YLeaf(YType.enumeration, "csubJobMatchMedia")

                self.csubjobmatchmlpnegotiated = YLeaf(YType.boolean, "csubJobMatchMlpNegotiated")

                self.csubjobmatchnasport = YLeaf(YType.str, "csubJobMatchNasPort")

                self.csubjobmatchnativeipaddr = YLeaf(YType.str, "csubJobMatchNativeIpAddr")

                self.csubjobmatchnativeipaddrtype = YLeaf(YType.enumeration, "csubJobMatchNativeIpAddrType")

                self.csubjobmatchnativeipmask = YLeaf(YType.str, "csubJobMatchNativeIpMask")

                self.csubjobmatchnativevrf = YLeaf(YType.str, "csubJobMatchNativeVrf")

                self.csubjobmatchotherparams = YLeaf(YType.bits, "csubJobMatchOtherParams")

                self.csubjobmatchpbhk = YLeaf(YType.str, "csubJobMatchPbhk")

                self.csubjobmatchprotocol = YLeaf(YType.enumeration, "csubJobMatchProtocol")

                self.csubjobmatchredundancymode = YLeaf(YType.enumeration, "csubJobMatchRedundancyMode")

                self.csubjobmatchremoteid = YLeaf(YType.str, "csubJobMatchRemoteId")

                self.csubjobmatchservicename = YLeaf(YType.str, "csubJobMatchServiceName")

                self.csubjobmatchstate = YLeaf(YType.enumeration, "csubJobMatchState")

                self.csubjobmatchsubscriberlabel = YLeaf(YType.uint32, "csubJobMatchSubscriberLabel")

                self.csubjobmatchtunnelname = YLeaf(YType.str, "csubJobMatchTunnelName")

                self.csubjobmatchusername = YLeaf(YType.str, "csubJobMatchUsername")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csubjobid",
                                "csubjobmatchacctsessionid",
                                "csubjobmatchauthenticated",
                                "csubjobmatchcircuitid",
                                "csubjobmatchdanglingduration",
                                "csubjobmatchdhcpclass",
                                "csubjobmatchdnis",
                                "csubjobmatchdomain",
                                "csubjobmatchdomainipaddr",
                                "csubjobmatchdomainipaddrtype",
                                "csubjobmatchdomainipmask",
                                "csubjobmatchdomainvrf",
                                "csubjobmatchidentities",
                                "csubjobmatchmacaddress",
                                "csubjobmatchmedia",
                                "csubjobmatchmlpnegotiated",
                                "csubjobmatchnasport",
                                "csubjobmatchnativeipaddr",
                                "csubjobmatchnativeipaddrtype",
                                "csubjobmatchnativeipmask",
                                "csubjobmatchnativevrf",
                                "csubjobmatchotherparams",
                                "csubjobmatchpbhk",
                                "csubjobmatchprotocol",
                                "csubjobmatchredundancymode",
                                "csubjobmatchremoteid",
                                "csubjobmatchservicename",
                                "csubjobmatchstate",
                                "csubjobmatchsubscriberlabel",
                                "csubjobmatchtunnelname",
                                "csubjobmatchusername") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSubscriberSessionMib.Csubjobmatchparamstable.Csubjobmatchparamsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSubscriberSessionMib.Csubjobmatchparamstable.Csubjobmatchparamsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csubjobid.is_set or
                    self.csubjobmatchacctsessionid.is_set or
                    self.csubjobmatchauthenticated.is_set or
                    self.csubjobmatchcircuitid.is_set or
                    self.csubjobmatchdanglingduration.is_set or
                    self.csubjobmatchdhcpclass.is_set or
                    self.csubjobmatchdnis.is_set or
                    self.csubjobmatchdomain.is_set or
                    self.csubjobmatchdomainipaddr.is_set or
                    self.csubjobmatchdomainipaddrtype.is_set or
                    self.csubjobmatchdomainipmask.is_set or
                    self.csubjobmatchdomainvrf.is_set or
                    self.csubjobmatchidentities.is_set or
                    self.csubjobmatchmacaddress.is_set or
                    self.csubjobmatchmedia.is_set or
                    self.csubjobmatchmlpnegotiated.is_set or
                    self.csubjobmatchnasport.is_set or
                    self.csubjobmatchnativeipaddr.is_set or
                    self.csubjobmatchnativeipaddrtype.is_set or
                    self.csubjobmatchnativeipmask.is_set or
                    self.csubjobmatchnativevrf.is_set or
                    self.csubjobmatchotherparams.is_set or
                    self.csubjobmatchpbhk.is_set or
                    self.csubjobmatchprotocol.is_set or
                    self.csubjobmatchredundancymode.is_set or
                    self.csubjobmatchremoteid.is_set or
                    self.csubjobmatchservicename.is_set or
                    self.csubjobmatchstate.is_set or
                    self.csubjobmatchsubscriberlabel.is_set or
                    self.csubjobmatchtunnelname.is_set or
                    self.csubjobmatchusername.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csubjobid.yfilter != YFilter.not_set or
                    self.csubjobmatchacctsessionid.yfilter != YFilter.not_set or
                    self.csubjobmatchauthenticated.yfilter != YFilter.not_set or
                    self.csubjobmatchcircuitid.yfilter != YFilter.not_set or
                    self.csubjobmatchdanglingduration.yfilter != YFilter.not_set or
                    self.csubjobmatchdhcpclass.yfilter != YFilter.not_set or
                    self.csubjobmatchdnis.yfilter != YFilter.not_set or
                    self.csubjobmatchdomain.yfilter != YFilter.not_set or
                    self.csubjobmatchdomainipaddr.yfilter != YFilter.not_set or
                    self.csubjobmatchdomainipaddrtype.yfilter != YFilter.not_set or
                    self.csubjobmatchdomainipmask.yfilter != YFilter.not_set or
                    self.csubjobmatchdomainvrf.yfilter != YFilter.not_set or
                    self.csubjobmatchidentities.yfilter != YFilter.not_set or
                    self.csubjobmatchmacaddress.yfilter != YFilter.not_set or
                    self.csubjobmatchmedia.yfilter != YFilter.not_set or
                    self.csubjobmatchmlpnegotiated.yfilter != YFilter.not_set or
                    self.csubjobmatchnasport.yfilter != YFilter.not_set or
                    self.csubjobmatchnativeipaddr.yfilter != YFilter.not_set or
                    self.csubjobmatchnativeipaddrtype.yfilter != YFilter.not_set or
                    self.csubjobmatchnativeipmask.yfilter != YFilter.not_set or
                    self.csubjobmatchnativevrf.yfilter != YFilter.not_set or
                    self.csubjobmatchotherparams.yfilter != YFilter.not_set or
                    self.csubjobmatchpbhk.yfilter != YFilter.not_set or
                    self.csubjobmatchprotocol.yfilter != YFilter.not_set or
                    self.csubjobmatchredundancymode.yfilter != YFilter.not_set or
                    self.csubjobmatchremoteid.yfilter != YFilter.not_set or
                    self.csubjobmatchservicename.yfilter != YFilter.not_set or
                    self.csubjobmatchstate.yfilter != YFilter.not_set or
                    self.csubjobmatchsubscriberlabel.yfilter != YFilter.not_set or
                    self.csubjobmatchtunnelname.yfilter != YFilter.not_set or
                    self.csubjobmatchusername.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csubJobMatchParamsEntry" + "[csubJobId='" + self.csubjobid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubJobMatchParamsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csubjobid.is_set or self.csubjobid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobid.get_name_leafdata())
                if (self.csubjobmatchacctsessionid.is_set or self.csubjobmatchacctsessionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchacctsessionid.get_name_leafdata())
                if (self.csubjobmatchauthenticated.is_set or self.csubjobmatchauthenticated.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchauthenticated.get_name_leafdata())
                if (self.csubjobmatchcircuitid.is_set or self.csubjobmatchcircuitid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchcircuitid.get_name_leafdata())
                if (self.csubjobmatchdanglingduration.is_set or self.csubjobmatchdanglingduration.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchdanglingduration.get_name_leafdata())
                if (self.csubjobmatchdhcpclass.is_set or self.csubjobmatchdhcpclass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchdhcpclass.get_name_leafdata())
                if (self.csubjobmatchdnis.is_set or self.csubjobmatchdnis.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchdnis.get_name_leafdata())
                if (self.csubjobmatchdomain.is_set or self.csubjobmatchdomain.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchdomain.get_name_leafdata())
                if (self.csubjobmatchdomainipaddr.is_set or self.csubjobmatchdomainipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchdomainipaddr.get_name_leafdata())
                if (self.csubjobmatchdomainipaddrtype.is_set or self.csubjobmatchdomainipaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchdomainipaddrtype.get_name_leafdata())
                if (self.csubjobmatchdomainipmask.is_set or self.csubjobmatchdomainipmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchdomainipmask.get_name_leafdata())
                if (self.csubjobmatchdomainvrf.is_set or self.csubjobmatchdomainvrf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchdomainvrf.get_name_leafdata())
                if (self.csubjobmatchidentities.is_set or self.csubjobmatchidentities.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchidentities.get_name_leafdata())
                if (self.csubjobmatchmacaddress.is_set or self.csubjobmatchmacaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchmacaddress.get_name_leafdata())
                if (self.csubjobmatchmedia.is_set or self.csubjobmatchmedia.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchmedia.get_name_leafdata())
                if (self.csubjobmatchmlpnegotiated.is_set or self.csubjobmatchmlpnegotiated.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchmlpnegotiated.get_name_leafdata())
                if (self.csubjobmatchnasport.is_set or self.csubjobmatchnasport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchnasport.get_name_leafdata())
                if (self.csubjobmatchnativeipaddr.is_set or self.csubjobmatchnativeipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchnativeipaddr.get_name_leafdata())
                if (self.csubjobmatchnativeipaddrtype.is_set or self.csubjobmatchnativeipaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchnativeipaddrtype.get_name_leafdata())
                if (self.csubjobmatchnativeipmask.is_set or self.csubjobmatchnativeipmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchnativeipmask.get_name_leafdata())
                if (self.csubjobmatchnativevrf.is_set or self.csubjobmatchnativevrf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchnativevrf.get_name_leafdata())
                if (self.csubjobmatchotherparams.is_set or self.csubjobmatchotherparams.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchotherparams.get_name_leafdata())
                if (self.csubjobmatchpbhk.is_set or self.csubjobmatchpbhk.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchpbhk.get_name_leafdata())
                if (self.csubjobmatchprotocol.is_set or self.csubjobmatchprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchprotocol.get_name_leafdata())
                if (self.csubjobmatchredundancymode.is_set or self.csubjobmatchredundancymode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchredundancymode.get_name_leafdata())
                if (self.csubjobmatchremoteid.is_set or self.csubjobmatchremoteid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchremoteid.get_name_leafdata())
                if (self.csubjobmatchservicename.is_set or self.csubjobmatchservicename.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchservicename.get_name_leafdata())
                if (self.csubjobmatchstate.is_set or self.csubjobmatchstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchstate.get_name_leafdata())
                if (self.csubjobmatchsubscriberlabel.is_set or self.csubjobmatchsubscriberlabel.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchsubscriberlabel.get_name_leafdata())
                if (self.csubjobmatchtunnelname.is_set or self.csubjobmatchtunnelname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchtunnelname.get_name_leafdata())
                if (self.csubjobmatchusername.is_set or self.csubjobmatchusername.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobmatchusername.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csubJobId" or name == "csubJobMatchAcctSessionId" or name == "csubJobMatchAuthenticated" or name == "csubJobMatchCircuitId" or name == "csubJobMatchDanglingDuration" or name == "csubJobMatchDhcpClass" or name == "csubJobMatchDnis" or name == "csubJobMatchDomain" or name == "csubJobMatchDomainIpAddr" or name == "csubJobMatchDomainIpAddrType" or name == "csubJobMatchDomainIpMask" or name == "csubJobMatchDomainVrf" or name == "csubJobMatchIdentities" or name == "csubJobMatchMacAddress" or name == "csubJobMatchMedia" or name == "csubJobMatchMlpNegotiated" or name == "csubJobMatchNasPort" or name == "csubJobMatchNativeIpAddr" or name == "csubJobMatchNativeIpAddrType" or name == "csubJobMatchNativeIpMask" or name == "csubJobMatchNativeVrf" or name == "csubJobMatchOtherParams" or name == "csubJobMatchPbhk" or name == "csubJobMatchProtocol" or name == "csubJobMatchRedundancyMode" or name == "csubJobMatchRemoteId" or name == "csubJobMatchServiceName" or name == "csubJobMatchState" or name == "csubJobMatchSubscriberLabel" or name == "csubJobMatchTunnelName" or name == "csubJobMatchUsername"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "csubJobId"):
                    self.csubjobid = value
                    self.csubjobid.value_namespace = name_space
                    self.csubjobid.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchAcctSessionId"):
                    self.csubjobmatchacctsessionid = value
                    self.csubjobmatchacctsessionid.value_namespace = name_space
                    self.csubjobmatchacctsessionid.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchAuthenticated"):
                    self.csubjobmatchauthenticated = value
                    self.csubjobmatchauthenticated.value_namespace = name_space
                    self.csubjobmatchauthenticated.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchCircuitId"):
                    self.csubjobmatchcircuitid = value
                    self.csubjobmatchcircuitid.value_namespace = name_space
                    self.csubjobmatchcircuitid.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchDanglingDuration"):
                    self.csubjobmatchdanglingduration = value
                    self.csubjobmatchdanglingduration.value_namespace = name_space
                    self.csubjobmatchdanglingduration.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchDhcpClass"):
                    self.csubjobmatchdhcpclass = value
                    self.csubjobmatchdhcpclass.value_namespace = name_space
                    self.csubjobmatchdhcpclass.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchDnis"):
                    self.csubjobmatchdnis = value
                    self.csubjobmatchdnis.value_namespace = name_space
                    self.csubjobmatchdnis.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchDomain"):
                    self.csubjobmatchdomain = value
                    self.csubjobmatchdomain.value_namespace = name_space
                    self.csubjobmatchdomain.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchDomainIpAddr"):
                    self.csubjobmatchdomainipaddr = value
                    self.csubjobmatchdomainipaddr.value_namespace = name_space
                    self.csubjobmatchdomainipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchDomainIpAddrType"):
                    self.csubjobmatchdomainipaddrtype = value
                    self.csubjobmatchdomainipaddrtype.value_namespace = name_space
                    self.csubjobmatchdomainipaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchDomainIpMask"):
                    self.csubjobmatchdomainipmask = value
                    self.csubjobmatchdomainipmask.value_namespace = name_space
                    self.csubjobmatchdomainipmask.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchDomainVrf"):
                    self.csubjobmatchdomainvrf = value
                    self.csubjobmatchdomainvrf.value_namespace = name_space
                    self.csubjobmatchdomainvrf.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchIdentities"):
                    self.csubjobmatchidentities[value] = True
                if(value_path == "csubJobMatchMacAddress"):
                    self.csubjobmatchmacaddress = value
                    self.csubjobmatchmacaddress.value_namespace = name_space
                    self.csubjobmatchmacaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchMedia"):
                    self.csubjobmatchmedia = value
                    self.csubjobmatchmedia.value_namespace = name_space
                    self.csubjobmatchmedia.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchMlpNegotiated"):
                    self.csubjobmatchmlpnegotiated = value
                    self.csubjobmatchmlpnegotiated.value_namespace = name_space
                    self.csubjobmatchmlpnegotiated.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchNasPort"):
                    self.csubjobmatchnasport = value
                    self.csubjobmatchnasport.value_namespace = name_space
                    self.csubjobmatchnasport.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchNativeIpAddr"):
                    self.csubjobmatchnativeipaddr = value
                    self.csubjobmatchnativeipaddr.value_namespace = name_space
                    self.csubjobmatchnativeipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchNativeIpAddrType"):
                    self.csubjobmatchnativeipaddrtype = value
                    self.csubjobmatchnativeipaddrtype.value_namespace = name_space
                    self.csubjobmatchnativeipaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchNativeIpMask"):
                    self.csubjobmatchnativeipmask = value
                    self.csubjobmatchnativeipmask.value_namespace = name_space
                    self.csubjobmatchnativeipmask.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchNativeVrf"):
                    self.csubjobmatchnativevrf = value
                    self.csubjobmatchnativevrf.value_namespace = name_space
                    self.csubjobmatchnativevrf.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchOtherParams"):
                    self.csubjobmatchotherparams[value] = True
                if(value_path == "csubJobMatchPbhk"):
                    self.csubjobmatchpbhk = value
                    self.csubjobmatchpbhk.value_namespace = name_space
                    self.csubjobmatchpbhk.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchProtocol"):
                    self.csubjobmatchprotocol = value
                    self.csubjobmatchprotocol.value_namespace = name_space
                    self.csubjobmatchprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchRedundancyMode"):
                    self.csubjobmatchredundancymode = value
                    self.csubjobmatchredundancymode.value_namespace = name_space
                    self.csubjobmatchredundancymode.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchRemoteId"):
                    self.csubjobmatchremoteid = value
                    self.csubjobmatchremoteid.value_namespace = name_space
                    self.csubjobmatchremoteid.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchServiceName"):
                    self.csubjobmatchservicename = value
                    self.csubjobmatchservicename.value_namespace = name_space
                    self.csubjobmatchservicename.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchState"):
                    self.csubjobmatchstate = value
                    self.csubjobmatchstate.value_namespace = name_space
                    self.csubjobmatchstate.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchSubscriberLabel"):
                    self.csubjobmatchsubscriberlabel = value
                    self.csubjobmatchsubscriberlabel.value_namespace = name_space
                    self.csubjobmatchsubscriberlabel.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchTunnelName"):
                    self.csubjobmatchtunnelname = value
                    self.csubjobmatchtunnelname.value_namespace = name_space
                    self.csubjobmatchtunnelname.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobMatchUsername"):
                    self.csubjobmatchusername = value
                    self.csubjobmatchusername.value_namespace = name_space
                    self.csubjobmatchusername.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csubjobmatchparamsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csubjobmatchparamsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csubJobMatchParamsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csubJobMatchParamsEntry"):
                for c in self.csubjobmatchparamsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSubscriberSessionMib.Csubjobmatchparamstable.Csubjobmatchparamsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csubjobmatchparamsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csubJobMatchParamsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csubjobqueryparamstable(Entity):
        """
        This table contains subscriber session job parameters
        describing query parameters.
        
        This table has a sparse\-dependent relationship on the
        csubJobTable, containing a row for each job having a
        csubJobType of 'query'.
        
        .. attribute:: csubjobqueryparamsentry
        
        	An entry describes a set of subscriber session query parameters.  The system automatically creates an entry when the EMS/NMS sets the corresponding instance of csubJobType to 'query'.  Likewise, the system automatically destroys an entry under the following circumstances\:  1)  The EMS/NMS destroys the corresponding row in the csubJobTable.  2)  The EMS/NMS sets the corresponding instance of csubJobType to     'noop' or 'clear'
        	**type**\: list of    :py:class:`Csubjobqueryparamsentry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjobqueryparamstable.Csubjobqueryparamsentry>`
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CiscoSubscriberSessionMib.Csubjobqueryparamstable, self).__init__()

            self.yang_name = "csubJobQueryParamsTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"

            self.csubjobqueryparamsentry = YList(self)

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
                        super(CiscoSubscriberSessionMib.Csubjobqueryparamstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSubscriberSessionMib.Csubjobqueryparamstable, self).__setattr__(name, value)


        class Csubjobqueryparamsentry(Entity):
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
            
            .. attribute:: csubjobid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`csubjobid <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry>`
            
            .. attribute:: csubjobqueryresultingreportsize
            
            	This object indicates the number of subscriber sessions that matched the corresponding subscriber session query.  The value of this column should be '0' unless the corresponding value of csubJobState is 'finished'.  The value of this column should be '0' after the EMS/NMS sets the corresponding csubJobControl to 'release'
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: csubjobquerysortkey1
            
            	This object specifies the first subscriber identity that the system uses when sorting subscriber sessions into the final report corresponding to a subscriber session query.  It is not valid to set this column to 'other' or 'ifIndex'
            	**type**\:   :py:class:`Subsessionidentity <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.Subsessionidentity>`
            
            .. attribute:: csubjobquerysortkey2
            
            	This object specifies the second subscriber identity that the system uses when sorting subscriber sessions into the final report corresponding to a subscriber session query.  If it is the desire to have the final report sorted on a single subscriber identity, then this column should be 'other'
            	**type**\:   :py:class:`Subsessionidentity <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.Subsessionidentity>`
            
            .. attribute:: csubjobquerysortkey3
            
            	This object specifies the third subscriber identity that the system uses when sorting subscriber sessions into the final report corresponding to a subscriber session query.  If it is the desire to have the final report sorted on one or two subscriber identities, then this column should be 'other'
            	**type**\:   :py:class:`Subsessionidentity <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_IDENTITY_TC_MIB.Subsessionidentity>`
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CiscoSubscriberSessionMib.Csubjobqueryparamstable.Csubjobqueryparamsentry, self).__init__()

                self.yang_name = "csubJobQueryParamsEntry"
                self.yang_parent_name = "csubJobQueryParamsTable"

                self.csubjobid = YLeaf(YType.str, "csubJobId")

                self.csubjobqueryresultingreportsize = YLeaf(YType.uint32, "csubJobQueryResultingReportSize")

                self.csubjobquerysortkey1 = YLeaf(YType.enumeration, "csubJobQuerySortKey1")

                self.csubjobquerysortkey2 = YLeaf(YType.enumeration, "csubJobQuerySortKey2")

                self.csubjobquerysortkey3 = YLeaf(YType.enumeration, "csubJobQuerySortKey3")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csubjobid",
                                "csubjobqueryresultingreportsize",
                                "csubjobquerysortkey1",
                                "csubjobquerysortkey2",
                                "csubjobquerysortkey3") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSubscriberSessionMib.Csubjobqueryparamstable.Csubjobqueryparamsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSubscriberSessionMib.Csubjobqueryparamstable.Csubjobqueryparamsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csubjobid.is_set or
                    self.csubjobqueryresultingreportsize.is_set or
                    self.csubjobquerysortkey1.is_set or
                    self.csubjobquerysortkey2.is_set or
                    self.csubjobquerysortkey3.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csubjobid.yfilter != YFilter.not_set or
                    self.csubjobqueryresultingreportsize.yfilter != YFilter.not_set or
                    self.csubjobquerysortkey1.yfilter != YFilter.not_set or
                    self.csubjobquerysortkey2.yfilter != YFilter.not_set or
                    self.csubjobquerysortkey3.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csubJobQueryParamsEntry" + "[csubJobId='" + self.csubjobid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubJobQueryParamsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csubjobid.is_set or self.csubjobid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobid.get_name_leafdata())
                if (self.csubjobqueryresultingreportsize.is_set or self.csubjobqueryresultingreportsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobqueryresultingreportsize.get_name_leafdata())
                if (self.csubjobquerysortkey1.is_set or self.csubjobquerysortkey1.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobquerysortkey1.get_name_leafdata())
                if (self.csubjobquerysortkey2.is_set or self.csubjobquerysortkey2.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobquerysortkey2.get_name_leafdata())
                if (self.csubjobquerysortkey3.is_set or self.csubjobquerysortkey3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobquerysortkey3.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csubJobId" or name == "csubJobQueryResultingReportSize" or name == "csubJobQuerySortKey1" or name == "csubJobQuerySortKey2" or name == "csubJobQuerySortKey3"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "csubJobId"):
                    self.csubjobid = value
                    self.csubjobid.value_namespace = name_space
                    self.csubjobid.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobQueryResultingReportSize"):
                    self.csubjobqueryresultingreportsize = value
                    self.csubjobqueryresultingreportsize.value_namespace = name_space
                    self.csubjobqueryresultingreportsize.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobQuerySortKey1"):
                    self.csubjobquerysortkey1 = value
                    self.csubjobquerysortkey1.value_namespace = name_space
                    self.csubjobquerysortkey1.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobQuerySortKey2"):
                    self.csubjobquerysortkey2 = value
                    self.csubjobquerysortkey2.value_namespace = name_space
                    self.csubjobquerysortkey2.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobQuerySortKey3"):
                    self.csubjobquerysortkey3 = value
                    self.csubjobquerysortkey3.value_namespace = name_space
                    self.csubjobquerysortkey3.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csubjobqueryparamsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csubjobqueryparamsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csubJobQueryParamsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csubJobQueryParamsEntry"):
                for c in self.csubjobqueryparamsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSubscriberSessionMib.Csubjobqueryparamstable.Csubjobqueryparamsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csubjobqueryparamsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csubJobQueryParamsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csubjobqueuetable(Entity):
        """
        This table lists the subscriber session jobs currently pending
        in the subscriber session job queue.
        
        .. attribute:: csubjobqueueentry
        
        	An entry describing an subscriber session job in the subscriber session job queue.  The system creates an entry in this table when it places a subscriber session job on the subscriber session job queue.  It does this when the EMS/NMS sets an instance of csubJobControl to 'start' and the system is already executing a subscriber session job.  Likewise, the system destroys an entry when it removes it from the queue.  This occurs under the following circumstances\:  1)  The system has finished executing a job, for whatever     reason, and is ready to start executing the job at the head     of the queue.  2)  The EMS/NMS has set an instance of csubJobControl to 'abort'     for a job that was on the queue
        	**type**\: list of    :py:class:`Csubjobqueueentry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjobqueuetable.Csubjobqueueentry>`
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CiscoSubscriberSessionMib.Csubjobqueuetable, self).__init__()

            self.yang_name = "csubJobQueueTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"

            self.csubjobqueueentry = YList(self)

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
                        super(CiscoSubscriberSessionMib.Csubjobqueuetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSubscriberSessionMib.Csubjobqueuetable, self).__setattr__(name, value)


        class Csubjobqueueentry(Entity):
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
            
            .. attribute:: csubjobqueuenumber  <key>
            
            	This object indicates an positive, integer\-value that uniquely identifies the entry in the table. The value of this object starts at '1' and monotonically increases for each subscriber session job inserted into the subscriber session job queue.  If the value of this object is '4294967295', the system will reset it to '1' when it inserts the next subscriber session job into the subscriber session job queue
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: csubjobqueuejobid
            
            	This object indicates the identifier associated with the subscriber session job
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CiscoSubscriberSessionMib.Csubjobqueuetable.Csubjobqueueentry, self).__init__()

                self.yang_name = "csubJobQueueEntry"
                self.yang_parent_name = "csubJobQueueTable"

                self.csubjobqueuenumber = YLeaf(YType.uint32, "csubJobQueueNumber")

                self.csubjobqueuejobid = YLeaf(YType.uint32, "csubJobQueueJobId")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csubjobqueuenumber",
                                "csubjobqueuejobid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSubscriberSessionMib.Csubjobqueuetable.Csubjobqueueentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSubscriberSessionMib.Csubjobqueuetable.Csubjobqueueentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csubjobqueuenumber.is_set or
                    self.csubjobqueuejobid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csubjobqueuenumber.yfilter != YFilter.not_set or
                    self.csubjobqueuejobid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csubJobQueueEntry" + "[csubJobQueueNumber='" + self.csubjobqueuenumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubJobQueueTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csubjobqueuenumber.is_set or self.csubjobqueuenumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobqueuenumber.get_name_leafdata())
                if (self.csubjobqueuejobid.is_set or self.csubjobqueuejobid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobqueuejobid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csubJobQueueNumber" or name == "csubJobQueueJobId"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "csubJobQueueNumber"):
                    self.csubjobqueuenumber = value
                    self.csubjobqueuenumber.value_namespace = name_space
                    self.csubjobqueuenumber.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobQueueJobId"):
                    self.csubjobqueuejobid = value
                    self.csubjobqueuejobid.value_namespace = name_space
                    self.csubjobqueuejobid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csubjobqueueentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csubjobqueueentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csubJobQueueTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csubJobQueueEntry"):
                for c in self.csubjobqueueentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSubscriberSessionMib.Csubjobqueuetable.Csubjobqueueentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csubjobqueueentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csubJobQueueEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Csubjobreporttable(Entity):
        """
        This table contains the reports corresponding to subscriber
        session jobs that have a csubJobType of 'query' and
        csubJobState of 'finished'.
        
        This table has an expansion dependent relationship on the
        csubJobTable, containing zero or more rows for each job.
        
        .. attribute:: csubjobreportentry
        
        	An entry describes a subscriber session that satisfied the match criteria specified by the corresponding job.  The system creates an entry for each subscriber session that satisfied the specified match criteria of a subscriber session job having a csubJobType of 'query'.  However, it does not create these entries until after the system has successfully executed the subscriber session job.  The system destroys an entry under the following circumstances\:  1)  The corresponding subscriber session job has been destroyed     by the EMS/NMS.  2)  The value of csubJobMaxLife is non\-zero and the age of the     report has reached the specified maximum life.  3)  The EMS/NMS has set the corresponding instance of     csubJobControl to 'release'.  4)  The EMS/NMS has restarted the corresponding subscriber     session job (i.e., has set the corresponding instance of     csubJobControl to 'start')
        	**type**\: list of    :py:class:`Csubjobreportentry <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjobreporttable.Csubjobreportentry>`
        
        

        """

        _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
        _revision = '2012-08-08'

        def __init__(self):
            super(CiscoSubscriberSessionMib.Csubjobreporttable, self).__init__()

            self.yang_name = "csubJobReportTable"
            self.yang_parent_name = "CISCO-SUBSCRIBER-SESSION-MIB"

            self.csubjobreportentry = YList(self)

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
                        super(CiscoSubscriberSessionMib.Csubjobreporttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoSubscriberSessionMib.Csubjobreporttable, self).__setattr__(name, value)


        class Csubjobreportentry(Entity):
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
            
            .. attribute:: csubjobid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`csubjobid <ydk.models.cisco_ios_xe.CISCO_SUBSCRIBER_SESSION_MIB.CiscoSubscriberSessionMib.Csubjobtable.Csubjobentry>`
            
            .. attribute:: csubjobreportid  <key>
            
            	This object indicates an arbitrary, positive, integer\-value that uniquely identifies this entry in a report.  This auxiliary value is necessary, as the corresponding subscriber session job can specify up to three subscriber identities on which to sort the subscriber sessions that end up in the final report
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: csubjobreportsession
            
            	This object indicates the ifIndex\-value assigned to the subscriber session that satisfied the match criteria specified by the corresponding subscriber session job having a csubJobType of 'query'
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            

            """

            _prefix = 'CISCO-SUBSCRIBER-SESSION-MIB'
            _revision = '2012-08-08'

            def __init__(self):
                super(CiscoSubscriberSessionMib.Csubjobreporttable.Csubjobreportentry, self).__init__()

                self.yang_name = "csubJobReportEntry"
                self.yang_parent_name = "csubJobReportTable"

                self.csubjobid = YLeaf(YType.str, "csubJobId")

                self.csubjobreportid = YLeaf(YType.uint32, "csubJobReportId")

                self.csubjobreportsession = YLeaf(YType.int32, "csubJobReportSession")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("csubjobid",
                                "csubjobreportid",
                                "csubjobreportsession") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoSubscriberSessionMib.Csubjobreporttable.Csubjobreportentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoSubscriberSessionMib.Csubjobreporttable.Csubjobreportentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.csubjobid.is_set or
                    self.csubjobreportid.is_set or
                    self.csubjobreportsession.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.csubjobid.yfilter != YFilter.not_set or
                    self.csubjobreportid.yfilter != YFilter.not_set or
                    self.csubjobreportsession.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "csubJobReportEntry" + "[csubJobId='" + self.csubjobid.get() + "']" + "[csubJobReportId='" + self.csubjobreportid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/csubJobReportTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.csubjobid.is_set or self.csubjobid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobid.get_name_leafdata())
                if (self.csubjobreportid.is_set or self.csubjobreportid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobreportid.get_name_leafdata())
                if (self.csubjobreportsession.is_set or self.csubjobreportsession.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.csubjobreportsession.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "csubJobId" or name == "csubJobReportId" or name == "csubJobReportSession"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "csubJobId"):
                    self.csubjobid = value
                    self.csubjobid.value_namespace = name_space
                    self.csubjobid.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobReportId"):
                    self.csubjobreportid = value
                    self.csubjobreportid.value_namespace = name_space
                    self.csubjobreportid.value_namespace_prefix = name_space_prefix
                if(value_path == "csubJobReportSession"):
                    self.csubjobreportsession = value
                    self.csubjobreportsession.value_namespace = name_space
                    self.csubjobreportsession.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.csubjobreportentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.csubjobreportentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "csubJobReportTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "csubJobReportEntry"):
                for c in self.csubjobreportentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoSubscriberSessionMib.Csubjobreporttable.Csubjobreportentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.csubjobreportentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "csubJobReportEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.csubaggstatsinttable is not None and self.csubaggstatsinttable.has_data()) or
            (self.csubaggstatstable is not None and self.csubaggstatstable.has_data()) or
            (self.csubaggstatsthreshtable is not None and self.csubaggstatsthreshtable.has_data()) or
            (self.csubaggthresh is not None and self.csubaggthresh.has_data()) or
            (self.csubjob is not None and self.csubjob.has_data()) or
            (self.csubjobmatchparamstable is not None and self.csubjobmatchparamstable.has_data()) or
            (self.csubjobqueryparamstable is not None and self.csubjobqueryparamstable.has_data()) or
            (self.csubjobqueuetable is not None and self.csubjobqueuetable.has_data()) or
            (self.csubjobreporttable is not None and self.csubjobreporttable.has_data()) or
            (self.csubjobtable is not None and self.csubjobtable.has_data()) or
            (self.csubsessionbytypetable is not None and self.csubsessionbytypetable.has_data()) or
            (self.csubsessiontable is not None and self.csubsessiontable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.csubaggstatsinttable is not None and self.csubaggstatsinttable.has_operation()) or
            (self.csubaggstatstable is not None and self.csubaggstatstable.has_operation()) or
            (self.csubaggstatsthreshtable is not None and self.csubaggstatsthreshtable.has_operation()) or
            (self.csubaggthresh is not None and self.csubaggthresh.has_operation()) or
            (self.csubjob is not None and self.csubjob.has_operation()) or
            (self.csubjobmatchparamstable is not None and self.csubjobmatchparamstable.has_operation()) or
            (self.csubjobqueryparamstable is not None and self.csubjobqueryparamstable.has_operation()) or
            (self.csubjobqueuetable is not None and self.csubjobqueuetable.has_operation()) or
            (self.csubjobreporttable is not None and self.csubjobreporttable.has_operation()) or
            (self.csubjobtable is not None and self.csubjobtable.has_operation()) or
            (self.csubsessionbytypetable is not None and self.csubsessionbytypetable.has_operation()) or
            (self.csubsessiontable is not None and self.csubsessiontable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-SUBSCRIBER-SESSION-MIB:CISCO-SUBSCRIBER-SESSION-MIB" + path_buffer

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

        if (child_yang_name == "csubAggStatsIntTable"):
            if (self.csubaggstatsinttable is None):
                self.csubaggstatsinttable = CiscoSubscriberSessionMib.Csubaggstatsinttable()
                self.csubaggstatsinttable.parent = self
                self._children_name_map["csubaggstatsinttable"] = "csubAggStatsIntTable"
            return self.csubaggstatsinttable

        if (child_yang_name == "csubAggStatsTable"):
            if (self.csubaggstatstable is None):
                self.csubaggstatstable = CiscoSubscriberSessionMib.Csubaggstatstable()
                self.csubaggstatstable.parent = self
                self._children_name_map["csubaggstatstable"] = "csubAggStatsTable"
            return self.csubaggstatstable

        if (child_yang_name == "csubAggStatsThreshTable"):
            if (self.csubaggstatsthreshtable is None):
                self.csubaggstatsthreshtable = CiscoSubscriberSessionMib.Csubaggstatsthreshtable()
                self.csubaggstatsthreshtable.parent = self
                self._children_name_map["csubaggstatsthreshtable"] = "csubAggStatsThreshTable"
            return self.csubaggstatsthreshtable

        if (child_yang_name == "csubAggThresh"):
            if (self.csubaggthresh is None):
                self.csubaggthresh = CiscoSubscriberSessionMib.Csubaggthresh()
                self.csubaggthresh.parent = self
                self._children_name_map["csubaggthresh"] = "csubAggThresh"
            return self.csubaggthresh

        if (child_yang_name == "csubJob"):
            if (self.csubjob is None):
                self.csubjob = CiscoSubscriberSessionMib.Csubjob()
                self.csubjob.parent = self
                self._children_name_map["csubjob"] = "csubJob"
            return self.csubjob

        if (child_yang_name == "csubJobMatchParamsTable"):
            if (self.csubjobmatchparamstable is None):
                self.csubjobmatchparamstable = CiscoSubscriberSessionMib.Csubjobmatchparamstable()
                self.csubjobmatchparamstable.parent = self
                self._children_name_map["csubjobmatchparamstable"] = "csubJobMatchParamsTable"
            return self.csubjobmatchparamstable

        if (child_yang_name == "csubJobQueryParamsTable"):
            if (self.csubjobqueryparamstable is None):
                self.csubjobqueryparamstable = CiscoSubscriberSessionMib.Csubjobqueryparamstable()
                self.csubjobqueryparamstable.parent = self
                self._children_name_map["csubjobqueryparamstable"] = "csubJobQueryParamsTable"
            return self.csubjobqueryparamstable

        if (child_yang_name == "csubJobQueueTable"):
            if (self.csubjobqueuetable is None):
                self.csubjobqueuetable = CiscoSubscriberSessionMib.Csubjobqueuetable()
                self.csubjobqueuetable.parent = self
                self._children_name_map["csubjobqueuetable"] = "csubJobQueueTable"
            return self.csubjobqueuetable

        if (child_yang_name == "csubJobReportTable"):
            if (self.csubjobreporttable is None):
                self.csubjobreporttable = CiscoSubscriberSessionMib.Csubjobreporttable()
                self.csubjobreporttable.parent = self
                self._children_name_map["csubjobreporttable"] = "csubJobReportTable"
            return self.csubjobreporttable

        if (child_yang_name == "csubJobTable"):
            if (self.csubjobtable is None):
                self.csubjobtable = CiscoSubscriberSessionMib.Csubjobtable()
                self.csubjobtable.parent = self
                self._children_name_map["csubjobtable"] = "csubJobTable"
            return self.csubjobtable

        if (child_yang_name == "csubSessionByTypeTable"):
            if (self.csubsessionbytypetable is None):
                self.csubsessionbytypetable = CiscoSubscriberSessionMib.Csubsessionbytypetable()
                self.csubsessionbytypetable.parent = self
                self._children_name_map["csubsessionbytypetable"] = "csubSessionByTypeTable"
            return self.csubsessionbytypetable

        if (child_yang_name == "csubSessionTable"):
            if (self.csubsessiontable is None):
                self.csubsessiontable = CiscoSubscriberSessionMib.Csubsessiontable()
                self.csubsessiontable.parent = self
                self._children_name_map["csubsessiontable"] = "csubSessionTable"
            return self.csubsessiontable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "csubAggStatsIntTable" or name == "csubAggStatsTable" or name == "csubAggStatsThreshTable" or name == "csubAggThresh" or name == "csubJob" or name == "csubJobMatchParamsTable" or name == "csubJobQueryParamsTable" or name == "csubJobQueueTable" or name == "csubJobReportTable" or name == "csubJobTable" or name == "csubSessionByTypeTable" or name == "csubSessionTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoSubscriberSessionMib()
        return self._top_entity

