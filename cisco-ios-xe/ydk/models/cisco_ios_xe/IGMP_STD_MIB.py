""" IGMP_STD_MIB 

The MIB module for IGMP Management.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError




class IgmpStdMib(object):
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
        self.igmpcachetable = IgmpStdMib.Igmpcachetable()
        self.igmpcachetable.parent = self
        self.igmpinterfacetable = IgmpStdMib.Igmpinterfacetable()
        self.igmpinterfacetable.parent = self


    class Igmpinterfacetable(object):
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
            self.parent = None
            self.igmpinterfaceentry = YList()
            self.igmpinterfaceentry.parent = self
            self.igmpinterfaceentry.name = 'igmpinterfaceentry'


        class Igmpinterfaceentry(object):
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
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
                self.parent = None
                self.igmpinterfaceifindex = None
                self.igmpinterfacegroups = None
                self.igmpinterfacejoins = None
                self.igmpinterfacelastmembqueryintvl = None
                self.igmpinterfaceproxyifindex = None
                self.igmpinterfacequerier = None
                self.igmpinterfacequerierexpirytime = None
                self.igmpinterfacequerieruptime = None
                self.igmpinterfacequeryinterval = None
                self.igmpinterfacequerymaxresponsetime = None
                self.igmpinterfacerobustness = None
                self.igmpinterfacestatus = None
                self.igmpinterfaceversion = None
                self.igmpinterfaceversion1queriertimer = None
                self.igmpinterfacewrongversionqueries = None

            @property
            def _common_path(self):
                if self.igmpinterfaceifindex is None:
                    raise YPYModelError('Key property igmpinterfaceifindex is None')

                return '/IGMP-STD-MIB:IGMP-STD-MIB/IGMP-STD-MIB:igmpInterfaceTable/IGMP-STD-MIB:igmpInterfaceEntry[IGMP-STD-MIB:igmpInterfaceIfIndex = ' + str(self.igmpinterfaceifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.igmpinterfaceifindex is not None:
                    return True

                if self.igmpinterfacegroups is not None:
                    return True

                if self.igmpinterfacejoins is not None:
                    return True

                if self.igmpinterfacelastmembqueryintvl is not None:
                    return True

                if self.igmpinterfaceproxyifindex is not None:
                    return True

                if self.igmpinterfacequerier is not None:
                    return True

                if self.igmpinterfacequerierexpirytime is not None:
                    return True

                if self.igmpinterfacequerieruptime is not None:
                    return True

                if self.igmpinterfacequeryinterval is not None:
                    return True

                if self.igmpinterfacequerymaxresponsetime is not None:
                    return True

                if self.igmpinterfacerobustness is not None:
                    return True

                if self.igmpinterfacestatus is not None:
                    return True

                if self.igmpinterfaceversion is not None:
                    return True

                if self.igmpinterfaceversion1queriertimer is not None:
                    return True

                if self.igmpinterfacewrongversionqueries is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IGMP_STD_MIB as meta
                return meta._meta_table['IgmpStdMib.Igmpinterfacetable.Igmpinterfaceentry']['meta_info']

        @property
        def _common_path(self):

            return '/IGMP-STD-MIB:IGMP-STD-MIB/IGMP-STD-MIB:igmpInterfaceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.igmpinterfaceentry is not None:
                for child_ref in self.igmpinterfaceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IGMP_STD_MIB as meta
            return meta._meta_table['IgmpStdMib.Igmpinterfacetable']['meta_info']


    class Igmpcachetable(object):
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
            self.parent = None
            self.igmpcacheentry = YList()
            self.igmpcacheentry.parent = self
            self.igmpcacheentry.name = 'igmpcacheentry'


        class Igmpcacheentry(object):
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
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
                self.parent = None
                self.igmpcacheaddress = None
                self.igmpcacheifindex = None
                self.igmpcacheexpirytime = None
                self.igmpcachelastreporter = None
                self.igmpcacheself = None
                self.igmpcachestatus = None
                self.igmpcacheuptime = None
                self.igmpcacheversion1hosttimer = None

            @property
            def _common_path(self):
                if self.igmpcacheaddress is None:
                    raise YPYModelError('Key property igmpcacheaddress is None')
                if self.igmpcacheifindex is None:
                    raise YPYModelError('Key property igmpcacheifindex is None')

                return '/IGMP-STD-MIB:IGMP-STD-MIB/IGMP-STD-MIB:igmpCacheTable/IGMP-STD-MIB:igmpCacheEntry[IGMP-STD-MIB:igmpCacheAddress = ' + str(self.igmpcacheaddress) + '][IGMP-STD-MIB:igmpCacheIfIndex = ' + str(self.igmpcacheifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.igmpcacheaddress is not None:
                    return True

                if self.igmpcacheifindex is not None:
                    return True

                if self.igmpcacheexpirytime is not None:
                    return True

                if self.igmpcachelastreporter is not None:
                    return True

                if self.igmpcacheself is not None:
                    return True

                if self.igmpcachestatus is not None:
                    return True

                if self.igmpcacheuptime is not None:
                    return True

                if self.igmpcacheversion1hosttimer is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IGMP_STD_MIB as meta
                return meta._meta_table['IgmpStdMib.Igmpcachetable.Igmpcacheentry']['meta_info']

        @property
        def _common_path(self):

            return '/IGMP-STD-MIB:IGMP-STD-MIB/IGMP-STD-MIB:igmpCacheTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.igmpcacheentry is not None:
                for child_ref in self.igmpcacheentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IGMP_STD_MIB as meta
            return meta._meta_table['IgmpStdMib.Igmpcachetable']['meta_info']

    @property
    def _common_path(self):

        return '/IGMP-STD-MIB:IGMP-STD-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.igmpcachetable is not None and self.igmpcachetable._has_data():
            return True

        if self.igmpinterfacetable is not None and self.igmpinterfacetable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _IGMP_STD_MIB as meta
        return meta._meta_table['IgmpStdMib']['meta_info']


