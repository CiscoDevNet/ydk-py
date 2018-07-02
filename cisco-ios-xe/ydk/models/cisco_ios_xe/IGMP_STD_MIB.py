""" IGMP_STD_MIB 

The MIB module for IGMP Management.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class IGMPSTDMIB(Entity):
    """
    
    
    .. attribute:: igmpinterfacetable
    
    	The (conceptual) table listing the interfaces on which IGMP is enabled
    	**type**\:  :py:class:`IgmpInterfaceTable <ydk.models.cisco_ios_xe.IGMP_STD_MIB.IGMPSTDMIB.IgmpInterfaceTable>`
    
    .. attribute:: igmpcachetable
    
    	The (conceptual) table listing the IP multicast groups for which there are members on a particular interface
    	**type**\:  :py:class:`IgmpCacheTable <ydk.models.cisco_ios_xe.IGMP_STD_MIB.IGMPSTDMIB.IgmpCacheTable>`
    
    

    """

    _prefix = 'IGMP-STD-MIB'
    _revision = '2000-09-28'

    def __init__(self):
        super(IGMPSTDMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "IGMP-STD-MIB"
        self.yang_parent_name = "IGMP-STD-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("igmpInterfaceTable", ("igmpinterfacetable", IGMPSTDMIB.IgmpInterfaceTable)), ("igmpCacheTable", ("igmpcachetable", IGMPSTDMIB.IgmpCacheTable))])
        self._leafs = OrderedDict()

        self.igmpinterfacetable = IGMPSTDMIB.IgmpInterfaceTable()
        self.igmpinterfacetable.parent = self
        self._children_name_map["igmpinterfacetable"] = "igmpInterfaceTable"

        self.igmpcachetable = IGMPSTDMIB.IgmpCacheTable()
        self.igmpcachetable.parent = self
        self._children_name_map["igmpcachetable"] = "igmpCacheTable"
        self._segment_path = lambda: "IGMP-STD-MIB:IGMP-STD-MIB"

    def __setattr__(self, name, value):
        self._perform_setattr(IGMPSTDMIB, [], name, value)


    class IgmpInterfaceTable(Entity):
        """
        The (conceptual) table listing the interfaces on which IGMP
        is enabled.
        
        .. attribute:: igmpinterfaceentry
        
        	An entry (conceptual row) representing an interface on which IGMP is enabled
        	**type**\: list of  		 :py:class:`IgmpInterfaceEntry <ydk.models.cisco_ios_xe.IGMP_STD_MIB.IGMPSTDMIB.IgmpInterfaceTable.IgmpInterfaceEntry>`
        
        

        """

        _prefix = 'IGMP-STD-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(IGMPSTDMIB.IgmpInterfaceTable, self).__init__()

            self.yang_name = "igmpInterfaceTable"
            self.yang_parent_name = "IGMP-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("igmpInterfaceEntry", ("igmpinterfaceentry", IGMPSTDMIB.IgmpInterfaceTable.IgmpInterfaceEntry))])
            self._leafs = OrderedDict()

            self.igmpinterfaceentry = YList(self)
            self._segment_path = lambda: "igmpInterfaceTable"
            self._absolute_path = lambda: "IGMP-STD-MIB:IGMP-STD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IGMPSTDMIB.IgmpInterfaceTable, [], name, value)


        class IgmpInterfaceEntry(Entity):
            """
            An entry (conceptual row) representing an interface on
            which IGMP is enabled.
            
            .. attribute:: igmpinterfaceifindex  (key)
            
            	The ifIndex value of the interface for which IGMP is enabled
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: igmpinterfacequeryinterval
            
            	The frequency at which IGMP Host\-Query packets are transmitted on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: igmpinterfacestatus
            
            	The activation of a row enables IGMP on the interface.  The destruction of a row disables IGMP on the interface
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: igmpinterfaceversion
            
            	The version of IGMP which is running on this interface. This object can be used to configure a router capable of running either value.  For IGMP to function correctly, all routers on a LAN must be configured to run the same version of IGMP on that LAN
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfacequerier
            
            	The address of the IGMP Querier on the IP subnet to which      this interface is attached
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: igmpinterfacequerymaxresponsetime
            
            	The maximum query response time advertised in IGMPv2 queries on this interface
            	**type**\: int
            
            	**range:** 0..255
            
            	**units**\: tenths of seconds
            
            .. attribute:: igmpinterfacequerieruptime
            
            	The time since igmpInterfaceQuerier was last changed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfacequerierexpirytime
            
            	The amount of time remaining before the Other Querier Present Timer expires.  If the local system is the querier, the value of this object is zero
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfaceversion1queriertimer
            
            	The time remaining until the host assumes that there are no IGMPv1 routers present on the interface.  While this is non\- zero, the host will reply to all queries with version 1 membership reports
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfacewrongversionqueries
            
            	The number of queries received whose IGMP version does not match igmpInterfaceVersion, over the lifetime of the row entry.  IGMP requires that all routers on a LAN be configured to run the same version of IGMP.  Thus, if any queries are received with the wrong version, this indicates a configuration error
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfacejoins
            
            	The number of times a group membership has been added on this interface; that is, the number of times an entry for this interface has been added to the Cache Table.  This object gives an indication of the amount of IGMP activity over the lifetime of the row entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfaceproxyifindex
            
            	Some devices implement a form of IGMP proxying whereby memberships learned on the interface represented by this row, cause IGMP Host Membership Reports to be sent on the interface whose ifIndex value is given by this object.  Such a device would implement the igmpV2RouterMIBGroup only on its router interfaces (those interfaces with non\-zero igmpInterfaceProxyIfIndex).  Typically, the value of this object is 0, indicating that no proxying is being done
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: igmpinterfacegroups
            
            	The current number of entries for this interface in the Cache Table
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpinterfacerobustness
            
            	The Robustness Variable allows tuning for the expected packet loss on a subnet.  If a subnet is expected to be lossy, the Robustness Variable may be increased.  IGMP is robust to (Robustness Variable\-1) packet losses
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: igmpinterfacelastmembqueryintvl
            
            	The Last Member Query Interval is the Max Response Time inserted into Group\-Specific Queries sent in response to Leave Group messages, and is also the amount of time between Group\-Specific Query messages.  This value may be tuned to modify the leave latency of the network.  A reduced value results in reduced time to detect the loss of the last member of a group.  The value of this object is irrelevant if igmpInterfaceVersion is 1
            	**type**\: int
            
            	**range:** 0..255
            
            	**units**\: tenths of seconds
            
            

            """

            _prefix = 'IGMP-STD-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(IGMPSTDMIB.IgmpInterfaceTable.IgmpInterfaceEntry, self).__init__()

                self.yang_name = "igmpInterfaceEntry"
                self.yang_parent_name = "igmpInterfaceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['igmpinterfaceifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('igmpinterfaceifindex', YLeaf(YType.int32, 'igmpInterfaceIfIndex')),
                    ('igmpinterfacequeryinterval', YLeaf(YType.uint32, 'igmpInterfaceQueryInterval')),
                    ('igmpinterfacestatus', YLeaf(YType.enumeration, 'igmpInterfaceStatus')),
                    ('igmpinterfaceversion', YLeaf(YType.uint32, 'igmpInterfaceVersion')),
                    ('igmpinterfacequerier', YLeaf(YType.str, 'igmpInterfaceQuerier')),
                    ('igmpinterfacequerymaxresponsetime', YLeaf(YType.uint32, 'igmpInterfaceQueryMaxResponseTime')),
                    ('igmpinterfacequerieruptime', YLeaf(YType.uint32, 'igmpInterfaceQuerierUpTime')),
                    ('igmpinterfacequerierexpirytime', YLeaf(YType.uint32, 'igmpInterfaceQuerierExpiryTime')),
                    ('igmpinterfaceversion1queriertimer', YLeaf(YType.uint32, 'igmpInterfaceVersion1QuerierTimer')),
                    ('igmpinterfacewrongversionqueries', YLeaf(YType.uint32, 'igmpInterfaceWrongVersionQueries')),
                    ('igmpinterfacejoins', YLeaf(YType.uint32, 'igmpInterfaceJoins')),
                    ('igmpinterfaceproxyifindex', YLeaf(YType.int32, 'igmpInterfaceProxyIfIndex')),
                    ('igmpinterfacegroups', YLeaf(YType.uint32, 'igmpInterfaceGroups')),
                    ('igmpinterfacerobustness', YLeaf(YType.uint32, 'igmpInterfaceRobustness')),
                    ('igmpinterfacelastmembqueryintvl', YLeaf(YType.uint32, 'igmpInterfaceLastMembQueryIntvl')),
                ])
                self.igmpinterfaceifindex = None
                self.igmpinterfacequeryinterval = None
                self.igmpinterfacestatus = None
                self.igmpinterfaceversion = None
                self.igmpinterfacequerier = None
                self.igmpinterfacequerymaxresponsetime = None
                self.igmpinterfacequerieruptime = None
                self.igmpinterfacequerierexpirytime = None
                self.igmpinterfaceversion1queriertimer = None
                self.igmpinterfacewrongversionqueries = None
                self.igmpinterfacejoins = None
                self.igmpinterfaceproxyifindex = None
                self.igmpinterfacegroups = None
                self.igmpinterfacerobustness = None
                self.igmpinterfacelastmembqueryintvl = None
                self._segment_path = lambda: "igmpInterfaceEntry" + "[igmpInterfaceIfIndex='" + str(self.igmpinterfaceifindex) + "']"
                self._absolute_path = lambda: "IGMP-STD-MIB:IGMP-STD-MIB/igmpInterfaceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IGMPSTDMIB.IgmpInterfaceTable.IgmpInterfaceEntry, ['igmpinterfaceifindex', 'igmpinterfacequeryinterval', 'igmpinterfacestatus', 'igmpinterfaceversion', 'igmpinterfacequerier', 'igmpinterfacequerymaxresponsetime', 'igmpinterfacequerieruptime', 'igmpinterfacequerierexpirytime', 'igmpinterfaceversion1queriertimer', 'igmpinterfacewrongversionqueries', 'igmpinterfacejoins', 'igmpinterfaceproxyifindex', 'igmpinterfacegroups', 'igmpinterfacerobustness', 'igmpinterfacelastmembqueryintvl'], name, value)


    class IgmpCacheTable(Entity):
        """
        The (conceptual) table listing the IP multicast groups for
        which there are members on a particular interface.
        
        .. attribute:: igmpcacheentry
        
        	An entry (conceptual row) in the igmpCacheTable
        	**type**\: list of  		 :py:class:`IgmpCacheEntry <ydk.models.cisco_ios_xe.IGMP_STD_MIB.IGMPSTDMIB.IgmpCacheTable.IgmpCacheEntry>`
        
        

        """

        _prefix = 'IGMP-STD-MIB'
        _revision = '2000-09-28'

        def __init__(self):
            super(IGMPSTDMIB.IgmpCacheTable, self).__init__()

            self.yang_name = "igmpCacheTable"
            self.yang_parent_name = "IGMP-STD-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("igmpCacheEntry", ("igmpcacheentry", IGMPSTDMIB.IgmpCacheTable.IgmpCacheEntry))])
            self._leafs = OrderedDict()

            self.igmpcacheentry = YList(self)
            self._segment_path = lambda: "igmpCacheTable"
            self._absolute_path = lambda: "IGMP-STD-MIB:IGMP-STD-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IGMPSTDMIB.IgmpCacheTable, [], name, value)


        class IgmpCacheEntry(Entity):
            """
            An entry (conceptual row) in the igmpCacheTable.
            
            .. attribute:: igmpcacheaddress  (key)
            
            	The IP multicast group address for which this entry contains information
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: igmpcacheifindex  (key)
            
            	The interface for which this entry contains information for an IP multicast group address
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: igmpcacheself
            
            	An indication of whether the local system is a member of this group address on this interface
            	**type**\: bool
            
            .. attribute:: igmpcachelastreporter
            
            	The IP address of the source of the last membership report received for this IP Multicast group address on this interface.  If no membership report has been received, this object has the value 0.0.0.0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: igmpcacheuptime
            
            	The time elapsed since this entry was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpcacheexpirytime
            
            	The minimum amount of time remaining before this entry will be aged out.  A value of 0 indicates that the entry is only present because igmpCacheSelf is true and that if the router left the group, this entry would be aged out immediately. Note that some implementations may process membership reports from the local system in the same way as reports from other hosts, so a value of 0 is not required
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: igmpcachestatus
            
            	The status of this entry
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: igmpcacheversion1hosttimer
            
            	The time remaining until the local router will assume that there are no longer any IGMP version 1 members on the IP subnet attached to this interface.  Upon hearing any IGMPv1 Membership Report, this value is reset to the group membership timer.  While this time remaining is non\-zero, the local router ignores any IGMPv2 Leave messages for this group that it receives on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'IGMP-STD-MIB'
            _revision = '2000-09-28'

            def __init__(self):
                super(IGMPSTDMIB.IgmpCacheTable.IgmpCacheEntry, self).__init__()

                self.yang_name = "igmpCacheEntry"
                self.yang_parent_name = "igmpCacheTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['igmpcacheaddress','igmpcacheifindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('igmpcacheaddress', YLeaf(YType.str, 'igmpCacheAddress')),
                    ('igmpcacheifindex', YLeaf(YType.int32, 'igmpCacheIfIndex')),
                    ('igmpcacheself', YLeaf(YType.boolean, 'igmpCacheSelf')),
                    ('igmpcachelastreporter', YLeaf(YType.str, 'igmpCacheLastReporter')),
                    ('igmpcacheuptime', YLeaf(YType.uint32, 'igmpCacheUpTime')),
                    ('igmpcacheexpirytime', YLeaf(YType.uint32, 'igmpCacheExpiryTime')),
                    ('igmpcachestatus', YLeaf(YType.enumeration, 'igmpCacheStatus')),
                    ('igmpcacheversion1hosttimer', YLeaf(YType.uint32, 'igmpCacheVersion1HostTimer')),
                ])
                self.igmpcacheaddress = None
                self.igmpcacheifindex = None
                self.igmpcacheself = None
                self.igmpcachelastreporter = None
                self.igmpcacheuptime = None
                self.igmpcacheexpirytime = None
                self.igmpcachestatus = None
                self.igmpcacheversion1hosttimer = None
                self._segment_path = lambda: "igmpCacheEntry" + "[igmpCacheAddress='" + str(self.igmpcacheaddress) + "']" + "[igmpCacheIfIndex='" + str(self.igmpcacheifindex) + "']"
                self._absolute_path = lambda: "IGMP-STD-MIB:IGMP-STD-MIB/igmpCacheTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IGMPSTDMIB.IgmpCacheTable.IgmpCacheEntry, ['igmpcacheaddress', 'igmpcacheifindex', 'igmpcacheself', 'igmpcachelastreporter', 'igmpcacheuptime', 'igmpcacheexpirytime', 'igmpcachestatus', 'igmpcacheversion1hosttimer'], name, value)

    def clone_ptr(self):
        self._top_entity = IGMPSTDMIB()
        return self._top_entity

