""" INTEGRATED_SERVICES_MIB 

The MIB module to describe the Integrated Services
Protocol

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class QosService(Enum):
    """
    QosService

    The class of service in use by a flow.

    .. data:: bestEffort = 1

    .. data:: guaranteedDelay = 2

    .. data:: controlledLoad = 5

    """

    bestEffort = Enum.YLeaf(1, "bestEffort")

    guaranteedDelay = Enum.YLeaf(2, "guaranteedDelay")

    controlledLoad = Enum.YLeaf(5, "controlledLoad")



class INTEGRATEDSERVICESMIB(Entity):
    """
    
    
    .. attribute:: intsrvflowtable
    
    	Information describing the reserved flows  us\- ing the system's interfaces
    	**type**\:   :py:class:`Intsrvflowtable <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.INTEGRATEDSERVICESMIB.Intsrvflowtable>`
    
    .. attribute:: intsrvgenobjects
    
    	
    	**type**\:   :py:class:`Intsrvgenobjects <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.INTEGRATEDSERVICESMIB.Intsrvgenobjects>`
    
    .. attribute:: intsrvifattribtable
    
    	The reservable attributes of the system's  in\- terfaces
    	**type**\:   :py:class:`Intsrvifattribtable <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.INTEGRATEDSERVICESMIB.Intsrvifattribtable>`
    
    

    """

    _prefix = 'INTEGRATED-SERVICES-MIB'
    _revision = '1995-11-03'

    def __init__(self):
        super(INTEGRATEDSERVICESMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "INTEGRATED-SERVICES-MIB"
        self.yang_parent_name = "INTEGRATED-SERVICES-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"intSrvFlowTable" : ("intsrvflowtable", INTEGRATEDSERVICESMIB.Intsrvflowtable), "intSrvGenObjects" : ("intsrvgenobjects", INTEGRATEDSERVICESMIB.Intsrvgenobjects), "intSrvIfAttribTable" : ("intsrvifattribtable", INTEGRATEDSERVICESMIB.Intsrvifattribtable)}
        self._child_list_classes = {}

        self.intsrvflowtable = INTEGRATEDSERVICESMIB.Intsrvflowtable()
        self.intsrvflowtable.parent = self
        self._children_name_map["intsrvflowtable"] = "intSrvFlowTable"
        self._children_yang_names.add("intSrvFlowTable")

        self.intsrvgenobjects = INTEGRATEDSERVICESMIB.Intsrvgenobjects()
        self.intsrvgenobjects.parent = self
        self._children_name_map["intsrvgenobjects"] = "intSrvGenObjects"
        self._children_yang_names.add("intSrvGenObjects")

        self.intsrvifattribtable = INTEGRATEDSERVICESMIB.Intsrvifattribtable()
        self.intsrvifattribtable.parent = self
        self._children_name_map["intsrvifattribtable"] = "intSrvIfAttribTable"
        self._children_yang_names.add("intSrvIfAttribTable")
        self._segment_path = lambda: "INTEGRATED-SERVICES-MIB:INTEGRATED-SERVICES-MIB"


    class Intsrvflowtable(Entity):
        """
        Information describing the reserved flows  us\-
        ing the system's interfaces.
        
        .. attribute:: intsrvflowentry
        
        	Information describing the use of a given  in\- terface   by   a   given   flow.   The  counter intSrvFlowPoliced starts counting  at  the  in\- stallation of the flow
        	**type**\: list of    :py:class:`Intsrvflowentry <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.INTEGRATEDSERVICESMIB.Intsrvflowtable.Intsrvflowentry>`
        
        

        """

        _prefix = 'INTEGRATED-SERVICES-MIB'
        _revision = '1995-11-03'

        def __init__(self):
            super(INTEGRATEDSERVICESMIB.Intsrvflowtable, self).__init__()

            self.yang_name = "intSrvFlowTable"
            self.yang_parent_name = "INTEGRATED-SERVICES-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"intSrvFlowEntry" : ("intsrvflowentry", INTEGRATEDSERVICESMIB.Intsrvflowtable.Intsrvflowentry)}

            self.intsrvflowentry = YList(self)
            self._segment_path = lambda: "intSrvFlowTable"
            self._absolute_path = lambda: "INTEGRATED-SERVICES-MIB:INTEGRATED-SERVICES-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(INTEGRATEDSERVICESMIB.Intsrvflowtable, [], name, value)


        class Intsrvflowentry(Entity):
            """
            Information describing the use of a given  in\-
            terface   by   a   given   flow.   The  counter
            intSrvFlowPoliced starts counting  at  the  in\-
            stallation of the flow.
            
            .. attribute:: intsrvflownumber  <key>
            
            	The number of this flow.  This is for SNMP In\- dexing purposes only and has no relation to any protocol value
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: intsrvflowbesteffort
            
            	The number of packets that  were  remanded  to best effort service
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: intsrvflowburst
            
            	The size of the largest  burst  expected  from the sender at a time.  If this is less than  the  sender's  advertised burst  size, the receiver is asking the network to provide flow pacing  beyond  what  would  be provided  under normal circumstances. Such pac\- ing is at the network's option
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bytes
            
            .. attribute:: intsrvflowdestaddr
            
            	The destination address used by all senders in this  session.   This object may not be changed when the value of the RowStatus object is  'ac\- tive'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: intsrvflowdestaddrlength
            
            	The length of the destination address in bits. This  is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: intsrvflowdestport
            
            	The UDP or TCP port number used as a  destina\- tion  port for all senders in this session.  If the  IP   protocol   in   use,   specified   by intSrvResvFwdProtocol,  is 50 (ESP) or 51 (AH), this  represents  a  virtual  destination  port number.   A value of zero indicates that the IP protocol in use does not have ports.  This  ob\- ject  may  not be changed when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: intsrvflowdiscard
            
            	If 'true', the flow  is  to  incur  loss  when traffic is policed.  If 'false', policed traff\- ic is treated as best effort traffic
            	**type**\:  bool
            
            .. attribute:: intsrvflowflowid
            
            	The flow ID that  this  sender  is  using,  if this  is  an IPv6 session
            	**type**\:  int
            
            	**range:** 0..16777215
            
            .. attribute:: intsrvflowifaddr
            
            	The IP Address on the ifEntry  on  which  this reservation  exists.  This is present primarily to support those interfaces which layer  multi\- ple IP Addresses on the interface
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: intsrvflowinterface
            
            	The ifIndex value of the  interface  on  which this reservation exists
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: intsrvflowmaxtu
            
            	The maximum datagram size for this  flow  that will conform to the traffic specification. This value cannot exceed the MTU of the interface
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: intsrvflowmintu
            
            	The minimum message size for  this  flow.  The policing  algorithm will treat smaller messages as though they are this size
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: intsrvfloworder
            
            	In the event of ambiguity, the order in  which the  classifier  should  make  its comparisons. The row with intSrvFlowOrder=0 is tried  first, and  comparisons  proceed  in  the order of in\- creasing value.  Non\-serial implementations  of the classifier should emulate this behavior
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: intsrvflowowner
            
            	The process that installed this  flow  in  the queue policy database
            	**type**\:   :py:class:`Intsrvflowowner <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.INTEGRATEDSERVICESMIB.Intsrvflowtable.Intsrvflowentry.Intsrvflowowner>`
            
            .. attribute:: intsrvflowpoliced
            
            	The number of packets policed since the incep\- tion of the flow's service
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: intsrvflowport
            
            	The UDP or TCP port number used  as  a  source port  for  this sender in this session.  If the IP    protocol    in    use,    specified    by intSrvResvFwdProtocol  is  50 (ESP) or 51 (AH), this represents a generalized  port  identifier (GPI).   A  value of zero indicates that the IP protocol in use does not have ports.  This  ob\- ject  may  not be changed when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: intsrvflowprotocol
            
            	The IP Protocol used by a session.   This  ob\- ject  may  not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: intsrvflowqueue
            
            	The number of the queue used by this  traffic. Note  that the interpretation of this object is implementation\-specific,   as   implementations vary in their use of queue identifiers
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: intsrvflowrate
            
            	The Reserved Rate of the sender's data stream. If this is a Controlled Load service flow, this rate is derived from the Tspec  rate  parameter (r).   If  this  is  a Guaranteed service flow, this rate is derived from  the  Rspec  clearing rate parameter (R)
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: intsrvflowsenderaddr
            
            	The source address of the sender  selected  by this  reservation.  The value of all zeroes in\- dicates 'all senders'.  This object may not  be changed  when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: intsrvflowsenderaddrlength
            
            	The length of the sender's  address  in  bits. This  is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: intsrvflowservice
            
            	The QoS service being applied to this flow
            	**type**\:   :py:class:`QosService <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.QosService>`
            
            .. attribute:: intsrvflowstatus
            
            	'active' for all active  flows.   This  object may be used to install static classifier infor\- mation, delete classifier information,  or  au\- thorize such
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: intsrvflowtype
            
            	The type of session (IP4, IP6, IP6  with  flow information, etc)
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: intsrvflowweight
            
            	The weight used  to  prioritize  the  traffic. Note  that the interpretation of this object is implementation\-specific,   as   implementations vary in their use of weighting procedures
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            

            """

            _prefix = 'INTEGRATED-SERVICES-MIB'
            _revision = '1995-11-03'

            def __init__(self):
                super(INTEGRATEDSERVICESMIB.Intsrvflowtable.Intsrvflowentry, self).__init__()

                self.yang_name = "intSrvFlowEntry"
                self.yang_parent_name = "intSrvFlowTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.intsrvflownumber = YLeaf(YType.int32, "intSrvFlowNumber")

                self.intsrvflowbesteffort = YLeaf(YType.uint32, "intSrvFlowBestEffort")

                self.intsrvflowburst = YLeaf(YType.int32, "intSrvFlowBurst")

                self.intsrvflowdestaddr = YLeaf(YType.str, "intSrvFlowDestAddr")

                self.intsrvflowdestaddrlength = YLeaf(YType.int32, "intSrvFlowDestAddrLength")

                self.intsrvflowdestport = YLeaf(YType.str, "intSrvFlowDestPort")

                self.intsrvflowdiscard = YLeaf(YType.boolean, "intSrvFlowDiscard")

                self.intsrvflowflowid = YLeaf(YType.int32, "intSrvFlowFlowId")

                self.intsrvflowifaddr = YLeaf(YType.str, "intSrvFlowIfAddr")

                self.intsrvflowinterface = YLeaf(YType.int32, "intSrvFlowInterface")

                self.intsrvflowmaxtu = YLeaf(YType.int32, "intSrvFlowMaxTU")

                self.intsrvflowmintu = YLeaf(YType.int32, "intSrvFlowMinTU")

                self.intsrvfloworder = YLeaf(YType.int32, "intSrvFlowOrder")

                self.intsrvflowowner = YLeaf(YType.enumeration, "intSrvFlowOwner")

                self.intsrvflowpoliced = YLeaf(YType.uint32, "intSrvFlowPoliced")

                self.intsrvflowport = YLeaf(YType.str, "intSrvFlowPort")

                self.intsrvflowprotocol = YLeaf(YType.int32, "intSrvFlowProtocol")

                self.intsrvflowqueue = YLeaf(YType.int32, "intSrvFlowQueue")

                self.intsrvflowrate = YLeaf(YType.int32, "intSrvFlowRate")

                self.intsrvflowsenderaddr = YLeaf(YType.str, "intSrvFlowSenderAddr")

                self.intsrvflowsenderaddrlength = YLeaf(YType.int32, "intSrvFlowSenderAddrLength")

                self.intsrvflowservice = YLeaf(YType.enumeration, "intSrvFlowService")

                self.intsrvflowstatus = YLeaf(YType.enumeration, "intSrvFlowStatus")

                self.intsrvflowtype = YLeaf(YType.int32, "intSrvFlowType")

                self.intsrvflowweight = YLeaf(YType.int32, "intSrvFlowWeight")
                self._segment_path = lambda: "intSrvFlowEntry" + "[intSrvFlowNumber='" + self.intsrvflownumber.get() + "']"
                self._absolute_path = lambda: "INTEGRATED-SERVICES-MIB:INTEGRATED-SERVICES-MIB/intSrvFlowTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(INTEGRATEDSERVICESMIB.Intsrvflowtable.Intsrvflowentry, ['intsrvflownumber', 'intsrvflowbesteffort', 'intsrvflowburst', 'intsrvflowdestaddr', 'intsrvflowdestaddrlength', 'intsrvflowdestport', 'intsrvflowdiscard', 'intsrvflowflowid', 'intsrvflowifaddr', 'intsrvflowinterface', 'intsrvflowmaxtu', 'intsrvflowmintu', 'intsrvfloworder', 'intsrvflowowner', 'intsrvflowpoliced', 'intsrvflowport', 'intsrvflowprotocol', 'intsrvflowqueue', 'intsrvflowrate', 'intsrvflowsenderaddr', 'intsrvflowsenderaddrlength', 'intsrvflowservice', 'intsrvflowstatus', 'intsrvflowtype', 'intsrvflowweight'], name, value)

            class Intsrvflowowner(Enum):
                """
                Intsrvflowowner

                The process that installed this  flow  in  the

                queue policy database.

                .. data:: other = 1

                .. data:: rsvp = 2

                .. data:: management = 3

                """

                other = Enum.YLeaf(1, "other")

                rsvp = Enum.YLeaf(2, "rsvp")

                management = Enum.YLeaf(3, "management")



    class Intsrvgenobjects(Entity):
        """
        
        
        .. attribute:: intsrvflownewindex
        
        	This  object  is  used  to  assign  values  to intSrvFlowNumber  as described in 'Textual Con\- ventions  for  SNMPv2'.   The  network  manager reads  the  object,  and  then writes the value back in the SET that creates a new instance  of intSrvFlowEntry.   If  the  SET  fails with the code 'inconsistentValue', then the process must be  repeated; If the SET succeeds, then the ob\- ject is incremented, and the  new  instance  is created according to the manager's directions
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'INTEGRATED-SERVICES-MIB'
        _revision = '1995-11-03'

        def __init__(self):
            super(INTEGRATEDSERVICESMIB.Intsrvgenobjects, self).__init__()

            self.yang_name = "intSrvGenObjects"
            self.yang_parent_name = "INTEGRATED-SERVICES-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.intsrvflownewindex = YLeaf(YType.int32, "intSrvFlowNewIndex")
            self._segment_path = lambda: "intSrvGenObjects"
            self._absolute_path = lambda: "INTEGRATED-SERVICES-MIB:INTEGRATED-SERVICES-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(INTEGRATEDSERVICESMIB.Intsrvgenobjects, ['intsrvflownewindex'], name, value)


    class Intsrvifattribtable(Entity):
        """
        The reservable attributes of the system's  in\-
        terfaces.
        
        .. attribute:: intsrvifattribentry
        
        	The reservable attributes of  a  given  inter\- face
        	**type**\: list of    :py:class:`Intsrvifattribentry <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.INTEGRATEDSERVICESMIB.Intsrvifattribtable.Intsrvifattribentry>`
        
        

        """

        _prefix = 'INTEGRATED-SERVICES-MIB'
        _revision = '1995-11-03'

        def __init__(self):
            super(INTEGRATEDSERVICESMIB.Intsrvifattribtable, self).__init__()

            self.yang_name = "intSrvIfAttribTable"
            self.yang_parent_name = "INTEGRATED-SERVICES-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"intSrvIfAttribEntry" : ("intsrvifattribentry", INTEGRATEDSERVICESMIB.Intsrvifattribtable.Intsrvifattribentry)}

            self.intsrvifattribentry = YList(self)
            self._segment_path = lambda: "intSrvIfAttribTable"
            self._absolute_path = lambda: "INTEGRATED-SERVICES-MIB:INTEGRATED-SERVICES-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(INTEGRATEDSERVICESMIB.Intsrvifattribtable, [], name, value)


        class Intsrvifattribentry(Entity):
            """
            The reservable attributes of  a  given  inter\-
            face.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: intsrvifattriballocatedbits
            
            	The number of bits/second currently  allocated to reserved sessions on the interface
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: Bits per second
            
            .. attribute:: intsrvifattriballocatedbuffer
            
            	The amount of buffer space  required  to  hold the simultaneous burst of all reserved flows on the interface
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: Bytes
            
            .. attribute:: intsrvifattribflows
            
            	The number of reserved flows currently  active on  this  interface.  A flow can be created ei\- ther from a reservation protocol (such as  RSVP or ST\-II) or via configuration information
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: intsrvifattribmaxallocatedbits
            
            	The maximum number of bits/second that may  be allocated  to  reserved  sessions on the inter\- face
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: Bits per second
            
            .. attribute:: intsrvifattribpropagationdelay
            
            	The amount of propagation delay that this  in\- terface  introduces  in addition to that intro\- diced by bit propagation delays
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: intsrvifattribstatus
            
            	'active' on interfaces that are configured for RSVP
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'INTEGRATED-SERVICES-MIB'
            _revision = '1995-11-03'

            def __init__(self):
                super(INTEGRATEDSERVICESMIB.Intsrvifattribtable.Intsrvifattribentry, self).__init__()

                self.yang_name = "intSrvIfAttribEntry"
                self.yang_parent_name = "intSrvIfAttribTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.intsrvifattriballocatedbits = YLeaf(YType.int32, "intSrvIfAttribAllocatedBits")

                self.intsrvifattriballocatedbuffer = YLeaf(YType.int32, "intSrvIfAttribAllocatedBuffer")

                self.intsrvifattribflows = YLeaf(YType.uint32, "intSrvIfAttribFlows")

                self.intsrvifattribmaxallocatedbits = YLeaf(YType.int32, "intSrvIfAttribMaxAllocatedBits")

                self.intsrvifattribpropagationdelay = YLeaf(YType.int32, "intSrvIfAttribPropagationDelay")

                self.intsrvifattribstatus = YLeaf(YType.enumeration, "intSrvIfAttribStatus")
                self._segment_path = lambda: "intSrvIfAttribEntry" + "[ifIndex='" + self.ifindex.get() + "']"
                self._absolute_path = lambda: "INTEGRATED-SERVICES-MIB:INTEGRATED-SERVICES-MIB/intSrvIfAttribTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(INTEGRATEDSERVICESMIB.Intsrvifattribtable.Intsrvifattribentry, ['ifindex', 'intsrvifattriballocatedbits', 'intsrvifattriballocatedbuffer', 'intsrvifattribflows', 'intsrvifattribmaxallocatedbits', 'intsrvifattribpropagationdelay', 'intsrvifattribstatus'], name, value)

    def clone_ptr(self):
        self._top_entity = INTEGRATEDSERVICESMIB()
        return self._top_entity

