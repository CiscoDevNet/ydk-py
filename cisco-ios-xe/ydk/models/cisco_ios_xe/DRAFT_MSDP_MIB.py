""" DRAFT_MSDP_MIB 

An experimental MIB module for MSDP Management.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DraftMsdpMib(Entity):
    """
    
    
    .. attribute:: msdp
    
    	
    	**type**\:   :py:class:`Msdp <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdp>`
    
    .. attribute:: msdppeertable
    
    	The (conceptual) table listing the MSDP speaker's peers
    	**type**\:   :py:class:`Msdppeertable <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdppeertable>`
    
    .. attribute:: msdprequeststable
    
    	The (conceptual) table listing group ranges and MSDP peers used when deciding where to send an SA Request message when required.  If SA Caching is enabled, this table may be empty
    	**type**\:   :py:class:`Msdprequeststable <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdprequeststable>`
    
    .. attribute:: msdpsacachetable
    
    	The (conceptual) table listing the MSDP SA advertisements currently in the MSDP speaker's cache
    	**type**\:   :py:class:`Msdpsacachetable <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdpsacachetable>`
    
    

    """

    _prefix = 'DRAFT-MSDP-MIB'
    _revision = '1999-12-16'

    def __init__(self):
        super(DraftMsdpMib, self).__init__()
        self._top_entity = None

        self.yang_name = "DRAFT-MSDP-MIB"
        self.yang_parent_name = "DRAFT-MSDP-MIB"

        self.msdp = DraftMsdpMib.Msdp()
        self.msdp.parent = self
        self._children_name_map["msdp"] = "msdp"
        self._children_yang_names.add("msdp")

        self.msdppeertable = DraftMsdpMib.Msdppeertable()
        self.msdppeertable.parent = self
        self._children_name_map["msdppeertable"] = "msdpPeerTable"
        self._children_yang_names.add("msdpPeerTable")

        self.msdprequeststable = DraftMsdpMib.Msdprequeststable()
        self.msdprequeststable.parent = self
        self._children_name_map["msdprequeststable"] = "msdpRequestsTable"
        self._children_yang_names.add("msdpRequestsTable")

        self.msdpsacachetable = DraftMsdpMib.Msdpsacachetable()
        self.msdpsacachetable.parent = self
        self._children_name_map["msdpsacachetable"] = "msdpSACacheTable"
        self._children_yang_names.add("msdpSACacheTable")


    class Msdp(Entity):
        """
        
        
        .. attribute:: msdpcachelifetime
        
        	The lifetime given to SA cache entries when created or refreshed.  A value of 0 means no SA caching is done by this MSDP speaker
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: msdpenabled
        
        	The state of MSDP on this MSDP speaker \- globally enabled or disabled
        	**type**\:  bool
        
        .. attribute:: msdpnumsacacheentries
        
        	The total number of entries in the SA Cache table
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: msdpsaholddownperiod
        
        	The number of seconds in the MSDP SA Hold\-down period
        	**type**\:  int
        
        	**range:** 1..2147483647
        
        	**units**\: seconds
        
        

        """

        _prefix = 'DRAFT-MSDP-MIB'
        _revision = '1999-12-16'

        def __init__(self):
            super(DraftMsdpMib.Msdp, self).__init__()

            self.yang_name = "msdp"
            self.yang_parent_name = "DRAFT-MSDP-MIB"

            self.msdpcachelifetime = YLeaf(YType.uint32, "msdpCacheLifetime")

            self.msdpenabled = YLeaf(YType.boolean, "msdpEnabled")

            self.msdpnumsacacheentries = YLeaf(YType.uint32, "msdpNumSACacheEntries")

            self.msdpsaholddownperiod = YLeaf(YType.int32, "msdpSAHoldDownPeriod")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("msdpcachelifetime",
                            "msdpenabled",
                            "msdpnumsacacheentries",
                            "msdpsaholddownperiod") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(DraftMsdpMib.Msdp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DraftMsdpMib.Msdp, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.msdpcachelifetime.is_set or
                self.msdpenabled.is_set or
                self.msdpnumsacacheentries.is_set or
                self.msdpsaholddownperiod.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.msdpcachelifetime.yfilter != YFilter.not_set or
                self.msdpenabled.yfilter != YFilter.not_set or
                self.msdpnumsacacheentries.yfilter != YFilter.not_set or
                self.msdpsaholddownperiod.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "msdp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.msdpcachelifetime.is_set or self.msdpcachelifetime.yfilter != YFilter.not_set):
                leaf_name_data.append(self.msdpcachelifetime.get_name_leafdata())
            if (self.msdpenabled.is_set or self.msdpenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.msdpenabled.get_name_leafdata())
            if (self.msdpnumsacacheentries.is_set or self.msdpnumsacacheentries.yfilter != YFilter.not_set):
                leaf_name_data.append(self.msdpnumsacacheentries.get_name_leafdata())
            if (self.msdpsaholddownperiod.is_set or self.msdpsaholddownperiod.yfilter != YFilter.not_set):
                leaf_name_data.append(self.msdpsaholddownperiod.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "msdpCacheLifetime" or name == "msdpEnabled" or name == "msdpNumSACacheEntries" or name == "msdpSAHoldDownPeriod"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "msdpCacheLifetime"):
                self.msdpcachelifetime = value
                self.msdpcachelifetime.value_namespace = name_space
                self.msdpcachelifetime.value_namespace_prefix = name_space_prefix
            if(value_path == "msdpEnabled"):
                self.msdpenabled = value
                self.msdpenabled.value_namespace = name_space
                self.msdpenabled.value_namespace_prefix = name_space_prefix
            if(value_path == "msdpNumSACacheEntries"):
                self.msdpnumsacacheentries = value
                self.msdpnumsacacheentries.value_namespace = name_space
                self.msdpnumsacacheentries.value_namespace_prefix = name_space_prefix
            if(value_path == "msdpSAHoldDownPeriod"):
                self.msdpsaholddownperiod = value
                self.msdpsaholddownperiod.value_namespace = name_space
                self.msdpsaholddownperiod.value_namespace_prefix = name_space_prefix


    class Msdprequeststable(Entity):
        """
        The (conceptual) table listing group ranges and MSDP
        peers used when deciding where to send an SA Request
        message when required.  If SA Caching is enabled, this
        table may be empty.
        
        .. attribute:: msdprequestsentry
        
        	An entry (conceptual row) representing a group range used when deciding where to send an SA Request message
        	**type**\: list of    :py:class:`Msdprequestsentry <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdprequeststable.Msdprequestsentry>`
        
        

        """

        _prefix = 'DRAFT-MSDP-MIB'
        _revision = '1999-12-16'

        def __init__(self):
            super(DraftMsdpMib.Msdprequeststable, self).__init__()

            self.yang_name = "msdpRequestsTable"
            self.yang_parent_name = "DRAFT-MSDP-MIB"

            self.msdprequestsentry = YList(self)

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
                        super(DraftMsdpMib.Msdprequeststable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DraftMsdpMib.Msdprequeststable, self).__setattr__(name, value)


        class Msdprequestsentry(Entity):
            """
            An entry (conceptual row) representing a group range
            used when deciding where to send an SA Request
            message.
            
            .. attribute:: msdprequestsgroupaddress  <key>
            
            	The group address that, when combined with the mask in this entry, represents the group range for which this peer will service MSDP SA Requests
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdprequestsgroupmask  <key>
            
            	The mask that, when combined with the group address in this entry, represents the group range for which this peer will service MSDP SA Requests
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdprequestspeer
            
            	The peer to which MSDP SA Requests for groups matching this entry's group range will be sent.  Must match the INDEX of a row in the msdpPeerTable
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdprequestsstatus
            
            	The status of this row, by which new rows may be added to the table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'DRAFT-MSDP-MIB'
            _revision = '1999-12-16'

            def __init__(self):
                super(DraftMsdpMib.Msdprequeststable.Msdprequestsentry, self).__init__()

                self.yang_name = "msdpRequestsEntry"
                self.yang_parent_name = "msdpRequestsTable"

                self.msdprequestsgroupaddress = YLeaf(YType.str, "msdpRequestsGroupAddress")

                self.msdprequestsgroupmask = YLeaf(YType.str, "msdpRequestsGroupMask")

                self.msdprequestspeer = YLeaf(YType.str, "msdpRequestsPeer")

                self.msdprequestsstatus = YLeaf(YType.enumeration, "msdpRequestsStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("msdprequestsgroupaddress",
                                "msdprequestsgroupmask",
                                "msdprequestspeer",
                                "msdprequestsstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DraftMsdpMib.Msdprequeststable.Msdprequestsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DraftMsdpMib.Msdprequeststable.Msdprequestsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.msdprequestsgroupaddress.is_set or
                    self.msdprequestsgroupmask.is_set or
                    self.msdprequestspeer.is_set or
                    self.msdprequestsstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.msdprequestsgroupaddress.yfilter != YFilter.not_set or
                    self.msdprequestsgroupmask.yfilter != YFilter.not_set or
                    self.msdprequestspeer.yfilter != YFilter.not_set or
                    self.msdprequestsstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "msdpRequestsEntry" + "[msdpRequestsGroupAddress='" + self.msdprequestsgroupaddress.get() + "']" + "[msdpRequestsGroupMask='" + self.msdprequestsgroupmask.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/msdpRequestsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.msdprequestsgroupaddress.is_set or self.msdprequestsgroupaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdprequestsgroupaddress.get_name_leafdata())
                if (self.msdprequestsgroupmask.is_set or self.msdprequestsgroupmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdprequestsgroupmask.get_name_leafdata())
                if (self.msdprequestspeer.is_set or self.msdprequestspeer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdprequestspeer.get_name_leafdata())
                if (self.msdprequestsstatus.is_set or self.msdprequestsstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdprequestsstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "msdpRequestsGroupAddress" or name == "msdpRequestsGroupMask" or name == "msdpRequestsPeer" or name == "msdpRequestsStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "msdpRequestsGroupAddress"):
                    self.msdprequestsgroupaddress = value
                    self.msdprequestsgroupaddress.value_namespace = name_space
                    self.msdprequestsgroupaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpRequestsGroupMask"):
                    self.msdprequestsgroupmask = value
                    self.msdprequestsgroupmask.value_namespace = name_space
                    self.msdprequestsgroupmask.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpRequestsPeer"):
                    self.msdprequestspeer = value
                    self.msdprequestspeer.value_namespace = name_space
                    self.msdprequestspeer.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpRequestsStatus"):
                    self.msdprequestsstatus = value
                    self.msdprequestsstatus.value_namespace = name_space
                    self.msdprequestsstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.msdprequestsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.msdprequestsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "msdpRequestsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "msdpRequestsEntry"):
                for c in self.msdprequestsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DraftMsdpMib.Msdprequeststable.Msdprequestsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.msdprequestsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "msdpRequestsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Msdppeertable(Entity):
        """
        The (conceptual) table listing the MSDP speaker's
        peers.
        
        .. attribute:: msdppeerentry
        
        	An entry (conceptual row) representing an MSDP peer
        	**type**\: list of    :py:class:`Msdppeerentry <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdppeertable.Msdppeerentry>`
        
        

        """

        _prefix = 'DRAFT-MSDP-MIB'
        _revision = '1999-12-16'

        def __init__(self):
            super(DraftMsdpMib.Msdppeertable, self).__init__()

            self.yang_name = "msdpPeerTable"
            self.yang_parent_name = "DRAFT-MSDP-MIB"

            self.msdppeerentry = YList(self)

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
                        super(DraftMsdpMib.Msdppeertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DraftMsdpMib.Msdppeertable, self).__setattr__(name, value)


        class Msdppeerentry(Entity):
            """
            An entry (conceptual row) representing an MSDP peer.
            
            .. attribute:: msdppeerremoteaddress  <key>
            
            	The address of the remote MSDP peer
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdppeerconnectionattempts
            
            	The number of times the state machine has transitioned from inactive to connecting
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerconnectretryinterval
            
            	Time interval in seconds for the ConnectRetry timer
            	**type**\:  int
            
            	**range:** 1..65535
            
            	**units**\: seconds
            
            .. attribute:: msdppeerdatattl
            
            	The minimum TTL a packet is required to have before it may be forwarded using SA encapsulation to this peer
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: msdppeerencapsulationstate
            
            	The status of the encapsulation negotiation state machine
            	**type**\:   :py:class:`Msdppeerencapsulationstate <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdppeertable.Msdppeerentry.Msdppeerencapsulationstate>`
            
            .. attribute:: msdppeerencapsulationtype
            
            	The encapsulation in use when encapsulating data in SA messages to this peer
            	**type**\:   :py:class:`Msdppeerencapsulationtype <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdppeertable.Msdppeerentry.Msdppeerencapsulationtype>`
            
            .. attribute:: msdppeerfsmestablishedtime
            
            	This timer indicates how long (in seconds) this peer has been in the Established state or how long since this peer was last in the Established state.  It is set to zero when a new peer is configured or the MSDP speaker is booted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: msdppeerfsmestablishedtransitions
            
            	The total number of times the MSDP FSM transitioned into the established state
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerholdtimeconfigured
            
            	Time interval in seconds for the Hold Timer configured for this MSDP speaker with this peer
            	**type**\:  int
            
            	**range:** 0..None \| 3..65535
            
            	**units**\: seconds
            
            .. attribute:: msdppeerincontrolmessages
            
            	The total number of MSDP messages received on this TCP connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerindatapackets
            
            	The total number of encapsulated data packets received from this peer.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerinmessageelapsedtime
            
            	Elapsed time in seconds since the last MSDP message was received from the peer.  Each time msdpPeerInControlMessages is incremented, the value of this object is set to zero (0)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: msdppeerinnotifications
            
            	The number of MSDP Notification messages received on this connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerinsarequests
            
            	The number of MSDP SA\-Request messages received on this connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerinsaresponses
            
            	The number of MSDP SA\-Response messages received on this connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerinsas
            
            	The number of MSDP SA messages received on this connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerkeepaliveconfigured
            
            	Time interval in seconds for the KeepAlive timer configured for this MSDP speaker with this peer.  A reasonable maximum value for this timer would be configured to be one third of that of msdpPeerHoldTimeConfigured.  If the value of this object is zero (0), no periodic KEEPALIVE messages are sent to the peer after the MSDP connection has been established
            	**type**\:  int
            
            	**range:** 0..21845
            
            	**units**\: seconds
            
            .. attribute:: msdppeerlasterror
            
            	The last error code and subcode seen by this peer on this connection.  If no error has occurred, this field is zero.  Otherwise, the first byte of this two byte OCTET STRING contains the error code, and the second byte contains the subcode
            	**type**\:  str
            
            	**length:** 2
            
            .. attribute:: msdppeerlocaladdress
            
            	The local IP address of this entry's MSDP connection
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdppeerlocalport
            
            	The local port for the TCP connection between the MSDP peers
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: msdppeeroutcontrolmessages
            
            	The total number of MSDP messages transmitted on this TCP connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeeroutdatapackets
            
            	The total number of encapsulated data packets sent to this peer.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeeroutnotifications
            
            	The number of MSDP Notification messages transmitted on this connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeeroutsarequests
            
            	The number of MSDP SA\-Request messages transmitted on this connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeeroutsaresponses
            
            	The number of MSDP SA Response messages transmitted on this TCP connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeeroutsas
            
            	The number of MSDP SA messages transmitted on this connection.  This object should be initialized to zero when the connection is established
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeerprocessrequestsfrom
            
            	This object indicates whether or not to process MSDP SA Request messages from this peer.  If True(1), MSDP SA Request messages from this peer are processed and replied to (if appropriate) with SA Response messages. If False(2), MSDP SA Request messages from this peer are silently ignored.  It defaults to False when msdpCacheLifetime is 0 and True when msdpCacheLifetime is non\-0
            	**type**\:  bool
            
            .. attribute:: msdppeerremoteport
            
            	The remote port for the TCP connection between the MSDP peers
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: msdppeerrpffailures
            
            	The number of RPF failures on SA messages received from this peer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdppeersaadvperiod
            
            	Time interval in seconds for the MinSAAdvertisementInterval MSDP timer
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**units**\: seconds
            
            .. attribute:: msdppeerstate
            
            	The state of the MSDP TCP connection with this peer
            	**type**\:   :py:class:`Msdppeerstate <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdppeertable.Msdppeerentry.Msdppeerstate>`
            
            .. attribute:: msdppeerstatus
            
            	The RowStatus object by which peers can be added and deleted.  A transition to 'active' will cause the MSDP Start Event to be generated.  A transition out of the 'active' state will cause the MSDP Stop Event to be generated.  Care should be used in providing write access to this object without adequate authentication
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'DRAFT-MSDP-MIB'
            _revision = '1999-12-16'

            def __init__(self):
                super(DraftMsdpMib.Msdppeertable.Msdppeerentry, self).__init__()

                self.yang_name = "msdpPeerEntry"
                self.yang_parent_name = "msdpPeerTable"

                self.msdppeerremoteaddress = YLeaf(YType.str, "msdpPeerRemoteAddress")

                self.msdppeerconnectionattempts = YLeaf(YType.uint32, "msdpPeerConnectionAttempts")

                self.msdppeerconnectretryinterval = YLeaf(YType.int32, "msdpPeerConnectRetryInterval")

                self.msdppeerdatattl = YLeaf(YType.int32, "msdpPeerDataTtl")

                self.msdppeerencapsulationstate = YLeaf(YType.enumeration, "msdpPeerEncapsulationState")

                self.msdppeerencapsulationtype = YLeaf(YType.enumeration, "msdpPeerEncapsulationType")

                self.msdppeerfsmestablishedtime = YLeaf(YType.uint32, "msdpPeerFsmEstablishedTime")

                self.msdppeerfsmestablishedtransitions = YLeaf(YType.uint32, "msdpPeerFsmEstablishedTransitions")

                self.msdppeerholdtimeconfigured = YLeaf(YType.int32, "msdpPeerHoldTimeConfigured")

                self.msdppeerincontrolmessages = YLeaf(YType.uint32, "msdpPeerInControlMessages")

                self.msdppeerindatapackets = YLeaf(YType.uint32, "msdpPeerInDataPackets")

                self.msdppeerinmessageelapsedtime = YLeaf(YType.uint32, "msdpPeerInMessageElapsedTime")

                self.msdppeerinnotifications = YLeaf(YType.uint32, "msdpPeerInNotifications")

                self.msdppeerinsarequests = YLeaf(YType.uint32, "msdpPeerInSARequests")

                self.msdppeerinsaresponses = YLeaf(YType.uint32, "msdpPeerInSAResponses")

                self.msdppeerinsas = YLeaf(YType.uint32, "msdpPeerInSAs")

                self.msdppeerkeepaliveconfigured = YLeaf(YType.int32, "msdpPeerKeepAliveConfigured")

                self.msdppeerlasterror = YLeaf(YType.str, "msdpPeerLastError")

                self.msdppeerlocaladdress = YLeaf(YType.str, "msdpPeerLocalAddress")

                self.msdppeerlocalport = YLeaf(YType.int32, "msdpPeerLocalPort")

                self.msdppeeroutcontrolmessages = YLeaf(YType.uint32, "msdpPeerOutControlMessages")

                self.msdppeeroutdatapackets = YLeaf(YType.uint32, "msdpPeerOutDataPackets")

                self.msdppeeroutnotifications = YLeaf(YType.uint32, "msdpPeerOutNotifications")

                self.msdppeeroutsarequests = YLeaf(YType.uint32, "msdpPeerOutSARequests")

                self.msdppeeroutsaresponses = YLeaf(YType.uint32, "msdpPeerOutSAResponses")

                self.msdppeeroutsas = YLeaf(YType.uint32, "msdpPeerOutSAs")

                self.msdppeerprocessrequestsfrom = YLeaf(YType.boolean, "msdpPeerProcessRequestsFrom")

                self.msdppeerremoteport = YLeaf(YType.int32, "msdpPeerRemotePort")

                self.msdppeerrpffailures = YLeaf(YType.uint32, "msdpPeerRPFFailures")

                self.msdppeersaadvperiod = YLeaf(YType.int32, "msdpPeerSAAdvPeriod")

                self.msdppeerstate = YLeaf(YType.enumeration, "msdpPeerState")

                self.msdppeerstatus = YLeaf(YType.enumeration, "msdpPeerStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("msdppeerremoteaddress",
                                "msdppeerconnectionattempts",
                                "msdppeerconnectretryinterval",
                                "msdppeerdatattl",
                                "msdppeerencapsulationstate",
                                "msdppeerencapsulationtype",
                                "msdppeerfsmestablishedtime",
                                "msdppeerfsmestablishedtransitions",
                                "msdppeerholdtimeconfigured",
                                "msdppeerincontrolmessages",
                                "msdppeerindatapackets",
                                "msdppeerinmessageelapsedtime",
                                "msdppeerinnotifications",
                                "msdppeerinsarequests",
                                "msdppeerinsaresponses",
                                "msdppeerinsas",
                                "msdppeerkeepaliveconfigured",
                                "msdppeerlasterror",
                                "msdppeerlocaladdress",
                                "msdppeerlocalport",
                                "msdppeeroutcontrolmessages",
                                "msdppeeroutdatapackets",
                                "msdppeeroutnotifications",
                                "msdppeeroutsarequests",
                                "msdppeeroutsaresponses",
                                "msdppeeroutsas",
                                "msdppeerprocessrequestsfrom",
                                "msdppeerremoteport",
                                "msdppeerrpffailures",
                                "msdppeersaadvperiod",
                                "msdppeerstate",
                                "msdppeerstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DraftMsdpMib.Msdppeertable.Msdppeerentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DraftMsdpMib.Msdppeertable.Msdppeerentry, self).__setattr__(name, value)

            class Msdppeerencapsulationstate(Enum):
                """
                Msdppeerencapsulationstate

                The status of the encapsulation negotiation state

                machine.

                .. data:: default = 1

                .. data:: received = 2

                .. data:: advertising = 3

                .. data:: sent = 4

                .. data:: agreed = 5

                .. data:: failed = 6

                """

                default = Enum.YLeaf(1, "default")

                received = Enum.YLeaf(2, "received")

                advertising = Enum.YLeaf(3, "advertising")

                sent = Enum.YLeaf(4, "sent")

                agreed = Enum.YLeaf(5, "agreed")

                failed = Enum.YLeaf(6, "failed")


            class Msdppeerencapsulationtype(Enum):
                """
                Msdppeerencapsulationtype

                The encapsulation in use when encapsulating data in

                SA messages to this peer.

                .. data:: tcp = 1

                .. data:: udp = 2

                .. data:: gre = 3

                """

                tcp = Enum.YLeaf(1, "tcp")

                udp = Enum.YLeaf(2, "udp")

                gre = Enum.YLeaf(3, "gre")


            class Msdppeerstate(Enum):
                """
                Msdppeerstate

                The state of the MSDP TCP connection with this peer.

                .. data:: inactive = 1

                .. data:: listen = 2

                .. data:: connecting = 3

                .. data:: established = 4

                .. data:: disabled = 5

                """

                inactive = Enum.YLeaf(1, "inactive")

                listen = Enum.YLeaf(2, "listen")

                connecting = Enum.YLeaf(3, "connecting")

                established = Enum.YLeaf(4, "established")

                disabled = Enum.YLeaf(5, "disabled")


            def has_data(self):
                return (
                    self.msdppeerremoteaddress.is_set or
                    self.msdppeerconnectionattempts.is_set or
                    self.msdppeerconnectretryinterval.is_set or
                    self.msdppeerdatattl.is_set or
                    self.msdppeerencapsulationstate.is_set or
                    self.msdppeerencapsulationtype.is_set or
                    self.msdppeerfsmestablishedtime.is_set or
                    self.msdppeerfsmestablishedtransitions.is_set or
                    self.msdppeerholdtimeconfigured.is_set or
                    self.msdppeerincontrolmessages.is_set or
                    self.msdppeerindatapackets.is_set or
                    self.msdppeerinmessageelapsedtime.is_set or
                    self.msdppeerinnotifications.is_set or
                    self.msdppeerinsarequests.is_set or
                    self.msdppeerinsaresponses.is_set or
                    self.msdppeerinsas.is_set or
                    self.msdppeerkeepaliveconfigured.is_set or
                    self.msdppeerlasterror.is_set or
                    self.msdppeerlocaladdress.is_set or
                    self.msdppeerlocalport.is_set or
                    self.msdppeeroutcontrolmessages.is_set or
                    self.msdppeeroutdatapackets.is_set or
                    self.msdppeeroutnotifications.is_set or
                    self.msdppeeroutsarequests.is_set or
                    self.msdppeeroutsaresponses.is_set or
                    self.msdppeeroutsas.is_set or
                    self.msdppeerprocessrequestsfrom.is_set or
                    self.msdppeerremoteport.is_set or
                    self.msdppeerrpffailures.is_set or
                    self.msdppeersaadvperiod.is_set or
                    self.msdppeerstate.is_set or
                    self.msdppeerstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.msdppeerremoteaddress.yfilter != YFilter.not_set or
                    self.msdppeerconnectionattempts.yfilter != YFilter.not_set or
                    self.msdppeerconnectretryinterval.yfilter != YFilter.not_set or
                    self.msdppeerdatattl.yfilter != YFilter.not_set or
                    self.msdppeerencapsulationstate.yfilter != YFilter.not_set or
                    self.msdppeerencapsulationtype.yfilter != YFilter.not_set or
                    self.msdppeerfsmestablishedtime.yfilter != YFilter.not_set or
                    self.msdppeerfsmestablishedtransitions.yfilter != YFilter.not_set or
                    self.msdppeerholdtimeconfigured.yfilter != YFilter.not_set or
                    self.msdppeerincontrolmessages.yfilter != YFilter.not_set or
                    self.msdppeerindatapackets.yfilter != YFilter.not_set or
                    self.msdppeerinmessageelapsedtime.yfilter != YFilter.not_set or
                    self.msdppeerinnotifications.yfilter != YFilter.not_set or
                    self.msdppeerinsarequests.yfilter != YFilter.not_set or
                    self.msdppeerinsaresponses.yfilter != YFilter.not_set or
                    self.msdppeerinsas.yfilter != YFilter.not_set or
                    self.msdppeerkeepaliveconfigured.yfilter != YFilter.not_set or
                    self.msdppeerlasterror.yfilter != YFilter.not_set or
                    self.msdppeerlocaladdress.yfilter != YFilter.not_set or
                    self.msdppeerlocalport.yfilter != YFilter.not_set or
                    self.msdppeeroutcontrolmessages.yfilter != YFilter.not_set or
                    self.msdppeeroutdatapackets.yfilter != YFilter.not_set or
                    self.msdppeeroutnotifications.yfilter != YFilter.not_set or
                    self.msdppeeroutsarequests.yfilter != YFilter.not_set or
                    self.msdppeeroutsaresponses.yfilter != YFilter.not_set or
                    self.msdppeeroutsas.yfilter != YFilter.not_set or
                    self.msdppeerprocessrequestsfrom.yfilter != YFilter.not_set or
                    self.msdppeerremoteport.yfilter != YFilter.not_set or
                    self.msdppeerrpffailures.yfilter != YFilter.not_set or
                    self.msdppeersaadvperiod.yfilter != YFilter.not_set or
                    self.msdppeerstate.yfilter != YFilter.not_set or
                    self.msdppeerstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "msdpPeerEntry" + "[msdpPeerRemoteAddress='" + self.msdppeerremoteaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/msdpPeerTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.msdppeerremoteaddress.is_set or self.msdppeerremoteaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerremoteaddress.get_name_leafdata())
                if (self.msdppeerconnectionattempts.is_set or self.msdppeerconnectionattempts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerconnectionattempts.get_name_leafdata())
                if (self.msdppeerconnectretryinterval.is_set or self.msdppeerconnectretryinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerconnectretryinterval.get_name_leafdata())
                if (self.msdppeerdatattl.is_set or self.msdppeerdatattl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerdatattl.get_name_leafdata())
                if (self.msdppeerencapsulationstate.is_set or self.msdppeerencapsulationstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerencapsulationstate.get_name_leafdata())
                if (self.msdppeerencapsulationtype.is_set or self.msdppeerencapsulationtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerencapsulationtype.get_name_leafdata())
                if (self.msdppeerfsmestablishedtime.is_set or self.msdppeerfsmestablishedtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerfsmestablishedtime.get_name_leafdata())
                if (self.msdppeerfsmestablishedtransitions.is_set or self.msdppeerfsmestablishedtransitions.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerfsmestablishedtransitions.get_name_leafdata())
                if (self.msdppeerholdtimeconfigured.is_set or self.msdppeerholdtimeconfigured.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerholdtimeconfigured.get_name_leafdata())
                if (self.msdppeerincontrolmessages.is_set or self.msdppeerincontrolmessages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerincontrolmessages.get_name_leafdata())
                if (self.msdppeerindatapackets.is_set or self.msdppeerindatapackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerindatapackets.get_name_leafdata())
                if (self.msdppeerinmessageelapsedtime.is_set or self.msdppeerinmessageelapsedtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerinmessageelapsedtime.get_name_leafdata())
                if (self.msdppeerinnotifications.is_set or self.msdppeerinnotifications.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerinnotifications.get_name_leafdata())
                if (self.msdppeerinsarequests.is_set or self.msdppeerinsarequests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerinsarequests.get_name_leafdata())
                if (self.msdppeerinsaresponses.is_set or self.msdppeerinsaresponses.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerinsaresponses.get_name_leafdata())
                if (self.msdppeerinsas.is_set or self.msdppeerinsas.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerinsas.get_name_leafdata())
                if (self.msdppeerkeepaliveconfigured.is_set or self.msdppeerkeepaliveconfigured.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerkeepaliveconfigured.get_name_leafdata())
                if (self.msdppeerlasterror.is_set or self.msdppeerlasterror.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerlasterror.get_name_leafdata())
                if (self.msdppeerlocaladdress.is_set or self.msdppeerlocaladdress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerlocaladdress.get_name_leafdata())
                if (self.msdppeerlocalport.is_set or self.msdppeerlocalport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerlocalport.get_name_leafdata())
                if (self.msdppeeroutcontrolmessages.is_set or self.msdppeeroutcontrolmessages.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeeroutcontrolmessages.get_name_leafdata())
                if (self.msdppeeroutdatapackets.is_set or self.msdppeeroutdatapackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeeroutdatapackets.get_name_leafdata())
                if (self.msdppeeroutnotifications.is_set or self.msdppeeroutnotifications.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeeroutnotifications.get_name_leafdata())
                if (self.msdppeeroutsarequests.is_set or self.msdppeeroutsarequests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeeroutsarequests.get_name_leafdata())
                if (self.msdppeeroutsaresponses.is_set or self.msdppeeroutsaresponses.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeeroutsaresponses.get_name_leafdata())
                if (self.msdppeeroutsas.is_set or self.msdppeeroutsas.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeeroutsas.get_name_leafdata())
                if (self.msdppeerprocessrequestsfrom.is_set or self.msdppeerprocessrequestsfrom.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerprocessrequestsfrom.get_name_leafdata())
                if (self.msdppeerremoteport.is_set or self.msdppeerremoteport.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerremoteport.get_name_leafdata())
                if (self.msdppeerrpffailures.is_set or self.msdppeerrpffailures.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerrpffailures.get_name_leafdata())
                if (self.msdppeersaadvperiod.is_set or self.msdppeersaadvperiod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeersaadvperiod.get_name_leafdata())
                if (self.msdppeerstate.is_set or self.msdppeerstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerstate.get_name_leafdata())
                if (self.msdppeerstatus.is_set or self.msdppeerstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdppeerstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "msdpPeerRemoteAddress" or name == "msdpPeerConnectionAttempts" or name == "msdpPeerConnectRetryInterval" or name == "msdpPeerDataTtl" or name == "msdpPeerEncapsulationState" or name == "msdpPeerEncapsulationType" or name == "msdpPeerFsmEstablishedTime" or name == "msdpPeerFsmEstablishedTransitions" or name == "msdpPeerHoldTimeConfigured" or name == "msdpPeerInControlMessages" or name == "msdpPeerInDataPackets" or name == "msdpPeerInMessageElapsedTime" or name == "msdpPeerInNotifications" or name == "msdpPeerInSARequests" or name == "msdpPeerInSAResponses" or name == "msdpPeerInSAs" or name == "msdpPeerKeepAliveConfigured" or name == "msdpPeerLastError" or name == "msdpPeerLocalAddress" or name == "msdpPeerLocalPort" or name == "msdpPeerOutControlMessages" or name == "msdpPeerOutDataPackets" or name == "msdpPeerOutNotifications" or name == "msdpPeerOutSARequests" or name == "msdpPeerOutSAResponses" or name == "msdpPeerOutSAs" or name == "msdpPeerProcessRequestsFrom" or name == "msdpPeerRemotePort" or name == "msdpPeerRPFFailures" or name == "msdpPeerSAAdvPeriod" or name == "msdpPeerState" or name == "msdpPeerStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "msdpPeerRemoteAddress"):
                    self.msdppeerremoteaddress = value
                    self.msdppeerremoteaddress.value_namespace = name_space
                    self.msdppeerremoteaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerConnectionAttempts"):
                    self.msdppeerconnectionattempts = value
                    self.msdppeerconnectionattempts.value_namespace = name_space
                    self.msdppeerconnectionattempts.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerConnectRetryInterval"):
                    self.msdppeerconnectretryinterval = value
                    self.msdppeerconnectretryinterval.value_namespace = name_space
                    self.msdppeerconnectretryinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerDataTtl"):
                    self.msdppeerdatattl = value
                    self.msdppeerdatattl.value_namespace = name_space
                    self.msdppeerdatattl.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerEncapsulationState"):
                    self.msdppeerencapsulationstate = value
                    self.msdppeerencapsulationstate.value_namespace = name_space
                    self.msdppeerencapsulationstate.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerEncapsulationType"):
                    self.msdppeerencapsulationtype = value
                    self.msdppeerencapsulationtype.value_namespace = name_space
                    self.msdppeerencapsulationtype.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerFsmEstablishedTime"):
                    self.msdppeerfsmestablishedtime = value
                    self.msdppeerfsmestablishedtime.value_namespace = name_space
                    self.msdppeerfsmestablishedtime.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerFsmEstablishedTransitions"):
                    self.msdppeerfsmestablishedtransitions = value
                    self.msdppeerfsmestablishedtransitions.value_namespace = name_space
                    self.msdppeerfsmestablishedtransitions.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerHoldTimeConfigured"):
                    self.msdppeerholdtimeconfigured = value
                    self.msdppeerholdtimeconfigured.value_namespace = name_space
                    self.msdppeerholdtimeconfigured.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerInControlMessages"):
                    self.msdppeerincontrolmessages = value
                    self.msdppeerincontrolmessages.value_namespace = name_space
                    self.msdppeerincontrolmessages.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerInDataPackets"):
                    self.msdppeerindatapackets = value
                    self.msdppeerindatapackets.value_namespace = name_space
                    self.msdppeerindatapackets.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerInMessageElapsedTime"):
                    self.msdppeerinmessageelapsedtime = value
                    self.msdppeerinmessageelapsedtime.value_namespace = name_space
                    self.msdppeerinmessageelapsedtime.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerInNotifications"):
                    self.msdppeerinnotifications = value
                    self.msdppeerinnotifications.value_namespace = name_space
                    self.msdppeerinnotifications.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerInSARequests"):
                    self.msdppeerinsarequests = value
                    self.msdppeerinsarequests.value_namespace = name_space
                    self.msdppeerinsarequests.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerInSAResponses"):
                    self.msdppeerinsaresponses = value
                    self.msdppeerinsaresponses.value_namespace = name_space
                    self.msdppeerinsaresponses.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerInSAs"):
                    self.msdppeerinsas = value
                    self.msdppeerinsas.value_namespace = name_space
                    self.msdppeerinsas.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerKeepAliveConfigured"):
                    self.msdppeerkeepaliveconfigured = value
                    self.msdppeerkeepaliveconfigured.value_namespace = name_space
                    self.msdppeerkeepaliveconfigured.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerLastError"):
                    self.msdppeerlasterror = value
                    self.msdppeerlasterror.value_namespace = name_space
                    self.msdppeerlasterror.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerLocalAddress"):
                    self.msdppeerlocaladdress = value
                    self.msdppeerlocaladdress.value_namespace = name_space
                    self.msdppeerlocaladdress.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerLocalPort"):
                    self.msdppeerlocalport = value
                    self.msdppeerlocalport.value_namespace = name_space
                    self.msdppeerlocalport.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerOutControlMessages"):
                    self.msdppeeroutcontrolmessages = value
                    self.msdppeeroutcontrolmessages.value_namespace = name_space
                    self.msdppeeroutcontrolmessages.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerOutDataPackets"):
                    self.msdppeeroutdatapackets = value
                    self.msdppeeroutdatapackets.value_namespace = name_space
                    self.msdppeeroutdatapackets.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerOutNotifications"):
                    self.msdppeeroutnotifications = value
                    self.msdppeeroutnotifications.value_namespace = name_space
                    self.msdppeeroutnotifications.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerOutSARequests"):
                    self.msdppeeroutsarequests = value
                    self.msdppeeroutsarequests.value_namespace = name_space
                    self.msdppeeroutsarequests.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerOutSAResponses"):
                    self.msdppeeroutsaresponses = value
                    self.msdppeeroutsaresponses.value_namespace = name_space
                    self.msdppeeroutsaresponses.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerOutSAs"):
                    self.msdppeeroutsas = value
                    self.msdppeeroutsas.value_namespace = name_space
                    self.msdppeeroutsas.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerProcessRequestsFrom"):
                    self.msdppeerprocessrequestsfrom = value
                    self.msdppeerprocessrequestsfrom.value_namespace = name_space
                    self.msdppeerprocessrequestsfrom.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerRemotePort"):
                    self.msdppeerremoteport = value
                    self.msdppeerremoteport.value_namespace = name_space
                    self.msdppeerremoteport.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerRPFFailures"):
                    self.msdppeerrpffailures = value
                    self.msdppeerrpffailures.value_namespace = name_space
                    self.msdppeerrpffailures.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerSAAdvPeriod"):
                    self.msdppeersaadvperiod = value
                    self.msdppeersaadvperiod.value_namespace = name_space
                    self.msdppeersaadvperiod.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerState"):
                    self.msdppeerstate = value
                    self.msdppeerstate.value_namespace = name_space
                    self.msdppeerstate.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpPeerStatus"):
                    self.msdppeerstatus = value
                    self.msdppeerstatus.value_namespace = name_space
                    self.msdppeerstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.msdppeerentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.msdppeerentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "msdpPeerTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "msdpPeerEntry"):
                for c in self.msdppeerentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DraftMsdpMib.Msdppeertable.Msdppeerentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.msdppeerentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "msdpPeerEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Msdpsacachetable(Entity):
        """
        The (conceptual) table listing the MSDP SA
        advertisements currently in the MSDP speaker's cache.
        
        .. attribute:: msdpsacacheentry
        
        	An entry (conceptual row) representing an MSDP SA advert
        	**type**\: list of    :py:class:`Msdpsacacheentry <ydk.models.cisco_ios_xe.DRAFT_MSDP_MIB.DraftMsdpMib.Msdpsacachetable.Msdpsacacheentry>`
        
        

        """

        _prefix = 'DRAFT-MSDP-MIB'
        _revision = '1999-12-16'

        def __init__(self):
            super(DraftMsdpMib.Msdpsacachetable, self).__init__()

            self.yang_name = "msdpSACacheTable"
            self.yang_parent_name = "DRAFT-MSDP-MIB"

            self.msdpsacacheentry = YList(self)

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
                        super(DraftMsdpMib.Msdpsacachetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(DraftMsdpMib.Msdpsacachetable, self).__setattr__(name, value)


        class Msdpsacacheentry(Entity):
            """
            An entry (conceptual row) representing an MSDP SA
            advert.
            
            .. attribute:: msdpsacachegroupaddr  <key>
            
            	The group address of the SA Cache entry
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdpsacachesourceaddr  <key>
            
            	The source address of the SA Cache entry
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdpsacacheoriginrp  <key>
            
            	The address of the RP which originated the last SA message accepted for this entry
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdpsacacheexpirytime
            
            	The time remaining before this entry will expire from the SA cache
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdpsacacheindatapackets
            
            	The number of MSDP encapsulated data packets received relevant to this cache entry.  This object must be initialized to zero when creating a cache entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdpsacacheinsas
            
            	The number of MSDP SA messages received relevant to this cache entry.  This object must be initialized to zero when creating a cache entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: msdpsacachepeerlearnedfrom
            
            	The peer from which this SA Cache entry was last accepted.  This address must correspond to the msdpPeerRemoteAddress value for a row in the MSDP Peer Table
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdpsacacherpfpeer
            
            	The peer from which an SA message corresponding to this cache entry would be accepted (i.e. the RPF peer for msdpSACacheOriginRP).  This may be different than msdpSACachePeerLearnedFrom if this entry was created by an MSDP SA\-Response.  This address must correspond to the msdpPeerRemoteAddress value for a row in the MSDP Peer Table
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: msdpsacachestatus
            
            	The status of this row in the table.  The only allowable actions are to retreive the status, which will be `active', or to set the status to `destroy' in order to remove this entry from the cache
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: msdpsacacheuptime
            
            	The time since this entry was placed in the SA cache
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'DRAFT-MSDP-MIB'
            _revision = '1999-12-16'

            def __init__(self):
                super(DraftMsdpMib.Msdpsacachetable.Msdpsacacheentry, self).__init__()

                self.yang_name = "msdpSACacheEntry"
                self.yang_parent_name = "msdpSACacheTable"

                self.msdpsacachegroupaddr = YLeaf(YType.str, "msdpSACacheGroupAddr")

                self.msdpsacachesourceaddr = YLeaf(YType.str, "msdpSACacheSourceAddr")

                self.msdpsacacheoriginrp = YLeaf(YType.str, "msdpSACacheOriginRP")

                self.msdpsacacheexpirytime = YLeaf(YType.uint32, "msdpSACacheExpiryTime")

                self.msdpsacacheindatapackets = YLeaf(YType.uint32, "msdpSACacheInDataPackets")

                self.msdpsacacheinsas = YLeaf(YType.uint32, "msdpSACacheInSAs")

                self.msdpsacachepeerlearnedfrom = YLeaf(YType.str, "msdpSACachePeerLearnedFrom")

                self.msdpsacacherpfpeer = YLeaf(YType.str, "msdpSACacheRPFPeer")

                self.msdpsacachestatus = YLeaf(YType.enumeration, "msdpSACacheStatus")

                self.msdpsacacheuptime = YLeaf(YType.uint32, "msdpSACacheUpTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("msdpsacachegroupaddr",
                                "msdpsacachesourceaddr",
                                "msdpsacacheoriginrp",
                                "msdpsacacheexpirytime",
                                "msdpsacacheindatapackets",
                                "msdpsacacheinsas",
                                "msdpsacachepeerlearnedfrom",
                                "msdpsacacherpfpeer",
                                "msdpsacachestatus",
                                "msdpsacacheuptime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(DraftMsdpMib.Msdpsacachetable.Msdpsacacheentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(DraftMsdpMib.Msdpsacachetable.Msdpsacacheentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.msdpsacachegroupaddr.is_set or
                    self.msdpsacachesourceaddr.is_set or
                    self.msdpsacacheoriginrp.is_set or
                    self.msdpsacacheexpirytime.is_set or
                    self.msdpsacacheindatapackets.is_set or
                    self.msdpsacacheinsas.is_set or
                    self.msdpsacachepeerlearnedfrom.is_set or
                    self.msdpsacacherpfpeer.is_set or
                    self.msdpsacachestatus.is_set or
                    self.msdpsacacheuptime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.msdpsacachegroupaddr.yfilter != YFilter.not_set or
                    self.msdpsacachesourceaddr.yfilter != YFilter.not_set or
                    self.msdpsacacheoriginrp.yfilter != YFilter.not_set or
                    self.msdpsacacheexpirytime.yfilter != YFilter.not_set or
                    self.msdpsacacheindatapackets.yfilter != YFilter.not_set or
                    self.msdpsacacheinsas.yfilter != YFilter.not_set or
                    self.msdpsacachepeerlearnedfrom.yfilter != YFilter.not_set or
                    self.msdpsacacherpfpeer.yfilter != YFilter.not_set or
                    self.msdpsacachestatus.yfilter != YFilter.not_set or
                    self.msdpsacacheuptime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "msdpSACacheEntry" + "[msdpSACacheGroupAddr='" + self.msdpsacachegroupaddr.get() + "']" + "[msdpSACacheSourceAddr='" + self.msdpsacachesourceaddr.get() + "']" + "[msdpSACacheOriginRP='" + self.msdpsacacheoriginrp.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/msdpSACacheTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.msdpsacachegroupaddr.is_set or self.msdpsacachegroupaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdpsacachegroupaddr.get_name_leafdata())
                if (self.msdpsacachesourceaddr.is_set or self.msdpsacachesourceaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdpsacachesourceaddr.get_name_leafdata())
                if (self.msdpsacacheoriginrp.is_set or self.msdpsacacheoriginrp.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdpsacacheoriginrp.get_name_leafdata())
                if (self.msdpsacacheexpirytime.is_set or self.msdpsacacheexpirytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdpsacacheexpirytime.get_name_leafdata())
                if (self.msdpsacacheindatapackets.is_set or self.msdpsacacheindatapackets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdpsacacheindatapackets.get_name_leafdata())
                if (self.msdpsacacheinsas.is_set or self.msdpsacacheinsas.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdpsacacheinsas.get_name_leafdata())
                if (self.msdpsacachepeerlearnedfrom.is_set or self.msdpsacachepeerlearnedfrom.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdpsacachepeerlearnedfrom.get_name_leafdata())
                if (self.msdpsacacherpfpeer.is_set or self.msdpsacacherpfpeer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdpsacacherpfpeer.get_name_leafdata())
                if (self.msdpsacachestatus.is_set or self.msdpsacachestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdpsacachestatus.get_name_leafdata())
                if (self.msdpsacacheuptime.is_set or self.msdpsacacheuptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.msdpsacacheuptime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "msdpSACacheGroupAddr" or name == "msdpSACacheSourceAddr" or name == "msdpSACacheOriginRP" or name == "msdpSACacheExpiryTime" or name == "msdpSACacheInDataPackets" or name == "msdpSACacheInSAs" or name == "msdpSACachePeerLearnedFrom" or name == "msdpSACacheRPFPeer" or name == "msdpSACacheStatus" or name == "msdpSACacheUpTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "msdpSACacheGroupAddr"):
                    self.msdpsacachegroupaddr = value
                    self.msdpsacachegroupaddr.value_namespace = name_space
                    self.msdpsacachegroupaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpSACacheSourceAddr"):
                    self.msdpsacachesourceaddr = value
                    self.msdpsacachesourceaddr.value_namespace = name_space
                    self.msdpsacachesourceaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpSACacheOriginRP"):
                    self.msdpsacacheoriginrp = value
                    self.msdpsacacheoriginrp.value_namespace = name_space
                    self.msdpsacacheoriginrp.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpSACacheExpiryTime"):
                    self.msdpsacacheexpirytime = value
                    self.msdpsacacheexpirytime.value_namespace = name_space
                    self.msdpsacacheexpirytime.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpSACacheInDataPackets"):
                    self.msdpsacacheindatapackets = value
                    self.msdpsacacheindatapackets.value_namespace = name_space
                    self.msdpsacacheindatapackets.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpSACacheInSAs"):
                    self.msdpsacacheinsas = value
                    self.msdpsacacheinsas.value_namespace = name_space
                    self.msdpsacacheinsas.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpSACachePeerLearnedFrom"):
                    self.msdpsacachepeerlearnedfrom = value
                    self.msdpsacachepeerlearnedfrom.value_namespace = name_space
                    self.msdpsacachepeerlearnedfrom.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpSACacheRPFPeer"):
                    self.msdpsacacherpfpeer = value
                    self.msdpsacacherpfpeer.value_namespace = name_space
                    self.msdpsacacherpfpeer.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpSACacheStatus"):
                    self.msdpsacachestatus = value
                    self.msdpsacachestatus.value_namespace = name_space
                    self.msdpsacachestatus.value_namespace_prefix = name_space_prefix
                if(value_path == "msdpSACacheUpTime"):
                    self.msdpsacacheuptime = value
                    self.msdpsacacheuptime.value_namespace = name_space
                    self.msdpsacacheuptime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.msdpsacacheentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.msdpsacacheentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "msdpSACacheTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "DRAFT-MSDP-MIB:DRAFT-MSDP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "msdpSACacheEntry"):
                for c in self.msdpsacacheentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = DraftMsdpMib.Msdpsacachetable.Msdpsacacheentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.msdpsacacheentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "msdpSACacheEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.msdp is not None and self.msdp.has_data()) or
            (self.msdppeertable is not None and self.msdppeertable.has_data()) or
            (self.msdprequeststable is not None and self.msdprequeststable.has_data()) or
            (self.msdpsacachetable is not None and self.msdpsacachetable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.msdp is not None and self.msdp.has_operation()) or
            (self.msdppeertable is not None and self.msdppeertable.has_operation()) or
            (self.msdprequeststable is not None and self.msdprequeststable.has_operation()) or
            (self.msdpsacachetable is not None and self.msdpsacachetable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "DRAFT-MSDP-MIB:DRAFT-MSDP-MIB" + path_buffer

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

        if (child_yang_name == "msdp"):
            if (self.msdp is None):
                self.msdp = DraftMsdpMib.Msdp()
                self.msdp.parent = self
                self._children_name_map["msdp"] = "msdp"
            return self.msdp

        if (child_yang_name == "msdpPeerTable"):
            if (self.msdppeertable is None):
                self.msdppeertable = DraftMsdpMib.Msdppeertable()
                self.msdppeertable.parent = self
                self._children_name_map["msdppeertable"] = "msdpPeerTable"
            return self.msdppeertable

        if (child_yang_name == "msdpRequestsTable"):
            if (self.msdprequeststable is None):
                self.msdprequeststable = DraftMsdpMib.Msdprequeststable()
                self.msdprequeststable.parent = self
                self._children_name_map["msdprequeststable"] = "msdpRequestsTable"
            return self.msdprequeststable

        if (child_yang_name == "msdpSACacheTable"):
            if (self.msdpsacachetable is None):
                self.msdpsacachetable = DraftMsdpMib.Msdpsacachetable()
                self.msdpsacachetable.parent = self
                self._children_name_map["msdpsacachetable"] = "msdpSACacheTable"
            return self.msdpsacachetable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "msdp" or name == "msdpPeerTable" or name == "msdpRequestsTable" or name == "msdpSACacheTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = DraftMsdpMib()
        return self._top_entity

