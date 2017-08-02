""" IGMP_STD_MIB 

The MIB module for IGMP Management.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IgmpStdMib(Entity):
    """
    
    
    .. attribute:: igmpcachetable
    
    	The (conceptual) table listing the IP multicast groups for which there are members on a particular interface
    	**type**\:   :py:class:`Igmpcachetable <ydk.models.cisco_ios_xe.IGMP_STD_MIB.IgmpStdMib.Igmpcachetable>`
    
    .. attribute:: igmpinterfacetable
    
    	The (conceptual) table listing the interfaces on which IGMP is enabled
    	**type**\:   :py:class:`Igmpinterfacetable <ydk.models.cisco_ios_xe.IGMP_STD_MIB.IgmpStdMib.Igmpinterfacetable>`
    
    

    """

    _prefix = 'IGMP-STD-MIB'
    _revision = '2000-09-28'

    def __init__(self):
        super(IgmpStdMib, self).__init__()
        self._top_entity = None

        self.yang_name = "IGMP-STD-MIB"
        self.yang_parent_name = "IGMP-STD-MIB"

        self.igmpcachetable = IgmpStdMib.Igmpcachetable()
        self.igmpcachetable.parent = self
        self._children_name_map["igmpcachetable"] = "igmpCacheTable"
        self._children_yang_names.add("igmpCacheTable")

        self.igmpinterfacetable = IgmpStdMib.Igmpinterfacetable()
        self.igmpinterfacetable.parent = self
        self._children_name_map["igmpinterfacetable"] = "igmpInterfaceTable"
        self._children_yang_names.add("igmpInterfaceTable")


    class Igmpinterfacetable(Entity):
        """
        The (conceptual) table listing the interfaces on which IGMP
        is enabled.
        
        .. attribute:: igmpinterfaceentry
        
        	An entry (conceptual row) representing an interface on which IGMP is enabled
        	**type**\: list of    :py:class:`Igmpinterfaceentry <ydk.models.cisco_ios_xe.IGMP_STD_MIB.IgmpStdMib.Igmpinterfacetable.Igmpinterfaceentry>`
        
        

        """

        _prefix = 'IGMP-STD-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(IgmpStdMib.Igmpinterfacetable, self).__init__()

            self.yang_name = "igmpInterfaceTable"
            self.yang_parent_name = "IGMP-STD-MIB"

            self.igmpinterfaceentry = YList(self)

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
                        super(IgmpStdMib.Igmpinterfacetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IgmpStdMib.Igmpinterfacetable, self).__setattr__(name, value)


        class Igmpinterfaceentry(Entity):
            """
            An entry (conceptual row) representing an interface on
            which IGMP is enabled.
            
            .. attribute:: igmpinterfaceifindex  <key>
            
            	The ifIndex value of the interface for which IGMP is enabled
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: igmpinterfacegroups
            
            	The current number of entries for this interface in the Cache Table
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfacejoins
            
            	The number of times a group membership has been added on this interface; that is, the number of times an entry for this interface has been added to the Cache Table.  This object gives an indication of the amount of IGMP activity over the lifetime of the row entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfacelastmembqueryintvl
            
            	The Last Member Query Interval is the Max Response Time inserted into Group\-Specific Queries sent in response to Leave Group messages, and is also the amount of time between Group\-Specific Query messages.  This value may be tuned to modify the leave latency of the network.  A reduced value results in reduced time to detect the loss of the last member of a group.  The value of this object is irrelevant if igmpInterfaceVersion is 1
            	**type**\:  int
            
            	**range:** 0..255
            
            	**units**\: tenths of seconds
            
            .. attribute:: igmpinterfaceproxyifindex
            
            	Some devices implement a form of IGMP proxying whereby memberships learned on the interface represented by this row, cause IGMP Host Membership Reports to be sent on the interface whose ifIndex value is given by this object.  Such a device would implement the igmpV2RouterMIBGroup only on its router interfaces (those interfaces with non\-zero igmpInterfaceProxyIfIndex).  Typically, the value of this object is 0, indicating that no proxying is being done
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: igmpinterfacequerier
            
            	The address of the IGMP Querier on the IP subnet to which      this interface is attached
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: igmpinterfacequerierexpirytime
            
            	The amount of time remaining before the Other Querier Present Timer expires.  If the local system is the querier, the value of this object is zero
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfacequerieruptime
            
            	The time since igmpInterfaceQuerier was last changed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfacequeryinterval
            
            	The frequency at which IGMP Host\-Query packets are transmitted on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: igmpinterfacequerymaxresponsetime
            
            	The maximum query response time advertised in IGMPv2 queries on this interface
            	**type**\:  int
            
            	**range:** 0..255
            
            	**units**\: tenths of seconds
            
            .. attribute:: igmpinterfacerobustness
            
            	The Robustness Variable allows tuning for the expected packet loss on a subnet.  If a subnet is expected to be lossy, the Robustness Variable may be increased.  IGMP is robust to (Robustness Variable\-1) packet losses
            	**type**\:  int
            
            	**range:** 1..255
            
            .. attribute:: igmpinterfacestatus
            
            	The activation of a row enables IGMP on the interface.  The destruction of a row disables IGMP on the interface
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: igmpinterfaceversion
            
            	The version of IGMP which is running on this interface. This object can be used to configure a router capable of running either value.  For IGMP to function correctly, all routers on a LAN must be configured to run the same version of IGMP on that LAN
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfaceversion1queriertimer
            
            	The time remaining until the host assumes that there are no IGMPv1 routers present on the interface.  While this is non\- zero, the host will reply to all queries with version 1 membership reports
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfacewrongversionqueries
            
            	The number of queries received whose IGMP version does not match igmpInterfaceVersion, over the lifetime of the row entry.  IGMP requires that all routers on a LAN be configured to run the same version of IGMP.  Thus, if any queries are received with the wrong version, this indicates a configuration error
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'IGMP-STD-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(IgmpStdMib.Igmpinterfacetable.Igmpinterfaceentry, self).__init__()

                self.yang_name = "igmpInterfaceEntry"
                self.yang_parent_name = "igmpInterfaceTable"

                self.igmpinterfaceifindex = YLeaf(YType.int32, "igmpInterfaceIfIndex")

                self.igmpinterfacegroups = YLeaf(YType.uint32, "igmpInterfaceGroups")

                self.igmpinterfacejoins = YLeaf(YType.uint32, "igmpInterfaceJoins")

                self.igmpinterfacelastmembqueryintvl = YLeaf(YType.uint32, "igmpInterfaceLastMembQueryIntvl")

                self.igmpinterfaceproxyifindex = YLeaf(YType.int32, "igmpInterfaceProxyIfIndex")

                self.igmpinterfacequerier = YLeaf(YType.str, "igmpInterfaceQuerier")

                self.igmpinterfacequerierexpirytime = YLeaf(YType.uint32, "igmpInterfaceQuerierExpiryTime")

                self.igmpinterfacequerieruptime = YLeaf(YType.uint32, "igmpInterfaceQuerierUpTime")

                self.igmpinterfacequeryinterval = YLeaf(YType.uint32, "igmpInterfaceQueryInterval")

                self.igmpinterfacequerymaxresponsetime = YLeaf(YType.uint32, "igmpInterfaceQueryMaxResponseTime")

                self.igmpinterfacerobustness = YLeaf(YType.uint32, "igmpInterfaceRobustness")

                self.igmpinterfacestatus = YLeaf(YType.enumeration, "igmpInterfaceStatus")

                self.igmpinterfaceversion = YLeaf(YType.uint32, "igmpInterfaceVersion")

                self.igmpinterfaceversion1queriertimer = YLeaf(YType.uint32, "igmpInterfaceVersion1QuerierTimer")

                self.igmpinterfacewrongversionqueries = YLeaf(YType.uint32, "igmpInterfaceWrongVersionQueries")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("igmpinterfaceifindex",
                                "igmpinterfacegroups",
                                "igmpinterfacejoins",
                                "igmpinterfacelastmembqueryintvl",
                                "igmpinterfaceproxyifindex",
                                "igmpinterfacequerier",
                                "igmpinterfacequerierexpirytime",
                                "igmpinterfacequerieruptime",
                                "igmpinterfacequeryinterval",
                                "igmpinterfacequerymaxresponsetime",
                                "igmpinterfacerobustness",
                                "igmpinterfacestatus",
                                "igmpinterfaceversion",
                                "igmpinterfaceversion1queriertimer",
                                "igmpinterfacewrongversionqueries") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IgmpStdMib.Igmpinterfacetable.Igmpinterfaceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IgmpStdMib.Igmpinterfacetable.Igmpinterfaceentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.igmpinterfaceifindex.is_set or
                    self.igmpinterfacegroups.is_set or
                    self.igmpinterfacejoins.is_set or
                    self.igmpinterfacelastmembqueryintvl.is_set or
                    self.igmpinterfaceproxyifindex.is_set or
                    self.igmpinterfacequerier.is_set or
                    self.igmpinterfacequerierexpirytime.is_set or
                    self.igmpinterfacequerieruptime.is_set or
                    self.igmpinterfacequeryinterval.is_set or
                    self.igmpinterfacequerymaxresponsetime.is_set or
                    self.igmpinterfacerobustness.is_set or
                    self.igmpinterfacestatus.is_set or
                    self.igmpinterfaceversion.is_set or
                    self.igmpinterfaceversion1queriertimer.is_set or
                    self.igmpinterfacewrongversionqueries.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.igmpinterfaceifindex.yfilter != YFilter.not_set or
                    self.igmpinterfacegroups.yfilter != YFilter.not_set or
                    self.igmpinterfacejoins.yfilter != YFilter.not_set or
                    self.igmpinterfacelastmembqueryintvl.yfilter != YFilter.not_set or
                    self.igmpinterfaceproxyifindex.yfilter != YFilter.not_set or
                    self.igmpinterfacequerier.yfilter != YFilter.not_set or
                    self.igmpinterfacequerierexpirytime.yfilter != YFilter.not_set or
                    self.igmpinterfacequerieruptime.yfilter != YFilter.not_set or
                    self.igmpinterfacequeryinterval.yfilter != YFilter.not_set or
                    self.igmpinterfacequerymaxresponsetime.yfilter != YFilter.not_set or
                    self.igmpinterfacerobustness.yfilter != YFilter.not_set or
                    self.igmpinterfacestatus.yfilter != YFilter.not_set or
                    self.igmpinterfaceversion.yfilter != YFilter.not_set or
                    self.igmpinterfaceversion1queriertimer.yfilter != YFilter.not_set or
                    self.igmpinterfacewrongversionqueries.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "igmpInterfaceEntry" + "[igmpInterfaceIfIndex='" + self.igmpinterfaceifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IGMP-STD-MIB:IGMP-STD-MIB/igmpInterfaceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.igmpinterfaceifindex.is_set or self.igmpinterfaceifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpinterfaceifindex.get_name_leafdata())
                if (self.igmpinterfacegroups.is_set or self.igmpinterfacegroups.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpinterfacegroups.get_name_leafdata())
                if (self.igmpinterfacejoins.is_set or self.igmpinterfacejoins.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpinterfacejoins.get_name_leafdata())
                if (self.igmpinterfacelastmembqueryintvl.is_set or self.igmpinterfacelastmembqueryintvl.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpinterfacelastmembqueryintvl.get_name_leafdata())
                if (self.igmpinterfaceproxyifindex.is_set or self.igmpinterfaceproxyifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpinterfaceproxyifindex.get_name_leafdata())
                if (self.igmpinterfacequerier.is_set or self.igmpinterfacequerier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpinterfacequerier.get_name_leafdata())
                if (self.igmpinterfacequerierexpirytime.is_set or self.igmpinterfacequerierexpirytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpinterfacequerierexpirytime.get_name_leafdata())
                if (self.igmpinterfacequerieruptime.is_set or self.igmpinterfacequerieruptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpinterfacequerieruptime.get_name_leafdata())
                if (self.igmpinterfacequeryinterval.is_set or self.igmpinterfacequeryinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpinterfacequeryinterval.get_name_leafdata())
                if (self.igmpinterfacequerymaxresponsetime.is_set or self.igmpinterfacequerymaxresponsetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpinterfacequerymaxresponsetime.get_name_leafdata())
                if (self.igmpinterfacerobustness.is_set or self.igmpinterfacerobustness.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpinterfacerobustness.get_name_leafdata())
                if (self.igmpinterfacestatus.is_set or self.igmpinterfacestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpinterfacestatus.get_name_leafdata())
                if (self.igmpinterfaceversion.is_set or self.igmpinterfaceversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpinterfaceversion.get_name_leafdata())
                if (self.igmpinterfaceversion1queriertimer.is_set or self.igmpinterfaceversion1queriertimer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpinterfaceversion1queriertimer.get_name_leafdata())
                if (self.igmpinterfacewrongversionqueries.is_set or self.igmpinterfacewrongversionqueries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpinterfacewrongversionqueries.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "igmpInterfaceIfIndex" or name == "igmpInterfaceGroups" or name == "igmpInterfaceJoins" or name == "igmpInterfaceLastMembQueryIntvl" or name == "igmpInterfaceProxyIfIndex" or name == "igmpInterfaceQuerier" or name == "igmpInterfaceQuerierExpiryTime" or name == "igmpInterfaceQuerierUpTime" or name == "igmpInterfaceQueryInterval" or name == "igmpInterfaceQueryMaxResponseTime" or name == "igmpInterfaceRobustness" or name == "igmpInterfaceStatus" or name == "igmpInterfaceVersion" or name == "igmpInterfaceVersion1QuerierTimer" or name == "igmpInterfaceWrongVersionQueries"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "igmpInterfaceIfIndex"):
                    self.igmpinterfaceifindex = value
                    self.igmpinterfaceifindex.value_namespace = name_space
                    self.igmpinterfaceifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpInterfaceGroups"):
                    self.igmpinterfacegroups = value
                    self.igmpinterfacegroups.value_namespace = name_space
                    self.igmpinterfacegroups.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpInterfaceJoins"):
                    self.igmpinterfacejoins = value
                    self.igmpinterfacejoins.value_namespace = name_space
                    self.igmpinterfacejoins.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpInterfaceLastMembQueryIntvl"):
                    self.igmpinterfacelastmembqueryintvl = value
                    self.igmpinterfacelastmembqueryintvl.value_namespace = name_space
                    self.igmpinterfacelastmembqueryintvl.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpInterfaceProxyIfIndex"):
                    self.igmpinterfaceproxyifindex = value
                    self.igmpinterfaceproxyifindex.value_namespace = name_space
                    self.igmpinterfaceproxyifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpInterfaceQuerier"):
                    self.igmpinterfacequerier = value
                    self.igmpinterfacequerier.value_namespace = name_space
                    self.igmpinterfacequerier.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpInterfaceQuerierExpiryTime"):
                    self.igmpinterfacequerierexpirytime = value
                    self.igmpinterfacequerierexpirytime.value_namespace = name_space
                    self.igmpinterfacequerierexpirytime.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpInterfaceQuerierUpTime"):
                    self.igmpinterfacequerieruptime = value
                    self.igmpinterfacequerieruptime.value_namespace = name_space
                    self.igmpinterfacequerieruptime.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpInterfaceQueryInterval"):
                    self.igmpinterfacequeryinterval = value
                    self.igmpinterfacequeryinterval.value_namespace = name_space
                    self.igmpinterfacequeryinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpInterfaceQueryMaxResponseTime"):
                    self.igmpinterfacequerymaxresponsetime = value
                    self.igmpinterfacequerymaxresponsetime.value_namespace = name_space
                    self.igmpinterfacequerymaxresponsetime.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpInterfaceRobustness"):
                    self.igmpinterfacerobustness = value
                    self.igmpinterfacerobustness.value_namespace = name_space
                    self.igmpinterfacerobustness.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpInterfaceStatus"):
                    self.igmpinterfacestatus = value
                    self.igmpinterfacestatus.value_namespace = name_space
                    self.igmpinterfacestatus.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpInterfaceVersion"):
                    self.igmpinterfaceversion = value
                    self.igmpinterfaceversion.value_namespace = name_space
                    self.igmpinterfaceversion.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpInterfaceVersion1QuerierTimer"):
                    self.igmpinterfaceversion1queriertimer = value
                    self.igmpinterfaceversion1queriertimer.value_namespace = name_space
                    self.igmpinterfaceversion1queriertimer.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpInterfaceWrongVersionQueries"):
                    self.igmpinterfacewrongversionqueries = value
                    self.igmpinterfacewrongversionqueries.value_namespace = name_space
                    self.igmpinterfacewrongversionqueries.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.igmpinterfaceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.igmpinterfaceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "igmpInterfaceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IGMP-STD-MIB:IGMP-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "igmpInterfaceEntry"):
                for c in self.igmpinterfaceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IgmpStdMib.Igmpinterfacetable.Igmpinterfaceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.igmpinterfaceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "igmpInterfaceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Igmpcachetable(Entity):
        """
        The (conceptual) table listing the IP multicast groups for
        which there are members on a particular interface.
        
        .. attribute:: igmpcacheentry
        
        	An entry (conceptual row) in the igmpCacheTable
        	**type**\: list of    :py:class:`Igmpcacheentry <ydk.models.cisco_ios_xe.IGMP_STD_MIB.IgmpStdMib.Igmpcachetable.Igmpcacheentry>`
        
        

        """

        _prefix = 'IGMP-STD-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(IgmpStdMib.Igmpcachetable, self).__init__()

            self.yang_name = "igmpCacheTable"
            self.yang_parent_name = "IGMP-STD-MIB"

            self.igmpcacheentry = YList(self)

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
                        super(IgmpStdMib.Igmpcachetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IgmpStdMib.Igmpcachetable, self).__setattr__(name, value)


        class Igmpcacheentry(Entity):
            """
            An entry (conceptual row) in the igmpCacheTable.
            
            .. attribute:: igmpcacheaddress  <key>
            
            	The IP multicast group address for which this entry contains information
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: igmpcacheifindex  <key>
            
            	The interface for which this entry contains information for an IP multicast group address
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: igmpcacheexpirytime
            
            	The minimum amount of time remaining before this entry will be aged out.  A value of 0 indicates that the entry is only present because igmpCacheSelf is true and that if the router left the group, this entry would be aged out immediately. Note that some implementations may process membership reports from the local system in the same way as reports from other hosts, so a value of 0 is not required
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpcachelastreporter
            
            	The IP address of the source of the last membership report received for this IP Multicast group address on this interface.  If no membership report has been received, this object has the value 0.0.0.0
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: igmpcacheself
            
            	An indication of whether the local system is a member of this group address on this interface
            	**type**\:  bool
            
            .. attribute:: igmpcachestatus
            
            	The status of this entry
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: igmpcacheuptime
            
            	The time elapsed since this entry was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpcacheversion1hosttimer
            
            	The time remaining until the local router will assume that there are no longer any IGMP version 1 members on the IP subnet attached to this interface.  Upon hearing any IGMPv1 Membership Report, this value is reset to the group membership timer.  While this time remaining is non\-zero, the local router ignores any IGMPv2 Leave messages for this group that it receives on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'IGMP-STD-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(IgmpStdMib.Igmpcachetable.Igmpcacheentry, self).__init__()

                self.yang_name = "igmpCacheEntry"
                self.yang_parent_name = "igmpCacheTable"

                self.igmpcacheaddress = YLeaf(YType.str, "igmpCacheAddress")

                self.igmpcacheifindex = YLeaf(YType.int32, "igmpCacheIfIndex")

                self.igmpcacheexpirytime = YLeaf(YType.uint32, "igmpCacheExpiryTime")

                self.igmpcachelastreporter = YLeaf(YType.str, "igmpCacheLastReporter")

                self.igmpcacheself = YLeaf(YType.boolean, "igmpCacheSelf")

                self.igmpcachestatus = YLeaf(YType.enumeration, "igmpCacheStatus")

                self.igmpcacheuptime = YLeaf(YType.uint32, "igmpCacheUpTime")

                self.igmpcacheversion1hosttimer = YLeaf(YType.uint32, "igmpCacheVersion1HostTimer")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("igmpcacheaddress",
                                "igmpcacheifindex",
                                "igmpcacheexpirytime",
                                "igmpcachelastreporter",
                                "igmpcacheself",
                                "igmpcachestatus",
                                "igmpcacheuptime",
                                "igmpcacheversion1hosttimer") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IgmpStdMib.Igmpcachetable.Igmpcacheentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IgmpStdMib.Igmpcachetable.Igmpcacheentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.igmpcacheaddress.is_set or
                    self.igmpcacheifindex.is_set or
                    self.igmpcacheexpirytime.is_set or
                    self.igmpcachelastreporter.is_set or
                    self.igmpcacheself.is_set or
                    self.igmpcachestatus.is_set or
                    self.igmpcacheuptime.is_set or
                    self.igmpcacheversion1hosttimer.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.igmpcacheaddress.yfilter != YFilter.not_set or
                    self.igmpcacheifindex.yfilter != YFilter.not_set or
                    self.igmpcacheexpirytime.yfilter != YFilter.not_set or
                    self.igmpcachelastreporter.yfilter != YFilter.not_set or
                    self.igmpcacheself.yfilter != YFilter.not_set or
                    self.igmpcachestatus.yfilter != YFilter.not_set or
                    self.igmpcacheuptime.yfilter != YFilter.not_set or
                    self.igmpcacheversion1hosttimer.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "igmpCacheEntry" + "[igmpCacheAddress='" + self.igmpcacheaddress.get() + "']" + "[igmpCacheIfIndex='" + self.igmpcacheifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IGMP-STD-MIB:IGMP-STD-MIB/igmpCacheTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.igmpcacheaddress.is_set or self.igmpcacheaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpcacheaddress.get_name_leafdata())
                if (self.igmpcacheifindex.is_set or self.igmpcacheifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpcacheifindex.get_name_leafdata())
                if (self.igmpcacheexpirytime.is_set or self.igmpcacheexpirytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpcacheexpirytime.get_name_leafdata())
                if (self.igmpcachelastreporter.is_set or self.igmpcachelastreporter.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpcachelastreporter.get_name_leafdata())
                if (self.igmpcacheself.is_set or self.igmpcacheself.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpcacheself.get_name_leafdata())
                if (self.igmpcachestatus.is_set or self.igmpcachestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpcachestatus.get_name_leafdata())
                if (self.igmpcacheuptime.is_set or self.igmpcacheuptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpcacheuptime.get_name_leafdata())
                if (self.igmpcacheversion1hosttimer.is_set or self.igmpcacheversion1hosttimer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.igmpcacheversion1hosttimer.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "igmpCacheAddress" or name == "igmpCacheIfIndex" or name == "igmpCacheExpiryTime" or name == "igmpCacheLastReporter" or name == "igmpCacheSelf" or name == "igmpCacheStatus" or name == "igmpCacheUpTime" or name == "igmpCacheVersion1HostTimer"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "igmpCacheAddress"):
                    self.igmpcacheaddress = value
                    self.igmpcacheaddress.value_namespace = name_space
                    self.igmpcacheaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpCacheIfIndex"):
                    self.igmpcacheifindex = value
                    self.igmpcacheifindex.value_namespace = name_space
                    self.igmpcacheifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpCacheExpiryTime"):
                    self.igmpcacheexpirytime = value
                    self.igmpcacheexpirytime.value_namespace = name_space
                    self.igmpcacheexpirytime.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpCacheLastReporter"):
                    self.igmpcachelastreporter = value
                    self.igmpcachelastreporter.value_namespace = name_space
                    self.igmpcachelastreporter.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpCacheSelf"):
                    self.igmpcacheself = value
                    self.igmpcacheself.value_namespace = name_space
                    self.igmpcacheself.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpCacheStatus"):
                    self.igmpcachestatus = value
                    self.igmpcachestatus.value_namespace = name_space
                    self.igmpcachestatus.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpCacheUpTime"):
                    self.igmpcacheuptime = value
                    self.igmpcacheuptime.value_namespace = name_space
                    self.igmpcacheuptime.value_namespace_prefix = name_space_prefix
                if(value_path == "igmpCacheVersion1HostTimer"):
                    self.igmpcacheversion1hosttimer = value
                    self.igmpcacheversion1hosttimer.value_namespace = name_space
                    self.igmpcacheversion1hosttimer.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.igmpcacheentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.igmpcacheentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "igmpCacheTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IGMP-STD-MIB:IGMP-STD-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "igmpCacheEntry"):
                for c in self.igmpcacheentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IgmpStdMib.Igmpcachetable.Igmpcacheentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.igmpcacheentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "igmpCacheEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.igmpcachetable is not None and self.igmpcachetable.has_data()) or
            (self.igmpinterfacetable is not None and self.igmpinterfacetable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.igmpcachetable is not None and self.igmpcachetable.has_operation()) or
            (self.igmpinterfacetable is not None and self.igmpinterfacetable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "IGMP-STD-MIB:IGMP-STD-MIB" + path_buffer

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

        if (child_yang_name == "igmpCacheTable"):
            if (self.igmpcachetable is None):
                self.igmpcachetable = IgmpStdMib.Igmpcachetable()
                self.igmpcachetable.parent = self
                self._children_name_map["igmpcachetable"] = "igmpCacheTable"
            return self.igmpcachetable

        if (child_yang_name == "igmpInterfaceTable"):
            if (self.igmpinterfacetable is None):
                self.igmpinterfacetable = IgmpStdMib.Igmpinterfacetable()
                self.igmpinterfacetable.parent = self
                self._children_name_map["igmpinterfacetable"] = "igmpInterfaceTable"
            return self.igmpinterfacetable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "igmpCacheTable" or name == "igmpInterfaceTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = IgmpStdMib()
        return self._top_entity

