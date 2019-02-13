""" RSVP_MIB 

The MIB module to describe the RSVP Protocol

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class RsvpEncapsulation(Enum):
    """
    RsvpEncapsulation (Enum Class)

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
    
    	
    	**type**\:  :py:class:`RsvpGenObjects <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpGenObjects>`
    
    	**config**\: False
    
    .. attribute:: rsvpsessiontable
    
    	A table  of	 all  sessions	seen  by  a  given system
    	**type**\:  :py:class:`RsvpSessionTable <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpSessionTable>`
    
    	**config**\: False
    
    .. attribute:: rsvpsendertable
    
    	Information	describing the	state  information displayed by	senders	in PATH	messages
    	**type**\:  :py:class:`RsvpSenderTable <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpSenderTable>`
    
    	**config**\: False
    
    .. attribute:: rsvpsenderoutinterfacetable
    
    	List of outgoing interfaces	that PATH messages use.	 The  ifIndex  is the ifIndex value of the egress interface
    	**type**\:  :py:class:`RsvpSenderOutInterfaceTable <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpSenderOutInterfaceTable>`
    
    	**config**\: False
    
    .. attribute:: rsvpresvtable
    
    	Information	describing the	state  information displayed by	receivers in RESV messages
    	**type**\:  :py:class:`RsvpResvTable <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpResvTable>`
    
    	**config**\: False
    
    .. attribute:: rsvpresvfwdtable
    
    	Information	describing the	state  information displayed upstream in RESV messages
    	**type**\:  :py:class:`RsvpResvFwdTable <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpResvFwdTable>`
    
    	**config**\: False
    
    .. attribute:: rsvpiftable
    
    	The	RSVP\-specific attributes of  the  system's interfaces
    	**type**\:  :py:class:`RsvpIfTable <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpIfTable>`
    
    	**config**\: False
    
    .. attribute:: rsvpnbrtable
    
    	Information	describing  the	 Neighbors  of	an RSVP	system
    	**type**\:  :py:class:`RsvpNbrTable <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpNbrTable>`
    
    	**config**\: False
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("rsvpGenObjects", ("rsvpgenobjects", RSVPMIB.RsvpGenObjects)), ("rsvpSessionTable", ("rsvpsessiontable", RSVPMIB.RsvpSessionTable)), ("rsvpSenderTable", ("rsvpsendertable", RSVPMIB.RsvpSenderTable)), ("rsvpSenderOutInterfaceTable", ("rsvpsenderoutinterfacetable", RSVPMIB.RsvpSenderOutInterfaceTable)), ("rsvpResvTable", ("rsvpresvtable", RSVPMIB.RsvpResvTable)), ("rsvpResvFwdTable", ("rsvpresvfwdtable", RSVPMIB.RsvpResvFwdTable)), ("rsvpIfTable", ("rsvpiftable", RSVPMIB.RsvpIfTable)), ("rsvpNbrTable", ("rsvpnbrtable", RSVPMIB.RsvpNbrTable))])
        self._leafs = OrderedDict()

        self.rsvpgenobjects = RSVPMIB.RsvpGenObjects()
        self.rsvpgenobjects.parent = self
        self._children_name_map["rsvpgenobjects"] = "rsvpGenObjects"

        self.rsvpsessiontable = RSVPMIB.RsvpSessionTable()
        self.rsvpsessiontable.parent = self
        self._children_name_map["rsvpsessiontable"] = "rsvpSessionTable"

        self.rsvpsendertable = RSVPMIB.RsvpSenderTable()
        self.rsvpsendertable.parent = self
        self._children_name_map["rsvpsendertable"] = "rsvpSenderTable"

        self.rsvpsenderoutinterfacetable = RSVPMIB.RsvpSenderOutInterfaceTable()
        self.rsvpsenderoutinterfacetable.parent = self
        self._children_name_map["rsvpsenderoutinterfacetable"] = "rsvpSenderOutInterfaceTable"

        self.rsvpresvtable = RSVPMIB.RsvpResvTable()
        self.rsvpresvtable.parent = self
        self._children_name_map["rsvpresvtable"] = "rsvpResvTable"

        self.rsvpresvfwdtable = RSVPMIB.RsvpResvFwdTable()
        self.rsvpresvfwdtable.parent = self
        self._children_name_map["rsvpresvfwdtable"] = "rsvpResvFwdTable"

        self.rsvpiftable = RSVPMIB.RsvpIfTable()
        self.rsvpiftable.parent = self
        self._children_name_map["rsvpiftable"] = "rsvpIfTable"

        self.rsvpnbrtable = RSVPMIB.RsvpNbrTable()
        self.rsvpnbrtable.parent = self
        self._children_name_map["rsvpnbrtable"] = "rsvpNbrTable"
        self._segment_path = lambda: "RSVP-MIB:RSVP-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(RSVPMIB, [], name, value)


    class RsvpGenObjects(Entity):
        """
        
        
        .. attribute:: rsvpbadpackets
        
        	This object	keeps a	count of the number of bad RSVP	packets	received
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**config**\: False
        
        .. attribute:: rsvpsendernewindex
        
        	This  object  is  used  to	assign	values	to rsvpSenderNumber   as   described  in  'Textual Conventions for SNMPv2'.  The  network  manager reads  the  object,	and  then writes the value back	in the SET that	creates	a new instance	of rsvpSenderEntry.   If  the  SET  fails with the code	'inconsistentValue', then the process must be  repeated;  If  the  SET	succeeds, then the object is incremented, and the new instance	is created according to	the manager's directions
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        .. attribute:: rsvpresvnewindex
        
        	This  object  is  used  to	assign	values	to rsvpResvNumber   as	 described   in	  'Textual Conventions for SNMPv2'.  The  network  manager reads  the  object,	and  then writes the value back	in the SET that	creates	a new instance	of rsvpResvEntry.   If the SET fails with the code 'inconsistentValue',	then the process  must	be repeated;  If the SET succeeds, then	the object is incremented, and the new instance	is created according to	the manager's directions
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        .. attribute:: rsvpresvfwdnewindex
        
        	This  object  is  used  to	assign	values	to rsvpResvFwdNumber   as  described  in  'Textual Conventions for SNMPv2'.  The  network  manager reads  the  object,	and  then writes the value back	in the SET that	creates	a new instance	of rsvpResvFwdEntry.   If  the	SET fails with the code	'inconsistentValue', then the process must be  repeated;  If  the  SET	succeeds, then the object is incremented, and the new instance	is created according to	the manager's directions
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        .. attribute:: rsvpsessionnewindex
        
        	This  object  is  used  to	assign	values	to rsvpSessionNumber   as  described  in  'Textual Conventions for SNMPv2'.  The  network  manager reads  the  object,	and  then writes the value back	in the SET that	creates	a new instance	of rsvpSessionEntry.   If  the	SET fails with the code	'inconsistentValue', then the process must be  repeated;  If  the  SET	succeeds, then the object is incremented, and the new instance	is created according to	the manager's directions
        	**type**\: int
        
        	**range:** 0..2147483647
        
        	**config**\: False
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RSVPMIB.RsvpGenObjects, self).__init__()

            self.yang_name = "rsvpGenObjects"
            self.yang_parent_name = "RSVP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('rsvpbadpackets', (YLeaf(YType.uint32, 'rsvpBadPackets'), ['int'])),
                ('rsvpsendernewindex', (YLeaf(YType.int32, 'rsvpSenderNewIndex'), ['int'])),
                ('rsvpresvnewindex', (YLeaf(YType.int32, 'rsvpResvNewIndex'), ['int'])),
                ('rsvpresvfwdnewindex', (YLeaf(YType.int32, 'rsvpResvFwdNewIndex'), ['int'])),
                ('rsvpsessionnewindex', (YLeaf(YType.int32, 'rsvpSessionNewIndex'), ['int'])),
            ])
            self.rsvpbadpackets = None
            self.rsvpsendernewindex = None
            self.rsvpresvnewindex = None
            self.rsvpresvfwdnewindex = None
            self.rsvpsessionnewindex = None
            self._segment_path = lambda: "rsvpGenObjects"
            self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RSVPMIB.RsvpGenObjects, ['rsvpbadpackets', 'rsvpsendernewindex', 'rsvpresvnewindex', 'rsvpresvfwdnewindex', 'rsvpsessionnewindex'], name, value)



    class RsvpSessionTable(Entity):
        """
        A table  of	 all  sessions	seen  by  a  given
        system.
        
        .. attribute:: rsvpsessionentry
        
        	A single session seen by a given system
        	**type**\: list of  		 :py:class:`RsvpSessionEntry <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpSessionTable.RsvpSessionEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RSVPMIB.RsvpSessionTable, self).__init__()

            self.yang_name = "rsvpSessionTable"
            self.yang_parent_name = "RSVP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rsvpSessionEntry", ("rsvpsessionentry", RSVPMIB.RsvpSessionTable.RsvpSessionEntry))])
            self._leafs = OrderedDict()

            self.rsvpsessionentry = YList(self)
            self._segment_path = lambda: "rsvpSessionTable"
            self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RSVPMIB.RsvpSessionTable, [], name, value)


        class RsvpSessionEntry(Entity):
            """
            A single session seen by a given system.
            
            .. attribute:: rsvpsessionnumber  (key)
            
            	The	number of this session.	 This is for  SNMP Indexing  purposes  only and	has no relation	to any protocol	value
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpsessiontype
            
            	The	type of	session	(IP4, IP6, IP6	with  flow information,	etc)
            	**type**\: int
            
            	**range:** 1..255
            
            	**config**\: False
            
            .. attribute:: rsvpsessiondestaddr
            
            	The	destination address used by all	senders	in this	 session.   This object	may not	be changed when	the  value  of	the  RowStatus	object	is 'active'
            	**type**\: str
            
            	**length:** 4..16
            
            	**config**\: False
            
            .. attribute:: rsvpsessiondestaddrlength
            
            	The	CIDR prefix length of the session address, which   is	32  for	 IP4  host  and	 multicast addresses, and 128  for  IP6	 addresses.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 0..128
            
            	**config**\: False
            
            .. attribute:: rsvpsessionprotocol
            
            	The	IP Protocol used by  this  session.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 1..255
            
            	**config**\: False
            
            .. attribute:: rsvpsessionport
            
            	The	 UDP  or  TCP  port  number  used   as	 a destination	 port  for  all	 senders  in  this session.  If	the IP protocol	in use,	 specified by  rsvpSenderProtocol, is 50 (ESP) or 51 (AH), this	 represents  a	virtual	 destination  port number.   A value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 2..4
            
            	**config**\: False
            
            .. attribute:: rsvpsessionsenders
            
            	The	number of distinct senders currently known to be part of this session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rsvpsessionreceivers
            
            	The	number of reservations being requested	of this	system for this	session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rsvpsessionrequests
            
            	The	number of reservation requests this system is sending upstream for this	session
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RSVPMIB.RsvpSessionTable.RsvpSessionEntry, self).__init__()

                self.yang_name = "rsvpSessionEntry"
                self.yang_parent_name = "rsvpSessionTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rsvpsessionnumber']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rsvpsessionnumber', (YLeaf(YType.int32, 'rsvpSessionNumber'), ['int'])),
                    ('rsvpsessiontype', (YLeaf(YType.int32, 'rsvpSessionType'), ['int'])),
                    ('rsvpsessiondestaddr', (YLeaf(YType.str, 'rsvpSessionDestAddr'), ['str'])),
                    ('rsvpsessiondestaddrlength', (YLeaf(YType.int32, 'rsvpSessionDestAddrLength'), ['int'])),
                    ('rsvpsessionprotocol', (YLeaf(YType.int32, 'rsvpSessionProtocol'), ['int'])),
                    ('rsvpsessionport', (YLeaf(YType.str, 'rsvpSessionPort'), ['str'])),
                    ('rsvpsessionsenders', (YLeaf(YType.uint32, 'rsvpSessionSenders'), ['int'])),
                    ('rsvpsessionreceivers', (YLeaf(YType.uint32, 'rsvpSessionReceivers'), ['int'])),
                    ('rsvpsessionrequests', (YLeaf(YType.uint32, 'rsvpSessionRequests'), ['int'])),
                ])
                self.rsvpsessionnumber = None
                self.rsvpsessiontype = None
                self.rsvpsessiondestaddr = None
                self.rsvpsessiondestaddrlength = None
                self.rsvpsessionprotocol = None
                self.rsvpsessionport = None
                self.rsvpsessionsenders = None
                self.rsvpsessionreceivers = None
                self.rsvpsessionrequests = None
                self._segment_path = lambda: "rsvpSessionEntry" + "[rsvpSessionNumber='" + str(self.rsvpsessionnumber) + "']"
                self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/rsvpSessionTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RSVPMIB.RsvpSessionTable.RsvpSessionEntry, ['rsvpsessionnumber', 'rsvpsessiontype', 'rsvpsessiondestaddr', 'rsvpsessiondestaddrlength', 'rsvpsessionprotocol', 'rsvpsessionport', 'rsvpsessionsenders', 'rsvpsessionreceivers', 'rsvpsessionrequests'], name, value)




    class RsvpSenderTable(Entity):
        """
        Information	describing the	state  information
        displayed by	senders	in PATH	messages.
        
        .. attribute:: rsvpsenderentry
        
        	Information	describing the	state  information displayed by	a single sender's PATH message
        	**type**\: list of  		 :py:class:`RsvpSenderEntry <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpSenderTable.RsvpSenderEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RSVPMIB.RsvpSenderTable, self).__init__()

            self.yang_name = "rsvpSenderTable"
            self.yang_parent_name = "RSVP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rsvpSenderEntry", ("rsvpsenderentry", RSVPMIB.RsvpSenderTable.RsvpSenderEntry))])
            self._leafs = OrderedDict()

            self.rsvpsenderentry = YList(self)
            self._segment_path = lambda: "rsvpSenderTable"
            self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RSVPMIB.RsvpSenderTable, [], name, value)


        class RsvpSenderEntry(Entity):
            """
            Information	describing the	state  information
            displayed by	a single sender's PATH message.
            
            .. attribute:: rsvpsessionnumber  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsessionnumber <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpSessionTable.RsvpSessionEntry>`
            
            	**config**\: False
            
            .. attribute:: rsvpsendernumber  (key)
            
            	The	number of this sender.	This is	 for  SNMP Indexing  purposes  only and	has no relation	to any protocol	value
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpsendertype
            
            	The	type of	session	(IP4, IP6, IP6	with  flow information,	etc)
            	**type**\: int
            
            	**range:** 1..255
            
            	**config**\: False
            
            .. attribute:: rsvpsenderdestaddr
            
            	The	destination address used by all	senders	in this	 session.   This object	may not	be changed when	the  value  of	the  RowStatus	object	is 'active'
            	**type**\: str
            
            	**length:** 4..16
            
            	**config**\: False
            
            .. attribute:: rsvpsenderaddr
            
            	The	source address used by this sender in this session.   This  object may not be changed when the value of	the RowStatus object is	'active'
            	**type**\: str
            
            	**length:** 4..16
            
            	**config**\: False
            
            .. attribute:: rsvpsenderdestaddrlength
            
            	The	length of the destination address in bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 0..128
            
            	**config**\: False
            
            .. attribute:: rsvpsenderaddrlength
            
            	The	length of the sender's	address	 in  bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 0..128
            
            	**config**\: False
            
            .. attribute:: rsvpsenderprotocol
            
            	The	IP Protocol used by  this  session.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 1..255
            
            	**config**\: False
            
            .. attribute:: rsvpsenderdestport
            
            	The	 UDP  or  TCP  port  number  used   as	 a destination	 port  for  all	 senders  in  this session.  If	the IP protocol	in use,	 specified by  rsvpSenderProtocol, is 50 (ESP) or 51 (AH), this	 represents  a	virtual	 destination  port number.   A value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 2..4
            
            	**config**\: False
            
            .. attribute:: rsvpsenderport
            
            	The	UDP or TCP port	number used  as	 a  source port	 for  this sender in this session.  If the IP	 protocol    in	   use,	   specified	by rsvpSenderProtocol is 50 (ESP) or 51	(AH), this represents a	generalized port identifier (GPI). A  value of zero indicates that the IP protocol in use does not have	ports.	 This  object  may not	be changed when	the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 2..4
            
            	**config**\: False
            
            .. attribute:: rsvpsenderflowid
            
            	The	flow ID	that  this  sender  is	using,	if this	 is  an	IPv6 session
            	**type**\: int
            
            	**range:** 0..16777215
            
            	**config**\: False
            
            .. attribute:: rsvpsenderhopaddr
            
            	The	address	used  by  the  previous	 RSVP  hop (which may be the original sender)
            	**type**\: str
            
            	**length:** 4..16
            
            	**config**\: False
            
            .. attribute:: rsvpsenderhoplih
            
            	The	 Logical  Interface  Handle  used  by  the previous  RSVP  hop	(which may be the original sender)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpsenderinterface
            
            	The	ifIndex	value of the  interface	 on  which this	PATH message was most recently received
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpsendertspecrate
            
            	The	Average	Bit  Rate  of  the  sender's  data stream.    Within  a	 transmission  burst,  the arrival   rate    may    be	  as	fast	as rsvpSenderTSpecPeakRate  (if	 supported  by the service model); however, averaged across two	or more	 burst	intervals,  the	 rate  should  not exceed rsvpSenderTSpecRate.  Note	that this is a prediction, often based	on the	general	 capability  of	a type of codec	or particular encoding;	the measured average  rate may be significantly	lower
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsendertspecpeakrate
            
            	The	Peak Bit Rate of the sender's data stream. Traffic  arrival is not expected to exceed this rate	at any time, apart  from  the  effects	of jitter in the network.  If not specified in the TSpec, this returns zero or noSuchValue
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsendertspecburst
            
            	The	size of	the largest  burst  expected  from the sender at a time
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: rsvpsendertspecmintu
            
            	The	minimum	message	size for  this	flow.  The policing  algorithm will treat smaller messages as though they are this size
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpsendertspecmaxtu
            
            	The	maximum	message	size for  this	flow.  The admission  algorithm	 will  reject TSpecs whose Maximum Transmission	Unit, plus  the	 interface headers, exceed the interface MTU
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpsenderinterval
            
            	The	 interval  between  refresh  messages	as advertised by the Previous Hop
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpsenderrsvphop
            
            	If TRUE, the node believes that  the  previous IP  hop  is	an  RSVP  hop.	If FALSE, the node believes that the previous IP hop may not be	an RSVP	hop
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rsvpsenderlastchange
            
            	The	time of	 the  last  change  in	this  PATH message;  This  is either the first time it was received or the time	of the most recent  change in parameters
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rsvpsenderpolicy
            
            	The	contents of the	policy	object,	 displayed as an uninterpreted string of octets, including the object header.  In the absence of  such	an object, this	should be of zero length
            	**type**\: str
            
            	**length:** 4..65536
            
            	**config**\: False
            
            .. attribute:: rsvpsenderadspecbreak
            
            	The	global break bit general  characterization parameter  from  the	ADSPEC.	 If TRUE, at least one non\-IS hop was detected in  the	path.	If FALSE, no non\-IS hops were detected
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rsvpsenderadspechopcount
            
            	The	  hop	count	general	  characterization parameter from the ADSPEC.  A return	of zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: rsvpsenderadspecpathbw
            
            	The	  path	  bandwidth    estimate	   general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsenderadspecminlatency
            
            	The	   minimum    path     latency	   general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecmtu
            
            	The	composed Maximum Transmission Unit general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderadspecguaranteedsvc
            
            	If TRUE,  the  ADSPEC  contains  a	Guaranteed Service  fragment.	If  FALSE, the ADSPEC does not contain a Guaranteed Service fragment
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rsvpsenderadspecguaranteedbreak
            
            	If TRUE, the Guaranteed Service  fragment  has its	'break'	 bit  set,  indicating that one	or more	nodes along the	path do	 not  support  the guaranteed	  service.     If    FALSE,    and rsvpSenderAdspecGuaranteedSvc  is   TRUE,   the 'break' bit is not set.  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns FALSE or noSuchValue
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rsvpsenderadspecguaranteedctot
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the  end\-to\-end	 composed  value  for  the guaranteed service 'C' parameter.  A	return	of zero	  or  noSuchValue  indicates  one  of  the following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderadspecguaranteeddtot
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the  end\-to\-end	 composed  value  for  the guaranteed service 'D' parameter.  A	return	of zero	  or  noSuchValue  indicates  one  of  the following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecguaranteedcsum
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the  composed  value  for  the	guaranteed service 'C' parameter since the last	 reshaping point.    A	 return	 of  zero  or  noSuchValue indicates one of the	following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderadspecguaranteeddsum
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the  composed  value  for  the	guaranteed service 'D' parameter since the last	 reshaping point.    A	 return	 of  zero  or  noSuchValue indicates one of the	following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecguaranteedhopcount
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is  the  service\-specific  override	of the hop count general characterization  parameter  from the	ADSPEC.	  A  return of zero or noSuchValue indicates one of the	following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: rsvpsenderadspecguaranteedpathbw
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is  the  service\-specific  override of the path bandwidth  estimate	general	  characterization parameter from the ADSPEC.  A return	of zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsenderadspecguaranteedminlatency
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is the service\-specific override of the minimum path	latency	general	characterization parameter from	  the	ADSPEC.	   A  return  of  zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecguaranteedmtu
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the   service\-specific	 override  of  the composed  Maximum  Transmission  Unit   general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderadspecctrlloadsvc
            
            	If TRUE, the ADSPEC	contains a Controlled Load Service  fragment.	If  FALSE, the ADSPEC does not	 contain   a   Controlled   Load   Service fragment
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rsvpsenderadspecctrlloadbreak
            
            	If TRUE, the Controlled Load Service  fragment has its 'break' bit set, indicating that one	or more	nodes along the	path do	 not  support  the controlled	load   service.	   If  FALSE,  and rsvpSenderAdspecCtrlLoadSvc	 is   TRUE,    the 'break' bit is not set.  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns FALSE or noSuchValue
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rsvpsenderadspecctrlloadhopcount
            
            	If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this is  the  service\-specific  override	of the hop count general characterization  parameter  from the	ADSPEC.	  A  return of zero or noSuchValue indicates one of the	following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            .. attribute:: rsvpsenderadspecctrlloadpathbw
            
            	If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this is  the  service\-specific  override of the path bandwidth  estimate	general	  characterization parameter from the ADSPEC.  A return	of zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsenderadspecctrlloadminlatency
            
            	If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this is the service\-specific override of the minimum path	latency	general	characterization parameter from	  the	ADSPEC.	   A  return  of  zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecctrlloadmtu
            
            	If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this is	the   service\-specific	 override  of  the composed  Maximum  Transmission  Unit   general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns zero	or noSuchValue
            	**type**\: int
            
            	**range:** 0..65535
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderstatus
            
            	'active' for all active PATH  messages.   This object  may	be  used  to  install  static PATH information or delete PATH information
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: rsvpsenderttl
            
            	The	TTL value in the RSVP header that was last received
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RSVPMIB.RsvpSenderTable.RsvpSenderEntry, self).__init__()

                self.yang_name = "rsvpSenderEntry"
                self.yang_parent_name = "rsvpSenderTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rsvpsessionnumber','rsvpsendernumber']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rsvpsessionnumber', (YLeaf(YType.str, 'rsvpSessionNumber'), ['int'])),
                    ('rsvpsendernumber', (YLeaf(YType.int32, 'rsvpSenderNumber'), ['int'])),
                    ('rsvpsendertype', (YLeaf(YType.int32, 'rsvpSenderType'), ['int'])),
                    ('rsvpsenderdestaddr', (YLeaf(YType.str, 'rsvpSenderDestAddr'), ['str'])),
                    ('rsvpsenderaddr', (YLeaf(YType.str, 'rsvpSenderAddr'), ['str'])),
                    ('rsvpsenderdestaddrlength', (YLeaf(YType.int32, 'rsvpSenderDestAddrLength'), ['int'])),
                    ('rsvpsenderaddrlength', (YLeaf(YType.int32, 'rsvpSenderAddrLength'), ['int'])),
                    ('rsvpsenderprotocol', (YLeaf(YType.int32, 'rsvpSenderProtocol'), ['int'])),
                    ('rsvpsenderdestport', (YLeaf(YType.str, 'rsvpSenderDestPort'), ['str'])),
                    ('rsvpsenderport', (YLeaf(YType.str, 'rsvpSenderPort'), ['str'])),
                    ('rsvpsenderflowid', (YLeaf(YType.int32, 'rsvpSenderFlowId'), ['int'])),
                    ('rsvpsenderhopaddr', (YLeaf(YType.str, 'rsvpSenderHopAddr'), ['str'])),
                    ('rsvpsenderhoplih', (YLeaf(YType.int32, 'rsvpSenderHopLih'), ['int'])),
                    ('rsvpsenderinterface', (YLeaf(YType.int32, 'rsvpSenderInterface'), ['int'])),
                    ('rsvpsendertspecrate', (YLeaf(YType.int32, 'rsvpSenderTSpecRate'), ['int'])),
                    ('rsvpsendertspecpeakrate', (YLeaf(YType.int32, 'rsvpSenderTSpecPeakRate'), ['int'])),
                    ('rsvpsendertspecburst', (YLeaf(YType.int32, 'rsvpSenderTSpecBurst'), ['int'])),
                    ('rsvpsendertspecmintu', (YLeaf(YType.int32, 'rsvpSenderTSpecMinTU'), ['int'])),
                    ('rsvpsendertspecmaxtu', (YLeaf(YType.int32, 'rsvpSenderTSpecMaxTU'), ['int'])),
                    ('rsvpsenderinterval', (YLeaf(YType.int32, 'rsvpSenderInterval'), ['int'])),
                    ('rsvpsenderrsvphop', (YLeaf(YType.boolean, 'rsvpSenderRSVPHop'), ['bool'])),
                    ('rsvpsenderlastchange', (YLeaf(YType.uint32, 'rsvpSenderLastChange'), ['int'])),
                    ('rsvpsenderpolicy', (YLeaf(YType.str, 'rsvpSenderPolicy'), ['str'])),
                    ('rsvpsenderadspecbreak', (YLeaf(YType.boolean, 'rsvpSenderAdspecBreak'), ['bool'])),
                    ('rsvpsenderadspechopcount', (YLeaf(YType.int32, 'rsvpSenderAdspecHopCount'), ['int'])),
                    ('rsvpsenderadspecpathbw', (YLeaf(YType.int32, 'rsvpSenderAdspecPathBw'), ['int'])),
                    ('rsvpsenderadspecminlatency', (YLeaf(YType.int32, 'rsvpSenderAdspecMinLatency'), ['int'])),
                    ('rsvpsenderadspecmtu', (YLeaf(YType.int32, 'rsvpSenderAdspecMtu'), ['int'])),
                    ('rsvpsenderadspecguaranteedsvc', (YLeaf(YType.boolean, 'rsvpSenderAdspecGuaranteedSvc'), ['bool'])),
                    ('rsvpsenderadspecguaranteedbreak', (YLeaf(YType.boolean, 'rsvpSenderAdspecGuaranteedBreak'), ['bool'])),
                    ('rsvpsenderadspecguaranteedctot', (YLeaf(YType.int32, 'rsvpSenderAdspecGuaranteedCtot'), ['int'])),
                    ('rsvpsenderadspecguaranteeddtot', (YLeaf(YType.int32, 'rsvpSenderAdspecGuaranteedDtot'), ['int'])),
                    ('rsvpsenderadspecguaranteedcsum', (YLeaf(YType.int32, 'rsvpSenderAdspecGuaranteedCsum'), ['int'])),
                    ('rsvpsenderadspecguaranteeddsum', (YLeaf(YType.int32, 'rsvpSenderAdspecGuaranteedDsum'), ['int'])),
                    ('rsvpsenderadspecguaranteedhopcount', (YLeaf(YType.int32, 'rsvpSenderAdspecGuaranteedHopCount'), ['int'])),
                    ('rsvpsenderadspecguaranteedpathbw', (YLeaf(YType.int32, 'rsvpSenderAdspecGuaranteedPathBw'), ['int'])),
                    ('rsvpsenderadspecguaranteedminlatency', (YLeaf(YType.int32, 'rsvpSenderAdspecGuaranteedMinLatency'), ['int'])),
                    ('rsvpsenderadspecguaranteedmtu', (YLeaf(YType.int32, 'rsvpSenderAdspecGuaranteedMtu'), ['int'])),
                    ('rsvpsenderadspecctrlloadsvc', (YLeaf(YType.boolean, 'rsvpSenderAdspecCtrlLoadSvc'), ['bool'])),
                    ('rsvpsenderadspecctrlloadbreak', (YLeaf(YType.boolean, 'rsvpSenderAdspecCtrlLoadBreak'), ['bool'])),
                    ('rsvpsenderadspecctrlloadhopcount', (YLeaf(YType.int32, 'rsvpSenderAdspecCtrlLoadHopCount'), ['int'])),
                    ('rsvpsenderadspecctrlloadpathbw', (YLeaf(YType.int32, 'rsvpSenderAdspecCtrlLoadPathBw'), ['int'])),
                    ('rsvpsenderadspecctrlloadminlatency', (YLeaf(YType.int32, 'rsvpSenderAdspecCtrlLoadMinLatency'), ['int'])),
                    ('rsvpsenderadspecctrlloadmtu', (YLeaf(YType.int32, 'rsvpSenderAdspecCtrlLoadMtu'), ['int'])),
                    ('rsvpsenderstatus', (YLeaf(YType.enumeration, 'rsvpSenderStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('rsvpsenderttl', (YLeaf(YType.int32, 'rsvpSenderTTL'), ['int'])),
                ])
                self.rsvpsessionnumber = None
                self.rsvpsendernumber = None
                self.rsvpsendertype = None
                self.rsvpsenderdestaddr = None
                self.rsvpsenderaddr = None
                self.rsvpsenderdestaddrlength = None
                self.rsvpsenderaddrlength = None
                self.rsvpsenderprotocol = None
                self.rsvpsenderdestport = None
                self.rsvpsenderport = None
                self.rsvpsenderflowid = None
                self.rsvpsenderhopaddr = None
                self.rsvpsenderhoplih = None
                self.rsvpsenderinterface = None
                self.rsvpsendertspecrate = None
                self.rsvpsendertspecpeakrate = None
                self.rsvpsendertspecburst = None
                self.rsvpsendertspecmintu = None
                self.rsvpsendertspecmaxtu = None
                self.rsvpsenderinterval = None
                self.rsvpsenderrsvphop = None
                self.rsvpsenderlastchange = None
                self.rsvpsenderpolicy = None
                self.rsvpsenderadspecbreak = None
                self.rsvpsenderadspechopcount = None
                self.rsvpsenderadspecpathbw = None
                self.rsvpsenderadspecminlatency = None
                self.rsvpsenderadspecmtu = None
                self.rsvpsenderadspecguaranteedsvc = None
                self.rsvpsenderadspecguaranteedbreak = None
                self.rsvpsenderadspecguaranteedctot = None
                self.rsvpsenderadspecguaranteeddtot = None
                self.rsvpsenderadspecguaranteedcsum = None
                self.rsvpsenderadspecguaranteeddsum = None
                self.rsvpsenderadspecguaranteedhopcount = None
                self.rsvpsenderadspecguaranteedpathbw = None
                self.rsvpsenderadspecguaranteedminlatency = None
                self.rsvpsenderadspecguaranteedmtu = None
                self.rsvpsenderadspecctrlloadsvc = None
                self.rsvpsenderadspecctrlloadbreak = None
                self.rsvpsenderadspecctrlloadhopcount = None
                self.rsvpsenderadspecctrlloadpathbw = None
                self.rsvpsenderadspecctrlloadminlatency = None
                self.rsvpsenderadspecctrlloadmtu = None
                self.rsvpsenderstatus = None
                self.rsvpsenderttl = None
                self._segment_path = lambda: "rsvpSenderEntry" + "[rsvpSessionNumber='" + str(self.rsvpsessionnumber) + "']" + "[rsvpSenderNumber='" + str(self.rsvpsendernumber) + "']"
                self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/rsvpSenderTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RSVPMIB.RsvpSenderTable.RsvpSenderEntry, ['rsvpsessionnumber', 'rsvpsendernumber', 'rsvpsendertype', 'rsvpsenderdestaddr', 'rsvpsenderaddr', 'rsvpsenderdestaddrlength', 'rsvpsenderaddrlength', 'rsvpsenderprotocol', 'rsvpsenderdestport', 'rsvpsenderport', 'rsvpsenderflowid', 'rsvpsenderhopaddr', 'rsvpsenderhoplih', 'rsvpsenderinterface', 'rsvpsendertspecrate', 'rsvpsendertspecpeakrate', 'rsvpsendertspecburst', 'rsvpsendertspecmintu', 'rsvpsendertspecmaxtu', 'rsvpsenderinterval', 'rsvpsenderrsvphop', 'rsvpsenderlastchange', 'rsvpsenderpolicy', 'rsvpsenderadspecbreak', 'rsvpsenderadspechopcount', 'rsvpsenderadspecpathbw', 'rsvpsenderadspecminlatency', 'rsvpsenderadspecmtu', 'rsvpsenderadspecguaranteedsvc', 'rsvpsenderadspecguaranteedbreak', 'rsvpsenderadspecguaranteedctot', 'rsvpsenderadspecguaranteeddtot', 'rsvpsenderadspecguaranteedcsum', 'rsvpsenderadspecguaranteeddsum', 'rsvpsenderadspecguaranteedhopcount', 'rsvpsenderadspecguaranteedpathbw', 'rsvpsenderadspecguaranteedminlatency', 'rsvpsenderadspecguaranteedmtu', 'rsvpsenderadspecctrlloadsvc', 'rsvpsenderadspecctrlloadbreak', 'rsvpsenderadspecctrlloadhopcount', 'rsvpsenderadspecctrlloadpathbw', 'rsvpsenderadspecctrlloadminlatency', 'rsvpsenderadspecctrlloadmtu', 'rsvpsenderstatus', 'rsvpsenderttl'], name, value)




    class RsvpSenderOutInterfaceTable(Entity):
        """
        List of outgoing interfaces	that PATH messages
        use.	 The  ifIndex  is the ifIndex value of the
        egress interface.
        
        .. attribute:: rsvpsenderoutinterfaceentry
        
        	List of outgoing interfaces	that a	particular PATH	message	has
        	**type**\: list of  		 :py:class:`RsvpSenderOutInterfaceEntry <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpSenderOutInterfaceTable.RsvpSenderOutInterfaceEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RSVPMIB.RsvpSenderOutInterfaceTable, self).__init__()

            self.yang_name = "rsvpSenderOutInterfaceTable"
            self.yang_parent_name = "RSVP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rsvpSenderOutInterfaceEntry", ("rsvpsenderoutinterfaceentry", RSVPMIB.RsvpSenderOutInterfaceTable.RsvpSenderOutInterfaceEntry))])
            self._leafs = OrderedDict()

            self.rsvpsenderoutinterfaceentry = YList(self)
            self._segment_path = lambda: "rsvpSenderOutInterfaceTable"
            self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RSVPMIB.RsvpSenderOutInterfaceTable, [], name, value)


        class RsvpSenderOutInterfaceEntry(Entity):
            """
            List of outgoing interfaces	that a	particular
            PATH	message	has.
            
            .. attribute:: rsvpsessionnumber  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsessionnumber <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpSessionTable.RsvpSessionEntry>`
            
            	**config**\: False
            
            .. attribute:: rsvpsendernumber  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsendernumber <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpSenderTable.RsvpSenderEntry>`
            
            	**config**\: False
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: rsvpsenderoutinterfacestatus
            
            	'active' for all active PATH messages
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RSVPMIB.RsvpSenderOutInterfaceTable.RsvpSenderOutInterfaceEntry, self).__init__()

                self.yang_name = "rsvpSenderOutInterfaceEntry"
                self.yang_parent_name = "rsvpSenderOutInterfaceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rsvpsessionnumber','rsvpsendernumber','ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rsvpsessionnumber', (YLeaf(YType.str, 'rsvpSessionNumber'), ['int'])),
                    ('rsvpsendernumber', (YLeaf(YType.str, 'rsvpSenderNumber'), ['int'])),
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('rsvpsenderoutinterfacestatus', (YLeaf(YType.enumeration, 'rsvpSenderOutInterfaceStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.rsvpsessionnumber = None
                self.rsvpsendernumber = None
                self.ifindex = None
                self.rsvpsenderoutinterfacestatus = None
                self._segment_path = lambda: "rsvpSenderOutInterfaceEntry" + "[rsvpSessionNumber='" + str(self.rsvpsessionnumber) + "']" + "[rsvpSenderNumber='" + str(self.rsvpsendernumber) + "']" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/rsvpSenderOutInterfaceTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RSVPMIB.RsvpSenderOutInterfaceTable.RsvpSenderOutInterfaceEntry, ['rsvpsessionnumber', 'rsvpsendernumber', 'ifindex', 'rsvpsenderoutinterfacestatus'], name, value)




    class RsvpResvTable(Entity):
        """
        Information	describing the	state  information
        displayed by	receivers in RESV messages.
        
        .. attribute:: rsvpresventry
        
        	Information	describing the	state  information displayed  by  a single receiver's RESV message concerning a	single sender
        	**type**\: list of  		 :py:class:`RsvpResvEntry <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpResvTable.RsvpResvEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RSVPMIB.RsvpResvTable, self).__init__()

            self.yang_name = "rsvpResvTable"
            self.yang_parent_name = "RSVP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rsvpResvEntry", ("rsvpresventry", RSVPMIB.RsvpResvTable.RsvpResvEntry))])
            self._leafs = OrderedDict()

            self.rsvpresventry = YList(self)
            self._segment_path = lambda: "rsvpResvTable"
            self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RSVPMIB.RsvpResvTable, [], name, value)


        class RsvpResvEntry(Entity):
            """
            Information	describing the	state  information
            displayed  by  a single receiver's RESV message
            concerning a	single sender.
            
            .. attribute:: rsvpsessionnumber  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsessionnumber <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpSessionTable.RsvpSessionEntry>`
            
            	**config**\: False
            
            .. attribute:: rsvpresvnumber  (key)
            
            	The	number of this reservation request.   This is  for  SNMP Indexing purposes only	and has	no relation to any protocol value
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpresvtype
            
            	The	type of	session	(IP4, IP6, IP6	with  flow information,	etc)
            	**type**\: int
            
            	**range:** 1..255
            
            	**config**\: False
            
            .. attribute:: rsvpresvdestaddr
            
            	The	destination address used by all	senders	in this	 session.   This object	may not	be changed when	the  value  of	the  RowStatus	object	is 'active'
            	**type**\: str
            
            	**length:** 4..16
            
            	**config**\: False
            
            .. attribute:: rsvpresvsenderaddr
            
            	The	source address of the sender  selected	by this	 reservation.	The  value  of	all zeroes indicates 'all senders'.  This object  may  not be  changed	when  the  value  of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 4..16
            
            	**config**\: False
            
            .. attribute:: rsvpresvdestaddrlength
            
            	The	length of the destination address in bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 0..128
            
            	**config**\: False
            
            .. attribute:: rsvpresvsenderaddrlength
            
            	The	length of the sender's	address	 in  bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 0..128
            
            	**config**\: False
            
            .. attribute:: rsvpresvprotocol
            
            	The	IP Protocol used by  this  session.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 1..255
            
            	**config**\: False
            
            .. attribute:: rsvpresvdestport
            
            	The	 UDP  or  TCP  port  number  used   as	 a destination	 port  for  all	 senders  in  this session.  If	the IP protocol	in use,	 specified by  rsvpResvProtocol,  is  50 (ESP) or 51 (AH), this	 represents  a	virtual	 destination  port number.   A value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 2..4
            
            	**config**\: False
            
            .. attribute:: rsvpresvport
            
            	The	UDP or TCP port	number used  as	 a  source port	 for  this sender in this session.  If the IP	 protocol    in	   use,	   specified	by rsvpResvProtocol  is	 50 (ESP) or 51	(AH), this represents a	generalized port identifier (GPI). A  value of zero indicates that the IP protocol in use does not have	ports.	 This  object  may not	be changed when	the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 2..4
            
            	**config**\: False
            
            .. attribute:: rsvpresvhopaddr
            
            	The	address	used by	the next RSVP  hop  (which may be the ultimate receiver)
            	**type**\: str
            
            	**length:** 4..16
            
            	**config**\: False
            
            .. attribute:: rsvpresvhoplih
            
            	The	Logical	Interface Handle received from the previous  RSVP  hop	(which may be the ultimate receiver)
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpresvinterface
            
            	The	ifIndex	value of the  interface	 on  which this	RESV message was most recently received
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpresvservice
            
            	The	QoS Service  classification  requested	by the receiver
            	**type**\:  :py:class:`QosService <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.QosService>`
            
            	**config**\: False
            
            .. attribute:: rsvpresvtspecrate
            
            	The	Average	Bit  Rate  of  the  sender's  data stream.    Within  a	 transmission  burst,  the arrival   rate    may    be	  as	fast	as rsvpResvTSpecPeakRate   (if	supported  by  the service model); however, averaged across two	or more	 burst	intervals,  the	 rate  should  not exceed rsvpResvTSpecRate.  Note	that this is a prediction, often based	on the	general	 capability  of	a type of codec	or particular encoding;	the measured average  rate may be significantly	lower
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvtspecpeakrate
            
            	The	Peak Bit Rate of the sender's data stream. Traffic  arrival is not expected to exceed this rate	at any time, apart  from  the  effects	of jitter in the network.  If not specified in the TSpec, this returns zero or noSuchValue
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvtspecburst
            
            	The	size of	the largest  burst  expected  from the sender at a time.  If this is less than	 the  sender's	advertised burst  size,	the receiver is	asking the network to provide flow pacing  beyond  what	 would	be provided   under   normal  circumstances.  Such pacing is at	the network's option
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: rsvpresvtspecmintu
            
            	The	minimum	message	size for  this	flow.  The policing  algorithm will treat smaller messages as though they are this size
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpresvtspecmaxtu
            
            	The	maximum	message	size for  this	flow.  The admission  algorithm	 will  reject TSpecs whose Maximum Transmission	Unit, plus  the	 interface headers, exceed the interface MTU
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpresvrspecrate
            
            	If the requested  service  is  Guaranteed,	as specified   by  rsvpResvService,  this  is  the clearing  rate   that   is	being	requested. Otherwise,  it is zero, or the agent	may return noSuchValue
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvrspecslack
            
            	If the requested  service  is  Guaranteed,	as specified by	rsvpResvService, this is the delay slack.  Otherwise, it is zero, or the agent may return noSuchValue
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: microseconds
            
            .. attribute:: rsvpresvinterval
            
            	The	 interval  between  refresh  messages	as advertised by the Next Hop
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpresvscope
            
            	The	contents of the	scope object, displayed	as an  uninterpreted  string  of octets, including the object header.  In the absence of  such	an object, this	should be of zero length.  If the length  is  non\-zero,	 this  contains	 a series of IP4 or IP6	addresses
            	**type**\: str
            
            	**length:** 0..65536
            
            	**config**\: False
            
            .. attribute:: rsvpresvshared
            
            	If TRUE, a reservation shared among	senders	is requested.  If FALSE, a reservation specific	to this	sender is requested
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rsvpresvexplicit
            
            	If TRUE, individual	senders	are  listed  using Filter  Specifications.   If	FALSE, all senders are implicitly selected.  The Scope Object will contain  a list of senders that need	to receive this	reservation request  for  the  purpose	of routing the RESV message
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rsvpresvrsvphop
            
            	If TRUE, the node believes that  the  previous IP  hop  is	an  RSVP  hop.	If FALSE, the node believes that the previous IP hop may not be	an RSVP	hop
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rsvpresvlastchange
            
            	The	 time  of  the	 last	change	 in   this reservation	request;  This is either the first time	it was received	or the time  of	 the  most recent change in parameters
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rsvpresvpolicy
            
            	The	contents of the	policy	object,	 displayed as an uninterpreted string of octets, including the object header.  In the absence of  such	an object, this	should be of zero length
            	**type**\: str
            
            	**length:** 0..65536
            
            	**config**\: False
            
            .. attribute:: rsvpresvstatus
            
            	'active' for all active RESV  messages.   This object  may	be  used  to  install  static RESV information or delete RESV information
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: rsvpresvttl
            
            	The	TTL value in the RSVP header that was last received
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: rsvpresvflowid
            
            	The	flow ID	that this receiver  is	using,	if this	 is  an	IPv6 session
            	**type**\: int
            
            	**range:** 0..16777215
            
            	**config**\: False
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RSVPMIB.RsvpResvTable.RsvpResvEntry, self).__init__()

                self.yang_name = "rsvpResvEntry"
                self.yang_parent_name = "rsvpResvTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rsvpsessionnumber','rsvpresvnumber']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rsvpsessionnumber', (YLeaf(YType.str, 'rsvpSessionNumber'), ['int'])),
                    ('rsvpresvnumber', (YLeaf(YType.int32, 'rsvpResvNumber'), ['int'])),
                    ('rsvpresvtype', (YLeaf(YType.int32, 'rsvpResvType'), ['int'])),
                    ('rsvpresvdestaddr', (YLeaf(YType.str, 'rsvpResvDestAddr'), ['str'])),
                    ('rsvpresvsenderaddr', (YLeaf(YType.str, 'rsvpResvSenderAddr'), ['str'])),
                    ('rsvpresvdestaddrlength', (YLeaf(YType.int32, 'rsvpResvDestAddrLength'), ['int'])),
                    ('rsvpresvsenderaddrlength', (YLeaf(YType.int32, 'rsvpResvSenderAddrLength'), ['int'])),
                    ('rsvpresvprotocol', (YLeaf(YType.int32, 'rsvpResvProtocol'), ['int'])),
                    ('rsvpresvdestport', (YLeaf(YType.str, 'rsvpResvDestPort'), ['str'])),
                    ('rsvpresvport', (YLeaf(YType.str, 'rsvpResvPort'), ['str'])),
                    ('rsvpresvhopaddr', (YLeaf(YType.str, 'rsvpResvHopAddr'), ['str'])),
                    ('rsvpresvhoplih', (YLeaf(YType.int32, 'rsvpResvHopLih'), ['int'])),
                    ('rsvpresvinterface', (YLeaf(YType.int32, 'rsvpResvInterface'), ['int'])),
                    ('rsvpresvservice', (YLeaf(YType.enumeration, 'rsvpResvService'), [('ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB', 'QosService', '')])),
                    ('rsvpresvtspecrate', (YLeaf(YType.int32, 'rsvpResvTSpecRate'), ['int'])),
                    ('rsvpresvtspecpeakrate', (YLeaf(YType.int32, 'rsvpResvTSpecPeakRate'), ['int'])),
                    ('rsvpresvtspecburst', (YLeaf(YType.int32, 'rsvpResvTSpecBurst'), ['int'])),
                    ('rsvpresvtspecmintu', (YLeaf(YType.int32, 'rsvpResvTSpecMinTU'), ['int'])),
                    ('rsvpresvtspecmaxtu', (YLeaf(YType.int32, 'rsvpResvTSpecMaxTU'), ['int'])),
                    ('rsvpresvrspecrate', (YLeaf(YType.int32, 'rsvpResvRSpecRate'), ['int'])),
                    ('rsvpresvrspecslack', (YLeaf(YType.int32, 'rsvpResvRSpecSlack'), ['int'])),
                    ('rsvpresvinterval', (YLeaf(YType.int32, 'rsvpResvInterval'), ['int'])),
                    ('rsvpresvscope', (YLeaf(YType.str, 'rsvpResvScope'), ['str'])),
                    ('rsvpresvshared', (YLeaf(YType.boolean, 'rsvpResvShared'), ['bool'])),
                    ('rsvpresvexplicit', (YLeaf(YType.boolean, 'rsvpResvExplicit'), ['bool'])),
                    ('rsvpresvrsvphop', (YLeaf(YType.boolean, 'rsvpResvRSVPHop'), ['bool'])),
                    ('rsvpresvlastchange', (YLeaf(YType.uint32, 'rsvpResvLastChange'), ['int'])),
                    ('rsvpresvpolicy', (YLeaf(YType.str, 'rsvpResvPolicy'), ['str'])),
                    ('rsvpresvstatus', (YLeaf(YType.enumeration, 'rsvpResvStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('rsvpresvttl', (YLeaf(YType.int32, 'rsvpResvTTL'), ['int'])),
                    ('rsvpresvflowid', (YLeaf(YType.int32, 'rsvpResvFlowId'), ['int'])),
                ])
                self.rsvpsessionnumber = None
                self.rsvpresvnumber = None
                self.rsvpresvtype = None
                self.rsvpresvdestaddr = None
                self.rsvpresvsenderaddr = None
                self.rsvpresvdestaddrlength = None
                self.rsvpresvsenderaddrlength = None
                self.rsvpresvprotocol = None
                self.rsvpresvdestport = None
                self.rsvpresvport = None
                self.rsvpresvhopaddr = None
                self.rsvpresvhoplih = None
                self.rsvpresvinterface = None
                self.rsvpresvservice = None
                self.rsvpresvtspecrate = None
                self.rsvpresvtspecpeakrate = None
                self.rsvpresvtspecburst = None
                self.rsvpresvtspecmintu = None
                self.rsvpresvtspecmaxtu = None
                self.rsvpresvrspecrate = None
                self.rsvpresvrspecslack = None
                self.rsvpresvinterval = None
                self.rsvpresvscope = None
                self.rsvpresvshared = None
                self.rsvpresvexplicit = None
                self.rsvpresvrsvphop = None
                self.rsvpresvlastchange = None
                self.rsvpresvpolicy = None
                self.rsvpresvstatus = None
                self.rsvpresvttl = None
                self.rsvpresvflowid = None
                self._segment_path = lambda: "rsvpResvEntry" + "[rsvpSessionNumber='" + str(self.rsvpsessionnumber) + "']" + "[rsvpResvNumber='" + str(self.rsvpresvnumber) + "']"
                self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/rsvpResvTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RSVPMIB.RsvpResvTable.RsvpResvEntry, ['rsvpsessionnumber', 'rsvpresvnumber', 'rsvpresvtype', 'rsvpresvdestaddr', 'rsvpresvsenderaddr', 'rsvpresvdestaddrlength', 'rsvpresvsenderaddrlength', 'rsvpresvprotocol', 'rsvpresvdestport', 'rsvpresvport', 'rsvpresvhopaddr', 'rsvpresvhoplih', 'rsvpresvinterface', 'rsvpresvservice', 'rsvpresvtspecrate', 'rsvpresvtspecpeakrate', 'rsvpresvtspecburst', 'rsvpresvtspecmintu', 'rsvpresvtspecmaxtu', 'rsvpresvrspecrate', 'rsvpresvrspecslack', 'rsvpresvinterval', 'rsvpresvscope', 'rsvpresvshared', 'rsvpresvexplicit', 'rsvpresvrsvphop', 'rsvpresvlastchange', 'rsvpresvpolicy', 'rsvpresvstatus', 'rsvpresvttl', 'rsvpresvflowid'], name, value)




    class RsvpResvFwdTable(Entity):
        """
        Information	describing the	state  information
        displayed upstream in RESV messages.
        
        .. attribute:: rsvpresvfwdentry
        
        	Information	describing the	state  information displayed   upstream	  in   an   RESV   message concerning a	single sender
        	**type**\: list of  		 :py:class:`RsvpResvFwdEntry <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpResvFwdTable.RsvpResvFwdEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RSVPMIB.RsvpResvFwdTable, self).__init__()

            self.yang_name = "rsvpResvFwdTable"
            self.yang_parent_name = "RSVP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rsvpResvFwdEntry", ("rsvpresvfwdentry", RSVPMIB.RsvpResvFwdTable.RsvpResvFwdEntry))])
            self._leafs = OrderedDict()

            self.rsvpresvfwdentry = YList(self)
            self._segment_path = lambda: "rsvpResvFwdTable"
            self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RSVPMIB.RsvpResvFwdTable, [], name, value)


        class RsvpResvFwdEntry(Entity):
            """
            Information	describing the	state  information
            displayed   upstream	  in   an   RESV   message
            concerning a	single sender.
            
            .. attribute:: rsvpsessionnumber  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsessionnumber <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpSessionTable.RsvpSessionEntry>`
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdnumber  (key)
            
            	The	number of this reservation request.   This is  for  SNMP Indexing purposes only	and has	no relation to any protocol value
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdtype
            
            	The	type of	session	(IP4, IP6, IP6	with  flow information,	etc)
            	**type**\: int
            
            	**range:** 1..255
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwddestaddr
            
            	The	destination address used by all	senders	in this	 session.   This object	may not	be changed when	the  value  of	the  RowStatus	object	is 'active'
            	**type**\: str
            
            	**length:** 4..16
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdsenderaddr
            
            	The	source address of the sender  selected	by this	 reservation.	The  value  of	all zeroes indicates 'all senders'.  This object  may  not be  changed	when  the  value  of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 4..16
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwddestaddrlength
            
            	The	length of the destination address in bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 0..128
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdsenderaddrlength
            
            	The	length of the sender's	address	 in  bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 0..128
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdprotocol
            
            	The	IP Protocol used by a session. for  secure sessions,  this  indicates  IP  Security.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: int
            
            	**range:** 1..255
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwddestport
            
            	The	 UDP  or  TCP  port  number  used   as	 a destination	 port  for  all	 senders  in  this session.  If	the IP protocol	in use,	 specified by rsvpResvFwdProtocol, is 50 (ESP) or 51 (AH), this	 represents  a	virtual	 destination  port number.   A value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 2..4
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdport
            
            	The	UDP or TCP port	number used  as	 a  source port	 for  this sender in this session.  If the IP	 protocol    in	   use,	   specified	by rsvpResvFwdProtocol	is  50	(ESP)  or 51 (AH), this	represents a generalized  port	identifier (GPI).   A  value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 2..4
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdhopaddr
            
            	The	address	of the (previous) RSVP	that  will receive this	message
            	**type**\: str
            
            	**length:** 4..16
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdhoplih
            
            	The	 Logical  Interface  Handle  sent  to  the (previous)	RSVP   that   will   receive  this message
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdinterface
            
            	The	ifIndex	value of the  interface	 on  which this	RESV message was most recently sent
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdservice
            
            	The	QoS Service classification requested
            	**type**\:  :py:class:`QosService <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.QosService>`
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdtspecrate
            
            	The	Average	Bit  Rate  of  the  sender's  data stream.    Within  a	 transmission  burst,  the arrival   rate    may    be	  as	fast	as rsvpResvFwdTSpecPeakRate  (if  supported by the service model); however, averaged across two	or more	 burst	intervals,  the	 rate  should  not exceed rsvpResvFwdTSpecRate.  Note	that this is a prediction, often based	on the	general	 capability  of	a type of codec	or particular encoding;	the measured average  rate may be significantly	lower
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvfwdtspecpeakrate
            
            	The	Peak Bit Rate of the sender's data  stream Traffic  arrival is not expected to exceed this rate	at any time, apart  from  the  effects	of jitter in the network.  If not specified in the TSpec, this returns zero or noSuchValue
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvfwdtspecburst
            
            	The	size of	the largest  burst  expected  from the sender at a time.  If this is less than	 the  sender's	advertised burst  size,	the receiver is	asking the network to provide flow pacing  beyond  what	 would	be provided   under   normal  circumstances.  Such pacing is at	the network's option
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: rsvpresvfwdtspecmintu
            
            	The	minimum	message	size for  this	flow.  The policing  algorithm will treat smaller messages as though they are this size
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdtspecmaxtu
            
            	The	maximum	message	size for  this	flow.  The admission  algorithm	 will  reject TSpecs whose Maximum Transmission	Unit, plus  the	 interface headers, exceed the interface MTU
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdrspecrate
            
            	If the requested  service  is  Guaranteed,	as specified   by  rsvpResvService,  this  is  the clearing  rate   that   is	being	requested. Otherwise,  it is zero, or the agent	may return noSuchValue
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: bytes per second
            
            .. attribute:: rsvpresvfwdrspecslack
            
            	If the requested  service  is  Guaranteed,	as specified by	rsvpResvService, this is the delay slack.  Otherwise, it is zero, or the agent may return noSuchValue
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            	**units**\: microseconds
            
            .. attribute:: rsvpresvfwdinterval
            
            	The	  interval   between   refresh	  messages advertised to the Previous Hop
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdscope
            
            	The	contents of the	scope object, displayed	as an  uninterpreted  string  of octets, including the object header.  In the absence of  such	an object, this	should be of zero length
            	**type**\: str
            
            	**length:** 0..65536
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdshared
            
            	If TRUE, a reservation shared among	senders	is requested.  If FALSE, a reservation specific	to this	sender is requested
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdexplicit
            
            	If TRUE, individual	senders	are  listed  using Filter  Specifications.   If	FALSE, all senders are implicitly selected.  The Scope Object will contain  a list of senders that need	to receive this	reservation request  for  the  purpose	of routing the RESV message
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdrsvphop
            
            	If TRUE, the node believes that  the  next	IP hop	is  an	RSVP  hop.   If	 FALSE,	 the  node believes that the next IP hop  may  not  be	an RSVP	hop
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdlastchange
            
            	The	time of	the last change	in  this  request; This	 is  either  the first time it was sent	or the	time  of  the  most   recent   change	in parameters
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdpolicy
            
            	The	contents of the	policy	object,	 displayed as an uninterpreted string of octets, including the object header.  In the absence of  such	an object, this	should be of zero length
            	**type**\: str
            
            	**length:** 0..65536
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdstatus
            
            	'active' for all active RESV  messages.   This object may be used to delete	RESV information
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdttl
            
            	The	TTL value in the RSVP header that was last received
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: rsvpresvfwdflowid
            
            	The	flow ID	that this receiver  is	using,	if this	 is  an	IPv6 session
            	**type**\: int
            
            	**range:** 0..16777215
            
            	**config**\: False
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RSVPMIB.RsvpResvFwdTable.RsvpResvFwdEntry, self).__init__()

                self.yang_name = "rsvpResvFwdEntry"
                self.yang_parent_name = "rsvpResvFwdTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rsvpsessionnumber','rsvpresvfwdnumber']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rsvpsessionnumber', (YLeaf(YType.str, 'rsvpSessionNumber'), ['int'])),
                    ('rsvpresvfwdnumber', (YLeaf(YType.int32, 'rsvpResvFwdNumber'), ['int'])),
                    ('rsvpresvfwdtype', (YLeaf(YType.int32, 'rsvpResvFwdType'), ['int'])),
                    ('rsvpresvfwddestaddr', (YLeaf(YType.str, 'rsvpResvFwdDestAddr'), ['str'])),
                    ('rsvpresvfwdsenderaddr', (YLeaf(YType.str, 'rsvpResvFwdSenderAddr'), ['str'])),
                    ('rsvpresvfwddestaddrlength', (YLeaf(YType.int32, 'rsvpResvFwdDestAddrLength'), ['int'])),
                    ('rsvpresvfwdsenderaddrlength', (YLeaf(YType.int32, 'rsvpResvFwdSenderAddrLength'), ['int'])),
                    ('rsvpresvfwdprotocol', (YLeaf(YType.int32, 'rsvpResvFwdProtocol'), ['int'])),
                    ('rsvpresvfwddestport', (YLeaf(YType.str, 'rsvpResvFwdDestPort'), ['str'])),
                    ('rsvpresvfwdport', (YLeaf(YType.str, 'rsvpResvFwdPort'), ['str'])),
                    ('rsvpresvfwdhopaddr', (YLeaf(YType.str, 'rsvpResvFwdHopAddr'), ['str'])),
                    ('rsvpresvfwdhoplih', (YLeaf(YType.int32, 'rsvpResvFwdHopLih'), ['int'])),
                    ('rsvpresvfwdinterface', (YLeaf(YType.int32, 'rsvpResvFwdInterface'), ['int'])),
                    ('rsvpresvfwdservice', (YLeaf(YType.enumeration, 'rsvpResvFwdService'), [('ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB', 'QosService', '')])),
                    ('rsvpresvfwdtspecrate', (YLeaf(YType.int32, 'rsvpResvFwdTSpecRate'), ['int'])),
                    ('rsvpresvfwdtspecpeakrate', (YLeaf(YType.int32, 'rsvpResvFwdTSpecPeakRate'), ['int'])),
                    ('rsvpresvfwdtspecburst', (YLeaf(YType.int32, 'rsvpResvFwdTSpecBurst'), ['int'])),
                    ('rsvpresvfwdtspecmintu', (YLeaf(YType.int32, 'rsvpResvFwdTSpecMinTU'), ['int'])),
                    ('rsvpresvfwdtspecmaxtu', (YLeaf(YType.int32, 'rsvpResvFwdTSpecMaxTU'), ['int'])),
                    ('rsvpresvfwdrspecrate', (YLeaf(YType.int32, 'rsvpResvFwdRSpecRate'), ['int'])),
                    ('rsvpresvfwdrspecslack', (YLeaf(YType.int32, 'rsvpResvFwdRSpecSlack'), ['int'])),
                    ('rsvpresvfwdinterval', (YLeaf(YType.int32, 'rsvpResvFwdInterval'), ['int'])),
                    ('rsvpresvfwdscope', (YLeaf(YType.str, 'rsvpResvFwdScope'), ['str'])),
                    ('rsvpresvfwdshared', (YLeaf(YType.boolean, 'rsvpResvFwdShared'), ['bool'])),
                    ('rsvpresvfwdexplicit', (YLeaf(YType.boolean, 'rsvpResvFwdExplicit'), ['bool'])),
                    ('rsvpresvfwdrsvphop', (YLeaf(YType.boolean, 'rsvpResvFwdRSVPHop'), ['bool'])),
                    ('rsvpresvfwdlastchange', (YLeaf(YType.uint32, 'rsvpResvFwdLastChange'), ['int'])),
                    ('rsvpresvfwdpolicy', (YLeaf(YType.str, 'rsvpResvFwdPolicy'), ['str'])),
                    ('rsvpresvfwdstatus', (YLeaf(YType.enumeration, 'rsvpResvFwdStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                    ('rsvpresvfwdttl', (YLeaf(YType.int32, 'rsvpResvFwdTTL'), ['int'])),
                    ('rsvpresvfwdflowid', (YLeaf(YType.int32, 'rsvpResvFwdFlowId'), ['int'])),
                ])
                self.rsvpsessionnumber = None
                self.rsvpresvfwdnumber = None
                self.rsvpresvfwdtype = None
                self.rsvpresvfwddestaddr = None
                self.rsvpresvfwdsenderaddr = None
                self.rsvpresvfwddestaddrlength = None
                self.rsvpresvfwdsenderaddrlength = None
                self.rsvpresvfwdprotocol = None
                self.rsvpresvfwddestport = None
                self.rsvpresvfwdport = None
                self.rsvpresvfwdhopaddr = None
                self.rsvpresvfwdhoplih = None
                self.rsvpresvfwdinterface = None
                self.rsvpresvfwdservice = None
                self.rsvpresvfwdtspecrate = None
                self.rsvpresvfwdtspecpeakrate = None
                self.rsvpresvfwdtspecburst = None
                self.rsvpresvfwdtspecmintu = None
                self.rsvpresvfwdtspecmaxtu = None
                self.rsvpresvfwdrspecrate = None
                self.rsvpresvfwdrspecslack = None
                self.rsvpresvfwdinterval = None
                self.rsvpresvfwdscope = None
                self.rsvpresvfwdshared = None
                self.rsvpresvfwdexplicit = None
                self.rsvpresvfwdrsvphop = None
                self.rsvpresvfwdlastchange = None
                self.rsvpresvfwdpolicy = None
                self.rsvpresvfwdstatus = None
                self.rsvpresvfwdttl = None
                self.rsvpresvfwdflowid = None
                self._segment_path = lambda: "rsvpResvFwdEntry" + "[rsvpSessionNumber='" + str(self.rsvpsessionnumber) + "']" + "[rsvpResvFwdNumber='" + str(self.rsvpresvfwdnumber) + "']"
                self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/rsvpResvFwdTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RSVPMIB.RsvpResvFwdTable.RsvpResvFwdEntry, ['rsvpsessionnumber', 'rsvpresvfwdnumber', 'rsvpresvfwdtype', 'rsvpresvfwddestaddr', 'rsvpresvfwdsenderaddr', 'rsvpresvfwddestaddrlength', 'rsvpresvfwdsenderaddrlength', 'rsvpresvfwdprotocol', 'rsvpresvfwddestport', 'rsvpresvfwdport', 'rsvpresvfwdhopaddr', 'rsvpresvfwdhoplih', 'rsvpresvfwdinterface', 'rsvpresvfwdservice', 'rsvpresvfwdtspecrate', 'rsvpresvfwdtspecpeakrate', 'rsvpresvfwdtspecburst', 'rsvpresvfwdtspecmintu', 'rsvpresvfwdtspecmaxtu', 'rsvpresvfwdrspecrate', 'rsvpresvfwdrspecslack', 'rsvpresvfwdinterval', 'rsvpresvfwdscope', 'rsvpresvfwdshared', 'rsvpresvfwdexplicit', 'rsvpresvfwdrsvphop', 'rsvpresvfwdlastchange', 'rsvpresvfwdpolicy', 'rsvpresvfwdstatus', 'rsvpresvfwdttl', 'rsvpresvfwdflowid'], name, value)




    class RsvpIfTable(Entity):
        """
        The	RSVP\-specific attributes of  the  system's
        interfaces.
        
        .. attribute:: rsvpifentry
        
        	The	RSVP\-specific attributes of  the  a  given interface
        	**type**\: list of  		 :py:class:`RsvpIfEntry <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpIfTable.RsvpIfEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RSVPMIB.RsvpIfTable, self).__init__()

            self.yang_name = "rsvpIfTable"
            self.yang_parent_name = "RSVP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rsvpIfEntry", ("rsvpifentry", RSVPMIB.RsvpIfTable.RsvpIfEntry))])
            self._leafs = OrderedDict()

            self.rsvpifentry = YList(self)
            self._segment_path = lambda: "rsvpIfTable"
            self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RSVPMIB.RsvpIfTable, [], name, value)


        class RsvpIfEntry(Entity):
            """
            The	RSVP\-specific attributes of  the  a  given
            interface.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: rsvpifudpnbrs
            
            	The	number of neighbors perceived to be  using only	the RSVP UDP Encapsulation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rsvpifipnbrs
            
            	The	number of neighbors perceived to be  using only	the RSVP IP Encapsulation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rsvpifnbrs
            
            	The	number of neighbors  currently	perceived; this	 will  exceed rsvpIfIpNbrs + rsvpIfUdpNbrs by  the  number   of	  neighbors   using   both encapsulations
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: rsvpifrefreshblockademultiple
            
            	The	value of the RSVP value	'Kb', Which is the minimum   number   of  refresh  intervals  that blockade state will last once entered
            	**type**\: int
            
            	**range:** 1..65536
            
            	**config**\: False
            
            .. attribute:: rsvpifrefreshmultiple
            
            	The	value of the RSVP value	'K', which is  the number  of  refresh intervals which must elapse (minimum) before a PATH or RESV  message  which is not being	refreshed will be aged out
            	**type**\: int
            
            	**range:** 1..65536
            
            	**config**\: False
            
            .. attribute:: rsvpifttl
            
            	The	value of SEND\_TTL used on  this	 interface for	messages  this node originates.	 If set	to zero, the node determines  the  TTL	via  other means
            	**type**\: int
            
            	**range:** 0..255
            
            	**config**\: False
            
            .. attribute:: rsvpifrefreshinterval
            
            	The	value of the RSVP value	'R', which is  the minimum period between refresh transmissions	of a given PATH	or RESV	message	on an interface
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: milliseconds
            
            .. attribute:: rsvpifroutedelay
            
            	The	approximate period from	the time  a  route is  changed	to  the	 time  a resulting message appears on the interface
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            	**units**\: hundredths	of a second
            
            .. attribute:: rsvpifenabled
            
            	If TRUE, RSVP is enabled  on  this	Interface. If	FALSE,	 RSVP	is  not	 enabled  on  this interface
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rsvpifudprequired
            
            	If TRUE, manual configuration forces  the  use of  UDP  encapsulation  on  the  interface.	If FALSE,  UDP	encapsulation  is  only	 used	if rsvpIfUdpNbrs is not	zero
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: rsvpifstatus
            
            	'active' on	interfaces that	are configured for RSVP
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RSVPMIB.RsvpIfTable.RsvpIfEntry, self).__init__()

                self.yang_name = "rsvpIfEntry"
                self.yang_parent_name = "rsvpIfTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('rsvpifudpnbrs', (YLeaf(YType.uint32, 'rsvpIfUdpNbrs'), ['int'])),
                    ('rsvpifipnbrs', (YLeaf(YType.uint32, 'rsvpIfIpNbrs'), ['int'])),
                    ('rsvpifnbrs', (YLeaf(YType.uint32, 'rsvpIfNbrs'), ['int'])),
                    ('rsvpifrefreshblockademultiple', (YLeaf(YType.int32, 'rsvpIfRefreshBlockadeMultiple'), ['int'])),
                    ('rsvpifrefreshmultiple', (YLeaf(YType.int32, 'rsvpIfRefreshMultiple'), ['int'])),
                    ('rsvpifttl', (YLeaf(YType.int32, 'rsvpIfTTL'), ['int'])),
                    ('rsvpifrefreshinterval', (YLeaf(YType.int32, 'rsvpIfRefreshInterval'), ['int'])),
                    ('rsvpifroutedelay', (YLeaf(YType.int32, 'rsvpIfRouteDelay'), ['int'])),
                    ('rsvpifenabled', (YLeaf(YType.boolean, 'rsvpIfEnabled'), ['bool'])),
                    ('rsvpifudprequired', (YLeaf(YType.boolean, 'rsvpIfUdpRequired'), ['bool'])),
                    ('rsvpifstatus', (YLeaf(YType.enumeration, 'rsvpIfStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ifindex = None
                self.rsvpifudpnbrs = None
                self.rsvpifipnbrs = None
                self.rsvpifnbrs = None
                self.rsvpifrefreshblockademultiple = None
                self.rsvpifrefreshmultiple = None
                self.rsvpifttl = None
                self.rsvpifrefreshinterval = None
                self.rsvpifroutedelay = None
                self.rsvpifenabled = None
                self.rsvpifudprequired = None
                self.rsvpifstatus = None
                self._segment_path = lambda: "rsvpIfEntry" + "[ifIndex='" + str(self.ifindex) + "']"
                self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/rsvpIfTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RSVPMIB.RsvpIfTable.RsvpIfEntry, ['ifindex', 'rsvpifudpnbrs', 'rsvpifipnbrs', 'rsvpifnbrs', 'rsvpifrefreshblockademultiple', 'rsvpifrefreshmultiple', 'rsvpifttl', 'rsvpifrefreshinterval', 'rsvpifroutedelay', 'rsvpifenabled', 'rsvpifudprequired', 'rsvpifstatus'], name, value)




    class RsvpNbrTable(Entity):
        """
        Information	describing  the	 Neighbors  of	an
        RSVP	system.
        
        .. attribute:: rsvpnbrentry
        
        	Information	  describing   a    single    RSVP Neighbor
        	**type**\: list of  		 :py:class:`RsvpNbrEntry <ydk.models.cisco_ios_xe.RSVP_MIB.RSVPMIB.RsvpNbrTable.RsvpNbrEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RSVPMIB.RsvpNbrTable, self).__init__()

            self.yang_name = "rsvpNbrTable"
            self.yang_parent_name = "RSVP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("rsvpNbrEntry", ("rsvpnbrentry", RSVPMIB.RsvpNbrTable.RsvpNbrEntry))])
            self._leafs = OrderedDict()

            self.rsvpnbrentry = YList(self)
            self._segment_path = lambda: "rsvpNbrTable"
            self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(RSVPMIB.RsvpNbrTable, [], name, value)


        class RsvpNbrEntry(Entity):
            """
            Information	  describing   a    single    RSVP
            Neighbor.
            
            .. attribute:: ifindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IFMIB.IfTable.IfEntry>`
            
            	**config**\: False
            
            .. attribute:: rsvpnbraddress  (key)
            
            	The	IP4 or IP6 Address used	by this	 neighbor. This	 object	 may not be changed when the value of the RowStatus object is 'active'
            	**type**\: str
            
            	**length:** 4..16
            
            	**config**\: False
            
            .. attribute:: rsvpnbrprotocol
            
            	The	  encapsulation	  being	  used	 by   this neighbor
            	**type**\:  :py:class:`RsvpEncapsulation <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpEncapsulation>`
            
            	**config**\: False
            
            .. attribute:: rsvpnbrstatus
            
            	'active' for all neighbors.	 This  object  may be	used   to  configure  neighbors.   In  the presence   of   configured	 neighbors,    the implementation  may	(but  is  not required to) limit the  set  of  valid  neighbors	 to  those configured
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            	**config**\: False
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RSVPMIB.RsvpNbrTable.RsvpNbrEntry, self).__init__()

                self.yang_name = "rsvpNbrEntry"
                self.yang_parent_name = "rsvpNbrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ifindex','rsvpnbraddress']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ifindex', (YLeaf(YType.str, 'ifIndex'), ['int'])),
                    ('rsvpnbraddress', (YLeaf(YType.str, 'rsvpNbrAddress'), ['str'])),
                    ('rsvpnbrprotocol', (YLeaf(YType.enumeration, 'rsvpNbrProtocol'), [('ydk.models.cisco_ios_xe.RSVP_MIB', 'RsvpEncapsulation', '')])),
                    ('rsvpnbrstatus', (YLeaf(YType.enumeration, 'rsvpNbrStatus'), [('ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowStatus', '')])),
                ])
                self.ifindex = None
                self.rsvpnbraddress = None
                self.rsvpnbrprotocol = None
                self.rsvpnbrstatus = None
                self._segment_path = lambda: "rsvpNbrEntry" + "[ifIndex='" + str(self.ifindex) + "']" + "[rsvpNbrAddress='" + str(self.rsvpnbraddress) + "']"
                self._absolute_path = lambda: "RSVP-MIB:RSVP-MIB/rsvpNbrTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(RSVPMIB.RsvpNbrTable.RsvpNbrEntry, ['ifindex', 'rsvpnbraddress', 'rsvpnbrprotocol', 'rsvpnbrstatus'], name, value)



    def clone_ptr(self):
        self._top_entity = RSVPMIB()
        return self._top_entity



