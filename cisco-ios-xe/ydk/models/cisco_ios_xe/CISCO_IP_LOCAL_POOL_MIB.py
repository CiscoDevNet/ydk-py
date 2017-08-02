""" CISCO_IP_LOCAL_POOL_MIB 

This MIB defines the configuration and monitoring capabilities
relating to local IP pools.

Local IP pools have the following characteristics\:

\- An IP local pool consists of one or more IP address ranges.

\- An IP pool group consists of one or more IP local pools.

\- An IP local pool can only belong to one IP pool group.

\- IP local pools that belong to different groups can have
  overlapping addresses.

\- IP local pool names are unique even when they belong to
  different groups.

\- Addresses within an IP pool group can not overlap.

\- IP local pools without an explicit group name are considered
  members of the base system group.  In this MIB, the base
  system group is represented by a null IP pool group name.

This MIB defines objects that expose the relationship between
IP pool groups and IP local pools.  There exist other objects
that maintain statistics about the address usage of IP local
pools.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoIpLocalPoolMib(Entity):
    """
    
    
    .. attribute:: ciplocalpoolalloctable
    
    	This table lists all addresses that have been allocated out of an IP local pool.  Entries in this table are created when a remote peer allocates an address from one of the IP local pools in the cIpLocalPoolConfigTable.  Entries in this table are deleted when a remote peer deallocates an address from one of the IP local pool in the cIpLocalPoolConfigTable.  Entries in this table are uniquely indexed by the name of the IP local pool, and the allocated address, together with its address type
    	**type**\:   :py:class:`Ciplocalpoolalloctable <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CiscoIpLocalPoolMib.Ciplocalpoolalloctable>`
    
    .. attribute:: ciplocalpoolconfig
    
    	
    	**type**\:   :py:class:`Ciplocalpoolconfig <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CiscoIpLocalPoolMib.Ciplocalpoolconfig>`
    
    .. attribute:: ciplocalpoolconfigtable
    
    	This table manages the creation, modification, and deletion of IP local pools using the RowStatus textual convention.  An entry in this table defines an IP address range that is associated with an IP local pool.  A conceptual row in this table can not be modified while cIpLocalPoolRowStatus is set to 'active'.  Since IP local pool names are unique even when they belong to different groups, and addresses within a group can not overlap, a row in this table is uniquely indexed by the pool name, and by the low address of the IP local pool together with its address type
    	**type**\:   :py:class:`Ciplocalpoolconfigtable <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CiscoIpLocalPoolMib.Ciplocalpoolconfigtable>`
    
    .. attribute:: ciplocalpoolgroupcontainstable
    
    	A table which exposes the container/'containee' relationships between local IP pools and IP pool groups.  Entries in this table are created or deleted as a by\-product of creating or deleting entries in the cIpLocalPoolConfigTable.  When an entry is created and activated in the cIpLocalPoolConfigTable table, an entry in this table will come into existence if it does not already exist.  When an entry is deleted in the cIpLocalPoolConfigTable table, if there is no other entry existing in that table with the same cIpLocalPoolGroupContainedIn and cIpLocalPoolName, the entry in this table with the respective cIpLocalPoolGroupName and cIpLocalPoolName indices will be removed
    	**type**\:   :py:class:`Ciplocalpoolgroupcontainstable <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable>`
    
    .. attribute:: ciplocalpoolgrouptable
    
    	This table provides statistics for configured IP pool groups.  Entries in this table are created as the result of adding a new IP pool group to the cIpLocalPoolConfigTable.  Entries in this table are deleted as the result of removing all IP local pools that are contained in an IP pool group in the cIpLocalPoolConfigTable.  An entry in this table is uniquely indexed by IP pool group name
    	**type**\:   :py:class:`Ciplocalpoolgrouptable <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CiscoIpLocalPoolMib.Ciplocalpoolgrouptable>`
    
    .. attribute:: ciplocalpoolstatstable
    
    	A table providing statistics for each IP local pool.  Entries in this table are created as the result of adding a new IP local pool to the cIpLocalPoolConfigTable.  Entries in this table are deleted as the result of removing all the address ranges that are contained in an IP local pool in the cIpLocalPoolConfigTable.  Entries in this table are uniquely indexed by the name of the IP local pool
    	**type**\:   :py:class:`Ciplocalpoolstatstable <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CiscoIpLocalPoolMib.Ciplocalpoolstatstable>`
    
    

    """

    _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
    _revision = '2007-11-12'

    def __init__(self):
        super(CiscoIpLocalPoolMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-IP-LOCAL-POOL-MIB"
        self.yang_parent_name = "CISCO-IP-LOCAL-POOL-MIB"

        self.ciplocalpoolalloctable = CiscoIpLocalPoolMib.Ciplocalpoolalloctable()
        self.ciplocalpoolalloctable.parent = self
        self._children_name_map["ciplocalpoolalloctable"] = "cIpLocalPoolAllocTable"
        self._children_yang_names.add("cIpLocalPoolAllocTable")

        self.ciplocalpoolconfig = CiscoIpLocalPoolMib.Ciplocalpoolconfig()
        self.ciplocalpoolconfig.parent = self
        self._children_name_map["ciplocalpoolconfig"] = "cIpLocalPoolConfig"
        self._children_yang_names.add("cIpLocalPoolConfig")

        self.ciplocalpoolconfigtable = CiscoIpLocalPoolMib.Ciplocalpoolconfigtable()
        self.ciplocalpoolconfigtable.parent = self
        self._children_name_map["ciplocalpoolconfigtable"] = "cIpLocalPoolConfigTable"
        self._children_yang_names.add("cIpLocalPoolConfigTable")

        self.ciplocalpoolgroupcontainstable = CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable()
        self.ciplocalpoolgroupcontainstable.parent = self
        self._children_name_map["ciplocalpoolgroupcontainstable"] = "cIpLocalPoolGroupContainsTable"
        self._children_yang_names.add("cIpLocalPoolGroupContainsTable")

        self.ciplocalpoolgrouptable = CiscoIpLocalPoolMib.Ciplocalpoolgrouptable()
        self.ciplocalpoolgrouptable.parent = self
        self._children_name_map["ciplocalpoolgrouptable"] = "cIpLocalPoolGroupTable"
        self._children_yang_names.add("cIpLocalPoolGroupTable")

        self.ciplocalpoolstatstable = CiscoIpLocalPoolMib.Ciplocalpoolstatstable()
        self.ciplocalpoolstatstable.parent = self
        self._children_name_map["ciplocalpoolstatstable"] = "cIpLocalPoolStatsTable"
        self._children_yang_names.add("cIpLocalPoolStatsTable")


    class Ciplocalpoolconfig(Entity):
        """
        
        
        .. attribute:: ciplocalpoolnotificationsenable
        
        	An indication of whether the notifications defined by the ciscoIpLocalPoolNotifGroup are enabled
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
        _revision = '2007-11-12'

        def __init__(self):
            super(CiscoIpLocalPoolMib.Ciplocalpoolconfig, self).__init__()

            self.yang_name = "cIpLocalPoolConfig"
            self.yang_parent_name = "CISCO-IP-LOCAL-POOL-MIB"

            self.ciplocalpoolnotificationsenable = YLeaf(YType.boolean, "cIpLocalPoolNotificationsEnable")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ciplocalpoolnotificationsenable") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoIpLocalPoolMib.Ciplocalpoolconfig, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpLocalPoolMib.Ciplocalpoolconfig, self).__setattr__(name, value)

        def has_data(self):
            return self.ciplocalpoolnotificationsenable.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ciplocalpoolnotificationsenable.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cIpLocalPoolConfig" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ciplocalpoolnotificationsenable.is_set or self.ciplocalpoolnotificationsenable.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ciplocalpoolnotificationsenable.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cIpLocalPoolNotificationsEnable"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cIpLocalPoolNotificationsEnable"):
                self.ciplocalpoolnotificationsenable = value
                self.ciplocalpoolnotificationsenable.value_namespace = name_space
                self.ciplocalpoolnotificationsenable.value_namespace_prefix = name_space_prefix


    class Ciplocalpoolconfigtable(Entity):
        """
        This table manages the creation, modification, and deletion
        of IP local pools using the RowStatus textual convention.  An
        entry in this table defines an IP address range that is
        associated with an IP local pool.
        
        A conceptual row in this table can not be modified while
        cIpLocalPoolRowStatus is set to 'active'.
        
        Since IP local pool names are unique even when they belong to
        different groups, and addresses within a group can not overlap,
        a row in this table is uniquely indexed by the pool name, and by
        the low address of the IP local pool together with its address
        type.
        
        .. attribute:: ciplocalpoolconfigentry
        
        	Each entry provides information about a particular IP local pool, including the number of free and used addresses and its priority
        	**type**\: list of    :py:class:`Ciplocalpoolconfigentry <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CiscoIpLocalPoolMib.Ciplocalpoolconfigtable.Ciplocalpoolconfigentry>`
        
        

        """

        _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
        _revision = '2007-11-12'

        def __init__(self):
            super(CiscoIpLocalPoolMib.Ciplocalpoolconfigtable, self).__init__()

            self.yang_name = "cIpLocalPoolConfigTable"
            self.yang_parent_name = "CISCO-IP-LOCAL-POOL-MIB"

            self.ciplocalpoolconfigentry = YList(self)

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
                        super(CiscoIpLocalPoolMib.Ciplocalpoolconfigtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpLocalPoolMib.Ciplocalpoolconfigtable, self).__setattr__(name, value)


        class Ciplocalpoolconfigentry(Entity):
            """
            Each entry provides information about a particular IP local
            pool, including the number of free and used addresses and its priority.
            
            .. attribute:: ciplocalpoolname  <key>
            
            	An arbitrary non\-empty string that uniquely identifies the IP local pool.  This name must be unique among all the local IP pools even when they belong to different pool groups
            	**type**\:  str
            
            	**length:** 1..48
            
            .. attribute:: ciplocalpooladdrtype  <key>
            
            	This object specifies the address type of cIpLocalPoolAddressLo and cIpLocalPoolAddressHi
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ciplocalpooladdresslo  <key>
            
            	This object specifies the first IP address of the range of IP addresses contained by this pool entry.  The address type of this object is described by cIpLocalPoolAddrType.  This address must be less than or equal to the address in cIpLocalPoolAddressHi
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ciplocalpooladdresshi
            
            	This object specifies the last IP address of the range of IP addresses mapped by this pool entry.  The address type of this object is described by cIpLocalPoolAddrType.  If only a single address is being mapped, the value of this object is equal to the value of cIpLocalPoolAddressLo
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ciplocalpoolfreeaddrs
            
            	The number of IP addresses available for use in the range of IP addresses
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolgroupcontainedin
            
            	This object relates an IP local pool to its IP pool group.  A null string indicates this IP local pool is not contained in a named IP pool group, but that it is contained in the base IP pool group.  An IP local pool can only belong to one IP pool group
            	**type**\:  str
            
            	**length:** 0..48
            
            .. attribute:: ciplocalpoolinuseaddrs
            
            	The number of IP addresses being used in the range of IP addresses
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolpriority
            
            	This object specifies priority of the IP local pool, where smaller value indicates the lower priority. The priority value is used in assigning IP Address  from local pools
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: ciplocalpoolrowstatus
            
            	This object facilitates the creation, or deletion of a conceptual row in this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
            _revision = '2007-11-12'

            def __init__(self):
                super(CiscoIpLocalPoolMib.Ciplocalpoolconfigtable.Ciplocalpoolconfigentry, self).__init__()

                self.yang_name = "cIpLocalPoolConfigEntry"
                self.yang_parent_name = "cIpLocalPoolConfigTable"

                self.ciplocalpoolname = YLeaf(YType.str, "cIpLocalPoolName")

                self.ciplocalpooladdrtype = YLeaf(YType.enumeration, "cIpLocalPoolAddrType")

                self.ciplocalpooladdresslo = YLeaf(YType.str, "cIpLocalPoolAddressLo")

                self.ciplocalpooladdresshi = YLeaf(YType.str, "cIpLocalPoolAddressHi")

                self.ciplocalpoolfreeaddrs = YLeaf(YType.uint32, "cIpLocalPoolFreeAddrs")

                self.ciplocalpoolgroupcontainedin = YLeaf(YType.str, "cIpLocalPoolGroupContainedIn")

                self.ciplocalpoolinuseaddrs = YLeaf(YType.uint32, "cIpLocalPoolInUseAddrs")

                self.ciplocalpoolpriority = YLeaf(YType.uint32, "cIpLocalPoolPriority")

                self.ciplocalpoolrowstatus = YLeaf(YType.enumeration, "cIpLocalPoolRowStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciplocalpoolname",
                                "ciplocalpooladdrtype",
                                "ciplocalpooladdresslo",
                                "ciplocalpooladdresshi",
                                "ciplocalpoolfreeaddrs",
                                "ciplocalpoolgroupcontainedin",
                                "ciplocalpoolinuseaddrs",
                                "ciplocalpoolpriority",
                                "ciplocalpoolrowstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpLocalPoolMib.Ciplocalpoolconfigtable.Ciplocalpoolconfigentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpLocalPoolMib.Ciplocalpoolconfigtable.Ciplocalpoolconfigentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ciplocalpoolname.is_set or
                    self.ciplocalpooladdrtype.is_set or
                    self.ciplocalpooladdresslo.is_set or
                    self.ciplocalpooladdresshi.is_set or
                    self.ciplocalpoolfreeaddrs.is_set or
                    self.ciplocalpoolgroupcontainedin.is_set or
                    self.ciplocalpoolinuseaddrs.is_set or
                    self.ciplocalpoolpriority.is_set or
                    self.ciplocalpoolrowstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciplocalpoolname.yfilter != YFilter.not_set or
                    self.ciplocalpooladdrtype.yfilter != YFilter.not_set or
                    self.ciplocalpooladdresslo.yfilter != YFilter.not_set or
                    self.ciplocalpooladdresshi.yfilter != YFilter.not_set or
                    self.ciplocalpoolfreeaddrs.yfilter != YFilter.not_set or
                    self.ciplocalpoolgroupcontainedin.yfilter != YFilter.not_set or
                    self.ciplocalpoolinuseaddrs.yfilter != YFilter.not_set or
                    self.ciplocalpoolpriority.yfilter != YFilter.not_set or
                    self.ciplocalpoolrowstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cIpLocalPoolConfigEntry" + "[cIpLocalPoolName='" + self.ciplocalpoolname.get() + "']" + "[cIpLocalPoolAddrType='" + self.ciplocalpooladdrtype.get() + "']" + "[cIpLocalPoolAddressLo='" + self.ciplocalpooladdresslo.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/cIpLocalPoolConfigTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciplocalpoolname.is_set or self.ciplocalpoolname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolname.get_name_leafdata())
                if (self.ciplocalpooladdrtype.is_set or self.ciplocalpooladdrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpooladdrtype.get_name_leafdata())
                if (self.ciplocalpooladdresslo.is_set or self.ciplocalpooladdresslo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpooladdresslo.get_name_leafdata())
                if (self.ciplocalpooladdresshi.is_set or self.ciplocalpooladdresshi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpooladdresshi.get_name_leafdata())
                if (self.ciplocalpoolfreeaddrs.is_set or self.ciplocalpoolfreeaddrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolfreeaddrs.get_name_leafdata())
                if (self.ciplocalpoolgroupcontainedin.is_set or self.ciplocalpoolgroupcontainedin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolgroupcontainedin.get_name_leafdata())
                if (self.ciplocalpoolinuseaddrs.is_set or self.ciplocalpoolinuseaddrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolinuseaddrs.get_name_leafdata())
                if (self.ciplocalpoolpriority.is_set or self.ciplocalpoolpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolpriority.get_name_leafdata())
                if (self.ciplocalpoolrowstatus.is_set or self.ciplocalpoolrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolrowstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cIpLocalPoolName" or name == "cIpLocalPoolAddrType" or name == "cIpLocalPoolAddressLo" or name == "cIpLocalPoolAddressHi" or name == "cIpLocalPoolFreeAddrs" or name == "cIpLocalPoolGroupContainedIn" or name == "cIpLocalPoolInUseAddrs" or name == "cIpLocalPoolPriority" or name == "cIpLocalPoolRowStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cIpLocalPoolName"):
                    self.ciplocalpoolname = value
                    self.ciplocalpoolname.value_namespace = name_space
                    self.ciplocalpoolname.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolAddrType"):
                    self.ciplocalpooladdrtype = value
                    self.ciplocalpooladdrtype.value_namespace = name_space
                    self.ciplocalpooladdrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolAddressLo"):
                    self.ciplocalpooladdresslo = value
                    self.ciplocalpooladdresslo.value_namespace = name_space
                    self.ciplocalpooladdresslo.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolAddressHi"):
                    self.ciplocalpooladdresshi = value
                    self.ciplocalpooladdresshi.value_namespace = name_space
                    self.ciplocalpooladdresshi.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolFreeAddrs"):
                    self.ciplocalpoolfreeaddrs = value
                    self.ciplocalpoolfreeaddrs.value_namespace = name_space
                    self.ciplocalpoolfreeaddrs.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolGroupContainedIn"):
                    self.ciplocalpoolgroupcontainedin = value
                    self.ciplocalpoolgroupcontainedin.value_namespace = name_space
                    self.ciplocalpoolgroupcontainedin.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolInUseAddrs"):
                    self.ciplocalpoolinuseaddrs = value
                    self.ciplocalpoolinuseaddrs.value_namespace = name_space
                    self.ciplocalpoolinuseaddrs.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolPriority"):
                    self.ciplocalpoolpriority = value
                    self.ciplocalpoolpriority.value_namespace = name_space
                    self.ciplocalpoolpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolRowStatus"):
                    self.ciplocalpoolrowstatus = value
                    self.ciplocalpoolrowstatus.value_namespace = name_space
                    self.ciplocalpoolrowstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciplocalpoolconfigentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciplocalpoolconfigentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cIpLocalPoolConfigTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cIpLocalPoolConfigEntry"):
                for c in self.ciplocalpoolconfigentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpLocalPoolMib.Ciplocalpoolconfigtable.Ciplocalpoolconfigentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciplocalpoolconfigentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cIpLocalPoolConfigEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciplocalpoolgroupcontainstable(Entity):
        """
        A table which exposes the container/'containee' relationships
        between local IP pools and IP pool groups.
        
        Entries in this table are created or deleted as a by\-product of
        creating or deleting entries in the cIpLocalPoolConfigTable.
        
        When an entry is created and activated in the
        cIpLocalPoolConfigTable table, an entry in this table will come
        into existence if it does not already exist.
        
        When an entry is deleted in the cIpLocalPoolConfigTable table,
        if there is no other entry existing in that table with the same
        cIpLocalPoolGroupContainedIn and cIpLocalPoolName, the entry in
        this table with the respective cIpLocalPoolGroupName and
        cIpLocalPoolName indices will be removed.
        
        .. attribute:: ciplocalpoolgroupcontainsentry
        
        	Each entry describes single container/'containee' relationship.  Pool names can only be associated with one group.  Pools carry implicit group identifiers because pool names can only be associated with one group.  An entry in this table describes such an association
        	**type**\: list of    :py:class:`Ciplocalpoolgroupcontainsentry <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable.Ciplocalpoolgroupcontainsentry>`
        
        

        """

        _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
        _revision = '2007-11-12'

        def __init__(self):
            super(CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable, self).__init__()

            self.yang_name = "cIpLocalPoolGroupContainsTable"
            self.yang_parent_name = "CISCO-IP-LOCAL-POOL-MIB"

            self.ciplocalpoolgroupcontainsentry = YList(self)

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
                        super(CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable, self).__setattr__(name, value)


        class Ciplocalpoolgroupcontainsentry(Entity):
            """
            Each entry describes single container/'containee'
            relationship.
            
            Pool names can only be associated with one group.  Pools carry
            implicit group identifiers because pool names can only be
            associated with one group.  An entry in this table describes
            such an association.
            
            .. attribute:: ciplocalpoolgroupname  <key>
            
            	A unique group name that identifies the IP pool group.  The null string represents the base IP pool group
            	**type**\:  str
            
            	**length:** 0..48
            
            .. attribute:: ciplocalpoolchildindex  <key>
            
            	The value of cIpLocalPoolName for the contained IP local pool
            	**type**\:  str
            
            	**length:** 1..48
            
            

            """

            _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
            _revision = '2007-11-12'

            def __init__(self):
                super(CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable.Ciplocalpoolgroupcontainsentry, self).__init__()

                self.yang_name = "cIpLocalPoolGroupContainsEntry"
                self.yang_parent_name = "cIpLocalPoolGroupContainsTable"

                self.ciplocalpoolgroupname = YLeaf(YType.str, "cIpLocalPoolGroupName")

                self.ciplocalpoolchildindex = YLeaf(YType.str, "cIpLocalPoolChildIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciplocalpoolgroupname",
                                "ciplocalpoolchildindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable.Ciplocalpoolgroupcontainsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable.Ciplocalpoolgroupcontainsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ciplocalpoolgroupname.is_set or
                    self.ciplocalpoolchildindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciplocalpoolgroupname.yfilter != YFilter.not_set or
                    self.ciplocalpoolchildindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cIpLocalPoolGroupContainsEntry" + "[cIpLocalPoolGroupName='" + self.ciplocalpoolgroupname.get() + "']" + "[cIpLocalPoolChildIndex='" + self.ciplocalpoolchildindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/cIpLocalPoolGroupContainsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciplocalpoolgroupname.is_set or self.ciplocalpoolgroupname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolgroupname.get_name_leafdata())
                if (self.ciplocalpoolchildindex.is_set or self.ciplocalpoolchildindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolchildindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cIpLocalPoolGroupName" or name == "cIpLocalPoolChildIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cIpLocalPoolGroupName"):
                    self.ciplocalpoolgroupname = value
                    self.ciplocalpoolgroupname.value_namespace = name_space
                    self.ciplocalpoolgroupname.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolChildIndex"):
                    self.ciplocalpoolchildindex = value
                    self.ciplocalpoolchildindex.value_namespace = name_space
                    self.ciplocalpoolchildindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciplocalpoolgroupcontainsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciplocalpoolgroupcontainsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cIpLocalPoolGroupContainsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cIpLocalPoolGroupContainsEntry"):
                for c in self.ciplocalpoolgroupcontainsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable.Ciplocalpoolgroupcontainsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciplocalpoolgroupcontainsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cIpLocalPoolGroupContainsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciplocalpoolgrouptable(Entity):
        """
        This table provides statistics for configured IP pool groups.
        
        Entries in this table are created as the result of adding a new
        IP pool group to the cIpLocalPoolConfigTable.
        
        Entries in this table are deleted as the result of removing all
        IP local pools that are contained in an IP pool group in the
        cIpLocalPoolConfigTable.
        
        An entry in this table is uniquely indexed by IP pool group
        name.
        
        .. attribute:: ciplocalpoolgroupentry
        
        	Each entry provides information about a particular IP pool group and the number of free and used addresses in an IP pool group
        	**type**\: list of    :py:class:`Ciplocalpoolgroupentry <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CiscoIpLocalPoolMib.Ciplocalpoolgrouptable.Ciplocalpoolgroupentry>`
        
        

        """

        _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
        _revision = '2007-11-12'

        def __init__(self):
            super(CiscoIpLocalPoolMib.Ciplocalpoolgrouptable, self).__init__()

            self.yang_name = "cIpLocalPoolGroupTable"
            self.yang_parent_name = "CISCO-IP-LOCAL-POOL-MIB"

            self.ciplocalpoolgroupentry = YList(self)

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
                        super(CiscoIpLocalPoolMib.Ciplocalpoolgrouptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpLocalPoolMib.Ciplocalpoolgrouptable, self).__setattr__(name, value)


        class Ciplocalpoolgroupentry(Entity):
            """
            Each entry provides information about a particular IP pool
            group and the number of free and used addresses in an IP pool
            group.
            
            .. attribute:: ciplocalpoolgroupname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 0..48
            
            	**refers to**\:  :py:class:`ciplocalpoolgroupname <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable.Ciplocalpoolgroupcontainsentry>`
            
            .. attribute:: ciplocalpoolgroupfreeaddrs
            
            	The number of IP addresses available for use in the IP pool group
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolgroupinuseaddrs
            
            	The number of IP addresses that have been allocated from the IP pool group
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
            _revision = '2007-11-12'

            def __init__(self):
                super(CiscoIpLocalPoolMib.Ciplocalpoolgrouptable.Ciplocalpoolgroupentry, self).__init__()

                self.yang_name = "cIpLocalPoolGroupEntry"
                self.yang_parent_name = "cIpLocalPoolGroupTable"

                self.ciplocalpoolgroupname = YLeaf(YType.str, "cIpLocalPoolGroupName")

                self.ciplocalpoolgroupfreeaddrs = YLeaf(YType.uint32, "cIpLocalPoolGroupFreeAddrs")

                self.ciplocalpoolgroupinuseaddrs = YLeaf(YType.uint32, "cIpLocalPoolGroupInUseAddrs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciplocalpoolgroupname",
                                "ciplocalpoolgroupfreeaddrs",
                                "ciplocalpoolgroupinuseaddrs") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpLocalPoolMib.Ciplocalpoolgrouptable.Ciplocalpoolgroupentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpLocalPoolMib.Ciplocalpoolgrouptable.Ciplocalpoolgroupentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ciplocalpoolgroupname.is_set or
                    self.ciplocalpoolgroupfreeaddrs.is_set or
                    self.ciplocalpoolgroupinuseaddrs.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciplocalpoolgroupname.yfilter != YFilter.not_set or
                    self.ciplocalpoolgroupfreeaddrs.yfilter != YFilter.not_set or
                    self.ciplocalpoolgroupinuseaddrs.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cIpLocalPoolGroupEntry" + "[cIpLocalPoolGroupName='" + self.ciplocalpoolgroupname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/cIpLocalPoolGroupTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciplocalpoolgroupname.is_set or self.ciplocalpoolgroupname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolgroupname.get_name_leafdata())
                if (self.ciplocalpoolgroupfreeaddrs.is_set or self.ciplocalpoolgroupfreeaddrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolgroupfreeaddrs.get_name_leafdata())
                if (self.ciplocalpoolgroupinuseaddrs.is_set or self.ciplocalpoolgroupinuseaddrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolgroupinuseaddrs.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cIpLocalPoolGroupName" or name == "cIpLocalPoolGroupFreeAddrs" or name == "cIpLocalPoolGroupInUseAddrs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cIpLocalPoolGroupName"):
                    self.ciplocalpoolgroupname = value
                    self.ciplocalpoolgroupname.value_namespace = name_space
                    self.ciplocalpoolgroupname.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolGroupFreeAddrs"):
                    self.ciplocalpoolgroupfreeaddrs = value
                    self.ciplocalpoolgroupfreeaddrs.value_namespace = name_space
                    self.ciplocalpoolgroupfreeaddrs.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolGroupInUseAddrs"):
                    self.ciplocalpoolgroupinuseaddrs = value
                    self.ciplocalpoolgroupinuseaddrs.value_namespace = name_space
                    self.ciplocalpoolgroupinuseaddrs.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciplocalpoolgroupentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciplocalpoolgroupentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cIpLocalPoolGroupTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cIpLocalPoolGroupEntry"):
                for c in self.ciplocalpoolgroupentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpLocalPoolMib.Ciplocalpoolgrouptable.Ciplocalpoolgroupentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciplocalpoolgroupentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cIpLocalPoolGroupEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciplocalpoolstatstable(Entity):
        """
        A table providing statistics for each IP local pool.
        
        Entries in this table are created as the result of adding a new
        IP local pool to the cIpLocalPoolConfigTable.
        
        Entries in this table are deleted as the result of removing all
        the address ranges that are contained in an IP local pool in the
        cIpLocalPoolConfigTable.
        
        Entries in this table are uniquely indexed by the name of the IP
        local pool.
        
        .. attribute:: ciplocalpoolstatsentry
        
        	Each entry provides statistical information about a particular IP local pool, and the total number of free and used addresses of all the ranges in an IP local pool
        	**type**\: list of    :py:class:`Ciplocalpoolstatsentry <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CiscoIpLocalPoolMib.Ciplocalpoolstatstable.Ciplocalpoolstatsentry>`
        
        

        """

        _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
        _revision = '2007-11-12'

        def __init__(self):
            super(CiscoIpLocalPoolMib.Ciplocalpoolstatstable, self).__init__()

            self.yang_name = "cIpLocalPoolStatsTable"
            self.yang_parent_name = "CISCO-IP-LOCAL-POOL-MIB"

            self.ciplocalpoolstatsentry = YList(self)

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
                        super(CiscoIpLocalPoolMib.Ciplocalpoolstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpLocalPoolMib.Ciplocalpoolstatstable, self).__setattr__(name, value)


        class Ciplocalpoolstatsentry(Entity):
            """
            Each entry provides statistical information about a particular
            IP local pool, and the total number of free and used addresses
            of all the ranges in an IP local pool.
            
            .. attribute:: ciplocalpoolname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..48
            
            	**refers to**\:  :py:class:`ciplocalpoolname <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CiscoIpLocalPoolMib.Ciplocalpoolconfigtable.Ciplocalpoolconfigentry>`
            
            .. attribute:: ciplocalpoolpercentaddrthldhi
            
            	When the percentage of used addresses in an IP local pool is equal or exceeds this threshold value, a cilpPercentAddrUsedHiNotif notification will be generated. Once the notification is generated, it will be disarmed and it will not be generated again until the number of used addresses falls below the value indicated by cIpLocalPoolPercentAddrThldLo.  The value of this object should never be smaller than the value of cIpLocalPoolPercentAddrThldLo
            	**type**\:  int
            
            	**range:** 0..100
            
            .. attribute:: ciplocalpoolpercentaddrthldlo
            
            	When the percentage of used addresses in an IP local pool falls below this threshold value, a cilpPercentAddrUsedLoNotif notification will be generated.  Once the notification is generated, it will be disarmed and it will not be generated again until the number of used addresses equals or exceeds the value indicated by cIpLocalPoolPercentAddrThldHi.  The value of this object should never be greater than the value of cIpLocalPoolPercentAddrThldHi
            	**type**\:  int
            
            	**range:** 0..100
            
            .. attribute:: ciplocalpoolstatfreeaddrs
            
            	The number of IP addresses available for use in this IP local pool
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolstathiwaterusedaddrs
            
            	This object contains the high water mark of used addresses in an IP local pool since pool creation, since the system was restarted, or since this object was reset, whichever occurred last.  This object can only be set to zero, and by doing so, it is reset to the value of cIpLocalPoolStatInUseAddrs.  Since the number of addresses in a pool can be reduced (e.g. by deleting one of its ranges), the value of this object may be greater than the sum of cIpLocalPoolStatFreeAddrs and cIpLocalPoolStatInUseAddrs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolstatinuseaddrs
            
            	The number of IP addresses being used in this IP local pool
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolstatinuseaddrthldhi
            
            	When the number of used addresses in an IP local pool is equal or exceeds this threshold value, a ciscoIpLocalPoolInUseAddrNoti notification will be generated. Once this notification is generated, it will be disarmed and it will not be generated again until the number of used address falls below the value indicated by cIpLocalPoolStatInUseAddrThldLo.  The value of this object should never be smaller than the value of cIpLocalPoolStatInUseAddrThldLo
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolstatinuseaddrthldlo
            
            	When the number of used addresses in an IP local pool falls below this threshold value, the ciscoIpLocalPoolInUseAddrNoti notification will be rearmed.  The value of this object should never be greater than the value of cIpLocalPoolStatInUseAddrThldHi
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
            _revision = '2007-11-12'

            def __init__(self):
                super(CiscoIpLocalPoolMib.Ciplocalpoolstatstable.Ciplocalpoolstatsentry, self).__init__()

                self.yang_name = "cIpLocalPoolStatsEntry"
                self.yang_parent_name = "cIpLocalPoolStatsTable"

                self.ciplocalpoolname = YLeaf(YType.str, "cIpLocalPoolName")

                self.ciplocalpoolpercentaddrthldhi = YLeaf(YType.uint32, "cIpLocalPoolPercentAddrThldHi")

                self.ciplocalpoolpercentaddrthldlo = YLeaf(YType.uint32, "cIpLocalPoolPercentAddrThldLo")

                self.ciplocalpoolstatfreeaddrs = YLeaf(YType.uint32, "cIpLocalPoolStatFreeAddrs")

                self.ciplocalpoolstathiwaterusedaddrs = YLeaf(YType.uint32, "cIpLocalPoolStatHiWaterUsedAddrs")

                self.ciplocalpoolstatinuseaddrs = YLeaf(YType.uint32, "cIpLocalPoolStatInUseAddrs")

                self.ciplocalpoolstatinuseaddrthldhi = YLeaf(YType.uint32, "cIpLocalPoolStatInUseAddrThldHi")

                self.ciplocalpoolstatinuseaddrthldlo = YLeaf(YType.uint32, "cIpLocalPoolStatInUseAddrThldLo")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciplocalpoolname",
                                "ciplocalpoolpercentaddrthldhi",
                                "ciplocalpoolpercentaddrthldlo",
                                "ciplocalpoolstatfreeaddrs",
                                "ciplocalpoolstathiwaterusedaddrs",
                                "ciplocalpoolstatinuseaddrs",
                                "ciplocalpoolstatinuseaddrthldhi",
                                "ciplocalpoolstatinuseaddrthldlo") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpLocalPoolMib.Ciplocalpoolstatstable.Ciplocalpoolstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpLocalPoolMib.Ciplocalpoolstatstable.Ciplocalpoolstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ciplocalpoolname.is_set or
                    self.ciplocalpoolpercentaddrthldhi.is_set or
                    self.ciplocalpoolpercentaddrthldlo.is_set or
                    self.ciplocalpoolstatfreeaddrs.is_set or
                    self.ciplocalpoolstathiwaterusedaddrs.is_set or
                    self.ciplocalpoolstatinuseaddrs.is_set or
                    self.ciplocalpoolstatinuseaddrthldhi.is_set or
                    self.ciplocalpoolstatinuseaddrthldlo.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciplocalpoolname.yfilter != YFilter.not_set or
                    self.ciplocalpoolpercentaddrthldhi.yfilter != YFilter.not_set or
                    self.ciplocalpoolpercentaddrthldlo.yfilter != YFilter.not_set or
                    self.ciplocalpoolstatfreeaddrs.yfilter != YFilter.not_set or
                    self.ciplocalpoolstathiwaterusedaddrs.yfilter != YFilter.not_set or
                    self.ciplocalpoolstatinuseaddrs.yfilter != YFilter.not_set or
                    self.ciplocalpoolstatinuseaddrthldhi.yfilter != YFilter.not_set or
                    self.ciplocalpoolstatinuseaddrthldlo.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cIpLocalPoolStatsEntry" + "[cIpLocalPoolName='" + self.ciplocalpoolname.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/cIpLocalPoolStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciplocalpoolname.is_set or self.ciplocalpoolname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolname.get_name_leafdata())
                if (self.ciplocalpoolpercentaddrthldhi.is_set or self.ciplocalpoolpercentaddrthldhi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolpercentaddrthldhi.get_name_leafdata())
                if (self.ciplocalpoolpercentaddrthldlo.is_set or self.ciplocalpoolpercentaddrthldlo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolpercentaddrthldlo.get_name_leafdata())
                if (self.ciplocalpoolstatfreeaddrs.is_set or self.ciplocalpoolstatfreeaddrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolstatfreeaddrs.get_name_leafdata())
                if (self.ciplocalpoolstathiwaterusedaddrs.is_set or self.ciplocalpoolstathiwaterusedaddrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolstathiwaterusedaddrs.get_name_leafdata())
                if (self.ciplocalpoolstatinuseaddrs.is_set or self.ciplocalpoolstatinuseaddrs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolstatinuseaddrs.get_name_leafdata())
                if (self.ciplocalpoolstatinuseaddrthldhi.is_set or self.ciplocalpoolstatinuseaddrthldhi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolstatinuseaddrthldhi.get_name_leafdata())
                if (self.ciplocalpoolstatinuseaddrthldlo.is_set or self.ciplocalpoolstatinuseaddrthldlo.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolstatinuseaddrthldlo.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cIpLocalPoolName" or name == "cIpLocalPoolPercentAddrThldHi" or name == "cIpLocalPoolPercentAddrThldLo" or name == "cIpLocalPoolStatFreeAddrs" or name == "cIpLocalPoolStatHiWaterUsedAddrs" or name == "cIpLocalPoolStatInUseAddrs" or name == "cIpLocalPoolStatInUseAddrThldHi" or name == "cIpLocalPoolStatInUseAddrThldLo"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cIpLocalPoolName"):
                    self.ciplocalpoolname = value
                    self.ciplocalpoolname.value_namespace = name_space
                    self.ciplocalpoolname.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolPercentAddrThldHi"):
                    self.ciplocalpoolpercentaddrthldhi = value
                    self.ciplocalpoolpercentaddrthldhi.value_namespace = name_space
                    self.ciplocalpoolpercentaddrthldhi.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolPercentAddrThldLo"):
                    self.ciplocalpoolpercentaddrthldlo = value
                    self.ciplocalpoolpercentaddrthldlo.value_namespace = name_space
                    self.ciplocalpoolpercentaddrthldlo.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolStatFreeAddrs"):
                    self.ciplocalpoolstatfreeaddrs = value
                    self.ciplocalpoolstatfreeaddrs.value_namespace = name_space
                    self.ciplocalpoolstatfreeaddrs.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolStatHiWaterUsedAddrs"):
                    self.ciplocalpoolstathiwaterusedaddrs = value
                    self.ciplocalpoolstathiwaterusedaddrs.value_namespace = name_space
                    self.ciplocalpoolstathiwaterusedaddrs.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolStatInUseAddrs"):
                    self.ciplocalpoolstatinuseaddrs = value
                    self.ciplocalpoolstatinuseaddrs.value_namespace = name_space
                    self.ciplocalpoolstatinuseaddrs.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolStatInUseAddrThldHi"):
                    self.ciplocalpoolstatinuseaddrthldhi = value
                    self.ciplocalpoolstatinuseaddrthldhi.value_namespace = name_space
                    self.ciplocalpoolstatinuseaddrthldhi.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolStatInUseAddrThldLo"):
                    self.ciplocalpoolstatinuseaddrthldlo = value
                    self.ciplocalpoolstatinuseaddrthldlo.value_namespace = name_space
                    self.ciplocalpoolstatinuseaddrthldlo.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciplocalpoolstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciplocalpoolstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cIpLocalPoolStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cIpLocalPoolStatsEntry"):
                for c in self.ciplocalpoolstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpLocalPoolMib.Ciplocalpoolstatstable.Ciplocalpoolstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciplocalpoolstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cIpLocalPoolStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ciplocalpoolalloctable(Entity):
        """
        This table lists all addresses that have been allocated out of
        an IP local pool.
        
        Entries in this table are created when a remote peer allocates
        an address from one of the IP local pools in the
        cIpLocalPoolConfigTable.
        
        Entries in this table are deleted when a remote peer deallocates
        an address from one of the IP local pool in the
        cIpLocalPoolConfigTable.
        
        Entries in this table are uniquely indexed by the name of the IP
        local pool, and the allocated address, together with its address
        type.
        
        .. attribute:: ciplocalpoolallocentry
        
        	Each entry refers to conceptual row that associates an IP addresses with the interface where the request was received, and the user that requested the address
        	**type**\: list of    :py:class:`Ciplocalpoolallocentry <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CiscoIpLocalPoolMib.Ciplocalpoolalloctable.Ciplocalpoolallocentry>`
        
        

        """

        _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
        _revision = '2007-11-12'

        def __init__(self):
            super(CiscoIpLocalPoolMib.Ciplocalpoolalloctable, self).__init__()

            self.yang_name = "cIpLocalPoolAllocTable"
            self.yang_parent_name = "CISCO-IP-LOCAL-POOL-MIB"

            self.ciplocalpoolallocentry = YList(self)

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
                        super(CiscoIpLocalPoolMib.Ciplocalpoolalloctable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoIpLocalPoolMib.Ciplocalpoolalloctable, self).__setattr__(name, value)


        class Ciplocalpoolallocentry(Entity):
            """
            Each entry refers to conceptual row that associates an IP
            addresses with the interface where the request was received, and
            the user that requested the address.
            
            .. attribute:: ciplocalpoolname  <key>
            
            	
            	**type**\:  str
            
            	**length:** 1..48
            
            	**refers to**\:  :py:class:`ciplocalpoolname <ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB.CiscoIpLocalPoolMib.Ciplocalpoolconfigtable.Ciplocalpoolconfigentry>`
            
            .. attribute:: ciplocalpoolallocaddrtype  <key>
            
            	This object specifies the address type of cIpLocalPoolAllocAddr
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ciplocalpoolallocaddr  <key>
            
            	This object specifies the allocated IP address.  The address type of this object is described by cIpLocalPoolAllocAddrType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ciplocalpoolallocifindex
            
            	This object indicates the interface from which the allocation message was sent.  In the case that the interface can not be determined, the value of this object will be zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciplocalpoolallocuser
            
            	This object indicates the user name of the person from whom the allocation message was sent.  In the case that the user name can not be determined, the value of this object will the null string
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-IP-LOCAL-POOL-MIB'
            _revision = '2007-11-12'

            def __init__(self):
                super(CiscoIpLocalPoolMib.Ciplocalpoolalloctable.Ciplocalpoolallocentry, self).__init__()

                self.yang_name = "cIpLocalPoolAllocEntry"
                self.yang_parent_name = "cIpLocalPoolAllocTable"

                self.ciplocalpoolname = YLeaf(YType.str, "cIpLocalPoolName")

                self.ciplocalpoolallocaddrtype = YLeaf(YType.enumeration, "cIpLocalPoolAllocAddrType")

                self.ciplocalpoolallocaddr = YLeaf(YType.str, "cIpLocalPoolAllocAddr")

                self.ciplocalpoolallocifindex = YLeaf(YType.int32, "cIpLocalPoolAllocIfIndex")

                self.ciplocalpoolallocuser = YLeaf(YType.str, "cIpLocalPoolAllocUser")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ciplocalpoolname",
                                "ciplocalpoolallocaddrtype",
                                "ciplocalpoolallocaddr",
                                "ciplocalpoolallocifindex",
                                "ciplocalpoolallocuser") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoIpLocalPoolMib.Ciplocalpoolalloctable.Ciplocalpoolallocentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoIpLocalPoolMib.Ciplocalpoolalloctable.Ciplocalpoolallocentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ciplocalpoolname.is_set or
                    self.ciplocalpoolallocaddrtype.is_set or
                    self.ciplocalpoolallocaddr.is_set or
                    self.ciplocalpoolallocifindex.is_set or
                    self.ciplocalpoolallocuser.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ciplocalpoolname.yfilter != YFilter.not_set or
                    self.ciplocalpoolallocaddrtype.yfilter != YFilter.not_set or
                    self.ciplocalpoolallocaddr.yfilter != YFilter.not_set or
                    self.ciplocalpoolallocifindex.yfilter != YFilter.not_set or
                    self.ciplocalpoolallocuser.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cIpLocalPoolAllocEntry" + "[cIpLocalPoolName='" + self.ciplocalpoolname.get() + "']" + "[cIpLocalPoolAllocAddrType='" + self.ciplocalpoolallocaddrtype.get() + "']" + "[cIpLocalPoolAllocAddr='" + self.ciplocalpoolallocaddr.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/cIpLocalPoolAllocTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ciplocalpoolname.is_set or self.ciplocalpoolname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolname.get_name_leafdata())
                if (self.ciplocalpoolallocaddrtype.is_set or self.ciplocalpoolallocaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolallocaddrtype.get_name_leafdata())
                if (self.ciplocalpoolallocaddr.is_set or self.ciplocalpoolallocaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolallocaddr.get_name_leafdata())
                if (self.ciplocalpoolallocifindex.is_set or self.ciplocalpoolallocifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolallocifindex.get_name_leafdata())
                if (self.ciplocalpoolallocuser.is_set or self.ciplocalpoolallocuser.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ciplocalpoolallocuser.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cIpLocalPoolName" or name == "cIpLocalPoolAllocAddrType" or name == "cIpLocalPoolAllocAddr" or name == "cIpLocalPoolAllocIfIndex" or name == "cIpLocalPoolAllocUser"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cIpLocalPoolName"):
                    self.ciplocalpoolname = value
                    self.ciplocalpoolname.value_namespace = name_space
                    self.ciplocalpoolname.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolAllocAddrType"):
                    self.ciplocalpoolallocaddrtype = value
                    self.ciplocalpoolallocaddrtype.value_namespace = name_space
                    self.ciplocalpoolallocaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolAllocAddr"):
                    self.ciplocalpoolallocaddr = value
                    self.ciplocalpoolallocaddr.value_namespace = name_space
                    self.ciplocalpoolallocaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolAllocIfIndex"):
                    self.ciplocalpoolallocifindex = value
                    self.ciplocalpoolallocifindex.value_namespace = name_space
                    self.ciplocalpoolallocifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cIpLocalPoolAllocUser"):
                    self.ciplocalpoolallocuser = value
                    self.ciplocalpoolallocuser.value_namespace = name_space
                    self.ciplocalpoolallocuser.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ciplocalpoolallocentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ciplocalpoolallocentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cIpLocalPoolAllocTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cIpLocalPoolAllocEntry"):
                for c in self.ciplocalpoolallocentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoIpLocalPoolMib.Ciplocalpoolalloctable.Ciplocalpoolallocentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ciplocalpoolallocentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cIpLocalPoolAllocEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ciplocalpoolalloctable is not None and self.ciplocalpoolalloctable.has_data()) or
            (self.ciplocalpoolconfig is not None and self.ciplocalpoolconfig.has_data()) or
            (self.ciplocalpoolconfigtable is not None and self.ciplocalpoolconfigtable.has_data()) or
            (self.ciplocalpoolgroupcontainstable is not None and self.ciplocalpoolgroupcontainstable.has_data()) or
            (self.ciplocalpoolgrouptable is not None and self.ciplocalpoolgrouptable.has_data()) or
            (self.ciplocalpoolstatstable is not None and self.ciplocalpoolstatstable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ciplocalpoolalloctable is not None and self.ciplocalpoolalloctable.has_operation()) or
            (self.ciplocalpoolconfig is not None and self.ciplocalpoolconfig.has_operation()) or
            (self.ciplocalpoolconfigtable is not None and self.ciplocalpoolconfigtable.has_operation()) or
            (self.ciplocalpoolgroupcontainstable is not None and self.ciplocalpoolgroupcontainstable.has_operation()) or
            (self.ciplocalpoolgrouptable is not None and self.ciplocalpoolgrouptable.has_operation()) or
            (self.ciplocalpoolstatstable is not None and self.ciplocalpoolstatstable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB" + path_buffer

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

        if (child_yang_name == "cIpLocalPoolAllocTable"):
            if (self.ciplocalpoolalloctable is None):
                self.ciplocalpoolalloctable = CiscoIpLocalPoolMib.Ciplocalpoolalloctable()
                self.ciplocalpoolalloctable.parent = self
                self._children_name_map["ciplocalpoolalloctable"] = "cIpLocalPoolAllocTable"
            return self.ciplocalpoolalloctable

        if (child_yang_name == "cIpLocalPoolConfig"):
            if (self.ciplocalpoolconfig is None):
                self.ciplocalpoolconfig = CiscoIpLocalPoolMib.Ciplocalpoolconfig()
                self.ciplocalpoolconfig.parent = self
                self._children_name_map["ciplocalpoolconfig"] = "cIpLocalPoolConfig"
            return self.ciplocalpoolconfig

        if (child_yang_name == "cIpLocalPoolConfigTable"):
            if (self.ciplocalpoolconfigtable is None):
                self.ciplocalpoolconfigtable = CiscoIpLocalPoolMib.Ciplocalpoolconfigtable()
                self.ciplocalpoolconfigtable.parent = self
                self._children_name_map["ciplocalpoolconfigtable"] = "cIpLocalPoolConfigTable"
            return self.ciplocalpoolconfigtable

        if (child_yang_name == "cIpLocalPoolGroupContainsTable"):
            if (self.ciplocalpoolgroupcontainstable is None):
                self.ciplocalpoolgroupcontainstable = CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable()
                self.ciplocalpoolgroupcontainstable.parent = self
                self._children_name_map["ciplocalpoolgroupcontainstable"] = "cIpLocalPoolGroupContainsTable"
            return self.ciplocalpoolgroupcontainstable

        if (child_yang_name == "cIpLocalPoolGroupTable"):
            if (self.ciplocalpoolgrouptable is None):
                self.ciplocalpoolgrouptable = CiscoIpLocalPoolMib.Ciplocalpoolgrouptable()
                self.ciplocalpoolgrouptable.parent = self
                self._children_name_map["ciplocalpoolgrouptable"] = "cIpLocalPoolGroupTable"
            return self.ciplocalpoolgrouptable

        if (child_yang_name == "cIpLocalPoolStatsTable"):
            if (self.ciplocalpoolstatstable is None):
                self.ciplocalpoolstatstable = CiscoIpLocalPoolMib.Ciplocalpoolstatstable()
                self.ciplocalpoolstatstable.parent = self
                self._children_name_map["ciplocalpoolstatstable"] = "cIpLocalPoolStatsTable"
            return self.ciplocalpoolstatstable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cIpLocalPoolAllocTable" or name == "cIpLocalPoolConfig" or name == "cIpLocalPoolConfigTable" or name == "cIpLocalPoolGroupContainsTable" or name == "cIpLocalPoolGroupTable" or name == "cIpLocalPoolStatsTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoIpLocalPoolMib()
        return self._top_entity

