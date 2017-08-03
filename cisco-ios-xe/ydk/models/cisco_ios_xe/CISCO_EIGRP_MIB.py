""" CISCO_EIGRP_MIB 

Enhanced Interior Gateway Protocol (EIGRP) is a Cisco
proprietary distance vector routing protocol.   It is based on
the Diffusing Update Algorithm (DUAL), which is a method of
finding loop\-free paths through a network.   Directly
connected routers running EIGRP form neighbor adjacencies in
order to propagate best\-path and alternate\-path routing
information for configured and learned routes.

The tables defined within the MIB are closely aligned with how
the router command\-line interface for EIGRP displays
information on EIGRP configurations, i.e., the topology table
contains objects associated with the EIGRP topology commands,
and the peer table contains objects associated withe EIGRP
neighbor commands, etc.

There are five main tables within this mib\:

   EIGRP VPN table
      Contains information regarding which virtual private
      networks (VPN) are configured with EIGRP.

   EIGRP traffic statistics table
      Contains counter & statistcs regarding specific types of
      EIGRP packets sent and related collective information
      per VPN and per autonomous system (AS).

   EIGRP topology table
      Contains information regarding EIGRP routes received in
      updates and originated locally.   EIGRP sends and
      receives routing updates from adjacent routers running
      EIGRP with which it formed a peer relationship.

   EIGRP peer (neighbor) table
      Contains information about neighbor EIGRP routers with
      which peer adjacencies have been established.   EIGRP
      uses a Hello protocol to form neighbor relationships
      with directly connected routers also running EIGRP.

   EIGRP interfaces table
      Contains information and statistics on each of the
      interfaces on the router over which EIGRP has been
      configured to run.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoEigrpMib(Entity):
    """
    
    
    .. attribute:: ceigrpinterfacetable
    
    	The table of interfaces over which EIGRP is running, and their associated statistics.   This table is independent of whether any peer adjacencies have been formed over the interfaces or not.   Interfaces running EIGRP are determined by whether their assigned IP addresses fall within configured EIGRP network statements
    	**type**\:   :py:class:`Ceigrpinterfacetable <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrpinterfacetable>`
    
    .. attribute:: ceigrppeertable
    
    	The table of established EIGRP peers (neighbors) in the selected autonomous system.   Peers are indexed by their unique internal handle id, as well as the AS number and VPN id.   The peer entry is removed from the table if the peer is declared down
    	**type**\:   :py:class:`Ceigrppeertable <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrppeertable>`
    
    .. attribute:: ceigrptopotable
    
    	The table of EIGRP routes and their associated attributes for an Autonomous System (AS) configured in a VPN is called a topology table.  All route entries in the topology table will be indexed by IP network type, IP network number and network mask (prefix) size
    	**type**\:   :py:class:`Ceigrptopotable <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrptopotable>`
    
    .. attribute:: ceigrptraffstatstable
    
    	Table of EIGRP traffic statistics and information associated with all EIGRP autonomous systems
    	**type**\:   :py:class:`Ceigrptraffstatstable <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrptraffstatstable>`
    
    .. attribute:: ceigrpvpntable
    
    	This table contains information on those VPN's configured to run EIGRP.  The VPN creation on a router is independent of the routing protocol to be used over it.   A VPN is given a name and has a dedicated routing table associated with it.  This routing table is identified internally by a unique integer value
    	**type**\:   :py:class:`Ceigrpvpntable <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrpvpntable>`
    
    

    """

    _prefix = 'CISCO-EIGRP-MIB'
    _revision = '2004-11-16'

    def __init__(self):
        super(CiscoEigrpMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-EIGRP-MIB"
        self.yang_parent_name = "CISCO-EIGRP-MIB"

        self.ceigrpinterfacetable = CiscoEigrpMib.Ceigrpinterfacetable()
        self.ceigrpinterfacetable.parent = self
        self._children_name_map["ceigrpinterfacetable"] = "cEigrpInterfaceTable"
        self._children_yang_names.add("cEigrpInterfaceTable")

        self.ceigrppeertable = CiscoEigrpMib.Ceigrppeertable()
        self.ceigrppeertable.parent = self
        self._children_name_map["ceigrppeertable"] = "cEigrpPeerTable"
        self._children_yang_names.add("cEigrpPeerTable")

        self.ceigrptopotable = CiscoEigrpMib.Ceigrptopotable()
        self.ceigrptopotable.parent = self
        self._children_name_map["ceigrptopotable"] = "cEigrpTopoTable"
        self._children_yang_names.add("cEigrpTopoTable")

        self.ceigrptraffstatstable = CiscoEigrpMib.Ceigrptraffstatstable()
        self.ceigrptraffstatstable.parent = self
        self._children_name_map["ceigrptraffstatstable"] = "cEigrpTraffStatsTable"
        self._children_yang_names.add("cEigrpTraffStatsTable")

        self.ceigrpvpntable = CiscoEigrpMib.Ceigrpvpntable()
        self.ceigrpvpntable.parent = self
        self._children_name_map["ceigrpvpntable"] = "cEigrpVpnTable"
        self._children_yang_names.add("cEigrpVpnTable")


    class Ceigrpvpntable(Entity):
        """
        This table contains information on those VPN's configured
        to run EIGRP.  The VPN creation on a router is independent
        of the routing protocol to be used over it.   A VPN is
        given a name and has a dedicated routing table associated
        with it.  This routing table is identified internally
        by a unique integer value.
        
        .. attribute:: ceigrpvpnentry
        
        	Information relating to a single VPN which is configured to run EIGRP
        	**type**\: list of    :py:class:`Ceigrpvpnentry <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry>`
        
        

        """

        _prefix = 'CISCO-EIGRP-MIB'
        _revision = '2004-11-16'

        def __init__(self):
            super(CiscoEigrpMib.Ceigrpvpntable, self).__init__()

            self.yang_name = "cEigrpVpnTable"
            self.yang_parent_name = "CISCO-EIGRP-MIB"

            self.ceigrpvpnentry = YList(self)

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
                        super(CiscoEigrpMib.Ceigrpvpntable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEigrpMib.Ceigrpvpntable, self).__setattr__(name, value)


        class Ceigrpvpnentry(Entity):
            """
            Information relating to a single VPN which is configured
            to run EIGRP.
            
            .. attribute:: ceigrpvpnid  <key>
            
            	The unique VPN identifier.  This is a unique integer relative to all other VPN's defined on the router.  It also identifies internally the routing table instance
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpvpnname
            
            	The name given to the VPN
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-EIGRP-MIB'
            _revision = '2004-11-16'

            def __init__(self):
                super(CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry, self).__init__()

                self.yang_name = "cEigrpVpnEntry"
                self.yang_parent_name = "cEigrpVpnTable"

                self.ceigrpvpnid = YLeaf(YType.uint32, "cEigrpVpnId")

                self.ceigrpvpnname = YLeaf(YType.str, "cEigrpVpnName")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ceigrpvpnid",
                                "ceigrpvpnname") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ceigrpvpnid.is_set or
                    self.ceigrpvpnname.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ceigrpvpnid.yfilter != YFilter.not_set or
                    self.ceigrpvpnname.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cEigrpVpnEntry" + "[cEigrpVpnId='" + self.ceigrpvpnid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/cEigrpVpnTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ceigrpvpnid.is_set or self.ceigrpvpnid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpvpnid.get_name_leafdata())
                if (self.ceigrpvpnname.is_set or self.ceigrpvpnname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpvpnname.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cEigrpVpnId" or name == "cEigrpVpnName"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cEigrpVpnId"):
                    self.ceigrpvpnid = value
                    self.ceigrpvpnid.value_namespace = name_space
                    self.ceigrpvpnid.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpVpnName"):
                    self.ceigrpvpnname = value
                    self.ceigrpvpnname.value_namespace = name_space
                    self.ceigrpvpnname.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ceigrpvpnentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ceigrpvpnentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cEigrpVpnTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cEigrpVpnEntry"):
                for c in self.ceigrpvpnentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ceigrpvpnentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cEigrpVpnEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ceigrptraffstatstable(Entity):
        """
        Table of EIGRP traffic statistics and information
        associated with all EIGRP autonomous systems.
        
        .. attribute:: ceigrptraffstatsentry
        
        	The set of statistics and information for a single EIGRP Autonomous System
        	**type**\: list of    :py:class:`Ceigrptraffstatsentry <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrptraffstatstable.Ceigrptraffstatsentry>`
        
        

        """

        _prefix = 'CISCO-EIGRP-MIB'
        _revision = '2004-11-16'

        def __init__(self):
            super(CiscoEigrpMib.Ceigrptraffstatstable, self).__init__()

            self.yang_name = "cEigrpTraffStatsTable"
            self.yang_parent_name = "CISCO-EIGRP-MIB"

            self.ceigrptraffstatsentry = YList(self)

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
                        super(CiscoEigrpMib.Ceigrptraffstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEigrpMib.Ceigrptraffstatstable, self).__setattr__(name, value)


        class Ceigrptraffstatsentry(Entity):
            """
            The set of statistics and information for a single EIGRP
            Autonomous System.
            
            .. attribute:: ceigrpvpnid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpvpnid <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry>`
            
            .. attribute:: ceigrpasnumber  <key>
            
            	The Autonomous System number which is unique integer per VPN
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpacksrcvd
            
            	The total number packet acknowledgements that have been received from all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpackssent
            
            	The total number packet acknowledgements that have been sent to all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpasrouterid
            
            	The router\-id configured or automatically selected for the EIGRP AS.   Each EIGRP routing process has a unique router\-id selected from each autonomous system configured. The format is governed by object cEigrpAsRouterIdType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ceigrpasrouteridtype
            
            	The format of the router\-id configured or automatically selected for the EIGRP AS
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ceigrpheadserial
            
            	Routes in a topology table for an AS are assigned serial numbers and are sequenced internally as they are inserted and deleted.   The serial number of the first route in that internal sequence is called the head serial number. Each AS has its own topology table, and its own serial number space, each of which begins with the value 1. A serial number of zero implies that there are no routes in the topology
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceigrphellosrcvd
            
            	The total number Hello packets that have been received from all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrphellossent
            
            	The total number Hello packets that have been sent to all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpinputqdrops
            
            	The number of EIGRP packets dropped from the input queue due to it being full within the AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpinputqhighmark
            
            	The highest number of EIGRP packets in the input queue waiting to be processed internally addressed to this AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpnbrcount
            
            	The total number of live EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured in the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpnextserial
            
            	The serial number that would be assigned to the next new or changed route in the topology table for the AS
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceigrpqueriesrcvd
            
            	The total number alternate route query packets that have been received from all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpqueriessent
            
            	The total number alternate route query packets that have been sent to all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrprepliesrcvd
            
            	The total number query reply packets that have been received from all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrprepliessent
            
            	The total number query reply packets that have been sent to all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpsiaqueriesrcvd
            
            	The total number of Stuck\-In\-Active (SIA) query packets received from all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpsiaqueriessent
            
            	The total number of Stuck\-In\-Active (SIA) query packets sent to all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrptoporoutes
            
            	The total number of EIGRP derived routes currently existing in the topology table for the AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpupdatesrcvd
            
            	The total number routing update packets that have been received from all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpupdatessent
            
            	The total number routing update packets that have been sent to all EIGRP neighbors formed on all interfaces whose IP addresses fall under networks configured for the EIGRP AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpxmitdummies
            
            	A dummy is a temporary internal entity used as a place holder in the topology table for an AS. They are not transmitted in routing updates.  This is the total number currently in existence associated with the AS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpxmitpendreplies
            
            	When alternate route query packets are sent to adjacent EIGRP peers in an AS, replies are expected.   This object is the total number of outstanding replies expected to queries that have been sent to peers in the current AS. It remains at zero most of the time until an EIGRP route becomes active
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-EIGRP-MIB'
            _revision = '2004-11-16'

            def __init__(self):
                super(CiscoEigrpMib.Ceigrptraffstatstable.Ceigrptraffstatsentry, self).__init__()

                self.yang_name = "cEigrpTraffStatsEntry"
                self.yang_parent_name = "cEigrpTraffStatsTable"

                self.ceigrpvpnid = YLeaf(YType.str, "cEigrpVpnId")

                self.ceigrpasnumber = YLeaf(YType.uint32, "cEigrpAsNumber")

                self.ceigrpacksrcvd = YLeaf(YType.uint32, "cEigrpAcksRcvd")

                self.ceigrpackssent = YLeaf(YType.uint32, "cEigrpAcksSent")

                self.ceigrpasrouterid = YLeaf(YType.str, "cEigrpAsRouterId")

                self.ceigrpasrouteridtype = YLeaf(YType.enumeration, "cEigrpAsRouterIdType")

                self.ceigrpheadserial = YLeaf(YType.uint64, "cEigrpHeadSerial")

                self.ceigrphellosrcvd = YLeaf(YType.uint32, "cEigrpHellosRcvd")

                self.ceigrphellossent = YLeaf(YType.uint32, "cEigrpHellosSent")

                self.ceigrpinputqdrops = YLeaf(YType.uint32, "cEigrpInputQDrops")

                self.ceigrpinputqhighmark = YLeaf(YType.uint32, "cEigrpInputQHighMark")

                self.ceigrpnbrcount = YLeaf(YType.uint32, "cEigrpNbrCount")

                self.ceigrpnextserial = YLeaf(YType.uint64, "cEigrpNextSerial")

                self.ceigrpqueriesrcvd = YLeaf(YType.uint32, "cEigrpQueriesRcvd")

                self.ceigrpqueriessent = YLeaf(YType.uint32, "cEigrpQueriesSent")

                self.ceigrprepliesrcvd = YLeaf(YType.uint32, "cEigrpRepliesRcvd")

                self.ceigrprepliessent = YLeaf(YType.uint32, "cEigrpRepliesSent")

                self.ceigrpsiaqueriesrcvd = YLeaf(YType.uint32, "cEigrpSiaQueriesRcvd")

                self.ceigrpsiaqueriessent = YLeaf(YType.uint32, "cEigrpSiaQueriesSent")

                self.ceigrptoporoutes = YLeaf(YType.uint32, "cEigrpTopoRoutes")

                self.ceigrpupdatesrcvd = YLeaf(YType.uint32, "cEigrpUpdatesRcvd")

                self.ceigrpupdatessent = YLeaf(YType.uint32, "cEigrpUpdatesSent")

                self.ceigrpxmitdummies = YLeaf(YType.uint32, "cEigrpXmitDummies")

                self.ceigrpxmitpendreplies = YLeaf(YType.uint32, "cEigrpXmitPendReplies")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ceigrpvpnid",
                                "ceigrpasnumber",
                                "ceigrpacksrcvd",
                                "ceigrpackssent",
                                "ceigrpasrouterid",
                                "ceigrpasrouteridtype",
                                "ceigrpheadserial",
                                "ceigrphellosrcvd",
                                "ceigrphellossent",
                                "ceigrpinputqdrops",
                                "ceigrpinputqhighmark",
                                "ceigrpnbrcount",
                                "ceigrpnextserial",
                                "ceigrpqueriesrcvd",
                                "ceigrpqueriessent",
                                "ceigrprepliesrcvd",
                                "ceigrprepliessent",
                                "ceigrpsiaqueriesrcvd",
                                "ceigrpsiaqueriessent",
                                "ceigrptoporoutes",
                                "ceigrpupdatesrcvd",
                                "ceigrpupdatessent",
                                "ceigrpxmitdummies",
                                "ceigrpxmitpendreplies") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEigrpMib.Ceigrptraffstatstable.Ceigrptraffstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEigrpMib.Ceigrptraffstatstable.Ceigrptraffstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ceigrpvpnid.is_set or
                    self.ceigrpasnumber.is_set or
                    self.ceigrpacksrcvd.is_set or
                    self.ceigrpackssent.is_set or
                    self.ceigrpasrouterid.is_set or
                    self.ceigrpasrouteridtype.is_set or
                    self.ceigrpheadserial.is_set or
                    self.ceigrphellosrcvd.is_set or
                    self.ceigrphellossent.is_set or
                    self.ceigrpinputqdrops.is_set or
                    self.ceigrpinputqhighmark.is_set or
                    self.ceigrpnbrcount.is_set or
                    self.ceigrpnextserial.is_set or
                    self.ceigrpqueriesrcvd.is_set or
                    self.ceigrpqueriessent.is_set or
                    self.ceigrprepliesrcvd.is_set or
                    self.ceigrprepliessent.is_set or
                    self.ceigrpsiaqueriesrcvd.is_set or
                    self.ceigrpsiaqueriessent.is_set or
                    self.ceigrptoporoutes.is_set or
                    self.ceigrpupdatesrcvd.is_set or
                    self.ceigrpupdatessent.is_set or
                    self.ceigrpxmitdummies.is_set or
                    self.ceigrpxmitpendreplies.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ceigrpvpnid.yfilter != YFilter.not_set or
                    self.ceigrpasnumber.yfilter != YFilter.not_set or
                    self.ceigrpacksrcvd.yfilter != YFilter.not_set or
                    self.ceigrpackssent.yfilter != YFilter.not_set or
                    self.ceigrpasrouterid.yfilter != YFilter.not_set or
                    self.ceigrpasrouteridtype.yfilter != YFilter.not_set or
                    self.ceigrpheadserial.yfilter != YFilter.not_set or
                    self.ceigrphellosrcvd.yfilter != YFilter.not_set or
                    self.ceigrphellossent.yfilter != YFilter.not_set or
                    self.ceigrpinputqdrops.yfilter != YFilter.not_set or
                    self.ceigrpinputqhighmark.yfilter != YFilter.not_set or
                    self.ceigrpnbrcount.yfilter != YFilter.not_set or
                    self.ceigrpnextserial.yfilter != YFilter.not_set or
                    self.ceigrpqueriesrcvd.yfilter != YFilter.not_set or
                    self.ceigrpqueriessent.yfilter != YFilter.not_set or
                    self.ceigrprepliesrcvd.yfilter != YFilter.not_set or
                    self.ceigrprepliessent.yfilter != YFilter.not_set or
                    self.ceigrpsiaqueriesrcvd.yfilter != YFilter.not_set or
                    self.ceigrpsiaqueriessent.yfilter != YFilter.not_set or
                    self.ceigrptoporoutes.yfilter != YFilter.not_set or
                    self.ceigrpupdatesrcvd.yfilter != YFilter.not_set or
                    self.ceigrpupdatessent.yfilter != YFilter.not_set or
                    self.ceigrpxmitdummies.yfilter != YFilter.not_set or
                    self.ceigrpxmitpendreplies.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cEigrpTraffStatsEntry" + "[cEigrpVpnId='" + self.ceigrpvpnid.get() + "']" + "[cEigrpAsNumber='" + self.ceigrpasnumber.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/cEigrpTraffStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ceigrpvpnid.is_set or self.ceigrpvpnid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpvpnid.get_name_leafdata())
                if (self.ceigrpasnumber.is_set or self.ceigrpasnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpasnumber.get_name_leafdata())
                if (self.ceigrpacksrcvd.is_set or self.ceigrpacksrcvd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpacksrcvd.get_name_leafdata())
                if (self.ceigrpackssent.is_set or self.ceigrpackssent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpackssent.get_name_leafdata())
                if (self.ceigrpasrouterid.is_set or self.ceigrpasrouterid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpasrouterid.get_name_leafdata())
                if (self.ceigrpasrouteridtype.is_set or self.ceigrpasrouteridtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpasrouteridtype.get_name_leafdata())
                if (self.ceigrpheadserial.is_set or self.ceigrpheadserial.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpheadserial.get_name_leafdata())
                if (self.ceigrphellosrcvd.is_set or self.ceigrphellosrcvd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrphellosrcvd.get_name_leafdata())
                if (self.ceigrphellossent.is_set or self.ceigrphellossent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrphellossent.get_name_leafdata())
                if (self.ceigrpinputqdrops.is_set or self.ceigrpinputqdrops.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpinputqdrops.get_name_leafdata())
                if (self.ceigrpinputqhighmark.is_set or self.ceigrpinputqhighmark.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpinputqhighmark.get_name_leafdata())
                if (self.ceigrpnbrcount.is_set or self.ceigrpnbrcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpnbrcount.get_name_leafdata())
                if (self.ceigrpnextserial.is_set or self.ceigrpnextserial.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpnextserial.get_name_leafdata())
                if (self.ceigrpqueriesrcvd.is_set or self.ceigrpqueriesrcvd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpqueriesrcvd.get_name_leafdata())
                if (self.ceigrpqueriessent.is_set or self.ceigrpqueriessent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpqueriessent.get_name_leafdata())
                if (self.ceigrprepliesrcvd.is_set or self.ceigrprepliesrcvd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrprepliesrcvd.get_name_leafdata())
                if (self.ceigrprepliessent.is_set or self.ceigrprepliessent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrprepliessent.get_name_leafdata())
                if (self.ceigrpsiaqueriesrcvd.is_set or self.ceigrpsiaqueriesrcvd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpsiaqueriesrcvd.get_name_leafdata())
                if (self.ceigrpsiaqueriessent.is_set or self.ceigrpsiaqueriessent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpsiaqueriessent.get_name_leafdata())
                if (self.ceigrptoporoutes.is_set or self.ceigrptoporoutes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrptoporoutes.get_name_leafdata())
                if (self.ceigrpupdatesrcvd.is_set or self.ceigrpupdatesrcvd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpupdatesrcvd.get_name_leafdata())
                if (self.ceigrpupdatessent.is_set or self.ceigrpupdatessent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpupdatessent.get_name_leafdata())
                if (self.ceigrpxmitdummies.is_set or self.ceigrpxmitdummies.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpxmitdummies.get_name_leafdata())
                if (self.ceigrpxmitpendreplies.is_set or self.ceigrpxmitpendreplies.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpxmitpendreplies.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cEigrpVpnId" or name == "cEigrpAsNumber" or name == "cEigrpAcksRcvd" or name == "cEigrpAcksSent" or name == "cEigrpAsRouterId" or name == "cEigrpAsRouterIdType" or name == "cEigrpHeadSerial" or name == "cEigrpHellosRcvd" or name == "cEigrpHellosSent" or name == "cEigrpInputQDrops" or name == "cEigrpInputQHighMark" or name == "cEigrpNbrCount" or name == "cEigrpNextSerial" or name == "cEigrpQueriesRcvd" or name == "cEigrpQueriesSent" or name == "cEigrpRepliesRcvd" or name == "cEigrpRepliesSent" or name == "cEigrpSiaQueriesRcvd" or name == "cEigrpSiaQueriesSent" or name == "cEigrpTopoRoutes" or name == "cEigrpUpdatesRcvd" or name == "cEigrpUpdatesSent" or name == "cEigrpXmitDummies" or name == "cEigrpXmitPendReplies"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cEigrpVpnId"):
                    self.ceigrpvpnid = value
                    self.ceigrpvpnid.value_namespace = name_space
                    self.ceigrpvpnid.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpAsNumber"):
                    self.ceigrpasnumber = value
                    self.ceigrpasnumber.value_namespace = name_space
                    self.ceigrpasnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpAcksRcvd"):
                    self.ceigrpacksrcvd = value
                    self.ceigrpacksrcvd.value_namespace = name_space
                    self.ceigrpacksrcvd.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpAcksSent"):
                    self.ceigrpackssent = value
                    self.ceigrpackssent.value_namespace = name_space
                    self.ceigrpackssent.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpAsRouterId"):
                    self.ceigrpasrouterid = value
                    self.ceigrpasrouterid.value_namespace = name_space
                    self.ceigrpasrouterid.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpAsRouterIdType"):
                    self.ceigrpasrouteridtype = value
                    self.ceigrpasrouteridtype.value_namespace = name_space
                    self.ceigrpasrouteridtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpHeadSerial"):
                    self.ceigrpheadserial = value
                    self.ceigrpheadserial.value_namespace = name_space
                    self.ceigrpheadserial.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpHellosRcvd"):
                    self.ceigrphellosrcvd = value
                    self.ceigrphellosrcvd.value_namespace = name_space
                    self.ceigrphellosrcvd.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpHellosSent"):
                    self.ceigrphellossent = value
                    self.ceigrphellossent.value_namespace = name_space
                    self.ceigrphellossent.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpInputQDrops"):
                    self.ceigrpinputqdrops = value
                    self.ceigrpinputqdrops.value_namespace = name_space
                    self.ceigrpinputqdrops.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpInputQHighMark"):
                    self.ceigrpinputqhighmark = value
                    self.ceigrpinputqhighmark.value_namespace = name_space
                    self.ceigrpinputqhighmark.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpNbrCount"):
                    self.ceigrpnbrcount = value
                    self.ceigrpnbrcount.value_namespace = name_space
                    self.ceigrpnbrcount.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpNextSerial"):
                    self.ceigrpnextserial = value
                    self.ceigrpnextserial.value_namespace = name_space
                    self.ceigrpnextserial.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpQueriesRcvd"):
                    self.ceigrpqueriesrcvd = value
                    self.ceigrpqueriesrcvd.value_namespace = name_space
                    self.ceigrpqueriesrcvd.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpQueriesSent"):
                    self.ceigrpqueriessent = value
                    self.ceigrpqueriessent.value_namespace = name_space
                    self.ceigrpqueriessent.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpRepliesRcvd"):
                    self.ceigrprepliesrcvd = value
                    self.ceigrprepliesrcvd.value_namespace = name_space
                    self.ceigrprepliesrcvd.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpRepliesSent"):
                    self.ceigrprepliessent = value
                    self.ceigrprepliessent.value_namespace = name_space
                    self.ceigrprepliessent.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpSiaQueriesRcvd"):
                    self.ceigrpsiaqueriesrcvd = value
                    self.ceigrpsiaqueriesrcvd.value_namespace = name_space
                    self.ceigrpsiaqueriesrcvd.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpSiaQueriesSent"):
                    self.ceigrpsiaqueriessent = value
                    self.ceigrpsiaqueriessent.value_namespace = name_space
                    self.ceigrpsiaqueriessent.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpTopoRoutes"):
                    self.ceigrptoporoutes = value
                    self.ceigrptoporoutes.value_namespace = name_space
                    self.ceigrptoporoutes.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpUpdatesRcvd"):
                    self.ceigrpupdatesrcvd = value
                    self.ceigrpupdatesrcvd.value_namespace = name_space
                    self.ceigrpupdatesrcvd.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpUpdatesSent"):
                    self.ceigrpupdatessent = value
                    self.ceigrpupdatessent.value_namespace = name_space
                    self.ceigrpupdatessent.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpXmitDummies"):
                    self.ceigrpxmitdummies = value
                    self.ceigrpxmitdummies.value_namespace = name_space
                    self.ceigrpxmitdummies.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpXmitPendReplies"):
                    self.ceigrpxmitpendreplies = value
                    self.ceigrpxmitpendreplies.value_namespace = name_space
                    self.ceigrpxmitpendreplies.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ceigrptraffstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ceigrptraffstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cEigrpTraffStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cEigrpTraffStatsEntry"):
                for c in self.ceigrptraffstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEigrpMib.Ceigrptraffstatstable.Ceigrptraffstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ceigrptraffstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cEigrpTraffStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ceigrptopotable(Entity):
        """
        The table of EIGRP routes and their associated
        attributes for an Autonomous System (AS) configured
        in a VPN is called a topology table.  All route entries in
        the topology table will be indexed by IP network type,
        IP network number and network mask (prefix) size.
        
        .. attribute:: ceigrptopoentry
        
        	The entry for a single EIGRP topology table in the given AS
        	**type**\: list of    :py:class:`Ceigrptopoentry <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrptopotable.Ceigrptopoentry>`
        
        

        """

        _prefix = 'CISCO-EIGRP-MIB'
        _revision = '2004-11-16'

        def __init__(self):
            super(CiscoEigrpMib.Ceigrptopotable, self).__init__()

            self.yang_name = "cEigrpTopoTable"
            self.yang_parent_name = "CISCO-EIGRP-MIB"

            self.ceigrptopoentry = YList(self)

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
                        super(CiscoEigrpMib.Ceigrptopotable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEigrpMib.Ceigrptopotable, self).__setattr__(name, value)


        class Ceigrptopoentry(Entity):
            """
            The entry for a single EIGRP topology table in the given
            AS.
            
            .. attribute:: ceigrpvpnid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpvpnid <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry>`
            
            .. attribute:: ceigrpasnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpasnumber <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrptraffstatstable.Ceigrptraffstatsentry>`
            
            .. attribute:: ceigrpdestnettype  <key>
            
            	The format of the destination IP network number for a single route in the topology table in the AS specified in cEigrpDestNet
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ceigrpdestnet  <key>
            
            	The destination IP network number for a single route in the topology table in the AS.  The format is governed by object cEigrpDestNetType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ceigrpdestnetprefixlen  <key>
            
            	The prefix length associated with the destination IP network address for a single route in the topology table in the AS.  The format is governed by the object cEigrpDestNetType
            	**type**\:  int
            
            	**range:** 0..2040
            
            .. attribute:: ceigrpactive
            
            	A value of true(1) indicates the route to the destination network has failed and an active (query) search for an alternative path is in progress.  A value of false(2) indicates the route is stable (passive)
            	**type**\:  bool
            
            .. attribute:: ceigrpdestsuccessors
            
            	A successor is the next routing hop for a path to the destination IP network number for a single route in the topology table in the AS.  There can be several potential successors if there are multiple paths to the destination.   This is the total number of successors for a topology entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpdistance
            
            	The computed distance to the destination network entry from this router
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpfdistance
            
            	The feasibility (best) distance is the minimum distance from this router to the destination IP network in this topology entry.  The feasibility distance is used in determining the best successor for a path to the destination network
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpnexthopaddress
            
            	This is the next hop IP address for the route represented by the topology entry.   The next hop is where network traffic will be routed to in order to reach the destination network for this topology entry.  The format is governed by cEigrpNextHopAddressType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ceigrpnexthopaddresstype
            
            	The format of the next hop IP address for the route represented by the topology entry
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ceigrpnexthopinterface
            
            	The interface through which the next hop IP address is reached to send network traffic to the destination network represented by the topology entry
            	**type**\:  str
            
            .. attribute:: ceigrpreportdistance
            
            	The computed distance to the destination network in the topology entry reported to this router by the originator of this route
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrprouteoriginaddr
            
            	If the origin of the topology route entry is external to this router, then this object is the IP address of the router from which it originated.  The format  is governed by object cEigrpRouteOriginAddrType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ceigrprouteoriginaddrtype
            
            	The format of the IP address defined as the origin of this topology route entry
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ceigrprouteorigintype
            
            	This is a text string describing the internal origin of the EIGRP route represented by the topology entry
            	**type**\:  str
            
            .. attribute:: ceigrpstuckinactive
            
            	A value of true(1) indicates that that this route which is in active state (cEigrpActive = true(1)) has not received any replies to queries for alternate paths, and a second EIGRP route query, called a stuck\-in\-active query, has now been sent
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-EIGRP-MIB'
            _revision = '2004-11-16'

            def __init__(self):
                super(CiscoEigrpMib.Ceigrptopotable.Ceigrptopoentry, self).__init__()

                self.yang_name = "cEigrpTopoEntry"
                self.yang_parent_name = "cEigrpTopoTable"

                self.ceigrpvpnid = YLeaf(YType.str, "cEigrpVpnId")

                self.ceigrpasnumber = YLeaf(YType.str, "cEigrpAsNumber")

                self.ceigrpdestnettype = YLeaf(YType.enumeration, "cEigrpDestNetType")

                self.ceigrpdestnet = YLeaf(YType.str, "cEigrpDestNet")

                self.ceigrpdestnetprefixlen = YLeaf(YType.uint32, "cEigrpDestNetPrefixLen")

                self.ceigrpactive = YLeaf(YType.boolean, "cEigrpActive")

                self.ceigrpdestsuccessors = YLeaf(YType.uint32, "cEigrpDestSuccessors")

                self.ceigrpdistance = YLeaf(YType.uint32, "cEigrpDistance")

                self.ceigrpfdistance = YLeaf(YType.uint32, "cEigrpFdistance")

                self.ceigrpnexthopaddress = YLeaf(YType.str, "cEigrpNextHopAddress")

                self.ceigrpnexthopaddresstype = YLeaf(YType.enumeration, "cEigrpNextHopAddressType")

                self.ceigrpnexthopinterface = YLeaf(YType.str, "cEigrpNextHopInterface")

                self.ceigrpreportdistance = YLeaf(YType.uint32, "cEigrpReportDistance")

                self.ceigrprouteoriginaddr = YLeaf(YType.str, "cEigrpRouteOriginAddr")

                self.ceigrprouteoriginaddrtype = YLeaf(YType.enumeration, "cEigrpRouteOriginAddrType")

                self.ceigrprouteorigintype = YLeaf(YType.str, "cEigrpRouteOriginType")

                self.ceigrpstuckinactive = YLeaf(YType.boolean, "cEigrpStuckInActive")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ceigrpvpnid",
                                "ceigrpasnumber",
                                "ceigrpdestnettype",
                                "ceigrpdestnet",
                                "ceigrpdestnetprefixlen",
                                "ceigrpactive",
                                "ceigrpdestsuccessors",
                                "ceigrpdistance",
                                "ceigrpfdistance",
                                "ceigrpnexthopaddress",
                                "ceigrpnexthopaddresstype",
                                "ceigrpnexthopinterface",
                                "ceigrpreportdistance",
                                "ceigrprouteoriginaddr",
                                "ceigrprouteoriginaddrtype",
                                "ceigrprouteorigintype",
                                "ceigrpstuckinactive") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEigrpMib.Ceigrptopotable.Ceigrptopoentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEigrpMib.Ceigrptopotable.Ceigrptopoentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ceigrpvpnid.is_set or
                    self.ceigrpasnumber.is_set or
                    self.ceigrpdestnettype.is_set or
                    self.ceigrpdestnet.is_set or
                    self.ceigrpdestnetprefixlen.is_set or
                    self.ceigrpactive.is_set or
                    self.ceigrpdestsuccessors.is_set or
                    self.ceigrpdistance.is_set or
                    self.ceigrpfdistance.is_set or
                    self.ceigrpnexthopaddress.is_set or
                    self.ceigrpnexthopaddresstype.is_set or
                    self.ceigrpnexthopinterface.is_set or
                    self.ceigrpreportdistance.is_set or
                    self.ceigrprouteoriginaddr.is_set or
                    self.ceigrprouteoriginaddrtype.is_set or
                    self.ceigrprouteorigintype.is_set or
                    self.ceigrpstuckinactive.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ceigrpvpnid.yfilter != YFilter.not_set or
                    self.ceigrpasnumber.yfilter != YFilter.not_set or
                    self.ceigrpdestnettype.yfilter != YFilter.not_set or
                    self.ceigrpdestnet.yfilter != YFilter.not_set or
                    self.ceigrpdestnetprefixlen.yfilter != YFilter.not_set or
                    self.ceigrpactive.yfilter != YFilter.not_set or
                    self.ceigrpdestsuccessors.yfilter != YFilter.not_set or
                    self.ceigrpdistance.yfilter != YFilter.not_set or
                    self.ceigrpfdistance.yfilter != YFilter.not_set or
                    self.ceigrpnexthopaddress.yfilter != YFilter.not_set or
                    self.ceigrpnexthopaddresstype.yfilter != YFilter.not_set or
                    self.ceigrpnexthopinterface.yfilter != YFilter.not_set or
                    self.ceigrpreportdistance.yfilter != YFilter.not_set or
                    self.ceigrprouteoriginaddr.yfilter != YFilter.not_set or
                    self.ceigrprouteoriginaddrtype.yfilter != YFilter.not_set or
                    self.ceigrprouteorigintype.yfilter != YFilter.not_set or
                    self.ceigrpstuckinactive.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cEigrpTopoEntry" + "[cEigrpVpnId='" + self.ceigrpvpnid.get() + "']" + "[cEigrpAsNumber='" + self.ceigrpasnumber.get() + "']" + "[cEigrpDestNetType='" + self.ceigrpdestnettype.get() + "']" + "[cEigrpDestNet='" + self.ceigrpdestnet.get() + "']" + "[cEigrpDestNetPrefixLen='" + self.ceigrpdestnetprefixlen.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/cEigrpTopoTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ceigrpvpnid.is_set or self.ceigrpvpnid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpvpnid.get_name_leafdata())
                if (self.ceigrpasnumber.is_set or self.ceigrpasnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpasnumber.get_name_leafdata())
                if (self.ceigrpdestnettype.is_set or self.ceigrpdestnettype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpdestnettype.get_name_leafdata())
                if (self.ceigrpdestnet.is_set or self.ceigrpdestnet.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpdestnet.get_name_leafdata())
                if (self.ceigrpdestnetprefixlen.is_set or self.ceigrpdestnetprefixlen.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpdestnetprefixlen.get_name_leafdata())
                if (self.ceigrpactive.is_set or self.ceigrpactive.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpactive.get_name_leafdata())
                if (self.ceigrpdestsuccessors.is_set or self.ceigrpdestsuccessors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpdestsuccessors.get_name_leafdata())
                if (self.ceigrpdistance.is_set or self.ceigrpdistance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpdistance.get_name_leafdata())
                if (self.ceigrpfdistance.is_set or self.ceigrpfdistance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpfdistance.get_name_leafdata())
                if (self.ceigrpnexthopaddress.is_set or self.ceigrpnexthopaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpnexthopaddress.get_name_leafdata())
                if (self.ceigrpnexthopaddresstype.is_set or self.ceigrpnexthopaddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpnexthopaddresstype.get_name_leafdata())
                if (self.ceigrpnexthopinterface.is_set or self.ceigrpnexthopinterface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpnexthopinterface.get_name_leafdata())
                if (self.ceigrpreportdistance.is_set or self.ceigrpreportdistance.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpreportdistance.get_name_leafdata())
                if (self.ceigrprouteoriginaddr.is_set or self.ceigrprouteoriginaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrprouteoriginaddr.get_name_leafdata())
                if (self.ceigrprouteoriginaddrtype.is_set or self.ceigrprouteoriginaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrprouteoriginaddrtype.get_name_leafdata())
                if (self.ceigrprouteorigintype.is_set or self.ceigrprouteorigintype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrprouteorigintype.get_name_leafdata())
                if (self.ceigrpstuckinactive.is_set or self.ceigrpstuckinactive.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpstuckinactive.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cEigrpVpnId" or name == "cEigrpAsNumber" or name == "cEigrpDestNetType" or name == "cEigrpDestNet" or name == "cEigrpDestNetPrefixLen" or name == "cEigrpActive" or name == "cEigrpDestSuccessors" or name == "cEigrpDistance" or name == "cEigrpFdistance" or name == "cEigrpNextHopAddress" or name == "cEigrpNextHopAddressType" or name == "cEigrpNextHopInterface" or name == "cEigrpReportDistance" or name == "cEigrpRouteOriginAddr" or name == "cEigrpRouteOriginAddrType" or name == "cEigrpRouteOriginType" or name == "cEigrpStuckInActive"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cEigrpVpnId"):
                    self.ceigrpvpnid = value
                    self.ceigrpvpnid.value_namespace = name_space
                    self.ceigrpvpnid.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpAsNumber"):
                    self.ceigrpasnumber = value
                    self.ceigrpasnumber.value_namespace = name_space
                    self.ceigrpasnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpDestNetType"):
                    self.ceigrpdestnettype = value
                    self.ceigrpdestnettype.value_namespace = name_space
                    self.ceigrpdestnettype.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpDestNet"):
                    self.ceigrpdestnet = value
                    self.ceigrpdestnet.value_namespace = name_space
                    self.ceigrpdestnet.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpDestNetPrefixLen"):
                    self.ceigrpdestnetprefixlen = value
                    self.ceigrpdestnetprefixlen.value_namespace = name_space
                    self.ceigrpdestnetprefixlen.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpActive"):
                    self.ceigrpactive = value
                    self.ceigrpactive.value_namespace = name_space
                    self.ceigrpactive.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpDestSuccessors"):
                    self.ceigrpdestsuccessors = value
                    self.ceigrpdestsuccessors.value_namespace = name_space
                    self.ceigrpdestsuccessors.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpDistance"):
                    self.ceigrpdistance = value
                    self.ceigrpdistance.value_namespace = name_space
                    self.ceigrpdistance.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpFdistance"):
                    self.ceigrpfdistance = value
                    self.ceigrpfdistance.value_namespace = name_space
                    self.ceigrpfdistance.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpNextHopAddress"):
                    self.ceigrpnexthopaddress = value
                    self.ceigrpnexthopaddress.value_namespace = name_space
                    self.ceigrpnexthopaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpNextHopAddressType"):
                    self.ceigrpnexthopaddresstype = value
                    self.ceigrpnexthopaddresstype.value_namespace = name_space
                    self.ceigrpnexthopaddresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpNextHopInterface"):
                    self.ceigrpnexthopinterface = value
                    self.ceigrpnexthopinterface.value_namespace = name_space
                    self.ceigrpnexthopinterface.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpReportDistance"):
                    self.ceigrpreportdistance = value
                    self.ceigrpreportdistance.value_namespace = name_space
                    self.ceigrpreportdistance.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpRouteOriginAddr"):
                    self.ceigrprouteoriginaddr = value
                    self.ceigrprouteoriginaddr.value_namespace = name_space
                    self.ceigrprouteoriginaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpRouteOriginAddrType"):
                    self.ceigrprouteoriginaddrtype = value
                    self.ceigrprouteoriginaddrtype.value_namespace = name_space
                    self.ceigrprouteoriginaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpRouteOriginType"):
                    self.ceigrprouteorigintype = value
                    self.ceigrprouteorigintype.value_namespace = name_space
                    self.ceigrprouteorigintype.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpStuckInActive"):
                    self.ceigrpstuckinactive = value
                    self.ceigrpstuckinactive.value_namespace = name_space
                    self.ceigrpstuckinactive.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ceigrptopoentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ceigrptopoentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cEigrpTopoTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cEigrpTopoEntry"):
                for c in self.ceigrptopoentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEigrpMib.Ceigrptopotable.Ceigrptopoentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ceigrptopoentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cEigrpTopoEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ceigrppeertable(Entity):
        """
        The table of established EIGRP peers (neighbors) in the
        selected autonomous system.   Peers are indexed by their
        unique internal handle id, as well as the AS number and
        VPN id.   The peer entry is removed from the table if
        the peer is declared down.
        
        .. attribute:: ceigrppeerentry
        
        	Statistics and operational parameters for a single peer in the AS
        	**type**\: list of    :py:class:`Ceigrppeerentry <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrppeertable.Ceigrppeerentry>`
        
        

        """

        _prefix = 'CISCO-EIGRP-MIB'
        _revision = '2004-11-16'

        def __init__(self):
            super(CiscoEigrpMib.Ceigrppeertable, self).__init__()

            self.yang_name = "cEigrpPeerTable"
            self.yang_parent_name = "CISCO-EIGRP-MIB"

            self.ceigrppeerentry = YList(self)

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
                        super(CiscoEigrpMib.Ceigrppeertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEigrpMib.Ceigrppeertable, self).__setattr__(name, value)


        class Ceigrppeerentry(Entity):
            """
            Statistics and operational parameters for a single peer
            in the AS.
            
            .. attribute:: ceigrpvpnid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpvpnid <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry>`
            
            .. attribute:: ceigrpasnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpasnumber <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrptraffstatstable.Ceigrptraffstatsentry>`
            
            .. attribute:: ceigrphandle  <key>
            
            	The unique internal identifier for the peer in the AS. This is a unique value among peer entries in a selected table
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpholdtime
            
            	The count\-down timer indicating how much time must pass without receiving a hello packet from this EIGRP peer before this router declares the peer down. A peer declared as down is removed from the table and is no longer visible
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: ceigrplastseq
            
            	All transmitted EIGRP packets have a sequence number assigned. This is the sequence number of the last EIGRP packet sent to this peer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrppeeraddr
            
            	The source IP address used by the peer to establish the EIGRP adjacency with this router.  The format is governed by object cEigrpPeerAddrType
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ceigrppeeraddrtype
            
            	The format of the remote source IP address used by the peer to establish the EIGRP adjacency with this router
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ceigrppeerifindex
            
            	The ifIndex of the interface on this router through which this peer can be reached
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: ceigrppktsenqueued
            
            	The number of any EIGRP packets currently enqueued waiting to be sent to this peer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpretrans
            
            	The cumulative number of retransmissions to this peer during the period that the peer adjacency has remained up
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpretries
            
            	The number of times the current unacknowledged packet has been retried, i.e. resent to this peer to be acknowledged
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrprto
            
            	The computed retransmission timeout for the peer. This value is computed over time as packets are sent to the peer and acknowledgements are received from it, and is the amount of time to wait before resending a packet from the retransmission queue to the peer when an expected acknowledgement has not been received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: ceigrpsrtt
            
            	The computed smooth round trip time for packets to and from the peer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: ceigrpuptime
            
            	The elapsed time since the EIGRP adjacency was first established with the peer
            	**type**\:  str
            
            .. attribute:: ceigrpversion
            
            	The EIGRP version information reported by the remote peer
            	**type**\:  str
            
            

            """

            _prefix = 'CISCO-EIGRP-MIB'
            _revision = '2004-11-16'

            def __init__(self):
                super(CiscoEigrpMib.Ceigrppeertable.Ceigrppeerentry, self).__init__()

                self.yang_name = "cEigrpPeerEntry"
                self.yang_parent_name = "cEigrpPeerTable"

                self.ceigrpvpnid = YLeaf(YType.str, "cEigrpVpnId")

                self.ceigrpasnumber = YLeaf(YType.str, "cEigrpAsNumber")

                self.ceigrphandle = YLeaf(YType.uint32, "cEigrpHandle")

                self.ceigrpholdtime = YLeaf(YType.uint32, "cEigrpHoldTime")

                self.ceigrplastseq = YLeaf(YType.uint32, "cEigrpLastSeq")

                self.ceigrppeeraddr = YLeaf(YType.str, "cEigrpPeerAddr")

                self.ceigrppeeraddrtype = YLeaf(YType.enumeration, "cEigrpPeerAddrType")

                self.ceigrppeerifindex = YLeaf(YType.int32, "cEigrpPeerIfIndex")

                self.ceigrppktsenqueued = YLeaf(YType.uint32, "cEigrpPktsEnqueued")

                self.ceigrpretrans = YLeaf(YType.uint32, "cEigrpRetrans")

                self.ceigrpretries = YLeaf(YType.uint32, "cEigrpRetries")

                self.ceigrprto = YLeaf(YType.uint32, "cEigrpRto")

                self.ceigrpsrtt = YLeaf(YType.uint32, "cEigrpSrtt")

                self.ceigrpuptime = YLeaf(YType.str, "cEigrpUpTime")

                self.ceigrpversion = YLeaf(YType.str, "cEigrpVersion")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ceigrpvpnid",
                                "ceigrpasnumber",
                                "ceigrphandle",
                                "ceigrpholdtime",
                                "ceigrplastseq",
                                "ceigrppeeraddr",
                                "ceigrppeeraddrtype",
                                "ceigrppeerifindex",
                                "ceigrppktsenqueued",
                                "ceigrpretrans",
                                "ceigrpretries",
                                "ceigrprto",
                                "ceigrpsrtt",
                                "ceigrpuptime",
                                "ceigrpversion") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEigrpMib.Ceigrppeertable.Ceigrppeerentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEigrpMib.Ceigrppeertable.Ceigrppeerentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ceigrpvpnid.is_set or
                    self.ceigrpasnumber.is_set or
                    self.ceigrphandle.is_set or
                    self.ceigrpholdtime.is_set or
                    self.ceigrplastseq.is_set or
                    self.ceigrppeeraddr.is_set or
                    self.ceigrppeeraddrtype.is_set or
                    self.ceigrppeerifindex.is_set or
                    self.ceigrppktsenqueued.is_set or
                    self.ceigrpretrans.is_set or
                    self.ceigrpretries.is_set or
                    self.ceigrprto.is_set or
                    self.ceigrpsrtt.is_set or
                    self.ceigrpuptime.is_set or
                    self.ceigrpversion.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ceigrpvpnid.yfilter != YFilter.not_set or
                    self.ceigrpasnumber.yfilter != YFilter.not_set or
                    self.ceigrphandle.yfilter != YFilter.not_set or
                    self.ceigrpholdtime.yfilter != YFilter.not_set or
                    self.ceigrplastseq.yfilter != YFilter.not_set or
                    self.ceigrppeeraddr.yfilter != YFilter.not_set or
                    self.ceigrppeeraddrtype.yfilter != YFilter.not_set or
                    self.ceigrppeerifindex.yfilter != YFilter.not_set or
                    self.ceigrppktsenqueued.yfilter != YFilter.not_set or
                    self.ceigrpretrans.yfilter != YFilter.not_set or
                    self.ceigrpretries.yfilter != YFilter.not_set or
                    self.ceigrprto.yfilter != YFilter.not_set or
                    self.ceigrpsrtt.yfilter != YFilter.not_set or
                    self.ceigrpuptime.yfilter != YFilter.not_set or
                    self.ceigrpversion.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cEigrpPeerEntry" + "[cEigrpVpnId='" + self.ceigrpvpnid.get() + "']" + "[cEigrpAsNumber='" + self.ceigrpasnumber.get() + "']" + "[cEigrpHandle='" + self.ceigrphandle.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/cEigrpPeerTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ceigrpvpnid.is_set or self.ceigrpvpnid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpvpnid.get_name_leafdata())
                if (self.ceigrpasnumber.is_set or self.ceigrpasnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpasnumber.get_name_leafdata())
                if (self.ceigrphandle.is_set or self.ceigrphandle.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrphandle.get_name_leafdata())
                if (self.ceigrpholdtime.is_set or self.ceigrpholdtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpholdtime.get_name_leafdata())
                if (self.ceigrplastseq.is_set or self.ceigrplastseq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrplastseq.get_name_leafdata())
                if (self.ceigrppeeraddr.is_set or self.ceigrppeeraddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrppeeraddr.get_name_leafdata())
                if (self.ceigrppeeraddrtype.is_set or self.ceigrppeeraddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrppeeraddrtype.get_name_leafdata())
                if (self.ceigrppeerifindex.is_set or self.ceigrppeerifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrppeerifindex.get_name_leafdata())
                if (self.ceigrppktsenqueued.is_set or self.ceigrppktsenqueued.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrppktsenqueued.get_name_leafdata())
                if (self.ceigrpretrans.is_set or self.ceigrpretrans.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpretrans.get_name_leafdata())
                if (self.ceigrpretries.is_set or self.ceigrpretries.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpretries.get_name_leafdata())
                if (self.ceigrprto.is_set or self.ceigrprto.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrprto.get_name_leafdata())
                if (self.ceigrpsrtt.is_set or self.ceigrpsrtt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpsrtt.get_name_leafdata())
                if (self.ceigrpuptime.is_set or self.ceigrpuptime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpuptime.get_name_leafdata())
                if (self.ceigrpversion.is_set or self.ceigrpversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpversion.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cEigrpVpnId" or name == "cEigrpAsNumber" or name == "cEigrpHandle" or name == "cEigrpHoldTime" or name == "cEigrpLastSeq" or name == "cEigrpPeerAddr" or name == "cEigrpPeerAddrType" or name == "cEigrpPeerIfIndex" or name == "cEigrpPktsEnqueued" or name == "cEigrpRetrans" or name == "cEigrpRetries" or name == "cEigrpRto" or name == "cEigrpSrtt" or name == "cEigrpUpTime" or name == "cEigrpVersion"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cEigrpVpnId"):
                    self.ceigrpvpnid = value
                    self.ceigrpvpnid.value_namespace = name_space
                    self.ceigrpvpnid.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpAsNumber"):
                    self.ceigrpasnumber = value
                    self.ceigrpasnumber.value_namespace = name_space
                    self.ceigrpasnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpHandle"):
                    self.ceigrphandle = value
                    self.ceigrphandle.value_namespace = name_space
                    self.ceigrphandle.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpHoldTime"):
                    self.ceigrpholdtime = value
                    self.ceigrpholdtime.value_namespace = name_space
                    self.ceigrpholdtime.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpLastSeq"):
                    self.ceigrplastseq = value
                    self.ceigrplastseq.value_namespace = name_space
                    self.ceigrplastseq.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpPeerAddr"):
                    self.ceigrppeeraddr = value
                    self.ceigrppeeraddr.value_namespace = name_space
                    self.ceigrppeeraddr.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpPeerAddrType"):
                    self.ceigrppeeraddrtype = value
                    self.ceigrppeeraddrtype.value_namespace = name_space
                    self.ceigrppeeraddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpPeerIfIndex"):
                    self.ceigrppeerifindex = value
                    self.ceigrppeerifindex.value_namespace = name_space
                    self.ceigrppeerifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpPktsEnqueued"):
                    self.ceigrppktsenqueued = value
                    self.ceigrppktsenqueued.value_namespace = name_space
                    self.ceigrppktsenqueued.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpRetrans"):
                    self.ceigrpretrans = value
                    self.ceigrpretrans.value_namespace = name_space
                    self.ceigrpretrans.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpRetries"):
                    self.ceigrpretries = value
                    self.ceigrpretries.value_namespace = name_space
                    self.ceigrpretries.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpRto"):
                    self.ceigrprto = value
                    self.ceigrprto.value_namespace = name_space
                    self.ceigrprto.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpSrtt"):
                    self.ceigrpsrtt = value
                    self.ceigrpsrtt.value_namespace = name_space
                    self.ceigrpsrtt.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpUpTime"):
                    self.ceigrpuptime = value
                    self.ceigrpuptime.value_namespace = name_space
                    self.ceigrpuptime.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpVersion"):
                    self.ceigrpversion = value
                    self.ceigrpversion.value_namespace = name_space
                    self.ceigrpversion.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ceigrppeerentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ceigrppeerentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cEigrpPeerTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cEigrpPeerEntry"):
                for c in self.ceigrppeerentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEigrpMib.Ceigrppeertable.Ceigrppeerentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ceigrppeerentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cEigrpPeerEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ceigrpinterfacetable(Entity):
        """
        The table of interfaces over which EIGRP is running, and
        their associated statistics.   This table is independent
        of whether any peer adjacencies have been formed over
        the interfaces or not.   Interfaces running EIGRP are
        determined by whether their assigned IP addresses fall
        within configured EIGRP network statements.
        
        .. attribute:: ceigrpinterfaceentry
        
        	Information for a single interface running EIGRP in the AS and VPN
        	**type**\: list of    :py:class:`Ceigrpinterfaceentry <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrpinterfacetable.Ceigrpinterfaceentry>`
        
        

        """

        _prefix = 'CISCO-EIGRP-MIB'
        _revision = '2004-11-16'

        def __init__(self):
            super(CiscoEigrpMib.Ceigrpinterfacetable, self).__init__()

            self.yang_name = "cEigrpInterfaceTable"
            self.yang_parent_name = "CISCO-EIGRP-MIB"

            self.ceigrpinterfaceentry = YList(self)

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
                        super(CiscoEigrpMib.Ceigrpinterfacetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEigrpMib.Ceigrpinterfacetable, self).__setattr__(name, value)


        class Ceigrpinterfaceentry(Entity):
            """
            Information for a single interface running EIGRP in the
            AS and VPN.
            
            .. attribute:: ceigrpvpnid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpvpnid <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrpvpntable.Ceigrpvpnentry>`
            
            .. attribute:: ceigrpasnumber  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`ceigrpasnumber <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrptraffstatstable.Ceigrptraffstatsentry>`
            
            .. attribute:: ifindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`ifindex <ydk.models.cisco_ios_xe.IF_MIB.IfMib.Iftable.Ifentry>`
            
            .. attribute:: ceigrpackssuppressed
            
            	The total number of individual EIGRP acknowledgement packets that have been suppressed and combined in an already enqueued outbound reliable packet on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpauthkeychain
            
            	The name of the authentication key\-chain configured on this interface.   The key\-chain is a reference to which set of secret keys are to be accessed in order to determine which secret key string to use.  The key chain name is not the secret key string password and can also be used in other routing protocols, such as RIP and ISIS
            	**type**\:  str
            
            .. attribute:: ceigrpauthmode
            
            	The EIGRP authentication mode of the interface. none  \:  no authentication enabled on the interface md5   \:  MD5 authentication enabled on the interface
            	**type**\:   :py:class:`Ceigrpauthmode <ydk.models.cisco_ios_xe.CISCO_EIGRP_MIB.CiscoEigrpMib.Ceigrpinterfacetable.Ceigrpinterfaceentry.Ceigrpauthmode>`
            
            .. attribute:: ceigrpcrpkts
            
            	The total number EIGRP Conditional\-Receive packets sent on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrphellointerval
            
            	The configured time interval between Hello packet transmissions for this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: ceigrpmcastexcepts
            
            	The total number of EIGRP multicast exception transmissions that have occurred on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpmeansrtt
            
            	The average of all the computed smooth round trip time values for a packet to and from all peers established on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: ceigrpmflowtimer
            
            	The configured multicast flow control timer value for this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: ceigrpoosrvcd
            
            	The total number of out\-of\-sequence EIGRP packets received
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrppacingreliable
            
            	The configured time interval between EIGRP packet transmissions on the interface when the reliable transport method is used
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: ceigrppacingunreliable
            
            	The configured time interval between EIGRP packet transmissions on the interface when the unreliable transport method is used
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: ceigrppeercount
            
            	The number of EIGRP adjacencies currently formed with peers reached through this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrppendingroutes
            
            	The number of queued EIGRP routing updates awaiting transmission on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpretranssent
            
            	The total number EIGRP packet retransmissions sent on the interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrprmcasts
            
            	The total number of reliable (acknowledgement required) EIGRP multicast packets sent on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrprucasts
            
            	The total number of reliable (acknowledgement required) unicast packets sent on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpumcasts
            
            	The total number of unreliable (no acknowledgement required) EIGRP multicast packets sent on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpuucasts
            
            	The total number of unreliable (no acknowledgement required) EIGRP unicast packets sent on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpxmitnextserial
            
            	The serial number of the next EIGRP packet that is to be queued for transmission on this interface
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ceigrpxmitreliableq
            
            	The number of EIGRP packets currently waiting in the reliable transport (acknowledgement\-required)  transmission queue to be sent to a peer
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ceigrpxmitunreliableq
            
            	The number EIGRP of packets currently waiting in the unreliable transport (no acknowledgement required) transmission queue
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-EIGRP-MIB'
            _revision = '2004-11-16'

            def __init__(self):
                super(CiscoEigrpMib.Ceigrpinterfacetable.Ceigrpinterfaceentry, self).__init__()

                self.yang_name = "cEigrpInterfaceEntry"
                self.yang_parent_name = "cEigrpInterfaceTable"

                self.ceigrpvpnid = YLeaf(YType.str, "cEigrpVpnId")

                self.ceigrpasnumber = YLeaf(YType.str, "cEigrpAsNumber")

                self.ifindex = YLeaf(YType.str, "ifIndex")

                self.ceigrpackssuppressed = YLeaf(YType.uint32, "cEigrpAcksSuppressed")

                self.ceigrpauthkeychain = YLeaf(YType.str, "cEigrpAuthKeyChain")

                self.ceigrpauthmode = YLeaf(YType.enumeration, "cEigrpAuthMode")

                self.ceigrpcrpkts = YLeaf(YType.uint32, "cEigrpCRpkts")

                self.ceigrphellointerval = YLeaf(YType.uint32, "cEigrpHelloInterval")

                self.ceigrpmcastexcepts = YLeaf(YType.uint32, "cEigrpMcastExcepts")

                self.ceigrpmeansrtt = YLeaf(YType.uint32, "cEigrpMeanSrtt")

                self.ceigrpmflowtimer = YLeaf(YType.uint32, "cEigrpMFlowTimer")

                self.ceigrpoosrvcd = YLeaf(YType.uint32, "cEigrpOOSrvcd")

                self.ceigrppacingreliable = YLeaf(YType.uint32, "cEigrpPacingReliable")

                self.ceigrppacingunreliable = YLeaf(YType.uint32, "cEigrpPacingUnreliable")

                self.ceigrppeercount = YLeaf(YType.uint32, "cEigrpPeerCount")

                self.ceigrppendingroutes = YLeaf(YType.uint32, "cEigrpPendingRoutes")

                self.ceigrpretranssent = YLeaf(YType.uint32, "cEigrpRetransSent")

                self.ceigrprmcasts = YLeaf(YType.uint32, "cEigrpRMcasts")

                self.ceigrprucasts = YLeaf(YType.uint32, "cEigrpRUcasts")

                self.ceigrpumcasts = YLeaf(YType.uint32, "cEigrpUMcasts")

                self.ceigrpuucasts = YLeaf(YType.uint32, "cEigrpUUcasts")

                self.ceigrpxmitnextserial = YLeaf(YType.uint64, "cEigrpXmitNextSerial")

                self.ceigrpxmitreliableq = YLeaf(YType.uint32, "cEigrpXmitReliableQ")

                self.ceigrpxmitunreliableq = YLeaf(YType.uint32, "cEigrpXmitUnreliableQ")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ceigrpvpnid",
                                "ceigrpasnumber",
                                "ifindex",
                                "ceigrpackssuppressed",
                                "ceigrpauthkeychain",
                                "ceigrpauthmode",
                                "ceigrpcrpkts",
                                "ceigrphellointerval",
                                "ceigrpmcastexcepts",
                                "ceigrpmeansrtt",
                                "ceigrpmflowtimer",
                                "ceigrpoosrvcd",
                                "ceigrppacingreliable",
                                "ceigrppacingunreliable",
                                "ceigrppeercount",
                                "ceigrppendingroutes",
                                "ceigrpretranssent",
                                "ceigrprmcasts",
                                "ceigrprucasts",
                                "ceigrpumcasts",
                                "ceigrpuucasts",
                                "ceigrpxmitnextserial",
                                "ceigrpxmitreliableq",
                                "ceigrpxmitunreliableq") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEigrpMib.Ceigrpinterfacetable.Ceigrpinterfaceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEigrpMib.Ceigrpinterfacetable.Ceigrpinterfaceentry, self).__setattr__(name, value)

            class Ceigrpauthmode(Enum):
                """
                Ceigrpauthmode

                The EIGRP authentication mode of the interface.

                none  \:  no authentication enabled on the interface

                md5   \:  MD5 authentication enabled on the interface

                .. data:: none = 1

                .. data:: md5 = 2

                """

                none = Enum.YLeaf(1, "none")

                md5 = Enum.YLeaf(2, "md5")


            def has_data(self):
                return (
                    self.ceigrpvpnid.is_set or
                    self.ceigrpasnumber.is_set or
                    self.ifindex.is_set or
                    self.ceigrpackssuppressed.is_set or
                    self.ceigrpauthkeychain.is_set or
                    self.ceigrpauthmode.is_set or
                    self.ceigrpcrpkts.is_set or
                    self.ceigrphellointerval.is_set or
                    self.ceigrpmcastexcepts.is_set or
                    self.ceigrpmeansrtt.is_set or
                    self.ceigrpmflowtimer.is_set or
                    self.ceigrpoosrvcd.is_set or
                    self.ceigrppacingreliable.is_set or
                    self.ceigrppacingunreliable.is_set or
                    self.ceigrppeercount.is_set or
                    self.ceigrppendingroutes.is_set or
                    self.ceigrpretranssent.is_set or
                    self.ceigrprmcasts.is_set or
                    self.ceigrprucasts.is_set or
                    self.ceigrpumcasts.is_set or
                    self.ceigrpuucasts.is_set or
                    self.ceigrpxmitnextserial.is_set or
                    self.ceigrpxmitreliableq.is_set or
                    self.ceigrpxmitunreliableq.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ceigrpvpnid.yfilter != YFilter.not_set or
                    self.ceigrpasnumber.yfilter != YFilter.not_set or
                    self.ifindex.yfilter != YFilter.not_set or
                    self.ceigrpackssuppressed.yfilter != YFilter.not_set or
                    self.ceigrpauthkeychain.yfilter != YFilter.not_set or
                    self.ceigrpauthmode.yfilter != YFilter.not_set or
                    self.ceigrpcrpkts.yfilter != YFilter.not_set or
                    self.ceigrphellointerval.yfilter != YFilter.not_set or
                    self.ceigrpmcastexcepts.yfilter != YFilter.not_set or
                    self.ceigrpmeansrtt.yfilter != YFilter.not_set or
                    self.ceigrpmflowtimer.yfilter != YFilter.not_set or
                    self.ceigrpoosrvcd.yfilter != YFilter.not_set or
                    self.ceigrppacingreliable.yfilter != YFilter.not_set or
                    self.ceigrppacingunreliable.yfilter != YFilter.not_set or
                    self.ceigrppeercount.yfilter != YFilter.not_set or
                    self.ceigrppendingroutes.yfilter != YFilter.not_set or
                    self.ceigrpretranssent.yfilter != YFilter.not_set or
                    self.ceigrprmcasts.yfilter != YFilter.not_set or
                    self.ceigrprucasts.yfilter != YFilter.not_set or
                    self.ceigrpumcasts.yfilter != YFilter.not_set or
                    self.ceigrpuucasts.yfilter != YFilter.not_set or
                    self.ceigrpxmitnextserial.yfilter != YFilter.not_set or
                    self.ceigrpxmitreliableq.yfilter != YFilter.not_set or
                    self.ceigrpxmitunreliableq.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cEigrpInterfaceEntry" + "[cEigrpVpnId='" + self.ceigrpvpnid.get() + "']" + "[cEigrpAsNumber='" + self.ceigrpasnumber.get() + "']" + "[ifIndex='" + self.ifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/cEigrpInterfaceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ceigrpvpnid.is_set or self.ceigrpvpnid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpvpnid.get_name_leafdata())
                if (self.ceigrpasnumber.is_set or self.ceigrpasnumber.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpasnumber.get_name_leafdata())
                if (self.ifindex.is_set or self.ifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ifindex.get_name_leafdata())
                if (self.ceigrpackssuppressed.is_set or self.ceigrpackssuppressed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpackssuppressed.get_name_leafdata())
                if (self.ceigrpauthkeychain.is_set or self.ceigrpauthkeychain.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpauthkeychain.get_name_leafdata())
                if (self.ceigrpauthmode.is_set or self.ceigrpauthmode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpauthmode.get_name_leafdata())
                if (self.ceigrpcrpkts.is_set or self.ceigrpcrpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpcrpkts.get_name_leafdata())
                if (self.ceigrphellointerval.is_set or self.ceigrphellointerval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrphellointerval.get_name_leafdata())
                if (self.ceigrpmcastexcepts.is_set or self.ceigrpmcastexcepts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpmcastexcepts.get_name_leafdata())
                if (self.ceigrpmeansrtt.is_set or self.ceigrpmeansrtt.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpmeansrtt.get_name_leafdata())
                if (self.ceigrpmflowtimer.is_set or self.ceigrpmflowtimer.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpmflowtimer.get_name_leafdata())
                if (self.ceigrpoosrvcd.is_set or self.ceigrpoosrvcd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpoosrvcd.get_name_leafdata())
                if (self.ceigrppacingreliable.is_set or self.ceigrppacingreliable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrppacingreliable.get_name_leafdata())
                if (self.ceigrppacingunreliable.is_set or self.ceigrppacingunreliable.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrppacingunreliable.get_name_leafdata())
                if (self.ceigrppeercount.is_set or self.ceigrppeercount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrppeercount.get_name_leafdata())
                if (self.ceigrppendingroutes.is_set or self.ceigrppendingroutes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrppendingroutes.get_name_leafdata())
                if (self.ceigrpretranssent.is_set or self.ceigrpretranssent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpretranssent.get_name_leafdata())
                if (self.ceigrprmcasts.is_set or self.ceigrprmcasts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrprmcasts.get_name_leafdata())
                if (self.ceigrprucasts.is_set or self.ceigrprucasts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrprucasts.get_name_leafdata())
                if (self.ceigrpumcasts.is_set or self.ceigrpumcasts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpumcasts.get_name_leafdata())
                if (self.ceigrpuucasts.is_set or self.ceigrpuucasts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpuucasts.get_name_leafdata())
                if (self.ceigrpxmitnextserial.is_set or self.ceigrpxmitnextserial.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpxmitnextserial.get_name_leafdata())
                if (self.ceigrpxmitreliableq.is_set or self.ceigrpxmitreliableq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpxmitreliableq.get_name_leafdata())
                if (self.ceigrpxmitunreliableq.is_set or self.ceigrpxmitunreliableq.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ceigrpxmitunreliableq.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cEigrpVpnId" or name == "cEigrpAsNumber" or name == "ifIndex" or name == "cEigrpAcksSuppressed" or name == "cEigrpAuthKeyChain" or name == "cEigrpAuthMode" or name == "cEigrpCRpkts" or name == "cEigrpHelloInterval" or name == "cEigrpMcastExcepts" or name == "cEigrpMeanSrtt" or name == "cEigrpMFlowTimer" or name == "cEigrpOOSrvcd" or name == "cEigrpPacingReliable" or name == "cEigrpPacingUnreliable" or name == "cEigrpPeerCount" or name == "cEigrpPendingRoutes" or name == "cEigrpRetransSent" or name == "cEigrpRMcasts" or name == "cEigrpRUcasts" or name == "cEigrpUMcasts" or name == "cEigrpUUcasts" or name == "cEigrpXmitNextSerial" or name == "cEigrpXmitReliableQ" or name == "cEigrpXmitUnreliableQ"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cEigrpVpnId"):
                    self.ceigrpvpnid = value
                    self.ceigrpvpnid.value_namespace = name_space
                    self.ceigrpvpnid.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpAsNumber"):
                    self.ceigrpasnumber = value
                    self.ceigrpasnumber.value_namespace = name_space
                    self.ceigrpasnumber.value_namespace_prefix = name_space_prefix
                if(value_path == "ifIndex"):
                    self.ifindex = value
                    self.ifindex.value_namespace = name_space
                    self.ifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpAcksSuppressed"):
                    self.ceigrpackssuppressed = value
                    self.ceigrpackssuppressed.value_namespace = name_space
                    self.ceigrpackssuppressed.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpAuthKeyChain"):
                    self.ceigrpauthkeychain = value
                    self.ceigrpauthkeychain.value_namespace = name_space
                    self.ceigrpauthkeychain.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpAuthMode"):
                    self.ceigrpauthmode = value
                    self.ceigrpauthmode.value_namespace = name_space
                    self.ceigrpauthmode.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpCRpkts"):
                    self.ceigrpcrpkts = value
                    self.ceigrpcrpkts.value_namespace = name_space
                    self.ceigrpcrpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpHelloInterval"):
                    self.ceigrphellointerval = value
                    self.ceigrphellointerval.value_namespace = name_space
                    self.ceigrphellointerval.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpMcastExcepts"):
                    self.ceigrpmcastexcepts = value
                    self.ceigrpmcastexcepts.value_namespace = name_space
                    self.ceigrpmcastexcepts.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpMeanSrtt"):
                    self.ceigrpmeansrtt = value
                    self.ceigrpmeansrtt.value_namespace = name_space
                    self.ceigrpmeansrtt.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpMFlowTimer"):
                    self.ceigrpmflowtimer = value
                    self.ceigrpmflowtimer.value_namespace = name_space
                    self.ceigrpmflowtimer.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpOOSrvcd"):
                    self.ceigrpoosrvcd = value
                    self.ceigrpoosrvcd.value_namespace = name_space
                    self.ceigrpoosrvcd.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpPacingReliable"):
                    self.ceigrppacingreliable = value
                    self.ceigrppacingreliable.value_namespace = name_space
                    self.ceigrppacingreliable.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpPacingUnreliable"):
                    self.ceigrppacingunreliable = value
                    self.ceigrppacingunreliable.value_namespace = name_space
                    self.ceigrppacingunreliable.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpPeerCount"):
                    self.ceigrppeercount = value
                    self.ceigrppeercount.value_namespace = name_space
                    self.ceigrppeercount.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpPendingRoutes"):
                    self.ceigrppendingroutes = value
                    self.ceigrppendingroutes.value_namespace = name_space
                    self.ceigrppendingroutes.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpRetransSent"):
                    self.ceigrpretranssent = value
                    self.ceigrpretranssent.value_namespace = name_space
                    self.ceigrpretranssent.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpRMcasts"):
                    self.ceigrprmcasts = value
                    self.ceigrprmcasts.value_namespace = name_space
                    self.ceigrprmcasts.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpRUcasts"):
                    self.ceigrprucasts = value
                    self.ceigrprucasts.value_namespace = name_space
                    self.ceigrprucasts.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpUMcasts"):
                    self.ceigrpumcasts = value
                    self.ceigrpumcasts.value_namespace = name_space
                    self.ceigrpumcasts.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpUUcasts"):
                    self.ceigrpuucasts = value
                    self.ceigrpuucasts.value_namespace = name_space
                    self.ceigrpuucasts.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpXmitNextSerial"):
                    self.ceigrpxmitnextserial = value
                    self.ceigrpxmitnextserial.value_namespace = name_space
                    self.ceigrpxmitnextserial.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpXmitReliableQ"):
                    self.ceigrpxmitreliableq = value
                    self.ceigrpxmitreliableq.value_namespace = name_space
                    self.ceigrpxmitreliableq.value_namespace_prefix = name_space_prefix
                if(value_path == "cEigrpXmitUnreliableQ"):
                    self.ceigrpxmitunreliableq = value
                    self.ceigrpxmitunreliableq.value_namespace = name_space
                    self.ceigrpxmitunreliableq.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ceigrpinterfaceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ceigrpinterfaceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cEigrpInterfaceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cEigrpInterfaceEntry"):
                for c in self.ceigrpinterfaceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEigrpMib.Ceigrpinterfacetable.Ceigrpinterfaceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ceigrpinterfaceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cEigrpInterfaceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.ceigrpinterfacetable is not None and self.ceigrpinterfacetable.has_data()) or
            (self.ceigrppeertable is not None and self.ceigrppeertable.has_data()) or
            (self.ceigrptopotable is not None and self.ceigrptopotable.has_data()) or
            (self.ceigrptraffstatstable is not None and self.ceigrptraffstatstable.has_data()) or
            (self.ceigrpvpntable is not None and self.ceigrpvpntable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.ceigrpinterfacetable is not None and self.ceigrpinterfacetable.has_operation()) or
            (self.ceigrppeertable is not None and self.ceigrppeertable.has_operation()) or
            (self.ceigrptopotable is not None and self.ceigrptopotable.has_operation()) or
            (self.ceigrptraffstatstable is not None and self.ceigrptraffstatstable.has_operation()) or
            (self.ceigrpvpntable is not None and self.ceigrpvpntable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-EIGRP-MIB:CISCO-EIGRP-MIB" + path_buffer

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

        if (child_yang_name == "cEigrpInterfaceTable"):
            if (self.ceigrpinterfacetable is None):
                self.ceigrpinterfacetable = CiscoEigrpMib.Ceigrpinterfacetable()
                self.ceigrpinterfacetable.parent = self
                self._children_name_map["ceigrpinterfacetable"] = "cEigrpInterfaceTable"
            return self.ceigrpinterfacetable

        if (child_yang_name == "cEigrpPeerTable"):
            if (self.ceigrppeertable is None):
                self.ceigrppeertable = CiscoEigrpMib.Ceigrppeertable()
                self.ceigrppeertable.parent = self
                self._children_name_map["ceigrppeertable"] = "cEigrpPeerTable"
            return self.ceigrppeertable

        if (child_yang_name == "cEigrpTopoTable"):
            if (self.ceigrptopotable is None):
                self.ceigrptopotable = CiscoEigrpMib.Ceigrptopotable()
                self.ceigrptopotable.parent = self
                self._children_name_map["ceigrptopotable"] = "cEigrpTopoTable"
            return self.ceigrptopotable

        if (child_yang_name == "cEigrpTraffStatsTable"):
            if (self.ceigrptraffstatstable is None):
                self.ceigrptraffstatstable = CiscoEigrpMib.Ceigrptraffstatstable()
                self.ceigrptraffstatstable.parent = self
                self._children_name_map["ceigrptraffstatstable"] = "cEigrpTraffStatsTable"
            return self.ceigrptraffstatstable

        if (child_yang_name == "cEigrpVpnTable"):
            if (self.ceigrpvpntable is None):
                self.ceigrpvpntable = CiscoEigrpMib.Ceigrpvpntable()
                self.ceigrpvpntable.parent = self
                self._children_name_map["ceigrpvpntable"] = "cEigrpVpnTable"
            return self.ceigrpvpntable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cEigrpInterfaceTable" or name == "cEigrpPeerTable" or name == "cEigrpTopoTable" or name == "cEigrpTraffStatsTable" or name == "cEigrpVpnTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoEigrpMib()
        return self._top_entity

