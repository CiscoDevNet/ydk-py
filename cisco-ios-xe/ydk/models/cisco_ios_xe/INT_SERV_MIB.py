""" INT_SERV_MIB 

The MIB module to describe the Integrated Services
Protocol

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class QosService(Enum):
    """
    QosService (Enum Class)

    The class of service in use by a flow.

    .. data:: bestEffort = 1

    .. data:: guaranteedDelay = 2

    .. data:: controlledLoad = 5

    """

    bestEffort = Enum.YLeaf(1, "bestEffort")

    guaranteedDelay = Enum.YLeaf(2, "guaranteedDelay")

    controlledLoad = Enum.YLeaf(5, "controlledLoad")



class INTSERVMIB(Entity):
    """
    
    
    .. attribute:: intsrvgenobjects
    
    	
    	**type**\:  :py:class:`IntSrvGenObjects <ydk.models.cisco_ios_xe.INT_SERV_MIB.INTSERVMIB.IntSrvGenObjects>`
    
    	**config**\: False
    
    .. attribute:: intsrvifattribtable
    
    	The reservable attributes of the system's  in\- terfaces
    	**type**\:  :py:class:`IntSrvIfAttribTable <ydk.models.cisco_ios_xe.INT_SERV_MIB.INTSERVMIB.IntSrvIfAttribTable>`
    
    	**config**\: False
    
    .. attribute:: intsrvflowtable
    
    	Information describing the reserved flows  us\- ing the system's interfaces
    	**type**\:  :py:class:`IntSrvFlowTable <ydk.models.cisco_ios_xe.INT_SERV_MIB.INTSERVMIB.IntSrvFlowTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'INT-SERV-MIB'
    _revision = '1997-10-03'

    def __init__(self):
        super(INTSERVMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "INT-SERV-MIB"
        self.yang_parent_name = "INT-SERV-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("intSrvGenObjects", ("intsrvgenobjects", INTSERVMIB.IntSrvGenObjects)), ("intSrvIfAttribTable", ("intsrvifattribtable", INTSERVMIB.IntSrvIfAttribTable)), ("intSrvFlowTable", ("intsrvflowtable", INTSERVMIB.IntSrvFlowTable))])
        self._leafs = OrderedDict()

        self.intsrvgenobjects = INTSERVMIB.IntSrvGenObjects()
        self.intsrvgenobjects.parent = self
        self._children_name_map["intsrvgenobjects"] = "intSrvGenObjects"

        self.intsrvifattribtable = INTSERVMIB.IntSrvIfAttribTable()
        self.intsrvifattribtable.parent = self
        self._children_name_map["intsrvifattribtable"] = "intSrvIfAttribTable"

        self.intsrvflowtable = INTSERVMIB.IntSrvFlowTable()
        self.intsrvflowtable.parent = self
        self._children_name_map["intsrvflowtable"] = "intSrvFlowTable"
        self._segment_path = lambda: "INT-SERV-MIB:INT-SERV-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(INTSERVMIB, [], name, value)


    class IntSrvGenObjects(Entity):
        """
        
        
        .. attribute:: intsrvflownewindex
        
        	This  object  is  used  to  assign  values  to intSrvFlowNumber  as described in 'Textual Con\- ventions  for  SNMPv2'.   The  network  manager reads  the  object,  and  then writes the value back in the SET that creates a new instance  of intSrvFlowEntry.   If  the  SET  fails with the code 'inconsistentValue', then the process must be  repeated; If the SET succeeds, then the ob\- ject is incremented, and the  new  instance  is created according to the manager's directions
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        

        """

        _prefix = 'INT-SERV-MIB'
        _revision = '1997-10-03'

        def __init__(self):
            super(INTSERVMIB.IntSrvGenObjects, self).__init__()

            self.yang_name = "intSrvGenObjects"
            self.yang_parent_name = "INT-SERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('intsrvflownewindex', (YLeaf(YType.int32, 'intSrvFlowNewIndex'), ['int'])),
            ])
            self.intsrvflownewindex = None
            self._segment_path = lambda: "intSrvGenObjects"
            self._absolute_path = lambda: "INT-SERV-MIB:INT-SERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(INTSERVMIB.IntSrvGenObjects, ['intsrvflownewindex'], name, value)



    class IntSrvIfAttribTable(Entity):
        """
        The reservable attributes of the system's  in\-
        terfaces.
        
        .. attribute:: intsrvifattribentry
        
        	The reservable attributes of  a  given  inter\- face
        	**type**\: list of  		 :py:class:`IntSrvIfAttribEntry <ydk.models.cisco_ios_xe.INT_SERV_MIB.INTSERVMIB.IntSrvIfAttribTable.IntSrvIfAttribEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'INT-SERV-MIB'
        _revision = '1997-10-03'

        def __init__(self):
            super(INTSERVMIB.IntSrvIfAttribTable, self).__init__()

            self.yang_name = "intSrvIfAttribTable"
            self.yang_parent_name = "INT-SERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("intSrvIfAttribEntry", ("intsrvifattribentry", INTSERVMIB.IntSrvIfAttribTable.IntSrvIfAttribEntry))])
            self._leafs = OrderedDict()

            self.intsrvifattribentry = YList(self)
            self._segment_path = lambda: "intSrvIfAttribTable"
            self._absolute_path = lambda: "INT-SERV-MIB:INT-SERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(INTSERVMIB.IntSrvIfAttribTable, [], name, value)


        class IntSrvIfAttribEntry(Entity):
            """
            The reservable attributes of  a  given  inter\-
            face.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: intsrvifattriballocatedbits
            
            	The number of bits/second currently  allocated to reserved sessions on the interface
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: Bits per second
            
            .. attribute:: intsrvifattribmaxallocatedbits
            
            	The maximum number of bits/second that may  be allocated  to  reserved  sessions on the inter\- face
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: Bits per second
            
            .. attribute:: intsrvifattriballocatedbuffer
            
            	The amount of buffer space  required  to  hold the simultaneous burst of all reserved flows on the interface
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: Bytes
            
            .. attribute:: intsrvifattribflows
            
            	The number of reserved flows currently  active on  this  interface.  A flow can be created ei\- ther from a reservation protocol (such as  RSVP or ST\-II) or via configuration information
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: intsrvifattribpropagationdelay
            
            	The amount of propagation delay that this  in\- terface  introduces  in addition to that intro\- diced by bit propagation delays
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: microseconds
            
            .. attribute:: intsrvifattribstatus
            
            	'active' on interfaces that are configured for RSVP
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'INT-SERV-MIB'
            _revision = '1997-10-03'

            def __init__(self):
                super(INTSERVMIB.IntSrvIfAttribTable.IntSrvIfAttribEntry, self).__init__()

                self.yang_name = "intSrvIfAttribEntry"
                self.yang_parent_name = "intSrvIfAttribTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('intsrvifattriballocatedbits', (YLeaf(YType.int32, 'intSrvIfAttribAllocatedBits'), ['int'])),
                    ('intsrvifattribmaxallocatedbits', (YLeaf(YType.int32, 'intSrvIfAttribMaxAllocatedBits'), ['int'])),
                    ('intsrvifattriballocatedbuffer', (YLeaf(YType.int32, 'intSrvIfAttribAllocatedBuffer'), ['int'])),
                    ('intsrvifattribflows', (YLeaf(YType.uint32, 'intSrvIfAttribFlows'), ['int'])),
                    ('intsrvifattribpropagationdelay', (YLeaf(YType.int32, 'intSrvIfAttribPropagationDelay'), ['int'])),
                    ('intsrvifattribstatus', (YLeaf(YType.enumeration, 'intSrvIfAttribStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ifindex = None
                self.intsrvifattriballocatedbits = None
                self.intsrvifattribmaxallocatedbits = None
                self.intsrvifattriballocatedbuffer = None
                self.intsrvifattribflows = None
                self.intsrvifattribpropagationdelay = None
                self.intsrvifattribstatus = None
                self._segment_path = lambda: "intSrvIfAttribEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "INT-SERV-MIB:INT-SERV-MIB/intSrvIfAttribTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(INTSERVMIB.IntSrvIfAttribTable.IntSrvIfAttribEntry, ['ifindex', 'intsrvifattriballocatedbits', 'intsrvifattribmaxallocatedbits', 'intsrvifattriballocatedbuffer', 'intsrvifattribflows', 'intsrvifattribpropagationdelay', 'intsrvifattribstatus'], name, value)




    class IntSrvFlowTable(Entity):
        """
        Information describing the reserved flows  us\-
        ing the system's interfaces.
        
        .. attribute:: intsrvflowentry
        
        	Information describing the use of a given  in\- terface   by   a   given   flow.   The  counter intSrvFlowPoliced starts counting  at  the  in\- stallation of the flow
        	**type**\: list of  		 :py:class:`IntSrvFlowEntry <ydk.models.cisco_ios_xe.INT_SERV_MIB.INTSERVMIB.IntSrvFlowTable.IntSrvFlowEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'INT-SERV-MIB'
        _revision = '1997-10-03'

        def __init__(self):
            super(INTSERVMIB.IntSrvFlowTable, self).__init__()

            self.yang_name = "intSrvFlowTable"
            self.yang_parent_name = "INT-SERV-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("intSrvFlowEntry", ("intsrvflowentry", INTSERVMIB.IntSrvFlowTable.IntSrvFlowEntry))])
            self._leafs = OrderedDict()

            self.intsrvflowentry = YList(self)
            self._segment_path = lambda: "intSrvFlowTable"
            self._absolute_path = lambda: "INT-SERV-MIB:INT-SERV-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(INTSERVMIB.IntSrvFlowTable, [], name, value)


        class IntSrvFlowEntry(Entity):
            """
            Information describing the use of a given  in\-
            terface   by   a   given   flow.   The  counter
            intSrvFlowPoliced starts counting  at  the  in\-
            stallation of the flow.
            
            .. attribute:: intsrvflownumber  (key)
            
            	The number of this flow.  This is for SNMP In\- dexing purposes only and has no relation to any protocol value
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: intsrvflowtype
            
            	The type of session (IP4, IP6, IP6  with  flow information, etc)
            	**type**\: int
            
            	**range:** 1..255
            
            	**config**\: False
            
            .. attribute:: intsrvflowowner
            
            	The process that installed this  flow  in  the queue policy database
            	**type**\:  :py:class:`IntSrvFlowOwner <ydk.models.cisco_ios_xe.INT_SERV_MIB.INTSERVMIB.IntSrvFlowTable.IntSrvFlowEntry.IntSrvFlowOwner>`
            
            	**config**\: False
            
            .. attribute:: intsrvflowdestaddr
            
            	The destination address used by all senders in this  session.   This object may not be changed when the value of the RowStatus object is  'ac\- tive'
            	**type**\: str
            
            	**length:** 4..16
            
            	**config**\: False
            
            .. attribute:: intsrvflowsenderaddr
            
            	The source address of the sender  selected  by this  reservation.  The value of all zeroes in\- dicates 'all senders'.  This object may not  be changed  when the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 4..16
            
            	**config**\: False
            
            .. attribute:: intsrvflowdestaddrlength
            
            	The length of the destination address in bits. This  is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 0..128
            
            	**config**\: False
            
            .. attribute:: intsrvflowsenderaddrlength
            
            	The length of the sender's  address  in  bits. This  is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 0..128
            
            	**config**\: False
            
            .. attribute:: intsrvflowprotocol
            
            	The IP Protocol used by a session.   This  ob\- ject  may  not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 1..255
            
            	**config**\: False
            
            .. attribute:: intsrvflowdestport
            
            	The UDP or TCP port number used as a  destina\- tion  port for all senders in this session.  If the  IP   protocol   in   use,   specified   by intSrvResvFwdProtocol,  is 50 (ESP) or 51 (AH), this  represents  a  virtual  destination  port number.   A value of zero indicates that the IP protocol in use does not have ports.  This  ob\- ject  may  not be changed when the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 2..4
            
            	**config**\: False
            
            .. attribute:: intsrvflowport
            
            	The UDP or TCP port number used  as  a  source port  for  this sender in this session.  If the IP    protocol    in    use,    specified    by intSrvResvFwdProtocol  is  50 (ESP) or 51 (AH), this represents a generalized  port  identifier (GPI).   A  value of zero indicates that the IP protocol in use does not have ports.  This  ob\- ject  may  not be changed when the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 2..4
            
            	**config**\: False
            
            .. attribute:: intsrvflowflowid
            
            	The flow ID that  this  sender  is  using,  if this  is  an IPv6 session
            	**type**\: int
            
            	**range:** 0..16777215
            
            	**config**\: False
            
            .. attribute:: intsrvflowinterface
            
            	The ifIndex value of the  interface  on  which this reservation exists
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: intsrvflowifaddr
            
            	The IP Address on the ifEntry  on  which  this reservation  exists.  This is present primarily to support those interfaces which layer  multi\- ple IP Addresses on the interface
            	**type**\: str
            
            	**length:** 4..16
            
            	**config**\: False
            
            .. attribute:: intsrvflowrate
            
            	The Reserved Rate of the sender's data stream. If this is a Controlled Load service flow, this rate is derived from the Tspec  rate  parameter (r).   If  this  is  a Guaranteed service flow, this rate is derived from  the  Rspec  clearing rate parameter (R)
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: bits per second
            
            .. attribute:: intsrvflowburst
            
            	The size of the largest  burst  expected  from the sender at a time.  If this is less than  the  sender's  advertised burst  size, the receiver is asking the network to provide flow pacing  beyond  what  would  be provided  under normal circumstances. Such pac\- ing is at the network's option
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: intsrvflowweight
            
            	The weight used  to  prioritize  the  traffic. Note  that the interpretation of this object is implementation\-specific,   as   implementations vary in their use of weighting procedures
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: intsrvflowqueue
            
            	The number of the queue used by this  traffic. Note  that the interpretation of this object is implementation\-specific,   as   implementations vary in their use of queue identifiers
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: intsrvflowmintu
            
            	The minimum message size for  this  flow.  The policing  algorithm will treat smaller messages as though they are this size
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: intsrvflowmaxtu
            
            	The maximum datagram size for this  flow  that will conform to the traffic specification. This value cannot exceed the MTU of the interface
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: intsrvflowbesteffort
            
            	The number of packets that  were  remanded  to best effort service
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: intsrvflowpoliced
            
            	The number of packets policed since the incep\- tion of the flow's service
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: intsrvflowdiscard
            
            	If 'true', the flow  is  to  incur  loss  when traffic is policed.  If 'false', policed traff\- ic is treated as best effort traffic
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: intsrvflowservice
            
            	The QoS service being applied to this flow
            	**type**\:  :py:class:`QosService <ydk.models.cisco_ios_xe.INT_SERV_MIB.QosService>`
            
            	**config**\: False
            
            .. attribute:: intsrvfloworder
            
            	In the event of ambiguity, the order in  which the  classifier  should  make  its comparisons. The row with intSrvFlowOrder=0 is tried  first, and  comparisons  proceed  in  the order of in\- creasing value.  Non\-serial implementations  of the classifier should emulate this behavior
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: intsrvflowstatus
            
            	'active' for all active  flows.   This  object may be used to install static classifier infor\- mation, delete classifier information,  or  au\- thorize such
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'INT-SERV-MIB'
            _revision = '1997-10-03'

            def __init__(self):
                super(INTSERVMIB.IntSrvFlowTable.IntSrvFlowEntry, self).__init__()

                self.yang_name = "intSrvFlowEntry"
                self.yang_parent_name = "intSrvFlowTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['intsrvflownumber']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('intsrvflownumber', (YLeaf(YType.int32, 'intSrvFlowNumber'), ['int'])),
                    ('intsrvflowtype', (YLeaf(YType.int32, 'intSrvFlowType'), ['int'])),
                    ('intsrvflowowner', (YLeaf(YType.enumeration, 'intSrvFlowOwner'), [('ydk.models.cisco_ios_xe.INT_SERV_MIB', 'INTSERVMIB', 'IntSrvFlowTable.IntSrvFlowEntry.IntSrvFlowOwner')])),
                    ('intsrvflowdestaddr', (YLeaf(YType.str, 'intSrvFlowDestAddr'), ['str'])),
                    ('intsrvflowsenderaddr', (YLeaf(YType.str, 'intSrvFlowSenderAddr'), ['str'])),
                    ('intsrvflowdestaddrlength', (YLeaf(YType.int32, 'intSrvFlowDestAddrLength'), ['int'])),
                    ('intsrvflowsenderaddrlength', (YLeaf(YType.int32, 'intSrvFlowSenderAddrLength'), ['int'])),
                    ('intsrvflowprotocol', (YLeaf(YType.int32, 'intSrvFlowProtocol'), ['int'])),
                    ('intsrvflowdestport', (YLeaf(YType.str, 'intSrvFlowDestPort'), ['str'])),
                    ('intsrvflowport', (YLeaf(YType.str, 'intSrvFlowPort'), ['str'])),
                    ('intsrvflowflowid', (YLeaf(YType.int32, 'intSrvFlowFlowId'), ['int'])),
                    ('intsrvflowinterface', (YLeaf(YType.int32, 'intSrvFlowInterface'), ['int'])),
                    ('intsrvflowifaddr', (YLeaf(YType.str, 'intSrvFlowIfAddr'), ['str'])),
                    ('intsrvflowrate', (YLeaf(YType.int32, 'intSrvFlowRate'), ['int'])),
                    ('intsrvflowburst', (YLeaf(YType.int32, 'intSrvFlowBurst'), ['int'])),
                    ('intsrvflowweight', (YLeaf(YType.int32, 'intSrvFlowWeight'), ['int'])),
                    ('intsrvflowqueue', (YLeaf(YType.int32, 'intSrvFlowQueue'), ['int'])),
                    ('intsrvflowmintu', (YLeaf(YType.int32, 'intSrvFlowMinTU'), ['int'])),
                    ('intsrvflowmaxtu', (YLeaf(YType.int32, 'intSrvFlowMaxTU'), ['int'])),
                    ('intsrvflowbesteffort', (YLeaf(YType.uint32, 'intSrvFlowBestEffort'), ['int'])),
                    ('intsrvflowpoliced', (YLeaf(YType.uint32, 'intSrvFlowPoliced'), ['int'])),
                    ('intsrvflowdiscard', (YLeaf(YType.boolean, 'intSrvFlowDiscard'), ['bool'])),
                    ('intsrvflowservice', (YLeaf(YType.enumeration, 'intSrvFlowService'), [('ydk.models.cisco_ios_xe.INT_SERV_MIB', 'QosService', '')])),
                    ('intsrvfloworder', (YLeaf(YType.int32, 'intSrvFlowOrder'), ['int'])),
                    ('intsrvflowstatus', (YLeaf(YType.enumeration, 'intSrvFlowStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.intsrvflownumber = None
                self.intsrvflowtype = None
                self.intsrvflowowner = None
                self.intsrvflowdestaddr = None
                self.intsrvflowsenderaddr = None
                self.intsrvflowdestaddrlength = None
                self.intsrvflowsenderaddrlength = None
                self.intsrvflowprotocol = None
                self.intsrvflowdestport = None
                self.intsrvflowport = None
                self.intsrvflowflowid = None
                self.intsrvflowinterface = None
                self.intsrvflowifaddr = None
                self.intsrvflowrate = None
                self.intsrvflowburst = None
                self.intsrvflowweight = None
                self.intsrvflowqueue = None
                self.intsrvflowmintu = None
                self.intsrvflowmaxtu = None
                self.intsrvflowbesteffort = None
                self.intsrvflowpoliced = None
                self.intsrvflowdiscard = None
                self.intsrvflowservice = None
                self.intsrvfloworder = None
                self.intsrvflowstatus = None
                self._segment_path = lambda: "intSrvFlowEntry" + "[intSrvFlowNumber='" + str(self.intsrvflownumber) + "']"
                self._absolute_path = lambda: "INT-SERV-MIB:INT-SERV-MIB/intSrvFlowTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(INTSERVMIB.IntSrvFlowTable.IntSrvFlowEntry, ['intsrvflownumber', 'intsrvflowtype', 'intsrvflowowner', 'intsrvflowdestaddr', 'intsrvflowsenderaddr', 'intsrvflowdestaddrlength', 'intsrvflowsenderaddrlength', 'intsrvflowprotocol', 'intsrvflowdestport', 'intsrvflowport', 'intsrvflowflowid', 'intsrvflowinterface', 'intsrvflowifaddr', 'intsrvflowrate', 'intsrvflowburst', 'intsrvflowweight', 'intsrvflowqueue', 'intsrvflowmintu', 'intsrvflowmaxtu', 'intsrvflowbesteffort', 'intsrvflowpoliced', 'intsrvflowdiscard', 'intsrvflowservice', 'intsrvfloworder', 'intsrvflowstatus'], name, value)

            class IntSrvFlowOwner(Enum):
                """
                IntSrvFlowOwner (Enum Class)

                The process that installed this  flow  in  the

                queue policy database.

                .. data:: other = 1

                .. data:: rsvp = 2

                .. data:: management = 3

                """

                other = Enum.YLeaf(1, "other")

                rsvp = Enum.YLeaf(2, "rsvp")

                management = Enum.YLeaf(3, "management")




    def clone_ptr(self):
        self._top_entity = INTSERVMIB()
        return self._top_entity



