""" CISCO_HSRP_EXT_MIB 

The Extension MIB module for the CISCO\-HSRP\-MIB which is
based on RFC2281.

This MIB provides an extension to the CISCO\-HSRP\-MIB which 
defines Cisco's proprietary Hot Standby Routing Protocol 
(HSRP), defined in RFC2281. The extensions cover assigning 
of secondary HSRP ip addresses, modifying an HSRP Group's 
priority by tracking the operational status of interfaces, 
etc. 

Terminology\:
HSRP is a protocol used amoung a group of routers for the 
purpose of selecting an active router and a standby router. 

An active router is the router of choice for routing 
packets.

A standby router is a router that takes over the routing 
duties when an active router fails, or when preset 
conditions have been met.

A HSRP group or a standby group is a set of routers 
which communicate using HSRP. An HSRP group has a group 
MAC address and a group IP address. These are the 
designated addresses. The active router assumes  
(i.e. inherits) these group addresses. An HSRP group is
identified by a ( ifIndex, cHsrpGrpNumber ) pair.

BIA stands for Burned In Address.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoHsrpExtMib(Entity):
    """
    
    
    .. attribute:: chsrpextifstandbytable
    
    	A table containing information about standby interfaces per HSRP group
    	**type**\:   :py:class:`Chsrpextifstandbytable <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CiscoHsrpExtMib.Chsrpextifstandbytable>`
    
    .. attribute:: chsrpextiftable
    
    	HSRP\-specific configurations for each physical interface
    	**type**\:   :py:class:`Chsrpextiftable <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CiscoHsrpExtMib.Chsrpextiftable>`
    
    .. attribute:: chsrpextiftrackedtable
    
    	A table containing information about tracked interfaces per HSRP group
    	**type**\:   :py:class:`Chsrpextiftrackedtable <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CiscoHsrpExtMib.Chsrpextiftrackedtable>`
    
    .. attribute:: chsrpextsecaddrtable
    
    	A table containing information about secondary HSRP IP Addresses per interface and group
    	**type**\:   :py:class:`Chsrpextsecaddrtable <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CiscoHsrpExtMib.Chsrpextsecaddrtable>`
    
    

    """

    _prefix = 'CISCO-HSRP-EXT-MIB'
    _revision = '2010-09-02'

    def __init__(self):
        super(CiscoHsrpExtMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-HSRP-EXT-MIB"
        self.yang_parent_name = "CISCO-HSRP-EXT-MIB"

        self.chsrpextifstandbytable = CiscoHsrpExtMib.Chsrpextifstandbytable()
        self.chsrpextifstandbytable.parent = self
        self._children_name_map["chsrpextifstandbytable"] = "cHsrpExtIfStandbyTable"
        self._children_yang_names.add("cHsrpExtIfStandbyTable")

        self.chsrpextiftable = CiscoHsrpExtMib.Chsrpextiftable()
        self.chsrpextiftable.parent = self
        self._children_name_map["chsrpextiftable"] = "cHsrpExtIfTable"
        self._children_yang_names.add("cHsrpExtIfTable")

        self.chsrpextiftrackedtable = CiscoHsrpExtMib.Chsrpextiftrackedtable()
        self.chsrpextiftrackedtable.parent = self
        self._children_name_map["chsrpextiftrackedtable"] = "cHsrpExtIfTrackedTable"
        self._children_yang_names.add("cHsrpExtIfTrackedTable")

        self.chsrpextsecaddrtable = CiscoHsrpExtMib.Chsrpextsecaddrtable()
        self.chsrpextsecaddrtable.parent = self
        self._children_name_map["chsrpextsecaddrtable"] = "cHsrpExtSecAddrTable"
        self._children_yang_names.add("cHsrpExtSecAddrTable")


    class Chsrpextiftrackedtable(Entity):
        """
        A table containing information about tracked interfaces per
        HSRP group.
        
        .. attribute:: chsrpextiftrackedentry
        
        	Each row of this table allows the tracking of one interface of the HSRP group which is identified by the (ifIndex, cHsrpGrpNumber) values in this table's INDEX clause. Weight(priority) is given to each and every interface tracked.  When a tracked interface is unavailable, the HSRP priority of the router is decreased. i.e cHsrpGrpPriority value assigned  to an HSRP group will reduce by the value assigned to cHsrpExtIfTrackedPriority. This reduces the likelihood  of a router with a failed key interface becoming the  active router.  Setting cHsrpExtIfTrackedRowStatus to active starts the tracking of cHsrpExtIfTracked by the HSRP group.  The value of cHsrpExtIfTrackedRowStatus may be set  to destroy at any time.  Entries may not be created via SNMP without explicitly setting cHsrpExtIfTrackedRowStatus to either 'createAndGo'  or 'createAndWait'.  Entries can be created and modified via the management protocol or by the device's local management interface.  If the row is not active, and a local management interface command modifies that row, the row may transition to active state.  A row entry in the cHsrpExtIfTrackedTable can not be created unless the corresponding row in the cHsrpGrpTable has been  created. If that corresponding row in cHsrpGrpTable is  deleted, the interfaces it tracks also get deleted.  A row which is not in active state will timeout after a configurable period (five minutes by default). This timeout period can be changed by setting cHsrpConfigTimeout
        	**type**\: list of    :py:class:`Chsrpextiftrackedentry <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CiscoHsrpExtMib.Chsrpextiftrackedtable.Chsrpextiftrackedentry>`
        
        

        """

        _prefix = 'CISCO-HSRP-EXT-MIB'
        _revision = '2010-09-02'

        def __init__(self):
            super(CiscoHsrpExtMib.Chsrpextiftrackedtable, self).__init__()

            self.yang_name = "cHsrpExtIfTrackedTable"
            self.yang_parent_name = "CISCO-HSRP-EXT-MIB"

            self.chsrpextiftrackedentry = YList(self)

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
                        super(CiscoHsrpExtMib.Chsrpextiftrackedtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoHsrpExtMib.Chsrpextiftrackedtable, self).__setattr__(name, value)


        class Chsrpextiftrackedentry(Entity):
            """
            Each row of this table allows the tracking of one
            interface of the HSRP group which is identified by the
            (ifIndex, cHsrpGrpNumber) values in this table's INDEX clause.
            Weight(priority) is given to each and every interface tracked. 
            When a tracked interface is unavailable, the HSRP priority of
            the router is decreased. i.e cHsrpGrpPriority value assigned 
            to an HSRP group will reduce by the value assigned to
            cHsrpExtIfTrackedPriority. This reduces the likelihood 
            of a router with a failed key interface becoming the 
            active router.
            
            Setting cHsrpExtIfTrackedRowStatus to active starts
            the tracking of cHsrpExtIfTracked by the HSRP group. 
            The value of cHsrpExtIfTrackedRowStatus may be set 
            to destroy at any time.
            
            Entries may not be created via SNMP without explicitly setting
            cHsrpExtIfTrackedRowStatus to either 'createAndGo' 
            or 'createAndWait'.
            
            Entries can be created and modified via the management
            protocol or by the device's local management interface.
            
            If the row is not active, and a local management interface
            command modifies that row, the row may transition to active
            state.
            
            A row entry in the cHsrpExtIfTrackedTable can not be created
            unless the corresponding row in the cHsrpGrpTable has been 
            created. If that corresponding row in cHsrpGrpTable is 
            deleted, the interfaces it tracks also get deleted.
            
            A row which is not in active state will timeout after a
            configurable period (five minutes by default). This timeout
            period can be changed by setting cHsrpConfigTimeout.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: chsrpgrpnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..255
            
            	**refers to**\:  :py:class:`chsrpgrpnumber <ydk.models.cisco_ios_xe.CISCO_HSRP_MIB.CiscoHsrpMib.Chsrpgrptable.Chsrpgrpentry>`
            
            .. attribute:: chsrpextiftracked  <key>
            
            	The ifIndex value of the tracked interface
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: chsrpextiftrackedipnone
            
            	This object specifies the disable HSRP IPv4 virtual IP address
            	**type**\:  bool
            
            	**status**\: deprecated
            
            .. attribute:: chsrpextiftrackedpriority
            
            	Priority of the tracked interface for the corresponding { ifIndex, cHsrpGrpNumber } pair. In the range of 0 to 255, 0 is the lowest priority and 255 is the highest. When a tracked  interface is unavailable, the cHsrpGrpPriority of the router  is decreased by the value of this object instance (If the  cHsrpGrpPriority is less than the  cHsrpExtIfTrackedPriority, then the HSRP priority  becomes 0). This allows a standby router to be configured  with a priority such that if the currently active router's  priority is lowered because the tracked interface goes down,  the standby router can takeover
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: chsrpextiftrackedrowstatus
            
            	The control that allows modification, creation, and deletion of entries. For detailed rules see the DESCRIPTION for cHsrpExtIfTrackedEntry
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'CISCO-HSRP-EXT-MIB'
            _revision = '2010-09-02'

            def __init__(self):
                super(CiscoHsrpExtMib.Chsrpextiftrackedtable.Chsrpextiftrackedentry, self).__init__()

                self.yang_name = "cHsrpExtIfTrackedEntry"
                self.yang_parent_name = "cHsrpExtIfTrackedTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.chsrpgrpnumber = YLeaf(YType.str, "cHsrpGrpNumber")

                self.chsrpextiftracked = YLeaf(YType.int32, "cHsrpExtIfTracked")

                self.chsrpextiftrackedipnone = YLeaf(YType.boolean, "cHsrpExtIfTrackedIpNone")

                self.chsrpextiftrackedpriority = YLeaf(YType.uint32, "cHsrpExtIfTrackedPriority")

                self.chsrpextiftrackedrowstatus = YLeaf(YType.enumeration, "cHsrpExtIfTrackedRowStatus")

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
                                "chsrpgrpnumber",
                                "chsrpextiftracked",
                                "chsrpextiftrackedipnone",
                                "chsrpextiftrackedpriority",
                                "chsrpextiftrackedrowstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoHsrpExtMib.Chsrpextiftrackedtable.Chsrpextiftrackedentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoHsrpExtMib.Chsrpextiftrackedtable.Chsrpextiftrackedentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.chsrpgrpnumber.is_set or
                    self.chsrpextiftracked.is_set or
                    self.chsrpextiftrackedipnone.is_set or
                    self.chsrpextiftrackedpriority.is_set or
                    self.chsrpextiftrackedrowstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.chsrpgrpnumber.yfilter != YFilter.not_set or
                    self.chsrpextiftracked.yfilter != YFilter.not_set or
                    self.chsrpextiftrackedipnone.yfilter != YFilter.not_set or
                    self.chsrpextiftrackedpriority.yfilter != YFilter.not_set or
                    self.chsrpextiftrackedrowstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cHsrpExtIfTrackedEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[cHsrpGrpNumber='" + self.chsrpgrpnumber.get() + "']" + "[cHsrpExtIfTracked='" + self.chsrpextiftracked.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/cHsrpExtIfTrackedTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.chsrpgrpnumber.is_set or self.chsrpgrpnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrpnumber.get_name_leafdata())
                if (self.chsrpextiftracked.is_set or self.chsrpextiftracked.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpextiftracked.get_name_leafdata())
                if (self.chsrpextiftrackedipnone.is_set or self.chsrpextiftrackedipnone.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpextiftrackedipnone.get_name_leafdata())
                if (self.chsrpextiftrackedpriority.is_set or self.chsrpextiftrackedpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpextiftrackedpriority.get_name_leafdata())
                if (self.chsrpextiftrackedrowstatus.is_set or self.chsrpextiftrackedrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpextiftrackedrowstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cHsrpGrpNumber" or name == "cHsrpExtIfTracked" or name == "cHsrpExtIfTrackedIpNone" or name == "cHsrpExtIfTrackedPriority" or name == "cHsrpExtIfTrackedRowStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpNumber"):
                    self.chsrpgrpnumber = value
                    self.chsrpgrpnumber.value_namespace = name_space
                    self.chsrpgrpnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpExtIfTracked"):
                    self.chsrpextiftracked = value
                    self.chsrpextiftracked.value_namespace = name_space
                    self.chsrpextiftracked.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpExtIfTrackedIpNone"):
                    self.chsrpextiftrackedipnone = value
                    self.chsrpextiftrackedipnone.value_namespace = name_space
                    self.chsrpextiftrackedipnone.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpExtIfTrackedPriority"):
                    self.chsrpextiftrackedpriority = value
                    self.chsrpextiftrackedpriority.value_namespace = name_space
                    self.chsrpextiftrackedpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpExtIfTrackedRowStatus"):
                    self.chsrpextiftrackedrowstatus = value
                    self.chsrpextiftrackedrowstatus.value_namespace = name_space
                    self.chsrpextiftrackedrowstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.chsrpextiftrackedentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.chsrpextiftrackedentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cHsrpExtIfTrackedTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cHsrpExtIfTrackedEntry"):
                for c in self.chsrpextiftrackedentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoHsrpExtMib.Chsrpextiftrackedtable.Chsrpextiftrackedentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.chsrpextiftrackedentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cHsrpExtIfTrackedEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Chsrpextsecaddrtable(Entity):
        """
        A table containing information about secondary HSRP IP
        Addresses per interface and group.
        
        .. attribute:: chsrpextsecaddrentry
        
        	The CHsrpExtSecAddrEntry allows creation of secondary IP Addresses for each cHsrpGrpEntry row.  Secondary addresses can be added by setting  cHsrpExtSecAddrRowStatus to be active. The value of cHsrpExtSecAddrRowStatus may be set to destroy at any time.  Entries may not be created via SNMP without explicitly setting cHsrpExtSecAddrRowStatus to either 'createAndGo' or 'createAndWait'.  Entries can be created and modified via the management protocol or by the device's local management interface.  If the row is not active, and a local management interface command modifies that row, the row may transition to active state.  A row which is not in active state will timeout after a configurable period (five minutes by default). This timeout period can be changed by setting cHsrpConfigTimeout.  Before creation of a cHsrpExtSecAddrEntry row, either cHsrpGrpConfiguredVirtualIpAddr or  cHsrpGrpLearnedVirtualIpAddr must have a valid IP Address. This is because a secondary ip address cannot be created unless the primary ip address has already been set.  To create a new cHsrpExtSecAddrEntry row, a management  station should choose the ifIndex of the interface which is to  be added as part of an HSRP group. Also, an HSRP group number  and a cHsrpExtSecAddrAddress should be chosen.  Deleting a {ifIndex, cHsrpGrpNumber} row in the cHsrpGrpTable will delete all corresponding rows in the cHsrpExtSecAddrTable. Deleting a primary address value in the cHsrpGrpEntry row will delete all secondary addresses for the same {ifIndex, cHsrpGrpNumber} pair
        	**type**\: list of    :py:class:`Chsrpextsecaddrentry <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CiscoHsrpExtMib.Chsrpextsecaddrtable.Chsrpextsecaddrentry>`
        
        

        """

        _prefix = 'CISCO-HSRP-EXT-MIB'
        _revision = '2010-09-02'

        def __init__(self):
            super(CiscoHsrpExtMib.Chsrpextsecaddrtable, self).__init__()

            self.yang_name = "cHsrpExtSecAddrTable"
            self.yang_parent_name = "CISCO-HSRP-EXT-MIB"

            self.chsrpextsecaddrentry = YList(self)

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
                        super(CiscoHsrpExtMib.Chsrpextsecaddrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoHsrpExtMib.Chsrpextsecaddrtable, self).__setattr__(name, value)


        class Chsrpextsecaddrentry(Entity):
            """
            The CHsrpExtSecAddrEntry allows creation of secondary
            IP Addresses for each cHsrpGrpEntry row.
            
            Secondary addresses can be added by setting 
            cHsrpExtSecAddrRowStatus to be active. The value of
            cHsrpExtSecAddrRowStatus may be set to destroy at any
            time.
            
            Entries may not be created via SNMP without explicitly setting
            cHsrpExtSecAddrRowStatus to either 'createAndGo'
            or 'createAndWait'.
            
            Entries can be created and modified via the management
            protocol or by the device's local management interface.
            
            If the row is not active, and a local management interface
            command modifies that row, the row may transition to active
            state.
            
            A row which is not in active state will timeout after a
            configurable period (five minutes by default). This timeout
            period can be changed by setting cHsrpConfigTimeout.
            
            Before creation of a cHsrpExtSecAddrEntry row,
            either cHsrpGrpConfiguredVirtualIpAddr or 
            cHsrpGrpLearnedVirtualIpAddr must have a valid IP Address.
            This is because a secondary ip address cannot be created
            unless the primary ip address has already been set.
            
            To create a new cHsrpExtSecAddrEntry row, a management 
            station should choose the ifIndex of the interface which is to 
            be added as part of an HSRP group. Also, an HSRP group number 
            and a cHsrpExtSecAddrAddress should be chosen.
            
            Deleting a {ifIndex, cHsrpGrpNumber} row in the
            cHsrpGrpTable will delete all corresponding
            rows in the cHsrpExtSecAddrTable.
            Deleting a primary address value in the cHsrpGrpEntry row
            will delete all secondary addresses for the same
            {ifIndex, cHsrpGrpNumber} pair.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: chsrpgrpnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..255
            
            	**refers to**\:  :py:class:`chsrpgrpnumber <ydk.models.cisco_ios_xe.CISCO_HSRP_MIB.CiscoHsrpMib.Chsrpgrptable.Chsrpgrpentry>`
            
            .. attribute:: chsrpextsecaddraddress  <key>
            
            	A secondary IpAddress for the {ifIndex, cHsrpGrpNumber} pair. As explained in the DESCRIPTION for cHsrpExtSecAddrEntry, a primary address must exist before a secondary address for  the same {ifIndex, cHsrpGrpNumber} pair can be created
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: chsrpextsecaddrrowstatus
            
            	The control that allows modification, creation, and deletion of entries. For detailed rules see the DESCRIPTION for cHsrpExtSecAddrEntry
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'CISCO-HSRP-EXT-MIB'
            _revision = '2010-09-02'

            def __init__(self):
                super(CiscoHsrpExtMib.Chsrpextsecaddrtable.Chsrpextsecaddrentry, self).__init__()

                self.yang_name = "cHsrpExtSecAddrEntry"
                self.yang_parent_name = "cHsrpExtSecAddrTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.chsrpgrpnumber = YLeaf(YType.str, "cHsrpGrpNumber")

                self.chsrpextsecaddraddress = YLeaf(YType.str, "cHsrpExtSecAddrAddress")

                self.chsrpextsecaddrrowstatus = YLeaf(YType.enumeration, "cHsrpExtSecAddrRowStatus")

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
                                "chsrpgrpnumber",
                                "chsrpextsecaddraddress",
                                "chsrpextsecaddrrowstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoHsrpExtMib.Chsrpextsecaddrtable.Chsrpextsecaddrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoHsrpExtMib.Chsrpextsecaddrtable.Chsrpextsecaddrentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.chsrpgrpnumber.is_set or
                    self.chsrpextsecaddraddress.is_set or
                    self.chsrpextsecaddrrowstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.chsrpgrpnumber.yfilter != YFilter.not_set or
                    self.chsrpextsecaddraddress.yfilter != YFilter.not_set or
                    self.chsrpextsecaddrrowstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cHsrpExtSecAddrEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[cHsrpGrpNumber='" + self.chsrpgrpnumber.get() + "']" + "[cHsrpExtSecAddrAddress='" + self.chsrpextsecaddraddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/cHsrpExtSecAddrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.chsrpgrpnumber.is_set or self.chsrpgrpnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrpnumber.get_name_leafdata())
                if (self.chsrpextsecaddraddress.is_set or self.chsrpextsecaddraddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpextsecaddraddress.get_name_leafdata())
                if (self.chsrpextsecaddrrowstatus.is_set or self.chsrpextsecaddrrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpextsecaddrrowstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cHsrpGrpNumber" or name == "cHsrpExtSecAddrAddress" or name == "cHsrpExtSecAddrRowStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpNumber"):
                    self.chsrpgrpnumber = value
                    self.chsrpgrpnumber.value_namespace = name_space
                    self.chsrpgrpnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpExtSecAddrAddress"):
                    self.chsrpextsecaddraddress = value
                    self.chsrpextsecaddraddress.value_namespace = name_space
                    self.chsrpextsecaddraddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpExtSecAddrRowStatus"):
                    self.chsrpextsecaddrrowstatus = value
                    self.chsrpextsecaddrrowstatus.value_namespace = name_space
                    self.chsrpextsecaddrrowstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.chsrpextsecaddrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.chsrpextsecaddrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cHsrpExtSecAddrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cHsrpExtSecAddrEntry"):
                for c in self.chsrpextsecaddrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoHsrpExtMib.Chsrpextsecaddrtable.Chsrpextsecaddrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.chsrpextsecaddrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cHsrpExtSecAddrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Chsrpextifstandbytable(Entity):
        """
        A table containing information about standby
        interfaces per HSRP group.
        
        .. attribute:: chsrpextifstandbyentry
        
        	The cHsrpExtIfStandbyEntry allows an HSRP group interface to track one or more standby interfaces.  To create a new cHsrpExtIfStandbyEntry row, a management station should choose the ifIndex of the interface which is to be added as part of an HSRP group. Also, an HSRP group number and a cHsrpExtIfStandbyIndex should be chosen
        	**type**\: list of    :py:class:`Chsrpextifstandbyentry <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CiscoHsrpExtMib.Chsrpextifstandbytable.Chsrpextifstandbyentry>`
        
        

        """

        _prefix = 'CISCO-HSRP-EXT-MIB'
        _revision = '2010-09-02'

        def __init__(self):
            super(CiscoHsrpExtMib.Chsrpextifstandbytable, self).__init__()

            self.yang_name = "cHsrpExtIfStandbyTable"
            self.yang_parent_name = "CISCO-HSRP-EXT-MIB"

            self.chsrpextifstandbyentry = YList(self)

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
                        super(CiscoHsrpExtMib.Chsrpextifstandbytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoHsrpExtMib.Chsrpextifstandbytable, self).__setattr__(name, value)


        class Chsrpextifstandbyentry(Entity):
            """
            The cHsrpExtIfStandbyEntry allows an HSRP group
            interface to track one or more standby interfaces.
            
            To create a new cHsrpExtIfStandbyEntry row, a
            management station should choose the ifIndex of
            the interface which is to be added as part of an
            HSRP group. Also, an HSRP group number and a
            cHsrpExtIfStandbyIndex should be chosen.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: chsrpgrpnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..255
            
            	**refers to**\:  :py:class:`chsrpgrpnumber <ydk.models.cisco_ios_xe.CISCO_HSRP_MIB.CiscoHsrpMib.Chsrpgrptable.Chsrpgrpentry>`
            
            .. attribute:: chsrpextifstandbyindex  <key>
            
            	This object defines the index of the standby table
            	**type**\:  int
            
            	**range:** 1..4
            
            .. attribute:: chsrpextifstandbydestaddr
            
            	This object specifies the destination IP address of the standby router
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: chsrpextifstandbydestaddrtype
            
            	This object specifies the type of Internet address denoted by cHsrpExtIfStandbyDestAddr
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: chsrpextifstandbyrowstatus
            
            	The control that allows modification, creation, and deletion of entries. Entries may not be created via SNMP without explicitly setting cHsrpExtIfStandbyRowStatus to either 'createAndGo' or 'createAndWait'
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: chsrpextifstandbysourceaddr
            
            	This object specifies the source IP address of the standby router
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: chsrpextifstandbysourceaddrtype
            
            	This object specifies the type of Internet address denoted by cHsrpExtIfStandbySourceAddr
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            

            """

            _prefix = 'CISCO-HSRP-EXT-MIB'
            _revision = '2010-09-02'

            def __init__(self):
                super(CiscoHsrpExtMib.Chsrpextifstandbytable.Chsrpextifstandbyentry, self).__init__()

                self.yang_name = "cHsrpExtIfStandbyEntry"
                self.yang_parent_name = "cHsrpExtIfStandbyTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.chsrpgrpnumber = YLeaf(YType.str, "cHsrpGrpNumber")

                self.chsrpextifstandbyindex = YLeaf(YType.uint32, "cHsrpExtIfStandbyIndex")

                self.chsrpextifstandbydestaddr = YLeaf(YType.str, "cHsrpExtIfStandbyDestAddr")

                self.chsrpextifstandbydestaddrtype = YLeaf(YType.enumeration, "cHsrpExtIfStandbyDestAddrType")

                self.chsrpextifstandbyrowstatus = YLeaf(YType.enumeration, "cHsrpExtIfStandbyRowStatus")

                self.chsrpextifstandbysourceaddr = YLeaf(YType.str, "cHsrpExtIfStandbySourceAddr")

                self.chsrpextifstandbysourceaddrtype = YLeaf(YType.enumeration, "cHsrpExtIfStandbySourceAddrType")

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
                                "chsrpgrpnumber",
                                "chsrpextifstandbyindex",
                                "chsrpextifstandbydestaddr",
                                "chsrpextifstandbydestaddrtype",
                                "chsrpextifstandbyrowstatus",
                                "chsrpextifstandbysourceaddr",
                                "chsrpextifstandbysourceaddrtype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoHsrpExtMib.Chsrpextifstandbytable.Chsrpextifstandbyentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoHsrpExtMib.Chsrpextifstandbytable.Chsrpextifstandbyentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.chsrpgrpnumber.is_set or
                    self.chsrpextifstandbyindex.is_set or
                    self.chsrpextifstandbydestaddr.is_set or
                    self.chsrpextifstandbydestaddrtype.is_set or
                    self.chsrpextifstandbyrowstatus.is_set or
                    self.chsrpextifstandbysourceaddr.is_set or
                    self.chsrpextifstandbysourceaddrtype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.chsrpgrpnumber.yfilter != YFilter.not_set or
                    self.chsrpextifstandbyindex.yfilter != YFilter.not_set or
                    self.chsrpextifstandbydestaddr.yfilter != YFilter.not_set or
                    self.chsrpextifstandbydestaddrtype.yfilter != YFilter.not_set or
                    self.chsrpextifstandbyrowstatus.yfilter != YFilter.not_set or
                    self.chsrpextifstandbysourceaddr.yfilter != YFilter.not_set or
                    self.chsrpextifstandbysourceaddrtype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cHsrpExtIfStandbyEntry" + "[ifIndex='" + self.ifindex.get() + "']" + "[cHsrpGrpNumber='" + self.chsrpgrpnumber.get() + "']" + "[cHsrpExtIfStandbyIndex='" + self.chsrpextifstandbyindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/cHsrpExtIfStandbyTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.chsrpgrpnumber.is_set or self.chsrpgrpnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpgrpnumber.get_name_leafdata())
                if (self.chsrpextifstandbyindex.is_set or self.chsrpextifstandbyindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpextifstandbyindex.get_name_leafdata())
                if (self.chsrpextifstandbydestaddr.is_set or self.chsrpextifstandbydestaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpextifstandbydestaddr.get_name_leafdata())
                if (self.chsrpextifstandbydestaddrtype.is_set or self.chsrpextifstandbydestaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpextifstandbydestaddrtype.get_name_leafdata())
                if (self.chsrpextifstandbyrowstatus.is_set or self.chsrpextifstandbyrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpextifstandbyrowstatus.get_name_leafdata())
                if (self.chsrpextifstandbysourceaddr.is_set or self.chsrpextifstandbysourceaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpextifstandbysourceaddr.get_name_leafdata())
                if (self.chsrpextifstandbysourceaddrtype.is_set or self.chsrpextifstandbysourceaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpextifstandbysourceaddrtype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cHsrpGrpNumber" or name == "cHsrpExtIfStandbyIndex" or name == "cHsrpExtIfStandbyDestAddr" or name == "cHsrpExtIfStandbyDestAddrType" or name == "cHsrpExtIfStandbyRowStatus" or name == "cHsrpExtIfStandbySourceAddr" or name == "cHsrpExtIfStandbySourceAddrType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpGrpNumber"):
                    self.chsrpgrpnumber = value
                    self.chsrpgrpnumber.value_namespace = name_space
                    self.chsrpgrpnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpExtIfStandbyIndex"):
                    self.chsrpextifstandbyindex = value
                    self.chsrpextifstandbyindex.value_namespace = name_space
                    self.chsrpextifstandbyindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpExtIfStandbyDestAddr"):
                    self.chsrpextifstandbydestaddr = value
                    self.chsrpextifstandbydestaddr.value_namespace = name_space
                    self.chsrpextifstandbydestaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpExtIfStandbyDestAddrType"):
                    self.chsrpextifstandbydestaddrtype = value
                    self.chsrpextifstandbydestaddrtype.value_namespace = name_space
                    self.chsrpextifstandbydestaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpExtIfStandbyRowStatus"):
                    self.chsrpextifstandbyrowstatus = value
                    self.chsrpextifstandbyrowstatus.value_namespace = name_space
                    self.chsrpextifstandbyrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpExtIfStandbySourceAddr"):
                    self.chsrpextifstandbysourceaddr = value
                    self.chsrpextifstandbysourceaddr.value_namespace = name_space
                    self.chsrpextifstandbysourceaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpExtIfStandbySourceAddrType"):
                    self.chsrpextifstandbysourceaddrtype = value
                    self.chsrpextifstandbysourceaddrtype.value_namespace = name_space
                    self.chsrpextifstandbysourceaddrtype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.chsrpextifstandbyentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.chsrpextifstandbyentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cHsrpExtIfStandbyTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cHsrpExtIfStandbyEntry"):
                for c in self.chsrpextifstandbyentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoHsrpExtMib.Chsrpextifstandbytable.Chsrpextifstandbyentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.chsrpextifstandbyentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cHsrpExtIfStandbyEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Chsrpextiftable(Entity):
        """
        HSRP\-specific configurations for each physical interface.
        
        .. attribute:: chsrpextifentry
        
        	If HSRP entries on this interface must use the BIA (Burned In Address), there must be an entry for the interface in this  table. Entries of this table are only accessible if HSRP has  been enabled i.e entries can not be created if HSRP is not enabled. Also, the interfaces should be of IEEE 802 ones (Ethernet, Token Ring, FDDI,VLAN, LANE, TR\-LANE).  Setting cHsrpExtIfRowStatus to active initiates the entry with default value for cHsrpExtIfUseBIA as FALSE. The value of cHsrpExtIfRowStatus may be set to destroy at any time. If the row is not initiated, it is similar to having cHsrpExtIfUseBIA as FALSE.  Entries may not be created via SNMP without explicitly setting cHsrpExtIfRowStatus to either 'createAndGo' or 'createAndWait'.  Entries can be created and modified via the management protocol or by the device's local management interface.  If the row is not active, and a local management interface command modifies that row, the row may transition to active state.  A row which is not in active state will timeout after a configurable period (five minutes by default). This timeout period can be changed by setting cHsrpConfigTimeout
        	**type**\: list of    :py:class:`Chsrpextifentry <ydk.models.cisco_ios_xe.CISCO_HSRP_EXT_MIB.CiscoHsrpExtMib.Chsrpextiftable.Chsrpextifentry>`
        
        

        """

        _prefix = 'CISCO-HSRP-EXT-MIB'
        _revision = '2010-09-02'

        def __init__(self):
            super(CiscoHsrpExtMib.Chsrpextiftable, self).__init__()

            self.yang_name = "cHsrpExtIfTable"
            self.yang_parent_name = "CISCO-HSRP-EXT-MIB"

            self.chsrpextifentry = YList(self)

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
                        super(CiscoHsrpExtMib.Chsrpextiftable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoHsrpExtMib.Chsrpextiftable, self).__setattr__(name, value)


        class Chsrpextifentry(Entity):
            """
            If HSRP entries on this interface must use the BIA (Burned
            In Address), there must be an entry for the interface in this 
            table. Entries of this table are only accessible if HSRP has 
            been enabled i.e entries can not be created if HSRP is not
            enabled. Also, the interfaces should be of IEEE 802 ones
            (Ethernet, Token Ring, FDDI,VLAN, LANE, TR\-LANE).
            
            Setting cHsrpExtIfRowStatus to active initiates the
            entry with default value for cHsrpExtIfUseBIA as FALSE.
            The value of cHsrpExtIfRowStatus may be set to destroy
            at any time. If the row is not initiated, it is similar to
            having cHsrpExtIfUseBIA as FALSE.
            
            Entries may not be created via SNMP without explicitly setting
            cHsrpExtIfRowStatus to either 'createAndGo' or 'createAndWait'.
            
            Entries can be created and modified via the management
            protocol or by the device's local management interface.
            
            If the row is not active, and a local management interface
            command modifies that row, the row may transition to active
            state.
            
            A row which is not in active state will timeout after a
            configurable period (five minutes by default). This timeout
            period can be changed by setting cHsrpConfigTimeout.
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: chsrpextifrowstatus
            
            	The control that allows modification, creation, and deletion of entries. For detailed rules see the DESCRIPTION for cHsrpExtIfEntry
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: chsrpextifusebia
            
            	If set to TRUE, the HSRP Group MAC Address for all groups on this  interface will be the burned\-in\-address. Otherwise, this will be determined by ciscoHsrpGroupNumber. In case of sub\-interfaces, UseBIA applies to all sub\-interfaces on an  interface and to all groups on those sub\-interfaces
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-HSRP-EXT-MIB'
            _revision = '2010-09-02'

            def __init__(self):
                super(CiscoHsrpExtMib.Chsrpextiftable.Chsrpextifentry, self).__init__()

                self.yang_name = "cHsrpExtIfEntry"
                self.yang_parent_name = "cHsrpExtIfTable"

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.chsrpextifrowstatus = YLeaf(YType.enumeration, "cHsrpExtIfRowStatus")

                self.chsrpextifusebia = YLeaf(YType.boolean, "cHsrpExtIfUseBIA")

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
                                "chsrpextifrowstatus",
                                "chsrpextifusebia") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoHsrpExtMib.Chsrpextiftable.Chsrpextifentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoHsrpExtMib.Chsrpextiftable.Chsrpextifentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ifindex.is_set or
                    self.chsrpextifrowstatus.is_set or
                    self.chsrpextifusebia.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.chsrpextifrowstatus.yfilter != YFilter.not_set or
                    self.chsrpextifusebia.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cHsrpExtIfEntry" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/cHsrpExtIfTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.chsrpextifrowstatus.is_set or self.chsrpextifrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpextifrowstatus.get_name_leafdata())
                if (self.chsrpextifusebia.is_set or self.chsrpextifusebia.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.chsrpextifusebia.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ifIndex" or name == "cHsrpExtIfRowStatus" or name == "cHsrpExtIfUseBIA"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpExtIfRowStatus"):
                    self.chsrpextifrowstatus = value
                    self.chsrpextifrowstatus.value_namespace = name_space
                    self.chsrpextifrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "cHsrpExtIfUseBIA"):
                    self.chsrpextifusebia = value
                    self.chsrpextifusebia.value_namespace = name_space
                    self.chsrpextifusebia.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.chsrpextifentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.chsrpextifentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cHsrpExtIfTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cHsrpExtIfEntry"):
                for c in self.chsrpextifentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoHsrpExtMib.Chsrpextiftable.Chsrpextifentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.chsrpextifentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cHsrpExtIfEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.chsrpextifstandbytable is not None and self.chsrpextifstandbytable.has_data()) or
            (self.chsrpextiftable is not None and self.chsrpextiftable.has_data()) or
            (self.chsrpextiftrackedtable is not None and self.chsrpextiftrackedtable.has_data()) or
            (self.chsrpextsecaddrtable is not None and self.chsrpextsecaddrtable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.chsrpextifstandbytable is not None and self.chsrpextifstandbytable.has_operation()) or
            (self.chsrpextiftable is not None and self.chsrpextiftable.has_operation()) or
            (self.chsrpextiftrackedtable is not None and self.chsrpextiftrackedtable.has_operation()) or
            (self.chsrpextsecaddrtable is not None and self.chsrpextsecaddrtable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-HSRP-EXT-MIB:CISCO-HSRP-EXT-MIB" + path_buffer

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

        if (child_yang_name == "cHsrpExtIfStandbyTable"):
            if (self.chsrpextifstandbytable is None):
                self.chsrpextifstandbytable = CiscoHsrpExtMib.Chsrpextifstandbytable()
                self.chsrpextifstandbytable.parent = self
                self._children_name_map["chsrpextifstandbytable"] = "cHsrpExtIfStandbyTable"
            return self.chsrpextifstandbytable

        if (child_yang_name == "cHsrpExtIfTable"):
            if (self.chsrpextiftable is None):
                self.chsrpextiftable = CiscoHsrpExtMib.Chsrpextiftable()
                self.chsrpextiftable.parent = self
                self._children_name_map["chsrpextiftable"] = "cHsrpExtIfTable"
            return self.chsrpextiftable

        if (child_yang_name == "cHsrpExtIfTrackedTable"):
            if (self.chsrpextiftrackedtable is None):
                self.chsrpextiftrackedtable = CiscoHsrpExtMib.Chsrpextiftrackedtable()
                self.chsrpextiftrackedtable.parent = self
                self._children_name_map["chsrpextiftrackedtable"] = "cHsrpExtIfTrackedTable"
            return self.chsrpextiftrackedtable

        if (child_yang_name == "cHsrpExtSecAddrTable"):
            if (self.chsrpextsecaddrtable is None):
                self.chsrpextsecaddrtable = CiscoHsrpExtMib.Chsrpextsecaddrtable()
                self.chsrpextsecaddrtable.parent = self
                self._children_name_map["chsrpextsecaddrtable"] = "cHsrpExtSecAddrTable"
            return self.chsrpextsecaddrtable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cHsrpExtIfStandbyTable" or name == "cHsrpExtIfTable" or name == "cHsrpExtIfTrackedTable" or name == "cHsrpExtSecAddrTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoHsrpExtMib()
        return self._top_entity

