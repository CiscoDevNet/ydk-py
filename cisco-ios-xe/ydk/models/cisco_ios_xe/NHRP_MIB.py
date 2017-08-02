""" NHRP_MIB 

This MIB contains managed object definitions for the Next
Hop Resolution Procol, NHRP, as defined in RFC 2332 [17].

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class NhrpMib(Entity):
    """
    
    
    .. attribute:: nhrpcachetable
    
    	This table contains mappings between internetwork layer addresses and NBMA subnetwork layer addresses
    	**type**\:   :py:class:`Nhrpcachetable <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpcachetable>`
    
    .. attribute:: nhrpclientnhstable
    
    	A table of NHSes that are available for use by this NHC (client). By default, the agent will add an entry to this table that corresponds to the client's default router
    	**type**\:   :py:class:`Nhrpclientnhstable <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpclientnhstable>`
    
    .. attribute:: nhrpclientregistrationtable
    
    	A table of Registration Request Information that needs to be maintained by the NHCs (clients)
    	**type**\:   :py:class:`Nhrpclientregistrationtable <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpclientregistrationtable>`
    
    .. attribute:: nhrpclientstattable
    
    	This table contains statistics collected by NHRP clients
    	**type**\:   :py:class:`Nhrpclientstattable <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpclientstattable>`
    
    .. attribute:: nhrpclienttable
    
    	Information about NHRP clients (NHCs) managed by this agent
    	**type**\:   :py:class:`Nhrpclienttable <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpclienttable>`
    
    .. attribute:: nhrpgeneralobjects
    
    	
    	**type**\:   :py:class:`Nhrpgeneralobjects <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpgeneralobjects>`
    
    .. attribute:: nhrppurgereqtable
    
    	This table will track Purge Request Information
    	**type**\:   :py:class:`Nhrppurgereqtable <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrppurgereqtable>`
    
    .. attribute:: nhrpservercachetable
    
    	This table extends the nhrpCacheTable for NHSes.  If the nhrpCacheTable has a row added due to an NHS or based on information regarding an NHS then a row is also added in this table.  The rows in this table will be created when rows in the nhrpCacheTable are created.  However, there may be rows created in the nhrpCacheTable which do not have corresponding rows in this table.  For example, if the nhrpCacheTable has a row added due to a Next Hop Client which is co\-resident on the same device as the NHS, a row will not be added to this table
    	**type**\:   :py:class:`Nhrpservercachetable <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpservercachetable>`
    
    .. attribute:: nhrpservernhctable
    
    	A table of NHCs that are available for use by this NHS (Server)
    	**type**\:   :py:class:`Nhrpservernhctable <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpservernhctable>`
    
    .. attribute:: nhrpserverstattable
    
    	Statistics collected by Next Hop Servers
    	**type**\:   :py:class:`Nhrpserverstattable <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpserverstattable>`
    
    .. attribute:: nhrpservertable
    
    	This table contains information for a set of NHSes associated with this agent
    	**type**\:   :py:class:`Nhrpservertable <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpservertable>`
    
    

    """

    _prefix = 'NHRP-MIB'
    _revision = '1999-08-26'

    def __init__(self):
        super(NhrpMib, self).__init__()
        self._top_entity = None

        self.yang_name = "NHRP-MIB"
        self.yang_parent_name = "NHRP-MIB"

        self.nhrpcachetable = NhrpMib.Nhrpcachetable()
        self.nhrpcachetable.parent = self
        self._children_name_map["nhrpcachetable"] = "nhrpCacheTable"
        self._children_yang_names.add("nhrpCacheTable")

        self.nhrpclientnhstable = NhrpMib.Nhrpclientnhstable()
        self.nhrpclientnhstable.parent = self
        self._children_name_map["nhrpclientnhstable"] = "nhrpClientNhsTable"
        self._children_yang_names.add("nhrpClientNhsTable")

        self.nhrpclientregistrationtable = NhrpMib.Nhrpclientregistrationtable()
        self.nhrpclientregistrationtable.parent = self
        self._children_name_map["nhrpclientregistrationtable"] = "nhrpClientRegistrationTable"
        self._children_yang_names.add("nhrpClientRegistrationTable")

        self.nhrpclientstattable = NhrpMib.Nhrpclientstattable()
        self.nhrpclientstattable.parent = self
        self._children_name_map["nhrpclientstattable"] = "nhrpClientStatTable"
        self._children_yang_names.add("nhrpClientStatTable")

        self.nhrpclienttable = NhrpMib.Nhrpclienttable()
        self.nhrpclienttable.parent = self
        self._children_name_map["nhrpclienttable"] = "nhrpClientTable"
        self._children_yang_names.add("nhrpClientTable")

        self.nhrpgeneralobjects = NhrpMib.Nhrpgeneralobjects()
        self.nhrpgeneralobjects.parent = self
        self._children_name_map["nhrpgeneralobjects"] = "nhrpGeneralObjects"
        self._children_yang_names.add("nhrpGeneralObjects")

        self.nhrppurgereqtable = NhrpMib.Nhrppurgereqtable()
        self.nhrppurgereqtable.parent = self
        self._children_name_map["nhrppurgereqtable"] = "nhrpPurgeReqTable"
        self._children_yang_names.add("nhrpPurgeReqTable")

        self.nhrpservercachetable = NhrpMib.Nhrpservercachetable()
        self.nhrpservercachetable.parent = self
        self._children_name_map["nhrpservercachetable"] = "nhrpServerCacheTable"
        self._children_yang_names.add("nhrpServerCacheTable")

        self.nhrpservernhctable = NhrpMib.Nhrpservernhctable()
        self.nhrpservernhctable.parent = self
        self._children_name_map["nhrpservernhctable"] = "nhrpServerNhcTable"
        self._children_yang_names.add("nhrpServerNhcTable")

        self.nhrpserverstattable = NhrpMib.Nhrpserverstattable()
        self.nhrpserverstattable.parent = self
        self._children_name_map["nhrpserverstattable"] = "nhrpServerStatTable"
        self._children_yang_names.add("nhrpServerStatTable")

        self.nhrpservertable = NhrpMib.Nhrpservertable()
        self.nhrpservertable.parent = self
        self._children_name_map["nhrpservertable"] = "nhrpServerTable"
        self._children_yang_names.add("nhrpServerTable")


    class Nhrpgeneralobjects(Entity):
        """
        
        
        .. attribute:: nhrpnextindex
        
        	This scalar is used for creating rows in the nhrpClientTable and the nhrpServerTable. The value of this variable is a currently unused value for nhrpClientIndex and nhrpServerIndex.     The value returned when reading this variable must be unique for the NHC's and NHS's indices associated with this row. Subsequent attempts to read this variable must return different values.  NOTE\:  this object exists in the General Group because it is to be used in establishing rows in the nhrpClientTable and the nhrpServerTable.  In other words, the value retrieved from this object could become the value of nhrpClientIndex and nhprServerIndex.  In the situation of an agent re\-initialization the value of this object must be saved in non\-volatile storage.  This variable will return the special value 0 if no new rows can be created
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NhrpMib.Nhrpgeneralobjects, self).__init__()

            self.yang_name = "nhrpGeneralObjects"
            self.yang_parent_name = "NHRP-MIB"

            self.nhrpnextindex = YLeaf(YType.uint32, "nhrpNextIndex")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("nhrpnextindex") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(NhrpMib.Nhrpgeneralobjects, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NhrpMib.Nhrpgeneralobjects, self).__setattr__(name, value)

        def has_data(self):
            return self.nhrpnextindex.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.nhrpnextindex.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nhrpGeneralObjects" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "NHRP-MIB:NHRP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.nhrpnextindex.is_set or self.nhrpnextindex.yfilter != YFilter.not_set):
                leaf_name_data.append(self.nhrpnextindex.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nhrpNextIndex"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "nhrpNextIndex"):
                self.nhrpnextindex = value
                self.nhrpnextindex.value_namespace = name_space
                self.nhrpnextindex.value_namespace_prefix = name_space_prefix


    class Nhrpcachetable(Entity):
        """
        This table contains mappings between internetwork layer
        addresses and NBMA subnetwork layer addresses.
        
        .. attribute:: nhrpcacheentry
        
        	A cached mapping between an internetwork layer address and an NBMA address. Entries can be created by the network administrator using the nhrpCacheRowStatus column, or they may be added dynamically based on protocol operation (including NHRP, SCSP, and others, such as ATMARP).  When created based by NHRP protocol operations this entry is largely based on contents contained in the Client Information Entry (CIE).  Zero or more Client Information Entries (CIEs) may be included in the NHRP Packet. For a complete description of the CIE, refer to Section 5.2.0.1 of RFC 2332 [17]
        	**type**\: list of    :py:class:`Nhrpcacheentry <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpcachetable.Nhrpcacheentry>`
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NhrpMib.Nhrpcachetable, self).__init__()

            self.yang_name = "nhrpCacheTable"
            self.yang_parent_name = "NHRP-MIB"

            self.nhrpcacheentry = YList(self)

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
                        super(NhrpMib.Nhrpcachetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NhrpMib.Nhrpcachetable, self).__setattr__(name, value)


        class Nhrpcacheentry(Entity):
            """
            A cached mapping between an internetwork layer address
            and an NBMA address. Entries can be created by the
            network administrator using the nhrpCacheRowStatus
            column, or they may be added dynamically based on
            protocol operation (including NHRP, SCSP, and others,
            such as ATMARP).
            
            When created based by NHRP protocol operations
            this entry is largely based on contents contained in
            the Client Information Entry (CIE).
            
            Zero or more Client Information Entries (CIEs) may be
            included in the NHRP Packet. For a complete description
            of the CIE, refer to Section 5.2.0.1 of
            RFC 2332 [17].
            
            .. attribute:: nhrpcacheinternetworkaddrtype  <key>
            
            	The internetwork layer address type of this Next Hop Resolution Cache entry. The value of this object indicates how to interpret the values of nhrpCacheInternetworkAddr and nhrpCacheNextHopInternetworkAddr
            	**type**\:   :py:class:`Addressfamilynumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.Addressfamilynumbers>`
            
            .. attribute:: nhrpcacheinternetworkaddr  <key>
            
            	The value of the internetwork address of the destination
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: nhrpcacheindex  <key>
            
            	An identifier for this entry that has local significance within the scope of the General Group.  This identifier is used here to uniquely identify this row, and also used in the 'nhrpPurgeTable' for the value of the 'nhrpPurgeCacheIdentifier'
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrpcacheholdingtime
            
            	If the value of 'nhrpCacheHoldingTimeValid is true(1) then this object represents the number of seconds that the cache entry will remain in this table.  When this value reaches 0 (zero) the row should be deleted.  If the value of 'nhrpCacheHoldingTimeValid is false(2) then this object is undefined
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: seconds
            
            .. attribute:: nhrpcacheholdingtimevalid
            
            	True(1) is returned if the value of 'nhrpCacheType' is not 'administrativelyAdded'.  Since the value of 'nhrpCacheType' was not configured by a user, the value of 'nhrpCacheHoldingTime' is considered valid.  In other words, the value of 'nhrpCacheHoldingTime' represents the Holding Time for the cache Entry.  If 'nhrpCacheType has been configured by a user, (i.e. the value of 'nhrpCacheType' is 'administrativelyAdded') then false(2) will be returned. This indicates that the value of 'nhrpCacheHoldingTime' is undefined because this row could possibly be backed up in nonvolatile storage
            	**type**\:  bool
            
            .. attribute:: nhrpcachenbmaaddr
            
            	The value of the NBMA subnetwork address of the next hop
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: nhrpcachenbmaaddrtype
            
            	The NBMA address type. The value of this object indicates how to interpret the values of nhrpCacheNbmaAddr and nhrpCacheNbmaSubaddr
            	**type**\:   :py:class:`Addressfamilynumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.Addressfamilynumbers>`
            
            .. attribute:: nhrpcachenbmasubaddr
            
            	The value of the NBMA subaddress of the next hop. If there is no subaddress concept for the NBMA address family, this value will be a zero\-length OCTET STRING
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: nhrpcachenegotiatedmtu
            
            	The maximum transmission unit (MTU) that was negotiated or registered for this entity. In other words, this is the actual MTU being used
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: nhrpcachenexthopinternetworkaddr
            
            	The value of the internetwork address of the next hop
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: nhrpcachepreference
            
            	An object which reflects the Preference value of the Client Information Entry (CIE).  Zero or more Client Information Entries (CIEs) may be included in the NHRP Packet.  One of the fields in the CIE is the Preference.  For a complete description of the CIE, refer to Section 5.2.0.1 of  RFC 2332 [17]
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: nhrpcacheprefixlength
            
            	The number of bits that define the internetwork layer prefix associated with the nhrpCacheInternetworkAddr
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: nhrpcacherowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: nhrpcachestate
            
            	An indication of the state of this entry. The values are\:  'incomplete(1)' The client has sent a NHRP Resolution                 Request but has not yet received the                 NHRP Resolution Reply.   'ackReply(2)'   For a client or server, this is a                 cached valid mapping.  'nakReply(3)'   For a client or server, this is a                 cached NAK mapping
            	**type**\:   :py:class:`Nhrpcachestate <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpcachetable.Nhrpcacheentry.Nhrpcachestate>`
            
            .. attribute:: nhrpcachestoragetype
            
            	This value only has meaning when the 'nhrpCacheType' has the value of 'administrativelyAdded'.  When the row is created due to being 'administrativelyAdded', this object reflects whether this row is kept in volatile storage and lost upon reboot or if this row is backed up by non\-volatile or permanent storage.  If the value of 'nhrpCacheType' has a value which is not 'administrativelyAdded, then the value of this object is 'other(1)'
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: nhrpcachetype
            
            	An indication of how this cache entry was created. The values are\:  'other(1)'                   The entry was added by some                              other means.  'register(2)'                In a server, added based on a                              client registration.  'resolveAuthoritative(3)'    In a client, added based on                              receiving an Authoritative                              NHRP Resolution Reply.     'resolveNonauthoritative(4)' In a client, added based on                              receiving a Nonauthoritative                              NHRP Resolution Reply.  'transit(5)'                 In a transit server, added by                              examining a forwarded NHRP                              packet.  'administrativelyAdded(6)'   In a client or server,                              manually added by the                              administrator. The                              StorageType of this entry is                              reflected in                              'nhrpCacheStorageType'.  'atmarp(7)'                  The entry was added due to an                              ATMARP.  'scsp(8)'                    The entry was added due to                              SCSP.   When the entry is under creation using the nhrpCacheRowStatus column, the only value that can be specified by the administrator is 'administrativelyAdded'. Attempting to set any other value will cause an 'inconsistentValue' error.  The value cannot be modified once the entry is active
            	**type**\:   :py:class:`Nhrpcachetype <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpcachetable.Nhrpcacheentry.Nhrpcachetype>`
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NhrpMib.Nhrpcachetable.Nhrpcacheentry, self).__init__()

                self.yang_name = "nhrpCacheEntry"
                self.yang_parent_name = "nhrpCacheTable"

                self.nhrpcacheinternetworkaddrtype = YLeaf(YType.enumeration, "nhrpCacheInternetworkAddrType")

                self.nhrpcacheinternetworkaddr = YLeaf(YType.str, "nhrpCacheInternetworkAddr")

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.nhrpcacheindex = YLeaf(YType.uint32, "nhrpCacheIndex")

                self.nhrpcacheholdingtime = YLeaf(YType.uint32, "nhrpCacheHoldingTime")

                self.nhrpcacheholdingtimevalid = YLeaf(YType.boolean, "nhrpCacheHoldingTimeValid")

                self.nhrpcachenbmaaddr = YLeaf(YType.str, "nhrpCacheNbmaAddr")

                self.nhrpcachenbmaaddrtype = YLeaf(YType.enumeration, "nhrpCacheNbmaAddrType")

                self.nhrpcachenbmasubaddr = YLeaf(YType.str, "nhrpCacheNbmaSubaddr")

                self.nhrpcachenegotiatedmtu = YLeaf(YType.int32, "nhrpCacheNegotiatedMtu")

                self.nhrpcachenexthopinternetworkaddr = YLeaf(YType.str, "nhrpCacheNextHopInternetworkAddr")

                self.nhrpcachepreference = YLeaf(YType.int32, "nhrpCachePreference")

                self.nhrpcacheprefixlength = YLeaf(YType.int32, "nhrpCachePrefixLength")

                self.nhrpcacherowstatus = YLeaf(YType.enumeration, "nhrpCacheRowStatus")

                self.nhrpcachestate = YLeaf(YType.enumeration, "nhrpCacheState")

                self.nhrpcachestoragetype = YLeaf(YType.enumeration, "nhrpCacheStorageType")

                self.nhrpcachetype = YLeaf(YType.enumeration, "nhrpCacheType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("nhrpcacheinternetworkaddrtype",
                                "nhrpcacheinternetworkaddr",
                                "ifindex",
                                "nhrpcacheindex",
                                "nhrpcacheholdingtime",
                                "nhrpcacheholdingtimevalid",
                                "nhrpcachenbmaaddr",
                                "nhrpcachenbmaaddrtype",
                                "nhrpcachenbmasubaddr",
                                "nhrpcachenegotiatedmtu",
                                "nhrpcachenexthopinternetworkaddr",
                                "nhrpcachepreference",
                                "nhrpcacheprefixlength",
                                "nhrpcacherowstatus",
                                "nhrpcachestate",
                                "nhrpcachestoragetype",
                                "nhrpcachetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NhrpMib.Nhrpcachetable.Nhrpcacheentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NhrpMib.Nhrpcachetable.Nhrpcacheentry, self).__setattr__(name, value)

            class Nhrpcachestate(Enum):
                """
                Nhrpcachestate

                An indication of the state of this entry. The values are\:

                'incomplete(1)' The client has sent a NHRP Resolution

                                Request but has not yet received the

                                NHRP Resolution Reply.

                'ackReply(2)'   For a client or server, this is a

                                cached valid mapping.

                'nakReply(3)'   For a client or server, this is a

                                cached NAK mapping.

                .. data:: incomplete = 1

                .. data:: ackReply = 2

                .. data:: nakReply = 3

                """

                incomplete = Enum.YLeaf(1, "incomplete")

                ackReply = Enum.YLeaf(2, "ackReply")

                nakReply = Enum.YLeaf(3, "nakReply")


            class Nhrpcachetype(Enum):
                """
                Nhrpcachetype

                An indication of how this cache entry

                was created. The values are\:

                'other(1)'                   The entry was added by some

                                             other means.

                'register(2)'                In a server, added based on a

                                             client registration.

                'resolveAuthoritative(3)'    In a client, added based on

                                             receiving an Authoritative

                                             NHRP Resolution Reply.

                'resolveNonauthoritative(4)' In a client, added based on

                                             receiving a Nonauthoritative

                                             NHRP Resolution Reply.

                'transit(5)'                 In a transit server, added by

                                             examining a forwarded NHRP

                                             packet.

                'administrativelyAdded(6)'   In a client or server,

                                             manually added by the

                                             administrator. The

                                             StorageType of this entry is

                                             reflected in

                                             'nhrpCacheStorageType'.

                'atmarp(7)'                  The entry was added due to an

                                             ATMARP.

                'scsp(8)'                    The entry was added due to

                                             SCSP.

                When the entry is under creation using the

                nhrpCacheRowStatus column, the only value that can be

                specified by the administrator is 'administrativelyAdded'.

                Attempting to set any other value will cause an

                'inconsistentValue' error.

                The value cannot be modified once the entry is active.

                .. data:: other = 1

                .. data:: register = 2

                .. data:: resolveAuthoritative = 3

                .. data:: resoveNonauthoritative = 4

                .. data:: transit = 5

                .. data:: administrativelyAdded = 6

                .. data:: atmarp = 7

                .. data:: scsp = 8

                """

                other = Enum.YLeaf(1, "other")

                register = Enum.YLeaf(2, "register")

                resolveAuthoritative = Enum.YLeaf(3, "resolveAuthoritative")

                resoveNonauthoritative = Enum.YLeaf(4, "resoveNonauthoritative")

                transit = Enum.YLeaf(5, "transit")

                administrativelyAdded = Enum.YLeaf(6, "administrativelyAdded")

                atmarp = Enum.YLeaf(7, "atmarp")

                scsp = Enum.YLeaf(8, "scsp")


            def has_data(self):
                return (
                    self.nhrpcacheinternetworkaddrtype.is_set or
                    self.nhrpcacheinternetworkaddr.is_set or
                    self.ifindex.is_set or
                    self.nhrpcacheindex.is_set or
                    self.nhrpcacheholdingtime.is_set or
                    self.nhrpcacheholdingtimevalid.is_set or
                    self.nhrpcachenbmaaddr.is_set or
                    self.nhrpcachenbmaaddrtype.is_set or
                    self.nhrpcachenbmasubaddr.is_set or
                    self.nhrpcachenegotiatedmtu.is_set or
                    self.nhrpcachenexthopinternetworkaddr.is_set or
                    self.nhrpcachepreference.is_set or
                    self.nhrpcacheprefixlength.is_set or
                    self.nhrpcacherowstatus.is_set or
                    self.nhrpcachestate.is_set or
                    self.nhrpcachestoragetype.is_set or
                    self.nhrpcachetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.nhrpcacheinternetworkaddrtype.yfilter != YFilter.not_set or
                    self.nhrpcacheinternetworkaddr.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.nhrpcacheindex.yfilter != YFilter.not_set or
                    self.nhrpcacheholdingtime.yfilter != YFilter.not_set or
                    self.nhrpcacheholdingtimevalid.yfilter != YFilter.not_set or
                    self.nhrpcachenbmaaddr.yfilter != YFilter.not_set or
                    self.nhrpcachenbmaaddrtype.yfilter != YFilter.not_set or
                    self.nhrpcachenbmasubaddr.yfilter != YFilter.not_set or
                    self.nhrpcachenegotiatedmtu.yfilter != YFilter.not_set or
                    self.nhrpcachenexthopinternetworkaddr.yfilter != YFilter.not_set or
                    self.nhrpcachepreference.yfilter != YFilter.not_set or
                    self.nhrpcacheprefixlength.yfilter != YFilter.not_set or
                    self.nhrpcacherowstatus.yfilter != YFilter.not_set or
                    self.nhrpcachestate.yfilter != YFilter.not_set or
                    self.nhrpcachestoragetype.yfilter != YFilter.not_set or
                    self.nhrpcachetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nhrpCacheEntry" + "[nhrpCacheInternetworkAddrType='" + self.nhrpcacheinternetworkaddrtype.get() + "']" + "[nhrpCacheInternetworkAddr='" + self.nhrpcacheinternetworkaddr.get() + "']" + "[ifIndex='" + self.ifindex.get() + "']" + "[nhrpCacheIndex='" + self.nhrpcacheindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "NHRP-MIB:NHRP-MIB/nhrpCacheTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.nhrpcacheinternetworkaddrtype.is_set or self.nhrpcacheinternetworkaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcacheinternetworkaddrtype.get_name_leafdata())
                if (self.nhrpcacheinternetworkaddr.is_set or self.nhrpcacheinternetworkaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcacheinternetworkaddr.get_name_leafdata())
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.nhrpcacheindex.is_set or self.nhrpcacheindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcacheindex.get_name_leafdata())
                if (self.nhrpcacheholdingtime.is_set or self.nhrpcacheholdingtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcacheholdingtime.get_name_leafdata())
                if (self.nhrpcacheholdingtimevalid.is_set or self.nhrpcacheholdingtimevalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcacheholdingtimevalid.get_name_leafdata())
                if (self.nhrpcachenbmaaddr.is_set or self.nhrpcachenbmaaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcachenbmaaddr.get_name_leafdata())
                if (self.nhrpcachenbmaaddrtype.is_set or self.nhrpcachenbmaaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcachenbmaaddrtype.get_name_leafdata())
                if (self.nhrpcachenbmasubaddr.is_set or self.nhrpcachenbmasubaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcachenbmasubaddr.get_name_leafdata())
                if (self.nhrpcachenegotiatedmtu.is_set or self.nhrpcachenegotiatedmtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcachenegotiatedmtu.get_name_leafdata())
                if (self.nhrpcachenexthopinternetworkaddr.is_set or self.nhrpcachenexthopinternetworkaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcachenexthopinternetworkaddr.get_name_leafdata())
                if (self.nhrpcachepreference.is_set or self.nhrpcachepreference.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcachepreference.get_name_leafdata())
                if (self.nhrpcacheprefixlength.is_set or self.nhrpcacheprefixlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcacheprefixlength.get_name_leafdata())
                if (self.nhrpcacherowstatus.is_set or self.nhrpcacherowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcacherowstatus.get_name_leafdata())
                if (self.nhrpcachestate.is_set or self.nhrpcachestate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcachestate.get_name_leafdata())
                if (self.nhrpcachestoragetype.is_set or self.nhrpcachestoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcachestoragetype.get_name_leafdata())
                if (self.nhrpcachetype.is_set or self.nhrpcachetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcachetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "nhrpCacheInternetworkAddrType" or name == "nhrpCacheInternetworkAddr" or name == "ifIndex" or name == "nhrpCacheIndex" or name == "nhrpCacheHoldingTime" or name == "nhrpCacheHoldingTimeValid" or name == "nhrpCacheNbmaAddr" or name == "nhrpCacheNbmaAddrType" or name == "nhrpCacheNbmaSubaddr" or name == "nhrpCacheNegotiatedMtu" or name == "nhrpCacheNextHopInternetworkAddr" or name == "nhrpCachePreference" or name == "nhrpCachePrefixLength" or name == "nhrpCacheRowStatus" or name == "nhrpCacheState" or name == "nhrpCacheStorageType" or name == "nhrpCacheType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "nhrpCacheInternetworkAddrType"):
                    self.nhrpcacheinternetworkaddrtype = value
                    self.nhrpcacheinternetworkaddrtype.value_namespace = name_space
                    self.nhrpcacheinternetworkaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpCacheInternetworkAddr"):
                    self.nhrpcacheinternetworkaddr = value
                    self.nhrpcacheinternetworkaddr.value_namespace = name_space
                    self.nhrpcacheinternetworkaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpCacheIndex"):
                    self.nhrpcacheindex = value
                    self.nhrpcacheindex.value_namespace = name_space
                    self.nhrpcacheindex.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpCacheHoldingTime"):
                    self.nhrpcacheholdingtime = value
                    self.nhrpcacheholdingtime.value_namespace = name_space
                    self.nhrpcacheholdingtime.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpCacheHoldingTimeValid"):
                    self.nhrpcacheholdingtimevalid = value
                    self.nhrpcacheholdingtimevalid.value_namespace = name_space
                    self.nhrpcacheholdingtimevalid.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpCacheNbmaAddr"):
                    self.nhrpcachenbmaaddr = value
                    self.nhrpcachenbmaaddr.value_namespace = name_space
                    self.nhrpcachenbmaaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpCacheNbmaAddrType"):
                    self.nhrpcachenbmaaddrtype = value
                    self.nhrpcachenbmaaddrtype.value_namespace = name_space
                    self.nhrpcachenbmaaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpCacheNbmaSubaddr"):
                    self.nhrpcachenbmasubaddr = value
                    self.nhrpcachenbmasubaddr.value_namespace = name_space
                    self.nhrpcachenbmasubaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpCacheNegotiatedMtu"):
                    self.nhrpcachenegotiatedmtu = value
                    self.nhrpcachenegotiatedmtu.value_namespace = name_space
                    self.nhrpcachenegotiatedmtu.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpCacheNextHopInternetworkAddr"):
                    self.nhrpcachenexthopinternetworkaddr = value
                    self.nhrpcachenexthopinternetworkaddr.value_namespace = name_space
                    self.nhrpcachenexthopinternetworkaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpCachePreference"):
                    self.nhrpcachepreference = value
                    self.nhrpcachepreference.value_namespace = name_space
                    self.nhrpcachepreference.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpCachePrefixLength"):
                    self.nhrpcacheprefixlength = value
                    self.nhrpcacheprefixlength.value_namespace = name_space
                    self.nhrpcacheprefixlength.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpCacheRowStatus"):
                    self.nhrpcacherowstatus = value
                    self.nhrpcacherowstatus.value_namespace = name_space
                    self.nhrpcacherowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpCacheState"):
                    self.nhrpcachestate = value
                    self.nhrpcachestate.value_namespace = name_space
                    self.nhrpcachestate.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpCacheStorageType"):
                    self.nhrpcachestoragetype = value
                    self.nhrpcachestoragetype.value_namespace = name_space
                    self.nhrpcachestoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpCacheType"):
                    self.nhrpcachetype = value
                    self.nhrpcachetype.value_namespace = name_space
                    self.nhrpcachetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.nhrpcacheentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.nhrpcacheentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nhrpCacheTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "NHRP-MIB:NHRP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "nhrpCacheEntry"):
                for c in self.nhrpcacheentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NhrpMib.Nhrpcachetable.Nhrpcacheentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.nhrpcacheentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nhrpCacheEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Nhrppurgereqtable(Entity):
        """
        This table will track Purge Request Information.
        
        .. attribute:: nhrppurgereqentry
        
        	Information regarding a Purge Request
        	**type**\: list of    :py:class:`Nhrppurgereqentry <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrppurgereqtable.Nhrppurgereqentry>`
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NhrpMib.Nhrppurgereqtable, self).__init__()

            self.yang_name = "nhrpPurgeReqTable"
            self.yang_parent_name = "NHRP-MIB"

            self.nhrppurgereqentry = YList(self)

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
                        super(NhrpMib.Nhrppurgereqtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NhrpMib.Nhrppurgereqtable, self).__setattr__(name, value)


        class Nhrppurgereqentry(Entity):
            """
            Information regarding a Purge Request.
            
            .. attribute:: nhrppurgeindex  <key>
            
            	An index for this entry that has local significance within the scope of this table
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrppurgecacheidentifier
            
            	This object identifies which row in 'nhrpCacheTable' is being purged.  This object should have the same value as the 'nhrpCacheIndex' in the 'nhrpCacheTable'
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrppurgeprefixlength
            
            	In the case of NHRP Purge Requests, this specifies the equivalence class of addresses which match the first 'Prefix Length' bit positions of the Client Protocol Address specified in the Client Information Entry (CIE)
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: nhrppurgereplyexpected
            
            	An indication of whether this Purge Request has the 'N' Bit cleared (off)
            	**type**\:  bool
            
            .. attribute:: nhrppurgerequestid
            
            	The Request ID used in the purge request
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrppurgerowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NhrpMib.Nhrppurgereqtable.Nhrppurgereqentry, self).__init__()

                self.yang_name = "nhrpPurgeReqEntry"
                self.yang_parent_name = "nhrpPurgeReqTable"

                self.nhrppurgeindex = YLeaf(YType.uint32, "nhrpPurgeIndex")

                self.nhrppurgecacheidentifier = YLeaf(YType.uint32, "nhrpPurgeCacheIdentifier")

                self.nhrppurgeprefixlength = YLeaf(YType.int32, "nhrpPurgePrefixLength")

                self.nhrppurgereplyexpected = YLeaf(YType.boolean, "nhrpPurgeReplyExpected")

                self.nhrppurgerequestid = YLeaf(YType.uint32, "nhrpPurgeRequestID")

                self.nhrppurgerowstatus = YLeaf(YType.enumeration, "nhrpPurgeRowStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("nhrppurgeindex",
                                "nhrppurgecacheidentifier",
                                "nhrppurgeprefixlength",
                                "nhrppurgereplyexpected",
                                "nhrppurgerequestid",
                                "nhrppurgerowstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NhrpMib.Nhrppurgereqtable.Nhrppurgereqentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NhrpMib.Nhrppurgereqtable.Nhrppurgereqentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.nhrppurgeindex.is_set or
                    self.nhrppurgecacheidentifier.is_set or
                    self.nhrppurgeprefixlength.is_set or
                    self.nhrppurgereplyexpected.is_set or
                    self.nhrppurgerequestid.is_set or
                    self.nhrppurgerowstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.nhrppurgeindex.yfilter != YFilter.not_set or
                    self.nhrppurgecacheidentifier.yfilter != YFilter.not_set or
                    self.nhrppurgeprefixlength.yfilter != YFilter.not_set or
                    self.nhrppurgereplyexpected.yfilter != YFilter.not_set or
                    self.nhrppurgerequestid.yfilter != YFilter.not_set or
                    self.nhrppurgerowstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nhrpPurgeReqEntry" + "[nhrpPurgeIndex='" + self.nhrppurgeindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "NHRP-MIB:NHRP-MIB/nhrpPurgeReqTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.nhrppurgeindex.is_set or self.nhrppurgeindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrppurgeindex.get_name_leafdata())
                if (self.nhrppurgecacheidentifier.is_set or self.nhrppurgecacheidentifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrppurgecacheidentifier.get_name_leafdata())
                if (self.nhrppurgeprefixlength.is_set or self.nhrppurgeprefixlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrppurgeprefixlength.get_name_leafdata())
                if (self.nhrppurgereplyexpected.is_set or self.nhrppurgereplyexpected.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrppurgereplyexpected.get_name_leafdata())
                if (self.nhrppurgerequestid.is_set or self.nhrppurgerequestid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrppurgerequestid.get_name_leafdata())
                if (self.nhrppurgerowstatus.is_set or self.nhrppurgerowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrppurgerowstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "nhrpPurgeIndex" or name == "nhrpPurgeCacheIdentifier" or name == "nhrpPurgePrefixLength" or name == "nhrpPurgeReplyExpected" or name == "nhrpPurgeRequestID" or name == "nhrpPurgeRowStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "nhrpPurgeIndex"):
                    self.nhrppurgeindex = value
                    self.nhrppurgeindex.value_namespace = name_space
                    self.nhrppurgeindex.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpPurgeCacheIdentifier"):
                    self.nhrppurgecacheidentifier = value
                    self.nhrppurgecacheidentifier.value_namespace = name_space
                    self.nhrppurgecacheidentifier.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpPurgePrefixLength"):
                    self.nhrppurgeprefixlength = value
                    self.nhrppurgeprefixlength.value_namespace = name_space
                    self.nhrppurgeprefixlength.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpPurgeReplyExpected"):
                    self.nhrppurgereplyexpected = value
                    self.nhrppurgereplyexpected.value_namespace = name_space
                    self.nhrppurgereplyexpected.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpPurgeRequestID"):
                    self.nhrppurgerequestid = value
                    self.nhrppurgerequestid.value_namespace = name_space
                    self.nhrppurgerequestid.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpPurgeRowStatus"):
                    self.nhrppurgerowstatus = value
                    self.nhrppurgerowstatus.value_namespace = name_space
                    self.nhrppurgerowstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.nhrppurgereqentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.nhrppurgereqentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nhrpPurgeReqTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "NHRP-MIB:NHRP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "nhrpPurgeReqEntry"):
                for c in self.nhrppurgereqentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NhrpMib.Nhrppurgereqtable.Nhrppurgereqentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.nhrppurgereqentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nhrpPurgeReqEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Nhrpclienttable(Entity):
        """
        Information about NHRP clients (NHCs) managed by this
        agent.
        
        .. attribute:: nhrpcliententry
        
        	Information about a single NHC
        	**type**\: list of    :py:class:`Nhrpcliententry <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpclienttable.Nhrpcliententry>`
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NhrpMib.Nhrpclienttable, self).__init__()

            self.yang_name = "nhrpClientTable"
            self.yang_parent_name = "NHRP-MIB"

            self.nhrpcliententry = YList(self)

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
                        super(NhrpMib.Nhrpclienttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NhrpMib.Nhrpclienttable, self).__setattr__(name, value)


        class Nhrpcliententry(Entity):
            """
            Information about a single NHC.
            
            .. attribute:: nhrpclientindex  <key>
            
            	An identifier for the NHRP client that is unique within the scope of this agent.  The 'nhrpNextIndex' value should be consulted (read), prior to creating a row in this table, and the value returned from reading 'nhrpNextIndex' should be used as this object's value
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrpclientdefaultmtu
            
            	The default maximum transmission unit (MTU) of the LIS/LAG which this client should use. This object will be initialized by the agent to the default MTU of the LIS/LAG (which is 9180) unless a different MTU value is specified during creation of this Client
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: nhrpclientholdtime
            
            	The hold time the client will register
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: seconds
            
            .. attribute:: nhrpclientinitialrequesttimeout
            
            	The number of seconds that the client will wait before timing out an NHRP initial request.  This object only has meaning for the initial timeout period
            	**type**\:  int
            
            	**range:** 1..900
            
            	**units**\: seconds
            
            .. attribute:: nhrpclientinternetworkaddr
            
            	The value of the internetwork layer address of this client
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: nhrpclientinternetworkaddrtype
            
            	The type of the internetwork layer address of this client. This object indicates how the value of nhrpClientInternetworkAddr is to be interpreted
            	**type**\:   :py:class:`Addressfamilynumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.Addressfamilynumbers>`
            
            .. attribute:: nhrpclientnbmaaddr
            
            	The NBMA subnetwork address of this client
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: nhrpclientnbmaaddrtype
            
            	The type of the NBMA subnetwork address of this client. This object indicates how the values of nhrpClientNbmaAddr and nhrpClientNbmaSubaddr are to be interpreted
            	**type**\:   :py:class:`Addressfamilynumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.Addressfamilynumbers>`
            
            .. attribute:: nhrpclientnbmasubaddr
            
            	The NBMA subaddress of this client. For NBMA address families without a subaddress concept, this will be a zero\-length OCTET STRING
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: nhrpclientpurgerequestretries
            
            	The number of times the client will retry a purge request before failure. A value of 0 means don't retry. A value of 65535 means retry forever
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: nhrpclientregistrationrequestretries
            
            	The number of times the client will retry the registration request before failure. A value of 0 means don't retry. A value of 65535 means retry forever
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: nhrpclientrequestid
            
            	The Request ID used to register this client with its server. According to Section 5.2.3 of the NHRP Specification, RFC 2332 [17], the Request ID must be kept in non\-volatile storage, so that if an NHC crashes and  re\-initializes, it will use a different  Request ID during the registration process when reregistering with the same NHS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientresolutionrequestretries
            
            	The number of times the client will retry the resolution request before failure. A value of 0 means don't retry. A value of 65535 means retry forever
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: nhrpclientrowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: nhrpclientstoragetype
            
            	This object defines whether this row is kept in volatile storage and lost upon a Client crash or reboot situation, or if this row is backed up by nonvolatile or permanent storage
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NhrpMib.Nhrpclienttable.Nhrpcliententry, self).__init__()

                self.yang_name = "nhrpClientEntry"
                self.yang_parent_name = "nhrpClientTable"

                self.nhrpclientindex = YLeaf(YType.uint32, "nhrpClientIndex")

                self.nhrpclientdefaultmtu = YLeaf(YType.uint32, "nhrpClientDefaultMtu")

                self.nhrpclientholdtime = YLeaf(YType.uint32, "nhrpClientHoldTime")

                self.nhrpclientinitialrequesttimeout = YLeaf(YType.int32, "nhrpClientInitialRequestTimeout")

                self.nhrpclientinternetworkaddr = YLeaf(YType.str, "nhrpClientInternetworkAddr")

                self.nhrpclientinternetworkaddrtype = YLeaf(YType.enumeration, "nhrpClientInternetworkAddrType")

                self.nhrpclientnbmaaddr = YLeaf(YType.str, "nhrpClientNbmaAddr")

                self.nhrpclientnbmaaddrtype = YLeaf(YType.enumeration, "nhrpClientNbmaAddrType")

                self.nhrpclientnbmasubaddr = YLeaf(YType.str, "nhrpClientNbmaSubaddr")

                self.nhrpclientpurgerequestretries = YLeaf(YType.int32, "nhrpClientPurgeRequestRetries")

                self.nhrpclientregistrationrequestretries = YLeaf(YType.int32, "nhrpClientRegistrationRequestRetries")

                self.nhrpclientrequestid = YLeaf(YType.uint32, "nhrpClientRequestID")

                self.nhrpclientresolutionrequestretries = YLeaf(YType.int32, "nhrpClientResolutionRequestRetries")

                self.nhrpclientrowstatus = YLeaf(YType.enumeration, "nhrpClientRowStatus")

                self.nhrpclientstoragetype = YLeaf(YType.enumeration, "nhrpClientStorageType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("nhrpclientindex",
                                "nhrpclientdefaultmtu",
                                "nhrpclientholdtime",
                                "nhrpclientinitialrequesttimeout",
                                "nhrpclientinternetworkaddr",
                                "nhrpclientinternetworkaddrtype",
                                "nhrpclientnbmaaddr",
                                "nhrpclientnbmaaddrtype",
                                "nhrpclientnbmasubaddr",
                                "nhrpclientpurgerequestretries",
                                "nhrpclientregistrationrequestretries",
                                "nhrpclientrequestid",
                                "nhrpclientresolutionrequestretries",
                                "nhrpclientrowstatus",
                                "nhrpclientstoragetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NhrpMib.Nhrpclienttable.Nhrpcliententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NhrpMib.Nhrpclienttable.Nhrpcliententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.nhrpclientindex.is_set or
                    self.nhrpclientdefaultmtu.is_set or
                    self.nhrpclientholdtime.is_set or
                    self.nhrpclientinitialrequesttimeout.is_set or
                    self.nhrpclientinternetworkaddr.is_set or
                    self.nhrpclientinternetworkaddrtype.is_set or
                    self.nhrpclientnbmaaddr.is_set or
                    self.nhrpclientnbmaaddrtype.is_set or
                    self.nhrpclientnbmasubaddr.is_set or
                    self.nhrpclientpurgerequestretries.is_set or
                    self.nhrpclientregistrationrequestretries.is_set or
                    self.nhrpclientrequestid.is_set or
                    self.nhrpclientresolutionrequestretries.is_set or
                    self.nhrpclientrowstatus.is_set or
                    self.nhrpclientstoragetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.nhrpclientindex.yfilter != YFilter.not_set or
                    self.nhrpclientdefaultmtu.yfilter != YFilter.not_set or
                    self.nhrpclientholdtime.yfilter != YFilter.not_set or
                    self.nhrpclientinitialrequesttimeout.yfilter != YFilter.not_set or
                    self.nhrpclientinternetworkaddr.yfilter != YFilter.not_set or
                    self.nhrpclientinternetworkaddrtype.yfilter != YFilter.not_set or
                    self.nhrpclientnbmaaddr.yfilter != YFilter.not_set or
                    self.nhrpclientnbmaaddrtype.yfilter != YFilter.not_set or
                    self.nhrpclientnbmasubaddr.yfilter != YFilter.not_set or
                    self.nhrpclientpurgerequestretries.yfilter != YFilter.not_set or
                    self.nhrpclientregistrationrequestretries.yfilter != YFilter.not_set or
                    self.nhrpclientrequestid.yfilter != YFilter.not_set or
                    self.nhrpclientresolutionrequestretries.yfilter != YFilter.not_set or
                    self.nhrpclientrowstatus.yfilter != YFilter.not_set or
                    self.nhrpclientstoragetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nhrpClientEntry" + "[nhrpClientIndex='" + self.nhrpclientindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "NHRP-MIB:NHRP-MIB/nhrpClientTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.nhrpclientindex.is_set or self.nhrpclientindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientindex.get_name_leafdata())
                if (self.nhrpclientdefaultmtu.is_set or self.nhrpclientdefaultmtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientdefaultmtu.get_name_leafdata())
                if (self.nhrpclientholdtime.is_set or self.nhrpclientholdtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientholdtime.get_name_leafdata())
                if (self.nhrpclientinitialrequesttimeout.is_set or self.nhrpclientinitialrequesttimeout.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientinitialrequesttimeout.get_name_leafdata())
                if (self.nhrpclientinternetworkaddr.is_set or self.nhrpclientinternetworkaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientinternetworkaddr.get_name_leafdata())
                if (self.nhrpclientinternetworkaddrtype.is_set or self.nhrpclientinternetworkaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientinternetworkaddrtype.get_name_leafdata())
                if (self.nhrpclientnbmaaddr.is_set or self.nhrpclientnbmaaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientnbmaaddr.get_name_leafdata())
                if (self.nhrpclientnbmaaddrtype.is_set or self.nhrpclientnbmaaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientnbmaaddrtype.get_name_leafdata())
                if (self.nhrpclientnbmasubaddr.is_set or self.nhrpclientnbmasubaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientnbmasubaddr.get_name_leafdata())
                if (self.nhrpclientpurgerequestretries.is_set or self.nhrpclientpurgerequestretries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientpurgerequestretries.get_name_leafdata())
                if (self.nhrpclientregistrationrequestretries.is_set or self.nhrpclientregistrationrequestretries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientregistrationrequestretries.get_name_leafdata())
                if (self.nhrpclientrequestid.is_set or self.nhrpclientrequestid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientrequestid.get_name_leafdata())
                if (self.nhrpclientresolutionrequestretries.is_set or self.nhrpclientresolutionrequestretries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientresolutionrequestretries.get_name_leafdata())
                if (self.nhrpclientrowstatus.is_set or self.nhrpclientrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientrowstatus.get_name_leafdata())
                if (self.nhrpclientstoragetype.is_set or self.nhrpclientstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstoragetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "nhrpClientIndex" or name == "nhrpClientDefaultMtu" or name == "nhrpClientHoldTime" or name == "nhrpClientInitialRequestTimeout" or name == "nhrpClientInternetworkAddr" or name == "nhrpClientInternetworkAddrType" or name == "nhrpClientNbmaAddr" or name == "nhrpClientNbmaAddrType" or name == "nhrpClientNbmaSubaddr" or name == "nhrpClientPurgeRequestRetries" or name == "nhrpClientRegistrationRequestRetries" or name == "nhrpClientRequestID" or name == "nhrpClientResolutionRequestRetries" or name == "nhrpClientRowStatus" or name == "nhrpClientStorageType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "nhrpClientIndex"):
                    self.nhrpclientindex = value
                    self.nhrpclientindex.value_namespace = name_space
                    self.nhrpclientindex.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientDefaultMtu"):
                    self.nhrpclientdefaultmtu = value
                    self.nhrpclientdefaultmtu.value_namespace = name_space
                    self.nhrpclientdefaultmtu.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientHoldTime"):
                    self.nhrpclientholdtime = value
                    self.nhrpclientholdtime.value_namespace = name_space
                    self.nhrpclientholdtime.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientInitialRequestTimeout"):
                    self.nhrpclientinitialrequesttimeout = value
                    self.nhrpclientinitialrequesttimeout.value_namespace = name_space
                    self.nhrpclientinitialrequesttimeout.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientInternetworkAddr"):
                    self.nhrpclientinternetworkaddr = value
                    self.nhrpclientinternetworkaddr.value_namespace = name_space
                    self.nhrpclientinternetworkaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientInternetworkAddrType"):
                    self.nhrpclientinternetworkaddrtype = value
                    self.nhrpclientinternetworkaddrtype.value_namespace = name_space
                    self.nhrpclientinternetworkaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientNbmaAddr"):
                    self.nhrpclientnbmaaddr = value
                    self.nhrpclientnbmaaddr.value_namespace = name_space
                    self.nhrpclientnbmaaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientNbmaAddrType"):
                    self.nhrpclientnbmaaddrtype = value
                    self.nhrpclientnbmaaddrtype.value_namespace = name_space
                    self.nhrpclientnbmaaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientNbmaSubaddr"):
                    self.nhrpclientnbmasubaddr = value
                    self.nhrpclientnbmasubaddr.value_namespace = name_space
                    self.nhrpclientnbmasubaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientPurgeRequestRetries"):
                    self.nhrpclientpurgerequestretries = value
                    self.nhrpclientpurgerequestretries.value_namespace = name_space
                    self.nhrpclientpurgerequestretries.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientRegistrationRequestRetries"):
                    self.nhrpclientregistrationrequestretries = value
                    self.nhrpclientregistrationrequestretries.value_namespace = name_space
                    self.nhrpclientregistrationrequestretries.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientRequestID"):
                    self.nhrpclientrequestid = value
                    self.nhrpclientrequestid.value_namespace = name_space
                    self.nhrpclientrequestid.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientResolutionRequestRetries"):
                    self.nhrpclientresolutionrequestretries = value
                    self.nhrpclientresolutionrequestretries.value_namespace = name_space
                    self.nhrpclientresolutionrequestretries.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientRowStatus"):
                    self.nhrpclientrowstatus = value
                    self.nhrpclientrowstatus.value_namespace = name_space
                    self.nhrpclientrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStorageType"):
                    self.nhrpclientstoragetype = value
                    self.nhrpclientstoragetype.value_namespace = name_space
                    self.nhrpclientstoragetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.nhrpcliententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.nhrpcliententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nhrpClientTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "NHRP-MIB:NHRP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "nhrpClientEntry"):
                for c in self.nhrpcliententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NhrpMib.Nhrpclienttable.Nhrpcliententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.nhrpcliententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nhrpClientEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Nhrpclientregistrationtable(Entity):
        """
        A table of Registration Request Information that
        needs to be maintained by the NHCs (clients).
        
        .. attribute:: nhrpclientregistrationentry
        
        	An NHC needs to maintain registration request information between the NHC and the NHS.  An entry in this table represents information for a single registration request
        	**type**\: list of    :py:class:`Nhrpclientregistrationentry <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpclientregistrationtable.Nhrpclientregistrationentry>`
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NhrpMib.Nhrpclientregistrationtable, self).__init__()

            self.yang_name = "nhrpClientRegistrationTable"
            self.yang_parent_name = "NHRP-MIB"

            self.nhrpclientregistrationentry = YList(self)

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
                        super(NhrpMib.Nhrpclientregistrationtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NhrpMib.Nhrpclientregistrationtable, self).__setattr__(name, value)


        class Nhrpclientregistrationentry(Entity):
            """
            An NHC needs to maintain registration request information
            between the NHC and the NHS.  An entry in this table
            represents information for a single registration request.
            
            .. attribute:: nhrpclientindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`nhrpclientindex <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpclienttable.Nhrpcliententry>`
            
            .. attribute:: nhrpclientregindex  <key>
            
            	An identifier for this entry such that it identifies a specific Registration Request from the NHC represented by the nhrpClientIndex
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrpclientregrowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: nhrpclientregstate
            
            	The registration state of this client. The values are\: 'other(1)'             The state of the registration                        request is not one of                        'registering',                        'ackRegisterReply' or                        'nakRegisterReply'.  'registering(2)'        A registration request has                         been issued and a registration                         reply is expected.  'ackRegisterReply(3)'   A positive registration reply                         has been received.  'nakRegisterReply(4)'   The client has received a                         negative registration                         reply (NAK)
            	**type**\:   :py:class:`Nhrpclientregstate <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpclientregistrationtable.Nhrpclientregistrationentry.Nhrpclientregstate>`
            
            .. attribute:: nhrpclientreguniqueness
            
            	The Uniqueness indicator for this Registration Request. If this object has the value of requestUnique(1), then the Uniqueness bit is set in the the NHRP Registration Request represented by this row.  The value cannot be changed once the row is created
            	**type**\:   :py:class:`Nhrpclientreguniqueness <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpclientregistrationtable.Nhrpclientregistrationentry.Nhrpclientreguniqueness>`
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NhrpMib.Nhrpclientregistrationtable.Nhrpclientregistrationentry, self).__init__()

                self.yang_name = "nhrpClientRegistrationEntry"
                self.yang_parent_name = "nhrpClientRegistrationTable"

                self.nhrpclientindex = YLeaf(YType.str, "nhrpClientIndex")

                self.nhrpclientregindex = YLeaf(YType.uint32, "nhrpClientRegIndex")

                self.nhrpclientregrowstatus = YLeaf(YType.enumeration, "nhrpClientRegRowStatus")

                self.nhrpclientregstate = YLeaf(YType.enumeration, "nhrpClientRegState")

                self.nhrpclientreguniqueness = YLeaf(YType.enumeration, "nhrpClientRegUniqueness")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("nhrpclientindex",
                                "nhrpclientregindex",
                                "nhrpclientregrowstatus",
                                "nhrpclientregstate",
                                "nhrpclientreguniqueness") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NhrpMib.Nhrpclientregistrationtable.Nhrpclientregistrationentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NhrpMib.Nhrpclientregistrationtable.Nhrpclientregistrationentry, self).__setattr__(name, value)

            class Nhrpclientregstate(Enum):
                """
                Nhrpclientregstate

                The registration state of this client. The values are\:

                'other(1)'             The state of the registration

                                       request is not one of

                                       'registering',

                                       'ackRegisterReply' or

                                       'nakRegisterReply'.

                'registering(2)'        A registration request has

                                        been issued and a registration

                                        reply is expected.

                'ackRegisterReply(3)'   A positive registration reply

                                        has been received.

                'nakRegisterReply(4)'   The client has received a

                                        negative registration

                                        reply (NAK).

                .. data:: other = 1

                .. data:: registering = 2

                .. data:: ackRegisterReply = 3

                .. data:: nakRegisterReply = 4

                """

                other = Enum.YLeaf(1, "other")

                registering = Enum.YLeaf(2, "registering")

                ackRegisterReply = Enum.YLeaf(3, "ackRegisterReply")

                nakRegisterReply = Enum.YLeaf(4, "nakRegisterReply")


            class Nhrpclientreguniqueness(Enum):
                """
                Nhrpclientreguniqueness

                The Uniqueness indicator for this Registration Request.

                If this object has the value of requestUnique(1), then

                the Uniqueness bit is set in the the NHRP Registration

                Request represented by this row.  The value cannot

                be changed once the row is created.

                .. data:: requestUnique = 1

                .. data:: requestNotUnique = 2

                """

                requestUnique = Enum.YLeaf(1, "requestUnique")

                requestNotUnique = Enum.YLeaf(2, "requestNotUnique")


            def has_data(self):
                return (
                    self.nhrpclientindex.is_set or
                    self.nhrpclientregindex.is_set or
                    self.nhrpclientregrowstatus.is_set or
                    self.nhrpclientregstate.is_set or
                    self.nhrpclientreguniqueness.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.nhrpclientindex.yfilter != YFilter.not_set or
                    self.nhrpclientregindex.yfilter != YFilter.not_set or
                    self.nhrpclientregrowstatus.yfilter != YFilter.not_set or
                    self.nhrpclientregstate.yfilter != YFilter.not_set or
                    self.nhrpclientreguniqueness.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nhrpClientRegistrationEntry" + "[nhrpClientIndex='" + self.nhrpclientindex.get() + "']" + "[nhrpClientRegIndex='" + self.nhrpclientregindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "NHRP-MIB:NHRP-MIB/nhrpClientRegistrationTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.nhrpclientindex.is_set or self.nhrpclientindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientindex.get_name_leafdata())
                if (self.nhrpclientregindex.is_set or self.nhrpclientregindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientregindex.get_name_leafdata())
                if (self.nhrpclientregrowstatus.is_set or self.nhrpclientregrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientregrowstatus.get_name_leafdata())
                if (self.nhrpclientregstate.is_set or self.nhrpclientregstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientregstate.get_name_leafdata())
                if (self.nhrpclientreguniqueness.is_set or self.nhrpclientreguniqueness.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientreguniqueness.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "nhrpClientIndex" or name == "nhrpClientRegIndex" or name == "nhrpClientRegRowStatus" or name == "nhrpClientRegState" or name == "nhrpClientRegUniqueness"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "nhrpClientIndex"):
                    self.nhrpclientindex = value
                    self.nhrpclientindex.value_namespace = name_space
                    self.nhrpclientindex.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientRegIndex"):
                    self.nhrpclientregindex = value
                    self.nhrpclientregindex.value_namespace = name_space
                    self.nhrpclientregindex.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientRegRowStatus"):
                    self.nhrpclientregrowstatus = value
                    self.nhrpclientregrowstatus.value_namespace = name_space
                    self.nhrpclientregrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientRegState"):
                    self.nhrpclientregstate = value
                    self.nhrpclientregstate.value_namespace = name_space
                    self.nhrpclientregstate.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientRegUniqueness"):
                    self.nhrpclientreguniqueness = value
                    self.nhrpclientreguniqueness.value_namespace = name_space
                    self.nhrpclientreguniqueness.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.nhrpclientregistrationentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.nhrpclientregistrationentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nhrpClientRegistrationTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "NHRP-MIB:NHRP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "nhrpClientRegistrationEntry"):
                for c in self.nhrpclientregistrationentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NhrpMib.Nhrpclientregistrationtable.Nhrpclientregistrationentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.nhrpclientregistrationentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nhrpClientRegistrationEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Nhrpclientnhstable(Entity):
        """
        A table of NHSes that are available for use by this NHC
        (client). By default, the agent will add an entry to this
        table that corresponds to the client's default router.
        
        .. attribute:: nhrpclientnhsentry
        
        	An NHS that may be used by an NHC
        	**type**\: list of    :py:class:`Nhrpclientnhsentry <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpclientnhstable.Nhrpclientnhsentry>`
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NhrpMib.Nhrpclientnhstable, self).__init__()

            self.yang_name = "nhrpClientNhsTable"
            self.yang_parent_name = "NHRP-MIB"

            self.nhrpclientnhsentry = YList(self)

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
                        super(NhrpMib.Nhrpclientnhstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NhrpMib.Nhrpclientnhstable, self).__setattr__(name, value)


        class Nhrpclientnhsentry(Entity):
            """
            An NHS that may be used by an NHC.
            
            .. attribute:: nhrpclientindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`nhrpclientindex <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpclienttable.Nhrpcliententry>`
            
            .. attribute:: nhrpclientnhsindex  <key>
            
            	An identifier for an NHS available to an NHC
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrpclientnhsinternetworkaddr
            
            	The value of the destination internetwork layer address of the NHRP server represented by this    entry.  If this value is not known, this will be a zero\-length OCTET STRING
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: nhrpclientnhsinternetworkaddrtype
            
            	The type of the internetwork layer address of the NHRP server represented in this entry. This object indicates how the value of nhrpClientNhsInternetworkAddr is to be interpreted
            	**type**\:   :py:class:`Addressfamilynumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.Addressfamilynumbers>`
            
            .. attribute:: nhrpclientnhsinuse
            
            	An indication of whether this NHS is in use by the NHC
            	**type**\:  bool
            
            .. attribute:: nhrpclientnhsnbmaaddr
            
            	The NBMA subnetwork address of the NHS. The type of the address is indicated by the corresponding value of nhrpClientNhsNbmaAddrType
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: nhrpclientnhsnbmaaddrtype
            
            	The type of the NBMA subnetwork address of the NHRP Server represented by this entry. This object indicates how the values of nhrpClientNhsNbmaAddr and nhrpClientNhsNbmaSubaddr are to be interpreted
            	**type**\:   :py:class:`Addressfamilynumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.Addressfamilynumbers>`
            
            .. attribute:: nhrpclientnhsnbmasubaddr
            
            	The NBMA subaddress of the NHS. For NMBA address families that do not have the concept of subaddress,      this will be a zero\-length OCTET STRING
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: nhrpclientnhsrowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NhrpMib.Nhrpclientnhstable.Nhrpclientnhsentry, self).__init__()

                self.yang_name = "nhrpClientNhsEntry"
                self.yang_parent_name = "nhrpClientNhsTable"

                self.nhrpclientindex = YLeaf(YType.str, "nhrpClientIndex")

                self.nhrpclientnhsindex = YLeaf(YType.uint32, "nhrpClientNhsIndex")

                self.nhrpclientnhsinternetworkaddr = YLeaf(YType.str, "nhrpClientNhsInternetworkAddr")

                self.nhrpclientnhsinternetworkaddrtype = YLeaf(YType.enumeration, "nhrpClientNhsInternetworkAddrType")

                self.nhrpclientnhsinuse = YLeaf(YType.boolean, "nhrpClientNhsInUse")

                self.nhrpclientnhsnbmaaddr = YLeaf(YType.str, "nhrpClientNhsNbmaAddr")

                self.nhrpclientnhsnbmaaddrtype = YLeaf(YType.enumeration, "nhrpClientNhsNbmaAddrType")

                self.nhrpclientnhsnbmasubaddr = YLeaf(YType.str, "nhrpClientNhsNbmaSubaddr")

                self.nhrpclientnhsrowstatus = YLeaf(YType.enumeration, "nhrpClientNhsRowStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("nhrpclientindex",
                                "nhrpclientnhsindex",
                                "nhrpclientnhsinternetworkaddr",
                                "nhrpclientnhsinternetworkaddrtype",
                                "nhrpclientnhsinuse",
                                "nhrpclientnhsnbmaaddr",
                                "nhrpclientnhsnbmaaddrtype",
                                "nhrpclientnhsnbmasubaddr",
                                "nhrpclientnhsrowstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NhrpMib.Nhrpclientnhstable.Nhrpclientnhsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NhrpMib.Nhrpclientnhstable.Nhrpclientnhsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.nhrpclientindex.is_set or
                    self.nhrpclientnhsindex.is_set or
                    self.nhrpclientnhsinternetworkaddr.is_set or
                    self.nhrpclientnhsinternetworkaddrtype.is_set or
                    self.nhrpclientnhsinuse.is_set or
                    self.nhrpclientnhsnbmaaddr.is_set or
                    self.nhrpclientnhsnbmaaddrtype.is_set or
                    self.nhrpclientnhsnbmasubaddr.is_set or
                    self.nhrpclientnhsrowstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.nhrpclientindex.yfilter != YFilter.not_set or
                    self.nhrpclientnhsindex.yfilter != YFilter.not_set or
                    self.nhrpclientnhsinternetworkaddr.yfilter != YFilter.not_set or
                    self.nhrpclientnhsinternetworkaddrtype.yfilter != YFilter.not_set or
                    self.nhrpclientnhsinuse.yfilter != YFilter.not_set or
                    self.nhrpclientnhsnbmaaddr.yfilter != YFilter.not_set or
                    self.nhrpclientnhsnbmaaddrtype.yfilter != YFilter.not_set or
                    self.nhrpclientnhsnbmasubaddr.yfilter != YFilter.not_set or
                    self.nhrpclientnhsrowstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nhrpClientNhsEntry" + "[nhrpClientIndex='" + self.nhrpclientindex.get() + "']" + "[nhrpClientNhsIndex='" + self.nhrpclientnhsindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "NHRP-MIB:NHRP-MIB/nhrpClientNhsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.nhrpclientindex.is_set or self.nhrpclientindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientindex.get_name_leafdata())
                if (self.nhrpclientnhsindex.is_set or self.nhrpclientnhsindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientnhsindex.get_name_leafdata())
                if (self.nhrpclientnhsinternetworkaddr.is_set or self.nhrpclientnhsinternetworkaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientnhsinternetworkaddr.get_name_leafdata())
                if (self.nhrpclientnhsinternetworkaddrtype.is_set or self.nhrpclientnhsinternetworkaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientnhsinternetworkaddrtype.get_name_leafdata())
                if (self.nhrpclientnhsinuse.is_set or self.nhrpclientnhsinuse.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientnhsinuse.get_name_leafdata())
                if (self.nhrpclientnhsnbmaaddr.is_set or self.nhrpclientnhsnbmaaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientnhsnbmaaddr.get_name_leafdata())
                if (self.nhrpclientnhsnbmaaddrtype.is_set or self.nhrpclientnhsnbmaaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientnhsnbmaaddrtype.get_name_leafdata())
                if (self.nhrpclientnhsnbmasubaddr.is_set or self.nhrpclientnhsnbmasubaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientnhsnbmasubaddr.get_name_leafdata())
                if (self.nhrpclientnhsrowstatus.is_set or self.nhrpclientnhsrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientnhsrowstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "nhrpClientIndex" or name == "nhrpClientNhsIndex" or name == "nhrpClientNhsInternetworkAddr" or name == "nhrpClientNhsInternetworkAddrType" or name == "nhrpClientNhsInUse" or name == "nhrpClientNhsNbmaAddr" or name == "nhrpClientNhsNbmaAddrType" or name == "nhrpClientNhsNbmaSubaddr" or name == "nhrpClientNhsRowStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "nhrpClientIndex"):
                    self.nhrpclientindex = value
                    self.nhrpclientindex.value_namespace = name_space
                    self.nhrpclientindex.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientNhsIndex"):
                    self.nhrpclientnhsindex = value
                    self.nhrpclientnhsindex.value_namespace = name_space
                    self.nhrpclientnhsindex.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientNhsInternetworkAddr"):
                    self.nhrpclientnhsinternetworkaddr = value
                    self.nhrpclientnhsinternetworkaddr.value_namespace = name_space
                    self.nhrpclientnhsinternetworkaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientNhsInternetworkAddrType"):
                    self.nhrpclientnhsinternetworkaddrtype = value
                    self.nhrpclientnhsinternetworkaddrtype.value_namespace = name_space
                    self.nhrpclientnhsinternetworkaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientNhsInUse"):
                    self.nhrpclientnhsinuse = value
                    self.nhrpclientnhsinuse.value_namespace = name_space
                    self.nhrpclientnhsinuse.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientNhsNbmaAddr"):
                    self.nhrpclientnhsnbmaaddr = value
                    self.nhrpclientnhsnbmaaddr.value_namespace = name_space
                    self.nhrpclientnhsnbmaaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientNhsNbmaAddrType"):
                    self.nhrpclientnhsnbmaaddrtype = value
                    self.nhrpclientnhsnbmaaddrtype.value_namespace = name_space
                    self.nhrpclientnhsnbmaaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientNhsNbmaSubaddr"):
                    self.nhrpclientnhsnbmasubaddr = value
                    self.nhrpclientnhsnbmasubaddr.value_namespace = name_space
                    self.nhrpclientnhsnbmasubaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientNhsRowStatus"):
                    self.nhrpclientnhsrowstatus = value
                    self.nhrpclientnhsrowstatus.value_namespace = name_space
                    self.nhrpclientnhsrowstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.nhrpclientnhsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.nhrpclientnhsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nhrpClientNhsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "NHRP-MIB:NHRP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "nhrpClientNhsEntry"):
                for c in self.nhrpclientnhsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NhrpMib.Nhrpclientnhstable.Nhrpclientnhsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.nhrpclientnhsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nhrpClientNhsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Nhrpclientstattable(Entity):
        """
        This table contains statistics collected by NHRP
        clients.
        
        .. attribute:: nhrpclientstatentry
        
        	Statistics collected by a NHRP client
        	**type**\: list of    :py:class:`Nhrpclientstatentry <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpclientstattable.Nhrpclientstatentry>`
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NhrpMib.Nhrpclientstattable, self).__init__()

            self.yang_name = "nhrpClientStatTable"
            self.yang_parent_name = "NHRP-MIB"

            self.nhrpclientstatentry = YList(self)

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
                        super(NhrpMib.Nhrpclientstattable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NhrpMib.Nhrpclientstattable, self).__setattr__(name, value)


        class Nhrpclientstatentry(Entity):
            """
            Statistics collected by a NHRP client.
            
            .. attribute:: nhrpclientindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`nhrpclientindex <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpclienttable.Nhrpcliententry>`
            
            .. attribute:: nhrpclientstatdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this Client's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem or the NHRP Client re\-initialization associated with this entry, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxerrauthenticationfailure
            
            	The number of NHRP Error Indication packets received by this client with the error code 'Authentication Failure'.      Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxerrhopcountexceeded
            
            	The number of NHRP Error Indication packets received by this client with the error code 'Hop Count Exceeded'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxerrinvalidextension
            
            	The number of NHRP Error Indication packets received by this client with the error code 'Invalid Extension'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxerrloopdetected
            
            	The number of NHRP Error Indication packets received by this client with the error code 'NHRP Loop Detected'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxerrprotoaddrunreachable
            
            	The number of NHRP Error Indication packets received by this client with the error code 'Protocol Address Unreachable'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxerrprotoerror
            
            	The number of NHRP Error Indication packets received by this client with the error code 'Protocol Error'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxerrsdusizeexceeded
            
            	The number of NHRP Error Indication packets received by this client with the error code 'NHRP SDU Size  Exceeded'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxerrunrecognizedextension
            
            	The number of NHRP Error Indication packets received by this client with the error code 'Unrecognized Extension'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxpurgereply
            
            	The number of NHRP Purge Replies received by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxpurgereq
            
            	The number of NHRP Purge Requests received by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxregisterack
            
            	The number of positively acknowledged NHRP Registration Replies received by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxregisternakalreadyreg
            
            	The number of NAKed NHRP Registration Replies received by this client that contained the code indicating 'Unique Internetworking Layer Address Already Registered'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxregisternakinsufresources
            
            	The number of NAKed NHRP Registration Replies received by this client that contained the code indicating 'Insufficient Resources'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxregisternakprohibited
            
            	The number of NAKed NHRP Registration Replies received by this client that contained the code indicating 'Administratively Prohibited'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxresolvereplyack
            
            	The number of positively acknowledged NHRP Resolution Replies received by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxresolvereplynakinsufresources
            
            	The number of NAKed NHRP Resolution Replies received by this client that contained the code indicating 'Insufficient Resources'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxresolvereplynaknobinding
            
            	The number of NAKed NHRP Resolution Replies received by this client that contained the code indicating 'No Internetworking Layer Address to NBMA Address Binding Exists'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxresolvereplynaknotunique
            
            	The number of NAKed NHRP Resolution Replies received by this client that contained the code indicating 'Binding Exists But Is Not Unique'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxresolvereplynakprohibited
            
            	The number of NAKed NHRP Resolution Replies received by this client that contained the code indicating 'Administratively Prohibited'.   Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstattxerrorindication
            
            	The number of NHRP Error Indication packets transmitted by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstattxpurgereply
            
            	The number of NHRP Purge Replies transmitted by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstattxpurgereq
            
            	The number of NHRP Purge Requests transmitted by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstattxregisterreq
            
            	The number of NHRP Registration Requests transmitted by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstattxresolvereq
            
            	The number of NHRP Resolution Requests transmitted by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NhrpMib.Nhrpclientstattable.Nhrpclientstatentry, self).__init__()

                self.yang_name = "nhrpClientStatEntry"
                self.yang_parent_name = "nhrpClientStatTable"

                self.nhrpclientindex = YLeaf(YType.str, "nhrpClientIndex")

                self.nhrpclientstatdiscontinuitytime = YLeaf(YType.uint32, "nhrpClientStatDiscontinuityTime")

                self.nhrpclientstatrxerrauthenticationfailure = YLeaf(YType.uint32, "nhrpClientStatRxErrAuthenticationFailure")

                self.nhrpclientstatrxerrhopcountexceeded = YLeaf(YType.uint32, "nhrpClientStatRxErrHopCountExceeded")

                self.nhrpclientstatrxerrinvalidextension = YLeaf(YType.uint32, "nhrpClientStatRxErrInvalidExtension")

                self.nhrpclientstatrxerrloopdetected = YLeaf(YType.uint32, "nhrpClientStatRxErrLoopDetected")

                self.nhrpclientstatrxerrprotoaddrunreachable = YLeaf(YType.uint32, "nhrpClientStatRxErrProtoAddrUnreachable")

                self.nhrpclientstatrxerrprotoerror = YLeaf(YType.uint32, "nhrpClientStatRxErrProtoError")

                self.nhrpclientstatrxerrsdusizeexceeded = YLeaf(YType.uint32, "nhrpClientStatRxErrSduSizeExceeded")

                self.nhrpclientstatrxerrunrecognizedextension = YLeaf(YType.uint32, "nhrpClientStatRxErrUnrecognizedExtension")

                self.nhrpclientstatrxpurgereply = YLeaf(YType.uint32, "nhrpClientStatRxPurgeReply")

                self.nhrpclientstatrxpurgereq = YLeaf(YType.uint32, "nhrpClientStatRxPurgeReq")

                self.nhrpclientstatrxregisterack = YLeaf(YType.uint32, "nhrpClientStatRxRegisterAck")

                self.nhrpclientstatrxregisternakalreadyreg = YLeaf(YType.uint32, "nhrpClientStatRxRegisterNakAlreadyReg")

                self.nhrpclientstatrxregisternakinsufresources = YLeaf(YType.uint32, "nhrpClientStatRxRegisterNakInsufResources")

                self.nhrpclientstatrxregisternakprohibited = YLeaf(YType.uint32, "nhrpClientStatRxRegisterNakProhibited")

                self.nhrpclientstatrxresolvereplyack = YLeaf(YType.uint32, "nhrpClientStatRxResolveReplyAck")

                self.nhrpclientstatrxresolvereplynakinsufresources = YLeaf(YType.uint32, "nhrpClientStatRxResolveReplyNakInsufResources")

                self.nhrpclientstatrxresolvereplynaknobinding = YLeaf(YType.uint32, "nhrpClientStatRxResolveReplyNakNoBinding")

                self.nhrpclientstatrxresolvereplynaknotunique = YLeaf(YType.uint32, "nhrpClientStatRxResolveReplyNakNotUnique")

                self.nhrpclientstatrxresolvereplynakprohibited = YLeaf(YType.uint32, "nhrpClientStatRxResolveReplyNakProhibited")

                self.nhrpclientstattxerrorindication = YLeaf(YType.uint32, "nhrpClientStatTxErrorIndication")

                self.nhrpclientstattxpurgereply = YLeaf(YType.uint32, "nhrpClientStatTxPurgeReply")

                self.nhrpclientstattxpurgereq = YLeaf(YType.uint32, "nhrpClientStatTxPurgeReq")

                self.nhrpclientstattxregisterreq = YLeaf(YType.uint32, "nhrpClientStatTxRegisterReq")

                self.nhrpclientstattxresolvereq = YLeaf(YType.uint32, "nhrpClientStatTxResolveReq")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("nhrpclientindex",
                                "nhrpclientstatdiscontinuitytime",
                                "nhrpclientstatrxerrauthenticationfailure",
                                "nhrpclientstatrxerrhopcountexceeded",
                                "nhrpclientstatrxerrinvalidextension",
                                "nhrpclientstatrxerrloopdetected",
                                "nhrpclientstatrxerrprotoaddrunreachable",
                                "nhrpclientstatrxerrprotoerror",
                                "nhrpclientstatrxerrsdusizeexceeded",
                                "nhrpclientstatrxerrunrecognizedextension",
                                "nhrpclientstatrxpurgereply",
                                "nhrpclientstatrxpurgereq",
                                "nhrpclientstatrxregisterack",
                                "nhrpclientstatrxregisternakalreadyreg",
                                "nhrpclientstatrxregisternakinsufresources",
                                "nhrpclientstatrxregisternakprohibited",
                                "nhrpclientstatrxresolvereplyack",
                                "nhrpclientstatrxresolvereplynakinsufresources",
                                "nhrpclientstatrxresolvereplynaknobinding",
                                "nhrpclientstatrxresolvereplynaknotunique",
                                "nhrpclientstatrxresolvereplynakprohibited",
                                "nhrpclientstattxerrorindication",
                                "nhrpclientstattxpurgereply",
                                "nhrpclientstattxpurgereq",
                                "nhrpclientstattxregisterreq",
                                "nhrpclientstattxresolvereq") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NhrpMib.Nhrpclientstattable.Nhrpclientstatentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NhrpMib.Nhrpclientstattable.Nhrpclientstatentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.nhrpclientindex.is_set or
                    self.nhrpclientstatdiscontinuitytime.is_set or
                    self.nhrpclientstatrxerrauthenticationfailure.is_set or
                    self.nhrpclientstatrxerrhopcountexceeded.is_set or
                    self.nhrpclientstatrxerrinvalidextension.is_set or
                    self.nhrpclientstatrxerrloopdetected.is_set or
                    self.nhrpclientstatrxerrprotoaddrunreachable.is_set or
                    self.nhrpclientstatrxerrprotoerror.is_set or
                    self.nhrpclientstatrxerrsdusizeexceeded.is_set or
                    self.nhrpclientstatrxerrunrecognizedextension.is_set or
                    self.nhrpclientstatrxpurgereply.is_set or
                    self.nhrpclientstatrxpurgereq.is_set or
                    self.nhrpclientstatrxregisterack.is_set or
                    self.nhrpclientstatrxregisternakalreadyreg.is_set or
                    self.nhrpclientstatrxregisternakinsufresources.is_set or
                    self.nhrpclientstatrxregisternakprohibited.is_set or
                    self.nhrpclientstatrxresolvereplyack.is_set or
                    self.nhrpclientstatrxresolvereplynakinsufresources.is_set or
                    self.nhrpclientstatrxresolvereplynaknobinding.is_set or
                    self.nhrpclientstatrxresolvereplynaknotunique.is_set or
                    self.nhrpclientstatrxresolvereplynakprohibited.is_set or
                    self.nhrpclientstattxerrorindication.is_set or
                    self.nhrpclientstattxpurgereply.is_set or
                    self.nhrpclientstattxpurgereq.is_set or
                    self.nhrpclientstattxregisterreq.is_set or
                    self.nhrpclientstattxresolvereq.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.nhrpclientindex.yfilter != YFilter.not_set or
                    self.nhrpclientstatdiscontinuitytime.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxerrauthenticationfailure.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxerrhopcountexceeded.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxerrinvalidextension.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxerrloopdetected.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxerrprotoaddrunreachable.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxerrprotoerror.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxerrsdusizeexceeded.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxerrunrecognizedextension.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxpurgereply.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxpurgereq.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxregisterack.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxregisternakalreadyreg.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxregisternakinsufresources.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxregisternakprohibited.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxresolvereplyack.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxresolvereplynakinsufresources.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxresolvereplynaknobinding.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxresolvereplynaknotunique.yfilter != YFilter.not_set or
                    self.nhrpclientstatrxresolvereplynakprohibited.yfilter != YFilter.not_set or
                    self.nhrpclientstattxerrorindication.yfilter != YFilter.not_set or
                    self.nhrpclientstattxpurgereply.yfilter != YFilter.not_set or
                    self.nhrpclientstattxpurgereq.yfilter != YFilter.not_set or
                    self.nhrpclientstattxregisterreq.yfilter != YFilter.not_set or
                    self.nhrpclientstattxresolvereq.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nhrpClientStatEntry" + "[nhrpClientIndex='" + self.nhrpclientindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "NHRP-MIB:NHRP-MIB/nhrpClientStatTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.nhrpclientindex.is_set or self.nhrpclientindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientindex.get_name_leafdata())
                if (self.nhrpclientstatdiscontinuitytime.is_set or self.nhrpclientstatdiscontinuitytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatdiscontinuitytime.get_name_leafdata())
                if (self.nhrpclientstatrxerrauthenticationfailure.is_set or self.nhrpclientstatrxerrauthenticationfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxerrauthenticationfailure.get_name_leafdata())
                if (self.nhrpclientstatrxerrhopcountexceeded.is_set or self.nhrpclientstatrxerrhopcountexceeded.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxerrhopcountexceeded.get_name_leafdata())
                if (self.nhrpclientstatrxerrinvalidextension.is_set or self.nhrpclientstatrxerrinvalidextension.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxerrinvalidextension.get_name_leafdata())
                if (self.nhrpclientstatrxerrloopdetected.is_set or self.nhrpclientstatrxerrloopdetected.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxerrloopdetected.get_name_leafdata())
                if (self.nhrpclientstatrxerrprotoaddrunreachable.is_set or self.nhrpclientstatrxerrprotoaddrunreachable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxerrprotoaddrunreachable.get_name_leafdata())
                if (self.nhrpclientstatrxerrprotoerror.is_set or self.nhrpclientstatrxerrprotoerror.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxerrprotoerror.get_name_leafdata())
                if (self.nhrpclientstatrxerrsdusizeexceeded.is_set or self.nhrpclientstatrxerrsdusizeexceeded.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxerrsdusizeexceeded.get_name_leafdata())
                if (self.nhrpclientstatrxerrunrecognizedextension.is_set or self.nhrpclientstatrxerrunrecognizedextension.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxerrunrecognizedextension.get_name_leafdata())
                if (self.nhrpclientstatrxpurgereply.is_set or self.nhrpclientstatrxpurgereply.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxpurgereply.get_name_leafdata())
                if (self.nhrpclientstatrxpurgereq.is_set or self.nhrpclientstatrxpurgereq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxpurgereq.get_name_leafdata())
                if (self.nhrpclientstatrxregisterack.is_set or self.nhrpclientstatrxregisterack.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxregisterack.get_name_leafdata())
                if (self.nhrpclientstatrxregisternakalreadyreg.is_set or self.nhrpclientstatrxregisternakalreadyreg.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxregisternakalreadyreg.get_name_leafdata())
                if (self.nhrpclientstatrxregisternakinsufresources.is_set or self.nhrpclientstatrxregisternakinsufresources.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxregisternakinsufresources.get_name_leafdata())
                if (self.nhrpclientstatrxregisternakprohibited.is_set or self.nhrpclientstatrxregisternakprohibited.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxregisternakprohibited.get_name_leafdata())
                if (self.nhrpclientstatrxresolvereplyack.is_set or self.nhrpclientstatrxresolvereplyack.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxresolvereplyack.get_name_leafdata())
                if (self.nhrpclientstatrxresolvereplynakinsufresources.is_set or self.nhrpclientstatrxresolvereplynakinsufresources.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxresolvereplynakinsufresources.get_name_leafdata())
                if (self.nhrpclientstatrxresolvereplynaknobinding.is_set or self.nhrpclientstatrxresolvereplynaknobinding.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxresolvereplynaknobinding.get_name_leafdata())
                if (self.nhrpclientstatrxresolvereplynaknotunique.is_set or self.nhrpclientstatrxresolvereplynaknotunique.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxresolvereplynaknotunique.get_name_leafdata())
                if (self.nhrpclientstatrxresolvereplynakprohibited.is_set or self.nhrpclientstatrxresolvereplynakprohibited.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstatrxresolvereplynakprohibited.get_name_leafdata())
                if (self.nhrpclientstattxerrorindication.is_set or self.nhrpclientstattxerrorindication.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstattxerrorindication.get_name_leafdata())
                if (self.nhrpclientstattxpurgereply.is_set or self.nhrpclientstattxpurgereply.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstattxpurgereply.get_name_leafdata())
                if (self.nhrpclientstattxpurgereq.is_set or self.nhrpclientstattxpurgereq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstattxpurgereq.get_name_leafdata())
                if (self.nhrpclientstattxregisterreq.is_set or self.nhrpclientstattxregisterreq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstattxregisterreq.get_name_leafdata())
                if (self.nhrpclientstattxresolvereq.is_set or self.nhrpclientstattxresolvereq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpclientstattxresolvereq.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "nhrpClientIndex" or name == "nhrpClientStatDiscontinuityTime" or name == "nhrpClientStatRxErrAuthenticationFailure" or name == "nhrpClientStatRxErrHopCountExceeded" or name == "nhrpClientStatRxErrInvalidExtension" or name == "nhrpClientStatRxErrLoopDetected" or name == "nhrpClientStatRxErrProtoAddrUnreachable" or name == "nhrpClientStatRxErrProtoError" or name == "nhrpClientStatRxErrSduSizeExceeded" or name == "nhrpClientStatRxErrUnrecognizedExtension" or name == "nhrpClientStatRxPurgeReply" or name == "nhrpClientStatRxPurgeReq" or name == "nhrpClientStatRxRegisterAck" or name == "nhrpClientStatRxRegisterNakAlreadyReg" or name == "nhrpClientStatRxRegisterNakInsufResources" or name == "nhrpClientStatRxRegisterNakProhibited" or name == "nhrpClientStatRxResolveReplyAck" or name == "nhrpClientStatRxResolveReplyNakInsufResources" or name == "nhrpClientStatRxResolveReplyNakNoBinding" or name == "nhrpClientStatRxResolveReplyNakNotUnique" or name == "nhrpClientStatRxResolveReplyNakProhibited" or name == "nhrpClientStatTxErrorIndication" or name == "nhrpClientStatTxPurgeReply" or name == "nhrpClientStatTxPurgeReq" or name == "nhrpClientStatTxRegisterReq" or name == "nhrpClientStatTxResolveReq"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "nhrpClientIndex"):
                    self.nhrpclientindex = value
                    self.nhrpclientindex.value_namespace = name_space
                    self.nhrpclientindex.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatDiscontinuityTime"):
                    self.nhrpclientstatdiscontinuitytime = value
                    self.nhrpclientstatdiscontinuitytime.value_namespace = name_space
                    self.nhrpclientstatdiscontinuitytime.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxErrAuthenticationFailure"):
                    self.nhrpclientstatrxerrauthenticationfailure = value
                    self.nhrpclientstatrxerrauthenticationfailure.value_namespace = name_space
                    self.nhrpclientstatrxerrauthenticationfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxErrHopCountExceeded"):
                    self.nhrpclientstatrxerrhopcountexceeded = value
                    self.nhrpclientstatrxerrhopcountexceeded.value_namespace = name_space
                    self.nhrpclientstatrxerrhopcountexceeded.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxErrInvalidExtension"):
                    self.nhrpclientstatrxerrinvalidextension = value
                    self.nhrpclientstatrxerrinvalidextension.value_namespace = name_space
                    self.nhrpclientstatrxerrinvalidextension.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxErrLoopDetected"):
                    self.nhrpclientstatrxerrloopdetected = value
                    self.nhrpclientstatrxerrloopdetected.value_namespace = name_space
                    self.nhrpclientstatrxerrloopdetected.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxErrProtoAddrUnreachable"):
                    self.nhrpclientstatrxerrprotoaddrunreachable = value
                    self.nhrpclientstatrxerrprotoaddrunreachable.value_namespace = name_space
                    self.nhrpclientstatrxerrprotoaddrunreachable.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxErrProtoError"):
                    self.nhrpclientstatrxerrprotoerror = value
                    self.nhrpclientstatrxerrprotoerror.value_namespace = name_space
                    self.nhrpclientstatrxerrprotoerror.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxErrSduSizeExceeded"):
                    self.nhrpclientstatrxerrsdusizeexceeded = value
                    self.nhrpclientstatrxerrsdusizeexceeded.value_namespace = name_space
                    self.nhrpclientstatrxerrsdusizeexceeded.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxErrUnrecognizedExtension"):
                    self.nhrpclientstatrxerrunrecognizedextension = value
                    self.nhrpclientstatrxerrunrecognizedextension.value_namespace = name_space
                    self.nhrpclientstatrxerrunrecognizedextension.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxPurgeReply"):
                    self.nhrpclientstatrxpurgereply = value
                    self.nhrpclientstatrxpurgereply.value_namespace = name_space
                    self.nhrpclientstatrxpurgereply.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxPurgeReq"):
                    self.nhrpclientstatrxpurgereq = value
                    self.nhrpclientstatrxpurgereq.value_namespace = name_space
                    self.nhrpclientstatrxpurgereq.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxRegisterAck"):
                    self.nhrpclientstatrxregisterack = value
                    self.nhrpclientstatrxregisterack.value_namespace = name_space
                    self.nhrpclientstatrxregisterack.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxRegisterNakAlreadyReg"):
                    self.nhrpclientstatrxregisternakalreadyreg = value
                    self.nhrpclientstatrxregisternakalreadyreg.value_namespace = name_space
                    self.nhrpclientstatrxregisternakalreadyreg.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxRegisterNakInsufResources"):
                    self.nhrpclientstatrxregisternakinsufresources = value
                    self.nhrpclientstatrxregisternakinsufresources.value_namespace = name_space
                    self.nhrpclientstatrxregisternakinsufresources.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxRegisterNakProhibited"):
                    self.nhrpclientstatrxregisternakprohibited = value
                    self.nhrpclientstatrxregisternakprohibited.value_namespace = name_space
                    self.nhrpclientstatrxregisternakprohibited.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxResolveReplyAck"):
                    self.nhrpclientstatrxresolvereplyack = value
                    self.nhrpclientstatrxresolvereplyack.value_namespace = name_space
                    self.nhrpclientstatrxresolvereplyack.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxResolveReplyNakInsufResources"):
                    self.nhrpclientstatrxresolvereplynakinsufresources = value
                    self.nhrpclientstatrxresolvereplynakinsufresources.value_namespace = name_space
                    self.nhrpclientstatrxresolvereplynakinsufresources.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxResolveReplyNakNoBinding"):
                    self.nhrpclientstatrxresolvereplynaknobinding = value
                    self.nhrpclientstatrxresolvereplynaknobinding.value_namespace = name_space
                    self.nhrpclientstatrxresolvereplynaknobinding.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxResolveReplyNakNotUnique"):
                    self.nhrpclientstatrxresolvereplynaknotunique = value
                    self.nhrpclientstatrxresolvereplynaknotunique.value_namespace = name_space
                    self.nhrpclientstatrxresolvereplynaknotunique.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatRxResolveReplyNakProhibited"):
                    self.nhrpclientstatrxresolvereplynakprohibited = value
                    self.nhrpclientstatrxresolvereplynakprohibited.value_namespace = name_space
                    self.nhrpclientstatrxresolvereplynakprohibited.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatTxErrorIndication"):
                    self.nhrpclientstattxerrorindication = value
                    self.nhrpclientstattxerrorindication.value_namespace = name_space
                    self.nhrpclientstattxerrorindication.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatTxPurgeReply"):
                    self.nhrpclientstattxpurgereply = value
                    self.nhrpclientstattxpurgereply.value_namespace = name_space
                    self.nhrpclientstattxpurgereply.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatTxPurgeReq"):
                    self.nhrpclientstattxpurgereq = value
                    self.nhrpclientstattxpurgereq.value_namespace = name_space
                    self.nhrpclientstattxpurgereq.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatTxRegisterReq"):
                    self.nhrpclientstattxregisterreq = value
                    self.nhrpclientstattxregisterreq.value_namespace = name_space
                    self.nhrpclientstattxregisterreq.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpClientStatTxResolveReq"):
                    self.nhrpclientstattxresolvereq = value
                    self.nhrpclientstattxresolvereq.value_namespace = name_space
                    self.nhrpclientstattxresolvereq.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.nhrpclientstatentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.nhrpclientstatentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nhrpClientStatTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "NHRP-MIB:NHRP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "nhrpClientStatEntry"):
                for c in self.nhrpclientstatentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NhrpMib.Nhrpclientstattable.Nhrpclientstatentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.nhrpclientstatentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nhrpClientStatEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Nhrpservertable(Entity):
        """
        This table contains information for a set of NHSes
        associated with this agent.
        
        .. attribute:: nhrpserverentry
        
        	Information about a single NHS
        	**type**\: list of    :py:class:`Nhrpserverentry <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpservertable.Nhrpserverentry>`
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NhrpMib.Nhrpservertable, self).__init__()

            self.yang_name = "nhrpServerTable"
            self.yang_parent_name = "NHRP-MIB"

            self.nhrpserverentry = YList(self)

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
                        super(NhrpMib.Nhrpservertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NhrpMib.Nhrpservertable, self).__setattr__(name, value)


        class Nhrpserverentry(Entity):
            """
            Information about a single NHS.
            
            .. attribute:: nhrpserverindex  <key>
            
            	An identifier for the server that is unique within the scope of this agent
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrpserverinternetworkaddr
            
            	The value of the internetwork layer address of this server
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: nhrpserverinternetworkaddrtype
            
            	The type of the internetwork layer address of this server. This object is used to interpret the value of nhrpServerInternetworkAddr
            	**type**\:   :py:class:`Addressfamilynumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.Addressfamilynumbers>`
            
            .. attribute:: nhrpservernbmaaddr
            
            	The value of the NBMA subnetwork address of this server
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: nhrpservernbmaaddrtype
            
            	The type of the NBMA subnetwork address of this server. This object is used to interpret the value of nhrpServerNbmaAddr
            	**type**\:   :py:class:`Addressfamilynumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.Addressfamilynumbers>`
            
            .. attribute:: nhrpservernbmasubaddr
            
            	The value of the NBMA subaddress of this server. For NBMA address families without a subaddress concept, this will be a zero\-length OCTET STRING
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: nhrpserverrowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: nhrpserverstoragetype
            
            	This object defines whether this row is kept in volatile storage and lost upon a Server crash or reboot situation, or if this row is backed up by nonvolatile or permanent storage
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NhrpMib.Nhrpservertable.Nhrpserverentry, self).__init__()

                self.yang_name = "nhrpServerEntry"
                self.yang_parent_name = "nhrpServerTable"

                self.nhrpserverindex = YLeaf(YType.uint32, "nhrpServerIndex")

                self.nhrpserverinternetworkaddr = YLeaf(YType.str, "nhrpServerInternetworkAddr")

                self.nhrpserverinternetworkaddrtype = YLeaf(YType.enumeration, "nhrpServerInternetworkAddrType")

                self.nhrpservernbmaaddr = YLeaf(YType.str, "nhrpServerNbmaAddr")

                self.nhrpservernbmaaddrtype = YLeaf(YType.enumeration, "nhrpServerNbmaAddrType")

                self.nhrpservernbmasubaddr = YLeaf(YType.str, "nhrpServerNbmaSubaddr")

                self.nhrpserverrowstatus = YLeaf(YType.enumeration, "nhrpServerRowStatus")

                self.nhrpserverstoragetype = YLeaf(YType.enumeration, "nhrpServerStorageType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("nhrpserverindex",
                                "nhrpserverinternetworkaddr",
                                "nhrpserverinternetworkaddrtype",
                                "nhrpservernbmaaddr",
                                "nhrpservernbmaaddrtype",
                                "nhrpservernbmasubaddr",
                                "nhrpserverrowstatus",
                                "nhrpserverstoragetype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NhrpMib.Nhrpservertable.Nhrpserverentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NhrpMib.Nhrpservertable.Nhrpserverentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.nhrpserverindex.is_set or
                    self.nhrpserverinternetworkaddr.is_set or
                    self.nhrpserverinternetworkaddrtype.is_set or
                    self.nhrpservernbmaaddr.is_set or
                    self.nhrpservernbmaaddrtype.is_set or
                    self.nhrpservernbmasubaddr.is_set or
                    self.nhrpserverrowstatus.is_set or
                    self.nhrpserverstoragetype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.nhrpserverindex.yfilter != YFilter.not_set or
                    self.nhrpserverinternetworkaddr.yfilter != YFilter.not_set or
                    self.nhrpserverinternetworkaddrtype.yfilter != YFilter.not_set or
                    self.nhrpservernbmaaddr.yfilter != YFilter.not_set or
                    self.nhrpservernbmaaddrtype.yfilter != YFilter.not_set or
                    self.nhrpservernbmasubaddr.yfilter != YFilter.not_set or
                    self.nhrpserverrowstatus.yfilter != YFilter.not_set or
                    self.nhrpserverstoragetype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nhrpServerEntry" + "[nhrpServerIndex='" + self.nhrpserverindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "NHRP-MIB:NHRP-MIB/nhrpServerTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.nhrpserverindex.is_set or self.nhrpserverindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverindex.get_name_leafdata())
                if (self.nhrpserverinternetworkaddr.is_set or self.nhrpserverinternetworkaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverinternetworkaddr.get_name_leafdata())
                if (self.nhrpserverinternetworkaddrtype.is_set or self.nhrpserverinternetworkaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverinternetworkaddrtype.get_name_leafdata())
                if (self.nhrpservernbmaaddr.is_set or self.nhrpservernbmaaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpservernbmaaddr.get_name_leafdata())
                if (self.nhrpservernbmaaddrtype.is_set or self.nhrpservernbmaaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpservernbmaaddrtype.get_name_leafdata())
                if (self.nhrpservernbmasubaddr.is_set or self.nhrpservernbmasubaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpservernbmasubaddr.get_name_leafdata())
                if (self.nhrpserverrowstatus.is_set or self.nhrpserverrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverrowstatus.get_name_leafdata())
                if (self.nhrpserverstoragetype.is_set or self.nhrpserverstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstoragetype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "nhrpServerIndex" or name == "nhrpServerInternetworkAddr" or name == "nhrpServerInternetworkAddrType" or name == "nhrpServerNbmaAddr" or name == "nhrpServerNbmaAddrType" or name == "nhrpServerNbmaSubaddr" or name == "nhrpServerRowStatus" or name == "nhrpServerStorageType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "nhrpServerIndex"):
                    self.nhrpserverindex = value
                    self.nhrpserverindex.value_namespace = name_space
                    self.nhrpserverindex.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerInternetworkAddr"):
                    self.nhrpserverinternetworkaddr = value
                    self.nhrpserverinternetworkaddr.value_namespace = name_space
                    self.nhrpserverinternetworkaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerInternetworkAddrType"):
                    self.nhrpserverinternetworkaddrtype = value
                    self.nhrpserverinternetworkaddrtype.value_namespace = name_space
                    self.nhrpserverinternetworkaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerNbmaAddr"):
                    self.nhrpservernbmaaddr = value
                    self.nhrpservernbmaaddr.value_namespace = name_space
                    self.nhrpservernbmaaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerNbmaAddrType"):
                    self.nhrpservernbmaaddrtype = value
                    self.nhrpservernbmaaddrtype.value_namespace = name_space
                    self.nhrpservernbmaaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerNbmaSubaddr"):
                    self.nhrpservernbmasubaddr = value
                    self.nhrpservernbmasubaddr.value_namespace = name_space
                    self.nhrpservernbmasubaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerRowStatus"):
                    self.nhrpserverrowstatus = value
                    self.nhrpserverrowstatus.value_namespace = name_space
                    self.nhrpserverrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStorageType"):
                    self.nhrpserverstoragetype = value
                    self.nhrpserverstoragetype.value_namespace = name_space
                    self.nhrpserverstoragetype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.nhrpserverentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.nhrpserverentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nhrpServerTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "NHRP-MIB:NHRP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "nhrpServerEntry"):
                for c in self.nhrpserverentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NhrpMib.Nhrpservertable.Nhrpserverentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.nhrpserverentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nhrpServerEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Nhrpservercachetable(Entity):
        """
        This table extends the nhrpCacheTable for
        NHSes.  If the nhrpCacheTable has a row added due to
        an NHS or based on information regarding an NHS then
        a row is also added in this table.
        
        The rows in this table will be created when rows in
        the nhrpCacheTable are created.  However, there may
        be rows created in the nhrpCacheTable which do not
        have corresponding rows in this table.  For example,
        if the nhrpCacheTable has a row added due to a Next
        Hop Client which is co\-resident on the same device
        as the NHS, a row will not be added to this table.
        
        .. attribute:: nhrpservercacheentry
        
        	Additional information kept by a NHS for a relevant Next Hop Resolution Cache entry
        	**type**\: list of    :py:class:`Nhrpservercacheentry <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpservercachetable.Nhrpservercacheentry>`
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NhrpMib.Nhrpservercachetable, self).__init__()

            self.yang_name = "nhrpServerCacheTable"
            self.yang_parent_name = "NHRP-MIB"

            self.nhrpservercacheentry = YList(self)

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
                        super(NhrpMib.Nhrpservercachetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NhrpMib.Nhrpservercachetable, self).__setattr__(name, value)


        class Nhrpservercacheentry(Entity):
            """
            Additional information kept by a NHS for a relevant
            Next Hop Resolution Cache entry.
            
            .. attribute:: nhrpcacheinternetworkaddrtype  <key>
            
            	
            	**type**\:   :py:class:`Addressfamilynumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.Addressfamilynumbers>`
            
            .. attribute:: nhrpcacheinternetworkaddr  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..64
            
            	**refers to**\:  :py:class:`nhrpcacheinternetworkaddr <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpcachetable.Nhrpcacheentry>`
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: nhrpcacheindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`nhrpcacheindex <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpcachetable.Nhrpcacheentry>`
            
            .. attribute:: nhrpservercacheauthoritative
            
            	An indication of whether this cache entry is authoritative, which means the entry was added because of a direct registration request with this server or by Server Cache Synchronization Protocol (SCSP) from an authoritative source
            	**type**\:  bool
            
            .. attribute:: nhrpservercacheuniqueness
            
            	The Uniqueness indicator for this cache entry used in duplicate address detection. This value cannot be changed after the entry is active
            	**type**\:  bool
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NhrpMib.Nhrpservercachetable.Nhrpservercacheentry, self).__init__()

                self.yang_name = "nhrpServerCacheEntry"
                self.yang_parent_name = "nhrpServerCacheTable"

                self.nhrpcacheinternetworkaddrtype = YLeaf(YType.enumeration, "nhrpCacheInternetworkAddrType")

                self.nhrpcacheinternetworkaddr = YLeaf(YType.str, "nhrpCacheInternetworkAddr")

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.nhrpcacheindex = YLeaf(YType.str, "nhrpCacheIndex")

                self.nhrpservercacheauthoritative = YLeaf(YType.boolean, "nhrpServerCacheAuthoritative")

                self.nhrpservercacheuniqueness = YLeaf(YType.boolean, "nhrpServerCacheUniqueness")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("nhrpcacheinternetworkaddrtype",
                                "nhrpcacheinternetworkaddr",
                                "ifindex",
                                "nhrpcacheindex",
                                "nhrpservercacheauthoritative",
                                "nhrpservercacheuniqueness") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NhrpMib.Nhrpservercachetable.Nhrpservercacheentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NhrpMib.Nhrpservercachetable.Nhrpservercacheentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.nhrpcacheinternetworkaddrtype.is_set or
                    self.nhrpcacheinternetworkaddr.is_set or
                    self.ifindex.is_set or
                    self.nhrpcacheindex.is_set or
                    self.nhrpservercacheauthoritative.is_set or
                    self.nhrpservercacheuniqueness.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.nhrpcacheinternetworkaddrtype.yfilter != YFilter.not_set or
                    self.nhrpcacheinternetworkaddr.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.nhrpcacheindex.yfilter != YFilter.not_set or
                    self.nhrpservercacheauthoritative.yfilter != YFilter.not_set or
                    self.nhrpservercacheuniqueness.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nhrpServerCacheEntry" + "[nhrpCacheInternetworkAddrType='" + self.nhrpcacheinternetworkaddrtype.get() + "']" + "[nhrpCacheInternetworkAddr='" + self.nhrpcacheinternetworkaddr.get() + "']" + "[ifIndex='" + self.ifindex.get() + "']" + "[nhrpCacheIndex='" + self.nhrpcacheindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "NHRP-MIB:NHRP-MIB/nhrpServerCacheTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.nhrpcacheinternetworkaddrtype.is_set or self.nhrpcacheinternetworkaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcacheinternetworkaddrtype.get_name_leafdata())
                if (self.nhrpcacheinternetworkaddr.is_set or self.nhrpcacheinternetworkaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcacheinternetworkaddr.get_name_leafdata())
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.nhrpcacheindex.is_set or self.nhrpcacheindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpcacheindex.get_name_leafdata())
                if (self.nhrpservercacheauthoritative.is_set or self.nhrpservercacheauthoritative.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpservercacheauthoritative.get_name_leafdata())
                if (self.nhrpservercacheuniqueness.is_set or self.nhrpservercacheuniqueness.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpservercacheuniqueness.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "nhrpCacheInternetworkAddrType" or name == "nhrpCacheInternetworkAddr" or name == "ifIndex" or name == "nhrpCacheIndex" or name == "nhrpServerCacheAuthoritative" or name == "nhrpServerCacheUniqueness"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "nhrpCacheInternetworkAddrType"):
                    self.nhrpcacheinternetworkaddrtype = value
                    self.nhrpcacheinternetworkaddrtype.value_namespace = name_space
                    self.nhrpcacheinternetworkaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpCacheInternetworkAddr"):
                    self.nhrpcacheinternetworkaddr = value
                    self.nhrpcacheinternetworkaddr.value_namespace = name_space
                    self.nhrpcacheinternetworkaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpCacheIndex"):
                    self.nhrpcacheindex = value
                    self.nhrpcacheindex.value_namespace = name_space
                    self.nhrpcacheindex.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerCacheAuthoritative"):
                    self.nhrpservercacheauthoritative = value
                    self.nhrpservercacheauthoritative.value_namespace = name_space
                    self.nhrpservercacheauthoritative.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerCacheUniqueness"):
                    self.nhrpservercacheuniqueness = value
                    self.nhrpservercacheuniqueness.value_namespace = name_space
                    self.nhrpservercacheuniqueness.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.nhrpservercacheentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.nhrpservercacheentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nhrpServerCacheTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "NHRP-MIB:NHRP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "nhrpServerCacheEntry"):
                for c in self.nhrpservercacheentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NhrpMib.Nhrpservercachetable.Nhrpservercacheentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.nhrpservercacheentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nhrpServerCacheEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Nhrpservernhctable(Entity):
        """
        A table of NHCs that are available for use by this NHS
        (Server).
        
        .. attribute:: nhrpservernhcentry
        
        	An NHC that may be used by an NHS
        	**type**\: list of    :py:class:`Nhrpservernhcentry <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpservernhctable.Nhrpservernhcentry>`
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NhrpMib.Nhrpservernhctable, self).__init__()

            self.yang_name = "nhrpServerNhcTable"
            self.yang_parent_name = "NHRP-MIB"

            self.nhrpservernhcentry = YList(self)

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
                        super(NhrpMib.Nhrpservernhctable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NhrpMib.Nhrpservernhctable, self).__setattr__(name, value)


        class Nhrpservernhcentry(Entity):
            """
            An NHC that may be used by an NHS.
            
            .. attribute:: nhrpserverindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`nhrpserverindex <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpservertable.Nhrpserverentry>`
            
            .. attribute:: nhrpservernhcindex  <key>
            
            	An identifier for an NHC available to an NHS
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrpservernhcinternetworkaddr
            
            	The value of the internetwork layer address of the NHRP Client represented by this entry.  If this value is not known, this will be a zero\-length OCTET STRING
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: nhrpservernhcinternetworkaddrtype
            
            	The type of the internetwork layer address of the NHRP Client represented in this entry. This object indicates how the value of nhrpServerNhcInternetworkAddr is to be interpreted
            	**type**\:   :py:class:`Addressfamilynumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.Addressfamilynumbers>`
            
            .. attribute:: nhrpservernhcinuse
            
            	An indication of whether this NHC is in use by the NHS
            	**type**\:  bool
            
            .. attribute:: nhrpservernhcnbmaaddr
            
            	The NBMA subnetwork address of the NHC. The type of the address is indicated by the corresponding value of nhrpServerNbmaAddrType
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: nhrpservernhcnbmaaddrtype
            
            	The type of the NBMA subnetwork address of the NHRP Client represented by this entry. This object indicates how the values of nhrpServerNhcNbmaAddr and nhrpServerNhcNbmaSubaddr are to be interpreted
            	**type**\:   :py:class:`Addressfamilynumbers <ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB.Addressfamilynumbers>`
            
            .. attribute:: nhrpservernhcnbmasubaddr
            
            	The NBMA subaddress of the NHC. For NMBA address familes that do not have the concept of subaddress, this will be a zero\-length OCTET STRING
            	**type**\:  str
            
            	**length:** 0..64
            
            .. attribute:: nhrpservernhcprefixlength
            
            	The number of bits that define the internetwork layer prefix associated with the nhrpServerNhcInternetworkAddr
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: nhrpservernhcrowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NhrpMib.Nhrpservernhctable.Nhrpservernhcentry, self).__init__()

                self.yang_name = "nhrpServerNhcEntry"
                self.yang_parent_name = "nhrpServerNhcTable"

                self.nhrpserverindex = YLeaf(YType.str, "nhrpServerIndex")

                self.nhrpservernhcindex = YLeaf(YType.uint32, "nhrpServerNhcIndex")

                self.nhrpservernhcinternetworkaddr = YLeaf(YType.str, "nhrpServerNhcInternetworkAddr")

                self.nhrpservernhcinternetworkaddrtype = YLeaf(YType.enumeration, "nhrpServerNhcInternetworkAddrType")

                self.nhrpservernhcinuse = YLeaf(YType.boolean, "nhrpServerNhcInUse")

                self.nhrpservernhcnbmaaddr = YLeaf(YType.str, "nhrpServerNhcNbmaAddr")

                self.nhrpservernhcnbmaaddrtype = YLeaf(YType.enumeration, "nhrpServerNhcNbmaAddrType")

                self.nhrpservernhcnbmasubaddr = YLeaf(YType.str, "nhrpServerNhcNbmaSubaddr")

                self.nhrpservernhcprefixlength = YLeaf(YType.int32, "nhrpServerNhcPrefixLength")

                self.nhrpservernhcrowstatus = YLeaf(YType.enumeration, "nhrpServerNhcRowStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("nhrpserverindex",
                                "nhrpservernhcindex",
                                "nhrpservernhcinternetworkaddr",
                                "nhrpservernhcinternetworkaddrtype",
                                "nhrpservernhcinuse",
                                "nhrpservernhcnbmaaddr",
                                "nhrpservernhcnbmaaddrtype",
                                "nhrpservernhcnbmasubaddr",
                                "nhrpservernhcprefixlength",
                                "nhrpservernhcrowstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NhrpMib.Nhrpservernhctable.Nhrpservernhcentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NhrpMib.Nhrpservernhctable.Nhrpservernhcentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.nhrpserverindex.is_set or
                    self.nhrpservernhcindex.is_set or
                    self.nhrpservernhcinternetworkaddr.is_set or
                    self.nhrpservernhcinternetworkaddrtype.is_set or
                    self.nhrpservernhcinuse.is_set or
                    self.nhrpservernhcnbmaaddr.is_set or
                    self.nhrpservernhcnbmaaddrtype.is_set or
                    self.nhrpservernhcnbmasubaddr.is_set or
                    self.nhrpservernhcprefixlength.is_set or
                    self.nhrpservernhcrowstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.nhrpserverindex.yfilter != YFilter.not_set or
                    self.nhrpservernhcindex.yfilter != YFilter.not_set or
                    self.nhrpservernhcinternetworkaddr.yfilter != YFilter.not_set or
                    self.nhrpservernhcinternetworkaddrtype.yfilter != YFilter.not_set or
                    self.nhrpservernhcinuse.yfilter != YFilter.not_set or
                    self.nhrpservernhcnbmaaddr.yfilter != YFilter.not_set or
                    self.nhrpservernhcnbmaaddrtype.yfilter != YFilter.not_set or
                    self.nhrpservernhcnbmasubaddr.yfilter != YFilter.not_set or
                    self.nhrpservernhcprefixlength.yfilter != YFilter.not_set or
                    self.nhrpservernhcrowstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nhrpServerNhcEntry" + "[nhrpServerIndex='" + self.nhrpserverindex.get() + "']" + "[nhrpServerNhcIndex='" + self.nhrpservernhcindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "NHRP-MIB:NHRP-MIB/nhrpServerNhcTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.nhrpserverindex.is_set or self.nhrpserverindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverindex.get_name_leafdata())
                if (self.nhrpservernhcindex.is_set or self.nhrpservernhcindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpservernhcindex.get_name_leafdata())
                if (self.nhrpservernhcinternetworkaddr.is_set or self.nhrpservernhcinternetworkaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpservernhcinternetworkaddr.get_name_leafdata())
                if (self.nhrpservernhcinternetworkaddrtype.is_set or self.nhrpservernhcinternetworkaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpservernhcinternetworkaddrtype.get_name_leafdata())
                if (self.nhrpservernhcinuse.is_set or self.nhrpservernhcinuse.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpservernhcinuse.get_name_leafdata())
                if (self.nhrpservernhcnbmaaddr.is_set or self.nhrpservernhcnbmaaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpservernhcnbmaaddr.get_name_leafdata())
                if (self.nhrpservernhcnbmaaddrtype.is_set or self.nhrpservernhcnbmaaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpservernhcnbmaaddrtype.get_name_leafdata())
                if (self.nhrpservernhcnbmasubaddr.is_set or self.nhrpservernhcnbmasubaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpservernhcnbmasubaddr.get_name_leafdata())
                if (self.nhrpservernhcprefixlength.is_set or self.nhrpservernhcprefixlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpservernhcprefixlength.get_name_leafdata())
                if (self.nhrpservernhcrowstatus.is_set or self.nhrpservernhcrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpservernhcrowstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "nhrpServerIndex" or name == "nhrpServerNhcIndex" or name == "nhrpServerNhcInternetworkAddr" or name == "nhrpServerNhcInternetworkAddrType" or name == "nhrpServerNhcInUse" or name == "nhrpServerNhcNbmaAddr" or name == "nhrpServerNhcNbmaAddrType" or name == "nhrpServerNhcNbmaSubaddr" or name == "nhrpServerNhcPrefixLength" or name == "nhrpServerNhcRowStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "nhrpServerIndex"):
                    self.nhrpserverindex = value
                    self.nhrpserverindex.value_namespace = name_space
                    self.nhrpserverindex.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerNhcIndex"):
                    self.nhrpservernhcindex = value
                    self.nhrpservernhcindex.value_namespace = name_space
                    self.nhrpservernhcindex.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerNhcInternetworkAddr"):
                    self.nhrpservernhcinternetworkaddr = value
                    self.nhrpservernhcinternetworkaddr.value_namespace = name_space
                    self.nhrpservernhcinternetworkaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerNhcInternetworkAddrType"):
                    self.nhrpservernhcinternetworkaddrtype = value
                    self.nhrpservernhcinternetworkaddrtype.value_namespace = name_space
                    self.nhrpservernhcinternetworkaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerNhcInUse"):
                    self.nhrpservernhcinuse = value
                    self.nhrpservernhcinuse.value_namespace = name_space
                    self.nhrpservernhcinuse.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerNhcNbmaAddr"):
                    self.nhrpservernhcnbmaaddr = value
                    self.nhrpservernhcnbmaaddr.value_namespace = name_space
                    self.nhrpservernhcnbmaaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerNhcNbmaAddrType"):
                    self.nhrpservernhcnbmaaddrtype = value
                    self.nhrpservernhcnbmaaddrtype.value_namespace = name_space
                    self.nhrpservernhcnbmaaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerNhcNbmaSubaddr"):
                    self.nhrpservernhcnbmasubaddr = value
                    self.nhrpservernhcnbmasubaddr.value_namespace = name_space
                    self.nhrpservernhcnbmasubaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerNhcPrefixLength"):
                    self.nhrpservernhcprefixlength = value
                    self.nhrpservernhcprefixlength.value_namespace = name_space
                    self.nhrpservernhcprefixlength.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerNhcRowStatus"):
                    self.nhrpservernhcrowstatus = value
                    self.nhrpservernhcrowstatus.value_namespace = name_space
                    self.nhrpservernhcrowstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.nhrpservernhcentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.nhrpservernhcentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nhrpServerNhcTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "NHRP-MIB:NHRP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "nhrpServerNhcEntry"):
                for c in self.nhrpservernhcentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NhrpMib.Nhrpservernhctable.Nhrpservernhcentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.nhrpservernhcentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nhrpServerNhcEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Nhrpserverstattable(Entity):
        """
        Statistics collected by Next Hop Servers.
        
        .. attribute:: nhrpserverstatentry
        
        	Statistics for a particular NHS. The statistics are broken into received (Rx), transmitted (Tx) and forwarded (Fw).  Forwarded (Fw) would be done by a transit NHS
        	**type**\: list of    :py:class:`Nhrpserverstatentry <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpserverstattable.Nhrpserverstatentry>`
        
        

        """

        _prefix = 'NHRP-MIB'
        _revision = '1999-08-26'

        def __init__(self):
            super(NhrpMib.Nhrpserverstattable, self).__init__()

            self.yang_name = "nhrpServerStatTable"
            self.yang_parent_name = "NHRP-MIB"

            self.nhrpserverstatentry = YList(self)

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
                        super(NhrpMib.Nhrpserverstattable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(NhrpMib.Nhrpserverstattable, self).__setattr__(name, value)


        class Nhrpserverstatentry(Entity):
            """
            Statistics for a particular NHS. The statistics are
            broken into received (Rx), transmitted (Tx)
            and forwarded (Fw).  Forwarded (Fw) would be done
            by a transit NHS.
            
            .. attribute:: nhrpserverindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`nhrpserverindex <ydk.models.cisco_ios_xe.NHRP_MIB.NhrpMib.Nhrpservertable.Nhrpserverentry>`
            
            .. attribute:: nhrpserverstatdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this Server's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\-initialization of the    local management subsystem or the NHRP Server re\-initialization associated with this entry, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatfwerrorindication
            
            	The number of NHRP Error Indication packets forwarded by this server acting as a transit NHS.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatfwpurgereply
            
            	The number of NHRP Purge Replies forwarded by this server acting as a transit NHS.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatfwpurgereq
            
            	The number of NHRP Purge Requests forwarded by this server acting as a transit NHS.   Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatfwregisterreply
            
            	The number of NHRP Registration Replies forwarded by this server acting as a transit NHS. Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatfwregisterreq
            
            	The number of NHRP Registration Requests forwarded by this server acting as a transit NHS.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatfwresolvereply
            
            	The number of NHRP Resolution Replies forwarded by this server acting as a transit NHS.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatfwresolvereq
            
            	The number of NHRP Resolution Requests forwarded by this server acting as a transit NHS.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxerrauthenticationfailure
            
            	The number of NHRP Error Indication packets received by this server with the error code 'Authentication Failure'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxerrhopcountexceeded
            
            	The number of NHRP Error Indication packets received by this server with the error code 'Hop Count Exceeded'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxerrinvalidextension
            
            	The number of NHRP Error Indication packets received by this server with the error code 'Invalid Extension'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxerrinvalidresreplyreceived
            
            	The number of NHRP Error Indication packets received by this server with the error code 'Invalid Resolution Reply Received'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxerrloopdetected
            
            	The number of NHRP Error Indication packets received by this server with the error code 'NHRP Loop Detected'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxerrprotoaddrunreachable
            
            	The number of NHRP Error Indication packets received by this server with the error code 'Protocol Address Unreachable'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxerrprotoerror
            
            	The number of NHRP Error Indication packets received by this server with the error code 'Protocol Error'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxerrsdusizeexceeded
            
            	The number of NHRP Error Indication packets received by this server with the error code 'NHRP SDU Size Exceeded'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxerrunrecognizedextension
            
            	The number of NHRP Error Indication packets received by this server with the error code  'Unrecognized Extension'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxpurgereply
            
            	The number of NHRP Purge Replies received by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxpurgereq
            
            	The number of NHRP Purge Requests received by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxregisterreq
            
            	The number of NHRP Registration Requests received by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxresolvereq
            
            	The number of NHRP Resolution Requests received by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxerrauthenticationfailure
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'Authentication Failure'.     Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxerrhopcountexceeded
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'Hop Count Exceeded'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxerrinvalidextension
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code  'Invalid Extension'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxerrloopdetected
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'NHRP Loop Detected'.     Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxerrprotoaddrunreachable
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'Protocol Address Unreachable'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxerrprotoerror
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'Protocol Error'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxerrsdusizeexceeded
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'NHRP SDU Size Exceeded'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxerrunrecognizedextension
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'Unrecognized Extension'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxpurgereply
            
            	The number of NHRP Purge Replies transmitted by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxpurgereq
            
            	The number of NHRP Purge Requests transmitted by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxregisterack
            
            	The number of positively acknowledged NHRP Registration Replies transmitted by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxregisternakalreadyreg
            
            	The number of NAKed NHRP Registration Replies transmitted by this server with the code 'Unique Internetworking Layer Address Already Registered'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxregisternakinsufresources
            
            	The number of NAKed NHRP Registration Replies transmitted by this server with the code 'Insufficient Resources'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxregisternakprohibited
            
            	The number of NAKed NHRP Registration Replies transmitted by this server with the code 'Administratively Prohibited'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxresolvereplyack
            
            	The number of positively acknowledged NHRP Resolution Replies transmitted by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxresolvereplynakinsufresources
            
            	The number of NAKed NHRP Resolution Replies transmitted by this server with the code 'Insufficient Resources'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxresolvereplynaknobinding
            
            	The number of NAKed NHRP Resolution Replies transmitted by this server with the code 'No Internetworking Layer Address to NBMA Address Binding Exists'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxresolvereplynaknotunique
            
            	The number of NAKed NHRP Resolution Replies transmitted by this server with the code 'Binding Exists But Is Not Unique'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxresolvereplynakprohibited
            
            	The number of NAKed NHRP Resolution Replies transmitted by this server with the code 'Administratively Prohibited'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'NHRP-MIB'
            _revision = '1999-08-26'

            def __init__(self):
                super(NhrpMib.Nhrpserverstattable.Nhrpserverstatentry, self).__init__()

                self.yang_name = "nhrpServerStatEntry"
                self.yang_parent_name = "nhrpServerStatTable"

                self.nhrpserverindex = YLeaf(YType.str, "nhrpServerIndex")

                self.nhrpserverstatdiscontinuitytime = YLeaf(YType.uint32, "nhrpServerStatDiscontinuityTime")

                self.nhrpserverstatfwerrorindication = YLeaf(YType.uint32, "nhrpServerStatFwErrorIndication")

                self.nhrpserverstatfwpurgereply = YLeaf(YType.uint32, "nhrpServerStatFwPurgeReply")

                self.nhrpserverstatfwpurgereq = YLeaf(YType.uint32, "nhrpServerStatFwPurgeReq")

                self.nhrpserverstatfwregisterreply = YLeaf(YType.uint32, "nhrpServerStatFwRegisterReply")

                self.nhrpserverstatfwregisterreq = YLeaf(YType.uint32, "nhrpServerStatFwRegisterReq")

                self.nhrpserverstatfwresolvereply = YLeaf(YType.uint32, "nhrpServerStatFwResolveReply")

                self.nhrpserverstatfwresolvereq = YLeaf(YType.uint32, "nhrpServerStatFwResolveReq")

                self.nhrpserverstatrxerrauthenticationfailure = YLeaf(YType.uint32, "nhrpServerStatRxErrAuthenticationFailure")

                self.nhrpserverstatrxerrhopcountexceeded = YLeaf(YType.uint32, "nhrpServerStatRxErrHopCountExceeded")

                self.nhrpserverstatrxerrinvalidextension = YLeaf(YType.uint32, "nhrpServerStatRxErrInvalidExtension")

                self.nhrpserverstatrxerrinvalidresreplyreceived = YLeaf(YType.uint32, "nhrpServerStatRxErrInvalidResReplyReceived")

                self.nhrpserverstatrxerrloopdetected = YLeaf(YType.uint32, "nhrpServerStatRxErrLoopDetected")

                self.nhrpserverstatrxerrprotoaddrunreachable = YLeaf(YType.uint32, "nhrpServerStatRxErrProtoAddrUnreachable")

                self.nhrpserverstatrxerrprotoerror = YLeaf(YType.uint32, "nhrpServerStatRxErrProtoError")

                self.nhrpserverstatrxerrsdusizeexceeded = YLeaf(YType.uint32, "nhrpServerStatRxErrSduSizeExceeded")

                self.nhrpserverstatrxerrunrecognizedextension = YLeaf(YType.uint32, "nhrpServerStatRxErrUnrecognizedExtension")

                self.nhrpserverstatrxpurgereply = YLeaf(YType.uint32, "nhrpServerStatRxPurgeReply")

                self.nhrpserverstatrxpurgereq = YLeaf(YType.uint32, "nhrpServerStatRxPurgeReq")

                self.nhrpserverstatrxregisterreq = YLeaf(YType.uint32, "nhrpServerStatRxRegisterReq")

                self.nhrpserverstatrxresolvereq = YLeaf(YType.uint32, "nhrpServerStatRxResolveReq")

                self.nhrpserverstattxerrauthenticationfailure = YLeaf(YType.uint32, "nhrpServerStatTxErrAuthenticationFailure")

                self.nhrpserverstattxerrhopcountexceeded = YLeaf(YType.uint32, "nhrpServerStatTxErrHopCountExceeded")

                self.nhrpserverstattxerrinvalidextension = YLeaf(YType.uint32, "nhrpServerStatTxErrInvalidExtension")

                self.nhrpserverstattxerrloopdetected = YLeaf(YType.uint32, "nhrpServerStatTxErrLoopDetected")

                self.nhrpserverstattxerrprotoaddrunreachable = YLeaf(YType.uint32, "nhrpServerStatTxErrProtoAddrUnreachable")

                self.nhrpserverstattxerrprotoerror = YLeaf(YType.uint32, "nhrpServerStatTxErrProtoError")

                self.nhrpserverstattxerrsdusizeexceeded = YLeaf(YType.uint32, "nhrpServerStatTxErrSduSizeExceeded")

                self.nhrpserverstattxerrunrecognizedextension = YLeaf(YType.uint32, "nhrpServerStatTxErrUnrecognizedExtension")

                self.nhrpserverstattxpurgereply = YLeaf(YType.uint32, "nhrpServerStatTxPurgeReply")

                self.nhrpserverstattxpurgereq = YLeaf(YType.uint32, "nhrpServerStatTxPurgeReq")

                self.nhrpserverstattxregisterack = YLeaf(YType.uint32, "nhrpServerStatTxRegisterAck")

                self.nhrpserverstattxregisternakalreadyreg = YLeaf(YType.uint32, "nhrpServerStatTxRegisterNakAlreadyReg")

                self.nhrpserverstattxregisternakinsufresources = YLeaf(YType.uint32, "nhrpServerStatTxRegisterNakInsufResources")

                self.nhrpserverstattxregisternakprohibited = YLeaf(YType.uint32, "nhrpServerStatTxRegisterNakProhibited")

                self.nhrpserverstattxresolvereplyack = YLeaf(YType.uint32, "nhrpServerStatTxResolveReplyAck")

                self.nhrpserverstattxresolvereplynakinsufresources = YLeaf(YType.uint32, "nhrpServerStatTxResolveReplyNakInsufResources")

                self.nhrpserverstattxresolvereplynaknobinding = YLeaf(YType.uint32, "nhrpServerStatTxResolveReplyNakNoBinding")

                self.nhrpserverstattxresolvereplynaknotunique = YLeaf(YType.uint32, "nhrpServerStatTxResolveReplyNakNotUnique")

                self.nhrpserverstattxresolvereplynakprohibited = YLeaf(YType.uint32, "nhrpServerStatTxResolveReplyNakProhibited")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("nhrpserverindex",
                                "nhrpserverstatdiscontinuitytime",
                                "nhrpserverstatfwerrorindication",
                                "nhrpserverstatfwpurgereply",
                                "nhrpserverstatfwpurgereq",
                                "nhrpserverstatfwregisterreply",
                                "nhrpserverstatfwregisterreq",
                                "nhrpserverstatfwresolvereply",
                                "nhrpserverstatfwresolvereq",
                                "nhrpserverstatrxerrauthenticationfailure",
                                "nhrpserverstatrxerrhopcountexceeded",
                                "nhrpserverstatrxerrinvalidextension",
                                "nhrpserverstatrxerrinvalidresreplyreceived",
                                "nhrpserverstatrxerrloopdetected",
                                "nhrpserverstatrxerrprotoaddrunreachable",
                                "nhrpserverstatrxerrprotoerror",
                                "nhrpserverstatrxerrsdusizeexceeded",
                                "nhrpserverstatrxerrunrecognizedextension",
                                "nhrpserverstatrxpurgereply",
                                "nhrpserverstatrxpurgereq",
                                "nhrpserverstatrxregisterreq",
                                "nhrpserverstatrxresolvereq",
                                "nhrpserverstattxerrauthenticationfailure",
                                "nhrpserverstattxerrhopcountexceeded",
                                "nhrpserverstattxerrinvalidextension",
                                "nhrpserverstattxerrloopdetected",
                                "nhrpserverstattxerrprotoaddrunreachable",
                                "nhrpserverstattxerrprotoerror",
                                "nhrpserverstattxerrsdusizeexceeded",
                                "nhrpserverstattxerrunrecognizedextension",
                                "nhrpserverstattxpurgereply",
                                "nhrpserverstattxpurgereq",
                                "nhrpserverstattxregisterack",
                                "nhrpserverstattxregisternakalreadyreg",
                                "nhrpserverstattxregisternakinsufresources",
                                "nhrpserverstattxregisternakprohibited",
                                "nhrpserverstattxresolvereplyack",
                                "nhrpserverstattxresolvereplynakinsufresources",
                                "nhrpserverstattxresolvereplynaknobinding",
                                "nhrpserverstattxresolvereplynaknotunique",
                                "nhrpserverstattxresolvereplynakprohibited") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(NhrpMib.Nhrpserverstattable.Nhrpserverstatentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(NhrpMib.Nhrpserverstattable.Nhrpserverstatentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.nhrpserverindex.is_set or
                    self.nhrpserverstatdiscontinuitytime.is_set or
                    self.nhrpserverstatfwerrorindication.is_set or
                    self.nhrpserverstatfwpurgereply.is_set or
                    self.nhrpserverstatfwpurgereq.is_set or
                    self.nhrpserverstatfwregisterreply.is_set or
                    self.nhrpserverstatfwregisterreq.is_set or
                    self.nhrpserverstatfwresolvereply.is_set or
                    self.nhrpserverstatfwresolvereq.is_set or
                    self.nhrpserverstatrxerrauthenticationfailure.is_set or
                    self.nhrpserverstatrxerrhopcountexceeded.is_set or
                    self.nhrpserverstatrxerrinvalidextension.is_set or
                    self.nhrpserverstatrxerrinvalidresreplyreceived.is_set or
                    self.nhrpserverstatrxerrloopdetected.is_set or
                    self.nhrpserverstatrxerrprotoaddrunreachable.is_set or
                    self.nhrpserverstatrxerrprotoerror.is_set or
                    self.nhrpserverstatrxerrsdusizeexceeded.is_set or
                    self.nhrpserverstatrxerrunrecognizedextension.is_set or
                    self.nhrpserverstatrxpurgereply.is_set or
                    self.nhrpserverstatrxpurgereq.is_set or
                    self.nhrpserverstatrxregisterreq.is_set or
                    self.nhrpserverstatrxresolvereq.is_set or
                    self.nhrpserverstattxerrauthenticationfailure.is_set or
                    self.nhrpserverstattxerrhopcountexceeded.is_set or
                    self.nhrpserverstattxerrinvalidextension.is_set or
                    self.nhrpserverstattxerrloopdetected.is_set or
                    self.nhrpserverstattxerrprotoaddrunreachable.is_set or
                    self.nhrpserverstattxerrprotoerror.is_set or
                    self.nhrpserverstattxerrsdusizeexceeded.is_set or
                    self.nhrpserverstattxerrunrecognizedextension.is_set or
                    self.nhrpserverstattxpurgereply.is_set or
                    self.nhrpserverstattxpurgereq.is_set or
                    self.nhrpserverstattxregisterack.is_set or
                    self.nhrpserverstattxregisternakalreadyreg.is_set or
                    self.nhrpserverstattxregisternakinsufresources.is_set or
                    self.nhrpserverstattxregisternakprohibited.is_set or
                    self.nhrpserverstattxresolvereplyack.is_set or
                    self.nhrpserverstattxresolvereplynakinsufresources.is_set or
                    self.nhrpserverstattxresolvereplynaknobinding.is_set or
                    self.nhrpserverstattxresolvereplynaknotunique.is_set or
                    self.nhrpserverstattxresolvereplynakprohibited.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.nhrpserverindex.yfilter != YFilter.not_set or
                    self.nhrpserverstatdiscontinuitytime.yfilter != YFilter.not_set or
                    self.nhrpserverstatfwerrorindication.yfilter != YFilter.not_set or
                    self.nhrpserverstatfwpurgereply.yfilter != YFilter.not_set or
                    self.nhrpserverstatfwpurgereq.yfilter != YFilter.not_set or
                    self.nhrpserverstatfwregisterreply.yfilter != YFilter.not_set or
                    self.nhrpserverstatfwregisterreq.yfilter != YFilter.not_set or
                    self.nhrpserverstatfwresolvereply.yfilter != YFilter.not_set or
                    self.nhrpserverstatfwresolvereq.yfilter != YFilter.not_set or
                    self.nhrpserverstatrxerrauthenticationfailure.yfilter != YFilter.not_set or
                    self.nhrpserverstatrxerrhopcountexceeded.yfilter != YFilter.not_set or
                    self.nhrpserverstatrxerrinvalidextension.yfilter != YFilter.not_set or
                    self.nhrpserverstatrxerrinvalidresreplyreceived.yfilter != YFilter.not_set or
                    self.nhrpserverstatrxerrloopdetected.yfilter != YFilter.not_set or
                    self.nhrpserverstatrxerrprotoaddrunreachable.yfilter != YFilter.not_set or
                    self.nhrpserverstatrxerrprotoerror.yfilter != YFilter.not_set or
                    self.nhrpserverstatrxerrsdusizeexceeded.yfilter != YFilter.not_set or
                    self.nhrpserverstatrxerrunrecognizedextension.yfilter != YFilter.not_set or
                    self.nhrpserverstatrxpurgereply.yfilter != YFilter.not_set or
                    self.nhrpserverstatrxpurgereq.yfilter != YFilter.not_set or
                    self.nhrpserverstatrxregisterreq.yfilter != YFilter.not_set or
                    self.nhrpserverstatrxresolvereq.yfilter != YFilter.not_set or
                    self.nhrpserverstattxerrauthenticationfailure.yfilter != YFilter.not_set or
                    self.nhrpserverstattxerrhopcountexceeded.yfilter != YFilter.not_set or
                    self.nhrpserverstattxerrinvalidextension.yfilter != YFilter.not_set or
                    self.nhrpserverstattxerrloopdetected.yfilter != YFilter.not_set or
                    self.nhrpserverstattxerrprotoaddrunreachable.yfilter != YFilter.not_set or
                    self.nhrpserverstattxerrprotoerror.yfilter != YFilter.not_set or
                    self.nhrpserverstattxerrsdusizeexceeded.yfilter != YFilter.not_set or
                    self.nhrpserverstattxerrunrecognizedextension.yfilter != YFilter.not_set or
                    self.nhrpserverstattxpurgereply.yfilter != YFilter.not_set or
                    self.nhrpserverstattxpurgereq.yfilter != YFilter.not_set or
                    self.nhrpserverstattxregisterack.yfilter != YFilter.not_set or
                    self.nhrpserverstattxregisternakalreadyreg.yfilter != YFilter.not_set or
                    self.nhrpserverstattxregisternakinsufresources.yfilter != YFilter.not_set or
                    self.nhrpserverstattxregisternakprohibited.yfilter != YFilter.not_set or
                    self.nhrpserverstattxresolvereplyack.yfilter != YFilter.not_set or
                    self.nhrpserverstattxresolvereplynakinsufresources.yfilter != YFilter.not_set or
                    self.nhrpserverstattxresolvereplynaknobinding.yfilter != YFilter.not_set or
                    self.nhrpserverstattxresolvereplynaknotunique.yfilter != YFilter.not_set or
                    self.nhrpserverstattxresolvereplynakprohibited.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "nhrpServerStatEntry" + "[nhrpServerIndex='" + self.nhrpserverindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "NHRP-MIB:NHRP-MIB/nhrpServerStatTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.nhrpserverindex.is_set or self.nhrpserverindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverindex.get_name_leafdata())
                if (self.nhrpserverstatdiscontinuitytime.is_set or self.nhrpserverstatdiscontinuitytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatdiscontinuitytime.get_name_leafdata())
                if (self.nhrpserverstatfwerrorindication.is_set or self.nhrpserverstatfwerrorindication.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatfwerrorindication.get_name_leafdata())
                if (self.nhrpserverstatfwpurgereply.is_set or self.nhrpserverstatfwpurgereply.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatfwpurgereply.get_name_leafdata())
                if (self.nhrpserverstatfwpurgereq.is_set or self.nhrpserverstatfwpurgereq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatfwpurgereq.get_name_leafdata())
                if (self.nhrpserverstatfwregisterreply.is_set or self.nhrpserverstatfwregisterreply.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatfwregisterreply.get_name_leafdata())
                if (self.nhrpserverstatfwregisterreq.is_set or self.nhrpserverstatfwregisterreq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatfwregisterreq.get_name_leafdata())
                if (self.nhrpserverstatfwresolvereply.is_set or self.nhrpserverstatfwresolvereply.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatfwresolvereply.get_name_leafdata())
                if (self.nhrpserverstatfwresolvereq.is_set or self.nhrpserverstatfwresolvereq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatfwresolvereq.get_name_leafdata())
                if (self.nhrpserverstatrxerrauthenticationfailure.is_set or self.nhrpserverstatrxerrauthenticationfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatrxerrauthenticationfailure.get_name_leafdata())
                if (self.nhrpserverstatrxerrhopcountexceeded.is_set or self.nhrpserverstatrxerrhopcountexceeded.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatrxerrhopcountexceeded.get_name_leafdata())
                if (self.nhrpserverstatrxerrinvalidextension.is_set or self.nhrpserverstatrxerrinvalidextension.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatrxerrinvalidextension.get_name_leafdata())
                if (self.nhrpserverstatrxerrinvalidresreplyreceived.is_set or self.nhrpserverstatrxerrinvalidresreplyreceived.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatrxerrinvalidresreplyreceived.get_name_leafdata())
                if (self.nhrpserverstatrxerrloopdetected.is_set or self.nhrpserverstatrxerrloopdetected.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatrxerrloopdetected.get_name_leafdata())
                if (self.nhrpserverstatrxerrprotoaddrunreachable.is_set or self.nhrpserverstatrxerrprotoaddrunreachable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatrxerrprotoaddrunreachable.get_name_leafdata())
                if (self.nhrpserverstatrxerrprotoerror.is_set or self.nhrpserverstatrxerrprotoerror.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatrxerrprotoerror.get_name_leafdata())
                if (self.nhrpserverstatrxerrsdusizeexceeded.is_set or self.nhrpserverstatrxerrsdusizeexceeded.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatrxerrsdusizeexceeded.get_name_leafdata())
                if (self.nhrpserverstatrxerrunrecognizedextension.is_set or self.nhrpserverstatrxerrunrecognizedextension.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatrxerrunrecognizedextension.get_name_leafdata())
                if (self.nhrpserverstatrxpurgereply.is_set or self.nhrpserverstatrxpurgereply.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatrxpurgereply.get_name_leafdata())
                if (self.nhrpserverstatrxpurgereq.is_set or self.nhrpserverstatrxpurgereq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatrxpurgereq.get_name_leafdata())
                if (self.nhrpserverstatrxregisterreq.is_set or self.nhrpserverstatrxregisterreq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatrxregisterreq.get_name_leafdata())
                if (self.nhrpserverstatrxresolvereq.is_set or self.nhrpserverstatrxresolvereq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstatrxresolvereq.get_name_leafdata())
                if (self.nhrpserverstattxerrauthenticationfailure.is_set or self.nhrpserverstattxerrauthenticationfailure.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxerrauthenticationfailure.get_name_leafdata())
                if (self.nhrpserverstattxerrhopcountexceeded.is_set or self.nhrpserverstattxerrhopcountexceeded.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxerrhopcountexceeded.get_name_leafdata())
                if (self.nhrpserverstattxerrinvalidextension.is_set or self.nhrpserverstattxerrinvalidextension.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxerrinvalidextension.get_name_leafdata())
                if (self.nhrpserverstattxerrloopdetected.is_set or self.nhrpserverstattxerrloopdetected.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxerrloopdetected.get_name_leafdata())
                if (self.nhrpserverstattxerrprotoaddrunreachable.is_set or self.nhrpserverstattxerrprotoaddrunreachable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxerrprotoaddrunreachable.get_name_leafdata())
                if (self.nhrpserverstattxerrprotoerror.is_set or self.nhrpserverstattxerrprotoerror.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxerrprotoerror.get_name_leafdata())
                if (self.nhrpserverstattxerrsdusizeexceeded.is_set or self.nhrpserverstattxerrsdusizeexceeded.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxerrsdusizeexceeded.get_name_leafdata())
                if (self.nhrpserverstattxerrunrecognizedextension.is_set or self.nhrpserverstattxerrunrecognizedextension.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxerrunrecognizedextension.get_name_leafdata())
                if (self.nhrpserverstattxpurgereply.is_set or self.nhrpserverstattxpurgereply.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxpurgereply.get_name_leafdata())
                if (self.nhrpserverstattxpurgereq.is_set or self.nhrpserverstattxpurgereq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxpurgereq.get_name_leafdata())
                if (self.nhrpserverstattxregisterack.is_set or self.nhrpserverstattxregisterack.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxregisterack.get_name_leafdata())
                if (self.nhrpserverstattxregisternakalreadyreg.is_set or self.nhrpserverstattxregisternakalreadyreg.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxregisternakalreadyreg.get_name_leafdata())
                if (self.nhrpserverstattxregisternakinsufresources.is_set or self.nhrpserverstattxregisternakinsufresources.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxregisternakinsufresources.get_name_leafdata())
                if (self.nhrpserverstattxregisternakprohibited.is_set or self.nhrpserverstattxregisternakprohibited.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxregisternakprohibited.get_name_leafdata())
                if (self.nhrpserverstattxresolvereplyack.is_set or self.nhrpserverstattxresolvereplyack.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxresolvereplyack.get_name_leafdata())
                if (self.nhrpserverstattxresolvereplynakinsufresources.is_set or self.nhrpserverstattxresolvereplynakinsufresources.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxresolvereplynakinsufresources.get_name_leafdata())
                if (self.nhrpserverstattxresolvereplynaknobinding.is_set or self.nhrpserverstattxresolvereplynaknobinding.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxresolvereplynaknobinding.get_name_leafdata())
                if (self.nhrpserverstattxresolvereplynaknotunique.is_set or self.nhrpserverstattxresolvereplynaknotunique.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxresolvereplynaknotunique.get_name_leafdata())
                if (self.nhrpserverstattxresolvereplynakprohibited.is_set or self.nhrpserverstattxresolvereplynakprohibited.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.nhrpserverstattxresolvereplynakprohibited.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "nhrpServerIndex" or name == "nhrpServerStatDiscontinuityTime" or name == "nhrpServerStatFwErrorIndication" or name == "nhrpServerStatFwPurgeReply" or name == "nhrpServerStatFwPurgeReq" or name == "nhrpServerStatFwRegisterReply" or name == "nhrpServerStatFwRegisterReq" or name == "nhrpServerStatFwResolveReply" or name == "nhrpServerStatFwResolveReq" or name == "nhrpServerStatRxErrAuthenticationFailure" or name == "nhrpServerStatRxErrHopCountExceeded" or name == "nhrpServerStatRxErrInvalidExtension" or name == "nhrpServerStatRxErrInvalidResReplyReceived" or name == "nhrpServerStatRxErrLoopDetected" or name == "nhrpServerStatRxErrProtoAddrUnreachable" or name == "nhrpServerStatRxErrProtoError" or name == "nhrpServerStatRxErrSduSizeExceeded" or name == "nhrpServerStatRxErrUnrecognizedExtension" or name == "nhrpServerStatRxPurgeReply" or name == "nhrpServerStatRxPurgeReq" or name == "nhrpServerStatRxRegisterReq" or name == "nhrpServerStatRxResolveReq" or name == "nhrpServerStatTxErrAuthenticationFailure" or name == "nhrpServerStatTxErrHopCountExceeded" or name == "nhrpServerStatTxErrInvalidExtension" or name == "nhrpServerStatTxErrLoopDetected" or name == "nhrpServerStatTxErrProtoAddrUnreachable" or name == "nhrpServerStatTxErrProtoError" or name == "nhrpServerStatTxErrSduSizeExceeded" or name == "nhrpServerStatTxErrUnrecognizedExtension" or name == "nhrpServerStatTxPurgeReply" or name == "nhrpServerStatTxPurgeReq" or name == "nhrpServerStatTxRegisterAck" or name == "nhrpServerStatTxRegisterNakAlreadyReg" or name == "nhrpServerStatTxRegisterNakInsufResources" or name == "nhrpServerStatTxRegisterNakProhibited" or name == "nhrpServerStatTxResolveReplyAck" or name == "nhrpServerStatTxResolveReplyNakInsufResources" or name == "nhrpServerStatTxResolveReplyNakNoBinding" or name == "nhrpServerStatTxResolveReplyNakNotUnique" or name == "nhrpServerStatTxResolveReplyNakProhibited"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "nhrpServerIndex"):
                    self.nhrpserverindex = value
                    self.nhrpserverindex.value_namespace = name_space
                    self.nhrpserverindex.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatDiscontinuityTime"):
                    self.nhrpserverstatdiscontinuitytime = value
                    self.nhrpserverstatdiscontinuitytime.value_namespace = name_space
                    self.nhrpserverstatdiscontinuitytime.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatFwErrorIndication"):
                    self.nhrpserverstatfwerrorindication = value
                    self.nhrpserverstatfwerrorindication.value_namespace = name_space
                    self.nhrpserverstatfwerrorindication.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatFwPurgeReply"):
                    self.nhrpserverstatfwpurgereply = value
                    self.nhrpserverstatfwpurgereply.value_namespace = name_space
                    self.nhrpserverstatfwpurgereply.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatFwPurgeReq"):
                    self.nhrpserverstatfwpurgereq = value
                    self.nhrpserverstatfwpurgereq.value_namespace = name_space
                    self.nhrpserverstatfwpurgereq.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatFwRegisterReply"):
                    self.nhrpserverstatfwregisterreply = value
                    self.nhrpserverstatfwregisterreply.value_namespace = name_space
                    self.nhrpserverstatfwregisterreply.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatFwRegisterReq"):
                    self.nhrpserverstatfwregisterreq = value
                    self.nhrpserverstatfwregisterreq.value_namespace = name_space
                    self.nhrpserverstatfwregisterreq.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatFwResolveReply"):
                    self.nhrpserverstatfwresolvereply = value
                    self.nhrpserverstatfwresolvereply.value_namespace = name_space
                    self.nhrpserverstatfwresolvereply.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatFwResolveReq"):
                    self.nhrpserverstatfwresolvereq = value
                    self.nhrpserverstatfwresolvereq.value_namespace = name_space
                    self.nhrpserverstatfwresolvereq.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatRxErrAuthenticationFailure"):
                    self.nhrpserverstatrxerrauthenticationfailure = value
                    self.nhrpserverstatrxerrauthenticationfailure.value_namespace = name_space
                    self.nhrpserverstatrxerrauthenticationfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatRxErrHopCountExceeded"):
                    self.nhrpserverstatrxerrhopcountexceeded = value
                    self.nhrpserverstatrxerrhopcountexceeded.value_namespace = name_space
                    self.nhrpserverstatrxerrhopcountexceeded.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatRxErrInvalidExtension"):
                    self.nhrpserverstatrxerrinvalidextension = value
                    self.nhrpserverstatrxerrinvalidextension.value_namespace = name_space
                    self.nhrpserverstatrxerrinvalidextension.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatRxErrInvalidResReplyReceived"):
                    self.nhrpserverstatrxerrinvalidresreplyreceived = value
                    self.nhrpserverstatrxerrinvalidresreplyreceived.value_namespace = name_space
                    self.nhrpserverstatrxerrinvalidresreplyreceived.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatRxErrLoopDetected"):
                    self.nhrpserverstatrxerrloopdetected = value
                    self.nhrpserverstatrxerrloopdetected.value_namespace = name_space
                    self.nhrpserverstatrxerrloopdetected.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatRxErrProtoAddrUnreachable"):
                    self.nhrpserverstatrxerrprotoaddrunreachable = value
                    self.nhrpserverstatrxerrprotoaddrunreachable.value_namespace = name_space
                    self.nhrpserverstatrxerrprotoaddrunreachable.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatRxErrProtoError"):
                    self.nhrpserverstatrxerrprotoerror = value
                    self.nhrpserverstatrxerrprotoerror.value_namespace = name_space
                    self.nhrpserverstatrxerrprotoerror.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatRxErrSduSizeExceeded"):
                    self.nhrpserverstatrxerrsdusizeexceeded = value
                    self.nhrpserverstatrxerrsdusizeexceeded.value_namespace = name_space
                    self.nhrpserverstatrxerrsdusizeexceeded.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatRxErrUnrecognizedExtension"):
                    self.nhrpserverstatrxerrunrecognizedextension = value
                    self.nhrpserverstatrxerrunrecognizedextension.value_namespace = name_space
                    self.nhrpserverstatrxerrunrecognizedextension.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatRxPurgeReply"):
                    self.nhrpserverstatrxpurgereply = value
                    self.nhrpserverstatrxpurgereply.value_namespace = name_space
                    self.nhrpserverstatrxpurgereply.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatRxPurgeReq"):
                    self.nhrpserverstatrxpurgereq = value
                    self.nhrpserverstatrxpurgereq.value_namespace = name_space
                    self.nhrpserverstatrxpurgereq.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatRxRegisterReq"):
                    self.nhrpserverstatrxregisterreq = value
                    self.nhrpserverstatrxregisterreq.value_namespace = name_space
                    self.nhrpserverstatrxregisterreq.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatRxResolveReq"):
                    self.nhrpserverstatrxresolvereq = value
                    self.nhrpserverstatrxresolvereq.value_namespace = name_space
                    self.nhrpserverstatrxresolvereq.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxErrAuthenticationFailure"):
                    self.nhrpserverstattxerrauthenticationfailure = value
                    self.nhrpserverstattxerrauthenticationfailure.value_namespace = name_space
                    self.nhrpserverstattxerrauthenticationfailure.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxErrHopCountExceeded"):
                    self.nhrpserverstattxerrhopcountexceeded = value
                    self.nhrpserverstattxerrhopcountexceeded.value_namespace = name_space
                    self.nhrpserverstattxerrhopcountexceeded.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxErrInvalidExtension"):
                    self.nhrpserverstattxerrinvalidextension = value
                    self.nhrpserverstattxerrinvalidextension.value_namespace = name_space
                    self.nhrpserverstattxerrinvalidextension.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxErrLoopDetected"):
                    self.nhrpserverstattxerrloopdetected = value
                    self.nhrpserverstattxerrloopdetected.value_namespace = name_space
                    self.nhrpserverstattxerrloopdetected.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxErrProtoAddrUnreachable"):
                    self.nhrpserverstattxerrprotoaddrunreachable = value
                    self.nhrpserverstattxerrprotoaddrunreachable.value_namespace = name_space
                    self.nhrpserverstattxerrprotoaddrunreachable.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxErrProtoError"):
                    self.nhrpserverstattxerrprotoerror = value
                    self.nhrpserverstattxerrprotoerror.value_namespace = name_space
                    self.nhrpserverstattxerrprotoerror.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxErrSduSizeExceeded"):
                    self.nhrpserverstattxerrsdusizeexceeded = value
                    self.nhrpserverstattxerrsdusizeexceeded.value_namespace = name_space
                    self.nhrpserverstattxerrsdusizeexceeded.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxErrUnrecognizedExtension"):
                    self.nhrpserverstattxerrunrecognizedextension = value
                    self.nhrpserverstattxerrunrecognizedextension.value_namespace = name_space
                    self.nhrpserverstattxerrunrecognizedextension.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxPurgeReply"):
                    self.nhrpserverstattxpurgereply = value
                    self.nhrpserverstattxpurgereply.value_namespace = name_space
                    self.nhrpserverstattxpurgereply.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxPurgeReq"):
                    self.nhrpserverstattxpurgereq = value
                    self.nhrpserverstattxpurgereq.value_namespace = name_space
                    self.nhrpserverstattxpurgereq.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxRegisterAck"):
                    self.nhrpserverstattxregisterack = value
                    self.nhrpserverstattxregisterack.value_namespace = name_space
                    self.nhrpserverstattxregisterack.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxRegisterNakAlreadyReg"):
                    self.nhrpserverstattxregisternakalreadyreg = value
                    self.nhrpserverstattxregisternakalreadyreg.value_namespace = name_space
                    self.nhrpserverstattxregisternakalreadyreg.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxRegisterNakInsufResources"):
                    self.nhrpserverstattxregisternakinsufresources = value
                    self.nhrpserverstattxregisternakinsufresources.value_namespace = name_space
                    self.nhrpserverstattxregisternakinsufresources.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxRegisterNakProhibited"):
                    self.nhrpserverstattxregisternakprohibited = value
                    self.nhrpserverstattxregisternakprohibited.value_namespace = name_space
                    self.nhrpserverstattxregisternakprohibited.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxResolveReplyAck"):
                    self.nhrpserverstattxresolvereplyack = value
                    self.nhrpserverstattxresolvereplyack.value_namespace = name_space
                    self.nhrpserverstattxresolvereplyack.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxResolveReplyNakInsufResources"):
                    self.nhrpserverstattxresolvereplynakinsufresources = value
                    self.nhrpserverstattxresolvereplynakinsufresources.value_namespace = name_space
                    self.nhrpserverstattxresolvereplynakinsufresources.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxResolveReplyNakNoBinding"):
                    self.nhrpserverstattxresolvereplynaknobinding = value
                    self.nhrpserverstattxresolvereplynaknobinding.value_namespace = name_space
                    self.nhrpserverstattxresolvereplynaknobinding.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxResolveReplyNakNotUnique"):
                    self.nhrpserverstattxresolvereplynaknotunique = value
                    self.nhrpserverstattxresolvereplynaknotunique.value_namespace = name_space
                    self.nhrpserverstattxresolvereplynaknotunique.value_namespace_prefix = name_space_prefix
                if(value_path == "nhrpServerStatTxResolveReplyNakProhibited"):
                    self.nhrpserverstattxresolvereplynakprohibited = value
                    self.nhrpserverstattxresolvereplynakprohibited.value_namespace = name_space
                    self.nhrpserverstattxresolvereplynakprohibited.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.nhrpserverstatentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.nhrpserverstatentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nhrpServerStatTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "NHRP-MIB:NHRP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "nhrpServerStatEntry"):
                for c in self.nhrpserverstatentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = NhrpMib.Nhrpserverstattable.Nhrpserverstatentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.nhrpserverstatentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "nhrpServerStatEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.nhrpcachetable is not None and self.nhrpcachetable.has_data()) or
            (self.nhrpclientnhstable is not None and self.nhrpclientnhstable.has_data()) or
            (self.nhrpclientregistrationtable is not None and self.nhrpclientregistrationtable.has_data()) or
            (self.nhrpclientstattable is not None and self.nhrpclientstattable.has_data()) or
            (self.nhrpclienttable is not None and self.nhrpclienttable.has_data()) or
            (self.nhrpgeneralobjects is not None and self.nhrpgeneralobjects.has_data()) or
            (self.nhrppurgereqtable is not None and self.nhrppurgereqtable.has_data()) or
            (self.nhrpservercachetable is not None and self.nhrpservercachetable.has_data()) or
            (self.nhrpservernhctable is not None and self.nhrpservernhctable.has_data()) or
            (self.nhrpserverstattable is not None and self.nhrpserverstattable.has_data()) or
            (self.nhrpservertable is not None and self.nhrpservertable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.nhrpcachetable is not None and self.nhrpcachetable.has_operation()) or
            (self.nhrpclientnhstable is not None and self.nhrpclientnhstable.has_operation()) or
            (self.nhrpclientregistrationtable is not None and self.nhrpclientregistrationtable.has_operation()) or
            (self.nhrpclientstattable is not None and self.nhrpclientstattable.has_operation()) or
            (self.nhrpclienttable is not None and self.nhrpclienttable.has_operation()) or
            (self.nhrpgeneralobjects is not None and self.nhrpgeneralobjects.has_operation()) or
            (self.nhrppurgereqtable is not None and self.nhrppurgereqtable.has_operation()) or
            (self.nhrpservercachetable is not None and self.nhrpservercachetable.has_operation()) or
            (self.nhrpservernhctable is not None and self.nhrpservernhctable.has_operation()) or
            (self.nhrpserverstattable is not None and self.nhrpserverstattable.has_operation()) or
            (self.nhrpservertable is not None and self.nhrpservertable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "NHRP-MIB:NHRP-MIB" + path_buffer

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

        if (child_yang_name == "nhrpCacheTable"):
            if (self.nhrpcachetable is None):
                self.nhrpcachetable = NhrpMib.Nhrpcachetable()
                self.nhrpcachetable.parent = self
                self._children_name_map["nhrpcachetable"] = "nhrpCacheTable"
            return self.nhrpcachetable

        if (child_yang_name == "nhrpClientNhsTable"):
            if (self.nhrpclientnhstable is None):
                self.nhrpclientnhstable = NhrpMib.Nhrpclientnhstable()
                self.nhrpclientnhstable.parent = self
                self._children_name_map["nhrpclientnhstable"] = "nhrpClientNhsTable"
            return self.nhrpclientnhstable

        if (child_yang_name == "nhrpClientRegistrationTable"):
            if (self.nhrpclientregistrationtable is None):
                self.nhrpclientregistrationtable = NhrpMib.Nhrpclientregistrationtable()
                self.nhrpclientregistrationtable.parent = self
                self._children_name_map["nhrpclientregistrationtable"] = "nhrpClientRegistrationTable"
            return self.nhrpclientregistrationtable

        if (child_yang_name == "nhrpClientStatTable"):
            if (self.nhrpclientstattable is None):
                self.nhrpclientstattable = NhrpMib.Nhrpclientstattable()
                self.nhrpclientstattable.parent = self
                self._children_name_map["nhrpclientstattable"] = "nhrpClientStatTable"
            return self.nhrpclientstattable

        if (child_yang_name == "nhrpClientTable"):
            if (self.nhrpclienttable is None):
                self.nhrpclienttable = NhrpMib.Nhrpclienttable()
                self.nhrpclienttable.parent = self
                self._children_name_map["nhrpclienttable"] = "nhrpClientTable"
            return self.nhrpclienttable

        if (child_yang_name == "nhrpGeneralObjects"):
            if (self.nhrpgeneralobjects is None):
                self.nhrpgeneralobjects = NhrpMib.Nhrpgeneralobjects()
                self.nhrpgeneralobjects.parent = self
                self._children_name_map["nhrpgeneralobjects"] = "nhrpGeneralObjects"
            return self.nhrpgeneralobjects

        if (child_yang_name == "nhrpPurgeReqTable"):
            if (self.nhrppurgereqtable is None):
                self.nhrppurgereqtable = NhrpMib.Nhrppurgereqtable()
                self.nhrppurgereqtable.parent = self
                self._children_name_map["nhrppurgereqtable"] = "nhrpPurgeReqTable"
            return self.nhrppurgereqtable

        if (child_yang_name == "nhrpServerCacheTable"):
            if (self.nhrpservercachetable is None):
                self.nhrpservercachetable = NhrpMib.Nhrpservercachetable()
                self.nhrpservercachetable.parent = self
                self._children_name_map["nhrpservercachetable"] = "nhrpServerCacheTable"
            return self.nhrpservercachetable

        if (child_yang_name == "nhrpServerNhcTable"):
            if (self.nhrpservernhctable is None):
                self.nhrpservernhctable = NhrpMib.Nhrpservernhctable()
                self.nhrpservernhctable.parent = self
                self._children_name_map["nhrpservernhctable"] = "nhrpServerNhcTable"
            return self.nhrpservernhctable

        if (child_yang_name == "nhrpServerStatTable"):
            if (self.nhrpserverstattable is None):
                self.nhrpserverstattable = NhrpMib.Nhrpserverstattable()
                self.nhrpserverstattable.parent = self
                self._children_name_map["nhrpserverstattable"] = "nhrpServerStatTable"
            return self.nhrpserverstattable

        if (child_yang_name == "nhrpServerTable"):
            if (self.nhrpservertable is None):
                self.nhrpservertable = NhrpMib.Nhrpservertable()
                self.nhrpservertable.parent = self
                self._children_name_map["nhrpservertable"] = "nhrpServerTable"
            return self.nhrpservertable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "nhrpCacheTable" or name == "nhrpClientNhsTable" or name == "nhrpClientRegistrationTable" or name == "nhrpClientStatTable" or name == "nhrpClientTable" or name == "nhrpGeneralObjects" or name == "nhrpPurgeReqTable" or name == "nhrpServerCacheTable" or name == "nhrpServerNhcTable" or name == "nhrpServerStatTable" or name == "nhrpServerTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = NhrpMib()
        return self._top_entity

