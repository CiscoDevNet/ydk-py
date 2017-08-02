""" CISCO_AAA_SESSION_MIB 

This MIB module provides data for accounting sessions
based on Authentication, Authorization, Accounting
(AAA) protocols.


References\:
    RFC 2139 RADIUS Accounting
    The TACACS+ Protocol Version 1.78, Internet Draft

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoAaaSessionMib(Entity):
    """
    
    
    .. attribute:: casnactive
    
    	
    	**type**\:   :py:class:`Casnactive <ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB.CiscoAaaSessionMib.Casnactive>`
    
    .. attribute:: casnactivetable
    
    	This table contains entries for active AAA accounting sessions in the system
    	**type**\:   :py:class:`Casnactivetable <ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB.CiscoAaaSessionMib.Casnactivetable>`
    
    .. attribute:: casngeneral
    
    	
    	**type**\:   :py:class:`Casngeneral <ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB.CiscoAaaSessionMib.Casngeneral>`
    
    

    """

    _prefix = 'CISCO-AAA-SESSION-MIB'
    _revision = '2006-03-21'

    def __init__(self):
        super(CiscoAaaSessionMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-AAA-SESSION-MIB"
        self.yang_parent_name = "CISCO-AAA-SESSION-MIB"

        self.casnactive = CiscoAaaSessionMib.Casnactive()
        self.casnactive.parent = self
        self._children_name_map["casnactive"] = "casnActive"
        self._children_yang_names.add("casnActive")

        self.casnactivetable = CiscoAaaSessionMib.Casnactivetable()
        self.casnactivetable.parent = self
        self._children_name_map["casnactivetable"] = "casnActiveTable"
        self._children_yang_names.add("casnActiveTable")

        self.casngeneral = CiscoAaaSessionMib.Casngeneral()
        self.casngeneral.parent = self
        self._children_name_map["casngeneral"] = "casnGeneral"
        self._children_yang_names.add("casnGeneral")


    class Casnactive(Entity):
        """
        
        
        .. attribute:: casnactivetableentries
        
        	Number of entries currently in casnActiveTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: casnactivetablehighwatermark
        
        	Maximum number of entries present in casnActiveTable since last system re\-initialization.  This corresponds to the maximum value reported by casnActiveTableEntries
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-AAA-SESSION-MIB'
        _revision = '2006-03-21'

        def __init__(self):
            super(CiscoAaaSessionMib.Casnactive, self).__init__()

            self.yang_name = "casnActive"
            self.yang_parent_name = "CISCO-AAA-SESSION-MIB"

            self.casnactivetableentries = YLeaf(YType.uint32, "casnActiveTableEntries")

            self.casnactivetablehighwatermark = YLeaf(YType.uint32, "casnActiveTableHighWaterMark")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("casnactivetableentries",
                            "casnactivetablehighwatermark") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoAaaSessionMib.Casnactive, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAaaSessionMib.Casnactive, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.casnactivetableentries.is_set or
                self.casnactivetablehighwatermark.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.casnactivetableentries.yfilter != YFilter.not_set or
                self.casnactivetablehighwatermark.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "casnActive" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-AAA-SESSION-MIB:CISCO-AAA-SESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.casnactivetableentries.is_set or self.casnactivetableentries.yfilter != YFilter.not_set):
                leaf_name_data.append(self.casnactivetableentries.get_name_leafdata())
            if (self.casnactivetablehighwatermark.is_set or self.casnactivetablehighwatermark.yfilter != YFilter.not_set):
                leaf_name_data.append(self.casnactivetablehighwatermark.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "casnActiveTableEntries" or name == "casnActiveTableHighWaterMark"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "casnActiveTableEntries"):
                self.casnactivetableentries = value
                self.casnactivetableentries.value_namespace = name_space
                self.casnactivetableentries.value_namespace_prefix = name_space_prefix
            if(value_path == "casnActiveTableHighWaterMark"):
                self.casnactivetablehighwatermark = value
                self.casnactivetablehighwatermark.value_namespace = name_space
                self.casnactivetablehighwatermark.value_namespace_prefix = name_space_prefix


    class Casngeneral(Entity):
        """
        
        
        .. attribute:: casndisconnectedsessions
        
        	Total number of sessions which have been disconnected using casnDisconnect since last system re\-initialization.  This value includes any sessions still in the casnActiveTable with a casnDisconnect value of true(1) and all previous sessions which terminated as a result of setting casnDisconnect
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: casntotalsessions
        
        	Total number of sessions since last system re\-initialization.  This value includes all sessions currently in the casnActiveTable and all previous sessions whether terminated via casnDisconnect or via other mechanisms
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'CISCO-AAA-SESSION-MIB'
        _revision = '2006-03-21'

        def __init__(self):
            super(CiscoAaaSessionMib.Casngeneral, self).__init__()

            self.yang_name = "casnGeneral"
            self.yang_parent_name = "CISCO-AAA-SESSION-MIB"

            self.casndisconnectedsessions = YLeaf(YType.uint32, "casnDisconnectedSessions")

            self.casntotalsessions = YLeaf(YType.uint32, "casnTotalSessions")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("casndisconnectedsessions",
                            "casntotalsessions") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoAaaSessionMib.Casngeneral, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAaaSessionMib.Casngeneral, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.casndisconnectedsessions.is_set or
                self.casntotalsessions.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.casndisconnectedsessions.yfilter != YFilter.not_set or
                self.casntotalsessions.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "casnGeneral" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-AAA-SESSION-MIB:CISCO-AAA-SESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.casndisconnectedsessions.is_set or self.casndisconnectedsessions.yfilter != YFilter.not_set):
                leaf_name_data.append(self.casndisconnectedsessions.get_name_leafdata())
            if (self.casntotalsessions.is_set or self.casntotalsessions.yfilter != YFilter.not_set):
                leaf_name_data.append(self.casntotalsessions.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "casnDisconnectedSessions" or name == "casnTotalSessions"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "casnDisconnectedSessions"):
                self.casndisconnectedsessions = value
                self.casndisconnectedsessions.value_namespace = name_space
                self.casndisconnectedsessions.value_namespace_prefix = name_space_prefix
            if(value_path == "casnTotalSessions"):
                self.casntotalsessions = value
                self.casntotalsessions.value_namespace = name_space
                self.casntotalsessions.value_namespace_prefix = name_space_prefix


    class Casnactivetable(Entity):
        """
        This table contains entries for active AAA accounting
        sessions in the system.
        
        .. attribute:: casnactiveentry
        
        	The information regarding a single accounting session.  Entries are created when a new accounting session is begun.  Entries are removed when the accounting session is ended.  Initiating termination of a session with the object casnDisconnect will cause removal of the entry when the session completes termination
        	**type**\: list of    :py:class:`Casnactiveentry <ydk.models.cisco_ios_xe.CISCO_AAA_SESSION_MIB.CiscoAaaSessionMib.Casnactivetable.Casnactiveentry>`
        
        

        """

        _prefix = 'CISCO-AAA-SESSION-MIB'
        _revision = '2006-03-21'

        def __init__(self):
            super(CiscoAaaSessionMib.Casnactivetable, self).__init__()

            self.yang_name = "casnActiveTable"
            self.yang_parent_name = "CISCO-AAA-SESSION-MIB"

            self.casnactiveentry = YList(self)

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
                        super(CiscoAaaSessionMib.Casnactivetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoAaaSessionMib.Casnactivetable, self).__setattr__(name, value)


        class Casnactiveentry(Entity):
            """
            The information regarding a single accounting session.
            
            Entries are created when a new accounting session
            is begun.
            
            Entries are removed when the accounting session
            is ended.
            
            Initiating termination of a session with the object
            casnDisconnect will cause removal of the entry when
            the session completes termination.
            
            .. attribute:: casnsessionid  <key>
            
            	This is the session identification used by the accounting protocol.  This value is unique to a session within the system, even if multiple accounting protocols are in use.  The value of this object corresponds to these accounting protocol attributes.    RADIUS\:  attribute 44, Acct\-Session\-Id    TACACS+\: attribute 'task\_id'
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: casncalltrackerid
            
            	The value of this object is the entry index in the CISCO\-CALL\-TRACKER\-MIB cctActiveTable of the call corresponding to this accounting session.  Using the value of this object to query the cctActiveTable will provide more detailed data regarding the session represented by this casnActiveEntry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: casndisconnect
            
            	This object is used to terminate this session.  Setting the value to true(1) will initiate termination of this session.  The entry will be removed once the session has completed termination.  Once this object has been set to true(1), the session termination process can not be cancelled by setting the value false(2)
            	**type**\:  bool
            
            .. attribute:: casnidletime
            
            	The elapsed time that this session has been idle.  This is the time since the last user\-level data has been received or transmitted. Protocol level handshaking associated with the call is considered to be idle for this object
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: casnipaddr
            
            	The IP address of the session or 0.0.0.0 if not applicable or unavailable.  RADIUS\:  attribute 8, Framed\-IP\-Address TACACS+\: attribute 'addr'
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: casnnasport
            
            	The value of this object identifies a particular conceptual row associated with the session identified by casnSessionId.  The conceptual row that this object points to represents a port that is used to transport a session.  If the port transporting the session cannot be determined, the value of this object will be zeroDotZero.  For example, suppose a session is established using an ATM PVC.  If the ifIndex of the ATM interface is 7, and the  VPI/VCI values of the PVC are 1, 100 respectively, then the value of this object might be as follows\:         casnNasPort.15 = atmVclAdminStatus.7.1.100                    ^                      ^ ^  ^                    \|                      \| \|  \|    casnSessionId \-\-+                      \| \|  \|          ifIndex \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+ \|  \|        atmVclVpi \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+  \|        atmVclVci \-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-+  where atmVclAdminStatus is the first accessible object of the atmVclTable of the ATM\-MIB
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: casnuserid
            
            	The User login ID or zero length string if unavailable.  The value of this object corresponds to these accounting protocol attributes.    RADIUS\:  attribute 1, User\-Name    TACACS+\: attribute 'user'
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: casnvaiifindex
            
            	The ifIndex of the Virtual Access Interface (VAI) that is associated with the PPP session.  This interface may not be represented in the IF\-MIB in which case the value of this object will be zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-AAA-SESSION-MIB'
            _revision = '2006-03-21'

            def __init__(self):
                super(CiscoAaaSessionMib.Casnactivetable.Casnactiveentry, self).__init__()

                self.yang_name = "casnActiveEntry"
                self.yang_parent_name = "casnActiveTable"

                self.casnsessionid = YLeaf(YType.uint32, "casnSessionId")

                self.casncalltrackerid = YLeaf(YType.uint32, "casnCallTrackerId")

                self.casndisconnect = YLeaf(YType.boolean, "casnDisconnect")

                self.casnidletime = YLeaf(YType.uint32, "casnIdleTime")

                self.casnipaddr = YLeaf(YType.str, "casnIpAddr")

                self.casnnasport = YLeaf(YType.str, "casnNasPort")

                self.casnuserid = YLeaf(YType.str, "casnUserId")

                self.casnvaiifindex = YLeaf(YType.int32, "casnVaiIfIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("casnsessionid",
                                "casncalltrackerid",
                                "casndisconnect",
                                "casnidletime",
                                "casnipaddr",
                                "casnnasport",
                                "casnuserid",
                                "casnvaiifindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoAaaSessionMib.Casnactivetable.Casnactiveentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoAaaSessionMib.Casnactivetable.Casnactiveentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.casnsessionid.is_set or
                    self.casncalltrackerid.is_set or
                    self.casndisconnect.is_set or
                    self.casnidletime.is_set or
                    self.casnipaddr.is_set or
                    self.casnnasport.is_set or
                    self.casnuserid.is_set or
                    self.casnvaiifindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.casnsessionid.yfilter != YFilter.not_set or
                    self.casncalltrackerid.yfilter != YFilter.not_set or
                    self.casndisconnect.yfilter != YFilter.not_set or
                    self.casnidletime.yfilter != YFilter.not_set or
                    self.casnipaddr.yfilter != YFilter.not_set or
                    self.casnnasport.yfilter != YFilter.not_set or
                    self.casnuserid.yfilter != YFilter.not_set or
                    self.casnvaiifindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "casnActiveEntry" + "[casnSessionId='" + self.casnsessionid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-AAA-SESSION-MIB:CISCO-AAA-SESSION-MIB/casnActiveTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.casnsessionid.is_set or self.casnsessionid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casnsessionid.get_name_leafdata())
                if (self.casncalltrackerid.is_set or self.casncalltrackerid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casncalltrackerid.get_name_leafdata())
                if (self.casndisconnect.is_set or self.casndisconnect.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casndisconnect.get_name_leafdata())
                if (self.casnidletime.is_set or self.casnidletime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casnidletime.get_name_leafdata())
                if (self.casnipaddr.is_set or self.casnipaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casnipaddr.get_name_leafdata())
                if (self.casnnasport.is_set or self.casnnasport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casnnasport.get_name_leafdata())
                if (self.casnuserid.is_set or self.casnuserid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casnuserid.get_name_leafdata())
                if (self.casnvaiifindex.is_set or self.casnvaiifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.casnvaiifindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "casnSessionId" or name == "casnCallTrackerId" or name == "casnDisconnect" or name == "casnIdleTime" or name == "casnIpAddr" or name == "casnNasPort" or name == "casnUserId" or name == "casnVaiIfIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "casnSessionId"):
                    self.casnsessionid = value
                    self.casnsessionid.value_namespace = name_space
                    self.casnsessionid.value_namespace_prefix = name_space_prefix
                if(value_path == "casnCallTrackerId"):
                    self.casncalltrackerid = value
                    self.casncalltrackerid.value_namespace = name_space
                    self.casncalltrackerid.value_namespace_prefix = name_space_prefix
                if(value_path == "casnDisconnect"):
                    self.casndisconnect = value
                    self.casndisconnect.value_namespace = name_space
                    self.casndisconnect.value_namespace_prefix = name_space_prefix
                if(value_path == "casnIdleTime"):
                    self.casnidletime = value
                    self.casnidletime.value_namespace = name_space
                    self.casnidletime.value_namespace_prefix = name_space_prefix
                if(value_path == "casnIpAddr"):
                    self.casnipaddr = value
                    self.casnipaddr.value_namespace = name_space
                    self.casnipaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "casnNasPort"):
                    self.casnnasport = value
                    self.casnnasport.value_namespace = name_space
                    self.casnnasport.value_namespace_prefix = name_space_prefix
                if(value_path == "casnUserId"):
                    self.casnuserid = value
                    self.casnuserid.value_namespace = name_space
                    self.casnuserid.value_namespace_prefix = name_space_prefix
                if(value_path == "casnVaiIfIndex"):
                    self.casnvaiifindex = value
                    self.casnvaiifindex.value_namespace = name_space
                    self.casnvaiifindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.casnactiveentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.casnactiveentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "casnActiveTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-AAA-SESSION-MIB:CISCO-AAA-SESSION-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "casnActiveEntry"):
                for c in self.casnactiveentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoAaaSessionMib.Casnactivetable.Casnactiveentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.casnactiveentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "casnActiveEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.casnactive is not None and self.casnactive.has_data()) or
            (self.casnactivetable is not None and self.casnactivetable.has_data()) or
            (self.casngeneral is not None and self.casngeneral.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.casnactive is not None and self.casnactive.has_operation()) or
            (self.casnactivetable is not None and self.casnactivetable.has_operation()) or
            (self.casngeneral is not None and self.casngeneral.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-AAA-SESSION-MIB:CISCO-AAA-SESSION-MIB" + path_buffer

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

        if (child_yang_name == "casnActive"):
            if (self.casnactive is None):
                self.casnactive = CiscoAaaSessionMib.Casnactive()
                self.casnactive.parent = self
                self._children_name_map["casnactive"] = "casnActive"
            return self.casnactive

        if (child_yang_name == "casnActiveTable"):
            if (self.casnactivetable is None):
                self.casnactivetable = CiscoAaaSessionMib.Casnactivetable()
                self.casnactivetable.parent = self
                self._children_name_map["casnactivetable"] = "casnActiveTable"
            return self.casnactivetable

        if (child_yang_name == "casnGeneral"):
            if (self.casngeneral is None):
                self.casngeneral = CiscoAaaSessionMib.Casngeneral()
                self.casngeneral.parent = self
                self._children_name_map["casngeneral"] = "casnGeneral"
            return self.casngeneral

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "casnActive" or name == "casnActiveTable" or name == "casnGeneral"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoAaaSessionMib()
        return self._top_entity

