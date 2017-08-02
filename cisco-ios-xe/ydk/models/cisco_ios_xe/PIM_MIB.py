""" PIM_MIB 

The MIB module for management of PIM routers.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class PimMib(Entity):
    """
    
    
    .. attribute:: pim
    
    	
    	**type**\:   :py:class:`Pim <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pim>`
    
    .. attribute:: pimcandidaterptable
    
    	The (conceptual) table listing the IP multicast groups for which the local router is to advertise itself as a Candidate\-RP when the value of pimComponentCRPHoldTime is non\-zero.  If this table is empty, then the local router      will advertise itself as a Candidate\-RP for all groups (providing the value of pimComponentCRPHoldTime is non\- zero)
    	**type**\:   :py:class:`Pimcandidaterptable <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimcandidaterptable>`
    
    .. attribute:: pimcomponenttable
    
    	The (conceptual) table containing objects specific to a PIM domain.  One row exists for each domain to which the router is connected.  A PIM\-SM domain is defined as an area of the network over which Bootstrap messages are forwarded. Typically, a PIM\-SM router will be a member of exactly one domain.  This table also supports, however, routers which may form a border between two PIM\-SM domains and do not forward Bootstrap messages between them
    	**type**\:   :py:class:`Pimcomponenttable <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimcomponenttable>`
    
    .. attribute:: piminterfacetable
    
    	The (conceptual) table listing the router's PIM interfaces. IGMP and PIM are enabled on all interfaces listed in this table
    	**type**\:   :py:class:`Piminterfacetable <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Piminterfacetable>`
    
    .. attribute:: pimipmroutenexthoptable
    
    	The (conceptual) table listing PIM\-specific information on a subset of the rows of the ipMRouteNextHopTable defined in the IP Multicast MIB
    	**type**\:   :py:class:`Pimipmroutenexthoptable <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimipmroutenexthoptable>`
    
    .. attribute:: pimipmroutetable
    
    	The (conceptual) table listing PIM\-specific information on a subset of the rows of the ipMRouteTable defined in the IP Multicast MIB
    	**type**\:   :py:class:`Pimipmroutetable <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimipmroutetable>`
    
    .. attribute:: pimneighbortable
    
    	The (conceptual) table listing the router's PIM neighbors
    	**type**\:   :py:class:`Pimneighbortable <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimneighbortable>`
    
    .. attribute:: pimrpsettable
    
    	The (conceptual) table listing PIM information for candidate Rendezvous Points (RPs) for IP multicast groups. When the local router is the BSR, this information is obtained from received Candidate\-RP\-Advertisements.  When the local router is not the BSR, this information is obtained from received RP\-Set messages
    	**type**\:   :py:class:`Pimrpsettable <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimrpsettable>`
    
    .. attribute:: pimrptable
    
    	The (conceptual) table listing PIM version 1 information for the Rendezvous Points (RPs) for IP multicast groups. This table is deprecated since its function is replaced by the pimRPSetTable for PIM version 2
    	**type**\:   :py:class:`Pimrptable <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimrptable>`
    
    	**status**\: deprecated
    
    

    """

    _prefix = 'PIM-MIB'
    _revision = '2000-09-28'

    def __init__(self):
        super(PimMib, self).__init__()
        self._top_entity = None

        self.yang_name = "PIM-MIB"
        self.yang_parent_name = "PIM-MIB"

        self.pim = PimMib.Pim()
        self.pim.parent = self
        self._children_name_map["pim"] = "pim"
        self._children_yang_names.add("pim")

        self.pimcandidaterptable = PimMib.Pimcandidaterptable()
        self.pimcandidaterptable.parent = self
        self._children_name_map["pimcandidaterptable"] = "pimCandidateRPTable"
        self._children_yang_names.add("pimCandidateRPTable")

        self.pimcomponenttable = PimMib.Pimcomponenttable()
        self.pimcomponenttable.parent = self
        self._children_name_map["pimcomponenttable"] = "pimComponentTable"
        self._children_yang_names.add("pimComponentTable")

        self.piminterfacetable = PimMib.Piminterfacetable()
        self.piminterfacetable.parent = self
        self._children_name_map["piminterfacetable"] = "pimInterfaceTable"
        self._children_yang_names.add("pimInterfaceTable")

        self.pimipmroutenexthoptable = PimMib.Pimipmroutenexthoptable()
        self.pimipmroutenexthoptable.parent = self
        self._children_name_map["pimipmroutenexthoptable"] = "pimIpMRouteNextHopTable"
        self._children_yang_names.add("pimIpMRouteNextHopTable")

        self.pimipmroutetable = PimMib.Pimipmroutetable()
        self.pimipmroutetable.parent = self
        self._children_name_map["pimipmroutetable"] = "pimIpMRouteTable"
        self._children_yang_names.add("pimIpMRouteTable")

        self.pimneighbortable = PimMib.Pimneighbortable()
        self.pimneighbortable.parent = self
        self._children_name_map["pimneighbortable"] = "pimNeighborTable"
        self._children_yang_names.add("pimNeighborTable")

        self.pimrpsettable = PimMib.Pimrpsettable()
        self.pimrpsettable.parent = self
        self._children_name_map["pimrpsettable"] = "pimRPSetTable"
        self._children_yang_names.add("pimRPSetTable")

        self.pimrptable = PimMib.Pimrptable()
        self.pimrptable.parent = self
        self._children_name_map["pimrptable"] = "pimRPTable"
        self._children_yang_names.add("pimRPTable")


    class Pim(Entity):
        """
        
        
        .. attribute:: pimjoinpruneinterval
        
        	The default interval at which periodic PIM\-SM Join/Prune messages are to be sent
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: seconds
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(PimMib.Pim, self).__init__()

            self.yang_name = "pim"
            self.yang_parent_name = "PIM-MIB"

            self.pimjoinpruneinterval = YLeaf(YType.int32, "pimJoinPruneInterval")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("pimjoinpruneinterval") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(PimMib.Pim, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PimMib.Pim, self).__setattr__(name, value)

        def has_data(self):
            return self.pimjoinpruneinterval.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.pimjoinpruneinterval.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "pim" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "PIM-MIB:PIM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.pimjoinpruneinterval.is_set or self.pimjoinpruneinterval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.pimjoinpruneinterval.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "pimJoinPruneInterval"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "pimJoinPruneInterval"):
                self.pimjoinpruneinterval = value
                self.pimjoinpruneinterval.value_namespace = name_space
                self.pimjoinpruneinterval.value_namespace_prefix = name_space_prefix


    class Piminterfacetable(Entity):
        """
        The (conceptual) table listing the router's PIM interfaces.
        IGMP and PIM are enabled on all interfaces listed in this
        table.
        
        .. attribute:: piminterfaceentry
        
        	An entry (conceptual row) in the pimInterfaceTable
        	**type**\: list of    :py:class:`Piminterfaceentry <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Piminterfacetable.Piminterfaceentry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(PimMib.Piminterfacetable, self).__init__()

            self.yang_name = "pimInterfaceTable"
            self.yang_parent_name = "PIM-MIB"

            self.piminterfaceentry = YList(self)

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
                        super(PimMib.Piminterfacetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PimMib.Piminterfacetable, self).__setattr__(name, value)


        class Piminterfaceentry(Entity):
            """
            An entry (conceptual row) in the pimInterfaceTable.
            
            .. attribute:: piminterfaceifindex  <key>
            
            	The ifIndex value of this PIM interface
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: piminterfaceaddress
            
            	The IP address of the PIM interface
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: piminterfacecbsrpreference
            
            	The preference value for the local interface as a candidate bootstrap router.  The value of \-1 is used to indicate that the local interface is not a candidate BSR interface
            	**type**\:  int
            
            	**range:** \-1..255
            
            .. attribute:: piminterfacedr
            
            	The Designated Router on this PIM interface.  For point\-to\- point interfaces, this object has the value 0.0.0.0
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: piminterfacehellointerval
            
            	The frequency at which PIM Hello messages are transmitted on this interface
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: seconds
            
            .. attribute:: piminterfacejoinpruneinterval
            
            	The frequency at which PIM Join/Prune messages are transmitted on this PIM interface.  The default value of this object is the pimJoinPruneInterval
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            	**units**\: seconds
            
            .. attribute:: piminterfacemode
            
            	The configured mode of this PIM interface.  A value of sparseDense is only valid for PIMv1
            	**type**\:   :py:class:`Piminterfacemode <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Piminterfacetable.Piminterfaceentry.Piminterfacemode>`
            
            .. attribute:: piminterfacenetmask
            
            	The network mask for the IP address of the PIM interface
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: piminterfacestatus
            
            	The status of this entry.  Creating the entry enables PIM on the interface; destroying the entry disables PIM on the interface
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(PimMib.Piminterfacetable.Piminterfaceentry, self).__init__()

                self.yang_name = "pimInterfaceEntry"
                self.yang_parent_name = "pimInterfaceTable"

                self.piminterfaceifindex = YLeaf(YType.int32, "pimInterfaceIfIndex")

                self.piminterfaceaddress = YLeaf(YType.str, "pimInterfaceAddress")

                self.piminterfacecbsrpreference = YLeaf(YType.int32, "pimInterfaceCBSRPreference")

                self.piminterfacedr = YLeaf(YType.str, "pimInterfaceDR")

                self.piminterfacehellointerval = YLeaf(YType.int32, "pimInterfaceHelloInterval")

                self.piminterfacejoinpruneinterval = YLeaf(YType.int32, "pimInterfaceJoinPruneInterval")

                self.piminterfacemode = YLeaf(YType.enumeration, "pimInterfaceMode")

                self.piminterfacenetmask = YLeaf(YType.str, "pimInterfaceNetMask")

                self.piminterfacestatus = YLeaf(YType.enumeration, "pimInterfaceStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("piminterfaceifindex",
                                "piminterfaceaddress",
                                "piminterfacecbsrpreference",
                                "piminterfacedr",
                                "piminterfacehellointerval",
                                "piminterfacejoinpruneinterval",
                                "piminterfacemode",
                                "piminterfacenetmask",
                                "piminterfacestatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PimMib.Piminterfacetable.Piminterfaceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PimMib.Piminterfacetable.Piminterfaceentry, self).__setattr__(name, value)

            class Piminterfacemode(Enum):
                """
                Piminterfacemode

                The configured mode of this PIM interface.  A value of

                sparseDense is only valid for PIMv1.

                .. data:: dense = 1

                .. data:: sparse = 2

                .. data:: sparseDense = 3

                """

                dense = Enum.YLeaf(1, "dense")

                sparse = Enum.YLeaf(2, "sparse")

                sparseDense = Enum.YLeaf(3, "sparseDense")


            def has_data(self):
                return (
                    self.piminterfaceifindex.is_set or
                    self.piminterfaceaddress.is_set or
                    self.piminterfacecbsrpreference.is_set or
                    self.piminterfacedr.is_set or
                    self.piminterfacehellointerval.is_set or
                    self.piminterfacejoinpruneinterval.is_set or
                    self.piminterfacemode.is_set or
                    self.piminterfacenetmask.is_set or
                    self.piminterfacestatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.piminterfaceifindex.yfilter != YFilter.not_set or
                    self.piminterfaceaddress.yfilter != YFilter.not_set or
                    self.piminterfacecbsrpreference.yfilter != YFilter.not_set or
                    self.piminterfacedr.yfilter != YFilter.not_set or
                    self.piminterfacehellointerval.yfilter != YFilter.not_set or
                    self.piminterfacejoinpruneinterval.yfilter != YFilter.not_set or
                    self.piminterfacemode.yfilter != YFilter.not_set or
                    self.piminterfacenetmask.yfilter != YFilter.not_set or
                    self.piminterfacestatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "pimInterfaceEntry" + "[pimInterfaceIfIndex='" + self.piminterfaceifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "PIM-MIB:PIM-MIB/pimInterfaceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.piminterfaceifindex.is_set or self.piminterfaceifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.piminterfaceifindex.get_name_leafdata())
                if (self.piminterfaceaddress.is_set or self.piminterfaceaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.piminterfaceaddress.get_name_leafdata())
                if (self.piminterfacecbsrpreference.is_set or self.piminterfacecbsrpreference.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.piminterfacecbsrpreference.get_name_leafdata())
                if (self.piminterfacedr.is_set or self.piminterfacedr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.piminterfacedr.get_name_leafdata())
                if (self.piminterfacehellointerval.is_set or self.piminterfacehellointerval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.piminterfacehellointerval.get_name_leafdata())
                if (self.piminterfacejoinpruneinterval.is_set or self.piminterfacejoinpruneinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.piminterfacejoinpruneinterval.get_name_leafdata())
                if (self.piminterfacemode.is_set or self.piminterfacemode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.piminterfacemode.get_name_leafdata())
                if (self.piminterfacenetmask.is_set or self.piminterfacenetmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.piminterfacenetmask.get_name_leafdata())
                if (self.piminterfacestatus.is_set or self.piminterfacestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.piminterfacestatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "pimInterfaceIfIndex" or name == "pimInterfaceAddress" or name == "pimInterfaceCBSRPreference" or name == "pimInterfaceDR" or name == "pimInterfaceHelloInterval" or name == "pimInterfaceJoinPruneInterval" or name == "pimInterfaceMode" or name == "pimInterfaceNetMask" or name == "pimInterfaceStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "pimInterfaceIfIndex"):
                    self.piminterfaceifindex = value
                    self.piminterfaceifindex.value_namespace = name_space
                    self.piminterfaceifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "pimInterfaceAddress"):
                    self.piminterfaceaddress = value
                    self.piminterfaceaddress.value_namespace = name_space
                    self.piminterfaceaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "pimInterfaceCBSRPreference"):
                    self.piminterfacecbsrpreference = value
                    self.piminterfacecbsrpreference.value_namespace = name_space
                    self.piminterfacecbsrpreference.value_namespace_prefix = name_space_prefix
                if(value_path == "pimInterfaceDR"):
                    self.piminterfacedr = value
                    self.piminterfacedr.value_namespace = name_space
                    self.piminterfacedr.value_namespace_prefix = name_space_prefix
                if(value_path == "pimInterfaceHelloInterval"):
                    self.piminterfacehellointerval = value
                    self.piminterfacehellointerval.value_namespace = name_space
                    self.piminterfacehellointerval.value_namespace_prefix = name_space_prefix
                if(value_path == "pimInterfaceJoinPruneInterval"):
                    self.piminterfacejoinpruneinterval = value
                    self.piminterfacejoinpruneinterval.value_namespace = name_space
                    self.piminterfacejoinpruneinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "pimInterfaceMode"):
                    self.piminterfacemode = value
                    self.piminterfacemode.value_namespace = name_space
                    self.piminterfacemode.value_namespace_prefix = name_space_prefix
                if(value_path == "pimInterfaceNetMask"):
                    self.piminterfacenetmask = value
                    self.piminterfacenetmask.value_namespace = name_space
                    self.piminterfacenetmask.value_namespace_prefix = name_space_prefix
                if(value_path == "pimInterfaceStatus"):
                    self.piminterfacestatus = value
                    self.piminterfacestatus.value_namespace = name_space
                    self.piminterfacestatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.piminterfaceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.piminterfaceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "pimInterfaceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "PIM-MIB:PIM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "pimInterfaceEntry"):
                for c in self.piminterfaceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PimMib.Piminterfacetable.Piminterfaceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.piminterfaceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "pimInterfaceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Pimneighbortable(Entity):
        """
        The (conceptual) table listing the router's PIM neighbors.
        
        .. attribute:: pimneighborentry
        
        	An entry (conceptual row) in the pimNeighborTable
        	**type**\: list of    :py:class:`Pimneighborentry <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimneighbortable.Pimneighborentry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(PimMib.Pimneighbortable, self).__init__()

            self.yang_name = "pimNeighborTable"
            self.yang_parent_name = "PIM-MIB"

            self.pimneighborentry = YList(self)

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
                        super(PimMib.Pimneighbortable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PimMib.Pimneighbortable, self).__setattr__(name, value)


        class Pimneighborentry(Entity):
            """
            An entry (conceptual row) in the pimNeighborTable.
            
            .. attribute:: pimneighboraddress  <key>
            
            	The IP address of the PIM neighbor for which this entry contains information
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimneighborexpirytime
            
            	The minimum time remaining before this PIM neighbor will be aged out
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pimneighborifindex
            
            	The value of ifIndex for the interface used to reach this PIM neighbor
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: pimneighbormode
            
            	The active PIM mode of this neighbor.  This object is deprecated for PIMv2 routers since all neighbors on the interface must be either dense or sparse as determined by the protocol running on the interface
            	**type**\:   :py:class:`Pimneighbormode <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimneighbortable.Pimneighborentry.Pimneighbormode>`
            
            	**status**\: deprecated
            
            .. attribute:: pimneighboruptime
            
            	The time since this PIM neighbor (last) became a neighbor of the local router
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(PimMib.Pimneighbortable.Pimneighborentry, self).__init__()

                self.yang_name = "pimNeighborEntry"
                self.yang_parent_name = "pimNeighborTable"

                self.pimneighboraddress = YLeaf(YType.str, "pimNeighborAddress")

                self.pimneighborexpirytime = YLeaf(YType.uint32, "pimNeighborExpiryTime")

                self.pimneighborifindex = YLeaf(YType.int32, "pimNeighborIfIndex")

                self.pimneighbormode = YLeaf(YType.enumeration, "pimNeighborMode")

                self.pimneighboruptime = YLeaf(YType.uint32, "pimNeighborUpTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("pimneighboraddress",
                                "pimneighborexpirytime",
                                "pimneighborifindex",
                                "pimneighbormode",
                                "pimneighboruptime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PimMib.Pimneighbortable.Pimneighborentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PimMib.Pimneighbortable.Pimneighborentry, self).__setattr__(name, value)

            class Pimneighbormode(Enum):
                """
                Pimneighbormode

                The active PIM mode of this neighbor.  This object is

                deprecated for PIMv2 routers since all neighbors on the

                interface must be either dense or sparse as determined by

                the protocol running on the interface.

                .. data:: dense = 1

                .. data:: sparse = 2

                """

                dense = Enum.YLeaf(1, "dense")

                sparse = Enum.YLeaf(2, "sparse")


            def has_data(self):
                return (
                    self.pimneighboraddress.is_set or
                    self.pimneighborexpirytime.is_set or
                    self.pimneighborifindex.is_set or
                    self.pimneighbormode.is_set or
                    self.pimneighboruptime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.pimneighboraddress.yfilter != YFilter.not_set or
                    self.pimneighborexpirytime.yfilter != YFilter.not_set or
                    self.pimneighborifindex.yfilter != YFilter.not_set or
                    self.pimneighbormode.yfilter != YFilter.not_set or
                    self.pimneighboruptime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "pimNeighborEntry" + "[pimNeighborAddress='" + self.pimneighboraddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "PIM-MIB:PIM-MIB/pimNeighborTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.pimneighboraddress.is_set or self.pimneighboraddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimneighboraddress.get_name_leafdata())
                if (self.pimneighborexpirytime.is_set or self.pimneighborexpirytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimneighborexpirytime.get_name_leafdata())
                if (self.pimneighborifindex.is_set or self.pimneighborifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimneighborifindex.get_name_leafdata())
                if (self.pimneighbormode.is_set or self.pimneighbormode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimneighbormode.get_name_leafdata())
                if (self.pimneighboruptime.is_set or self.pimneighboruptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimneighboruptime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "pimNeighborAddress" or name == "pimNeighborExpiryTime" or name == "pimNeighborIfIndex" or name == "pimNeighborMode" or name == "pimNeighborUpTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "pimNeighborAddress"):
                    self.pimneighboraddress = value
                    self.pimneighboraddress.value_namespace = name_space
                    self.pimneighboraddress.value_namespace_prefix = name_space_prefix
                if(value_path == "pimNeighborExpiryTime"):
                    self.pimneighborexpirytime = value
                    self.pimneighborexpirytime.value_namespace = name_space
                    self.pimneighborexpirytime.value_namespace_prefix = name_space_prefix
                if(value_path == "pimNeighborIfIndex"):
                    self.pimneighborifindex = value
                    self.pimneighborifindex.value_namespace = name_space
                    self.pimneighborifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "pimNeighborMode"):
                    self.pimneighbormode = value
                    self.pimneighbormode.value_namespace = name_space
                    self.pimneighbormode.value_namespace_prefix = name_space_prefix
                if(value_path == "pimNeighborUpTime"):
                    self.pimneighboruptime = value
                    self.pimneighboruptime.value_namespace = name_space
                    self.pimneighboruptime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.pimneighborentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.pimneighborentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "pimNeighborTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "PIM-MIB:PIM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "pimNeighborEntry"):
                for c in self.pimneighborentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PimMib.Pimneighbortable.Pimneighborentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.pimneighborentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "pimNeighborEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Pimipmroutetable(Entity):
        """
        The (conceptual) table listing PIM\-specific information on
        a subset of the rows of the ipMRouteTable defined in the IP
        Multicast MIB.
        
        .. attribute:: pimipmrouteentry
        
        	An entry (conceptual row) in the pimIpMRouteTable.  There is one entry per entry in the ipMRouteTable whose incoming interface is running PIM
        	**type**\: list of    :py:class:`Pimipmrouteentry <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimipmroutetable.Pimipmrouteentry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(PimMib.Pimipmroutetable, self).__init__()

            self.yang_name = "pimIpMRouteTable"
            self.yang_parent_name = "PIM-MIB"

            self.pimipmrouteentry = YList(self)

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
                        super(PimMib.Pimipmroutetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PimMib.Pimipmroutetable, self).__setattr__(name, value)


        class Pimipmrouteentry(Entity):
            """
            An entry (conceptual row) in the pimIpMRouteTable.  There
            is one entry per entry in the ipMRouteTable whose incoming
            interface is running PIM.
            
            .. attribute:: ipmroutegroup  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutegroup <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutetable.Ipmrouteentry>`
            
            .. attribute:: ipmroutesource  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutesource <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutetable.Ipmrouteentry>`
            
            .. attribute:: ipmroutesourcemask  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutesourcemask <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutetable.Ipmrouteentry>`
            
            .. attribute:: pimipmrouteassertmetric
            
            	The metric advertised by the assert winner on the upstream interface, or 0 if no such assert is in received
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: pimipmrouteassertmetricpref
            
            	The preference advertised by the assert winner on the upstream interface, or 0 if no such assert is in effect
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: pimipmrouteassertrptbit
            
            	The value of the RPT\-bit advertised by the assert winner on the upstream interface, or false if no such assert is in effect
            	**type**\:  bool
            
            .. attribute:: pimipmrouteflags
            
            	This object describes PIM\-specific flags related to a multicast state entry.  See the PIM Sparse Mode specification for the meaning of the RPT and SPT bits
            	**type**\:  str
            
            	**length:** 1
            
            .. attribute:: pimipmrouteupstreamasserttimer
            
            	The time remaining before the router changes its upstream neighbor back to its RPF neighbor.  This timer is called the Assert timer in the PIM Sparse and Dense mode specification.      A value of 0 indicates that no Assert has changed the upstream neighbor away from the RPF neighbor
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(PimMib.Pimipmroutetable.Pimipmrouteentry, self).__init__()

                self.yang_name = "pimIpMRouteEntry"
                self.yang_parent_name = "pimIpMRouteTable"

                self.ipmroutegroup = YLeaf(YType.str, "ipMRouteGroup")

                self.ipmroutesource = YLeaf(YType.str, "ipMRouteSource")

                self.ipmroutesourcemask = YLeaf(YType.str, "ipMRouteSourceMask")

                self.pimipmrouteassertmetric = YLeaf(YType.int32, "pimIpMRouteAssertMetric")

                self.pimipmrouteassertmetricpref = YLeaf(YType.int32, "pimIpMRouteAssertMetricPref")

                self.pimipmrouteassertrptbit = YLeaf(YType.boolean, "pimIpMRouteAssertRPTBit")

                self.pimipmrouteflags = YLeaf(YType.str, "pimIpMRouteFlags")

                self.pimipmrouteupstreamasserttimer = YLeaf(YType.uint32, "pimIpMRouteUpstreamAssertTimer")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipmroutegroup",
                                "ipmroutesource",
                                "ipmroutesourcemask",
                                "pimipmrouteassertmetric",
                                "pimipmrouteassertmetricpref",
                                "pimipmrouteassertrptbit",
                                "pimipmrouteflags",
                                "pimipmrouteupstreamasserttimer") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PimMib.Pimipmroutetable.Pimipmrouteentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PimMib.Pimipmroutetable.Pimipmrouteentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ipmroutegroup.is_set or
                    self.ipmroutesource.is_set or
                    self.ipmroutesourcemask.is_set or
                    self.pimipmrouteassertmetric.is_set or
                    self.pimipmrouteassertmetricpref.is_set or
                    self.pimipmrouteassertrptbit.is_set or
                    self.pimipmrouteflags.is_set or
                    self.pimipmrouteupstreamasserttimer.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipmroutegroup.yfilter != YFilter.not_set or
                    self.ipmroutesource.yfilter != YFilter.not_set or
                    self.ipmroutesourcemask.yfilter != YFilter.not_set or
                    self.pimipmrouteassertmetric.yfilter != YFilter.not_set or
                    self.pimipmrouteassertmetricpref.yfilter != YFilter.not_set or
                    self.pimipmrouteassertrptbit.yfilter != YFilter.not_set or
                    self.pimipmrouteflags.yfilter != YFilter.not_set or
                    self.pimipmrouteupstreamasserttimer.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "pimIpMRouteEntry" + "[ipMRouteGroup='" + self.ipmroutegroup.get() + "']" + "[ipMRouteSource='" + self.ipmroutesource.get() + "']" + "[ipMRouteSourceMask='" + self.ipmroutesourcemask.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "PIM-MIB:PIM-MIB/pimIpMRouteTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipmroutegroup.is_set or self.ipmroutegroup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutegroup.get_name_leafdata())
                if (self.ipmroutesource.is_set or self.ipmroutesource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutesource.get_name_leafdata())
                if (self.ipmroutesourcemask.is_set or self.ipmroutesourcemask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutesourcemask.get_name_leafdata())
                if (self.pimipmrouteassertmetric.is_set or self.pimipmrouteassertmetric.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimipmrouteassertmetric.get_name_leafdata())
                if (self.pimipmrouteassertmetricpref.is_set or self.pimipmrouteassertmetricpref.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimipmrouteassertmetricpref.get_name_leafdata())
                if (self.pimipmrouteassertrptbit.is_set or self.pimipmrouteassertrptbit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimipmrouteassertrptbit.get_name_leafdata())
                if (self.pimipmrouteflags.is_set or self.pimipmrouteflags.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimipmrouteflags.get_name_leafdata())
                if (self.pimipmrouteupstreamasserttimer.is_set or self.pimipmrouteupstreamasserttimer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimipmrouteupstreamasserttimer.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipMRouteGroup" or name == "ipMRouteSource" or name == "ipMRouteSourceMask" or name == "pimIpMRouteAssertMetric" or name == "pimIpMRouteAssertMetricPref" or name == "pimIpMRouteAssertRPTBit" or name == "pimIpMRouteFlags" or name == "pimIpMRouteUpstreamAssertTimer"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipMRouteGroup"):
                    self.ipmroutegroup = value
                    self.ipmroutegroup.value_namespace = name_space
                    self.ipmroutegroup.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteSource"):
                    self.ipmroutesource = value
                    self.ipmroutesource.value_namespace = name_space
                    self.ipmroutesource.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteSourceMask"):
                    self.ipmroutesourcemask = value
                    self.ipmroutesourcemask.value_namespace = name_space
                    self.ipmroutesourcemask.value_namespace_prefix = name_space_prefix
                if(value_path == "pimIpMRouteAssertMetric"):
                    self.pimipmrouteassertmetric = value
                    self.pimipmrouteassertmetric.value_namespace = name_space
                    self.pimipmrouteassertmetric.value_namespace_prefix = name_space_prefix
                if(value_path == "pimIpMRouteAssertMetricPref"):
                    self.pimipmrouteassertmetricpref = value
                    self.pimipmrouteassertmetricpref.value_namespace = name_space
                    self.pimipmrouteassertmetricpref.value_namespace_prefix = name_space_prefix
                if(value_path == "pimIpMRouteAssertRPTBit"):
                    self.pimipmrouteassertrptbit = value
                    self.pimipmrouteassertrptbit.value_namespace = name_space
                    self.pimipmrouteassertrptbit.value_namespace_prefix = name_space_prefix
                if(value_path == "pimIpMRouteFlags"):
                    self.pimipmrouteflags = value
                    self.pimipmrouteflags.value_namespace = name_space
                    self.pimipmrouteflags.value_namespace_prefix = name_space_prefix
                if(value_path == "pimIpMRouteUpstreamAssertTimer"):
                    self.pimipmrouteupstreamasserttimer = value
                    self.pimipmrouteupstreamasserttimer.value_namespace = name_space
                    self.pimipmrouteupstreamasserttimer.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.pimipmrouteentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.pimipmrouteentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "pimIpMRouteTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "PIM-MIB:PIM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "pimIpMRouteEntry"):
                for c in self.pimipmrouteentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PimMib.Pimipmroutetable.Pimipmrouteentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.pimipmrouteentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "pimIpMRouteEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Pimrptable(Entity):
        """
        The (conceptual) table listing PIM version 1 information
        for the Rendezvous Points (RPs) for IP multicast groups.
        This table is deprecated since its function is replaced by
        the pimRPSetTable for PIM version 2.
        
        .. attribute:: pimrpentry
        
        	An entry (conceptual row) in the pimRPTable.  There is one entry per RP address for each IP multicast group
        	**type**\: list of    :py:class:`Pimrpentry <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimrptable.Pimrpentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(PimMib.Pimrptable, self).__init__()

            self.yang_name = "pimRPTable"
            self.yang_parent_name = "PIM-MIB"

            self.pimrpentry = YList(self)

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
                        super(PimMib.Pimrptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PimMib.Pimrptable, self).__setattr__(name, value)


        class Pimrpentry(Entity):
            """
            An entry (conceptual row) in the pimRPTable.  There is one
            entry per RP address for each IP multicast group.
            
            .. attribute:: pimrpgroupaddress  <key>
            
            	The IP multicast group address for which this entry contains information about an RP
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: pimrpaddress  <key>
            
            	The unicast address of the RP
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: pimrplastchange
            
            	The value of sysUpTime at the time when the corresponding instance of pimRPState last changed its value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: pimrprowstatus
            
            	The status of this row, by which new entries may be created, or old entries deleted from this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            	**status**\: deprecated
            
            .. attribute:: pimrpstate
            
            	The state of the RP
            	**type**\:   :py:class:`Pimrpstate <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimrptable.Pimrpentry.Pimrpstate>`
            
            	**status**\: deprecated
            
            .. attribute:: pimrpstatetimer
            
            	The minimum time remaining before the next state change. When pimRPState is up, this is the minimum time which must expire until it can be declared down.  When pimRPState is down, this is the time until it will be declared up (in order to retry)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(PimMib.Pimrptable.Pimrpentry, self).__init__()

                self.yang_name = "pimRPEntry"
                self.yang_parent_name = "pimRPTable"

                self.pimrpgroupaddress = YLeaf(YType.str, "pimRPGroupAddress")

                self.pimrpaddress = YLeaf(YType.str, "pimRPAddress")

                self.pimrplastchange = YLeaf(YType.uint32, "pimRPLastChange")

                self.pimrprowstatus = YLeaf(YType.enumeration, "pimRPRowStatus")

                self.pimrpstate = YLeaf(YType.enumeration, "pimRPState")

                self.pimrpstatetimer = YLeaf(YType.uint32, "pimRPStateTimer")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("pimrpgroupaddress",
                                "pimrpaddress",
                                "pimrplastchange",
                                "pimrprowstatus",
                                "pimrpstate",
                                "pimrpstatetimer") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PimMib.Pimrptable.Pimrpentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PimMib.Pimrptable.Pimrpentry, self).__setattr__(name, value)

            class Pimrpstate(Enum):
                """
                Pimrpstate

                The state of the RP.

                .. data:: up = 1

                .. data:: down = 2

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")


            def has_data(self):
                return (
                    self.pimrpgroupaddress.is_set or
                    self.pimrpaddress.is_set or
                    self.pimrplastchange.is_set or
                    self.pimrprowstatus.is_set or
                    self.pimrpstate.is_set or
                    self.pimrpstatetimer.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.pimrpgroupaddress.yfilter != YFilter.not_set or
                    self.pimrpaddress.yfilter != YFilter.not_set or
                    self.pimrplastchange.yfilter != YFilter.not_set or
                    self.pimrprowstatus.yfilter != YFilter.not_set or
                    self.pimrpstate.yfilter != YFilter.not_set or
                    self.pimrpstatetimer.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "pimRPEntry" + "[pimRPGroupAddress='" + self.pimrpgroupaddress.get() + "']" + "[pimRPAddress='" + self.pimrpaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "PIM-MIB:PIM-MIB/pimRPTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.pimrpgroupaddress.is_set or self.pimrpgroupaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimrpgroupaddress.get_name_leafdata())
                if (self.pimrpaddress.is_set or self.pimrpaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimrpaddress.get_name_leafdata())
                if (self.pimrplastchange.is_set or self.pimrplastchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimrplastchange.get_name_leafdata())
                if (self.pimrprowstatus.is_set or self.pimrprowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimrprowstatus.get_name_leafdata())
                if (self.pimrpstate.is_set or self.pimrpstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimrpstate.get_name_leafdata())
                if (self.pimrpstatetimer.is_set or self.pimrpstatetimer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimrpstatetimer.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "pimRPGroupAddress" or name == "pimRPAddress" or name == "pimRPLastChange" or name == "pimRPRowStatus" or name == "pimRPState" or name == "pimRPStateTimer"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "pimRPGroupAddress"):
                    self.pimrpgroupaddress = value
                    self.pimrpgroupaddress.value_namespace = name_space
                    self.pimrpgroupaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "pimRPAddress"):
                    self.pimrpaddress = value
                    self.pimrpaddress.value_namespace = name_space
                    self.pimrpaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "pimRPLastChange"):
                    self.pimrplastchange = value
                    self.pimrplastchange.value_namespace = name_space
                    self.pimrplastchange.value_namespace_prefix = name_space_prefix
                if(value_path == "pimRPRowStatus"):
                    self.pimrprowstatus = value
                    self.pimrprowstatus.value_namespace = name_space
                    self.pimrprowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "pimRPState"):
                    self.pimrpstate = value
                    self.pimrpstate.value_namespace = name_space
                    self.pimrpstate.value_namespace_prefix = name_space_prefix
                if(value_path == "pimRPStateTimer"):
                    self.pimrpstatetimer = value
                    self.pimrpstatetimer.value_namespace = name_space
                    self.pimrpstatetimer.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.pimrpentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.pimrpentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "pimRPTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "PIM-MIB:PIM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "pimRPEntry"):
                for c in self.pimrpentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PimMib.Pimrptable.Pimrpentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.pimrpentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "pimRPEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Pimrpsettable(Entity):
        """
        The (conceptual) table listing PIM information for
        candidate Rendezvous Points (RPs) for IP multicast groups.
        When the local router is the BSR, this information is
        obtained from received Candidate\-RP\-Advertisements.  When
        the local router is not the BSR, this information is
        obtained from received RP\-Set messages.
        
        .. attribute:: pimrpsetentry
        
        	An entry (conceptual row) in the pimRPSetTable
        	**type**\: list of    :py:class:`Pimrpsetentry <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimrpsettable.Pimrpsetentry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(PimMib.Pimrpsettable, self).__init__()

            self.yang_name = "pimRPSetTable"
            self.yang_parent_name = "PIM-MIB"

            self.pimrpsetentry = YList(self)

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
                        super(PimMib.Pimrpsettable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PimMib.Pimrpsettable, self).__setattr__(name, value)


        class Pimrpsetentry(Entity):
            """
            An entry (conceptual row) in the pimRPSetTable.
            
            .. attribute:: pimrpsetcomponent  <key>
            
            	 A number uniquely identifying the component.  Each protocol instance connected to a separate domain should have a different index value
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: pimrpsetgroupaddress  <key>
            
            	The IP multicast group address which, when combined with pimRPSetGroupMask, gives the group prefix for which this entry contains information about the Candidate\-RP
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimrpsetgroupmask  <key>
            
            	The multicast group address mask which, when combined with pimRPSetGroupAddress, gives the group prefix for which this entry contains information about the Candidate\-RP
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimrpsetaddress  <key>
            
            	The IP address of the Candidate\-RP
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimrpsetexpirytime
            
            	The minimum time remaining before the Candidate\-RP will be declared down.  If the local router is not the BSR, this value is 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pimrpsetholdtime
            
            	The holdtime of a Candidate\-RP.  If the local router is not the BSR, this value is 0
            	**type**\:  int
            
            	**range:** 0..255
            
            	**units**\: seconds
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(PimMib.Pimrpsettable.Pimrpsetentry, self).__init__()

                self.yang_name = "pimRPSetEntry"
                self.yang_parent_name = "pimRPSetTable"

                self.pimrpsetcomponent = YLeaf(YType.int32, "pimRPSetComponent")

                self.pimrpsetgroupaddress = YLeaf(YType.str, "pimRPSetGroupAddress")

                self.pimrpsetgroupmask = YLeaf(YType.str, "pimRPSetGroupMask")

                self.pimrpsetaddress = YLeaf(YType.str, "pimRPSetAddress")

                self.pimrpsetexpirytime = YLeaf(YType.uint32, "pimRPSetExpiryTime")

                self.pimrpsetholdtime = YLeaf(YType.int32, "pimRPSetHoldTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("pimrpsetcomponent",
                                "pimrpsetgroupaddress",
                                "pimrpsetgroupmask",
                                "pimrpsetaddress",
                                "pimrpsetexpirytime",
                                "pimrpsetholdtime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PimMib.Pimrpsettable.Pimrpsetentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PimMib.Pimrpsettable.Pimrpsetentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.pimrpsetcomponent.is_set or
                    self.pimrpsetgroupaddress.is_set or
                    self.pimrpsetgroupmask.is_set or
                    self.pimrpsetaddress.is_set or
                    self.pimrpsetexpirytime.is_set or
                    self.pimrpsetholdtime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.pimrpsetcomponent.yfilter != YFilter.not_set or
                    self.pimrpsetgroupaddress.yfilter != YFilter.not_set or
                    self.pimrpsetgroupmask.yfilter != YFilter.not_set or
                    self.pimrpsetaddress.yfilter != YFilter.not_set or
                    self.pimrpsetexpirytime.yfilter != YFilter.not_set or
                    self.pimrpsetholdtime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "pimRPSetEntry" + "[pimRPSetComponent='" + self.pimrpsetcomponent.get() + "']" + "[pimRPSetGroupAddress='" + self.pimrpsetgroupaddress.get() + "']" + "[pimRPSetGroupMask='" + self.pimrpsetgroupmask.get() + "']" + "[pimRPSetAddress='" + self.pimrpsetaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "PIM-MIB:PIM-MIB/pimRPSetTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.pimrpsetcomponent.is_set or self.pimrpsetcomponent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimrpsetcomponent.get_name_leafdata())
                if (self.pimrpsetgroupaddress.is_set or self.pimrpsetgroupaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimrpsetgroupaddress.get_name_leafdata())
                if (self.pimrpsetgroupmask.is_set or self.pimrpsetgroupmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimrpsetgroupmask.get_name_leafdata())
                if (self.pimrpsetaddress.is_set or self.pimrpsetaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimrpsetaddress.get_name_leafdata())
                if (self.pimrpsetexpirytime.is_set or self.pimrpsetexpirytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimrpsetexpirytime.get_name_leafdata())
                if (self.pimrpsetholdtime.is_set or self.pimrpsetholdtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimrpsetholdtime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "pimRPSetComponent" or name == "pimRPSetGroupAddress" or name == "pimRPSetGroupMask" or name == "pimRPSetAddress" or name == "pimRPSetExpiryTime" or name == "pimRPSetHoldTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "pimRPSetComponent"):
                    self.pimrpsetcomponent = value
                    self.pimrpsetcomponent.value_namespace = name_space
                    self.pimrpsetcomponent.value_namespace_prefix = name_space_prefix
                if(value_path == "pimRPSetGroupAddress"):
                    self.pimrpsetgroupaddress = value
                    self.pimrpsetgroupaddress.value_namespace = name_space
                    self.pimrpsetgroupaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "pimRPSetGroupMask"):
                    self.pimrpsetgroupmask = value
                    self.pimrpsetgroupmask.value_namespace = name_space
                    self.pimrpsetgroupmask.value_namespace_prefix = name_space_prefix
                if(value_path == "pimRPSetAddress"):
                    self.pimrpsetaddress = value
                    self.pimrpsetaddress.value_namespace = name_space
                    self.pimrpsetaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "pimRPSetExpiryTime"):
                    self.pimrpsetexpirytime = value
                    self.pimrpsetexpirytime.value_namespace = name_space
                    self.pimrpsetexpirytime.value_namespace_prefix = name_space_prefix
                if(value_path == "pimRPSetHoldTime"):
                    self.pimrpsetholdtime = value
                    self.pimrpsetholdtime.value_namespace = name_space
                    self.pimrpsetholdtime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.pimrpsetentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.pimrpsetentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "pimRPSetTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "PIM-MIB:PIM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "pimRPSetEntry"):
                for c in self.pimrpsetentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PimMib.Pimrpsettable.Pimrpsetentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.pimrpsetentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "pimRPSetEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Pimipmroutenexthoptable(Entity):
        """
        The (conceptual) table listing PIM\-specific information on
        a subset of the rows of the ipMRouteNextHopTable defined in
        the IP Multicast MIB.
        
        .. attribute:: pimipmroutenexthopentry
        
        	An entry (conceptual row) in the pimIpMRouteNextHopTable. There is one entry per entry in the ipMRouteNextHopTable whose interface is running PIM and whose ipMRouteNextHopState is pruned(1)
        	**type**\: list of    :py:class:`Pimipmroutenexthopentry <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimipmroutenexthoptable.Pimipmroutenexthopentry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(PimMib.Pimipmroutenexthoptable, self).__init__()

            self.yang_name = "pimIpMRouteNextHopTable"
            self.yang_parent_name = "PIM-MIB"

            self.pimipmroutenexthopentry = YList(self)

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
                        super(PimMib.Pimipmroutenexthoptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PimMib.Pimipmroutenexthoptable, self).__setattr__(name, value)


        class Pimipmroutenexthopentry(Entity):
            """
            An entry (conceptual row) in the pimIpMRouteNextHopTable.
            There is one entry per entry in the ipMRouteNextHopTable
            whose interface is running PIM and whose
            ipMRouteNextHopState is pruned(1).
            
            .. attribute:: ipmroutenexthopgroup  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutenexthopgroup <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry>`
            
            .. attribute:: ipmroutenexthopsource  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutenexthopsource <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry>`
            
            .. attribute:: ipmroutenexthopsourcemask  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutenexthopsourcemask <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry>`
            
            .. attribute:: ipmroutenexthopifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ipmroutenexthopifindex <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry>`
            
            .. attribute:: ipmroutenexthopaddress  <key>
            
            	
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**refers to**\:  :py:class:`ipmroutenexthopaddress <ydk.models.cisco_ios_xe.IPMROUTE_STD_MIB.IpmrouteStdMib.Ipmroutenexthoptable.Ipmroutenexthopentry>`
            
            .. attribute:: pimipmroutenexthopprunereason
            
            	This object indicates why the downstream interface was pruned, whether in response to a PIM prune message or due to PIM Assert processing
            	**type**\:   :py:class:`Pimipmroutenexthopprunereason <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimipmroutenexthoptable.Pimipmroutenexthopentry.Pimipmroutenexthopprunereason>`
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(PimMib.Pimipmroutenexthoptable.Pimipmroutenexthopentry, self).__init__()

                self.yang_name = "pimIpMRouteNextHopEntry"
                self.yang_parent_name = "pimIpMRouteNextHopTable"

                self.ipmroutenexthopgroup = YLeaf(YType.str, "ipMRouteNextHopGroup")

                self.ipmroutenexthopsource = YLeaf(YType.str, "ipMRouteNextHopSource")

                self.ipmroutenexthopsourcemask = YLeaf(YType.str, "ipMRouteNextHopSourceMask")

                self.ipmroutenexthopifindex = YLeaf(YType.str, "ipMRouteNextHopIfIndex")

                self.ipmroutenexthopaddress = YLeaf(YType.str, "ipMRouteNextHopAddress")

                self.pimipmroutenexthopprunereason = YLeaf(YType.enumeration, "pimIpMRouteNextHopPruneReason")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipmroutenexthopgroup",
                                "ipmroutenexthopsource",
                                "ipmroutenexthopsourcemask",
                                "ipmroutenexthopifindex",
                                "ipmroutenexthopaddress",
                                "pimipmroutenexthopprunereason") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PimMib.Pimipmroutenexthoptable.Pimipmroutenexthopentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PimMib.Pimipmroutenexthoptable.Pimipmroutenexthopentry, self).__setattr__(name, value)

            class Pimipmroutenexthopprunereason(Enum):
                """
                Pimipmroutenexthopprunereason

                This object indicates why the downstream interface was

                pruned, whether in response to a PIM prune message or due to

                PIM Assert processing.

                .. data:: other = 1

                .. data:: prune = 2

                .. data:: assert_ = 3

                """

                other = Enum.YLeaf(1, "other")

                prune = Enum.YLeaf(2, "prune")

                assert_ = Enum.YLeaf(3, "assert")


            def has_data(self):
                return (
                    self.ipmroutenexthopgroup.is_set or
                    self.ipmroutenexthopsource.is_set or
                    self.ipmroutenexthopsourcemask.is_set or
                    self.ipmroutenexthopifindex.is_set or
                    self.ipmroutenexthopaddress.is_set or
                    self.pimipmroutenexthopprunereason.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipmroutenexthopgroup.yfilter != YFilter.not_set or
                    self.ipmroutenexthopsource.yfilter != YFilter.not_set or
                    self.ipmroutenexthopsourcemask.yfilter != YFilter.not_set or
                    self.ipmroutenexthopifindex.yfilter != YFilter.not_set or
                    self.ipmroutenexthopaddress.yfilter != YFilter.not_set or
                    self.pimipmroutenexthopprunereason.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "pimIpMRouteNextHopEntry" + "[ipMRouteNextHopGroup='" + self.ipmroutenexthopgroup.get() + "']" + "[ipMRouteNextHopSource='" + self.ipmroutenexthopsource.get() + "']" + "[ipMRouteNextHopSourceMask='" + self.ipmroutenexthopsourcemask.get() + "']" + "[ipMRouteNextHopIfIndex='" + self.ipmroutenexthopifindex.get() + "']" + "[ipMRouteNextHopAddress='" + self.ipmroutenexthopaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "PIM-MIB:PIM-MIB/pimIpMRouteNextHopTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipmroutenexthopgroup.is_set or self.ipmroutenexthopgroup.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutenexthopgroup.get_name_leafdata())
                if (self.ipmroutenexthopsource.is_set or self.ipmroutenexthopsource.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutenexthopsource.get_name_leafdata())
                if (self.ipmroutenexthopsourcemask.is_set or self.ipmroutenexthopsourcemask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutenexthopsourcemask.get_name_leafdata())
                if (self.ipmroutenexthopifindex.is_set or self.ipmroutenexthopifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutenexthopifindex.get_name_leafdata())
                if (self.ipmroutenexthopaddress.is_set or self.ipmroutenexthopaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipmroutenexthopaddress.get_name_leafdata())
                if (self.pimipmroutenexthopprunereason.is_set or self.pimipmroutenexthopprunereason.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimipmroutenexthopprunereason.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipMRouteNextHopGroup" or name == "ipMRouteNextHopSource" or name == "ipMRouteNextHopSourceMask" or name == "ipMRouteNextHopIfIndex" or name == "ipMRouteNextHopAddress" or name == "pimIpMRouteNextHopPruneReason"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipMRouteNextHopGroup"):
                    self.ipmroutenexthopgroup = value
                    self.ipmroutenexthopgroup.value_namespace = name_space
                    self.ipmroutenexthopgroup.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteNextHopSource"):
                    self.ipmroutenexthopsource = value
                    self.ipmroutenexthopsource.value_namespace = name_space
                    self.ipmroutenexthopsource.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteNextHopSourceMask"):
                    self.ipmroutenexthopsourcemask = value
                    self.ipmroutenexthopsourcemask.value_namespace = name_space
                    self.ipmroutenexthopsourcemask.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteNextHopIfIndex"):
                    self.ipmroutenexthopifindex = value
                    self.ipmroutenexthopifindex.value_namespace = name_space
                    self.ipmroutenexthopifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipMRouteNextHopAddress"):
                    self.ipmroutenexthopaddress = value
                    self.ipmroutenexthopaddress.value_namespace = name_space
                    self.ipmroutenexthopaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "pimIpMRouteNextHopPruneReason"):
                    self.pimipmroutenexthopprunereason = value
                    self.pimipmroutenexthopprunereason.value_namespace = name_space
                    self.pimipmroutenexthopprunereason.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.pimipmroutenexthopentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.pimipmroutenexthopentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "pimIpMRouteNextHopTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "PIM-MIB:PIM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "pimIpMRouteNextHopEntry"):
                for c in self.pimipmroutenexthopentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PimMib.Pimipmroutenexthoptable.Pimipmroutenexthopentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.pimipmroutenexthopentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "pimIpMRouteNextHopEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Pimcandidaterptable(Entity):
        """
        The (conceptual) table listing the IP multicast groups for
        which the local router is to advertise itself as a
        Candidate\-RP when the value of pimComponentCRPHoldTime is
        non\-zero.  If this table is empty, then the local router
        
        
        
        
        
        will advertise itself as a Candidate\-RP for all groups
        (providing the value of pimComponentCRPHoldTime is non\-
        zero).
        
        .. attribute:: pimcandidaterpentry
        
        	An entry (conceptual row) in the pimCandidateRPTable
        	**type**\: list of    :py:class:`Pimcandidaterpentry <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimcandidaterptable.Pimcandidaterpentry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(PimMib.Pimcandidaterptable, self).__init__()

            self.yang_name = "pimCandidateRPTable"
            self.yang_parent_name = "PIM-MIB"

            self.pimcandidaterpentry = YList(self)

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
                        super(PimMib.Pimcandidaterptable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PimMib.Pimcandidaterptable, self).__setattr__(name, value)


        class Pimcandidaterpentry(Entity):
            """
            An entry (conceptual row) in the pimCandidateRPTable.
            
            .. attribute:: pimcandidaterpgroupaddress  <key>
            
            	The IP multicast group address which, when combined with pimCandidateRPGroupMask, identifies a group prefix for which the local router will advertise itself as a Candidate\-RP
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimcandidaterpgroupmask  <key>
            
            	The multicast group address mask which, when combined with pimCandidateRPGroupMask, identifies a group prefix for which the local router will advertise itself as a Candidate\-RP
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimcandidaterpaddress
            
            	The (unicast) address of the interface which will be      advertised as a Candidate\-RP
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimcandidaterprowstatus
            
            	The status of this row, by which new entries may be created, or old entries deleted from this table
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(PimMib.Pimcandidaterptable.Pimcandidaterpentry, self).__init__()

                self.yang_name = "pimCandidateRPEntry"
                self.yang_parent_name = "pimCandidateRPTable"

                self.pimcandidaterpgroupaddress = YLeaf(YType.str, "pimCandidateRPGroupAddress")

                self.pimcandidaterpgroupmask = YLeaf(YType.str, "pimCandidateRPGroupMask")

                self.pimcandidaterpaddress = YLeaf(YType.str, "pimCandidateRPAddress")

                self.pimcandidaterprowstatus = YLeaf(YType.enumeration, "pimCandidateRPRowStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("pimcandidaterpgroupaddress",
                                "pimcandidaterpgroupmask",
                                "pimcandidaterpaddress",
                                "pimcandidaterprowstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PimMib.Pimcandidaterptable.Pimcandidaterpentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PimMib.Pimcandidaterptable.Pimcandidaterpentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.pimcandidaterpgroupaddress.is_set or
                    self.pimcandidaterpgroupmask.is_set or
                    self.pimcandidaterpaddress.is_set or
                    self.pimcandidaterprowstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.pimcandidaterpgroupaddress.yfilter != YFilter.not_set or
                    self.pimcandidaterpgroupmask.yfilter != YFilter.not_set or
                    self.pimcandidaterpaddress.yfilter != YFilter.not_set or
                    self.pimcandidaterprowstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "pimCandidateRPEntry" + "[pimCandidateRPGroupAddress='" + self.pimcandidaterpgroupaddress.get() + "']" + "[pimCandidateRPGroupMask='" + self.pimcandidaterpgroupmask.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "PIM-MIB:PIM-MIB/pimCandidateRPTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.pimcandidaterpgroupaddress.is_set or self.pimcandidaterpgroupaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimcandidaterpgroupaddress.get_name_leafdata())
                if (self.pimcandidaterpgroupmask.is_set or self.pimcandidaterpgroupmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimcandidaterpgroupmask.get_name_leafdata())
                if (self.pimcandidaterpaddress.is_set or self.pimcandidaterpaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimcandidaterpaddress.get_name_leafdata())
                if (self.pimcandidaterprowstatus.is_set or self.pimcandidaterprowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimcandidaterprowstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "pimCandidateRPGroupAddress" or name == "pimCandidateRPGroupMask" or name == "pimCandidateRPAddress" or name == "pimCandidateRPRowStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "pimCandidateRPGroupAddress"):
                    self.pimcandidaterpgroupaddress = value
                    self.pimcandidaterpgroupaddress.value_namespace = name_space
                    self.pimcandidaterpgroupaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "pimCandidateRPGroupMask"):
                    self.pimcandidaterpgroupmask = value
                    self.pimcandidaterpgroupmask.value_namespace = name_space
                    self.pimcandidaterpgroupmask.value_namespace_prefix = name_space_prefix
                if(value_path == "pimCandidateRPAddress"):
                    self.pimcandidaterpaddress = value
                    self.pimcandidaterpaddress.value_namespace = name_space
                    self.pimcandidaterpaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "pimCandidateRPRowStatus"):
                    self.pimcandidaterprowstatus = value
                    self.pimcandidaterprowstatus.value_namespace = name_space
                    self.pimcandidaterprowstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.pimcandidaterpentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.pimcandidaterpentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "pimCandidateRPTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "PIM-MIB:PIM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "pimCandidateRPEntry"):
                for c in self.pimcandidaterpentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PimMib.Pimcandidaterptable.Pimcandidaterpentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.pimcandidaterpentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "pimCandidateRPEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Pimcomponenttable(Entity):
        """
        The (conceptual) table containing objects specific to a PIM
        domain.  One row exists for each domain to which the router
        is connected.  A PIM\-SM domain is defined as an area of the
        network over which Bootstrap messages are forwarded.
        Typically, a PIM\-SM router will be a member of exactly one
        domain.  This table also supports, however, routers which
        may form a border between two PIM\-SM domains and do not
        forward Bootstrap messages between them.
        
        .. attribute:: pimcomponententry
        
        	An entry (conceptual row) in the pimComponentTable
        	**type**\: list of    :py:class:`Pimcomponententry <ydk.models.cisco_ios_xe.PIM_MIB.PimMib.Pimcomponenttable.Pimcomponententry>`
        
        

        """

        _prefix = 'PIM-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(PimMib.Pimcomponenttable, self).__init__()

            self.yang_name = "pimComponentTable"
            self.yang_parent_name = "PIM-MIB"

            self.pimcomponententry = YList(self)

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
                        super(PimMib.Pimcomponenttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PimMib.Pimcomponenttable, self).__setattr__(name, value)


        class Pimcomponententry(Entity):
            """
            An entry (conceptual row) in the pimComponentTable.
            
            .. attribute:: pimcomponentindex  <key>
            
            	A number uniquely identifying the component.  Each protocol instance connected to a separate domain should have a different index value.  Routers that only support membership in a single PIM\-SM domain should use a pimComponentIndex value of 1
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: pimcomponentbsraddress
            
            	The IP address of the bootstrap router (BSR) for the local PIM region
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: pimcomponentbsrexpirytime
            
            	The minimum time remaining before the bootstrap router in the local domain will be declared down.  For candidate BSRs, this is the time until the component sends an RP\-Set message.  For other routers, this is the time until it may accept an RP\-Set message from a lower candidate BSR
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: pimcomponentcrpholdtime
            
            	The holdtime of the component when it is a candidate RP in the local domain.  The value of 0 is used to indicate that the local system is not a Candidate\-RP
            	**type**\:  int
            
            	**range:** 0..255
            
            	**units**\: seconds
            
            .. attribute:: pimcomponentstatus
            
            	The status of this entry.  Creating the entry creates another protocol instance; destroying the entry disables a protocol instance
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'PIM-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(PimMib.Pimcomponenttable.Pimcomponententry, self).__init__()

                self.yang_name = "pimComponentEntry"
                self.yang_parent_name = "pimComponentTable"

                self.pimcomponentindex = YLeaf(YType.int32, "pimComponentIndex")

                self.pimcomponentbsraddress = YLeaf(YType.str, "pimComponentBSRAddress")

                self.pimcomponentbsrexpirytime = YLeaf(YType.uint32, "pimComponentBSRExpiryTime")

                self.pimcomponentcrpholdtime = YLeaf(YType.int32, "pimComponentCRPHoldTime")

                self.pimcomponentstatus = YLeaf(YType.enumeration, "pimComponentStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("pimcomponentindex",
                                "pimcomponentbsraddress",
                                "pimcomponentbsrexpirytime",
                                "pimcomponentcrpholdtime",
                                "pimcomponentstatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PimMib.Pimcomponenttable.Pimcomponententry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PimMib.Pimcomponenttable.Pimcomponententry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.pimcomponentindex.is_set or
                    self.pimcomponentbsraddress.is_set or
                    self.pimcomponentbsrexpirytime.is_set or
                    self.pimcomponentcrpholdtime.is_set or
                    self.pimcomponentstatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.pimcomponentindex.yfilter != YFilter.not_set or
                    self.pimcomponentbsraddress.yfilter != YFilter.not_set or
                    self.pimcomponentbsrexpirytime.yfilter != YFilter.not_set or
                    self.pimcomponentcrpholdtime.yfilter != YFilter.not_set or
                    self.pimcomponentstatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "pimComponentEntry" + "[pimComponentIndex='" + self.pimcomponentindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "PIM-MIB:PIM-MIB/pimComponentTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.pimcomponentindex.is_set or self.pimcomponentindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimcomponentindex.get_name_leafdata())
                if (self.pimcomponentbsraddress.is_set or self.pimcomponentbsraddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimcomponentbsraddress.get_name_leafdata())
                if (self.pimcomponentbsrexpirytime.is_set or self.pimcomponentbsrexpirytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimcomponentbsrexpirytime.get_name_leafdata())
                if (self.pimcomponentcrpholdtime.is_set or self.pimcomponentcrpholdtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimcomponentcrpholdtime.get_name_leafdata())
                if (self.pimcomponentstatus.is_set or self.pimcomponentstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.pimcomponentstatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "pimComponentIndex" or name == "pimComponentBSRAddress" or name == "pimComponentBSRExpiryTime" or name == "pimComponentCRPHoldTime" or name == "pimComponentStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "pimComponentIndex"):
                    self.pimcomponentindex = value
                    self.pimcomponentindex.value_namespace = name_space
                    self.pimcomponentindex.value_namespace_prefix = name_space_prefix
                if(value_path == "pimComponentBSRAddress"):
                    self.pimcomponentbsraddress = value
                    self.pimcomponentbsraddress.value_namespace = name_space
                    self.pimcomponentbsraddress.value_namespace_prefix = name_space_prefix
                if(value_path == "pimComponentBSRExpiryTime"):
                    self.pimcomponentbsrexpirytime = value
                    self.pimcomponentbsrexpirytime.value_namespace = name_space
                    self.pimcomponentbsrexpirytime.value_namespace_prefix = name_space_prefix
                if(value_path == "pimComponentCRPHoldTime"):
                    self.pimcomponentcrpholdtime = value
                    self.pimcomponentcrpholdtime.value_namespace = name_space
                    self.pimcomponentcrpholdtime.value_namespace_prefix = name_space_prefix
                if(value_path == "pimComponentStatus"):
                    self.pimcomponentstatus = value
                    self.pimcomponentstatus.value_namespace = name_space
                    self.pimcomponentstatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.pimcomponententry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.pimcomponententry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "pimComponentTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "PIM-MIB:PIM-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "pimComponentEntry"):
                for c in self.pimcomponententry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PimMib.Pimcomponenttable.Pimcomponententry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.pimcomponententry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "pimComponentEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.pim is not None and self.pim.has_data()) or
            (self.pimcandidaterptable is not None and self.pimcandidaterptable.has_data()) or
            (self.pimcomponenttable is not None and self.pimcomponenttable.has_data()) or
            (self.piminterfacetable is not None and self.piminterfacetable.has_data()) or
            (self.pimipmroutenexthoptable is not None and self.pimipmroutenexthoptable.has_data()) or
            (self.pimipmroutetable is not None and self.pimipmroutetable.has_data()) or
            (self.pimneighbortable is not None and self.pimneighbortable.has_data()) or
            (self.pimrpsettable is not None and self.pimrpsettable.has_data()) or
            (self.pimrptable is not None and self.pimrptable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.pim is not None and self.pim.has_operation()) or
            (self.pimcandidaterptable is not None and self.pimcandidaterptable.has_operation()) or
            (self.pimcomponenttable is not None and self.pimcomponenttable.has_operation()) or
            (self.piminterfacetable is not None and self.piminterfacetable.has_operation()) or
            (self.pimipmroutenexthoptable is not None and self.pimipmroutenexthoptable.has_operation()) or
            (self.pimipmroutetable is not None and self.pimipmroutetable.has_operation()) or
            (self.pimneighbortable is not None and self.pimneighbortable.has_operation()) or
            (self.pimrpsettable is not None and self.pimrpsettable.has_operation()) or
            (self.pimrptable is not None and self.pimrptable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "PIM-MIB:PIM-MIB" + path_buffer

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

        if (child_yang_name == "pim"):
            if (self.pim is None):
                self.pim = PimMib.Pim()
                self.pim.parent = self
                self._children_name_map["pim"] = "pim"
            return self.pim

        if (child_yang_name == "pimCandidateRPTable"):
            if (self.pimcandidaterptable is None):
                self.pimcandidaterptable = PimMib.Pimcandidaterptable()
                self.pimcandidaterptable.parent = self
                self._children_name_map["pimcandidaterptable"] = "pimCandidateRPTable"
            return self.pimcandidaterptable

        if (child_yang_name == "pimComponentTable"):
            if (self.pimcomponenttable is None):
                self.pimcomponenttable = PimMib.Pimcomponenttable()
                self.pimcomponenttable.parent = self
                self._children_name_map["pimcomponenttable"] = "pimComponentTable"
            return self.pimcomponenttable

        if (child_yang_name == "pimInterfaceTable"):
            if (self.piminterfacetable is None):
                self.piminterfacetable = PimMib.Piminterfacetable()
                self.piminterfacetable.parent = self
                self._children_name_map["piminterfacetable"] = "pimInterfaceTable"
            return self.piminterfacetable

        if (child_yang_name == "pimIpMRouteNextHopTable"):
            if (self.pimipmroutenexthoptable is None):
                self.pimipmroutenexthoptable = PimMib.Pimipmroutenexthoptable()
                self.pimipmroutenexthoptable.parent = self
                self._children_name_map["pimipmroutenexthoptable"] = "pimIpMRouteNextHopTable"
            return self.pimipmroutenexthoptable

        if (child_yang_name == "pimIpMRouteTable"):
            if (self.pimipmroutetable is None):
                self.pimipmroutetable = PimMib.Pimipmroutetable()
                self.pimipmroutetable.parent = self
                self._children_name_map["pimipmroutetable"] = "pimIpMRouteTable"
            return self.pimipmroutetable

        if (child_yang_name == "pimNeighborTable"):
            if (self.pimneighbortable is None):
                self.pimneighbortable = PimMib.Pimneighbortable()
                self.pimneighbortable.parent = self
                self._children_name_map["pimneighbortable"] = "pimNeighborTable"
            return self.pimneighbortable

        if (child_yang_name == "pimRPSetTable"):
            if (self.pimrpsettable is None):
                self.pimrpsettable = PimMib.Pimrpsettable()
                self.pimrpsettable.parent = self
                self._children_name_map["pimrpsettable"] = "pimRPSetTable"
            return self.pimrpsettable

        if (child_yang_name == "pimRPTable"):
            if (self.pimrptable is None):
                self.pimrptable = PimMib.Pimrptable()
                self.pimrptable.parent = self
                self._children_name_map["pimrptable"] = "pimRPTable"
            return self.pimrptable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "pim" or name == "pimCandidateRPTable" or name == "pimComponentTable" or name == "pimInterfaceTable" or name == "pimIpMRouteNextHopTable" or name == "pimIpMRouteTable" or name == "pimNeighborTable" or name == "pimRPSetTable" or name == "pimRPTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = PimMib()
        return self._top_entity

