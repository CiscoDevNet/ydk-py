""" RSVP_MIB 

The MIB module to describe the RSVP Protocol

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Rsvpencapsulation(Enum):
    """
    Rsvpencapsulation

    This indicates the encapsulation that an  RSVP

    Neighbor is perceived to be using.

    .. data:: ip = 1

    .. data:: udp = 2

    .. data:: both = 3

    """

    ip = Enum.YLeaf(1, "ip")

    udp = Enum.YLeaf(2, "udp")

    both = Enum.YLeaf(3, "both")



class RsvpMib(Entity):
    """
    
    
    .. attribute:: rsvpgenobjects
    
    	
    	**type**\:   :py:class:`Rsvpgenobjects <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpgenobjects>`
    
    .. attribute:: rsvpiftable
    
    	The	RSVP\-specific attributes of  the  system's interfaces
    	**type**\:   :py:class:`Rsvpiftable <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpiftable>`
    
    .. attribute:: rsvpnbrtable
    
    	Information	describing  the	 Neighbors  of	an RSVP	system
    	**type**\:   :py:class:`Rsvpnbrtable <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpnbrtable>`
    
    .. attribute:: rsvpresvfwdtable
    
    	Information	describing the	state  information displayed upstream in RESV messages
    	**type**\:   :py:class:`Rsvpresvfwdtable <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpresvfwdtable>`
    
    .. attribute:: rsvpresvtable
    
    	Information	describing the	state  information displayed by	receivers in RESV messages
    	**type**\:   :py:class:`Rsvpresvtable <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpresvtable>`
    
    .. attribute:: rsvpsenderoutinterfacetable
    
    	List of outgoing interfaces	that PATH messages use.	 The  ifIndex  is the ifIndex value of the egress interface
    	**type**\:   :py:class:`Rsvpsenderoutinterfacetable <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsenderoutinterfacetable>`
    
    .. attribute:: rsvpsendertable
    
    	Information	describing the	state  information displayed by	senders	in PATH	messages
    	**type**\:   :py:class:`Rsvpsendertable <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsendertable>`
    
    .. attribute:: rsvpsessiontable
    
    	A table  of	 all  sessions	seen  by  a  given system
    	**type**\:   :py:class:`Rsvpsessiontable <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsessiontable>`
    
    

    """

    _prefix = 'RSVP-MIB'
    _revision = '1998-08-25'

    def __init__(self):
        super(RsvpMib, self).__init__()
        self._top_entity = None

        self.yang_name = "RSVP-MIB"
        self.yang_parent_name = "RSVP-MIB"

        self.rsvpgenobjects = RsvpMib.Rsvpgenobjects()
        self.rsvpgenobjects.parent = self
        self._children_name_map["rsvpgenobjects"] = "rsvpGenObjects"
        self._children_yang_names.add("rsvpGenObjects")

        self.rsvpiftable = RsvpMib.Rsvpiftable()
        self.rsvpiftable.parent = self
        self._children_name_map["rsvpiftable"] = "rsvpIfTable"
        self._children_yang_names.add("rsvpIfTable")

        self.rsvpnbrtable = RsvpMib.Rsvpnbrtable()
        self.rsvpnbrtable.parent = self
        self._children_name_map["rsvpnbrtable"] = "rsvpNbrTable"
        self._children_yang_names.add("rsvpNbrTable")

        self.rsvpresvfwdtable = RsvpMib.Rsvpresvfwdtable()
        self.rsvpresvfwdtable.parent = self
        self._children_name_map["rsvpresvfwdtable"] = "rsvpResvFwdTable"
        self._children_yang_names.add("rsvpResvFwdTable")

        self.rsvpresvtable = RsvpMib.Rsvpresvtable()
        self.rsvpresvtable.parent = self
        self._children_name_map["rsvpresvtable"] = "rsvpResvTable"
        self._children_yang_names.add("rsvpResvTable")

        self.rsvpsenderoutinterfacetable = RsvpMib.Rsvpsenderoutinterfacetable()
        self.rsvpsenderoutinterfacetable.parent = self
        self._children_name_map["rsvpsenderoutinterfacetable"] = "rsvpSenderOutInterfaceTable"
        self._children_yang_names.add("rsvpSenderOutInterfaceTable")

        self.rsvpsendertable = RsvpMib.Rsvpsendertable()
        self.rsvpsendertable.parent = self
        self._children_name_map["rsvpsendertable"] = "rsvpSenderTable"
        self._children_yang_names.add("rsvpSenderTable")

        self.rsvpsessiontable = RsvpMib.Rsvpsessiontable()
        self.rsvpsessiontable.parent = self
        self._children_name_map["rsvpsessiontable"] = "rsvpSessionTable"
        self._children_yang_names.add("rsvpSessionTable")


    class Rsvpgenobjects(Entity):
        """
        
        
        .. attribute:: rsvpbadpackets
        
        	This object	keeps a	count of the number of bad RSVP	packets	received
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: rsvpresvfwdnewindex
        
        	This  object  is  used  to	assign	values	to rsvpResvFwdNumber   as  described  in  'Textual Conventions for SNMPv2'.  The  network  manager reads  the  object,	and  then writes the value back	in the SET that	creates	a new instance	of rsvpResvFwdEntry.   If  the	SET fails with the code	'inconsistentValue', then the process must be  repeated;  If  the  SET	succeeds, then the object is incremented, and the new instance	is created according to	the manager's directions
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: rsvpresvnewindex
        
        	This  object  is  used  to	assign	values	to rsvpResvNumber   as	 described   in	  'Textual Conventions for SNMPv2'.  The  network  manager reads  the  object,	and  then writes the value back	in the SET that	creates	a new instance	of rsvpResvEntry.   If the SET fails with the code 'inconsistentValue',	then the process  must	be repeated;  If the SET succeeds, then	the object is incremented, and the new instance	is created according to	the manager's directions
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: rsvpsendernewindex
        
        	This  object  is  used  to	assign	values	to rsvpSenderNumber   as   described  in  'Textual Conventions for SNMPv2'.  The  network  manager reads  the  object,	and  then writes the value back	in the SET that	creates	a new instance	of rsvpSenderEntry.   If  the  SET  fails with the code	'inconsistentValue', then the process must be  repeated;  If  the  SET	succeeds, then the object is incremented, and the new instance	is created according to	the manager's directions
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: rsvpsessionnewindex
        
        	This  object  is  used  to	assign	values	to rsvpSessionNumber   as  described  in  'Textual Conventions for SNMPv2'.  The  network  manager reads  the  object,	and  then writes the value back	in the SET that	creates	a new instance	of rsvpSessionEntry.   If  the	SET fails with the code	'inconsistentValue', then the process must be  repeated;  If  the  SET	succeeds, then the object is incremented, and the new instance	is created according to	the manager's directions
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RsvpMib.Rsvpgenobjects, self).__init__()

            self.yang_name = "rsvpGenObjects"
            self.yang_parent_name = "RSVP-MIB"

            self.rsvpbadpackets = YLeaf(YType.uint32, "rsvpBadPackets")

            self.rsvpresvfwdnewindex = YLeaf(YType.int32, "rsvpResvFwdNewIndex")

            self.rsvpresvnewindex = YLeaf(YType.int32, "rsvpResvNewIndex")

            self.rsvpsendernewindex = YLeaf(YType.int32, "rsvpSenderNewIndex")

            self.rsvpsessionnewindex = YLeaf(YType.int32, "rsvpSessionNewIndex")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("rsvpbadpackets",
                            "rsvpresvfwdnewindex",
                            "rsvpresvnewindex",
                            "rsvpsendernewindex",
                            "rsvpsessionnewindex") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(RsvpMib.Rsvpgenobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RsvpMib.Rsvpgenobjects, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.rsvpbadpackets.is_set or
                self.rsvpresvfwdnewindex.is_set or
                self.rsvpresvnewindex.is_set or
                self.rsvpsendernewindex.is_set or
                self.rsvpsessionnewindex.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.rsvpbadpackets.yfilter != YFilter.not_set or
                self.rsvpresvfwdnewindex.yfilter != YFilter.not_set or
                self.rsvpresvnewindex.yfilter != YFilter.not_set or
                self.rsvpsendernewindex.yfilter != YFilter.not_set or
                self.rsvpsessionnewindex.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rsvpGenObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RSVP-MIB:RSVP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.rsvpbadpackets.is_set or self.rsvpbadpackets.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rsvpbadpackets.get_name_leafdata())
            if (self.rsvpresvfwdnewindex.is_set or self.rsvpresvfwdnewindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rsvpresvfwdnewindex.get_name_leafdata())
            if (self.rsvpresvnewindex.is_set or self.rsvpresvnewindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rsvpresvnewindex.get_name_leafdata())
            if (self.rsvpsendernewindex.is_set or self.rsvpsendernewindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rsvpsendernewindex.get_name_leafdata())
            if (self.rsvpsessionnewindex.is_set or self.rsvpsessionnewindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.rsvpsessionnewindex.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rsvpBadPackets" or name == "rsvpResvFwdNewIndex" or name == "rsvpResvNewIndex" or name == "rsvpSenderNewIndex" or name == "rsvpSessionNewIndex"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "rsvpBadPackets"):
                self.rsvpbadpackets = value
                self.rsvpbadpackets.value_namespace = name_space
                self.rsvpbadpackets.value_namespace_prefix = name_space_prefix
            if(value_path == "rsvpResvFwdNewIndex"):
                self.rsvpresvfwdnewindex = value
                self.rsvpresvfwdnewindex.value_namespace = name_space
                self.rsvpresvfwdnewindex.value_namespace_prefix = name_space_prefix
            if(value_path == "rsvpResvNewIndex"):
                self.rsvpresvnewindex = value
                self.rsvpresvnewindex.value_namespace = name_space
                self.rsvpresvnewindex.value_namespace_prefix = name_space_prefix
            if(value_path == "rsvpSenderNewIndex"):
                self.rsvpsendernewindex = value
                self.rsvpsendernewindex.value_namespace = name_space
                self.rsvpsendernewindex.value_namespace_prefix = name_space_prefix
            if(value_path == "rsvpSessionNewIndex"):
                self.rsvpsessionnewindex = value
                self.rsvpsessionnewindex.value_namespace = name_space
                self.rsvpsessionnewindex.value_namespace_prefix = name_space_prefix


    class Rsvpsessiontable(Entity):
        """
        A table  of	 all  sessions	seen  by  a  given
        system.
        
        .. attribute:: rsvpsessionentry
        
        	A single session seen by a given system
        	**type**\: list of    :py:class:`Rsvpsessionentry <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsessiontable.Rsvpsessionentry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RsvpMib.Rsvpsessiontable, self).__init__()

            self.yang_name = "rsvpSessionTable"
            self.yang_parent_name = "RSVP-MIB"

            self.rsvpsessionentry = YList(self)

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
                        super(RsvpMib.Rsvpsessiontable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RsvpMib.Rsvpsessiontable, self).__setattr__(name, value)


        class Rsvpsessionentry(Entity):
            """
            A single session seen by a given system.
            
            .. attribute:: rsvpsessionnumber  <key>
            
            	The	number of this session.	 This is for  SNMP Indexing  purposes  only and	has no relation	to any protocol	value
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpsessiondestaddr
            
            	The	destination address used by all	senders	in this	 session.   This object	may not	be changed when	the  value  of	the  RowStatus	object	is 'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpsessiondestaddrlength
            
            	The	CIDR prefix length of the session address, which   is	32  for	 IP4  host  and	 multicast addresses, and 128  for  IP6	 addresses.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: rsvpsessionport
            
            	The	 UDP  or  TCP  port  number  used   as	 a destination	 port  for  all	 senders  in  this session.  If	the IP protocol	in use,	 specified by  rsvpSenderProtocol, is 50 (ESP) or 51 (AH), this	 represents  a	virtual	 destination  port number.   A value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: rsvpsessionprotocol
            
            	The	IP Protocol used by  this  session.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: rsvpsessionreceivers
            
            	The	number of reservations being requested	of this	system for this	session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpsessionrequests
            
            	The	number of reservation requests this system is sending upstream for this	session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpsessionsenders
            
            	The	number of distinct senders currently known to be part of this session
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpsessiontype
            
            	The	type of	session	(IP4, IP6, IP6	with  flow information,	etc)
            	**type**\:  int
            
            	**range:** 1..255
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RsvpMib.Rsvpsessiontable.Rsvpsessionentry, self).__init__()

                self.yang_name = "rsvpSessionEntry"
                self.yang_parent_name = "rsvpSessionTable"

                self.rsvpsessionnumber = YLeaf(YType.int32, "rsvpSessionNumber")

                self.rsvpsessiondestaddr = YLeaf(YType.str, "rsvpSessionDestAddr")

                self.rsvpsessiondestaddrlength = YLeaf(YType.int32, "rsvpSessionDestAddrLength")

                self.rsvpsessionport = YLeaf(YType.str, "rsvpSessionPort")

                self.rsvpsessionprotocol = YLeaf(YType.int32, "rsvpSessionProtocol")

                self.rsvpsessionreceivers = YLeaf(YType.uint32, "rsvpSessionReceivers")

                self.rsvpsessionrequests = YLeaf(YType.uint32, "rsvpSessionRequests")

                self.rsvpsessionsenders = YLeaf(YType.uint32, "rsvpSessionSenders")

                self.rsvpsessiontype = YLeaf(YType.int32, "rsvpSessionType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rsvpsessionnumber",
                                "rsvpsessiondestaddr",
                                "rsvpsessiondestaddrlength",
                                "rsvpsessionport",
                                "rsvpsessionprotocol",
                                "rsvpsessionreceivers",
                                "rsvpsessionrequests",
                                "rsvpsessionsenders",
                                "rsvpsessiontype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RsvpMib.Rsvpsessiontable.Rsvpsessionentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RsvpMib.Rsvpsessiontable.Rsvpsessionentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rsvpsessionnumber.is_set or
                    self.rsvpsessiondestaddr.is_set or
                    self.rsvpsessiondestaddrlength.is_set or
                    self.rsvpsessionport.is_set or
                    self.rsvpsessionprotocol.is_set or
                    self.rsvpsessionreceivers.is_set or
                    self.rsvpsessionrequests.is_set or
                    self.rsvpsessionsenders.is_set or
                    self.rsvpsessiontype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rsvpsessionnumber.yfilter != YFilter.not_set or
                    self.rsvpsessiondestaddr.yfilter != YFilter.not_set or
                    self.rsvpsessiondestaddrlength.yfilter != YFilter.not_set or
                    self.rsvpsessionport.yfilter != YFilter.not_set or
                    self.rsvpsessionprotocol.yfilter != YFilter.not_set or
                    self.rsvpsessionreceivers.yfilter != YFilter.not_set or
                    self.rsvpsessionrequests.yfilter != YFilter.not_set or
                    self.rsvpsessionsenders.yfilter != YFilter.not_set or
                    self.rsvpsessiontype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rsvpSessionEntry" + "[rsvpSessionNumber='" + self.rsvpsessionnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RSVP-MIB:RSVP-MIB/rsvpSessionTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rsvpsessionnumber.is_set or self.rsvpsessionnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsessionnumber.get_name_leafdata())
                if (self.rsvpsessiondestaddr.is_set or self.rsvpsessiondestaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsessiondestaddr.get_name_leafdata())
                if (self.rsvpsessiondestaddrlength.is_set or self.rsvpsessiondestaddrlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsessiondestaddrlength.get_name_leafdata())
                if (self.rsvpsessionport.is_set or self.rsvpsessionport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsessionport.get_name_leafdata())
                if (self.rsvpsessionprotocol.is_set or self.rsvpsessionprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsessionprotocol.get_name_leafdata())
                if (self.rsvpsessionreceivers.is_set or self.rsvpsessionreceivers.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsessionreceivers.get_name_leafdata())
                if (self.rsvpsessionrequests.is_set or self.rsvpsessionrequests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsessionrequests.get_name_leafdata())
                if (self.rsvpsessionsenders.is_set or self.rsvpsessionsenders.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsessionsenders.get_name_leafdata())
                if (self.rsvpsessiontype.is_set or self.rsvpsessiontype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsessiontype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rsvpSessionNumber" or name == "rsvpSessionDestAddr" or name == "rsvpSessionDestAddrLength" or name == "rsvpSessionPort" or name == "rsvpSessionProtocol" or name == "rsvpSessionReceivers" or name == "rsvpSessionRequests" or name == "rsvpSessionSenders" or name == "rsvpSessionType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rsvpSessionNumber"):
                    self.rsvpsessionnumber = value
                    self.rsvpsessionnumber.value_namespace = name_space
                    self.rsvpsessionnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSessionDestAddr"):
                    self.rsvpsessiondestaddr = value
                    self.rsvpsessiondestaddr.value_namespace = name_space
                    self.rsvpsessiondestaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSessionDestAddrLength"):
                    self.rsvpsessiondestaddrlength = value
                    self.rsvpsessiondestaddrlength.value_namespace = name_space
                    self.rsvpsessiondestaddrlength.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSessionPort"):
                    self.rsvpsessionport = value
                    self.rsvpsessionport.value_namespace = name_space
                    self.rsvpsessionport.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSessionProtocol"):
                    self.rsvpsessionprotocol = value
                    self.rsvpsessionprotocol.value_namespace = name_space
                    self.rsvpsessionprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSessionReceivers"):
                    self.rsvpsessionreceivers = value
                    self.rsvpsessionreceivers.value_namespace = name_space
                    self.rsvpsessionreceivers.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSessionRequests"):
                    self.rsvpsessionrequests = value
                    self.rsvpsessionrequests.value_namespace = name_space
                    self.rsvpsessionrequests.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSessionSenders"):
                    self.rsvpsessionsenders = value
                    self.rsvpsessionsenders.value_namespace = name_space
                    self.rsvpsessionsenders.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSessionType"):
                    self.rsvpsessiontype = value
                    self.rsvpsessiontype.value_namespace = name_space
                    self.rsvpsessiontype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rsvpsessionentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rsvpsessionentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rsvpSessionTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RSVP-MIB:RSVP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rsvpSessionEntry"):
                for c in self.rsvpsessionentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RsvpMib.Rsvpsessiontable.Rsvpsessionentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rsvpsessionentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rsvpSessionEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Rsvpsendertable(Entity):
        """
        Information	describing the	state  information
        displayed by	senders	in PATH	messages.
        
        .. attribute:: rsvpsenderentry
        
        	Information	describing the	state  information displayed by	a single sender's PATH message
        	**type**\: list of    :py:class:`Rsvpsenderentry <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsendertable.Rsvpsenderentry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RsvpMib.Rsvpsendertable, self).__init__()

            self.yang_name = "rsvpSenderTable"
            self.yang_parent_name = "RSVP-MIB"

            self.rsvpsenderentry = YList(self)

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
                        super(RsvpMib.Rsvpsendertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RsvpMib.Rsvpsendertable, self).__setattr__(name, value)


        class Rsvpsenderentry(Entity):
            """
            Information	describing the	state  information
            displayed by	a single sender's PATH message.
            
            .. attribute:: rsvpsessionnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsessionnumber <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsessiontable.Rsvpsessionentry>`
            
            .. attribute:: rsvpsendernumber  <key>
            
            	The	number of this sender.	This is	 for  SNMP Indexing  purposes  only and	has no relation	to any protocol	value
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpsenderaddr
            
            	The	source address used by this sender in this session.   This  object may not be changed when the value of	the RowStatus object is	'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpsenderaddrlength
            
            	The	length of the sender's	address	 in  bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: rsvpsenderadspecbreak
            
            	The	global break bit general  characterization parameter  from  the	ADSPEC.	 If TRUE, at least one non\-IS hop was detected in  the	path.	If FALSE, no non\-IS hops were detected
            	**type**\:  bool
            
            .. attribute:: rsvpsenderadspecctrlloadbreak
            
            	If TRUE, the Controlled Load Service  fragment has its 'break' bit set, indicating that one	or more	nodes along the	path do	 not  support  the controlled	load   service.	   If  FALSE,  and rsvpSenderAdspecCtrlLoadSvc	 is   TRUE,    the 'break' bit is not set.  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns FALSE or noSuchValue
            	**type**\:  bool
            
            .. attribute:: rsvpsenderadspecctrlloadhopcount
            
            	If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this is  the  service\-specific  override	of the hop count general characterization  parameter  from the	ADSPEC.	  A  return of zero or noSuchValue indicates one of the	following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: rsvpsenderadspecctrlloadminlatency
            
            	If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this is the service\-specific override of the minimum path	latency	general	characterization parameter from	  the	ADSPEC.	   A  return  of  zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecctrlloadmtu
            
            	If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this is	the   service\-specific	 override  of  the composed  Maximum  Transmission  Unit   general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderadspecctrlloadpathbw
            
            	If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this is  the  service\-specific  override of the path bandwidth  estimate	general	  characterization parameter from the ADSPEC.  A return	of zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsenderadspecctrlloadsvc
            
            	If TRUE, the ADSPEC	contains a Controlled Load Service  fragment.	If  FALSE, the ADSPEC does not	 contain   a   Controlled   Load   Service fragment
            	**type**\:  bool
            
            .. attribute:: rsvpsenderadspecguaranteedbreak
            
            	If TRUE, the Guaranteed Service  fragment  has its	'break'	 bit  set,  indicating that one	or more	nodes along the	path do	 not  support  the guaranteed	  service.     If    FALSE,    and rsvpSenderAdspecGuaranteedSvc  is   TRUE,   the 'break' bit is not set.  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns FALSE or noSuchValue
            	**type**\:  bool
            
            .. attribute:: rsvpsenderadspecguaranteedcsum
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the  composed  value  for  the	guaranteed service 'C' parameter since the last	 reshaping point.    A	 return	 of  zero  or  noSuchValue indicates one of the	following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderadspecguaranteedctot
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the  end\-to\-end	 composed  value  for  the guaranteed service 'C' parameter.  A	return	of zero	  or  noSuchValue  indicates  one  of  the following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderadspecguaranteeddsum
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the  composed  value  for  the	guaranteed service 'D' parameter since the last	 reshaping point.    A	 return	 of  zero  or  noSuchValue indicates one of the	following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecguaranteeddtot
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the  end\-to\-end	 composed  value  for  the guaranteed service 'D' parameter.  A	return	of zero	  or  noSuchValue  indicates  one  of  the following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecguaranteedhopcount
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is  the  service\-specific  override	of the hop count general characterization  parameter  from the	ADSPEC.	  A  return of zero or noSuchValue indicates one of the	following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: rsvpsenderadspecguaranteedminlatency
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is the service\-specific override of the minimum path	latency	general	characterization parameter from	  the	ADSPEC.	   A  return  of  zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecguaranteedmtu
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is	the   service\-specific	 override  of  the composed  Maximum  Transmission  Unit   general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderadspecguaranteedpathbw
            
            	If rsvpSenderAdspecGuaranteedSvc is	TRUE, this is  the  service\-specific  override of the path bandwidth  estimate	general	  characterization parameter from the ADSPEC.  A return	of zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present  If rsvpSenderAdspecGuaranteedSvc is FALSE, this returns zero	or noSuchValue
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsenderadspecguaranteedsvc
            
            	If TRUE,  the  ADSPEC  contains  a	Guaranteed Service  fragment.	If  FALSE, the ADSPEC does not contain a Guaranteed Service fragment
            	**type**\:  bool
            
            .. attribute:: rsvpsenderadspechopcount
            
            	The	  hop	count	general	  characterization parameter from the ADSPEC.  A return	of zero	or noSuchValue	indicates  one	of  the	 following conditions\:     the invalid bit was set    the parameter was	not present
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: rsvpsenderadspecminlatency
            
            	The	   minimum    path     latency	   general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpsenderadspecmtu
            
            	The	composed Maximum Transmission Unit general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: bytes
            
            .. attribute:: rsvpsenderadspecpathbw
            
            	The	  path	  bandwidth    estimate	   general characterization  parameter from the	ADSPEC.	 A return of zero or noSuchValue indicates one	of the following conditions\:     the invalid bit was set    the parameter was	not present
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsenderdestaddr
            
            	The	destination address used by all	senders	in this	 session.   This object	may not	be changed when	the  value  of	the  RowStatus	object	is 'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpsenderdestaddrlength
            
            	The	length of the destination address in bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: rsvpsenderdestport
            
            	The	 UDP  or  TCP  port  number  used   as	 a destination	 port  for  all	 senders  in  this session.  If	the IP protocol	in use,	 specified by  rsvpSenderProtocol, is 50 (ESP) or 51 (AH), this	 represents  a	virtual	 destination  port number.   A value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: rsvpsenderflowid
            
            	The	flow ID	that  this  sender  is	using,	if this	 is  an	IPv6 session
            	**type**\:  int
            
            	**range:** 0..16777215
            
            .. attribute:: rsvpsenderhopaddr
            
            	The	address	used  by  the  previous	 RSVP  hop (which may be the original sender)
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpsenderhoplih
            
            	The	 Logical  Interface  Handle  used  by  the previous  RSVP  hop	(which may be the original sender)
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: rsvpsenderinterface
            
            	The	ifIndex	value of the  interface	 on  which this	PATH message was most recently received
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: rsvpsenderinterval
            
            	The	 interval  between  refresh  messages	as advertised by the Previous Hop
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpsenderlastchange
            
            	The	time of	 the  last  change  in	this  PATH message;  This  is either the first time it was received or the time	of the most recent  change in parameters
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpsenderpolicy
            
            	The	contents of the	policy	object,	 displayed as an uninterpreted string of octets, including the object header.  In the absence of  such	an object, this	should be of zero length
            	**type**\:  str
            
            	**length:** 4..65536
            
            .. attribute:: rsvpsenderport
            
            	The	UDP or TCP port	number used  as	 a  source port	 for  this sender in this session.  If the IP	 protocol    in	   use,	   specified	by rsvpSenderProtocol is 50 (ESP) or 51	(AH), this represents a	generalized port identifier (GPI). A  value of zero indicates that the IP protocol in use does not have	ports.	 This  object  may not	be changed when	the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: rsvpsenderprotocol
            
            	The	IP Protocol used by  this  session.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: rsvpsenderrsvphop
            
            	If TRUE, the node believes that  the  previous IP  hop  is	an  RSVP  hop.	If FALSE, the node believes that the previous IP hop may not be	an RSVP	hop
            	**type**\:  bool
            
            .. attribute:: rsvpsenderstatus
            
            	'active' for all active PATH  messages.   This object  may	be  used  to  install  static PATH information or delete PATH information
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: rsvpsendertspecburst
            
            	The	size of	the largest  burst  expected  from the sender at a time
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bytes
            
            .. attribute:: rsvpsendertspecmaxtu
            
            	The	maximum	message	size for  this	flow.  The admission  algorithm	 will  reject TSpecs whose Maximum Transmission	Unit, plus  the	 interface headers, exceed the interface MTU
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpsendertspecmintu
            
            	The	minimum	message	size for  this	flow.  The policing  algorithm will treat smaller messages as though they are this size
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpsendertspecpeakrate
            
            	The	Peak Bit Rate of the sender's data stream. Traffic  arrival is not expected to exceed this rate	at any time, apart  from  the  effects	of jitter in the network.  If not specified in the TSpec, this returns zero or noSuchValue
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsendertspecrate
            
            	The	Average	Bit  Rate  of  the  sender's  data stream.    Within  a	 transmission  burst,  the arrival   rate    may    be	  as	fast	as rsvpSenderTSpecPeakRate  (if	 supported  by the service model); however, averaged across two	or more	 burst	intervals,  the	 rate  should  not exceed rsvpSenderTSpecRate.  Note	that this is a prediction, often based	on the	general	 capability  of	a type of codec	or particular encoding;	the measured average  rate may be significantly	lower
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpsenderttl
            
            	The	TTL value in the RSVP header that was last received
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: rsvpsendertype
            
            	The	type of	session	(IP4, IP6, IP6	with  flow information,	etc)
            	**type**\:  int
            
            	**range:** 1..255
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RsvpMib.Rsvpsendertable.Rsvpsenderentry, self).__init__()

                self.yang_name = "rsvpSenderEntry"
                self.yang_parent_name = "rsvpSenderTable"

                self.rsvpsessionnumber = YLeaf(YType.str, "rsvpSessionNumber")

                self.rsvpsendernumber = YLeaf(YType.int32, "rsvpSenderNumber")

                self.rsvpsenderaddr = YLeaf(YType.str, "rsvpSenderAddr")

                self.rsvpsenderaddrlength = YLeaf(YType.int32, "rsvpSenderAddrLength")

                self.rsvpsenderadspecbreak = YLeaf(YType.boolean, "rsvpSenderAdspecBreak")

                self.rsvpsenderadspecctrlloadbreak = YLeaf(YType.boolean, "rsvpSenderAdspecCtrlLoadBreak")

                self.rsvpsenderadspecctrlloadhopcount = YLeaf(YType.int32, "rsvpSenderAdspecCtrlLoadHopCount")

                self.rsvpsenderadspecctrlloadminlatency = YLeaf(YType.int32, "rsvpSenderAdspecCtrlLoadMinLatency")

                self.rsvpsenderadspecctrlloadmtu = YLeaf(YType.int32, "rsvpSenderAdspecCtrlLoadMtu")

                self.rsvpsenderadspecctrlloadpathbw = YLeaf(YType.int32, "rsvpSenderAdspecCtrlLoadPathBw")

                self.rsvpsenderadspecctrlloadsvc = YLeaf(YType.boolean, "rsvpSenderAdspecCtrlLoadSvc")

                self.rsvpsenderadspecguaranteedbreak = YLeaf(YType.boolean, "rsvpSenderAdspecGuaranteedBreak")

                self.rsvpsenderadspecguaranteedcsum = YLeaf(YType.int32, "rsvpSenderAdspecGuaranteedCsum")

                self.rsvpsenderadspecguaranteedctot = YLeaf(YType.int32, "rsvpSenderAdspecGuaranteedCtot")

                self.rsvpsenderadspecguaranteeddsum = YLeaf(YType.int32, "rsvpSenderAdspecGuaranteedDsum")

                self.rsvpsenderadspecguaranteeddtot = YLeaf(YType.int32, "rsvpSenderAdspecGuaranteedDtot")

                self.rsvpsenderadspecguaranteedhopcount = YLeaf(YType.int32, "rsvpSenderAdspecGuaranteedHopCount")

                self.rsvpsenderadspecguaranteedminlatency = YLeaf(YType.int32, "rsvpSenderAdspecGuaranteedMinLatency")

                self.rsvpsenderadspecguaranteedmtu = YLeaf(YType.int32, "rsvpSenderAdspecGuaranteedMtu")

                self.rsvpsenderadspecguaranteedpathbw = YLeaf(YType.int32, "rsvpSenderAdspecGuaranteedPathBw")

                self.rsvpsenderadspecguaranteedsvc = YLeaf(YType.boolean, "rsvpSenderAdspecGuaranteedSvc")

                self.rsvpsenderadspechopcount = YLeaf(YType.int32, "rsvpSenderAdspecHopCount")

                self.rsvpsenderadspecminlatency = YLeaf(YType.int32, "rsvpSenderAdspecMinLatency")

                self.rsvpsenderadspecmtu = YLeaf(YType.int32, "rsvpSenderAdspecMtu")

                self.rsvpsenderadspecpathbw = YLeaf(YType.int32, "rsvpSenderAdspecPathBw")

                self.rsvpsenderdestaddr = YLeaf(YType.str, "rsvpSenderDestAddr")

                self.rsvpsenderdestaddrlength = YLeaf(YType.int32, "rsvpSenderDestAddrLength")

                self.rsvpsenderdestport = YLeaf(YType.str, "rsvpSenderDestPort")

                self.rsvpsenderflowid = YLeaf(YType.int32, "rsvpSenderFlowId")

                self.rsvpsenderhopaddr = YLeaf(YType.str, "rsvpSenderHopAddr")

                self.rsvpsenderhoplih = YLeaf(YType.int32, "rsvpSenderHopLih")

                self.rsvpsenderinterface = YLeaf(YType.int32, "rsvpSenderInterface")

                self.rsvpsenderinterval = YLeaf(YType.int32, "rsvpSenderInterval")

                self.rsvpsenderlastchange = YLeaf(YType.uint32, "rsvpSenderLastChange")

                self.rsvpsenderpolicy = YLeaf(YType.str, "rsvpSenderPolicy")

                self.rsvpsenderport = YLeaf(YType.str, "rsvpSenderPort")

                self.rsvpsenderprotocol = YLeaf(YType.int32, "rsvpSenderProtocol")

                self.rsvpsenderrsvphop = YLeaf(YType.boolean, "rsvpSenderRSVPHop")

                self.rsvpsenderstatus = YLeaf(YType.enumeration, "rsvpSenderStatus")

                self.rsvpsendertspecburst = YLeaf(YType.int32, "rsvpSenderTSpecBurst")

                self.rsvpsendertspecmaxtu = YLeaf(YType.int32, "rsvpSenderTSpecMaxTU")

                self.rsvpsendertspecmintu = YLeaf(YType.int32, "rsvpSenderTSpecMinTU")

                self.rsvpsendertspecpeakrate = YLeaf(YType.int32, "rsvpSenderTSpecPeakRate")

                self.rsvpsendertspecrate = YLeaf(YType.int32, "rsvpSenderTSpecRate")

                self.rsvpsenderttl = YLeaf(YType.int32, "rsvpSenderTTL")

                self.rsvpsendertype = YLeaf(YType.int32, "rsvpSenderType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rsvpsessionnumber",
                                "rsvpsendernumber",
                                "rsvpsenderaddr",
                                "rsvpsenderaddrlength",
                                "rsvpsenderadspecbreak",
                                "rsvpsenderadspecctrlloadbreak",
                                "rsvpsenderadspecctrlloadhopcount",
                                "rsvpsenderadspecctrlloadminlatency",
                                "rsvpsenderadspecctrlloadmtu",
                                "rsvpsenderadspecctrlloadpathbw",
                                "rsvpsenderadspecctrlloadsvc",
                                "rsvpsenderadspecguaranteedbreak",
                                "rsvpsenderadspecguaranteedcsum",
                                "rsvpsenderadspecguaranteedctot",
                                "rsvpsenderadspecguaranteeddsum",
                                "rsvpsenderadspecguaranteeddtot",
                                "rsvpsenderadspecguaranteedhopcount",
                                "rsvpsenderadspecguaranteedminlatency",
                                "rsvpsenderadspecguaranteedmtu",
                                "rsvpsenderadspecguaranteedpathbw",
                                "rsvpsenderadspecguaranteedsvc",
                                "rsvpsenderadspechopcount",
                                "rsvpsenderadspecminlatency",
                                "rsvpsenderadspecmtu",
                                "rsvpsenderadspecpathbw",
                                "rsvpsenderdestaddr",
                                "rsvpsenderdestaddrlength",
                                "rsvpsenderdestport",
                                "rsvpsenderflowid",
                                "rsvpsenderhopaddr",
                                "rsvpsenderhoplih",
                                "rsvpsenderinterface",
                                "rsvpsenderinterval",
                                "rsvpsenderlastchange",
                                "rsvpsenderpolicy",
                                "rsvpsenderport",
                                "rsvpsenderprotocol",
                                "rsvpsenderrsvphop",
                                "rsvpsenderstatus",
                                "rsvpsendertspecburst",
                                "rsvpsendertspecmaxtu",
                                "rsvpsendertspecmintu",
                                "rsvpsendertspecpeakrate",
                                "rsvpsendertspecrate",
                                "rsvpsenderttl",
                                "rsvpsendertype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RsvpMib.Rsvpsendertable.Rsvpsenderentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RsvpMib.Rsvpsendertable.Rsvpsenderentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rsvpsessionnumber.is_set or
                    self.rsvpsendernumber.is_set or
                    self.rsvpsenderaddr.is_set or
                    self.rsvpsenderaddrlength.is_set or
                    self.rsvpsenderadspecbreak.is_set or
                    self.rsvpsenderadspecctrlloadbreak.is_set or
                    self.rsvpsenderadspecctrlloadhopcount.is_set or
                    self.rsvpsenderadspecctrlloadminlatency.is_set or
                    self.rsvpsenderadspecctrlloadmtu.is_set or
                    self.rsvpsenderadspecctrlloadpathbw.is_set or
                    self.rsvpsenderadspecctrlloadsvc.is_set or
                    self.rsvpsenderadspecguaranteedbreak.is_set or
                    self.rsvpsenderadspecguaranteedcsum.is_set or
                    self.rsvpsenderadspecguaranteedctot.is_set or
                    self.rsvpsenderadspecguaranteeddsum.is_set or
                    self.rsvpsenderadspecguaranteeddtot.is_set or
                    self.rsvpsenderadspecguaranteedhopcount.is_set or
                    self.rsvpsenderadspecguaranteedminlatency.is_set or
                    self.rsvpsenderadspecguaranteedmtu.is_set or
                    self.rsvpsenderadspecguaranteedpathbw.is_set or
                    self.rsvpsenderadspecguaranteedsvc.is_set or
                    self.rsvpsenderadspechopcount.is_set or
                    self.rsvpsenderadspecminlatency.is_set or
                    self.rsvpsenderadspecmtu.is_set or
                    self.rsvpsenderadspecpathbw.is_set or
                    self.rsvpsenderdestaddr.is_set or
                    self.rsvpsenderdestaddrlength.is_set or
                    self.rsvpsenderdestport.is_set or
                    self.rsvpsenderflowid.is_set or
                    self.rsvpsenderhopaddr.is_set or
                    self.rsvpsenderhoplih.is_set or
                    self.rsvpsenderinterface.is_set or
                    self.rsvpsenderinterval.is_set or
                    self.rsvpsenderlastchange.is_set or
                    self.rsvpsenderpolicy.is_set or
                    self.rsvpsenderport.is_set or
                    self.rsvpsenderprotocol.is_set or
                    self.rsvpsenderrsvphop.is_set or
                    self.rsvpsenderstatus.is_set or
                    self.rsvpsendertspecburst.is_set or
                    self.rsvpsendertspecmaxtu.is_set or
                    self.rsvpsendertspecmintu.is_set or
                    self.rsvpsendertspecpeakrate.is_set or
                    self.rsvpsendertspecrate.is_set or
                    self.rsvpsenderttl.is_set or
                    self.rsvpsendertype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rsvpsessionnumber.yfilter != YFilter.not_set or
                    self.rsvpsendernumber.yfilter != YFilter.not_set or
                    self.rsvpsenderaddr.yfilter != YFilter.not_set or
                    self.rsvpsenderaddrlength.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecbreak.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecctrlloadbreak.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecctrlloadhopcount.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecctrlloadminlatency.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecctrlloadmtu.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecctrlloadpathbw.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecctrlloadsvc.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecguaranteedbreak.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecguaranteedcsum.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecguaranteedctot.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecguaranteeddsum.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecguaranteeddtot.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecguaranteedhopcount.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecguaranteedminlatency.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecguaranteedmtu.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecguaranteedpathbw.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecguaranteedsvc.yfilter != YFilter.not_set or
                    self.rsvpsenderadspechopcount.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecminlatency.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecmtu.yfilter != YFilter.not_set or
                    self.rsvpsenderadspecpathbw.yfilter != YFilter.not_set or
                    self.rsvpsenderdestaddr.yfilter != YFilter.not_set or
                    self.rsvpsenderdestaddrlength.yfilter != YFilter.not_set or
                    self.rsvpsenderdestport.yfilter != YFilter.not_set or
                    self.rsvpsenderflowid.yfilter != YFilter.not_set or
                    self.rsvpsenderhopaddr.yfilter != YFilter.not_set or
                    self.rsvpsenderhoplih.yfilter != YFilter.not_set or
                    self.rsvpsenderinterface.yfilter != YFilter.not_set or
                    self.rsvpsenderinterval.yfilter != YFilter.not_set or
                    self.rsvpsenderlastchange.yfilter != YFilter.not_set or
                    self.rsvpsenderpolicy.yfilter != YFilter.not_set or
                    self.rsvpsenderport.yfilter != YFilter.not_set or
                    self.rsvpsenderprotocol.yfilter != YFilter.not_set or
                    self.rsvpsenderrsvphop.yfilter != YFilter.not_set or
                    self.rsvpsenderstatus.yfilter != YFilter.not_set or
                    self.rsvpsendertspecburst.yfilter != YFilter.not_set or
                    self.rsvpsendertspecmaxtu.yfilter != YFilter.not_set or
                    self.rsvpsendertspecmintu.yfilter != YFilter.not_set or
                    self.rsvpsendertspecpeakrate.yfilter != YFilter.not_set or
                    self.rsvpsendertspecrate.yfilter != YFilter.not_set or
                    self.rsvpsenderttl.yfilter != YFilter.not_set or
                    self.rsvpsendertype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rsvpSenderEntry" + "[rsvpSessionNumber='" + self.rsvpsessionnumber.get() + "']" + "[rsvpSenderNumber='" + self.rsvpsendernumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RSVP-MIB:RSVP-MIB/rsvpSenderTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rsvpsessionnumber.is_set or self.rsvpsessionnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsessionnumber.get_name_leafdata())
                if (self.rsvpsendernumber.is_set or self.rsvpsendernumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsendernumber.get_name_leafdata())
                if (self.rsvpsenderaddr.is_set or self.rsvpsenderaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderaddr.get_name_leafdata())
                if (self.rsvpsenderaddrlength.is_set or self.rsvpsenderaddrlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderaddrlength.get_name_leafdata())
                if (self.rsvpsenderadspecbreak.is_set or self.rsvpsenderadspecbreak.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecbreak.get_name_leafdata())
                if (self.rsvpsenderadspecctrlloadbreak.is_set or self.rsvpsenderadspecctrlloadbreak.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecctrlloadbreak.get_name_leafdata())
                if (self.rsvpsenderadspecctrlloadhopcount.is_set or self.rsvpsenderadspecctrlloadhopcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecctrlloadhopcount.get_name_leafdata())
                if (self.rsvpsenderadspecctrlloadminlatency.is_set or self.rsvpsenderadspecctrlloadminlatency.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecctrlloadminlatency.get_name_leafdata())
                if (self.rsvpsenderadspecctrlloadmtu.is_set or self.rsvpsenderadspecctrlloadmtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecctrlloadmtu.get_name_leafdata())
                if (self.rsvpsenderadspecctrlloadpathbw.is_set or self.rsvpsenderadspecctrlloadpathbw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecctrlloadpathbw.get_name_leafdata())
                if (self.rsvpsenderadspecctrlloadsvc.is_set or self.rsvpsenderadspecctrlloadsvc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecctrlloadsvc.get_name_leafdata())
                if (self.rsvpsenderadspecguaranteedbreak.is_set or self.rsvpsenderadspecguaranteedbreak.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecguaranteedbreak.get_name_leafdata())
                if (self.rsvpsenderadspecguaranteedcsum.is_set or self.rsvpsenderadspecguaranteedcsum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecguaranteedcsum.get_name_leafdata())
                if (self.rsvpsenderadspecguaranteedctot.is_set or self.rsvpsenderadspecguaranteedctot.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecguaranteedctot.get_name_leafdata())
                if (self.rsvpsenderadspecguaranteeddsum.is_set or self.rsvpsenderadspecguaranteeddsum.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecguaranteeddsum.get_name_leafdata())
                if (self.rsvpsenderadspecguaranteeddtot.is_set or self.rsvpsenderadspecguaranteeddtot.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecguaranteeddtot.get_name_leafdata())
                if (self.rsvpsenderadspecguaranteedhopcount.is_set or self.rsvpsenderadspecguaranteedhopcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecguaranteedhopcount.get_name_leafdata())
                if (self.rsvpsenderadspecguaranteedminlatency.is_set or self.rsvpsenderadspecguaranteedminlatency.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecguaranteedminlatency.get_name_leafdata())
                if (self.rsvpsenderadspecguaranteedmtu.is_set or self.rsvpsenderadspecguaranteedmtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecguaranteedmtu.get_name_leafdata())
                if (self.rsvpsenderadspecguaranteedpathbw.is_set or self.rsvpsenderadspecguaranteedpathbw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecguaranteedpathbw.get_name_leafdata())
                if (self.rsvpsenderadspecguaranteedsvc.is_set or self.rsvpsenderadspecguaranteedsvc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecguaranteedsvc.get_name_leafdata())
                if (self.rsvpsenderadspechopcount.is_set or self.rsvpsenderadspechopcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspechopcount.get_name_leafdata())
                if (self.rsvpsenderadspecminlatency.is_set or self.rsvpsenderadspecminlatency.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecminlatency.get_name_leafdata())
                if (self.rsvpsenderadspecmtu.is_set or self.rsvpsenderadspecmtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecmtu.get_name_leafdata())
                if (self.rsvpsenderadspecpathbw.is_set or self.rsvpsenderadspecpathbw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderadspecpathbw.get_name_leafdata())
                if (self.rsvpsenderdestaddr.is_set or self.rsvpsenderdestaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderdestaddr.get_name_leafdata())
                if (self.rsvpsenderdestaddrlength.is_set or self.rsvpsenderdestaddrlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderdestaddrlength.get_name_leafdata())
                if (self.rsvpsenderdestport.is_set or self.rsvpsenderdestport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderdestport.get_name_leafdata())
                if (self.rsvpsenderflowid.is_set or self.rsvpsenderflowid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderflowid.get_name_leafdata())
                if (self.rsvpsenderhopaddr.is_set or self.rsvpsenderhopaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderhopaddr.get_name_leafdata())
                if (self.rsvpsenderhoplih.is_set or self.rsvpsenderhoplih.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderhoplih.get_name_leafdata())
                if (self.rsvpsenderinterface.is_set or self.rsvpsenderinterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderinterface.get_name_leafdata())
                if (self.rsvpsenderinterval.is_set or self.rsvpsenderinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderinterval.get_name_leafdata())
                if (self.rsvpsenderlastchange.is_set or self.rsvpsenderlastchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderlastchange.get_name_leafdata())
                if (self.rsvpsenderpolicy.is_set or self.rsvpsenderpolicy.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderpolicy.get_name_leafdata())
                if (self.rsvpsenderport.is_set or self.rsvpsenderport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderport.get_name_leafdata())
                if (self.rsvpsenderprotocol.is_set or self.rsvpsenderprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderprotocol.get_name_leafdata())
                if (self.rsvpsenderrsvphop.is_set or self.rsvpsenderrsvphop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderrsvphop.get_name_leafdata())
                if (self.rsvpsenderstatus.is_set or self.rsvpsenderstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderstatus.get_name_leafdata())
                if (self.rsvpsendertspecburst.is_set or self.rsvpsendertspecburst.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsendertspecburst.get_name_leafdata())
                if (self.rsvpsendertspecmaxtu.is_set or self.rsvpsendertspecmaxtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsendertspecmaxtu.get_name_leafdata())
                if (self.rsvpsendertspecmintu.is_set or self.rsvpsendertspecmintu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsendertspecmintu.get_name_leafdata())
                if (self.rsvpsendertspecpeakrate.is_set or self.rsvpsendertspecpeakrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsendertspecpeakrate.get_name_leafdata())
                if (self.rsvpsendertspecrate.is_set or self.rsvpsendertspecrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsendertspecrate.get_name_leafdata())
                if (self.rsvpsenderttl.is_set or self.rsvpsenderttl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderttl.get_name_leafdata())
                if (self.rsvpsendertype.is_set or self.rsvpsendertype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsendertype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rsvpSessionNumber" or name == "rsvpSenderNumber" or name == "rsvpSenderAddr" or name == "rsvpSenderAddrLength" or name == "rsvpSenderAdspecBreak" or name == "rsvpSenderAdspecCtrlLoadBreak" or name == "rsvpSenderAdspecCtrlLoadHopCount" or name == "rsvpSenderAdspecCtrlLoadMinLatency" or name == "rsvpSenderAdspecCtrlLoadMtu" or name == "rsvpSenderAdspecCtrlLoadPathBw" or name == "rsvpSenderAdspecCtrlLoadSvc" or name == "rsvpSenderAdspecGuaranteedBreak" or name == "rsvpSenderAdspecGuaranteedCsum" or name == "rsvpSenderAdspecGuaranteedCtot" or name == "rsvpSenderAdspecGuaranteedDsum" or name == "rsvpSenderAdspecGuaranteedDtot" or name == "rsvpSenderAdspecGuaranteedHopCount" or name == "rsvpSenderAdspecGuaranteedMinLatency" or name == "rsvpSenderAdspecGuaranteedMtu" or name == "rsvpSenderAdspecGuaranteedPathBw" or name == "rsvpSenderAdspecGuaranteedSvc" or name == "rsvpSenderAdspecHopCount" or name == "rsvpSenderAdspecMinLatency" or name == "rsvpSenderAdspecMtu" or name == "rsvpSenderAdspecPathBw" or name == "rsvpSenderDestAddr" or name == "rsvpSenderDestAddrLength" or name == "rsvpSenderDestPort" or name == "rsvpSenderFlowId" or name == "rsvpSenderHopAddr" or name == "rsvpSenderHopLih" or name == "rsvpSenderInterface" or name == "rsvpSenderInterval" or name == "rsvpSenderLastChange" or name == "rsvpSenderPolicy" or name == "rsvpSenderPort" or name == "rsvpSenderProtocol" or name == "rsvpSenderRSVPHop" or name == "rsvpSenderStatus" or name == "rsvpSenderTSpecBurst" or name == "rsvpSenderTSpecMaxTU" or name == "rsvpSenderTSpecMinTU" or name == "rsvpSenderTSpecPeakRate" or name == "rsvpSenderTSpecRate" or name == "rsvpSenderTTL" or name == "rsvpSenderType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rsvpSessionNumber"):
                    self.rsvpsessionnumber = value
                    self.rsvpsessionnumber.value_namespace = name_space
                    self.rsvpsessionnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderNumber"):
                    self.rsvpsendernumber = value
                    self.rsvpsendernumber.value_namespace = name_space
                    self.rsvpsendernumber.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAddr"):
                    self.rsvpsenderaddr = value
                    self.rsvpsenderaddr.value_namespace = name_space
                    self.rsvpsenderaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAddrLength"):
                    self.rsvpsenderaddrlength = value
                    self.rsvpsenderaddrlength.value_namespace = name_space
                    self.rsvpsenderaddrlength.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecBreak"):
                    self.rsvpsenderadspecbreak = value
                    self.rsvpsenderadspecbreak.value_namespace = name_space
                    self.rsvpsenderadspecbreak.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecCtrlLoadBreak"):
                    self.rsvpsenderadspecctrlloadbreak = value
                    self.rsvpsenderadspecctrlloadbreak.value_namespace = name_space
                    self.rsvpsenderadspecctrlloadbreak.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecCtrlLoadHopCount"):
                    self.rsvpsenderadspecctrlloadhopcount = value
                    self.rsvpsenderadspecctrlloadhopcount.value_namespace = name_space
                    self.rsvpsenderadspecctrlloadhopcount.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecCtrlLoadMinLatency"):
                    self.rsvpsenderadspecctrlloadminlatency = value
                    self.rsvpsenderadspecctrlloadminlatency.value_namespace = name_space
                    self.rsvpsenderadspecctrlloadminlatency.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecCtrlLoadMtu"):
                    self.rsvpsenderadspecctrlloadmtu = value
                    self.rsvpsenderadspecctrlloadmtu.value_namespace = name_space
                    self.rsvpsenderadspecctrlloadmtu.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecCtrlLoadPathBw"):
                    self.rsvpsenderadspecctrlloadpathbw = value
                    self.rsvpsenderadspecctrlloadpathbw.value_namespace = name_space
                    self.rsvpsenderadspecctrlloadpathbw.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecCtrlLoadSvc"):
                    self.rsvpsenderadspecctrlloadsvc = value
                    self.rsvpsenderadspecctrlloadsvc.value_namespace = name_space
                    self.rsvpsenderadspecctrlloadsvc.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecGuaranteedBreak"):
                    self.rsvpsenderadspecguaranteedbreak = value
                    self.rsvpsenderadspecguaranteedbreak.value_namespace = name_space
                    self.rsvpsenderadspecguaranteedbreak.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecGuaranteedCsum"):
                    self.rsvpsenderadspecguaranteedcsum = value
                    self.rsvpsenderadspecguaranteedcsum.value_namespace = name_space
                    self.rsvpsenderadspecguaranteedcsum.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecGuaranteedCtot"):
                    self.rsvpsenderadspecguaranteedctot = value
                    self.rsvpsenderadspecguaranteedctot.value_namespace = name_space
                    self.rsvpsenderadspecguaranteedctot.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecGuaranteedDsum"):
                    self.rsvpsenderadspecguaranteeddsum = value
                    self.rsvpsenderadspecguaranteeddsum.value_namespace = name_space
                    self.rsvpsenderadspecguaranteeddsum.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecGuaranteedDtot"):
                    self.rsvpsenderadspecguaranteeddtot = value
                    self.rsvpsenderadspecguaranteeddtot.value_namespace = name_space
                    self.rsvpsenderadspecguaranteeddtot.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecGuaranteedHopCount"):
                    self.rsvpsenderadspecguaranteedhopcount = value
                    self.rsvpsenderadspecguaranteedhopcount.value_namespace = name_space
                    self.rsvpsenderadspecguaranteedhopcount.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecGuaranteedMinLatency"):
                    self.rsvpsenderadspecguaranteedminlatency = value
                    self.rsvpsenderadspecguaranteedminlatency.value_namespace = name_space
                    self.rsvpsenderadspecguaranteedminlatency.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecGuaranteedMtu"):
                    self.rsvpsenderadspecguaranteedmtu = value
                    self.rsvpsenderadspecguaranteedmtu.value_namespace = name_space
                    self.rsvpsenderadspecguaranteedmtu.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecGuaranteedPathBw"):
                    self.rsvpsenderadspecguaranteedpathbw = value
                    self.rsvpsenderadspecguaranteedpathbw.value_namespace = name_space
                    self.rsvpsenderadspecguaranteedpathbw.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecGuaranteedSvc"):
                    self.rsvpsenderadspecguaranteedsvc = value
                    self.rsvpsenderadspecguaranteedsvc.value_namespace = name_space
                    self.rsvpsenderadspecguaranteedsvc.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecHopCount"):
                    self.rsvpsenderadspechopcount = value
                    self.rsvpsenderadspechopcount.value_namespace = name_space
                    self.rsvpsenderadspechopcount.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecMinLatency"):
                    self.rsvpsenderadspecminlatency = value
                    self.rsvpsenderadspecminlatency.value_namespace = name_space
                    self.rsvpsenderadspecminlatency.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecMtu"):
                    self.rsvpsenderadspecmtu = value
                    self.rsvpsenderadspecmtu.value_namespace = name_space
                    self.rsvpsenderadspecmtu.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderAdspecPathBw"):
                    self.rsvpsenderadspecpathbw = value
                    self.rsvpsenderadspecpathbw.value_namespace = name_space
                    self.rsvpsenderadspecpathbw.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderDestAddr"):
                    self.rsvpsenderdestaddr = value
                    self.rsvpsenderdestaddr.value_namespace = name_space
                    self.rsvpsenderdestaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderDestAddrLength"):
                    self.rsvpsenderdestaddrlength = value
                    self.rsvpsenderdestaddrlength.value_namespace = name_space
                    self.rsvpsenderdestaddrlength.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderDestPort"):
                    self.rsvpsenderdestport = value
                    self.rsvpsenderdestport.value_namespace = name_space
                    self.rsvpsenderdestport.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderFlowId"):
                    self.rsvpsenderflowid = value
                    self.rsvpsenderflowid.value_namespace = name_space
                    self.rsvpsenderflowid.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderHopAddr"):
                    self.rsvpsenderhopaddr = value
                    self.rsvpsenderhopaddr.value_namespace = name_space
                    self.rsvpsenderhopaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderHopLih"):
                    self.rsvpsenderhoplih = value
                    self.rsvpsenderhoplih.value_namespace = name_space
                    self.rsvpsenderhoplih.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderInterface"):
                    self.rsvpsenderinterface = value
                    self.rsvpsenderinterface.value_namespace = name_space
                    self.rsvpsenderinterface.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderInterval"):
                    self.rsvpsenderinterval = value
                    self.rsvpsenderinterval.value_namespace = name_space
                    self.rsvpsenderinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderLastChange"):
                    self.rsvpsenderlastchange = value
                    self.rsvpsenderlastchange.value_namespace = name_space
                    self.rsvpsenderlastchange.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderPolicy"):
                    self.rsvpsenderpolicy = value
                    self.rsvpsenderpolicy.value_namespace = name_space
                    self.rsvpsenderpolicy.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderPort"):
                    self.rsvpsenderport = value
                    self.rsvpsenderport.value_namespace = name_space
                    self.rsvpsenderport.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderProtocol"):
                    self.rsvpsenderprotocol = value
                    self.rsvpsenderprotocol.value_namespace = name_space
                    self.rsvpsenderprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderRSVPHop"):
                    self.rsvpsenderrsvphop = value
                    self.rsvpsenderrsvphop.value_namespace = name_space
                    self.rsvpsenderrsvphop.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderStatus"):
                    self.rsvpsenderstatus = value
                    self.rsvpsenderstatus.value_namespace = name_space
                    self.rsvpsenderstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderTSpecBurst"):
                    self.rsvpsendertspecburst = value
                    self.rsvpsendertspecburst.value_namespace = name_space
                    self.rsvpsendertspecburst.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderTSpecMaxTU"):
                    self.rsvpsendertspecmaxtu = value
                    self.rsvpsendertspecmaxtu.value_namespace = name_space
                    self.rsvpsendertspecmaxtu.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderTSpecMinTU"):
                    self.rsvpsendertspecmintu = value
                    self.rsvpsendertspecmintu.value_namespace = name_space
                    self.rsvpsendertspecmintu.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderTSpecPeakRate"):
                    self.rsvpsendertspecpeakrate = value
                    self.rsvpsendertspecpeakrate.value_namespace = name_space
                    self.rsvpsendertspecpeakrate.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderTSpecRate"):
                    self.rsvpsendertspecrate = value
                    self.rsvpsendertspecrate.value_namespace = name_space
                    self.rsvpsendertspecrate.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderTTL"):
                    self.rsvpsenderttl = value
                    self.rsvpsenderttl.value_namespace = name_space
                    self.rsvpsenderttl.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderType"):
                    self.rsvpsendertype = value
                    self.rsvpsendertype.value_namespace = name_space
                    self.rsvpsendertype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rsvpsenderentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rsvpsenderentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rsvpSenderTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RSVP-MIB:RSVP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rsvpSenderEntry"):
                for c in self.rsvpsenderentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RsvpMib.Rsvpsendertable.Rsvpsenderentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rsvpsenderentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rsvpSenderEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Rsvpsenderoutinterfacetable(Entity):
        """
        List of outgoing interfaces	that PATH messages
        use.	 The  ifIndex  is the ifIndex value of the
        egress interface.
        
        .. attribute:: rsvpsenderoutinterfaceentry
        
        	List of outgoing interfaces	that a	particular PATH	message	has
        	**type**\: list of    :py:class:`Rsvpsenderoutinterfaceentry <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsenderoutinterfacetable.Rsvpsenderoutinterfaceentry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RsvpMib.Rsvpsenderoutinterfacetable, self).__init__()

            self.yang_name = "rsvpSenderOutInterfaceTable"
            self.yang_parent_name = "RSVP-MIB"

            self.rsvpsenderoutinterfaceentry = YList(self)

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
                        super(RsvpMib.Rsvpsenderoutinterfacetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RsvpMib.Rsvpsenderoutinterfacetable, self).__setattr__(name, value)


        class Rsvpsenderoutinterfaceentry(Entity):
            """
            List of outgoing interfaces	that a	particular
            PATH	message	has.
            
            .. attribute:: rsvpsessionnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsessionnumber <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsessiontable.Rsvpsessionentry>`
            
            .. attribute:: rsvpsendernumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsendernumber <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsendertable.Rsvpsenderentry>`
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: rsvpsenderoutinterfacestatus
            
            	'active' for all active PATH messages
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RsvpMib.Rsvpsenderoutinterfacetable.Rsvpsenderoutinterfaceentry, self).__init__()

                self.yang_name = "rsvpSenderOutInterfaceEntry"
                self.yang_parent_name = "rsvpSenderOutInterfaceTable"

                self.rsvpsessionnumber = YLeaf(YType.str, "rsvpSessionNumber")

                self.rsvpsendernumber = YLeaf(YType.str, "rsvpSenderNumber")

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.rsvpsenderoutinterfacestatus = YLeaf(YType.enumeration, "rsvpSenderOutInterfaceStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rsvpsessionnumber",
                                "rsvpsendernumber",
                                "ifindex",
                                "rsvpsenderoutinterfacestatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RsvpMib.Rsvpsenderoutinterfacetable.Rsvpsenderoutinterfaceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RsvpMib.Rsvpsenderoutinterfacetable.Rsvpsenderoutinterfaceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rsvpsessionnumber.is_set or
                    self.rsvpsendernumber.is_set or
                    self.ifindex.is_set or
                    self.rsvpsenderoutinterfacestatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rsvpsessionnumber.yfilter != YFilter.not_set or
                    self.rsvpsendernumber.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.rsvpsenderoutinterfacestatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rsvpSenderOutInterfaceEntry" + "[rsvpSessionNumber='" + self.rsvpsessionnumber.get() + "']" + "[rsvpSenderNumber='" + self.rsvpsendernumber.get() + "']" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RSVP-MIB:RSVP-MIB/rsvpSenderOutInterfaceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rsvpsessionnumber.is_set or self.rsvpsessionnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsessionnumber.get_name_leafdata())
                if (self.rsvpsendernumber.is_set or self.rsvpsendernumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsendernumber.get_name_leafdata())
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.rsvpsenderoutinterfacestatus.is_set or self.rsvpsenderoutinterfacestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsenderoutinterfacestatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rsvpSessionNumber" or name == "rsvpSenderNumber" or name == "ifIndex" or name == "rsvpSenderOutInterfaceStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rsvpSessionNumber"):
                    self.rsvpsessionnumber = value
                    self.rsvpsessionnumber.value_namespace = name_space
                    self.rsvpsessionnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderNumber"):
                    self.rsvpsendernumber = value
                    self.rsvpsendernumber.value_namespace = name_space
                    self.rsvpsendernumber.value_namespace_prefix = name_space_prefix
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpSenderOutInterfaceStatus"):
                    self.rsvpsenderoutinterfacestatus = value
                    self.rsvpsenderoutinterfacestatus.value_namespace = name_space
                    self.rsvpsenderoutinterfacestatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rsvpsenderoutinterfaceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rsvpsenderoutinterfaceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rsvpSenderOutInterfaceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RSVP-MIB:RSVP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rsvpSenderOutInterfaceEntry"):
                for c in self.rsvpsenderoutinterfaceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RsvpMib.Rsvpsenderoutinterfacetable.Rsvpsenderoutinterfaceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rsvpsenderoutinterfaceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rsvpSenderOutInterfaceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Rsvpresvtable(Entity):
        """
        Information	describing the	state  information
        displayed by	receivers in RESV messages.
        
        .. attribute:: rsvpresventry
        
        	Information	describing the	state  information displayed  by  a single receiver's RESV message concerning a	single sender
        	**type**\: list of    :py:class:`Rsvpresventry <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpresvtable.Rsvpresventry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RsvpMib.Rsvpresvtable, self).__init__()

            self.yang_name = "rsvpResvTable"
            self.yang_parent_name = "RSVP-MIB"

            self.rsvpresventry = YList(self)

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
                        super(RsvpMib.Rsvpresvtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RsvpMib.Rsvpresvtable, self).__setattr__(name, value)


        class Rsvpresventry(Entity):
            """
            Information	describing the	state  information
            displayed  by  a single receiver's RESV message
            concerning a	single sender.
            
            .. attribute:: rsvpsessionnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsessionnumber <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsessiontable.Rsvpsessionentry>`
            
            .. attribute:: rsvpresvnumber  <key>
            
            	The	number of this reservation request.   This is  for  SNMP Indexing purposes only	and has	no relation to any protocol value
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvdestaddr
            
            	The	destination address used by all	senders	in this	 session.   This object	may not	be changed when	the  value  of	the  RowStatus	object	is 'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpresvdestaddrlength
            
            	The	length of the destination address in bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: rsvpresvdestport
            
            	The	 UDP  or  TCP  port  number  used   as	 a destination	 port  for  all	 senders  in  this session.  If	the IP protocol	in use,	 specified by  rsvpResvProtocol,  is  50 (ESP) or 51 (AH), this	 represents  a	virtual	 destination  port number.   A value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: rsvpresvexplicit
            
            	If TRUE, individual	senders	are  listed  using Filter  Specifications.   If	FALSE, all senders are implicitly selected.  The Scope Object will contain  a list of senders that need	to receive this	reservation request  for  the  purpose	of routing the RESV message
            	**type**\:  bool
            
            .. attribute:: rsvpresvflowid
            
            	The	flow ID	that this receiver  is	using,	if this	 is  an	IPv6 session
            	**type**\:  int
            
            	**range:** 0..16777215
            
            .. attribute:: rsvpresvhopaddr
            
            	The	address	used by	the next RSVP  hop  (which may be the ultimate receiver)
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpresvhoplih
            
            	The	Logical	Interface Handle received from the previous  RSVP  hop	(which may be the ultimate receiver)
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: rsvpresvinterface
            
            	The	ifIndex	value of the  interface	 on  which this	RESV message was most recently received
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: rsvpresvinterval
            
            	The	 interval  between  refresh  messages	as advertised by the Next Hop
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvlastchange
            
            	The	 time  of  the	 last	change	 in   this reservation	request;  This is either the first time	it was received	or the time  of	 the  most recent change in parameters
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpresvpolicy
            
            	The	contents of the	policy	object,	 displayed as an uninterpreted string of octets, including the object header.  In the absence of  such	an object, this	should be of zero length
            	**type**\:  str
            
            	**length:** 0..65536
            
            .. attribute:: rsvpresvport
            
            	The	UDP or TCP port	number used  as	 a  source port	 for  this sender in this session.  If the IP	 protocol    in	   use,	   specified	by rsvpResvProtocol  is	 50 (ESP) or 51	(AH), this represents a	generalized port identifier (GPI). A  value of zero indicates that the IP protocol in use does not have	ports.	 This  object  may not	be changed when	the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: rsvpresvprotocol
            
            	The	IP Protocol used by  this  session.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: rsvpresvrspecrate
            
            	If the requested  service  is  Guaranteed,	as specified   by  rsvpResvService,  this  is  the clearing  rate   that   is	being	requested. Otherwise,  it is zero, or the agent	may return noSuchValue
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvrspecslack
            
            	If the requested  service  is  Guaranteed,	as specified by	rsvpResvService, this is the delay slack.  Otherwise, it is zero, or the agent may return noSuchValue
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpresvrsvphop
            
            	If TRUE, the node believes that  the  previous IP  hop  is	an  RSVP  hop.	If FALSE, the node believes that the previous IP hop may not be	an RSVP	hop
            	**type**\:  bool
            
            .. attribute:: rsvpresvscope
            
            	The	contents of the	scope object, displayed	as an  uninterpreted  string  of octets, including the object header.  In the absence of  such	an object, this	should be of zero length.  If the length  is  non\-zero,	 this  contains	 a series of IP4 or IP6	addresses
            	**type**\:  str
            
            	**length:** 0..65536
            
            .. attribute:: rsvpresvsenderaddr
            
            	The	source address of the sender  selected	by this	 reservation.	The  value  of	all zeroes indicates 'all senders'.  This object  may  not be  changed	when  the  value  of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpresvsenderaddrlength
            
            	The	length of the sender's	address	 in  bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: rsvpresvservice
            
            	The	QoS Service  classification  requested	by the receiver
            	**type**\:   :py:class:`Qosservice <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.Qosservice>`
            
            .. attribute:: rsvpresvshared
            
            	If TRUE, a reservation shared among	senders	is requested.  If FALSE, a reservation specific	to this	sender is requested
            	**type**\:  bool
            
            .. attribute:: rsvpresvstatus
            
            	'active' for all active RESV  messages.   This object  may	be  used  to  install  static RESV information or delete RESV information
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: rsvpresvtspecburst
            
            	The	size of	the largest  burst  expected  from the sender at a time.  If this is less than	 the  sender's	advertised burst  size,	the receiver is	asking the network to provide flow pacing  beyond  what	 would	be provided   under   normal  circumstances.  Such pacing is at	the network's option
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bytes
            
            .. attribute:: rsvpresvtspecmaxtu
            
            	The	maximum	message	size for  this	flow.  The admission  algorithm	 will  reject TSpecs whose Maximum Transmission	Unit, plus  the	 interface headers, exceed the interface MTU
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvtspecmintu
            
            	The	minimum	message	size for  this	flow.  The policing  algorithm will treat smaller messages as though they are this size
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvtspecpeakrate
            
            	The	Peak Bit Rate of the sender's data stream. Traffic  arrival is not expected to exceed this rate	at any time, apart  from  the  effects	of jitter in the network.  If not specified in the TSpec, this returns zero or noSuchValue
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvtspecrate
            
            	The	Average	Bit  Rate  of  the  sender's  data stream.    Within  a	 transmission  burst,  the arrival   rate    may    be	  as	fast	as rsvpResvTSpecPeakRate   (if	supported  by  the service model); however, averaged across two	or more	 burst	intervals,  the	 rate  should  not exceed rsvpResvTSpecRate.  Note	that this is a prediction, often based	on the	general	 capability  of	a type of codec	or particular encoding;	the measured average  rate may be significantly	lower
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvttl
            
            	The	TTL value in the RSVP header that was last received
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: rsvpresvtype
            
            	The	type of	session	(IP4, IP6, IP6	with  flow information,	etc)
            	**type**\:  int
            
            	**range:** 1..255
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RsvpMib.Rsvpresvtable.Rsvpresventry, self).__init__()

                self.yang_name = "rsvpResvEntry"
                self.yang_parent_name = "rsvpResvTable"

                self.rsvpsessionnumber = YLeaf(YType.str, "rsvpSessionNumber")

                self.rsvpresvnumber = YLeaf(YType.int32, "rsvpResvNumber")

                self.rsvpresvdestaddr = YLeaf(YType.str, "rsvpResvDestAddr")

                self.rsvpresvdestaddrlength = YLeaf(YType.int32, "rsvpResvDestAddrLength")

                self.rsvpresvdestport = YLeaf(YType.str, "rsvpResvDestPort")

                self.rsvpresvexplicit = YLeaf(YType.boolean, "rsvpResvExplicit")

                self.rsvpresvflowid = YLeaf(YType.int32, "rsvpResvFlowId")

                self.rsvpresvhopaddr = YLeaf(YType.str, "rsvpResvHopAddr")

                self.rsvpresvhoplih = YLeaf(YType.int32, "rsvpResvHopLih")

                self.rsvpresvinterface = YLeaf(YType.int32, "rsvpResvInterface")

                self.rsvpresvinterval = YLeaf(YType.int32, "rsvpResvInterval")

                self.rsvpresvlastchange = YLeaf(YType.uint32, "rsvpResvLastChange")

                self.rsvpresvpolicy = YLeaf(YType.str, "rsvpResvPolicy")

                self.rsvpresvport = YLeaf(YType.str, "rsvpResvPort")

                self.rsvpresvprotocol = YLeaf(YType.int32, "rsvpResvProtocol")

                self.rsvpresvrspecrate = YLeaf(YType.int32, "rsvpResvRSpecRate")

                self.rsvpresvrspecslack = YLeaf(YType.int32, "rsvpResvRSpecSlack")

                self.rsvpresvrsvphop = YLeaf(YType.boolean, "rsvpResvRSVPHop")

                self.rsvpresvscope = YLeaf(YType.str, "rsvpResvScope")

                self.rsvpresvsenderaddr = YLeaf(YType.str, "rsvpResvSenderAddr")

                self.rsvpresvsenderaddrlength = YLeaf(YType.int32, "rsvpResvSenderAddrLength")

                self.rsvpresvservice = YLeaf(YType.enumeration, "rsvpResvService")

                self.rsvpresvshared = YLeaf(YType.boolean, "rsvpResvShared")

                self.rsvpresvstatus = YLeaf(YType.enumeration, "rsvpResvStatus")

                self.rsvpresvtspecburst = YLeaf(YType.int32, "rsvpResvTSpecBurst")

                self.rsvpresvtspecmaxtu = YLeaf(YType.int32, "rsvpResvTSpecMaxTU")

                self.rsvpresvtspecmintu = YLeaf(YType.int32, "rsvpResvTSpecMinTU")

                self.rsvpresvtspecpeakrate = YLeaf(YType.int32, "rsvpResvTSpecPeakRate")

                self.rsvpresvtspecrate = YLeaf(YType.int32, "rsvpResvTSpecRate")

                self.rsvpresvttl = YLeaf(YType.int32, "rsvpResvTTL")

                self.rsvpresvtype = YLeaf(YType.int32, "rsvpResvType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rsvpsessionnumber",
                                "rsvpresvnumber",
                                "rsvpresvdestaddr",
                                "rsvpresvdestaddrlength",
                                "rsvpresvdestport",
                                "rsvpresvexplicit",
                                "rsvpresvflowid",
                                "rsvpresvhopaddr",
                                "rsvpresvhoplih",
                                "rsvpresvinterface",
                                "rsvpresvinterval",
                                "rsvpresvlastchange",
                                "rsvpresvpolicy",
                                "rsvpresvport",
                                "rsvpresvprotocol",
                                "rsvpresvrspecrate",
                                "rsvpresvrspecslack",
                                "rsvpresvrsvphop",
                                "rsvpresvscope",
                                "rsvpresvsenderaddr",
                                "rsvpresvsenderaddrlength",
                                "rsvpresvservice",
                                "rsvpresvshared",
                                "rsvpresvstatus",
                                "rsvpresvtspecburst",
                                "rsvpresvtspecmaxtu",
                                "rsvpresvtspecmintu",
                                "rsvpresvtspecpeakrate",
                                "rsvpresvtspecrate",
                                "rsvpresvttl",
                                "rsvpresvtype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RsvpMib.Rsvpresvtable.Rsvpresventry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RsvpMib.Rsvpresvtable.Rsvpresventry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rsvpsessionnumber.is_set or
                    self.rsvpresvnumber.is_set or
                    self.rsvpresvdestaddr.is_set or
                    self.rsvpresvdestaddrlength.is_set or
                    self.rsvpresvdestport.is_set or
                    self.rsvpresvexplicit.is_set or
                    self.rsvpresvflowid.is_set or
                    self.rsvpresvhopaddr.is_set or
                    self.rsvpresvhoplih.is_set or
                    self.rsvpresvinterface.is_set or
                    self.rsvpresvinterval.is_set or
                    self.rsvpresvlastchange.is_set or
                    self.rsvpresvpolicy.is_set or
                    self.rsvpresvport.is_set or
                    self.rsvpresvprotocol.is_set or
                    self.rsvpresvrspecrate.is_set or
                    self.rsvpresvrspecslack.is_set or
                    self.rsvpresvrsvphop.is_set or
                    self.rsvpresvscope.is_set or
                    self.rsvpresvsenderaddr.is_set or
                    self.rsvpresvsenderaddrlength.is_set or
                    self.rsvpresvservice.is_set or
                    self.rsvpresvshared.is_set or
                    self.rsvpresvstatus.is_set or
                    self.rsvpresvtspecburst.is_set or
                    self.rsvpresvtspecmaxtu.is_set or
                    self.rsvpresvtspecmintu.is_set or
                    self.rsvpresvtspecpeakrate.is_set or
                    self.rsvpresvtspecrate.is_set or
                    self.rsvpresvttl.is_set or
                    self.rsvpresvtype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rsvpsessionnumber.yfilter != YFilter.not_set or
                    self.rsvpresvnumber.yfilter != YFilter.not_set or
                    self.rsvpresvdestaddr.yfilter != YFilter.not_set or
                    self.rsvpresvdestaddrlength.yfilter != YFilter.not_set or
                    self.rsvpresvdestport.yfilter != YFilter.not_set or
                    self.rsvpresvexplicit.yfilter != YFilter.not_set or
                    self.rsvpresvflowid.yfilter != YFilter.not_set or
                    self.rsvpresvhopaddr.yfilter != YFilter.not_set or
                    self.rsvpresvhoplih.yfilter != YFilter.not_set or
                    self.rsvpresvinterface.yfilter != YFilter.not_set or
                    self.rsvpresvinterval.yfilter != YFilter.not_set or
                    self.rsvpresvlastchange.yfilter != YFilter.not_set or
                    self.rsvpresvpolicy.yfilter != YFilter.not_set or
                    self.rsvpresvport.yfilter != YFilter.not_set or
                    self.rsvpresvprotocol.yfilter != YFilter.not_set or
                    self.rsvpresvrspecrate.yfilter != YFilter.not_set or
                    self.rsvpresvrspecslack.yfilter != YFilter.not_set or
                    self.rsvpresvrsvphop.yfilter != YFilter.not_set or
                    self.rsvpresvscope.yfilter != YFilter.not_set or
                    self.rsvpresvsenderaddr.yfilter != YFilter.not_set or
                    self.rsvpresvsenderaddrlength.yfilter != YFilter.not_set or
                    self.rsvpresvservice.yfilter != YFilter.not_set or
                    self.rsvpresvshared.yfilter != YFilter.not_set or
                    self.rsvpresvstatus.yfilter != YFilter.not_set or
                    self.rsvpresvtspecburst.yfilter != YFilter.not_set or
                    self.rsvpresvtspecmaxtu.yfilter != YFilter.not_set or
                    self.rsvpresvtspecmintu.yfilter != YFilter.not_set or
                    self.rsvpresvtspecpeakrate.yfilter != YFilter.not_set or
                    self.rsvpresvtspecrate.yfilter != YFilter.not_set or
                    self.rsvpresvttl.yfilter != YFilter.not_set or
                    self.rsvpresvtype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rsvpResvEntry" + "[rsvpSessionNumber='" + self.rsvpsessionnumber.get() + "']" + "[rsvpResvNumber='" + self.rsvpresvnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RSVP-MIB:RSVP-MIB/rsvpResvTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rsvpsessionnumber.is_set or self.rsvpsessionnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsessionnumber.get_name_leafdata())
                if (self.rsvpresvnumber.is_set or self.rsvpresvnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvnumber.get_name_leafdata())
                if (self.rsvpresvdestaddr.is_set or self.rsvpresvdestaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvdestaddr.get_name_leafdata())
                if (self.rsvpresvdestaddrlength.is_set or self.rsvpresvdestaddrlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvdestaddrlength.get_name_leafdata())
                if (self.rsvpresvdestport.is_set or self.rsvpresvdestport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvdestport.get_name_leafdata())
                if (self.rsvpresvexplicit.is_set or self.rsvpresvexplicit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvexplicit.get_name_leafdata())
                if (self.rsvpresvflowid.is_set or self.rsvpresvflowid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvflowid.get_name_leafdata())
                if (self.rsvpresvhopaddr.is_set or self.rsvpresvhopaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvhopaddr.get_name_leafdata())
                if (self.rsvpresvhoplih.is_set or self.rsvpresvhoplih.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvhoplih.get_name_leafdata())
                if (self.rsvpresvinterface.is_set or self.rsvpresvinterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvinterface.get_name_leafdata())
                if (self.rsvpresvinterval.is_set or self.rsvpresvinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvinterval.get_name_leafdata())
                if (self.rsvpresvlastchange.is_set or self.rsvpresvlastchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvlastchange.get_name_leafdata())
                if (self.rsvpresvpolicy.is_set or self.rsvpresvpolicy.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvpolicy.get_name_leafdata())
                if (self.rsvpresvport.is_set or self.rsvpresvport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvport.get_name_leafdata())
                if (self.rsvpresvprotocol.is_set or self.rsvpresvprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvprotocol.get_name_leafdata())
                if (self.rsvpresvrspecrate.is_set or self.rsvpresvrspecrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvrspecrate.get_name_leafdata())
                if (self.rsvpresvrspecslack.is_set or self.rsvpresvrspecslack.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvrspecslack.get_name_leafdata())
                if (self.rsvpresvrsvphop.is_set or self.rsvpresvrsvphop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvrsvphop.get_name_leafdata())
                if (self.rsvpresvscope.is_set or self.rsvpresvscope.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvscope.get_name_leafdata())
                if (self.rsvpresvsenderaddr.is_set or self.rsvpresvsenderaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvsenderaddr.get_name_leafdata())
                if (self.rsvpresvsenderaddrlength.is_set or self.rsvpresvsenderaddrlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvsenderaddrlength.get_name_leafdata())
                if (self.rsvpresvservice.is_set or self.rsvpresvservice.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvservice.get_name_leafdata())
                if (self.rsvpresvshared.is_set or self.rsvpresvshared.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvshared.get_name_leafdata())
                if (self.rsvpresvstatus.is_set or self.rsvpresvstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvstatus.get_name_leafdata())
                if (self.rsvpresvtspecburst.is_set or self.rsvpresvtspecburst.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvtspecburst.get_name_leafdata())
                if (self.rsvpresvtspecmaxtu.is_set or self.rsvpresvtspecmaxtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvtspecmaxtu.get_name_leafdata())
                if (self.rsvpresvtspecmintu.is_set or self.rsvpresvtspecmintu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvtspecmintu.get_name_leafdata())
                if (self.rsvpresvtspecpeakrate.is_set or self.rsvpresvtspecpeakrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvtspecpeakrate.get_name_leafdata())
                if (self.rsvpresvtspecrate.is_set or self.rsvpresvtspecrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvtspecrate.get_name_leafdata())
                if (self.rsvpresvttl.is_set or self.rsvpresvttl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvttl.get_name_leafdata())
                if (self.rsvpresvtype.is_set or self.rsvpresvtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvtype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rsvpSessionNumber" or name == "rsvpResvNumber" or name == "rsvpResvDestAddr" or name == "rsvpResvDestAddrLength" or name == "rsvpResvDestPort" or name == "rsvpResvExplicit" or name == "rsvpResvFlowId" or name == "rsvpResvHopAddr" or name == "rsvpResvHopLih" or name == "rsvpResvInterface" or name == "rsvpResvInterval" or name == "rsvpResvLastChange" or name == "rsvpResvPolicy" or name == "rsvpResvPort" or name == "rsvpResvProtocol" or name == "rsvpResvRSpecRate" or name == "rsvpResvRSpecSlack" or name == "rsvpResvRSVPHop" or name == "rsvpResvScope" or name == "rsvpResvSenderAddr" or name == "rsvpResvSenderAddrLength" or name == "rsvpResvService" or name == "rsvpResvShared" or name == "rsvpResvStatus" or name == "rsvpResvTSpecBurst" or name == "rsvpResvTSpecMaxTU" or name == "rsvpResvTSpecMinTU" or name == "rsvpResvTSpecPeakRate" or name == "rsvpResvTSpecRate" or name == "rsvpResvTTL" or name == "rsvpResvType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rsvpSessionNumber"):
                    self.rsvpsessionnumber = value
                    self.rsvpsessionnumber.value_namespace = name_space
                    self.rsvpsessionnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvNumber"):
                    self.rsvpresvnumber = value
                    self.rsvpresvnumber.value_namespace = name_space
                    self.rsvpresvnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvDestAddr"):
                    self.rsvpresvdestaddr = value
                    self.rsvpresvdestaddr.value_namespace = name_space
                    self.rsvpresvdestaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvDestAddrLength"):
                    self.rsvpresvdestaddrlength = value
                    self.rsvpresvdestaddrlength.value_namespace = name_space
                    self.rsvpresvdestaddrlength.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvDestPort"):
                    self.rsvpresvdestport = value
                    self.rsvpresvdestport.value_namespace = name_space
                    self.rsvpresvdestport.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvExplicit"):
                    self.rsvpresvexplicit = value
                    self.rsvpresvexplicit.value_namespace = name_space
                    self.rsvpresvexplicit.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFlowId"):
                    self.rsvpresvflowid = value
                    self.rsvpresvflowid.value_namespace = name_space
                    self.rsvpresvflowid.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvHopAddr"):
                    self.rsvpresvhopaddr = value
                    self.rsvpresvhopaddr.value_namespace = name_space
                    self.rsvpresvhopaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvHopLih"):
                    self.rsvpresvhoplih = value
                    self.rsvpresvhoplih.value_namespace = name_space
                    self.rsvpresvhoplih.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvInterface"):
                    self.rsvpresvinterface = value
                    self.rsvpresvinterface.value_namespace = name_space
                    self.rsvpresvinterface.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvInterval"):
                    self.rsvpresvinterval = value
                    self.rsvpresvinterval.value_namespace = name_space
                    self.rsvpresvinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvLastChange"):
                    self.rsvpresvlastchange = value
                    self.rsvpresvlastchange.value_namespace = name_space
                    self.rsvpresvlastchange.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvPolicy"):
                    self.rsvpresvpolicy = value
                    self.rsvpresvpolicy.value_namespace = name_space
                    self.rsvpresvpolicy.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvPort"):
                    self.rsvpresvport = value
                    self.rsvpresvport.value_namespace = name_space
                    self.rsvpresvport.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvProtocol"):
                    self.rsvpresvprotocol = value
                    self.rsvpresvprotocol.value_namespace = name_space
                    self.rsvpresvprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvRSpecRate"):
                    self.rsvpresvrspecrate = value
                    self.rsvpresvrspecrate.value_namespace = name_space
                    self.rsvpresvrspecrate.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvRSpecSlack"):
                    self.rsvpresvrspecslack = value
                    self.rsvpresvrspecslack.value_namespace = name_space
                    self.rsvpresvrspecslack.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvRSVPHop"):
                    self.rsvpresvrsvphop = value
                    self.rsvpresvrsvphop.value_namespace = name_space
                    self.rsvpresvrsvphop.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvScope"):
                    self.rsvpresvscope = value
                    self.rsvpresvscope.value_namespace = name_space
                    self.rsvpresvscope.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvSenderAddr"):
                    self.rsvpresvsenderaddr = value
                    self.rsvpresvsenderaddr.value_namespace = name_space
                    self.rsvpresvsenderaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvSenderAddrLength"):
                    self.rsvpresvsenderaddrlength = value
                    self.rsvpresvsenderaddrlength.value_namespace = name_space
                    self.rsvpresvsenderaddrlength.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvService"):
                    self.rsvpresvservice = value
                    self.rsvpresvservice.value_namespace = name_space
                    self.rsvpresvservice.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvShared"):
                    self.rsvpresvshared = value
                    self.rsvpresvshared.value_namespace = name_space
                    self.rsvpresvshared.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvStatus"):
                    self.rsvpresvstatus = value
                    self.rsvpresvstatus.value_namespace = name_space
                    self.rsvpresvstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvTSpecBurst"):
                    self.rsvpresvtspecburst = value
                    self.rsvpresvtspecburst.value_namespace = name_space
                    self.rsvpresvtspecburst.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvTSpecMaxTU"):
                    self.rsvpresvtspecmaxtu = value
                    self.rsvpresvtspecmaxtu.value_namespace = name_space
                    self.rsvpresvtspecmaxtu.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvTSpecMinTU"):
                    self.rsvpresvtspecmintu = value
                    self.rsvpresvtspecmintu.value_namespace = name_space
                    self.rsvpresvtspecmintu.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvTSpecPeakRate"):
                    self.rsvpresvtspecpeakrate = value
                    self.rsvpresvtspecpeakrate.value_namespace = name_space
                    self.rsvpresvtspecpeakrate.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvTSpecRate"):
                    self.rsvpresvtspecrate = value
                    self.rsvpresvtspecrate.value_namespace = name_space
                    self.rsvpresvtspecrate.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvTTL"):
                    self.rsvpresvttl = value
                    self.rsvpresvttl.value_namespace = name_space
                    self.rsvpresvttl.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvType"):
                    self.rsvpresvtype = value
                    self.rsvpresvtype.value_namespace = name_space
                    self.rsvpresvtype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rsvpresventry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rsvpresventry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rsvpResvTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RSVP-MIB:RSVP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rsvpResvEntry"):
                for c in self.rsvpresventry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RsvpMib.Rsvpresvtable.Rsvpresventry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rsvpresventry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rsvpResvEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Rsvpresvfwdtable(Entity):
        """
        Information	describing the	state  information
        displayed upstream in RESV messages.
        
        .. attribute:: rsvpresvfwdentry
        
        	Information	describing the	state  information displayed   upstream	  in   an   RESV   message concerning a	single sender
        	**type**\: list of    :py:class:`Rsvpresvfwdentry <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpresvfwdtable.Rsvpresvfwdentry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RsvpMib.Rsvpresvfwdtable, self).__init__()

            self.yang_name = "rsvpResvFwdTable"
            self.yang_parent_name = "RSVP-MIB"

            self.rsvpresvfwdentry = YList(self)

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
                        super(RsvpMib.Rsvpresvfwdtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RsvpMib.Rsvpresvfwdtable, self).__setattr__(name, value)


        class Rsvpresvfwdentry(Entity):
            """
            Information	describing the	state  information
            displayed   upstream	  in   an   RESV   message
            concerning a	single sender.
            
            .. attribute:: rsvpsessionnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**refers to**\:  :py:class:`rsvpsessionnumber <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpsessiontable.Rsvpsessionentry>`
            
            .. attribute:: rsvpresvfwdnumber  <key>
            
            	The	number of this reservation request.   This is  for  SNMP Indexing purposes only	and has	no relation to any protocol value
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvfwddestaddr
            
            	The	destination address used by all	senders	in this	 session.   This object	may not	be changed when	the  value  of	the  RowStatus	object	is 'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpresvfwddestaddrlength
            
            	The	length of the destination address in bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: rsvpresvfwddestport
            
            	The	 UDP  or  TCP  port  number  used   as	 a destination	 port  for  all	 senders  in  this session.  If	the IP protocol	in use,	 specified by rsvpResvFwdProtocol, is 50 (ESP) or 51 (AH), this	 represents  a	virtual	 destination  port number.   A value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: rsvpresvfwdexplicit
            
            	If TRUE, individual	senders	are  listed  using Filter  Specifications.   If	FALSE, all senders are implicitly selected.  The Scope Object will contain  a list of senders that need	to receive this	reservation request  for  the  purpose	of routing the RESV message
            	**type**\:  bool
            
            .. attribute:: rsvpresvfwdflowid
            
            	The	flow ID	that this receiver  is	using,	if this	 is  an	IPv6 session
            	**type**\:  int
            
            	**range:** 0..16777215
            
            .. attribute:: rsvpresvfwdhopaddr
            
            	The	address	of the (previous) RSVP	that  will receive this	message
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpresvfwdhoplih
            
            	The	 Logical  Interface  Handle  sent  to  the (previous)	RSVP   that   will   receive  this message
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: rsvpresvfwdinterface
            
            	The	ifIndex	value of the  interface	 on  which this	RESV message was most recently sent
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: rsvpresvfwdinterval
            
            	The	  interval   between   refresh	  messages advertised to the Previous Hop
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvfwdlastchange
            
            	The	time of	the last change	in  this  request; This	 is  either  the first time it was sent	or the	time  of  the  most   recent   change	in parameters
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpresvfwdpolicy
            
            	The	contents of the	policy	object,	 displayed as an uninterpreted string of octets, including the object header.  In the absence of  such	an object, this	should be of zero length
            	**type**\:  str
            
            	**length:** 0..65536
            
            .. attribute:: rsvpresvfwdport
            
            	The	UDP or TCP port	number used  as	 a  source port	 for  this sender in this session.  If the IP	 protocol    in	   use,	   specified	by rsvpResvFwdProtocol	is  50	(ESP)  or 51 (AH), this	represents a generalized  port	identifier (GPI).   A  value of	zero indicates that the	IP protocol in use  does  not  have  ports.   This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 2..4
            
            .. attribute:: rsvpresvfwdprotocol
            
            	The	IP Protocol used by a session. for  secure sessions,  this  indicates  IP  Security.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: rsvpresvfwdrspecrate
            
            	If the requested  service  is  Guaranteed,	as specified   by  rsvpResvService,  this  is  the clearing  rate   that   is	being	requested. Otherwise,  it is zero, or the agent	may return noSuchValue
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bytes per second
            
            .. attribute:: rsvpresvfwdrspecslack
            
            	If the requested  service  is  Guaranteed,	as specified by	rsvpResvService, this is the delay slack.  Otherwise, it is zero, or the agent may return noSuchValue
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: microseconds
            
            .. attribute:: rsvpresvfwdrsvphop
            
            	If TRUE, the node believes that  the  next	IP hop	is  an	RSVP  hop.   If	 FALSE,	 the  node believes that the next IP hop  may  not  be	an RSVP	hop
            	**type**\:  bool
            
            .. attribute:: rsvpresvfwdscope
            
            	The	contents of the	scope object, displayed	as an  uninterpreted  string  of octets, including the object header.  In the absence of  such	an object, this	should be of zero length
            	**type**\:  str
            
            	**length:** 0..65536
            
            .. attribute:: rsvpresvfwdsenderaddr
            
            	The	source address of the sender  selected	by this	 reservation.	The  value  of	all zeroes indicates 'all senders'.  This object  may  not be  changed	when  the  value  of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpresvfwdsenderaddrlength
            
            	The	length of the sender's	address	 in  bits. This	 is  the CIDR Prefix Length, which for IP4 hosts and multicast addresses is 32 bits.  This object may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  int
            
            	**range:** 0..128
            
            .. attribute:: rsvpresvfwdservice
            
            	The	QoS Service classification requested
            	**type**\:   :py:class:`Qosservice <ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB.Qosservice>`
            
            .. attribute:: rsvpresvfwdshared
            
            	If TRUE, a reservation shared among	senders	is requested.  If FALSE, a reservation specific	to this	sender is requested
            	**type**\:  bool
            
            .. attribute:: rsvpresvfwdstatus
            
            	'active' for all active RESV  messages.   This object may be used to delete	RESV information
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: rsvpresvfwdtspecburst
            
            	The	size of	the largest  burst  expected  from the sender at a time.  If this is less than	 the  sender's	advertised burst  size,	the receiver is	asking the network to provide flow pacing  beyond  what	 would	be provided   under   normal  circumstances.  Such pacing is at	the network's option
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bytes
            
            .. attribute:: rsvpresvfwdtspecmaxtu
            
            	The	maximum	message	size for  this	flow.  The admission  algorithm	 will  reject TSpecs whose Maximum Transmission	Unit, plus  the	 interface headers, exceed the interface MTU
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvfwdtspecmintu
            
            	The	minimum	message	size for  this	flow.  The policing  algorithm will treat smaller messages as though they are this size
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: rsvpresvfwdtspecpeakrate
            
            	The	Peak Bit Rate of the sender's data  stream Traffic  arrival is not expected to exceed this rate	at any time, apart  from  the  effects	of jitter in the network.  If not specified in the TSpec, this returns zero or noSuchValue
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvfwdtspecrate
            
            	The	Average	Bit  Rate  of  the  sender's  data stream.    Within  a	 transmission  burst,  the arrival   rate    may    be	  as	fast	as rsvpResvFwdTSpecPeakRate  (if  supported by the service model); however, averaged across two	or more	 burst	intervals,  the	 rate  should  not exceed rsvpResvFwdTSpecRate.  Note	that this is a prediction, often based	on the	general	 capability  of	a type of codec	or particular encoding;	the measured average  rate may be significantly	lower
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: bits per second
            
            .. attribute:: rsvpresvfwdttl
            
            	The	TTL value in the RSVP header that was last received
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: rsvpresvfwdtype
            
            	The	type of	session	(IP4, IP6, IP6	with  flow information,	etc)
            	**type**\:  int
            
            	**range:** 1..255
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RsvpMib.Rsvpresvfwdtable.Rsvpresvfwdentry, self).__init__()

                self.yang_name = "rsvpResvFwdEntry"
                self.yang_parent_name = "rsvpResvFwdTable"

                self.rsvpsessionnumber = YLeaf(YType.str, "rsvpSessionNumber")

                self.rsvpresvfwdnumber = YLeaf(YType.int32, "rsvpResvFwdNumber")

                self.rsvpresvfwddestaddr = YLeaf(YType.str, "rsvpResvFwdDestAddr")

                self.rsvpresvfwddestaddrlength = YLeaf(YType.int32, "rsvpResvFwdDestAddrLength")

                self.rsvpresvfwddestport = YLeaf(YType.str, "rsvpResvFwdDestPort")

                self.rsvpresvfwdexplicit = YLeaf(YType.boolean, "rsvpResvFwdExplicit")

                self.rsvpresvfwdflowid = YLeaf(YType.int32, "rsvpResvFwdFlowId")

                self.rsvpresvfwdhopaddr = YLeaf(YType.str, "rsvpResvFwdHopAddr")

                self.rsvpresvfwdhoplih = YLeaf(YType.int32, "rsvpResvFwdHopLih")

                self.rsvpresvfwdinterface = YLeaf(YType.int32, "rsvpResvFwdInterface")

                self.rsvpresvfwdinterval = YLeaf(YType.int32, "rsvpResvFwdInterval")

                self.rsvpresvfwdlastchange = YLeaf(YType.uint32, "rsvpResvFwdLastChange")

                self.rsvpresvfwdpolicy = YLeaf(YType.str, "rsvpResvFwdPolicy")

                self.rsvpresvfwdport = YLeaf(YType.str, "rsvpResvFwdPort")

                self.rsvpresvfwdprotocol = YLeaf(YType.int32, "rsvpResvFwdProtocol")

                self.rsvpresvfwdrspecrate = YLeaf(YType.int32, "rsvpResvFwdRSpecRate")

                self.rsvpresvfwdrspecslack = YLeaf(YType.int32, "rsvpResvFwdRSpecSlack")

                self.rsvpresvfwdrsvphop = YLeaf(YType.boolean, "rsvpResvFwdRSVPHop")

                self.rsvpresvfwdscope = YLeaf(YType.str, "rsvpResvFwdScope")

                self.rsvpresvfwdsenderaddr = YLeaf(YType.str, "rsvpResvFwdSenderAddr")

                self.rsvpresvfwdsenderaddrlength = YLeaf(YType.int32, "rsvpResvFwdSenderAddrLength")

                self.rsvpresvfwdservice = YLeaf(YType.enumeration, "rsvpResvFwdService")

                self.rsvpresvfwdshared = YLeaf(YType.boolean, "rsvpResvFwdShared")

                self.rsvpresvfwdstatus = YLeaf(YType.enumeration, "rsvpResvFwdStatus")

                self.rsvpresvfwdtspecburst = YLeaf(YType.int32, "rsvpResvFwdTSpecBurst")

                self.rsvpresvfwdtspecmaxtu = YLeaf(YType.int32, "rsvpResvFwdTSpecMaxTU")

                self.rsvpresvfwdtspecmintu = YLeaf(YType.int32, "rsvpResvFwdTSpecMinTU")

                self.rsvpresvfwdtspecpeakrate = YLeaf(YType.int32, "rsvpResvFwdTSpecPeakRate")

                self.rsvpresvfwdtspecrate = YLeaf(YType.int32, "rsvpResvFwdTSpecRate")

                self.rsvpresvfwdttl = YLeaf(YType.int32, "rsvpResvFwdTTL")

                self.rsvpresvfwdtype = YLeaf(YType.int32, "rsvpResvFwdType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("rsvpsessionnumber",
                                "rsvpresvfwdnumber",
                                "rsvpresvfwddestaddr",
                                "rsvpresvfwddestaddrlength",
                                "rsvpresvfwddestport",
                                "rsvpresvfwdexplicit",
                                "rsvpresvfwdflowid",
                                "rsvpresvfwdhopaddr",
                                "rsvpresvfwdhoplih",
                                "rsvpresvfwdinterface",
                                "rsvpresvfwdinterval",
                                "rsvpresvfwdlastchange",
                                "rsvpresvfwdpolicy",
                                "rsvpresvfwdport",
                                "rsvpresvfwdprotocol",
                                "rsvpresvfwdrspecrate",
                                "rsvpresvfwdrspecslack",
                                "rsvpresvfwdrsvphop",
                                "rsvpresvfwdscope",
                                "rsvpresvfwdsenderaddr",
                                "rsvpresvfwdsenderaddrlength",
                                "rsvpresvfwdservice",
                                "rsvpresvfwdshared",
                                "rsvpresvfwdstatus",
                                "rsvpresvfwdtspecburst",
                                "rsvpresvfwdtspecmaxtu",
                                "rsvpresvfwdtspecmintu",
                                "rsvpresvfwdtspecpeakrate",
                                "rsvpresvfwdtspecrate",
                                "rsvpresvfwdttl",
                                "rsvpresvfwdtype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RsvpMib.Rsvpresvfwdtable.Rsvpresvfwdentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RsvpMib.Rsvpresvfwdtable.Rsvpresvfwdentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.rsvpsessionnumber.is_set or
                    self.rsvpresvfwdnumber.is_set or
                    self.rsvpresvfwddestaddr.is_set or
                    self.rsvpresvfwddestaddrlength.is_set or
                    self.rsvpresvfwddestport.is_set or
                    self.rsvpresvfwdexplicit.is_set or
                    self.rsvpresvfwdflowid.is_set or
                    self.rsvpresvfwdhopaddr.is_set or
                    self.rsvpresvfwdhoplih.is_set or
                    self.rsvpresvfwdinterface.is_set or
                    self.rsvpresvfwdinterval.is_set or
                    self.rsvpresvfwdlastchange.is_set or
                    self.rsvpresvfwdpolicy.is_set or
                    self.rsvpresvfwdport.is_set or
                    self.rsvpresvfwdprotocol.is_set or
                    self.rsvpresvfwdrspecrate.is_set or
                    self.rsvpresvfwdrspecslack.is_set or
                    self.rsvpresvfwdrsvphop.is_set or
                    self.rsvpresvfwdscope.is_set or
                    self.rsvpresvfwdsenderaddr.is_set or
                    self.rsvpresvfwdsenderaddrlength.is_set or
                    self.rsvpresvfwdservice.is_set or
                    self.rsvpresvfwdshared.is_set or
                    self.rsvpresvfwdstatus.is_set or
                    self.rsvpresvfwdtspecburst.is_set or
                    self.rsvpresvfwdtspecmaxtu.is_set or
                    self.rsvpresvfwdtspecmintu.is_set or
                    self.rsvpresvfwdtspecpeakrate.is_set or
                    self.rsvpresvfwdtspecrate.is_set or
                    self.rsvpresvfwdttl.is_set or
                    self.rsvpresvfwdtype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.rsvpsessionnumber.yfilter != YFilter.not_set or
                    self.rsvpresvfwdnumber.yfilter != YFilter.not_set or
                    self.rsvpresvfwddestaddr.yfilter != YFilter.not_set or
                    self.rsvpresvfwddestaddrlength.yfilter != YFilter.not_set or
                    self.rsvpresvfwddestport.yfilter != YFilter.not_set or
                    self.rsvpresvfwdexplicit.yfilter != YFilter.not_set or
                    self.rsvpresvfwdflowid.yfilter != YFilter.not_set or
                    self.rsvpresvfwdhopaddr.yfilter != YFilter.not_set or
                    self.rsvpresvfwdhoplih.yfilter != YFilter.not_set or
                    self.rsvpresvfwdinterface.yfilter != YFilter.not_set or
                    self.rsvpresvfwdinterval.yfilter != YFilter.not_set or
                    self.rsvpresvfwdlastchange.yfilter != YFilter.not_set or
                    self.rsvpresvfwdpolicy.yfilter != YFilter.not_set or
                    self.rsvpresvfwdport.yfilter != YFilter.not_set or
                    self.rsvpresvfwdprotocol.yfilter != YFilter.not_set or
                    self.rsvpresvfwdrspecrate.yfilter != YFilter.not_set or
                    self.rsvpresvfwdrspecslack.yfilter != YFilter.not_set or
                    self.rsvpresvfwdrsvphop.yfilter != YFilter.not_set or
                    self.rsvpresvfwdscope.yfilter != YFilter.not_set or
                    self.rsvpresvfwdsenderaddr.yfilter != YFilter.not_set or
                    self.rsvpresvfwdsenderaddrlength.yfilter != YFilter.not_set or
                    self.rsvpresvfwdservice.yfilter != YFilter.not_set or
                    self.rsvpresvfwdshared.yfilter != YFilter.not_set or
                    self.rsvpresvfwdstatus.yfilter != YFilter.not_set or
                    self.rsvpresvfwdtspecburst.yfilter != YFilter.not_set or
                    self.rsvpresvfwdtspecmaxtu.yfilter != YFilter.not_set or
                    self.rsvpresvfwdtspecmintu.yfilter != YFilter.not_set or
                    self.rsvpresvfwdtspecpeakrate.yfilter != YFilter.not_set or
                    self.rsvpresvfwdtspecrate.yfilter != YFilter.not_set or
                    self.rsvpresvfwdttl.yfilter != YFilter.not_set or
                    self.rsvpresvfwdtype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rsvpResvFwdEntry" + "[rsvpSessionNumber='" + self.rsvpsessionnumber.get() + "']" + "[rsvpResvFwdNumber='" + self.rsvpresvfwdnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RSVP-MIB:RSVP-MIB/rsvpResvFwdTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.rsvpsessionnumber.is_set or self.rsvpsessionnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpsessionnumber.get_name_leafdata())
                if (self.rsvpresvfwdnumber.is_set or self.rsvpresvfwdnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdnumber.get_name_leafdata())
                if (self.rsvpresvfwddestaddr.is_set or self.rsvpresvfwddestaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwddestaddr.get_name_leafdata())
                if (self.rsvpresvfwddestaddrlength.is_set or self.rsvpresvfwddestaddrlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwddestaddrlength.get_name_leafdata())
                if (self.rsvpresvfwddestport.is_set or self.rsvpresvfwddestport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwddestport.get_name_leafdata())
                if (self.rsvpresvfwdexplicit.is_set or self.rsvpresvfwdexplicit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdexplicit.get_name_leafdata())
                if (self.rsvpresvfwdflowid.is_set or self.rsvpresvfwdflowid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdflowid.get_name_leafdata())
                if (self.rsvpresvfwdhopaddr.is_set or self.rsvpresvfwdhopaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdhopaddr.get_name_leafdata())
                if (self.rsvpresvfwdhoplih.is_set or self.rsvpresvfwdhoplih.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdhoplih.get_name_leafdata())
                if (self.rsvpresvfwdinterface.is_set or self.rsvpresvfwdinterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdinterface.get_name_leafdata())
                if (self.rsvpresvfwdinterval.is_set or self.rsvpresvfwdinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdinterval.get_name_leafdata())
                if (self.rsvpresvfwdlastchange.is_set or self.rsvpresvfwdlastchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdlastchange.get_name_leafdata())
                if (self.rsvpresvfwdpolicy.is_set or self.rsvpresvfwdpolicy.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdpolicy.get_name_leafdata())
                if (self.rsvpresvfwdport.is_set or self.rsvpresvfwdport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdport.get_name_leafdata())
                if (self.rsvpresvfwdprotocol.is_set or self.rsvpresvfwdprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdprotocol.get_name_leafdata())
                if (self.rsvpresvfwdrspecrate.is_set or self.rsvpresvfwdrspecrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdrspecrate.get_name_leafdata())
                if (self.rsvpresvfwdrspecslack.is_set or self.rsvpresvfwdrspecslack.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdrspecslack.get_name_leafdata())
                if (self.rsvpresvfwdrsvphop.is_set or self.rsvpresvfwdrsvphop.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdrsvphop.get_name_leafdata())
                if (self.rsvpresvfwdscope.is_set or self.rsvpresvfwdscope.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdscope.get_name_leafdata())
                if (self.rsvpresvfwdsenderaddr.is_set or self.rsvpresvfwdsenderaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdsenderaddr.get_name_leafdata())
                if (self.rsvpresvfwdsenderaddrlength.is_set or self.rsvpresvfwdsenderaddrlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdsenderaddrlength.get_name_leafdata())
                if (self.rsvpresvfwdservice.is_set or self.rsvpresvfwdservice.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdservice.get_name_leafdata())
                if (self.rsvpresvfwdshared.is_set or self.rsvpresvfwdshared.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdshared.get_name_leafdata())
                if (self.rsvpresvfwdstatus.is_set or self.rsvpresvfwdstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdstatus.get_name_leafdata())
                if (self.rsvpresvfwdtspecburst.is_set or self.rsvpresvfwdtspecburst.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdtspecburst.get_name_leafdata())
                if (self.rsvpresvfwdtspecmaxtu.is_set or self.rsvpresvfwdtspecmaxtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdtspecmaxtu.get_name_leafdata())
                if (self.rsvpresvfwdtspecmintu.is_set or self.rsvpresvfwdtspecmintu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdtspecmintu.get_name_leafdata())
                if (self.rsvpresvfwdtspecpeakrate.is_set or self.rsvpresvfwdtspecpeakrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdtspecpeakrate.get_name_leafdata())
                if (self.rsvpresvfwdtspecrate.is_set or self.rsvpresvfwdtspecrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdtspecrate.get_name_leafdata())
                if (self.rsvpresvfwdttl.is_set or self.rsvpresvfwdttl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdttl.get_name_leafdata())
                if (self.rsvpresvfwdtype.is_set or self.rsvpresvfwdtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpresvfwdtype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "rsvpSessionNumber" or name == "rsvpResvFwdNumber" or name == "rsvpResvFwdDestAddr" or name == "rsvpResvFwdDestAddrLength" or name == "rsvpResvFwdDestPort" or name == "rsvpResvFwdExplicit" or name == "rsvpResvFwdFlowId" or name == "rsvpResvFwdHopAddr" or name == "rsvpResvFwdHopLih" or name == "rsvpResvFwdInterface" or name == "rsvpResvFwdInterval" or name == "rsvpResvFwdLastChange" or name == "rsvpResvFwdPolicy" or name == "rsvpResvFwdPort" or name == "rsvpResvFwdProtocol" or name == "rsvpResvFwdRSpecRate" or name == "rsvpResvFwdRSpecSlack" or name == "rsvpResvFwdRSVPHop" or name == "rsvpResvFwdScope" or name == "rsvpResvFwdSenderAddr" or name == "rsvpResvFwdSenderAddrLength" or name == "rsvpResvFwdService" or name == "rsvpResvFwdShared" or name == "rsvpResvFwdStatus" or name == "rsvpResvFwdTSpecBurst" or name == "rsvpResvFwdTSpecMaxTU" or name == "rsvpResvFwdTSpecMinTU" or name == "rsvpResvFwdTSpecPeakRate" or name == "rsvpResvFwdTSpecRate" or name == "rsvpResvFwdTTL" or name == "rsvpResvFwdType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "rsvpSessionNumber"):
                    self.rsvpsessionnumber = value
                    self.rsvpsessionnumber.value_namespace = name_space
                    self.rsvpsessionnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdNumber"):
                    self.rsvpresvfwdnumber = value
                    self.rsvpresvfwdnumber.value_namespace = name_space
                    self.rsvpresvfwdnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdDestAddr"):
                    self.rsvpresvfwddestaddr = value
                    self.rsvpresvfwddestaddr.value_namespace = name_space
                    self.rsvpresvfwddestaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdDestAddrLength"):
                    self.rsvpresvfwddestaddrlength = value
                    self.rsvpresvfwddestaddrlength.value_namespace = name_space
                    self.rsvpresvfwddestaddrlength.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdDestPort"):
                    self.rsvpresvfwddestport = value
                    self.rsvpresvfwddestport.value_namespace = name_space
                    self.rsvpresvfwddestport.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdExplicit"):
                    self.rsvpresvfwdexplicit = value
                    self.rsvpresvfwdexplicit.value_namespace = name_space
                    self.rsvpresvfwdexplicit.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdFlowId"):
                    self.rsvpresvfwdflowid = value
                    self.rsvpresvfwdflowid.value_namespace = name_space
                    self.rsvpresvfwdflowid.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdHopAddr"):
                    self.rsvpresvfwdhopaddr = value
                    self.rsvpresvfwdhopaddr.value_namespace = name_space
                    self.rsvpresvfwdhopaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdHopLih"):
                    self.rsvpresvfwdhoplih = value
                    self.rsvpresvfwdhoplih.value_namespace = name_space
                    self.rsvpresvfwdhoplih.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdInterface"):
                    self.rsvpresvfwdinterface = value
                    self.rsvpresvfwdinterface.value_namespace = name_space
                    self.rsvpresvfwdinterface.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdInterval"):
                    self.rsvpresvfwdinterval = value
                    self.rsvpresvfwdinterval.value_namespace = name_space
                    self.rsvpresvfwdinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdLastChange"):
                    self.rsvpresvfwdlastchange = value
                    self.rsvpresvfwdlastchange.value_namespace = name_space
                    self.rsvpresvfwdlastchange.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdPolicy"):
                    self.rsvpresvfwdpolicy = value
                    self.rsvpresvfwdpolicy.value_namespace = name_space
                    self.rsvpresvfwdpolicy.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdPort"):
                    self.rsvpresvfwdport = value
                    self.rsvpresvfwdport.value_namespace = name_space
                    self.rsvpresvfwdport.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdProtocol"):
                    self.rsvpresvfwdprotocol = value
                    self.rsvpresvfwdprotocol.value_namespace = name_space
                    self.rsvpresvfwdprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdRSpecRate"):
                    self.rsvpresvfwdrspecrate = value
                    self.rsvpresvfwdrspecrate.value_namespace = name_space
                    self.rsvpresvfwdrspecrate.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdRSpecSlack"):
                    self.rsvpresvfwdrspecslack = value
                    self.rsvpresvfwdrspecslack.value_namespace = name_space
                    self.rsvpresvfwdrspecslack.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdRSVPHop"):
                    self.rsvpresvfwdrsvphop = value
                    self.rsvpresvfwdrsvphop.value_namespace = name_space
                    self.rsvpresvfwdrsvphop.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdScope"):
                    self.rsvpresvfwdscope = value
                    self.rsvpresvfwdscope.value_namespace = name_space
                    self.rsvpresvfwdscope.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdSenderAddr"):
                    self.rsvpresvfwdsenderaddr = value
                    self.rsvpresvfwdsenderaddr.value_namespace = name_space
                    self.rsvpresvfwdsenderaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdSenderAddrLength"):
                    self.rsvpresvfwdsenderaddrlength = value
                    self.rsvpresvfwdsenderaddrlength.value_namespace = name_space
                    self.rsvpresvfwdsenderaddrlength.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdService"):
                    self.rsvpresvfwdservice = value
                    self.rsvpresvfwdservice.value_namespace = name_space
                    self.rsvpresvfwdservice.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdShared"):
                    self.rsvpresvfwdshared = value
                    self.rsvpresvfwdshared.value_namespace = name_space
                    self.rsvpresvfwdshared.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdStatus"):
                    self.rsvpresvfwdstatus = value
                    self.rsvpresvfwdstatus.value_namespace = name_space
                    self.rsvpresvfwdstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdTSpecBurst"):
                    self.rsvpresvfwdtspecburst = value
                    self.rsvpresvfwdtspecburst.value_namespace = name_space
                    self.rsvpresvfwdtspecburst.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdTSpecMaxTU"):
                    self.rsvpresvfwdtspecmaxtu = value
                    self.rsvpresvfwdtspecmaxtu.value_namespace = name_space
                    self.rsvpresvfwdtspecmaxtu.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdTSpecMinTU"):
                    self.rsvpresvfwdtspecmintu = value
                    self.rsvpresvfwdtspecmintu.value_namespace = name_space
                    self.rsvpresvfwdtspecmintu.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdTSpecPeakRate"):
                    self.rsvpresvfwdtspecpeakrate = value
                    self.rsvpresvfwdtspecpeakrate.value_namespace = name_space
                    self.rsvpresvfwdtspecpeakrate.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdTSpecRate"):
                    self.rsvpresvfwdtspecrate = value
                    self.rsvpresvfwdtspecrate.value_namespace = name_space
                    self.rsvpresvfwdtspecrate.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdTTL"):
                    self.rsvpresvfwdttl = value
                    self.rsvpresvfwdttl.value_namespace = name_space
                    self.rsvpresvfwdttl.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpResvFwdType"):
                    self.rsvpresvfwdtype = value
                    self.rsvpresvfwdtype.value_namespace = name_space
                    self.rsvpresvfwdtype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rsvpresvfwdentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rsvpresvfwdentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rsvpResvFwdTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RSVP-MIB:RSVP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rsvpResvFwdEntry"):
                for c in self.rsvpresvfwdentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RsvpMib.Rsvpresvfwdtable.Rsvpresvfwdentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rsvpresvfwdentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rsvpResvFwdEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Rsvpiftable(Entity):
        """
        The	RSVP\-specific attributes of  the  system's
        interfaces.
        
        .. attribute:: rsvpifentry
        
        	The	RSVP\-specific attributes of  the  a  given interface
        	**type**\: list of    :py:class:`Rsvpifentry <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpiftable.Rsvpifentry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RsvpMib.Rsvpiftable, self).__init__()

            self.yang_name = "rsvpIfTable"
            self.yang_parent_name = "RSVP-MIB"

            self.rsvpifentry = YList(self)

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
                        super(RsvpMib.Rsvpiftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RsvpMib.Rsvpiftable, self).__setattr__(name, value)


        class Rsvpifentry(Entity):
            """
            The	RSVP\-specific attributes of  the  a  given
            interface.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: rsvpifenabled
            
            	If TRUE, RSVP is enabled  on  this	Interface. If	FALSE,	 RSVP	is  not	 enabled  on  this interface
            	**type**\:  bool
            
            .. attribute:: rsvpifipnbrs
            
            	The	number of neighbors perceived to be  using only	the RSVP IP Encapsulation
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpifnbrs
            
            	The	number of neighbors  currently	perceived; this	 will  exceed rsvpIfIpNbrs + rsvpIfUdpNbrs by  the  number   of	  neighbors   using   both encapsulations
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpifrefreshblockademultiple
            
            	The	value of the RSVP value	'Kb', Which is the minimum   number   of  refresh  intervals  that blockade state will last once entered
            	**type**\:  int
            
            	**range:** 1..65536
            
            .. attribute:: rsvpifrefreshinterval
            
            	The	value of the RSVP value	'R', which is  the minimum period between refresh transmissions	of a given PATH	or RESV	message	on an interface
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: milliseconds
            
            .. attribute:: rsvpifrefreshmultiple
            
            	The	value of the RSVP value	'K', which is  the number  of  refresh intervals which must elapse (minimum) before a PATH or RESV  message  which is not being	refreshed will be aged out
            	**type**\:  int
            
            	**range:** 1..65536
            
            .. attribute:: rsvpifroutedelay
            
            	The	approximate period from	the time  a  route is  changed	to  the	 time  a resulting message appears on the interface
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            	**units**\: hundredths	of a second
            
            .. attribute:: rsvpifstatus
            
            	'active' on	interfaces that	are configured for RSVP
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: rsvpifttl
            
            	The	value of SEND\_TTL used on  this	 interface for	messages  this node originates.	 If set	to zero, the node determines  the  TTL	via  other means
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: rsvpifudpnbrs
            
            	The	number of neighbors perceived to be  using only	the RSVP UDP Encapsulation
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: rsvpifudprequired
            
            	If TRUE, manual configuration forces  the  use of  UDP  encapsulation  on  the  interface.	If FALSE,  UDP	encapsulation  is  only	 used	if rsvpIfUdpNbrs is not	zero
            	**type**\:  bool
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RsvpMib.Rsvpiftable.Rsvpifentry, self).__init__()

                self.yang_name = "rsvpIfEntry"
                self.yang_parent_name = "rsvpIfTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.rsvpifenabled = YLeaf(YType.boolean, "rsvpIfEnabled")

                self.rsvpifipnbrs = YLeaf(YType.uint32, "rsvpIfIpNbrs")

                self.rsvpifnbrs = YLeaf(YType.uint32, "rsvpIfNbrs")

                self.rsvpifrefreshblockademultiple = YLeaf(YType.int32, "rsvpIfRefreshBlockadeMultiple")

                self.rsvpifrefreshinterval = YLeaf(YType.int32, "rsvpIfRefreshInterval")

                self.rsvpifrefreshmultiple = YLeaf(YType.int32, "rsvpIfRefreshMultiple")

                self.rsvpifroutedelay = YLeaf(YType.int32, "rsvpIfRouteDelay")

                self.rsvpifstatus = YLeaf(YType.enumeration, "rsvpIfStatus")

                self.rsvpifttl = YLeaf(YType.int32, "rsvpIfTTL")

                self.rsvpifudpnbrs = YLeaf(YType.uint32, "rsvpIfUdpNbrs")

                self.rsvpifudprequired = YLeaf(YType.boolean, "rsvpIfUdpRequired")

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
                                "rsvpifenabled",
                                "rsvpifipnbrs",
                                "rsvpifnbrs",
                                "rsvpifrefreshblockademultiple",
                                "rsvpifrefreshinterval",
                                "rsvpifrefreshmultiple",
                                "rsvpifroutedelay",
                                "rsvpifstatus",
                                "rsvpifttl",
                                "rsvpifudpnbrs",
                                "rsvpifudprequired") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RsvpMib.Rsvpiftable.Rsvpifentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RsvpMib.Rsvpiftable.Rsvpifentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.rsvpifenabled.is_set or
                    self.rsvpifipnbrs.is_set or
                    self.rsvpifnbrs.is_set or
                    self.rsvpifrefreshblockademultiple.is_set or
                    self.rsvpifrefreshinterval.is_set or
                    self.rsvpifrefreshmultiple.is_set or
                    self.rsvpifroutedelay.is_set or
                    self.rsvpifstatus.is_set or
                    self.rsvpifttl.is_set or
                    self.rsvpifudpnbrs.is_set or
                    self.rsvpifudprequired.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.rsvpifenabled.yfilter != YFilter.not_set or
                    self.rsvpifipnbrs.yfilter != YFilter.not_set or
                    self.rsvpifnbrs.yfilter != YFilter.not_set or
                    self.rsvpifrefreshblockademultiple.yfilter != YFilter.not_set or
                    self.rsvpifrefreshinterval.yfilter != YFilter.not_set or
                    self.rsvpifrefreshmultiple.yfilter != YFilter.not_set or
                    self.rsvpifroutedelay.yfilter != YFilter.not_set or
                    self.rsvpifstatus.yfilter != YFilter.not_set or
                    self.rsvpifttl.yfilter != YFilter.not_set or
                    self.rsvpifudpnbrs.yfilter != YFilter.not_set or
                    self.rsvpifudprequired.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rsvpIfEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RSVP-MIB:RSVP-MIB/rsvpIfTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.rsvpifenabled.is_set or self.rsvpifenabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpifenabled.get_name_leafdata())
                if (self.rsvpifipnbrs.is_set or self.rsvpifipnbrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpifipnbrs.get_name_leafdata())
                if (self.rsvpifnbrs.is_set or self.rsvpifnbrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpifnbrs.get_name_leafdata())
                if (self.rsvpifrefreshblockademultiple.is_set or self.rsvpifrefreshblockademultiple.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpifrefreshblockademultiple.get_name_leafdata())
                if (self.rsvpifrefreshinterval.is_set or self.rsvpifrefreshinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpifrefreshinterval.get_name_leafdata())
                if (self.rsvpifrefreshmultiple.is_set or self.rsvpifrefreshmultiple.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpifrefreshmultiple.get_name_leafdata())
                if (self.rsvpifroutedelay.is_set or self.rsvpifroutedelay.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpifroutedelay.get_name_leafdata())
                if (self.rsvpifstatus.is_set or self.rsvpifstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpifstatus.get_name_leafdata())
                if (self.rsvpifttl.is_set or self.rsvpifttl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpifttl.get_name_leafdata())
                if (self.rsvpifudpnbrs.is_set or self.rsvpifudpnbrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpifudpnbrs.get_name_leafdata())
                if (self.rsvpifudprequired.is_set or self.rsvpifudprequired.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpifudprequired.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "rsvpIfEnabled" or name == "rsvpIfIpNbrs" or name == "rsvpIfNbrs" or name == "rsvpIfRefreshBlockadeMultiple" or name == "rsvpIfRefreshInterval" or name == "rsvpIfRefreshMultiple" or name == "rsvpIfRouteDelay" or name == "rsvpIfStatus" or name == "rsvpIfTTL" or name == "rsvpIfUdpNbrs" or name == "rsvpIfUdpRequired"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpIfEnabled"):
                    self.rsvpifenabled = value
                    self.rsvpifenabled.value_namespace = name_space
                    self.rsvpifenabled.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpIfIpNbrs"):
                    self.rsvpifipnbrs = value
                    self.rsvpifipnbrs.value_namespace = name_space
                    self.rsvpifipnbrs.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpIfNbrs"):
                    self.rsvpifnbrs = value
                    self.rsvpifnbrs.value_namespace = name_space
                    self.rsvpifnbrs.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpIfRefreshBlockadeMultiple"):
                    self.rsvpifrefreshblockademultiple = value
                    self.rsvpifrefreshblockademultiple.value_namespace = name_space
                    self.rsvpifrefreshblockademultiple.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpIfRefreshInterval"):
                    self.rsvpifrefreshinterval = value
                    self.rsvpifrefreshinterval.value_namespace = name_space
                    self.rsvpifrefreshinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpIfRefreshMultiple"):
                    self.rsvpifrefreshmultiple = value
                    self.rsvpifrefreshmultiple.value_namespace = name_space
                    self.rsvpifrefreshmultiple.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpIfRouteDelay"):
                    self.rsvpifroutedelay = value
                    self.rsvpifroutedelay.value_namespace = name_space
                    self.rsvpifroutedelay.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpIfStatus"):
                    self.rsvpifstatus = value
                    self.rsvpifstatus.value_namespace = name_space
                    self.rsvpifstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpIfTTL"):
                    self.rsvpifttl = value
                    self.rsvpifttl.value_namespace = name_space
                    self.rsvpifttl.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpIfUdpNbrs"):
                    self.rsvpifudpnbrs = value
                    self.rsvpifudpnbrs.value_namespace = name_space
                    self.rsvpifudpnbrs.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpIfUdpRequired"):
                    self.rsvpifudprequired = value
                    self.rsvpifudprequired.value_namespace = name_space
                    self.rsvpifudprequired.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rsvpifentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rsvpifentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rsvpIfTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RSVP-MIB:RSVP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rsvpIfEntry"):
                for c in self.rsvpifentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RsvpMib.Rsvpiftable.Rsvpifentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rsvpifentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rsvpIfEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Rsvpnbrtable(Entity):
        """
        Information	describing  the	 Neighbors  of	an
        RSVP	system.
        
        .. attribute:: rsvpnbrentry
        
        	Information	  describing   a    single    RSVP Neighbor
        	**type**\: list of    :py:class:`Rsvpnbrentry <ydk.models.cisco_ios_xe.RSVP_MIB.RsvpMib.Rsvpnbrtable.Rsvpnbrentry>`
        
        

        """

        _prefix = 'RSVP-MIB'
        _revision = '1998-08-25'

        def __init__(self):
            super(RsvpMib.Rsvpnbrtable, self).__init__()

            self.yang_name = "rsvpNbrTable"
            self.yang_parent_name = "RSVP-MIB"

            self.rsvpnbrentry = YList(self)

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
                        super(RsvpMib.Rsvpnbrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(RsvpMib.Rsvpnbrtable, self).__setattr__(name, value)


        class Rsvpnbrentry(Entity):
            """
            Information	  describing   a    single    RSVP
            Neighbor.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: rsvpnbraddress  <key>
            
            	The	IP4 or IP6 Address used	by this	 neighbor. This	 object	 may not be changed when the value of the RowStatus object is 'active'
            	**type**\:  str
            
            	**length:** 4..16
            
            .. attribute:: rsvpnbrprotocol
            
            	The	  encapsulation	  being	  used	 by   this neighbor
            	**type**\:   :py:class:`Rsvpencapsulation <ydk.models.cisco_ios_xe.RSVP_MIB.Rsvpencapsulation>`
            
            .. attribute:: rsvpnbrstatus
            
            	'active' for all neighbors.	 This  object  may be	used   to  configure  neighbors.   In  the presence   of   configured	 neighbors,    the implementation  may	(but  is  not required to) limit the  set  of  valid  neighbors	 to  those configured
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'RSVP-MIB'
            _revision = '1998-08-25'

            def __init__(self):
                super(RsvpMib.Rsvpnbrtable.Rsvpnbrentry, self).__init__()

                self.yang_name = "rsvpNbrEntry"
                self.yang_parent_name = "rsvpNbrTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.rsvpnbraddress = YLeaf(YType.str, "rsvpNbrAddress")

                self.rsvpnbrprotocol = YLeaf(YType.enumeration, "rsvpNbrProtocol")

                self.rsvpnbrstatus = YLeaf(YType.enumeration, "rsvpNbrStatus")

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
                                "rsvpnbraddress",
                                "rsvpnbrprotocol",
                                "rsvpnbrstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(RsvpMib.Rsvpnbrtable.Rsvpnbrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(RsvpMib.Rsvpnbrtable.Rsvpnbrentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.rsvpnbraddress.is_set or
                    self.rsvpnbrprotocol.is_set or
                    self.rsvpnbrstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.rsvpnbraddress.yfilter != YFilter.not_set or
                    self.rsvpnbrprotocol.yfilter != YFilter.not_set or
                    self.rsvpnbrstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "rsvpNbrEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[rsvpNbrAddress='" + self.rsvpnbraddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "RSVP-MIB:RSVP-MIB/rsvpNbrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.rsvpnbraddress.is_set or self.rsvpnbraddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpnbraddress.get_name_leafdata())
                if (self.rsvpnbrprotocol.is_set or self.rsvpnbrprotocol.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpnbrprotocol.get_name_leafdata())
                if (self.rsvpnbrstatus.is_set or self.rsvpnbrstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.rsvpnbrstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "rsvpNbrAddress" or name == "rsvpNbrProtocol" or name == "rsvpNbrStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpNbrAddress"):
                    self.rsvpnbraddress = value
                    self.rsvpnbraddress.value_namespace = name_space
                    self.rsvpnbraddress.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpNbrProtocol"):
                    self.rsvpnbrprotocol = value
                    self.rsvpnbrprotocol.value_namespace = name_space
                    self.rsvpnbrprotocol.value_namespace_prefix = name_space_prefix
                if(value_path == "rsvpNbrStatus"):
                    self.rsvpnbrstatus = value
                    self.rsvpnbrstatus.value_namespace = name_space
                    self.rsvpnbrstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.rsvpnbrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.rsvpnbrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rsvpNbrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "RSVP-MIB:RSVP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "rsvpNbrEntry"):
                for c in self.rsvpnbrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = RsvpMib.Rsvpnbrtable.Rsvpnbrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.rsvpnbrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "rsvpNbrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.rsvpgenobjects is not None and self.rsvpgenobjects.has_data()) or
            (self.rsvpiftable is not None and self.rsvpiftable.has_data()) or
            (self.rsvpnbrtable is not None and self.rsvpnbrtable.has_data()) or
            (self.rsvpresvfwdtable is not None and self.rsvpresvfwdtable.has_data()) or
            (self.rsvpresvtable is not None and self.rsvpresvtable.has_data()) or
            (self.rsvpsenderoutinterfacetable is not None and self.rsvpsenderoutinterfacetable.has_data()) or
            (self.rsvpsendertable is not None and self.rsvpsendertable.has_data()) or
            (self.rsvpsessiontable is not None and self.rsvpsessiontable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.rsvpgenobjects is not None and self.rsvpgenobjects.has_operation()) or
            (self.rsvpiftable is not None and self.rsvpiftable.has_operation()) or
            (self.rsvpnbrtable is not None and self.rsvpnbrtable.has_operation()) or
            (self.rsvpresvfwdtable is not None and self.rsvpresvfwdtable.has_operation()) or
            (self.rsvpresvtable is not None and self.rsvpresvtable.has_operation()) or
            (self.rsvpsenderoutinterfacetable is not None and self.rsvpsenderoutinterfacetable.has_operation()) or
            (self.rsvpsendertable is not None and self.rsvpsendertable.has_operation()) or
            (self.rsvpsessiontable is not None and self.rsvpsessiontable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "RSVP-MIB:RSVP-MIB" + path_buffer

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

        if (child_yang_name == "rsvpGenObjects"):
            if (self.rsvpgenobjects is None):
                self.rsvpgenobjects = RsvpMib.Rsvpgenobjects()
                self.rsvpgenobjects.parent = self
                self._children_name_map["rsvpgenobjects"] = "rsvpGenObjects"
            return self.rsvpgenobjects

        if (child_yang_name == "rsvpIfTable"):
            if (self.rsvpiftable is None):
                self.rsvpiftable = RsvpMib.Rsvpiftable()
                self.rsvpiftable.parent = self
                self._children_name_map["rsvpiftable"] = "rsvpIfTable"
            return self.rsvpiftable

        if (child_yang_name == "rsvpNbrTable"):
            if (self.rsvpnbrtable is None):
                self.rsvpnbrtable = RsvpMib.Rsvpnbrtable()
                self.rsvpnbrtable.parent = self
                self._children_name_map["rsvpnbrtable"] = "rsvpNbrTable"
            return self.rsvpnbrtable

        if (child_yang_name == "rsvpResvFwdTable"):
            if (self.rsvpresvfwdtable is None):
                self.rsvpresvfwdtable = RsvpMib.Rsvpresvfwdtable()
                self.rsvpresvfwdtable.parent = self
                self._children_name_map["rsvpresvfwdtable"] = "rsvpResvFwdTable"
            return self.rsvpresvfwdtable

        if (child_yang_name == "rsvpResvTable"):
            if (self.rsvpresvtable is None):
                self.rsvpresvtable = RsvpMib.Rsvpresvtable()
                self.rsvpresvtable.parent = self
                self._children_name_map["rsvpresvtable"] = "rsvpResvTable"
            return self.rsvpresvtable

        if (child_yang_name == "rsvpSenderOutInterfaceTable"):
            if (self.rsvpsenderoutinterfacetable is None):
                self.rsvpsenderoutinterfacetable = RsvpMib.Rsvpsenderoutinterfacetable()
                self.rsvpsenderoutinterfacetable.parent = self
                self._children_name_map["rsvpsenderoutinterfacetable"] = "rsvpSenderOutInterfaceTable"
            return self.rsvpsenderoutinterfacetable

        if (child_yang_name == "rsvpSenderTable"):
            if (self.rsvpsendertable is None):
                self.rsvpsendertable = RsvpMib.Rsvpsendertable()
                self.rsvpsendertable.parent = self
                self._children_name_map["rsvpsendertable"] = "rsvpSenderTable"
            return self.rsvpsendertable

        if (child_yang_name == "rsvpSessionTable"):
            if (self.rsvpsessiontable is None):
                self.rsvpsessiontable = RsvpMib.Rsvpsessiontable()
                self.rsvpsessiontable.parent = self
                self._children_name_map["rsvpsessiontable"] = "rsvpSessionTable"
            return self.rsvpsessiontable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "rsvpGenObjects" or name == "rsvpIfTable" or name == "rsvpNbrTable" or name == "rsvpResvFwdTable" or name == "rsvpResvTable" or name == "rsvpSenderOutInterfaceTable" or name == "rsvpSenderTable" or name == "rsvpSessionTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = RsvpMib()
        return self._top_entity

