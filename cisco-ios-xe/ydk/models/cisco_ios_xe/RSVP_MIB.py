""" RSVP_MIB 

The MIB module to describe the RSVP Protocol

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class RsvpEncapsulation(Enum):
    """
    RsvpEncapsulation

    This indicates the encapsulation that an  RSVP

    Neighbor is perceived to be using.

    .. data:: ip = 1

    .. data:: udp = 2

    .. data:: both = 3

    """

    ip = Enum.YLeaf(1, "ip")

    udp = Enum.YLeaf(2, "udp")

    both = Enum.YLeaf(3, "both")



class RSVPMIB(Entity):
    """
    
    
    .. attribute:: rsvpgenobjects
    
    	
    	**type**\:  :py:class:`Rsvpgenobjects <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpgenobjects>`
    
    .. attribute:: rsvpsessiontable
    
    	A table  of	 all  sessions	seen  by  a  given system
    	**type**\:  :py:class:`Rsvpsessiontable <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpsessiontable>`
    
    .. attribute:: rsvpsendertable
    
    	Information	describing the	state  information displayed by	senders	in PATH	messages
    	**type**\:  :py:class:`Rsvpsendertable <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpsendertable>`
    
    .. attribute:: rsvpsenderoutinterfacetable
    
    	List of outgoing interfaces	that PATH messages use.	 The  ifIndex  is the ifIndex value of the egress interface
    	**type**\:  :py:class:`Rsvpsenderoutinterfacetable <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpsenderoutinterfacetable>`
    
    .. attribute:: rsvpresvtable
    
    	Information	describing the	state  information displayed by	receivers in RESV messages
    	**type**\:  :py:class:`Rsvpresvtable <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpresvtable>`
    
    .. attribute:: rsvpresvfwdtable
    
    	Information	describing the	state  information displayed upstream in RESV messages
    	**type**\:  :py:class:`Rsvpresvfwdtable <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpresvfwdtable>`
    
    .. attribute:: rsvpiftable
    
    	The	RSVP\-specific attributes of  the  system's interfaces
    	**type**\:  :py:class:`Rsvpiftable <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpiftable>`
    
    .. attribute:: rsvpnbrtable
    
    	Information	describing  the	 Neighbors  of	an RSVP	system
    	**type**\:  :py:class:`Rsvpnbrtable <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpnbrtable>`
    
    

    """

    _prefix = 'RSVP-MIB'
    _revision = '1998-08-25'

    def __init__(self):
        super(RSVPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "RSVP-MIB"
        self.yang_parent_name = "RSVP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"rsvpGenObjects" : ("rsvpgenobjects", RSVPMIB.Rsvpgenobjects), "rsvpSessionTable" : ("rsvpsessiontable", RSVPMIB.Rsvpsessiontable), "rsvpSenderTable" : ("rsvpsendertable", RSVPMIB.Rsvpsendertable), "rsvpSenderOutInterfaceTable" : ("rsvpsenderoutinterfacetable", RSVPMIB.Rsvpsenderoutinterfacetable), "rsvpResvTable" : ("rsvpresvtable", RSVPMIB.Rsvpresvtable), "rsvpResvFwdTable" : ("rsvpresvfwdtable", RSVPMIB.Rsvpresvfwdtable), "rsvpIfTable" : ("rsvpiftable", RSVPMIB.Rsvpiftable), "rsvpNbrTable" : ("rsvpnbrtable", RSVPMIB.Rsvpnbrtable)}
        self._child_list_classes = {}

        self.rsvpgenobjects = RSVPMIB.Rsvpgenobjects()
        self.rsvpgenobjects.parent = self
        self._children_name_map["rsvpgenobjects"] = "rsvpGenObjects"
        self._children_yang_names.add("rsvpGenObjects")

        self.rsvpsessiontable = RSVPMIB.Rsvpsessiontable()
        self.rsvpsessiontable.parent = self
        self._children_name_map["rsvpsessiontable"] = "rsvpSessionTable"
        self._children_yang_names.add("rsvpSessionTable")

        self.rsvpsendertable = RSVPMIB.Rsvpsendertable()
        self.rsvpsendertable.parent = self
        self._children_name_map["rsvpsendertable"] = "rsvpSenderTable"
        self._children_yang_names.add("rsvpSenderTable")

        self.rsvpsenderoutinterfacetable = RSVPMIB.Rsvpsenderoutinterfacetable()
        self.rsvpsenderoutinterfacetable.parent = self
        self._children_name_map["rsvpsenderoutinterfacetable"] = "rsvpSenderOutInterfaceTable"
        self._children_yang_names.add("rsvpSenderOutInterfaceTable")

        self.rsvpresvtable = RSVPMIB.Rsvpresvtable()
        self.rsvpresvtable.parent = self
        self._children_name_map["rsvpresvtable"] = "rsvpResvTable"
        self._children_yang_names.add("rsvpResvTable")

        self.rsvpresvfwdtable = RSVPMIB.Rsvpresvfwdtable()
        self.rsvpresvfwdtable.parent = self
        self._children_name_map["rsvpresvfwdtable"] = "rsvpResvFwdTable"
        self._children_yang_names.add("rsvpResvFwdTable")

        self.rsvpiftable = RSVPMIB.Rsvpiftable()
        self.rsvpiftable.parent = self
        self._children_name_map["rsvpiftable"] = "rsvpIfTable"
        self._children_yang_names.add("rsvpIfTable")

        self.rsvpnbrtable = RSVPMIB.Rsvpnbrtable()
        self.rsvpnbrtable.parent = self
        self._children_name_map["rsvpnbrtable"] = "rsvpNbrTable"
        self._children_yang_names.add("rsvpNbrTable")
        self._segment_path = lambda: "RSVP-MIB:RSVP-MIB"


    class Rsvpgenobjects(Entity):
        """
        
        
        .. attribute:: rsvpbadpackets
        
        	This object	keeps a	count of the number of bad RSVP	packets	received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: rsvpsendernewindex
        
        	This  object  is  used  to	assign	values	to rsvpSenderNumber   as   described  in  'Textual Conventions for SNMPv2'.  The  network  manager reads  the  object,	and  then writes the value back	in the SET that	creates	a new instance	of rsvpSenderEntry.   If  the  SET  fails with the code	'inconsistentValue', then the process must be  repeated;  If  the  SET	succeeds, then the object is incremented, and the new instance	is created according to	the manager's directions
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: rsvpresvnewindex
        
        	This  object  is  used  to	assign	values	to rsvpResvNumber   as	 described   in	  'Textual Conventions for SNMPv2'.  The  network  manager reads  the  object,	and  then writes the value back	in the SET that	creates	a new instance	of rsvpResvEntry.   If the SET fails with the code 'inconsistentValue',	then the process  must	be repeated;  If the SET succeeds, then	the object is incremented, and the new instance	is created according to	the manager's directions
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: rsvpresvfwdnewindex
        
        	This  object  is  used  to	assign	values	to rsvpResvFwdNumber   as  described  in  'Textual Conventions for SNMPv2'.  The  network  manager reads  the  object,	and  then writes the value back	in the SET that	creates	a new instance	of rsvpResvFwdEntry.   If  the	SET fails with the code	'inconsistentValue', then the process must be  repeated;  If  the  SET	succeeds, then the object is incremented, and the new instance	is created according to	the manager's directions
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: rsvpsessionnewindex
        
        	This  object  is  used  to	assign	values	to rsvpSessionNumber   as  described  in  'Textual Conventions for SNMPv2'.  The  network  manager reads  the  object,	and  then writes the value back	in the SET that	creates	a new instance	of rsvpSessionEntry.   If  the	SET fails with the code	'inconsistentValue', then the process must be  repeated;  If  the  SET	succeeds, then the object is incremented, and the new instance	is created according to	the manager's directions
        	**type**\: int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RSVPMIB.Rsvpgenobjects, self).__init__()

            self.yang_name = "rsvpGenObjects"
            self.yang_parent_name = "RSVP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.rsvpbadpackets = YLeaf(YType.uint32, "rsvpBadPackets")

            self.rsvpsendernewindex = YLeaf(YType.int32, "rsvpSenderNewIndex")

            self.rsvpresvnewindex = YLeaf(YType.int32, "rsvpResvNewIndex")

            self.rsvpresvfwdnewindex = YLeaf(YType.int32, "rsvpResvFwdNewIndex")

            self.rsvpsessionnewindex = YLeaf(YType.int32, "rsvpSessionNewIndex")
            self._segment_path = lambda: "rsvpGenObjects"
            self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RSVPMIB.Rsvpgenobjects, ['rsvpbadpackets', 'rsvpsendernewindex', 'rsvpresvnewindex', 'rsvpresvfwdnewindex', 'rsvpsessionnewindex'], name, value)


    class Rsvpsessiontable(Entity):
        """
        A table  of	 all  sessions	seen  by  a  given
        system.
        
        .. attribute:: rsvpsessionentry
        
        	A single session seen by a given system
        	**type**\: list of  		 :py:class:`Rsvpsessionentry <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpsessiontable.Rsvpsessionentry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RSVPMIB.Rsvpsessiontable, self).__init__()

            self.yang_name = "rsvpSessionTable"
            self.yang_parent_name = "RSVP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rsvpSessionEntry" : ("rsvpsessionentry", RSVPMIB.Rsvpsessiontable.Rsvpsessionentry)}

            self.rsvpsessionentry = YList(self)
            self._segment_path = lambda: "rsvpSessionTable"
            self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RSVPMIB.Rsvpsessiontable, [], name, value)


        class Rsvpsessionentry(Entity):
            """
            A single session seen by a given system.
            
            .. attribute:: rsvpsessionnumber  <key>
            
            	The	number of this session.	 This is for  SNMP Indexing  purposes  only and	has no relation	to any protocol	value
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpsessiontype
            
            	The	type of	session	(IP4, IP6, IP6	with  flow information,	etc)
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: rsvpsessiondestaddr
            
            	The	destination address used by all	senders	in this	 session.   This object	may not	be changed when	the  value  of	the  RowStatus	object	is 'active'
            	**type**\: str
            
            	**length:** 4..16
            
            .. attribute:: rsvpsessiondestaddrlength
            
            	The	CIDR prefix length of the session address, which   is	32  for	 IP4  host  and	 multicast addresses, and 128  for  IP6	 addresses.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 0..128
            
            .. attribute:: rsvpsessionprotocol
            
            	The	IP Protocol used by  this  session.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: rsvpsessionport
            
            	The	 UDP  or  TCP  port  number  used   as	 a destination	 port  for  all	 senders  in  this session.  If	the IP protocol	in use,	 specified by  rsvpSenderProtocol, is 50 (ESP) or 51 (AH), this	 represents  a	virtual	 destination  port number.   A value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 2..4
            
            .. attribute:: rsvpsessionsenders
            
            	The	number of distinct senders currently known to be part of this session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpsessionreceivers
            
            	The	number of reservations being requested	of this	system for this	session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpsessionrequests
            
            	The	number of reservation requests this system is sending upstream for this	session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RSVPMIB.Rsvpsessiontable.Rsvpsessionentry, self).__init__()

                self.yang_name = "rsvpSessionEntry"
                self.yang_parent_name = "rsvpSessionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.rsvpsessionnumber = YLeaf(YType.int32, "rsvpSessionNumber")

                self.rsvpsessiontype = YLeaf(YType.int32, "rsvpSessionType")

                self.rsvpsessiondestaddr = YLeaf(YType.str, "rsvpSessionDestAddr")

                self.rsvpsessiondestaddrlength = YLeaf(YType.int32, "rsvpSessionDestAddrLength")

                self.rsvpsessionprotocol = YLeaf(YType.int32, "rsvpSessionProtocol")

                self.rsvpsessionport = YLeaf(YType.str, "rsvpSessionPort")

                self.rsvpsessionsenders = YLeaf(YType.uint32, "rsvpSessionSenders")

                self.rsvpsessionreceivers = YLeaf(YType.uint32, "rsvpSessionReceivers")

                self.rsvpsessionrequests = YLeaf(YType.uint32, "rsvpSessionRequests")
                self._segment_path = lambda: "rsvpSessionEntry" + "[rsvpSessionNumber='" + self.rsvpsessionnumber.get() + "']"
                self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/rsvpSessionTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RSVPMIB.Rsvpsessiontable.Rsvpsessionentry, ['rsvpsessionnumber', 'rsvpsessiontype', 'rsvpsessiondestaddr', 'rsvpsessiondestaddrlength', 'rsvpsessionprotocol', 'rsvpsessionport', 'rsvpsessionsenders', 'rsvpsessionreceivers', 'rsvpsessionrequests'], name, value)


    class Rsvpsendertable(Entity):
        """
        Information	describing the	state  information
        displayed by	senders	in PATH	messages.
        
        .. attribute:: rsvpsenderentry
        
        	Information	describing the	state  information displayed by	a single sender's PATH message
        	**type**\: list of  		 :py:class:`Rsvpsenderentry <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpsendertable.Rsvpsenderentry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RSVPMIB.Rsvpsendertable, self).__init__()

            self.yang_name = "rsvpSenderTable"
            self.yang_parent_name = "RSVP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rsvpSenderEntry" : ("rsvpsenderentry", RSVPMIB.Rsvpsendertable.Rsvpsenderentry)}

            self.rsvpsenderentry = YList(self)
            self._segment_path = lambda: "rsvpSenderTable"
            self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RSVPMIB.Rsvpsendertable, [], name, value)


        class Rsvpsenderentry(Entity):
            """
            Information	describing the	state  information
            displayed by	a single sender's PATH message.
            
            .. attribute:: rsvpsessionnumber  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsessionnumber <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpsessiontable.Rsvpsessionentry>`
            
            .. attribute:: rsvpsendernumber  <key>
            
            	The	number of this sender.	This is	 for  SNMP Indexing  purposes  only and	has no relation	to any protocol	value
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpsendertype
            
            	The	type of	session	(IP4, IP6, IP6	with  flow information,	etc)
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: rsvpsenderdestaddr
            
            	The	destination address used by all	senders	in this	 session.   This object	may not	be changed when	the  value  of	the  RowStatus	object	is 'active'
            	**type**\: str
            
            	**length:** 4..16
            
            .. attribute:: rsvpsenderaddr
            
            	The	source address used by this sender in this session.   This  object may not be changed when the value of	the RowStatus object is	'active'
            	**type**\: str
            
            	**length:** 4..16
            
            .. attribute:: rsvpsenderdestaddrlength
            
            	The	length of the destination address in bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 0..128
            
            .. attribute:: rsvpsenderaddrlength
            
            	The	length of the sender's	address	 in  bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 0..128
            
            .. attribute:: rsvpsenderprotocol
            
            	The	IP Protocol used by  this  session.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: rsvpsenderdestport
            
            	The	 UDP  or  TCP  port  number  used   as	 a destination	 port  for  all	 senders  in  this session.  If	the IP protocol	in use,	 specified by  rsvpSenderProtocol, is 50 (ESP) or 51 (AH), this	 represents  a	virtual	 destination  port number.   A value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 2..4
            
            .. attribute:: rsvpsenderport
            
            	The	UDP or TCP port	number used  as	 a  source port	 for  this sender in this session.  If the IP	 protocol    in	   use,	   specified	by rsvpSenderProtocol is 50 (ESP) or 51	(AH), this represents a	generalized port identifier (GPI). A  value of zero indicates that the IP protocol in use does not have	ports.	 This  object  may not	be changed when	the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 2..4
            
            .. attribute:: rsvpsenderflowid
            
            	The	flow ID	that  this  sender  is	using,	if this	 is  an	IPv6 session
            	**type**\: int
            
            	**range:** 0..16777215
            
            .. attribute:: rsvpsenderhopaddr
            
            	The	address	used  by  the  previous	 RSVP  hop (which may be the original sender)
            	**type**\: str
            
            	**length:** 4..16
            
            .. attribute:: rsvpsenderhoplih
            
            	The	 Logical  Interface  Handle  used  by  the previous  RSVP  hop	(which may be the original sender)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: rsvpsenderinterface
            
            	The	ifIndex	value of the  interface	 on  which this	PATH message was most recently received
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: rsvpsendertspecrate
            
            	The	Average	Bit  Rate  of  the  sender's  data stream.    Within  a	 transmission  burst,  the arrival   rate    may    be	  as	fast	as rsvpSenderTSpecPeakRate  (if	 supported  by the service model); however, averaged across two	or more	 burst	intervals,  the	 rate  should  not exceed rsvpSenderTSpecRate.  Note	that this is a prediction, often based	on the	general	 capability  of	a type of codec	or particular encoding;	the measured average  rate may be significantly	lower
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsendertspecpeakrate
            
            	The	Peak Bit Rate of the sender's data stream. Traffic  arrival is not expected to exceed this rate	at any time, apart  from  the  effects	of jitter in the network.  If not specified in the TSpec, this returns zero or noSuchValue
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsendertspecburst
            
            	The	size of	the largest  burst  expected  from the sender at a time
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: bytes
            
            .. attribute:: rsvpsendertspecmintu
            
            	The	minimum	message	size for  this	flow.  The policing  algorithm will treat smaller messages as though they are this size
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpsendertspecmaxtu
            
            	The	maximum	message	size for  this	flow.  The admission  algorithm	 will  reject TSpecs whose Maximum Transmission	Unit, plus  the	 interface headers, exceed the interface MTU
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpsenderinterval
            
            	The	 interval  between  refresh  messages	as advertised by the Previous Hop
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpsenderrsvphop
            
            	If TRUE, the node believes that  the  previous IP  hop  is	an  RSVP  hop.	If FALSE, the node believes that the previous IP hop may not be	an RSVP	hop
            	**type**\: bool
            
            .. attribute:: rsvpsenderlastchange
            
            	The	time of	 the  last  change  in	this  PATH message;  This  is either the first time it was received or the time	of the most recent  change in parameters
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpsenderpolicy
            
            	The	contents of the	policy	object,	 displayed as an uninterpreted string of octets, including the object header.  In the absence of  such	an object, this	should be of zero length
            	**type**\: str
            
            	**length:** 4..65536
            
            .. attribute:: rsvpsenderadspecbreak
            
            	The	global break bit general  characterization parameter  from  the	ADSPEC.	 If TRUE, at least one non\-IS hop was detected in  the	path.	If FALSE, no non\-IS hops were detected
            	**type**\: bool
            
            .. attribute:: rsvpsenderadspechopcount
            
            	The	  hop	count	general	  characterization parameter from the ADSPEC.  A return	of zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: rsvpsenderadspecpathbw
            
            	The	  path	  bandwidth    estimate	   general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsenderadspecminlatency
            
            	The	   minimum    path     latency	   general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecmtu
            
            	The	composed Maximum Transmission Unit general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderadspecguaranteedsvc
            
            	If TRUE,  the  ADSPEC  contains  a	Guaranteed Service  fragment.	If  FALSE, the ADSPEC does not contain a Guaranteed Service fragment
            	**type**\: bool
            
            .. attribute:: rsvpsenderadspecguaranteedbreak
            
            	If TRUE, the Guaranteed Service  fragment  has its	'break'	 bit  set,  indicating that one	or more	nodes along the	path do	 not  support  the guaranteed	  service.     If    FALSE,    and rsvpSenderAdspecGuaranteedSvc  is   TRUE,   the 'break' bit is not set.  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns FALSE or noSuchValue
            	**type**\: bool
            
            .. attribute:: rsvpsenderadspecguaranteedctot
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the  end\-to\-end	 composed  value  for  the guaranteed service 'C' parameter.  A	return	of zero	  or  noSuchValue  indicates  one  of  the following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderadspecguaranteeddtot
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the  end\-to\-end	 composed  value  for  the guaranteed service 'D' parameter.  A	return	of zero	  or  noSuchValue  indicates  one  of  the following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecguaranteedcsum
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the  composed  value  for  the	guaranteed service 'C' parameter since the last	 reshaping point.    A	 return	 of  zero  or  noSuchValue indicates one of the	following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderadspecguaranteeddsum
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the  composed  value  for  the	guaranteed service 'D' parameter since the last	 reshaping point.    A	 return	 of  zero  or  noSuchValue indicates one of the	following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecguaranteedhopcount
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is  the  service\-specific  override	of the hop count general characterization  parameter  from the	ADSPEC.	  A  return of zero or noSuchValue indicates one of the	following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: rsvpsenderadspecguaranteedpathbw
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is  the  service\-specific  override of the path bandwidth  estimate	general	  characterization parameter from the ADSPEC.  A return	of zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsenderadspecguaranteedminlatency
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is the service\-specific override of the minimum path	latency	general	characterization parameter from	  the	ADSPEC.	   A  return  of  zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecguaranteedmtu
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the   service\-specific	 override  of  the composed  Maximum  Transmission  Unit   general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderadspecctrlloadsvc
            
            	If TRUE, the ADSPEC	contains a Controlled Load Service  fragment.	If  FALSE, the ADSPEC does not	 contain   a   Controlled   Load   Service fragment
            	**type**\: bool
            
            .. attribute:: rsvpsenderadspecctrlloadbreak
            
            	If TRUE, the Controlled Load Service  fragment has its 'break' bit set, indicating that one	or more	nodes along the	path do	 not  support  the controlled	load   service.	   If  FALSE,  and rsvpSenderAdspecCtrlLoadSvc	 is   TRUE,    the 'break' bit is not set.  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns FALSE or noSuchValue
            	**type**\: bool
            
            .. attribute:: rsvpsenderadspecctrlloadhopcount
            
            	If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this is  the  service\-specific  override	of the hop count general characterization  parameter  from the	ADSPEC.	  A  return of zero or noSuchValue indicates one of the	following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: rsvpsenderadspecctrlloadpathbw
            
            	If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this is  the  service\-specific  override of the path bandwidth  estimate	general	  characterization parameter from the ADSPEC.  A return	of zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsenderadspecctrlloadminlatency
            
            	If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this is the service\-specific override of the minimum path	latency	general	characterization parameter from	  the	ADSPEC.	   A  return  of  zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecctrlloadmtu
            
            	If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this is	the   service\-specific	 override  of  the composed  Maximum  Transmission  Unit   general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderstatus
            
            	'active' for all active PATH  messages.   This object  may	be  used  to  install  static PATH information or delete PATH information
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: rsvpsenderttl
            
            	The	TTL value in the RSVP header that was last received
            	**type**\: int
            
            	**range:** 0..255
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RSVPMIB.Rsvpsendertable.Rsvpsenderentry, self).__init__()

                self.yang_name = "rsvpSenderEntry"
                self.yang_parent_name = "rsvpSenderTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.rsvpsessionnumber = YLeaf(YType.str, "rsvpSessionNumber")

                self.rsvpsendernumber = YLeaf(YType.int32, "rsvpSenderNumber")

                self.rsvpsendertype = YLeaf(YType.int32, "rsvpSenderType")

                self.rsvpsenderdestaddr = YLeaf(YType.str, "rsvpSenderDestAddr")

                self.rsvpsenderaddr = YLeaf(YType.str, "rsvpSenderAddr")

                self.rsvpsenderdestaddrlength = YLeaf(YType.int32, "rsvpSenderDestAddrLength")

                self.rsvpsenderaddrlength = YLeaf(YType.int32, "rsvpSenderAddrLength")

                self.rsvpsenderprotocol = YLeaf(YType.int32, "rsvpSenderProtocol")

                self.rsvpsenderdestport = YLeaf(YType.str, "rsvpSenderDestPort")

                self.rsvpsenderport = YLeaf(YType.str, "rsvpSenderPort")

                self.rsvpsenderflowid = YLeaf(YType.int32, "rsvpSenderFlowId")

                self.rsvpsenderhopaddr = YLeaf(YType.str, "rsvpSenderHopAddr")

                self.rsvpsenderhoplih = YLeaf(YType.int32, "rsvpSenderHopLih")

                self.rsvpsenderinterface = YLeaf(YType.int32, "rsvpSenderInterface")

                self.rsvpsendertspecrate = YLeaf(YType.int32, "rsvpSenderTSpecRate")

                self.rsvpsendertspecpeakrate = YLeaf(YType.int32, "rsvpSenderTSpecPeakRate")

                self.rsvpsendertspecburst = YLeaf(YType.int32, "rsvpSenderTSpecBurst")

                self.rsvpsendertspecmintu = YLeaf(YType.int32, "rsvpSenderTSpecMinTU")

                self.rsvpsendertspecmaxtu = YLeaf(YType.int32, "rsvpSenderTSpecMaxTU")

                self.rsvpsenderinterval = YLeaf(YType.int32, "rsvpSenderInterval")

                self.rsvpsenderrsvphop = YLeaf(YType.boolean, "rsvpSenderRSVPHop")

                self.rsvpsenderlastchange = YLeaf(YType.uint32, "rsvpSenderLastChange")

                self.rsvpsenderpolicy = YLeaf(YType.str, "rsvpSenderPolicy")

                self.rsvpsenderadspecbreak = YLeaf(YType.boolean, "rsvpSenderAdspecBreak")

                self.rsvpsenderadspechopcount = YLeaf(YType.int32, "rsvpSenderAdspecHopCount")

                self.rsvpsenderadspecpathbw = YLeaf(YType.int32, "rsvpSenderAdspecPathBw")

                self.rsvpsenderadspecminlatency = YLeaf(YType.int32, "rsvpSenderAdspecMinLatency")

                self.rsvpsenderadspecmtu = YLeaf(YType.int32, "rsvpSenderAdspecMtu")

                self.rsvpsenderadspecguaranteedsvc = YLeaf(YType.boolean, "rsvpSenderAdspecGuaranteedSvc")

                self.rsvpsenderadspecguaranteedbreak = YLeaf(YType.boolean, "rsvpSenderAdspecGuaranteedBreak")

                self.rsvpsenderadspecguaranteedctot = YLeaf(YType.int32, "rsvpSenderAdspecGuaranteedCtot")

                self.rsvpsenderadspecguaranteeddtot = YLeaf(YType.int32, "rsvpSenderAdspecGuaranteedDtot")

                self.rsvpsenderadspecguaranteedcsum = YLeaf(YType.int32, "rsvpSenderAdspecGuaranteedCsum")

                self.rsvpsenderadspecguaranteeddsum = YLeaf(YType.int32, "rsvpSenderAdspecGuaranteedDsum")

                self.rsvpsenderadspecguaranteedhopcount = YLeaf(YType.int32, "rsvpSenderAdspecGuaranteedHopCount")

                self.rsvpsenderadspecguaranteedpathbw = YLeaf(YType.int32, "rsvpSenderAdspecGuaranteedPathBw")

                self.rsvpsenderadspecguaranteedminlatency = YLeaf(YType.int32, "rsvpSenderAdspecGuaranteedMinLatency")

                self.rsvpsenderadspecguaranteedmtu = YLeaf(YType.int32, "rsvpSenderAdspecGuaranteedMtu")

                self.rsvpsenderadspecctrlloadsvc = YLeaf(YType.boolean, "rsvpSenderAdspecCtrlLoadSvc")

                self.rsvpsenderadspecctrlloadbreak = YLeaf(YType.boolean, "rsvpSenderAdspecCtrlLoadBreak")

                self.rsvpsenderadspecctrlloadhopcount = YLeaf(YType.int32, "rsvpSenderAdspecCtrlLoadHopCount")

                self.rsvpsenderadspecctrlloadpathbw = YLeaf(YType.int32, "rsvpSenderAdspecCtrlLoadPathBw")

                self.rsvpsenderadspecctrlloadminlatency = YLeaf(YType.int32, "rsvpSenderAdspecCtrlLoadMinLatency")

                self.rsvpsenderadspecctrlloadmtu = YLeaf(YType.int32, "rsvpSenderAdspecCtrlLoadMtu")

                self.rsvpsenderstatus = YLeaf(YType.enumeration, "rsvpSenderStatus")

                self.rsvpsenderttl = YLeaf(YType.int32, "rsvpSenderTTL")
                self._segment_path = lambda: "rsvpSenderEntry" + "[rsvpSessionNumber='" + self.rsvpsessionnumber.get() + "']" + "[rsvpSenderNumber='" + self.rsvpsendernumber.get() + "']"
                self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/rsvpSenderTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RSVPMIB.Rsvpsendertable.Rsvpsenderentry, ['rsvpsessionnumber', 'rsvpsendernumber', 'rsvpsendertype', 'rsvpsenderdestaddr', 'rsvpsenderaddr', 'rsvpsenderdestaddrlength', 'rsvpsenderaddrlength', 'rsvpsenderprotocol', 'rsvpsenderdestport', 'rsvpsenderport', 'rsvpsenderflowid', 'rsvpsenderhopaddr', 'rsvpsenderhoplih', 'rsvpsenderinterface', 'rsvpsendertspecrate', 'rsvpsendertspecpeakrate', 'rsvpsendertspecburst', 'rsvpsendertspecmintu', 'rsvpsendertspecmaxtu', 'rsvpsenderinterval', 'rsvpsenderrsvphop', 'rsvpsenderlastchange', 'rsvpsenderpolicy', 'rsvpsenderadspecbreak', 'rsvpsenderadspechopcount', 'rsvpsenderadspecpathbw', 'rsvpsenderadspecminlatency', 'rsvpsenderadspecmtu', 'rsvpsenderadspecguaranteedsvc', 'rsvpsenderadspecguaranteedbreak', 'rsvpsenderadspecguaranteedctot', 'rsvpsenderadspecguaranteeddtot', 'rsvpsenderadspecguaranteedcsum', 'rsvpsenderadspecguaranteeddsum', 'rsvpsenderadspecguaranteedhopcount', 'rsvpsenderadspecguaranteedpathbw', 'rsvpsenderadspecguaranteedminlatency', 'rsvpsenderadspecguaranteedmtu', 'rsvpsenderadspecctrlloadsvc', 'rsvpsenderadspecctrlloadbreak', 'rsvpsenderadspecctrlloadhopcount', 'rsvpsenderadspecctrlloadpathbw', 'rsvpsenderadspecctrlloadminlatency', 'rsvpsenderadspecctrlloadmtu', 'rsvpsenderstatus', 'rsvpsenderttl'], name, value)


    class Rsvpsenderoutinterfacetable(Entity):
        """
        List of outgoing interfaces	that PATH messages
        use.	 The  ifIndex  is the ifIndex value of the
        egress interface.
        
        .. attribute:: rsvpsenderoutinterfaceentry
        
        	List of outgoing interfaces	that a	particular PATH	message	has
        	**type**\: list of  		 :py:class:`Rsvpsenderoutinterfaceentry <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpsenderoutinterfacetable.Rsvpsenderoutinterfaceentry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RSVPMIB.Rsvpsenderoutinterfacetable, self).__init__()

            self.yang_name = "rsvpSenderOutInterfaceTable"
            self.yang_parent_name = "RSVP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rsvpSenderOutInterfaceEntry" : ("rsvpsenderoutinterfaceentry", RSVPMIB.Rsvpsenderoutinterfacetable.Rsvpsenderoutinterfaceentry)}

            self.rsvpsenderoutinterfaceentry = YList(self)
            self._segment_path = lambda: "rsvpSenderOutInterfaceTable"
            self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RSVPMIB.Rsvpsenderoutinterfacetable, [], name, value)


        class Rsvpsenderoutinterfaceentry(Entity):
            """
            List of outgoing interfaces	that a	particular
            PATH	message	has.
            
            .. attribute:: rsvpsessionnumber  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsessionnumber <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpsessiontable.Rsvpsessionentry>`
            
            .. attribute:: rsvpsendernumber  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsendernumber <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpsendertable.Rsvpsenderentry>`
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: rsvpsenderoutinterfacestatus
            
            	'active' for all active PATH messages
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RSVPMIB.Rsvpsenderoutinterfacetable.Rsvpsenderoutinterfaceentry, self).__init__()

                self.yang_name = "rsvpSenderOutInterfaceEntry"
                self.yang_parent_name = "rsvpSenderOutInterfaceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.rsvpsessionnumber = YLeaf(YType.str, "rsvpSessionNumber")

                self.rsvpsendernumber = YLeaf(YType.str, "rsvpSenderNumber")

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.rsvpsenderoutinterfacestatus = YLeaf(YType.enumeration, "rsvpSenderOutInterfaceStatus")
                self._segment_path = lambda: "rsvpSenderOutInterfaceEntry" + "[rsvpSessionNumber='" + self.rsvpsessionnumber.get() + "']" + "[rsvpSenderNumber='" + self.rsvpsendernumber.get() + "']" + "[ifIndex='" + self.ifindex.get() + "']"
                self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/rsvpSenderOutInterfaceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RSVPMIB.Rsvpsenderoutinterfacetable.Rsvpsenderoutinterfaceentry, ['rsvpsessionnumber', 'rsvpsendernumber', 'ifindex', 'rsvpsenderoutinterfacestatus'], name, value)


    class Rsvpresvtable(Entity):
        """
        Information	describing the	state  information
        displayed by	receivers in RESV messages.
        
        .. attribute:: rsvpresventry
        
        	Information	describing the	state  information displayed  by  a single receiver's RESV message concerning a	single sender
        	**type**\: list of  		 :py:class:`Rsvpresventry <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpresvtable.Rsvpresventry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RSVPMIB.Rsvpresvtable, self).__init__()

            self.yang_name = "rsvpResvTable"
            self.yang_parent_name = "RSVP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rsvpResvEntry" : ("rsvpresventry", RSVPMIB.Rsvpresvtable.Rsvpresventry)}

            self.rsvpresventry = YList(self)
            self._segment_path = lambda: "rsvpResvTable"
            self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RSVPMIB.Rsvpresvtable, [], name, value)


        class Rsvpresventry(Entity):
            """
            Information	describing the	state  information
            displayed  by  a single receiver's RESV message
            concerning a	single sender.
            
            .. attribute:: rsvpsessionnumber  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsessionnumber <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpsessiontable.Rsvpsessionentry>`
            
            .. attribute:: rsvpresvnumber  <key>
            
            	The	number of this reservation request.   This is  for  SNMP Indexing purposes only	and has	no relation to any protocol value
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvtype
            
            	The	type of	session	(IP4, IP6, IP6	with  flow information,	etc)
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: rsvpresvdestaddr
            
            	The	destination address used by all	senders	in this	 session.   This object	may not	be changed when	the  value  of	the  RowStatus	object	is 'active'
            	**type**\: str
            
            	**length:** 4..16
            
            .. attribute:: rsvpresvsenderaddr
            
            	The	source address of the sender  selected	by this	 reservation.	The  value  of	all zeroes indicates 'all senders'.  This object  may  not be  changed	when  the  value  of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 4..16
            
            .. attribute:: rsvpresvdestaddrlength
            
            	The	length of the destination address in bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 0..128
            
            .. attribute:: rsvpresvsenderaddrlength
            
            	The	length of the sender's	address	 in  bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 0..128
            
            .. attribute:: rsvpresvprotocol
            
            	The	IP Protocol used by  this  session.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: rsvpresvdestport
            
            	The	 UDP  or  TCP  port  number  used   as	 a destination	 port  for  all	 senders  in  this session.  If	the IP protocol	in use,	 specified by  rsvpResvProtocol,  is  50 (ESP) or 51 (AH), this	 represents  a	virtual	 destination  port number.   A value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 2..4
            
            .. attribute:: rsvpresvport
            
            	The	UDP or TCP port	number used  as	 a  source port	 for  this sender in this session.  If the IP	 protocol    in	   use,	   specified	by rsvpResvProtocol  is	 50 (ESP) or 51	(AH), this represents a	generalized port identifier (GPI). A  value of zero indicates that the IP protocol in use does not have	ports.	 This  object  may not	be changed when	the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 2..4
            
            .. attribute:: rsvpresvhopaddr
            
            	The	address	used by	the next RSVP  hop  (which may be the ultimate receiver)
            	**type**\: str
            
            	**length:** 4..16
            
            .. attribute:: rsvpresvhoplih
            
            	The	Logical	Interface Handle received from the previous  RSVP  hop	(which may be the ultimate receiver)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: rsvpresvinterface
            
            	The	ifIndex	value of the  interface	 on  which this	RESV message was most recently received
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: rsvpresvservice
            
            	The	QoS Service  classification  requested	by the receiver
            	**type**\:  :py:class:`QosService <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.QosService>`
            
            .. attribute:: rsvpresvtspecrate
            
            	The	Average	Bit  Rate  of  the  sender's  data stream.    Within  a	 transmission  burst,  the arrival   rate    may    be	  as	fast	as rsvpResvTSpecPeakRate   (if	supported  by  the service model); however, averaged across two	or more	 burst	intervals,  the	 rate  should  not exceed rsvpResvTSpecRate.  Note	that this is a prediction, often based	on the	general	 capability  of	a type of codec	or particular encoding;	the measured average  rate may be significantly	lower
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvtspecpeakrate
            
            	The	Peak Bit Rate of the sender's data stream. Traffic  arrival is not expected to exceed this rate	at any time, apart  from  the  effects	of jitter in the network.  If not specified in the TSpec, this returns zero or noSuchValue
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvtspecburst
            
            	The	size of	the largest  burst  expected  from the sender at a time.  If this is less than	 the  sender's	advertised burst  size,	the receiver is	asking the network to provide flow pacing  beyond  what	 would	be provided   under   normal  circumstances.  Such pacing is at	the network's option
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: bytes
            
            .. attribute:: rsvpresvtspecmintu
            
            	The	minimum	message	size for  this	flow.  The policing  algorithm will treat smaller messages as though they are this size
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvtspecmaxtu
            
            	The	maximum	message	size for  this	flow.  The admission  algorithm	 will  reject TSpecs whose Maximum Transmission	Unit, plus  the	 interface headers, exceed the interface MTU
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvrspecrate
            
            	If the requested  service  is  Guaranteed,	as specified   by  rsvpResvService,  this  is  the clearing  rate   that   is	being	requested. Otherwise,  it is zero, or the agent	may return noSuchValue
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvrspecslack
            
            	If the requested  service  is  Guaranteed,	as specified by	rsvpResvService, this is the delay slack.  Otherwise, it is zero, or the agent may return noSuchValue
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpresvinterval
            
            	The	 interval  between  refresh  messages	as advertised by the Next Hop
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvscope
            
            	The	contents of the	scope object, displayed	as an  uninterpreted  string  of octets, including the object header.  In the absence of  such	an object, this	should be of zero length.  If the length  is  non\-zero,	 this  contains	 a series of IP4 or IP6	addresses
            	**type**\: str
            
            	**length:** 0..65536
            
            .. attribute:: rsvpresvshared
            
            	If TRUE, a reservation shared among	senders	is requested.  If FALSE, a reservation specific	to this	sender is requested
            	**type**\: bool
            
            .. attribute:: rsvpresvexplicit
            
            	If TRUE, individual	senders	are  listed  using Filter  Specifications.   If	FALSE, all senders are implicitly selected.  The Scope Object will contain  a list of senders that need	to receive this	reservation request  for  the  purpose	of routing the RESV message
            	**type**\: bool
            
            .. attribute:: rsvpresvrsvphop
            
            	If TRUE, the node believes that  the  previous IP  hop  is	an  RSVP  hop.	If FALSE, the node believes that the previous IP hop may not be	an RSVP	hop
            	**type**\: bool
            
            .. attribute:: rsvpresvlastchange
            
            	The	 time  of  the	 last	change	 in   this reservation	request;  This is either the first time	it was received	or the time  of	 the  most recent change in parameters
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpresvpolicy
            
            	The	contents of the	policy	object,	 displayed as an uninterpreted string of octets, including the object header.  In the absence of  such	an object, this	should be of zero length
            	**type**\: str
            
            	**length:** 0..65536
            
            .. attribute:: rsvpresvstatus
            
            	'active' for all active RESV  messages.   This object  may	be  used  to  install  static RESV information or delete RESV information
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: rsvpresvttl
            
            	The	TTL value in the RSVP header that was last received
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: rsvpresvflowid
            
            	The	flow ID	that this receiver  is	using,	if this	 is  an	IPv6 session
            	**type**\: int
            
            	**range:** 0..16777215
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RSVPMIB.Rsvpresvtable.Rsvpresventry, self).__init__()

                self.yang_name = "rsvpResvEntry"
                self.yang_parent_name = "rsvpResvTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.rsvpsessionnumber = YLeaf(YType.str, "rsvpSessionNumber")

                self.rsvpresvnumber = YLeaf(YType.int32, "rsvpResvNumber")

                self.rsvpresvtype = YLeaf(YType.int32, "rsvpResvType")

                self.rsvpresvdestaddr = YLeaf(YType.str, "rsvpResvDestAddr")

                self.rsvpresvsenderaddr = YLeaf(YType.str, "rsvpResvSenderAddr")

                self.rsvpresvdestaddrlength = YLeaf(YType.int32, "rsvpResvDestAddrLength")

                self.rsvpresvsenderaddrlength = YLeaf(YType.int32, "rsvpResvSenderAddrLength")

                self.rsvpresvprotocol = YLeaf(YType.int32, "rsvpResvProtocol")

                self.rsvpresvdestport = YLeaf(YType.str, "rsvpResvDestPort")

                self.rsvpresvport = YLeaf(YType.str, "rsvpResvPort")

                self.rsvpresvhopaddr = YLeaf(YType.str, "rsvpResvHopAddr")

                self.rsvpresvhoplih = YLeaf(YType.int32, "rsvpResvHopLih")

                self.rsvpresvinterface = YLeaf(YType.int32, "rsvpResvInterface")

                self.rsvpresvservice = YLeaf(YType.enumeration, "rsvpResvService")

                self.rsvpresvtspecrate = YLeaf(YType.int32, "rsvpResvTSpecRate")

                self.rsvpresvtspecpeakrate = YLeaf(YType.int32, "rsvpResvTSpecPeakRate")

                self.rsvpresvtspecburst = YLeaf(YType.int32, "rsvpResvTSpecBurst")

                self.rsvpresvtspecmintu = YLeaf(YType.int32, "rsvpResvTSpecMinTU")

                self.rsvpresvtspecmaxtu = YLeaf(YType.int32, "rsvpResvTSpecMaxTU")

                self.rsvpresvrspecrate = YLeaf(YType.int32, "rsvpResvRSpecRate")

                self.rsvpresvrspecslack = YLeaf(YType.int32, "rsvpResvRSpecSlack")

                self.rsvpresvinterval = YLeaf(YType.int32, "rsvpResvInterval")

                self.rsvpresvscope = YLeaf(YType.str, "rsvpResvScope")

                self.rsvpresvshared = YLeaf(YType.boolean, "rsvpResvShared")

                self.rsvpresvexplicit = YLeaf(YType.boolean, "rsvpResvExplicit")

                self.rsvpresvrsvphop = YLeaf(YType.boolean, "rsvpResvRSVPHop")

                self.rsvpresvlastchange = YLeaf(YType.uint32, "rsvpResvLastChange")

                self.rsvpresvpolicy = YLeaf(YType.str, "rsvpResvPolicy")

                self.rsvpresvstatus = YLeaf(YType.enumeration, "rsvpResvStatus")

                self.rsvpresvttl = YLeaf(YType.int32, "rsvpResvTTL")

                self.rsvpresvflowid = YLeaf(YType.int32, "rsvpResvFlowId")
                self._segment_path = lambda: "rsvpResvEntry" + "[rsvpSessionNumber='" + self.rsvpsessionnumber.get() + "']" + "[rsvpResvNumber='" + self.rsvpresvnumber.get() + "']"
                self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/rsvpResvTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RSVPMIB.Rsvpresvtable.Rsvpresventry, ['rsvpsessionnumber', 'rsvpresvnumber', 'rsvpresvtype', 'rsvpresvdestaddr', 'rsvpresvsenderaddr', 'rsvpresvdestaddrlength', 'rsvpresvsenderaddrlength', 'rsvpresvprotocol', 'rsvpresvdestport', 'rsvpresvport', 'rsvpresvhopaddr', 'rsvpresvhoplih', 'rsvpresvinterface', 'rsvpresvservice', 'rsvpresvtspecrate', 'rsvpresvtspecpeakrate', 'rsvpresvtspecburst', 'rsvpresvtspecmintu', 'rsvpresvtspecmaxtu', 'rsvpresvrspecrate', 'rsvpresvrspecslack', 'rsvpresvinterval', 'rsvpresvscope', 'rsvpresvshared', 'rsvpresvexplicit', 'rsvpresvrsvphop', 'rsvpresvlastchange', 'rsvpresvpolicy', 'rsvpresvstatus', 'rsvpresvttl', 'rsvpresvflowid'], name, value)


    class Rsvpresvfwdtable(Entity):
        """
        Information	describing the	state  information
        displayed upstream in RESV messages.
        
        .. attribute:: rsvpresvfwdentry
        
        	Information	describing the	state  information displayed   upstream	  in   an   RESV   message concerning a	single sender
        	**type**\: list of  		 :py:class:`Rsvpresvfwdentry <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpresvfwdtable.Rsvpresvfwdentry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RSVPMIB.Rsvpresvfwdtable, self).__init__()

            self.yang_name = "rsvpResvFwdTable"
            self.yang_parent_name = "RSVP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rsvpResvFwdEntry" : ("rsvpresvfwdentry", RSVPMIB.Rsvpresvfwdtable.Rsvpresvfwdentry)}

            self.rsvpresvfwdentry = YList(self)
            self._segment_path = lambda: "rsvpResvFwdTable"
            self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RSVPMIB.Rsvpresvfwdtable, [], name, value)


        class Rsvpresvfwdentry(Entity):
            """
            Information	describing the	state  information
            displayed   upstream	  in   an   RESV   message
            concerning a	single sender.
            
            .. attribute:: rsvpsessionnumber  <key>
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsessionnumber <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpsessiontable.Rsvpsessionentry>`
            
            .. attribute:: rsvpresvfwdnumber  <key>
            
            	The	number of this reservation request.   This is  for  SNMP Indexing purposes only	and has	no relation to any protocol value
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvfwdtype
            
            	The	type of	session	(IP4, IP6, IP6	with  flow information,	etc)
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: rsvpresvfwddestaddr
            
            	The	destination address used by all	senders	in this	 session.   This object	may not	be changed when	the  value  of	the  RowStatus	object	is 'active'
            	**type**\: str
            
            	**length:** 4..16
            
            .. attribute:: rsvpresvfwdsenderaddr
            
            	The	source address of the sender  selected	by this	 reservation.	The  value  of	all zeroes indicates 'all senders'.  This object  may  not be  changed	when  the  value  of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 4..16
            
            .. attribute:: rsvpresvfwddestaddrlength
            
            	The	length of the destination address in bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 0..128
            
            .. attribute:: rsvpresvfwdsenderaddrlength
            
            	The	length of the sender's	address	 in  bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 0..128
            
            .. attribute:: rsvpresvfwdprotocol
            
            	The	IP Protocol used by a session. for  secure sessions,  this  indicates  IP  Security.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: rsvpresvfwddestport
            
            	The	 UDP  or  TCP  port  number  used   as	 a destination	 port  for  all	 senders  in  this session.  If	the IP protocol	in use,	 specified by rsvpResvFwdProtocol, is 50 (ESP) or 51 (AH), this	 represents  a	virtual	 destination  port number.   A value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 2..4
            
            .. attribute:: rsvpresvfwdport
            
            	The	UDP or TCP port	number used  as	 a  source port	 for  this sender in this session.  If the IP	 protocol    in	   use,	   specified	by rsvpResvFwdProtocol	is  50	(ESP)  or 51 (AH), this	represents a generalized  port	identifier (GPI).   A  value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 2..4
            
            .. attribute:: rsvpresvfwdhopaddr
            
            	The	address	of the (previous) RSVP	that  will receive this	message
            	**type**\: str
            
            	**length:** 4..16
            
            .. attribute:: rsvpresvfwdhoplih
            
            	The	 Logical  Interface  Handle  sent  to  the (previous)	RSVP   that   will   receive  this message
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: rsvpresvfwdinterface
            
            	The	ifIndex	value of the  interface	 on  which this	RESV message was most recently sent
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: rsvpresvfwdservice
            
            	The	QoS Service classification requested
            	**type**\:  :py:class:`QosService <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.QosService>`
            
            .. attribute:: rsvpresvfwdtspecrate
            
            	The	Average	Bit  Rate  of  the  sender's  data stream.    Within  a	 transmission  burst,  the arrival   rate    may    be	  as	fast	as rsvpResvFwdTSpecPeakRate  (if  supported by the service model); however, averaged across two	or more	 burst	intervals,  the	 rate  should  not exceed rsvpResvFwdTSpecRate.  Note	that this is a prediction, often based	on the	general	 capability  of	a type of codec	or particular encoding;	the measured average  rate may be significantly	lower
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvfwdtspecpeakrate
            
            	The	Peak Bit Rate of the sender's data  stream Traffic  arrival is not expected to exceed this rate	at any time, apart  from  the  effects	of jitter in the network.  If not specified in the TSpec, this returns zero or noSuchValue
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvfwdtspecburst
            
            	The	size of	the largest  burst  expected  from the sender at a time.  If this is less than	 the  sender's	advertised burst  size,	the receiver is	asking the network to provide flow pacing  beyond  what	 would	be provided   under   normal  circumstances.  Such pacing is at	the network's option
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: bytes
            
            .. attribute:: rsvpresvfwdtspecmintu
            
            	The	minimum	message	size for  this	flow.  The policing  algorithm will treat smaller messages as though they are this size
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvfwdtspecmaxtu
            
            	The	maximum	message	size for  this	flow.  The admission  algorithm	 will  reject TSpecs whose Maximum Transmission	Unit, plus  the	 interface headers, exceed the interface MTU
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvfwdrspecrate
            
            	If the requested  service  is  Guaranteed,	as specified   by  rsvpResvService,  this  is  the clearing  rate   that   is	being	requested. Otherwise,  it is zero, or the agent	may return noSuchValue
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: bytes per second
            
            .. attribute:: rsvpresvfwdrspecslack
            
            	If the requested  service  is  Guaranteed,	as specified by	rsvpResvService, this is the delay slack.  Otherwise, it is zero, or the agent may return noSuchValue
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpresvfwdinterval
            
            	The	  interval   between   refresh	  messages advertised to the Previous Hop
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvfwdscope
            
            	The	contents of the	scope object, displayed	as an  uninterpreted  string  of octets, including the object header.  In the absence of  such	an object, this	should be of zero length
            	**type**\: str
            
            	**length:** 0..65536
            
            .. attribute:: rsvpresvfwdshared
            
            	If TRUE, a reservation shared among	senders	is requested.  If FALSE, a reservation specific	to this	sender is requested
            	**type**\: bool
            
            .. attribute:: rsvpresvfwdexplicit
            
            	If TRUE, individual	senders	are  listed  using Filter  Specifications.   If	FALSE, all senders are implicitly selected.  The Scope Object will contain  a list of senders that need	to receive this	reservation request  for  the  purpose	of routing the RESV message
            	**type**\: bool
            
            .. attribute:: rsvpresvfwdrsvphop
            
            	If TRUE, the node believes that  the  next	IP hop	is  an	RSVP  hop.   If	 FALSE,	 the  node believes that the next IP hop  may  not  be	an RSVP	hop
            	**type**\: bool
            
            .. attribute:: rsvpresvfwdlastchange
            
            	The	time of	the last change	in  this  request; This	 is  either  the first time it was sent	or the	time  of  the  most   recent   change	in parameters
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpresvfwdpolicy
            
            	The	contents of the	policy	object,	 displayed as an uninterpreted string of octets, including the object header.  In the absence of  such	an object, this	should be of zero length
            	**type**\: str
            
            	**length:** 0..65536
            
            .. attribute:: rsvpresvfwdstatus
            
            	'active' for all active RESV  messages.   This object may be used to delete	RESV information
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: rsvpresvfwdttl
            
            	The	TTL value in the RSVP header that was last received
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: rsvpresvfwdflowid
            
            	The	flow ID	that this receiver  is	using,	if this	 is  an	IPv6 session
            	**type**\: int
            
            	**range:** 0..16777215
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RSVPMIB.Rsvpresvfwdtable.Rsvpresvfwdentry, self).__init__()

                self.yang_name = "rsvpResvFwdEntry"
                self.yang_parent_name = "rsvpResvFwdTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.rsvpsessionnumber = YLeaf(YType.str, "rsvpSessionNumber")

                self.rsvpresvfwdnumber = YLeaf(YType.int32, "rsvpResvFwdNumber")

                self.rsvpresvfwdtype = YLeaf(YType.int32, "rsvpResvFwdType")

                self.rsvpresvfwddestaddr = YLeaf(YType.str, "rsvpResvFwdDestAddr")

                self.rsvpresvfwdsenderaddr = YLeaf(YType.str, "rsvpResvFwdSenderAddr")

                self.rsvpresvfwddestaddrlength = YLeaf(YType.int32, "rsvpResvFwdDestAddrLength")

                self.rsvpresvfwdsenderaddrlength = YLeaf(YType.int32, "rsvpResvFwdSenderAddrLength")

                self.rsvpresvfwdprotocol = YLeaf(YType.int32, "rsvpResvFwdProtocol")

                self.rsvpresvfwddestport = YLeaf(YType.str, "rsvpResvFwdDestPort")

                self.rsvpresvfwdport = YLeaf(YType.str, "rsvpResvFwdPort")

                self.rsvpresvfwdhopaddr = YLeaf(YType.str, "rsvpResvFwdHopAddr")

                self.rsvpresvfwdhoplih = YLeaf(YType.int32, "rsvpResvFwdHopLih")

                self.rsvpresvfwdinterface = YLeaf(YType.int32, "rsvpResvFwdInterface")

                self.rsvpresvfwdservice = YLeaf(YType.enumeration, "rsvpResvFwdService")

                self.rsvpresvfwdtspecrate = YLeaf(YType.int32, "rsvpResvFwdTSpecRate")

                self.rsvpresvfwdtspecpeakrate = YLeaf(YType.int32, "rsvpResvFwdTSpecPeakRate")

                self.rsvpresvfwdtspecburst = YLeaf(YType.int32, "rsvpResvFwdTSpecBurst")

                self.rsvpresvfwdtspecmintu = YLeaf(YType.int32, "rsvpResvFwdTSpecMinTU")

                self.rsvpresvfwdtspecmaxtu = YLeaf(YType.int32, "rsvpResvFwdTSpecMaxTU")

                self.rsvpresvfwdrspecrate = YLeaf(YType.int32, "rsvpResvFwdRSpecRate")

                self.rsvpresvfwdrspecslack = YLeaf(YType.int32, "rsvpResvFwdRSpecSlack")

                self.rsvpresvfwdinterval = YLeaf(YType.int32, "rsvpResvFwdInterval")

                self.rsvpresvfwdscope = YLeaf(YType.str, "rsvpResvFwdScope")

                self.rsvpresvfwdshared = YLeaf(YType.boolean, "rsvpResvFwdShared")

                self.rsvpresvfwdexplicit = YLeaf(YType.boolean, "rsvpResvFwdExplicit")

                self.rsvpresvfwdrsvphop = YLeaf(YType.boolean, "rsvpResvFwdRSVPHop")

                self.rsvpresvfwdlastchange = YLeaf(YType.uint32, "rsvpResvFwdLastChange")

                self.rsvpresvfwdpolicy = YLeaf(YType.str, "rsvpResvFwdPolicy")

                self.rsvpresvfwdstatus = YLeaf(YType.enumeration, "rsvpResvFwdStatus")

                self.rsvpresvfwdttl = YLeaf(YType.int32, "rsvpResvFwdTTL")

                self.rsvpresvfwdflowid = YLeaf(YType.int32, "rsvpResvFwdFlowId")
                self._segment_path = lambda: "rsvpResvFwdEntry" + "[rsvpSessionNumber='" + self.rsvpsessionnumber.get() + "']" + "[rsvpResvFwdNumber='" + self.rsvpresvfwdnumber.get() + "']"
                self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/rsvpResvFwdTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RSVPMIB.Rsvpresvfwdtable.Rsvpresvfwdentry, ['rsvpsessionnumber', 'rsvpresvfwdnumber', 'rsvpresvfwdtype', 'rsvpresvfwddestaddr', 'rsvpresvfwdsenderaddr', 'rsvpresvfwddestaddrlength', 'rsvpresvfwdsenderaddrlength', 'rsvpresvfwdprotocol', 'rsvpresvfwddestport', 'rsvpresvfwdport', 'rsvpresvfwdhopaddr', 'rsvpresvfwdhoplih', 'rsvpresvfwdinterface', 'rsvpresvfwdservice', 'rsvpresvfwdtspecrate', 'rsvpresvfwdtspecpeakrate', 'rsvpresvfwdtspecburst', 'rsvpresvfwdtspecmintu', 'rsvpresvfwdtspecmaxtu', 'rsvpresvfwdrspecrate', 'rsvpresvfwdrspecslack', 'rsvpresvfwdinterval', 'rsvpresvfwdscope', 'rsvpresvfwdshared', 'rsvpresvfwdexplicit', 'rsvpresvfwdrsvphop', 'rsvpresvfwdlastchange', 'rsvpresvfwdpolicy', 'rsvpresvfwdstatus', 'rsvpresvfwdttl', 'rsvpresvfwdflowid'], name, value)


    class Rsvpiftable(Entity):
        """
        The	RSVP\-specific attributes of  the  system's
        interfaces.
        
        .. attribute:: rsvpifentry
        
        	The	RSVP\-specific attributes of  the  a  given interface
        	**type**\: list of  		 :py:class:`Rsvpifentry <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpiftable.Rsvpifentry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RSVPMIB.Rsvpiftable, self).__init__()

            self.yang_name = "rsvpIfTable"
            self.yang_parent_name = "RSVP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rsvpIfEntry" : ("rsvpifentry", RSVPMIB.Rsvpiftable.Rsvpifentry)}

            self.rsvpifentry = YList(self)
            self._segment_path = lambda: "rsvpIfTable"
            self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RSVPMIB.Rsvpiftable, [], name, value)


        class Rsvpifentry(Entity):
            """
            The	RSVP\-specific attributes of  the  a  given
            interface.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: rsvpifudpnbrs
            
            	The	number of neighbors perceived to be  using only	the RSVP UDP Encapsulation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpifipnbrs
            
            	The	number of neighbors perceived to be  using only	the RSVP IP Encapsulation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpifnbrs
            
            	The	number of neighbors  currently	perceived; this	 will  exceed rsvpIfIpNbrs + rsvpIfUdpNbrs by  the  number   of	  neighbors   using   both encapsulations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpifrefreshblockademultiple
            
            	The	value of the RSVP value	'Kb', Which is the minimum   number   of  refresh  intervals  that blockade state will last once entered
            	**type**\: int
            
            	**range:** 1..65536
            
            .. attribute:: rsvpifrefreshmultiple
            
            	The	value of the RSVP value	'K', which is  the number  of  refresh intervals which must elapse (minimum) before a PATH or RESV  message  which is not being	refreshed will be aged out
            	**type**\: int
            
            	**range:** 1..65536
            
            .. attribute:: rsvpifttl
            
            	The	value of SEND\_TTL used on  this	 interface for	messages  this node originates.	 If set	to zero, the node determines  the  TTL	via  other means
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: rsvpifrefreshinterval
            
            	The	value of the RSVP value	'R', which is  the minimum period between refresh transmissions	of a given PATH	or RESV	message	on an interface
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: rsvpifroutedelay
            
            	The	approximate period from	the time  a  route is  changed	to  the	 time  a resulting message appears on the interface
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**units**\: hundredths	of a second
            
            .. attribute:: rsvpifenabled
            
            	If TRUE, RSVP is enabled  on  this	Interface. If	FALSE,	 RSVP	is  not	 enabled  on  this interface
            	**type**\: bool
            
            .. attribute:: rsvpifudprequired
            
            	If TRUE, manual configuration forces  the  use of  UDP  encapsulation  on  the  interface.	If FALSE,  UDP	encapsulation  is  only	 used	if rsvpIfUdpNbrs is not	zero
            	**type**\: bool
            
            .. attribute:: rsvpifstatus
            
            	'active' on	interfaces that	are configured for RSVP
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RSVPMIB.Rsvpiftable.Rsvpifentry, self).__init__()

                self.yang_name = "rsvpIfEntry"
                self.yang_parent_name = "rsvpIfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.rsvpifudpnbrs = YLeaf(YType.uint32, "rsvpIfUdpNbrs")

                self.rsvpifipnbrs = YLeaf(YType.uint32, "rsvpIfIpNbrs")

                self.rsvpifnbrs = YLeaf(YType.uint32, "rsvpIfNbrs")

                self.rsvpifrefreshblockademultiple = YLeaf(YType.int32, "rsvpIfRefreshBlockadeMultiple")

                self.rsvpifrefreshmultiple = YLeaf(YType.int32, "rsvpIfRefreshMultiple")

                self.rsvpifttl = YLeaf(YType.int32, "rsvpIfTTL")

                self.rsvpifrefreshinterval = YLeaf(YType.int32, "rsvpIfRefreshInterval")

                self.rsvpifroutedelay = YLeaf(YType.int32, "rsvpIfRouteDelay")

                self.rsvpifenabled = YLeaf(YType.boolean, "rsvpIfEnabled")

                self.rsvpifudprequired = YLeaf(YType.boolean, "rsvpIfUdpRequired")

                self.rsvpifstatus = YLeaf(YType.enumeration, "rsvpIfStatus")
                self._segment_path = lambda: "rsvpIfEntry" + "[ifIndex='" + self.ifindex.get() + "']"
                self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/rsvpIfTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RSVPMIB.Rsvpiftable.Rsvpifentry, ['ifindex', 'rsvpifudpnbrs', 'rsvpifipnbrs', 'rsvpifnbrs', 'rsvpifrefreshblockademultiple', 'rsvpifrefreshmultiple', 'rsvpifttl', 'rsvpifrefreshinterval', 'rsvpifroutedelay', 'rsvpifenabled', 'rsvpifudprequired', 'rsvpifstatus'], name, value)


    class Rsvpnbrtable(Entity):
        """
        Information	describing  the	 Neighbors  of	an
        RSVP	system.
        
        .. attribute:: rsvpnbrentry
        
        	Information	  describing   a    single    RSVP Neighbor
        	**type**\: list of  		 :py:class:`Rsvpnbrentry <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.Rsvpnbrtable.Rsvpnbrentry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RSVPMIB.Rsvpnbrtable, self).__init__()

            self.yang_name = "rsvpNbrTable"
            self.yang_parent_name = "RSVP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"rsvpNbrEntry" : ("rsvpnbrentry", RSVPMIB.Rsvpnbrtable.Rsvpnbrentry)}

            self.rsvpnbrentry = YList(self)
            self._segment_path = lambda: "rsvpNbrTable"
            self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(RSVPMIB.Rsvpnbrtable, [], name, value)


        class Rsvpnbrentry(Entity):
            """
            Information	  describing   a    single    RSVP
            Neighbor.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.Iftable.Ifentry>`
            
            .. attribute:: rsvpnbraddress  <key>
            
            	The	IP4 or IP6 Address used	by this	 neighbor. This	 object	 may not be changed when the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 4..16
            
            .. attribute:: rsvpnbrprotocol
            
            	The	  encapsulation	  being	  used	 by   this neighbor
            	**type**\:  :py:class:`RsvpEncapsulation <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpEncapsulation>`
            
            .. attribute:: rsvpnbrstatus
            
            	'active' for all neighbors.	 This  object  may be	used   to  configure  neighbors.   In  the presence   of   configured	 neighbors,    the implementation  may	(but  is  not required to) limit the  set  of  valid  neighbors	 to  those configured
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RSVPMIB.Rsvpnbrtable.Rsvpnbrentry, self).__init__()

                self.yang_name = "rsvpNbrEntry"
                self.yang_parent_name = "rsvpNbrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.rsvpnbraddress = YLeaf(YType.str, "rsvpNbrAddress")

                self.rsvpnbrprotocol = YLeaf(YType.enumeration, "rsvpNbrProtocol")

                self.rsvpnbrstatus = YLeaf(YType.enumeration, "rsvpNbrStatus")
                self._segment_path = lambda: "rsvpNbrEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[rsvpNbrAddress='" + self.rsvpnbraddress.get() + "']"
                self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/rsvpNbrTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(RSVPMIB.Rsvpnbrtable.Rsvpnbrentry, ['ifindex', 'rsvpnbraddress', 'rsvpnbrprotocol', 'rsvpnbrstatus'], name, value)

    def clone_ptr(self):
        self._top_entity = RSVPMIB()
        return self._top_entity

