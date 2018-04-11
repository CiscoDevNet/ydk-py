""" IP_MIB 

The MIB module for managing IP and ICMP implementations, but
excluding their management of IP routes.

Copyright (C) The Internet Society (2006).  This version of
this MIB module is part of RFC 4293; see the RFC itself for
full legal notices.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class IpAddressOriginTC(Enum):
    """
    IpAddressOriginTC (Enum Class)

    The origin of the address.

    manual(2) indicates that the address was manually configured

    to a specified address, e.g., by user configuration.

    dhcp(4) indicates an address that was assigned to this

    system by a DHCP server.

    linklayer(5) indicates an address created by IPv6 stateless

    auto\-configuration.

    random(6) indicates an address chosen by the system at

    random, e.g., an IPv4 address within 169.254/16, or an RFC

    3041 privacy address.

    .. data:: other = 1

    .. data:: manual = 2

    .. data:: dhcp = 4

    .. data:: linklayer = 5

    .. data:: random = 6

    """

    other = Enum.YLeaf(1, "other")

    manual = Enum.YLeaf(2, "manual")

    dhcp = Enum.YLeaf(4, "dhcp")

    linklayer = Enum.YLeaf(5, "linklayer")

    random = Enum.YLeaf(6, "random")


class IpAddressPrefixOriginTC(Enum):
    """
    IpAddressPrefixOriginTC (Enum Class)

    The origin of this prefix.

    manual(2) indicates a prefix that was manually configured.

    wellknown(3) indicates a well\-known prefix, e.g., 169.254/16

    for IPv4 auto\-configuration or fe80\:\:/10 for IPv6 link\-local

    addresses.  Well known prefixes may be assigned by IANA,

    the address registries, or by specification in a standards

    track RFC.

    dhcp(4) indicates a prefix that was assigned by a DHCP

    server.

    routeradv(5) indicates a prefix learned from a router

    advertisement.

    Note\: while IpAddressOriginTC and IpAddressPrefixOriginTC

    are similar, they are not identical.  The first defines how

    an address was created, while the second defines how a

    prefix was found.

    .. data:: other = 1

    .. data:: manual = 2

    .. data:: wellknown = 3

    .. data:: dhcp = 4

    .. data:: routeradv = 5

    """

    other = Enum.YLeaf(1, "other")

    manual = Enum.YLeaf(2, "manual")

    wellknown = Enum.YLeaf(3, "wellknown")

    dhcp = Enum.YLeaf(4, "dhcp")

    routeradv = Enum.YLeaf(5, "routeradv")


class IpAddressStatusTC(Enum):
    """
    IpAddressStatusTC (Enum Class)

    The status of an address.  Most of the states correspond to

    states from the IPv6 Stateless Address Autoconfiguration

    protocol.

    The preferred(1) state indicates that this is a valid

    address that can appear as the destination or source address

    of a packet.

    The deprecated(2) state indicates that this is a valid but

    deprecated address that should no longer be used as a source

    address in new communications, but packets addressed to such

    an address are processed as expected.

    The invalid(3) state indicates that this isn't a valid

    address and it shouldn't appear as the destination or source

    address of a packet.

    The inaccessible(4) state indicates that the address is not

    accessible because the interface to which this address is

    assigned is not operational.

    The unknown(5) state indicates that the status cannot be

    determined for some reason.

    The tentative(6) state indicates that the uniqueness of the

    address on the link is being verified.  Addresses in this

    state should not be used for general communication and

    should only be used to determine the uniqueness of the

    address.

    The duplicate(7) state indicates the address has been

    determined to be non\-unique on the link and so must not be

    used.

    The optimistic(8) state indicates the address is available

    for use, subject to restrictions, while its uniqueness on

    a link is being verified.

    In the absence of other information, an IPv4 address is

    always preferred(1).

    .. data:: preferred = 1

    .. data:: deprecated = 2

    .. data:: invalid = 3

    .. data:: inaccessible = 4

    .. data:: unknown = 5

    .. data:: tentative = 6

    .. data:: duplicate = 7

    .. data:: optimistic = 8

    """

    preferred = Enum.YLeaf(1, "preferred")

    deprecated = Enum.YLeaf(2, "deprecated")

    invalid = Enum.YLeaf(3, "invalid")

    inaccessible = Enum.YLeaf(4, "inaccessible")

    unknown = Enum.YLeaf(5, "unknown")

    tentative = Enum.YLeaf(6, "tentative")

    duplicate = Enum.YLeaf(7, "duplicate")

    optimistic = Enum.YLeaf(8, "optimistic")



class IPMIB(Entity):
    """
    
    
    .. attribute:: ip
    
    	
    	**type**\:  :py:class:`Ip <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ip>`
    
    .. attribute:: iptrafficstats
    
    	
    	**type**\:  :py:class:`Iptrafficstats <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Iptrafficstats>`
    
    .. attribute:: icmp
    
    	
    	**type**\:  :py:class:`Icmp <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Icmp>`
    
    .. attribute:: ipaddrtable
    
    	The table of addressing information relevant to this entity's IPv4 addresses.  This table has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by the ipAddressTable although several objects that weren't deemed useful weren't carried forward while another (ipAdEntReasmMaxSize) was moved to the ipv4InterfaceTable
    	**type**\:  :py:class:`Ipaddrtable <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipaddrtable>`
    
    	**status**\: deprecated
    
    .. attribute:: ipnettomediatable
    
    	The IPv4 Address Translation table used for mapping from IPv4 addresses to physical addresses.  This table has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by the ipNetToPhysicalTable
    	**type**\:  :py:class:`Ipnettomediatable <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipnettomediatable>`
    
    	**status**\: deprecated
    
    .. attribute:: ipv4interfacetable
    
    	The table containing per\-interface IPv4\-specific information
    	**type**\:  :py:class:`Ipv4Interfacetable <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipv4Interfacetable>`
    
    .. attribute:: ipv6interfacetable
    
    	The table containing per\-interface IPv6\-specific information
    	**type**\:  :py:class:`Ipv6Interfacetable <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipv6Interfacetable>`
    
    .. attribute:: ipsystemstatstable
    
    	The table containing system wide, IP version specific traffic statistics.  This table and the ipIfStatsTable contain similar objects whose difference is in their granularity.  Where this table contains system wide traffic statistics, the ipIfStatsTable contains the same statistics but counted on a per\-interface basis
    	**type**\:  :py:class:`Ipsystemstatstable <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipsystemstatstable>`
    
    .. attribute:: ipifstatstable
    
    	The table containing per\-interface traffic statistics.  This table and the ipSystemStatsTable contain similar objects whose difference is in their granularity.  Where this table contains per\-interface statistics, the ipSystemStatsTable contains the same statistics, but counted on a system wide basis
    	**type**\:  :py:class:`Ipifstatstable <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipifstatstable>`
    
    .. attribute:: ipaddressprefixtable
    
    	This table allows the user to determine the source of an IP address or set of IP addresses, and allows other tables to share the information via pointer rather than by copying.  For example, when the node configures both a unicast and anycast address for a prefix, the ipAddressPrefix objects for those addresses will point to a single row in this table.  This table primarily provides support for IPv6 prefixes, and several of the objects are less meaningful for IPv4.  The table continues to allow IPv4 addresses to allow future flexibility.  In order to promote a common configuration, this document includes suggestions for default values for IPv4 prefixes.  Each of these values may be overridden if an object is meaningful to the node.  All prefixes used by this entity should be included in this table independent of how the entity learned the prefix. (This table isn't limited to prefixes learned from router   advertisements.)
    	**type**\:  :py:class:`Ipaddressprefixtable <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipaddressprefixtable>`
    
    .. attribute:: ipaddresstable
    
    	This table contains addressing information relevant to the entity's interfaces.  This table does not contain multicast address information. Tables for such information should be contained in multicast specific MIBs, such as RFC 3019.  While this table is writable, the user will note that several objects, such as ipAddressOrigin, are not.  The intention in allowing a user to write to this table is to allow them to add or remove any entry that isn't   permanent.  The user should be allowed to modify objects and entries when that would not cause inconsistencies within the table.  Allowing write access to objects, such as ipAddressOrigin, could allow a user to insert an entry and then label it incorrectly.  Note well\: When including IPv6 link\-local addresses in this table, the entry must use an InetAddressType of 'ipv6z' in order to differentiate between the possible interfaces
    	**type**\:  :py:class:`Ipaddresstable <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipaddresstable>`
    
    .. attribute:: ipnettophysicaltable
    
    	The IP Address Translation table used for mapping from IP addresses to physical addresses.  The Address Translation tables contain the IP address to 'physical' address equivalences.  Some interfaces do not use translation tables for determining address equivalences (e.g., DDN\-X.25 has an algorithmic method); if all interfaces are of this type, then the Address Translation table is empty, i.e., has zero entries.  While many protocols may be used to populate this table, ARP and Neighbor Discovery are the most likely options
    	**type**\:  :py:class:`Ipnettophysicaltable <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipnettophysicaltable>`
    
    .. attribute:: ipv6scopezoneindextable
    
    	The table used to describe IPv6 unicast and multicast scope zones.  For those objects that have names rather than numbers, the names were chosen to coincide with the names used in the IPv6 address architecture document. 
    	**type**\:  :py:class:`Ipv6Scopezoneindextable <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipv6Scopezoneindextable>`
    
    .. attribute:: ipdefaultroutertable
    
    	The table used to describe the default routers known to this   entity
    	**type**\:  :py:class:`Ipdefaultroutertable <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipdefaultroutertable>`
    
    .. attribute:: ipv6routeradverttable
    
    	The table containing information used to construct router advertisements
    	**type**\:  :py:class:`Ipv6Routeradverttable <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipv6Routeradverttable>`
    
    .. attribute:: icmpstatstable
    
    	The table of generic system\-wide ICMP counters
    	**type**\:  :py:class:`Icmpstatstable <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Icmpstatstable>`
    
    .. attribute:: icmpmsgstatstable
    
    	The table of system\-wide per\-version, per\-message type ICMP counters
    	**type**\:  :py:class:`Icmpmsgstatstable <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Icmpmsgstatstable>`
    
    

    """

    _prefix = 'IP-MIB'
    _revision = '2006-02-02'

    def __init__(self):
        super(IPMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "IP-MIB"
        self.yang_parent_name = "IP-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("ip", ("ip", IPMIB.Ip)), ("ipTrafficStats", ("iptrafficstats", IPMIB.Iptrafficstats)), ("icmp", ("icmp", IPMIB.Icmp)), ("ipAddrTable", ("ipaddrtable", IPMIB.Ipaddrtable)), ("ipNetToMediaTable", ("ipnettomediatable", IPMIB.Ipnettomediatable)), ("ipv4InterfaceTable", ("ipv4interfacetable", IPMIB.Ipv4Interfacetable)), ("ipv6InterfaceTable", ("ipv6interfacetable", IPMIB.Ipv6Interfacetable)), ("ipSystemStatsTable", ("ipsystemstatstable", IPMIB.Ipsystemstatstable)), ("ipIfStatsTable", ("ipifstatstable", IPMIB.Ipifstatstable)), ("ipAddressPrefixTable", ("ipaddressprefixtable", IPMIB.Ipaddressprefixtable)), ("ipAddressTable", ("ipaddresstable", IPMIB.Ipaddresstable)), ("ipNetToPhysicalTable", ("ipnettophysicaltable", IPMIB.Ipnettophysicaltable)), ("ipv6ScopeZoneIndexTable", ("ipv6scopezoneindextable", IPMIB.Ipv6Scopezoneindextable)), ("ipDefaultRouterTable", ("ipdefaultroutertable", IPMIB.Ipdefaultroutertable)), ("ipv6RouterAdvertTable", ("ipv6routeradverttable", IPMIB.Ipv6Routeradverttable)), ("icmpStatsTable", ("icmpstatstable", IPMIB.Icmpstatstable)), ("icmpMsgStatsTable", ("icmpmsgstatstable", IPMIB.Icmpmsgstatstable))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.ip = IPMIB.Ip()
        self.ip.parent = self
        self._children_name_map["ip"] = "ip"
        self._children_yang_names.add("ip")

        self.iptrafficstats = IPMIB.Iptrafficstats()
        self.iptrafficstats.parent = self
        self._children_name_map["iptrafficstats"] = "ipTrafficStats"
        self._children_yang_names.add("ipTrafficStats")

        self.icmp = IPMIB.Icmp()
        self.icmp.parent = self
        self._children_name_map["icmp"] = "icmp"
        self._children_yang_names.add("icmp")

        self.ipaddrtable = IPMIB.Ipaddrtable()
        self.ipaddrtable.parent = self
        self._children_name_map["ipaddrtable"] = "ipAddrTable"
        self._children_yang_names.add("ipAddrTable")

        self.ipnettomediatable = IPMIB.Ipnettomediatable()
        self.ipnettomediatable.parent = self
        self._children_name_map["ipnettomediatable"] = "ipNetToMediaTable"
        self._children_yang_names.add("ipNetToMediaTable")

        self.ipv4interfacetable = IPMIB.Ipv4Interfacetable()
        self.ipv4interfacetable.parent = self
        self._children_name_map["ipv4interfacetable"] = "ipv4InterfaceTable"
        self._children_yang_names.add("ipv4InterfaceTable")

        self.ipv6interfacetable = IPMIB.Ipv6Interfacetable()
        self.ipv6interfacetable.parent = self
        self._children_name_map["ipv6interfacetable"] = "ipv6InterfaceTable"
        self._children_yang_names.add("ipv6InterfaceTable")

        self.ipsystemstatstable = IPMIB.Ipsystemstatstable()
        self.ipsystemstatstable.parent = self
        self._children_name_map["ipsystemstatstable"] = "ipSystemStatsTable"
        self._children_yang_names.add("ipSystemStatsTable")

        self.ipifstatstable = IPMIB.Ipifstatstable()
        self.ipifstatstable.parent = self
        self._children_name_map["ipifstatstable"] = "ipIfStatsTable"
        self._children_yang_names.add("ipIfStatsTable")

        self.ipaddressprefixtable = IPMIB.Ipaddressprefixtable()
        self.ipaddressprefixtable.parent = self
        self._children_name_map["ipaddressprefixtable"] = "ipAddressPrefixTable"
        self._children_yang_names.add("ipAddressPrefixTable")

        self.ipaddresstable = IPMIB.Ipaddresstable()
        self.ipaddresstable.parent = self
        self._children_name_map["ipaddresstable"] = "ipAddressTable"
        self._children_yang_names.add("ipAddressTable")

        self.ipnettophysicaltable = IPMIB.Ipnettophysicaltable()
        self.ipnettophysicaltable.parent = self
        self._children_name_map["ipnettophysicaltable"] = "ipNetToPhysicalTable"
        self._children_yang_names.add("ipNetToPhysicalTable")

        self.ipv6scopezoneindextable = IPMIB.Ipv6Scopezoneindextable()
        self.ipv6scopezoneindextable.parent = self
        self._children_name_map["ipv6scopezoneindextable"] = "ipv6ScopeZoneIndexTable"
        self._children_yang_names.add("ipv6ScopeZoneIndexTable")

        self.ipdefaultroutertable = IPMIB.Ipdefaultroutertable()
        self.ipdefaultroutertable.parent = self
        self._children_name_map["ipdefaultroutertable"] = "ipDefaultRouterTable"
        self._children_yang_names.add("ipDefaultRouterTable")

        self.ipv6routeradverttable = IPMIB.Ipv6Routeradverttable()
        self.ipv6routeradverttable.parent = self
        self._children_name_map["ipv6routeradverttable"] = "ipv6RouterAdvertTable"
        self._children_yang_names.add("ipv6RouterAdvertTable")

        self.icmpstatstable = IPMIB.Icmpstatstable()
        self.icmpstatstable.parent = self
        self._children_name_map["icmpstatstable"] = "icmpStatsTable"
        self._children_yang_names.add("icmpStatsTable")

        self.icmpmsgstatstable = IPMIB.Icmpmsgstatstable()
        self.icmpmsgstatstable.parent = self
        self._children_name_map["icmpmsgstatstable"] = "icmpMsgStatsTable"
        self._children_yang_names.add("icmpMsgStatsTable")
        self._segment_path = lambda: "IP-MIB:IP-MIB"


    class Ip(Entity):
        """
        
        
        .. attribute:: ipforwarding
        
        	The indication of whether this entity is acting as an IPv4 router in respect to the forwarding of datagrams received by, but not addressed to, this entity.  IPv4 routers forward datagrams.  IPv4 hosts do not (except those source\-routed via the host).  When this object is written, the entity should save the change to non\-volatile storage and restore the object from non\-volatile storage upon re\-initialization of the system. Note\: a stronger requirement is not used because this object was previously defined
        	**type**\:  :py:class:`Ipforwarding <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ip.Ipforwarding>`
        
        .. attribute:: ipdefaultttl
        
        	The default value inserted into the Time\-To\-Live field of the IPv4 header of datagrams originated at this entity, whenever a TTL value is not supplied by the transport layer   protocol.  When this object is written, the entity should save the change to non\-volatile storage and restore the object from non\-volatile storage upon re\-initialization of the system. Note\: a stronger requirement is not used because this object was previously defined
        	**type**\: int
        
        	**range:** 1..255
        
        .. attribute:: ipinreceives
        
        	The total number of input datagrams received from interfaces, including those received in error.  This object has been deprecated, as a new IP version\-neutral   table has been added.  It is loosely replaced by ipSystemStatsInRecieves
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipinhdrerrors
        
        	The number of input datagrams discarded due to errors in their IPv4 headers, including bad checksums, version number mismatch, other format errors, time\-to\-live exceeded, errors discovered in processing their IPv4 options, etc.  This object has been deprecated as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsInHdrErrors
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipinaddrerrors
        
        	The number of input datagrams discarded because the IPv4 address in their IPv4 header's destination field was not a valid address to be received at this entity.  This count includes invalid addresses (e.g., 0.0.0.0) and addresses of unsupported Classes (e.g., Class E).  For entities which are not IPv4 routers, and therefore do not forward datagrams, this counter includes datagrams discarded because the destination address was not a local address.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsInAddrErrors
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipforwdatagrams
        
        	The number of input datagrams for which this entity was not their final IPv4 destination, as a result of which an attempt was made to find a route to forward them to that final destination.  In entities which do not act as IPv4 routers, this counter will include only those packets which   were Source\-Routed via this entity, and the Source\-Route option processing was successful.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsInForwDatagrams
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipinunknownprotos
        
        	The number of locally\-addressed datagrams received successfully but discarded because of an unknown or unsupported protocol.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsInUnknownProtos
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipindiscards
        
        	The number of input IPv4 datagrams for which no problems were encountered to prevent their continued processing, but which were discarded (e.g., for lack of buffer space).  Note that this counter does not include any datagrams discarded while awaiting re\-assembly.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsInDiscards
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipindelivers
        
        	The total number of input datagrams successfully delivered to IPv4 user\-protocols (including ICMP).  This object has been deprecated as a new IP version neutral table has been added.  It is loosely replaced by   ipSystemStatsIndelivers
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipoutrequests
        
        	The total number of IPv4 datagrams which local IPv4 user protocols (including ICMP) supplied to IPv4 in requests for transmission.  Note that this counter does not include any datagrams counted in ipForwDatagrams.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsOutRequests
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipoutdiscards
        
        	The number of output IPv4 datagrams for which no problem was encountered to prevent their transmission to their destination, but which were discarded (e.g., for lack of buffer space).  Note that this counter would include datagrams counted in ipForwDatagrams if any such packets met this (discretionary) discard criterion.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsOutDiscards
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipoutnoroutes
        
        	The number of IPv4 datagrams discarded because no route could be found to transmit them to their destination.  Note that this counter includes any packets counted in ipForwDatagrams which meet this `no\-route' criterion.  Note that this includes any datagrams which a host cannot route because all of its default routers are down.  This object has been deprecated, as a new IP version\-neutral   table has been added.  It is loosely replaced by ipSystemStatsOutNoRoutes
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipreasmtimeout
        
        	The maximum number of seconds that received fragments are held while they are awaiting reassembly at this entity
        	**type**\: int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: seconds
        
        .. attribute:: ipreasmreqds
        
        	The number of IPv4 fragments received which needed to be reassembled at this entity.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsReasmReqds
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipreasmoks
        
        	The number of IPv4 datagrams successfully re\-assembled.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsReasmOKs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipreasmfails
        
        	The number of failures detected by the IPv4 re\-assembly algorithm (for whatever reason\: timed out, errors, etc). Note that this is not necessarily a count of discarded IPv4 fragments since some algorithms (notably the algorithm in RFC 815) can lose track of the number of fragments by combining them as they are received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsReasmFails
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipfragoks
        
        	The number of IPv4 datagrams that have been successfully fragmented at this entity.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsOutFragOKs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipfragfails
        
        	The number of IPv4 datagrams that have been discarded because they needed to be fragmented at this entity but could not be, e.g., because their Don't Fragment flag was set.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsOutFragFails
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipfragcreates
        
        	The number of IPv4 datagram fragments that have been generated as a result of fragmentation at this entity.  This object has been deprecated as a new IP version neutral table has been added.  It is loosely replaced by ipSystemStatsOutFragCreates
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: iproutingdiscards
        
        	The number of routing entries which were chosen to be discarded even though they are valid.  One possible reason for discarding such an entry could be to free\-up buffer space for other routing entries.   This object was defined in pre\-IPv6 versions of the IP MIB. It was implicitly IPv4 only, but the original specifications did not indicate this protocol restriction.  In order to clarify the specifications, this object has been deprecated and a similar, but more thoroughly clarified, object has been added to the IP\-FORWARD\-MIB
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipv6ipforwarding
        
        	The indication of whether this entity is acting as an IPv6 router on any interface in respect to the forwarding of datagrams received by, but not addressed to, this entity. IPv6 routers forward datagrams.  IPv6 hosts do not (except those source\-routed via the host).  When this object is written, the entity SHOULD save the change to non\-volatile storage and restore the object from non\-volatile storage upon re\-initialization of the system
        	**type**\:  :py:class:`Ipv6Ipforwarding <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ip.Ipv6Ipforwarding>`
        
        .. attribute:: ipv6ipdefaulthoplimit
        
        	The default value inserted into the Hop Limit field of the IPv6 header of datagrams originated at this entity whenever a Hop Limit value is not supplied by the transport layer protocol.  When this object is written, the entity SHOULD save the change to non\-volatile storage and restore the object from non\-volatile storage upon re\-initialization of the system
        	**type**\: int
        
        	**range:** 0..255
        
        .. attribute:: ipv4interfacetablelastchange
        
        	The value of sysUpTime on the most recent occasion at which a row in the ipv4InterfaceTable was added or deleted, or when an ipv4InterfaceReasmMaxSize or an ipv4InterfaceEnableStatus object was modified.  If new objects are added to the ipv4InterfaceTable that require the ipv4InterfaceTableLastChange to be updated when they are modified, they must specify that requirement in their description clause
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6interfacetablelastchange
        
        	The value of sysUpTime on the most recent occasion at which a row in the ipv6InterfaceTable was added or deleted or when an ipv6InterfaceReasmMaxSize, ipv6InterfaceIdentifier, ipv6InterfaceEnableStatus, ipv6InterfaceReachableTime, ipv6InterfaceRetransmitTime, or ipv6InterfaceForwarding object was modified.  If new objects are added to the ipv6InterfaceTable that require the ipv6InterfaceTableLastChange to be updated when they are modified, they must specify that requirement in their description clause
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipaddressspinlock
        
        	An advisory lock used to allow cooperating SNMP managers to coordinate their use of the set operation in creating or modifying rows within this table.  In order to use this lock to coordinate the use of set operations, managers should first retrieve ipAddressTableSpinLock.  They should then determine the appropriate row to create or modify.  Finally, they should issue the appropriate set command, including the retrieved value of ipAddressSpinLock.  If another manager has altered the table in the meantime, then the value of ipAddressSpinLock will have changed, and the creation will fail as it will be specifying an incorrect value for ipAddressSpinLock.  It is suggested, but not required, that the ipAddressSpinLock be the first var bind for each set of objects representing a 'row' in a PDU
        	**type**\: int
        
        	**range:** 0..2147483647
        
        .. attribute:: ipv6routeradvertspinlock
        
        	An advisory lock used to allow cooperating SNMP managers to coordinate their use of the set operation in creating or modifying rows within this table.  In order to use this lock to coordinate the use of set operations, managers should first retrieve ipv6RouterAdvertSpinLock.  They should then determine the appropriate row to create or modify.  Finally, they should issue the appropriate set command including the retrieved value of ipv6RouterAdvertSpinLock.  If another manager has altered the table in the meantime, then the value of ipv6RouterAdvertSpinLock will have changed and the creation will fail as it will be specifying an incorrect value for ipv6RouterAdvertSpinLock.  It is suggested, but not required, that the ipv6RouterAdvertSpinLock be the first var bind for each set of objects representing a 'row' in a PDU
        	**type**\: int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IPMIB.Ip, self).__init__()

            self.yang_name = "ip"
            self.yang_parent_name = "IP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ipforwarding', YLeaf(YType.enumeration, 'ipForwarding')),
                ('ipdefaultttl', YLeaf(YType.int32, 'ipDefaultTTL')),
                ('ipinreceives', YLeaf(YType.uint32, 'ipInReceives')),
                ('ipinhdrerrors', YLeaf(YType.uint32, 'ipInHdrErrors')),
                ('ipinaddrerrors', YLeaf(YType.uint32, 'ipInAddrErrors')),
                ('ipforwdatagrams', YLeaf(YType.uint32, 'ipForwDatagrams')),
                ('ipinunknownprotos', YLeaf(YType.uint32, 'ipInUnknownProtos')),
                ('ipindiscards', YLeaf(YType.uint32, 'ipInDiscards')),
                ('ipindelivers', YLeaf(YType.uint32, 'ipInDelivers')),
                ('ipoutrequests', YLeaf(YType.uint32, 'ipOutRequests')),
                ('ipoutdiscards', YLeaf(YType.uint32, 'ipOutDiscards')),
                ('ipoutnoroutes', YLeaf(YType.uint32, 'ipOutNoRoutes')),
                ('ipreasmtimeout', YLeaf(YType.int32, 'ipReasmTimeout')),
                ('ipreasmreqds', YLeaf(YType.uint32, 'ipReasmReqds')),
                ('ipreasmoks', YLeaf(YType.uint32, 'ipReasmOKs')),
                ('ipreasmfails', YLeaf(YType.uint32, 'ipReasmFails')),
                ('ipfragoks', YLeaf(YType.uint32, 'ipFragOKs')),
                ('ipfragfails', YLeaf(YType.uint32, 'ipFragFails')),
                ('ipfragcreates', YLeaf(YType.uint32, 'ipFragCreates')),
                ('iproutingdiscards', YLeaf(YType.uint32, 'ipRoutingDiscards')),
                ('ipv6ipforwarding', YLeaf(YType.enumeration, 'ipv6IpForwarding')),
                ('ipv6ipdefaulthoplimit', YLeaf(YType.int32, 'ipv6IpDefaultHopLimit')),
                ('ipv4interfacetablelastchange', YLeaf(YType.uint32, 'ipv4InterfaceTableLastChange')),
                ('ipv6interfacetablelastchange', YLeaf(YType.uint32, 'ipv6InterfaceTableLastChange')),
                ('ipaddressspinlock', YLeaf(YType.int32, 'ipAddressSpinLock')),
                ('ipv6routeradvertspinlock', YLeaf(YType.int32, 'ipv6RouterAdvertSpinLock')),
            ])
            self.ipforwarding = None
            self.ipdefaultttl = None
            self.ipinreceives = None
            self.ipinhdrerrors = None
            self.ipinaddrerrors = None
            self.ipforwdatagrams = None
            self.ipinunknownprotos = None
            self.ipindiscards = None
            self.ipindelivers = None
            self.ipoutrequests = None
            self.ipoutdiscards = None
            self.ipoutnoroutes = None
            self.ipreasmtimeout = None
            self.ipreasmreqds = None
            self.ipreasmoks = None
            self.ipreasmfails = None
            self.ipfragoks = None
            self.ipfragfails = None
            self.ipfragcreates = None
            self.iproutingdiscards = None
            self.ipv6ipforwarding = None
            self.ipv6ipdefaulthoplimit = None
            self.ipv4interfacetablelastchange = None
            self.ipv6interfacetablelastchange = None
            self.ipaddressspinlock = None
            self.ipv6routeradvertspinlock = None
            self._segment_path = lambda: "ip"
            self._absolute_path = lambda: "IP-MIB:IP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMIB.Ip, ['ipforwarding', 'ipdefaultttl', 'ipinreceives', 'ipinhdrerrors', 'ipinaddrerrors', 'ipforwdatagrams', 'ipinunknownprotos', 'ipindiscards', 'ipindelivers', 'ipoutrequests', 'ipoutdiscards', 'ipoutnoroutes', 'ipreasmtimeout', 'ipreasmreqds', 'ipreasmoks', 'ipreasmfails', 'ipfragoks', 'ipfragfails', 'ipfragcreates', 'iproutingdiscards', 'ipv6ipforwarding', 'ipv6ipdefaulthoplimit', 'ipv4interfacetablelastchange', 'ipv6interfacetablelastchange', 'ipaddressspinlock', 'ipv6routeradvertspinlock'], name, value)

        class Ipforwarding(Enum):
            """
            Ipforwarding (Enum Class)

            The indication of whether this entity is acting as an IPv4

            router in respect to the forwarding of datagrams received

            by, but not addressed to, this entity.  IPv4 routers forward

            datagrams.  IPv4 hosts do not (except those source\-routed

            via the host).

            When this object is written, the entity should save the

            change to non\-volatile storage and restore the object from

            non\-volatile storage upon re\-initialization of the system.

            Note\: a stronger requirement is not used because this object

            was previously defined.

            .. data:: forwarding = 1

            .. data:: notForwarding = 2

            """

            forwarding = Enum.YLeaf(1, "forwarding")

            notForwarding = Enum.YLeaf(2, "notForwarding")


        class Ipv6Ipforwarding(Enum):
            """
            Ipv6Ipforwarding (Enum Class)

            The indication of whether this entity is acting as an IPv6

            router on any interface in respect to the forwarding of

            datagrams received by, but not addressed to, this entity.

            IPv6 routers forward datagrams.  IPv6 hosts do not (except

            those source\-routed via the host).

            When this object is written, the entity SHOULD save the

            change to non\-volatile storage and restore the object from

            non\-volatile storage upon re\-initialization of the system.

            .. data:: forwarding = 1

            .. data:: notForwarding = 2

            """

            forwarding = Enum.YLeaf(1, "forwarding")

            notForwarding = Enum.YLeaf(2, "notForwarding")



    class Iptrafficstats(Entity):
        """
        
        
        .. attribute:: ipifstatstablelastchange
        
        	The value of sysUpTime on the most recent occasion at which a row in the ipIfStatsTable was added or deleted.  If new objects are added to the ipIfStatsTable that require the ipIfStatsTableLastChange to be updated when they are modified, they must specify that requirement in their description clause
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IPMIB.Iptrafficstats, self).__init__()

            self.yang_name = "ipTrafficStats"
            self.yang_parent_name = "IP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('ipifstatstablelastchange', YLeaf(YType.uint32, 'ipIfStatsTableLastChange')),
            ])
            self.ipifstatstablelastchange = None
            self._segment_path = lambda: "ipTrafficStats"
            self._absolute_path = lambda: "IP-MIB:IP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMIB.Iptrafficstats, ['ipifstatstablelastchange'], name, value)


    class Icmp(Entity):
        """
        
        
        .. attribute:: icmpinmsgs
        
        	The total number of ICMP messages which the entity received. Note that this counter includes all those counted by icmpInErrors.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by icmpStatsInMsgs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpinerrors
        
        	The number of ICMP messages which the entity received but determined as having ICMP\-specific errors (bad ICMP checksums, bad length, etc.).  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by icmpStatsInErrors
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpindestunreachs
        
        	The number of ICMP Destination Unreachable messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpintimeexcds
        
        	The number of ICMP Time Exceeded messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpinparmprobs
        
        	The number of ICMP Parameter Problem messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpinsrcquenchs
        
        	The number of ICMP Source Quench messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpinredirects
        
        	The number of ICMP Redirect messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpinechos
        
        	The number of ICMP Echo (request) messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpinechoreps
        
        	The number of ICMP Echo Reply messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpintimestamps
        
        	The number of ICMP Timestamp (request) messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpintimestampreps
        
        	The number of ICMP Timestamp Reply messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpinaddrmasks
        
        	The number of ICMP Address Mask Request messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpinaddrmaskreps
        
        	The number of ICMP Address Mask Reply messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpoutmsgs
        
        	The total number of ICMP messages which this entity attempted to send.  Note that this counter includes all those counted by icmpOutErrors.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by icmpStatsOutMsgs
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpouterrors
        
        	The number of ICMP messages which this entity did not send due to problems discovered within ICMP, such as a lack of buffers.  This value should not include errors discovered outside the ICMP layer, such as the inability of IP to route the resultant datagram.  In some implementations, there may be no types of error which contribute to this counter's value.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by icmpStatsOutErrors
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpoutdestunreachs
        
        	The number of ICMP Destination Unreachable messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpouttimeexcds
        
        	The number of ICMP Time Exceeded messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpoutparmprobs
        
        	The number of ICMP Parameter Problem messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpoutsrcquenchs
        
        	The number of ICMP Source Quench messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpoutredirects
        
        	The number of ICMP Redirect messages sent.  For a host, this object will always be zero, since hosts do not send redirects.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpoutechos
        
        	The number of ICMP Echo (request) messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpoutechoreps
        
        	The number of ICMP Echo Reply messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpouttimestamps
        
        	The number of ICMP Timestamp (request) messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpouttimestampreps
        
        	The number of ICMP Timestamp Reply messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpoutaddrmasks
        
        	The number of ICMP Address Mask Request messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpoutaddrmaskreps
        
        	The number of ICMP Address Mask Reply messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\: int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IPMIB.Icmp, self).__init__()

            self.yang_name = "icmp"
            self.yang_parent_name = "IP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('icmpinmsgs', YLeaf(YType.uint32, 'icmpInMsgs')),
                ('icmpinerrors', YLeaf(YType.uint32, 'icmpInErrors')),
                ('icmpindestunreachs', YLeaf(YType.uint32, 'icmpInDestUnreachs')),
                ('icmpintimeexcds', YLeaf(YType.uint32, 'icmpInTimeExcds')),
                ('icmpinparmprobs', YLeaf(YType.uint32, 'icmpInParmProbs')),
                ('icmpinsrcquenchs', YLeaf(YType.uint32, 'icmpInSrcQuenchs')),
                ('icmpinredirects', YLeaf(YType.uint32, 'icmpInRedirects')),
                ('icmpinechos', YLeaf(YType.uint32, 'icmpInEchos')),
                ('icmpinechoreps', YLeaf(YType.uint32, 'icmpInEchoReps')),
                ('icmpintimestamps', YLeaf(YType.uint32, 'icmpInTimestamps')),
                ('icmpintimestampreps', YLeaf(YType.uint32, 'icmpInTimestampReps')),
                ('icmpinaddrmasks', YLeaf(YType.uint32, 'icmpInAddrMasks')),
                ('icmpinaddrmaskreps', YLeaf(YType.uint32, 'icmpInAddrMaskReps')),
                ('icmpoutmsgs', YLeaf(YType.uint32, 'icmpOutMsgs')),
                ('icmpouterrors', YLeaf(YType.uint32, 'icmpOutErrors')),
                ('icmpoutdestunreachs', YLeaf(YType.uint32, 'icmpOutDestUnreachs')),
                ('icmpouttimeexcds', YLeaf(YType.uint32, 'icmpOutTimeExcds')),
                ('icmpoutparmprobs', YLeaf(YType.uint32, 'icmpOutParmProbs')),
                ('icmpoutsrcquenchs', YLeaf(YType.uint32, 'icmpOutSrcQuenchs')),
                ('icmpoutredirects', YLeaf(YType.uint32, 'icmpOutRedirects')),
                ('icmpoutechos', YLeaf(YType.uint32, 'icmpOutEchos')),
                ('icmpoutechoreps', YLeaf(YType.uint32, 'icmpOutEchoReps')),
                ('icmpouttimestamps', YLeaf(YType.uint32, 'icmpOutTimestamps')),
                ('icmpouttimestampreps', YLeaf(YType.uint32, 'icmpOutTimestampReps')),
                ('icmpoutaddrmasks', YLeaf(YType.uint32, 'icmpOutAddrMasks')),
                ('icmpoutaddrmaskreps', YLeaf(YType.uint32, 'icmpOutAddrMaskReps')),
            ])
            self.icmpinmsgs = None
            self.icmpinerrors = None
            self.icmpindestunreachs = None
            self.icmpintimeexcds = None
            self.icmpinparmprobs = None
            self.icmpinsrcquenchs = None
            self.icmpinredirects = None
            self.icmpinechos = None
            self.icmpinechoreps = None
            self.icmpintimestamps = None
            self.icmpintimestampreps = None
            self.icmpinaddrmasks = None
            self.icmpinaddrmaskreps = None
            self.icmpoutmsgs = None
            self.icmpouterrors = None
            self.icmpoutdestunreachs = None
            self.icmpouttimeexcds = None
            self.icmpoutparmprobs = None
            self.icmpoutsrcquenchs = None
            self.icmpoutredirects = None
            self.icmpoutechos = None
            self.icmpoutechoreps = None
            self.icmpouttimestamps = None
            self.icmpouttimestampreps = None
            self.icmpoutaddrmasks = None
            self.icmpoutaddrmaskreps = None
            self._segment_path = lambda: "icmp"
            self._absolute_path = lambda: "IP-MIB:IP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMIB.Icmp, ['icmpinmsgs', 'icmpinerrors', 'icmpindestunreachs', 'icmpintimeexcds', 'icmpinparmprobs', 'icmpinsrcquenchs', 'icmpinredirects', 'icmpinechos', 'icmpinechoreps', 'icmpintimestamps', 'icmpintimestampreps', 'icmpinaddrmasks', 'icmpinaddrmaskreps', 'icmpoutmsgs', 'icmpouterrors', 'icmpoutdestunreachs', 'icmpouttimeexcds', 'icmpoutparmprobs', 'icmpoutsrcquenchs', 'icmpoutredirects', 'icmpoutechos', 'icmpoutechoreps', 'icmpouttimestamps', 'icmpouttimestampreps', 'icmpoutaddrmasks', 'icmpoutaddrmaskreps'], name, value)


    class Ipaddrtable(Entity):
        """
        The table of addressing information relevant to this
        entity's IPv4 addresses.
        
        This table has been deprecated, as a new IP version\-neutral
        table has been added.  It is loosely replaced by the
        ipAddressTable although several objects that weren't deemed
        useful weren't carried forward while another
        (ipAdEntReasmMaxSize) was moved to the ipv4InterfaceTable.
        
        .. attribute:: ipaddrentry
        
        	The addressing information for one of this entity's IPv4 addresses
        	**type**\: list of  		 :py:class:`Ipaddrentry <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipaddrtable.Ipaddrentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IPMIB.Ipaddrtable, self).__init__()

            self.yang_name = "ipAddrTable"
            self.yang_parent_name = "IP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ipAddrEntry", ("ipaddrentry", IPMIB.Ipaddrtable.Ipaddrentry))])
            self._leafs = OrderedDict()

            self.ipaddrentry = YList(self)
            self._segment_path = lambda: "ipAddrTable"
            self._absolute_path = lambda: "IP-MIB:IP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMIB.Ipaddrtable, [], name, value)


        class Ipaddrentry(Entity):
            """
            The addressing information for one of this entity's IPv4
            addresses.
            
            .. attribute:: ipadentaddr  (key)
            
            	The IPv4 address to which this entry's addressing information pertains
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: ipadentifindex
            
            	The index value which uniquely identifies the interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: ipadentnetmask
            
            	The subnet mask associated with the IPv4 address of this entry.  The value of the mask is an IPv4 address with all the network bits set to 1 and all the hosts bits set to 0
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: ipadentbcastaddr
            
            	The value of the least\-significant bit in the IPv4 broadcast address used for sending datagrams on the (logical) interface associated with the IPv4 address of this entry. For example, when the Internet standard all\-ones broadcast address is used, the value will be 1.  This value applies to both the subnet and network broadcast addresses used by the entity on this (logical) interface
            	**type**\: int
            
            	**range:** 0..1
            
            	**status**\: deprecated
            
            .. attribute:: ipadentreasmmaxsize
            
            	The size of the largest IPv4 datagram which this entity can re\-assemble from incoming IPv4 fragmented datagrams received on this interface
            	**type**\: int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IPMIB.Ipaddrtable.Ipaddrentry, self).__init__()

                self.yang_name = "ipAddrEntry"
                self.yang_parent_name = "ipAddrTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipadentaddr']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipadentaddr', YLeaf(YType.str, 'ipAdEntAddr')),
                    ('ipadentifindex', YLeaf(YType.int32, 'ipAdEntIfIndex')),
                    ('ipadentnetmask', YLeaf(YType.str, 'ipAdEntNetMask')),
                    ('ipadentbcastaddr', YLeaf(YType.int32, 'ipAdEntBcastAddr')),
                    ('ipadentreasmmaxsize', YLeaf(YType.int32, 'ipAdEntReasmMaxSize')),
                ])
                self.ipadentaddr = None
                self.ipadentifindex = None
                self.ipadentnetmask = None
                self.ipadentbcastaddr = None
                self.ipadentreasmmaxsize = None
                self._segment_path = lambda: "ipAddrEntry" + "[ipAdEntAddr='" + str(self.ipadentaddr) + "']"
                self._absolute_path = lambda: "IP-MIB:IP-MIB/ipAddrTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMIB.Ipaddrtable.Ipaddrentry, ['ipadentaddr', 'ipadentifindex', 'ipadentnetmask', 'ipadentbcastaddr', 'ipadentreasmmaxsize'], name, value)


    class Ipnettomediatable(Entity):
        """
        The IPv4 Address Translation table used for mapping from
        IPv4 addresses to physical addresses.
        
        This table has been deprecated, as a new IP version\-neutral
        table has been added.  It is loosely replaced by the
        ipNetToPhysicalTable.
        
        .. attribute:: ipnettomediaentry
        
        	Each entry contains one IpAddress to `physical' address equivalence
        	**type**\: list of  		 :py:class:`Ipnettomediaentry <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipnettomediatable.Ipnettomediaentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IPMIB.Ipnettomediatable, self).__init__()

            self.yang_name = "ipNetToMediaTable"
            self.yang_parent_name = "IP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ipNetToMediaEntry", ("ipnettomediaentry", IPMIB.Ipnettomediatable.Ipnettomediaentry))])
            self._leafs = OrderedDict()

            self.ipnettomediaentry = YList(self)
            self._segment_path = lambda: "ipNetToMediaTable"
            self._absolute_path = lambda: "IP-MIB:IP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMIB.Ipnettomediatable, [], name, value)


        class Ipnettomediaentry(Entity):
            """
            Each entry contains one IpAddress to `physical' address
            equivalence.
            
            .. attribute:: ipnettomediaifindex  (key)
            
            	The interface on which this entry's equivalence is effective.  The interface identified by a particular value of this index is the same interface as identified by the   same value of the IF\-MIB's ifIndex.  This object predates the rule limiting index objects to a max access value of 'not\-accessible' and so continues to use a value of 'read\-create'
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: ipnettomedianetaddress  (key)
            
            	The IpAddress corresponding to the media\-dependent `physical' address.  This object predates the rule limiting index objects to a max access value of 'not\-accessible' and so continues to use a value of 'read\-create'
            	**type**\: str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: ipnettomediaphysaddress
            
            	The media\-dependent `physical' address.  This object should return 0 when this entry is in the 'incomplete' state.  As the entries in this table are typically not persistent when this object is written the entity should not save the change to non\-volatile storage.  Note\: a stronger requirement is not used because this object was previously defined
            	**type**\: str
            
            	**length:** 0..65535
            
            	**status**\: deprecated
            
            .. attribute:: ipnettomediatype
            
            	The type of mapping.  Setting this object to the value invalid(2) has the effect   of invalidating the corresponding entry in the ipNetToMediaTable.  That is, it effectively dis\-associates the interface identified with said entry from the mapping identified with said entry.  It is an implementation\- specific matter as to whether the agent removes an invalidated entry from the table.  Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use.  Proper interpretation of such entries requires examination of the relevant ipNetToMediaType object.  As the entries in this table are typically not persistent when this object is written the entity should not save the change to non\-volatile storage.  Note\: a stronger requirement is not used because this object was previously defined
            	**type**\:  :py:class:`Ipnettomediatype <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipnettomediatable.Ipnettomediaentry.Ipnettomediatype>`
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IPMIB.Ipnettomediatable.Ipnettomediaentry, self).__init__()

                self.yang_name = "ipNetToMediaEntry"
                self.yang_parent_name = "ipNetToMediaTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipnettomediaifindex','ipnettomedianetaddress']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipnettomediaifindex', YLeaf(YType.int32, 'ipNetToMediaIfIndex')),
                    ('ipnettomedianetaddress', YLeaf(YType.str, 'ipNetToMediaNetAddress')),
                    ('ipnettomediaphysaddress', YLeaf(YType.str, 'ipNetToMediaPhysAddress')),
                    ('ipnettomediatype', YLeaf(YType.enumeration, 'ipNetToMediaType')),
                ])
                self.ipnettomediaifindex = None
                self.ipnettomedianetaddress = None
                self.ipnettomediaphysaddress = None
                self.ipnettomediatype = None
                self._segment_path = lambda: "ipNetToMediaEntry" + "[ipNetToMediaIfIndex='" + str(self.ipnettomediaifindex) + "']" + "[ipNetToMediaNetAddress='" + str(self.ipnettomedianetaddress) + "']"
                self._absolute_path = lambda: "IP-MIB:IP-MIB/ipNetToMediaTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMIB.Ipnettomediatable.Ipnettomediaentry, ['ipnettomediaifindex', 'ipnettomedianetaddress', 'ipnettomediaphysaddress', 'ipnettomediatype'], name, value)

            class Ipnettomediatype(Enum):
                """
                Ipnettomediatype (Enum Class)

                The type of mapping.

                Setting this object to the value invalid(2) has the effect

                of invalidating the corresponding entry in the

                ipNetToMediaTable.  That is, it effectively dis\-associates

                the interface identified with said entry from the mapping

                identified with said entry.  It is an implementation\-

                specific matter as to whether the agent removes an

                invalidated entry from the table.  Accordingly, management

                stations must be prepared to receive tabular information

                from agents that corresponds to entries not currently in

                use.  Proper interpretation of such entries requires

                examination of the relevant ipNetToMediaType object.

                As the entries in this table are typically not persistent

                when this object is written the entity should not save the

                change to non\-volatile storage.  Note\: a stronger

                requirement is not used because this object was previously

                defined.

                .. data:: other = 1

                .. data:: invalid = 2

                .. data:: dynamic = 3

                .. data:: static = 4

                """

                other = Enum.YLeaf(1, "other")

                invalid = Enum.YLeaf(2, "invalid")

                dynamic = Enum.YLeaf(3, "dynamic")

                static = Enum.YLeaf(4, "static")



    class Ipv4Interfacetable(Entity):
        """
        The table containing per\-interface IPv4\-specific
        information.
        
        .. attribute:: ipv4interfaceentry
        
        	An entry containing IPv4\-specific information for a specific interface
        	**type**\: list of  		 :py:class:`Ipv4Interfaceentry <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipv4Interfacetable.Ipv4Interfaceentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IPMIB.Ipv4Interfacetable, self).__init__()

            self.yang_name = "ipv4InterfaceTable"
            self.yang_parent_name = "IP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ipv4InterfaceEntry", ("ipv4interfaceentry", IPMIB.Ipv4Interfacetable.Ipv4Interfaceentry))])
            self._leafs = OrderedDict()

            self.ipv4interfaceentry = YList(self)
            self._segment_path = lambda: "ipv4InterfaceTable"
            self._absolute_path = lambda: "IP-MIB:IP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMIB.Ipv4Interfacetable, [], name, value)


        class Ipv4Interfaceentry(Entity):
            """
            An entry containing IPv4\-specific information for a specific
            interface.
            
            .. attribute:: ipv4interfaceifindex  (key)
            
            	The index value that uniquely identifies the interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipv4interfacereasmmaxsize
            
            	The size of the largest IPv4 datagram that this entity can re\-assemble from incoming IPv4 fragmented datagrams received on this interface
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: ipv4interfaceenablestatus
            
            	The indication of whether IPv4 is enabled (up) or disabled (down) on this interface.  This object does not affect the state of the interface itself, only its connection to an IPv4 stack.  The IF\-MIB should be used to control the state of the interface
            	**type**\:  :py:class:`Ipv4Interfaceenablestatus <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipv4Interfacetable.Ipv4Interfaceentry.Ipv4Interfaceenablestatus>`
            
            .. attribute:: ipv4interfaceretransmittime
            
            	The time between retransmissions of ARP requests to a neighbor when resolving the address or when probing the reachability of a neighbor
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IPMIB.Ipv4Interfacetable.Ipv4Interfaceentry, self).__init__()

                self.yang_name = "ipv4InterfaceEntry"
                self.yang_parent_name = "ipv4InterfaceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipv4interfaceifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipv4interfaceifindex', YLeaf(YType.int32, 'ipv4InterfaceIfIndex')),
                    ('ipv4interfacereasmmaxsize', YLeaf(YType.int32, 'ipv4InterfaceReasmMaxSize')),
                    ('ipv4interfaceenablestatus', YLeaf(YType.enumeration, 'ipv4InterfaceEnableStatus')),
                    ('ipv4interfaceretransmittime', YLeaf(YType.uint32, 'ipv4InterfaceRetransmitTime')),
                ])
                self.ipv4interfaceifindex = None
                self.ipv4interfacereasmmaxsize = None
                self.ipv4interfaceenablestatus = None
                self.ipv4interfaceretransmittime = None
                self._segment_path = lambda: "ipv4InterfaceEntry" + "[ipv4InterfaceIfIndex='" + str(self.ipv4interfaceifindex) + "']"
                self._absolute_path = lambda: "IP-MIB:IP-MIB/ipv4InterfaceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMIB.Ipv4Interfacetable.Ipv4Interfaceentry, ['ipv4interfaceifindex', 'ipv4interfacereasmmaxsize', 'ipv4interfaceenablestatus', 'ipv4interfaceretransmittime'], name, value)

            class Ipv4Interfaceenablestatus(Enum):
                """
                Ipv4Interfaceenablestatus (Enum Class)

                The indication of whether IPv4 is enabled (up) or disabled

                (down) on this interface.  This object does not affect the

                state of the interface itself, only its connection to an

                IPv4 stack.  The IF\-MIB should be used to control the state

                of the interface.

                .. data:: up = 1

                .. data:: down = 2

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")



    class Ipv6Interfacetable(Entity):
        """
        The table containing per\-interface IPv6\-specific
        information.
        
        .. attribute:: ipv6interfaceentry
        
        	An entry containing IPv6\-specific information for a given interface
        	**type**\: list of  		 :py:class:`Ipv6Interfaceentry <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipv6Interfacetable.Ipv6Interfaceentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IPMIB.Ipv6Interfacetable, self).__init__()

            self.yang_name = "ipv6InterfaceTable"
            self.yang_parent_name = "IP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ipv6InterfaceEntry", ("ipv6interfaceentry", IPMIB.Ipv6Interfacetable.Ipv6Interfaceentry))])
            self._leafs = OrderedDict()

            self.ipv6interfaceentry = YList(self)
            self._segment_path = lambda: "ipv6InterfaceTable"
            self._absolute_path = lambda: "IP-MIB:IP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMIB.Ipv6Interfacetable, [], name, value)


        class Ipv6Interfaceentry(Entity):
            """
            An entry containing IPv6\-specific information for a given
            interface.
            
            .. attribute:: ipv6interfaceifindex  (key)
            
            	The index value that uniquely identifies the interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipv6interfacereasmmaxsize
            
            	The size of the largest IPv6 datagram that this entity can re\-assemble from incoming IPv6 fragmented datagrams received on this interface
            	**type**\: int
            
            	**range:** 1500..65535
            
            	**units**\: octets
            
            .. attribute:: ipv6interfaceidentifier
            
            	The Interface Identifier for this interface.  The Interface Identifier is combined with an address prefix to form an interface address.  By default, the Interface Identifier is auto\-configured according to the rules of the link type to which this interface is attached.   A zero length identifier may be used where appropriate.  One possible example is a loopback interface
            	**type**\: str
            
            .. attribute:: ipv6interfaceenablestatus
            
            	The indication of whether IPv6 is enabled (up) or disabled (down) on this interface.  This object does not affect the state of the interface itself, only its connection to an IPv6 stack.  The IF\-MIB should be used to control the state of the interface.  When this object is written, the entity SHOULD save the change to non\-volatile storage and restore the object from non\-volatile storage upon re\-initialization of the system
            	**type**\:  :py:class:`Ipv6Interfaceenablestatus <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipv6Interfacetable.Ipv6Interfaceentry.Ipv6Interfaceenablestatus>`
            
            .. attribute:: ipv6interfacereachabletime
            
            	The time a neighbor is considered reachable after receiving a reachability confirmation
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: ipv6interfaceretransmittime
            
            	The time between retransmissions of Neighbor Solicitation messages to a neighbor when resolving the address or when probing the reachability of a neighbor
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: ipv6interfaceforwarding
            
            	The indication of whether this entity is acting as an IPv6 router on this interface with respect to the forwarding of datagrams received by, but not addressed to, this entity. IPv6 routers forward datagrams.  IPv6 hosts do not (except those source\-routed via the host).  This object is constrained by ipv6IpForwarding and is ignored if ipv6IpForwarding is set to notForwarding.  Those systems that do not provide per\-interface control of the forwarding function should set this object to forwarding for all interfaces and allow the ipv6IpForwarding object to control the forwarding capability.  When this object is written, the entity SHOULD save the change to non\-volatile storage and restore the object from non\-volatile storage upon re\-initialization of the system
            	**type**\:  :py:class:`Ipv6Interfaceforwarding <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipv6Interfacetable.Ipv6Interfaceentry.Ipv6Interfaceforwarding>`
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IPMIB.Ipv6Interfacetable.Ipv6Interfaceentry, self).__init__()

                self.yang_name = "ipv6InterfaceEntry"
                self.yang_parent_name = "ipv6InterfaceTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipv6interfaceifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipv6interfaceifindex', YLeaf(YType.int32, 'ipv6InterfaceIfIndex')),
                    ('ipv6interfacereasmmaxsize', YLeaf(YType.uint32, 'ipv6InterfaceReasmMaxSize')),
                    ('ipv6interfaceidentifier', YLeaf(YType.str, 'ipv6InterfaceIdentifier')),
                    ('ipv6interfaceenablestatus', YLeaf(YType.enumeration, 'ipv6InterfaceEnableStatus')),
                    ('ipv6interfacereachabletime', YLeaf(YType.uint32, 'ipv6InterfaceReachableTime')),
                    ('ipv6interfaceretransmittime', YLeaf(YType.uint32, 'ipv6InterfaceRetransmitTime')),
                    ('ipv6interfaceforwarding', YLeaf(YType.enumeration, 'ipv6InterfaceForwarding')),
                ])
                self.ipv6interfaceifindex = None
                self.ipv6interfacereasmmaxsize = None
                self.ipv6interfaceidentifier = None
                self.ipv6interfaceenablestatus = None
                self.ipv6interfacereachabletime = None
                self.ipv6interfaceretransmittime = None
                self.ipv6interfaceforwarding = None
                self._segment_path = lambda: "ipv6InterfaceEntry" + "[ipv6InterfaceIfIndex='" + str(self.ipv6interfaceifindex) + "']"
                self._absolute_path = lambda: "IP-MIB:IP-MIB/ipv6InterfaceTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMIB.Ipv6Interfacetable.Ipv6Interfaceentry, ['ipv6interfaceifindex', 'ipv6interfacereasmmaxsize', 'ipv6interfaceidentifier', 'ipv6interfaceenablestatus', 'ipv6interfacereachabletime', 'ipv6interfaceretransmittime', 'ipv6interfaceforwarding'], name, value)

            class Ipv6Interfaceenablestatus(Enum):
                """
                Ipv6Interfaceenablestatus (Enum Class)

                The indication of whether IPv6 is enabled (up) or disabled

                (down) on this interface.  This object does not affect the

                state of the interface itself, only its connection to an

                IPv6 stack.  The IF\-MIB should be used to control the state

                of the interface.

                When this object is written, the entity SHOULD save the

                change to non\-volatile storage and restore the object from

                non\-volatile storage upon re\-initialization of the system.

                .. data:: up = 1

                .. data:: down = 2

                """

                up = Enum.YLeaf(1, "up")

                down = Enum.YLeaf(2, "down")


            class Ipv6Interfaceforwarding(Enum):
                """
                Ipv6Interfaceforwarding (Enum Class)

                The indication of whether this entity is acting as an IPv6

                router on this interface with respect to the forwarding of

                datagrams received by, but not addressed to, this entity.

                IPv6 routers forward datagrams.  IPv6 hosts do not (except

                those source\-routed via the host).

                This object is constrained by ipv6IpForwarding and is

                ignored if ipv6IpForwarding is set to notForwarding.  Those

                systems that do not provide per\-interface control of the

                forwarding function should set this object to forwarding for

                all interfaces and allow the ipv6IpForwarding object to

                control the forwarding capability.

                When this object is written, the entity SHOULD save the

                change to non\-volatile storage and restore the object from

                non\-volatile storage upon re\-initialization of the system.

                .. data:: forwarding = 1

                .. data:: notForwarding = 2

                """

                forwarding = Enum.YLeaf(1, "forwarding")

                notForwarding = Enum.YLeaf(2, "notForwarding")



    class Ipsystemstatstable(Entity):
        """
        The table containing system wide, IP version specific
        traffic statistics.  This table and the ipIfStatsTable
        contain similar objects whose difference is in their
        granularity.  Where this table contains system wide traffic
        statistics, the ipIfStatsTable contains the same statistics
        but counted on a per\-interface basis.
        
        .. attribute:: ipsystemstatsentry
        
        	A statistics entry containing system\-wide objects for a particular IP version
        	**type**\: list of  		 :py:class:`Ipsystemstatsentry <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipsystemstatstable.Ipsystemstatsentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IPMIB.Ipsystemstatstable, self).__init__()

            self.yang_name = "ipSystemStatsTable"
            self.yang_parent_name = "IP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ipSystemStatsEntry", ("ipsystemstatsentry", IPMIB.Ipsystemstatstable.Ipsystemstatsentry))])
            self._leafs = OrderedDict()

            self.ipsystemstatsentry = YList(self)
            self._segment_path = lambda: "ipSystemStatsTable"
            self._absolute_path = lambda: "IP-MIB:IP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMIB.Ipsystemstatstable, [], name, value)


        class Ipsystemstatsentry(Entity):
            """
            A statistics entry containing system\-wide objects for a
            particular IP version.
            
            .. attribute:: ipsystemstatsipversion  (key)
            
            	The IP version of this row
            	**type**\:  :py:class:`IpVersion <ydk.models.ietf.ietf_inet_types.IpVersion>`
            
            .. attribute:: ipsystemstatsinreceives
            
            	The total number of input IP datagrams received, including those received in error.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatshcinreceives
            
            	The total number of input IP datagrams received, including those received in error.  This object counts the same datagrams as ipSystemStatsInReceives, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatsinoctets
            
            	The total number of octets received in input IP datagrams, including those received in error.  Octets from datagrams counted in ipSystemStatsInReceives MUST be counted here.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatshcinoctets
            
            	The total number of octets received in input IP datagrams, including those received in error.  This object counts the same octets as ipSystemStatsInOctets, but allows for larger   values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatsinhdrerrors
            
            	The number of input IP datagrams discarded due to errors in their IP headers, including version number mismatch, other format errors, hop count exceeded, errors discovered in processing their IP options, etc.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsinnoroutes
            
            	The number of input IP datagrams discarded because no route could be found to transmit them to their destination.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsinaddrerrors
            
            	The number of input IP datagrams discarded because the IP address in their IP header's destination field was not a valid address to be received at this entity.  This count includes invalid addresses (e.g., \:\:0).  For entities that are not IP routers and therefore do not forward   datagrams, this counter includes datagrams discarded because the destination address was not a local address.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsinunknownprotos
            
            	The number of locally\-addressed IP datagrams received successfully but discarded because of an unknown or unsupported protocol.  When tracking interface statistics, the counter of the interface to which these datagrams were addressed is incremented.  This interface might not be the same as the input interface for some of the datagrams.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsintruncatedpkts
            
            	The number of input IP datagrams discarded because the datagram frame didn't carry enough data.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsinforwdatagrams
            
            	The number of input datagrams for which this entity was not their final IP destination and for which this entity attempted to find a route to forward them to that final destination.  In entities that do not act as IP routers, this counter will include only those datagrams that were Source\-Routed via this entity, and the Source\-Route processing was successful.  When tracking interface statistics, the counter of the incoming interface is incremented for each datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatshcinforwdatagrams
            
            	The number of input datagrams for which this entity was not their final IP destination and for which this entity attempted to find a route to forward them to that final destination.  This object counts the same packets as ipSystemStatsInForwDatagrams, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatsreasmreqds
            
            	The number of IP fragments received that needed to be reassembled at this interface.  When tracking interface statistics, the counter of the interface to which these fragments were addressed is incremented.  This interface might not be the same as the input interface for some of the fragments.  Discontinuities in the value of this counter can occur at   re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsreasmoks
            
            	The number of IP datagrams successfully reassembled.  When tracking interface statistics, the counter of the interface to which these datagrams were addressed is incremented.  This interface might not be the same as the input interface for some of the datagrams.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsreasmfails
            
            	The number of failures detected by the IP re\-assembly algorithm (for whatever reason\: timed out, errors, etc.). Note that this is not necessarily a count of discarded IP fragments since some algorithms (notably the algorithm in RFC 815) can lose track of the number of fragments by combining them as they are received.  When tracking interface statistics, the counter of the interface to which these fragments were addressed is incremented.  This interface might not be the same as the input interface for some of the fragments.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsindiscards
            
            	The number of input IP datagrams for which no problems were encountered to prevent their continued processing, but were discarded (e.g., for lack of buffer space).  Note that this counter does not include any datagrams discarded while awaiting re\-assembly.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsindelivers
            
            	The total number of datagrams successfully delivered to IP user\-protocols (including ICMP).  When tracking interface statistics, the counter of the interface to which these datagrams were addressed is incremented.  This interface might not be the same as the input interface for some of the datagrams.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatshcindelivers
            
            	The total number of datagrams successfully delivered to IP user\-protocols (including ICMP).  This object counts the same packets as ipSystemStatsInDelivers, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatsoutrequests
            
            	The total number of IP datagrams that local IP user\- protocols (including ICMP) supplied to IP in requests for transmission.  Note that this counter does not include any datagrams counted in ipSystemStatsOutForwDatagrams.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatshcoutrequests
            
            	The total number of IP datagrams that local IP user\- protocols (including ICMP) supplied to IP in requests for transmission.  This object counts the same packets as ipSystemStatsOutRequests, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatsoutnoroutes
            
            	The number of locally generated IP datagrams discarded because no route could be found to transmit them to their destination.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsoutforwdatagrams
            
            	The number of datagrams for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination.  In entities that do not act as IP routers, this counter will include only those datagrams that were Source\-Routed via this entity, and the Source\-Route processing was successful.  When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully forwarded datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatshcoutforwdatagrams
            
            	The number of datagrams for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination.  This object counts the same packets as ipSystemStatsOutForwDatagrams, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatsoutdiscards
            
            	The number of output IP datagrams for which no problem was encountered to prevent their transmission to their destination, but were discarded (e.g., for lack of buffer space).  Note that this counter would include   datagrams counted in ipSystemStatsOutForwDatagrams if any such datagrams met this (discretionary) discard criterion.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsoutfragreqds
            
            	The number of IP datagrams that would require fragmentation in order to be transmitted.  When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully fragmented datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsoutfragoks
            
            	The number of IP datagrams that have been successfully fragmented.  When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully fragmented datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsoutfragfails
            
            	The number of IP datagrams that have been discarded because they needed to be fragmented but could not be.  This includes IPv4 packets that have the DF bit set and IPv6 packets that are being forwarded and exceed the outgoing link MTU.  When tracking interface statistics, the counter of the outgoing interface is incremented for an unsuccessfully fragmented datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsoutfragcreates
            
            	The number of output datagram fragments that have been generated as a result of IP fragmentation.  When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully fragmented datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsouttransmits
            
            	The total number of IP datagrams that this entity supplied to the lower layers for transmission.  This includes datagrams generated locally and those forwarded by this entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other   times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatshcouttransmits
            
            	The total number of IP datagrams that this entity supplied to the lower layers for transmission.  This object counts the same datagrams as ipSystemStatsOutTransmits, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatsoutoctets
            
            	The total number of octets in IP datagrams delivered to the lower layers for transmission.  Octets from datagrams counted in ipSystemStatsOutTransmits MUST be counted here.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatshcoutoctets
            
            	The total number of octets in IP datagrams delivered to the lower layers for transmission.  This objects counts the same octets as ipSystemStatsOutOctets, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of   ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatsinmcastpkts
            
            	The number of IP multicast datagrams received.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatshcinmcastpkts
            
            	The number of IP multicast datagrams received.  This object counts the same datagrams as ipSystemStatsInMcastPkts but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatsinmcastoctets
            
            	The total number of octets received in IP multicast datagrams.  Octets from datagrams counted in ipSystemStatsInMcastPkts MUST be counted here.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatshcinmcastoctets
            
            	The total number of octets received in IP multicast datagrams.  This object counts the same octets as ipSystemStatsInMcastOctets, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatsoutmcastpkts
            
            	The number of IP multicast datagrams transmitted.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatshcoutmcastpkts
            
            	The number of IP multicast datagrams transmitted.  This object counts the same datagrams as ipSystemStatsOutMcastPkts, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatsoutmcastoctets
            
            	The total number of octets transmitted in IP multicast datagrams.  Octets from datagrams counted in   ipSystemStatsOutMcastPkts MUST be counted here.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatshcoutmcastoctets
            
            	The total number of octets transmitted in IP multicast datagrams.  This object counts the same octets as ipSystemStatsOutMcastOctets, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatsinbcastpkts
            
            	The number of IP broadcast datagrams received.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatshcinbcastpkts
            
            	The number of IP broadcast datagrams received.  This object counts the same datagrams as ipSystemStatsInBcastPkts but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of   ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatsoutbcastpkts
            
            	The number of IP broadcast datagrams transmitted.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatshcoutbcastpkts
            
            	The number of IP broadcast datagrams transmitted.  This object counts the same datagrams as ipSystemStatsOutBcastPkts, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatsdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this entry's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\- initialization of the local management subsystem, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsrefreshrate
            
            	The minimum reasonable polling interval for this entry. This object provides an indication of the minimum amount of time required to update the counters in this entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milli-seconds
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IPMIB.Ipsystemstatstable.Ipsystemstatsentry, self).__init__()

                self.yang_name = "ipSystemStatsEntry"
                self.yang_parent_name = "ipSystemStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipsystemstatsipversion']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipsystemstatsipversion', YLeaf(YType.enumeration, 'ipSystemStatsIPVersion')),
                    ('ipsystemstatsinreceives', YLeaf(YType.uint32, 'ipSystemStatsInReceives')),
                    ('ipsystemstatshcinreceives', YLeaf(YType.uint64, 'ipSystemStatsHCInReceives')),
                    ('ipsystemstatsinoctets', YLeaf(YType.uint32, 'ipSystemStatsInOctets')),
                    ('ipsystemstatshcinoctets', YLeaf(YType.uint64, 'ipSystemStatsHCInOctets')),
                    ('ipsystemstatsinhdrerrors', YLeaf(YType.uint32, 'ipSystemStatsInHdrErrors')),
                    ('ipsystemstatsinnoroutes', YLeaf(YType.uint32, 'ipSystemStatsInNoRoutes')),
                    ('ipsystemstatsinaddrerrors', YLeaf(YType.uint32, 'ipSystemStatsInAddrErrors')),
                    ('ipsystemstatsinunknownprotos', YLeaf(YType.uint32, 'ipSystemStatsInUnknownProtos')),
                    ('ipsystemstatsintruncatedpkts', YLeaf(YType.uint32, 'ipSystemStatsInTruncatedPkts')),
                    ('ipsystemstatsinforwdatagrams', YLeaf(YType.uint32, 'ipSystemStatsInForwDatagrams')),
                    ('ipsystemstatshcinforwdatagrams', YLeaf(YType.uint64, 'ipSystemStatsHCInForwDatagrams')),
                    ('ipsystemstatsreasmreqds', YLeaf(YType.uint32, 'ipSystemStatsReasmReqds')),
                    ('ipsystemstatsreasmoks', YLeaf(YType.uint32, 'ipSystemStatsReasmOKs')),
                    ('ipsystemstatsreasmfails', YLeaf(YType.uint32, 'ipSystemStatsReasmFails')),
                    ('ipsystemstatsindiscards', YLeaf(YType.uint32, 'ipSystemStatsInDiscards')),
                    ('ipsystemstatsindelivers', YLeaf(YType.uint32, 'ipSystemStatsInDelivers')),
                    ('ipsystemstatshcindelivers', YLeaf(YType.uint64, 'ipSystemStatsHCInDelivers')),
                    ('ipsystemstatsoutrequests', YLeaf(YType.uint32, 'ipSystemStatsOutRequests')),
                    ('ipsystemstatshcoutrequests', YLeaf(YType.uint64, 'ipSystemStatsHCOutRequests')),
                    ('ipsystemstatsoutnoroutes', YLeaf(YType.uint32, 'ipSystemStatsOutNoRoutes')),
                    ('ipsystemstatsoutforwdatagrams', YLeaf(YType.uint32, 'ipSystemStatsOutForwDatagrams')),
                    ('ipsystemstatshcoutforwdatagrams', YLeaf(YType.uint64, 'ipSystemStatsHCOutForwDatagrams')),
                    ('ipsystemstatsoutdiscards', YLeaf(YType.uint32, 'ipSystemStatsOutDiscards')),
                    ('ipsystemstatsoutfragreqds', YLeaf(YType.uint32, 'ipSystemStatsOutFragReqds')),
                    ('ipsystemstatsoutfragoks', YLeaf(YType.uint32, 'ipSystemStatsOutFragOKs')),
                    ('ipsystemstatsoutfragfails', YLeaf(YType.uint32, 'ipSystemStatsOutFragFails')),
                    ('ipsystemstatsoutfragcreates', YLeaf(YType.uint32, 'ipSystemStatsOutFragCreates')),
                    ('ipsystemstatsouttransmits', YLeaf(YType.uint32, 'ipSystemStatsOutTransmits')),
                    ('ipsystemstatshcouttransmits', YLeaf(YType.uint64, 'ipSystemStatsHCOutTransmits')),
                    ('ipsystemstatsoutoctets', YLeaf(YType.uint32, 'ipSystemStatsOutOctets')),
                    ('ipsystemstatshcoutoctets', YLeaf(YType.uint64, 'ipSystemStatsHCOutOctets')),
                    ('ipsystemstatsinmcastpkts', YLeaf(YType.uint32, 'ipSystemStatsInMcastPkts')),
                    ('ipsystemstatshcinmcastpkts', YLeaf(YType.uint64, 'ipSystemStatsHCInMcastPkts')),
                    ('ipsystemstatsinmcastoctets', YLeaf(YType.uint32, 'ipSystemStatsInMcastOctets')),
                    ('ipsystemstatshcinmcastoctets', YLeaf(YType.uint64, 'ipSystemStatsHCInMcastOctets')),
                    ('ipsystemstatsoutmcastpkts', YLeaf(YType.uint32, 'ipSystemStatsOutMcastPkts')),
                    ('ipsystemstatshcoutmcastpkts', YLeaf(YType.uint64, 'ipSystemStatsHCOutMcastPkts')),
                    ('ipsystemstatsoutmcastoctets', YLeaf(YType.uint32, 'ipSystemStatsOutMcastOctets')),
                    ('ipsystemstatshcoutmcastoctets', YLeaf(YType.uint64, 'ipSystemStatsHCOutMcastOctets')),
                    ('ipsystemstatsinbcastpkts', YLeaf(YType.uint32, 'ipSystemStatsInBcastPkts')),
                    ('ipsystemstatshcinbcastpkts', YLeaf(YType.uint64, 'ipSystemStatsHCInBcastPkts')),
                    ('ipsystemstatsoutbcastpkts', YLeaf(YType.uint32, 'ipSystemStatsOutBcastPkts')),
                    ('ipsystemstatshcoutbcastpkts', YLeaf(YType.uint64, 'ipSystemStatsHCOutBcastPkts')),
                    ('ipsystemstatsdiscontinuitytime', YLeaf(YType.uint32, 'ipSystemStatsDiscontinuityTime')),
                    ('ipsystemstatsrefreshrate', YLeaf(YType.uint32, 'ipSystemStatsRefreshRate')),
                ])
                self.ipsystemstatsipversion = None
                self.ipsystemstatsinreceives = None
                self.ipsystemstatshcinreceives = None
                self.ipsystemstatsinoctets = None
                self.ipsystemstatshcinoctets = None
                self.ipsystemstatsinhdrerrors = None
                self.ipsystemstatsinnoroutes = None
                self.ipsystemstatsinaddrerrors = None
                self.ipsystemstatsinunknownprotos = None
                self.ipsystemstatsintruncatedpkts = None
                self.ipsystemstatsinforwdatagrams = None
                self.ipsystemstatshcinforwdatagrams = None
                self.ipsystemstatsreasmreqds = None
                self.ipsystemstatsreasmoks = None
                self.ipsystemstatsreasmfails = None
                self.ipsystemstatsindiscards = None
                self.ipsystemstatsindelivers = None
                self.ipsystemstatshcindelivers = None
                self.ipsystemstatsoutrequests = None
                self.ipsystemstatshcoutrequests = None
                self.ipsystemstatsoutnoroutes = None
                self.ipsystemstatsoutforwdatagrams = None
                self.ipsystemstatshcoutforwdatagrams = None
                self.ipsystemstatsoutdiscards = None
                self.ipsystemstatsoutfragreqds = None
                self.ipsystemstatsoutfragoks = None
                self.ipsystemstatsoutfragfails = None
                self.ipsystemstatsoutfragcreates = None
                self.ipsystemstatsouttransmits = None
                self.ipsystemstatshcouttransmits = None
                self.ipsystemstatsoutoctets = None
                self.ipsystemstatshcoutoctets = None
                self.ipsystemstatsinmcastpkts = None
                self.ipsystemstatshcinmcastpkts = None
                self.ipsystemstatsinmcastoctets = None
                self.ipsystemstatshcinmcastoctets = None
                self.ipsystemstatsoutmcastpkts = None
                self.ipsystemstatshcoutmcastpkts = None
                self.ipsystemstatsoutmcastoctets = None
                self.ipsystemstatshcoutmcastoctets = None
                self.ipsystemstatsinbcastpkts = None
                self.ipsystemstatshcinbcastpkts = None
                self.ipsystemstatsoutbcastpkts = None
                self.ipsystemstatshcoutbcastpkts = None
                self.ipsystemstatsdiscontinuitytime = None
                self.ipsystemstatsrefreshrate = None
                self._segment_path = lambda: "ipSystemStatsEntry" + "[ipSystemStatsIPVersion='" + str(self.ipsystemstatsipversion) + "']"
                self._absolute_path = lambda: "IP-MIB:IP-MIB/ipSystemStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMIB.Ipsystemstatstable.Ipsystemstatsentry, ['ipsystemstatsipversion', 'ipsystemstatsinreceives', 'ipsystemstatshcinreceives', 'ipsystemstatsinoctets', 'ipsystemstatshcinoctets', 'ipsystemstatsinhdrerrors', 'ipsystemstatsinnoroutes', 'ipsystemstatsinaddrerrors', 'ipsystemstatsinunknownprotos', 'ipsystemstatsintruncatedpkts', 'ipsystemstatsinforwdatagrams', 'ipsystemstatshcinforwdatagrams', 'ipsystemstatsreasmreqds', 'ipsystemstatsreasmoks', 'ipsystemstatsreasmfails', 'ipsystemstatsindiscards', 'ipsystemstatsindelivers', 'ipsystemstatshcindelivers', 'ipsystemstatsoutrequests', 'ipsystemstatshcoutrequests', 'ipsystemstatsoutnoroutes', 'ipsystemstatsoutforwdatagrams', 'ipsystemstatshcoutforwdatagrams', 'ipsystemstatsoutdiscards', 'ipsystemstatsoutfragreqds', 'ipsystemstatsoutfragoks', 'ipsystemstatsoutfragfails', 'ipsystemstatsoutfragcreates', 'ipsystemstatsouttransmits', 'ipsystemstatshcouttransmits', 'ipsystemstatsoutoctets', 'ipsystemstatshcoutoctets', 'ipsystemstatsinmcastpkts', 'ipsystemstatshcinmcastpkts', 'ipsystemstatsinmcastoctets', 'ipsystemstatshcinmcastoctets', 'ipsystemstatsoutmcastpkts', 'ipsystemstatshcoutmcastpkts', 'ipsystemstatsoutmcastoctets', 'ipsystemstatshcoutmcastoctets', 'ipsystemstatsinbcastpkts', 'ipsystemstatshcinbcastpkts', 'ipsystemstatsoutbcastpkts', 'ipsystemstatshcoutbcastpkts', 'ipsystemstatsdiscontinuitytime', 'ipsystemstatsrefreshrate'], name, value)


    class Ipifstatstable(Entity):
        """
        The table containing per\-interface traffic statistics.  This
        table and the ipSystemStatsTable contain similar objects
        whose difference is in their granularity.  Where this table
        contains per\-interface statistics, the ipSystemStatsTable
        contains the same statistics, but counted on a system wide
        basis.
        
        .. attribute:: ipifstatsentry
        
        	An interface statistics entry containing objects for a particular interface and version of IP
        	**type**\: list of  		 :py:class:`Ipifstatsentry <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipifstatstable.Ipifstatsentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IPMIB.Ipifstatstable, self).__init__()

            self.yang_name = "ipIfStatsTable"
            self.yang_parent_name = "IP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ipIfStatsEntry", ("ipifstatsentry", IPMIB.Ipifstatstable.Ipifstatsentry))])
            self._leafs = OrderedDict()

            self.ipifstatsentry = YList(self)
            self._segment_path = lambda: "ipIfStatsTable"
            self._absolute_path = lambda: "IP-MIB:IP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMIB.Ipifstatstable, [], name, value)


        class Ipifstatsentry(Entity):
            """
            An interface statistics entry containing objects for a
            particular interface and version of IP.
            
            .. attribute:: ipifstatsipversion  (key)
            
            	The IP version of this row
            	**type**\:  :py:class:`IpVersion <ydk.models.ietf.ietf_inet_types.IpVersion>`
            
            .. attribute:: ipifstatsifindex  (key)
            
            	The index value that uniquely identifies the interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipifstatsinreceives
            
            	The total number of input IP datagrams received, including those received in error.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatshcinreceives
            
            	The total number of input IP datagrams received, including those received in error.  This object counts the same datagrams as ipIfStatsInReceives, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatsinoctets
            
            	The total number of octets received in input IP datagrams, including those received in error.  Octets from datagrams counted in ipIfStatsInReceives MUST be counted here.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatshcinoctets
            
            	The total number of octets received in input IP datagrams, including those received in error.  This object counts the same octets as ipIfStatsInOctets, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatsinhdrerrors
            
            	The number of input IP datagrams discarded due to errors in their IP headers, including version number mismatch, other format errors, hop count exceeded, errors discovered in processing their IP options, etc.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsinnoroutes
            
            	The number of input IP datagrams discarded because no route could be found to transmit them to their destination.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsinaddrerrors
            
            	The number of input IP datagrams discarded because the IP address in their IP header's destination field was not a valid address to be received at this entity.  This count includes invalid addresses (e.g., \:\:0).  For entities that are not IP routers and therefore do not forward datagrams, this counter includes datagrams discarded because the destination address was not a local address.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsinunknownprotos
            
            	The number of locally\-addressed IP datagrams received successfully but discarded because of an unknown or unsupported protocol.  When tracking interface statistics, the counter of the interface to which these datagrams were addressed is incremented.  This interface might not be the same as the input interface for some of the datagrams.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of   ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsintruncatedpkts
            
            	The number of input IP datagrams discarded because the datagram frame didn't carry enough data.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsinforwdatagrams
            
            	The number of input datagrams for which this entity was not their final IP destination and for which this entity attempted to find a route to forward them to that final destination.  In entities that do not act as IP routers, this counter will include only those datagrams that were Source\-Routed via this entity, and the Source\-Route processing was successful.  When tracking interface statistics, the counter of the incoming interface is incremented for each datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatshcinforwdatagrams
            
            	The number of input datagrams for which this entity was not their final IP destination and for which this entity attempted to find a route to forward them to that final destination.  This object counts the same packets as   ipIfStatsInForwDatagrams, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatsreasmreqds
            
            	The number of IP fragments received that needed to be reassembled at this interface.  When tracking interface statistics, the counter of the interface to which these fragments were addressed is incremented.  This interface might not be the same as the input interface for some of the fragments.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsreasmoks
            
            	The number of IP datagrams successfully reassembled.  When tracking interface statistics, the counter of the interface to which these datagrams were addressed is incremented.  This interface might not be the same as the input interface for some of the datagrams.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsreasmfails
            
            	The number of failures detected by the IP re\-assembly algorithm (for whatever reason\: timed out, errors, etc.). Note that this is not necessarily a count of discarded IP fragments since some algorithms (notably the algorithm in RFC 815) can lose track of the number of fragments by combining them as they are received.  When tracking interface statistics, the counter of the interface to which these fragments were addressed is incremented.  This interface might not be the same as the input interface for some of the fragments.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsindiscards
            
            	The number of input IP datagrams for which no problems were encountered to prevent their continued processing, but were discarded (e.g., for lack of buffer space).  Note that this counter does not include any datagrams discarded while awaiting re\-assembly.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsindelivers
            
            	The total number of datagrams successfully delivered to IP user\-protocols (including ICMP).  When tracking interface statistics, the counter of the interface to which these datagrams were addressed is incremented.  This interface might not be the same as the   input interface for some of the datagrams.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatshcindelivers
            
            	The total number of datagrams successfully delivered to IP user\-protocols (including ICMP).  This object counts the same packets as ipIfStatsInDelivers, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatsoutrequests
            
            	The total number of IP datagrams that local IP user\- protocols (including ICMP) supplied to IP in requests for transmission.  Note that this counter does not include any datagrams counted in ipIfStatsOutForwDatagrams.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatshcoutrequests
            
            	The total number of IP datagrams that local IP user\- protocols (including ICMP) supplied to IP in requests for transmission.  This object counts the same packets as   ipIfStatsOutRequests, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatsoutforwdatagrams
            
            	The number of datagrams for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination.  In entities that do not act as IP routers, this counter will include only those datagrams that were Source\-Routed via this entity, and the Source\-Route processing was successful.  When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully forwarded datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatshcoutforwdatagrams
            
            	The number of datagrams for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination.  This object counts the same packets as ipIfStatsOutForwDatagrams, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of   ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatsoutdiscards
            
            	The number of output IP datagrams for which no problem was encountered to prevent their transmission to their destination, but were discarded (e.g., for lack of buffer space).  Note that this counter would include datagrams counted in ipIfStatsOutForwDatagrams if any such datagrams met this (discretionary) discard criterion.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsoutfragreqds
            
            	The number of IP datagrams that would require fragmentation in order to be transmitted.  When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully fragmented datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsoutfragoks
            
            	The number of IP datagrams that have been successfully fragmented.  When tracking interface statistics, the counter of the   outgoing interface is incremented for a successfully fragmented datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsoutfragfails
            
            	The number of IP datagrams that have been discarded because they needed to be fragmented but could not be.  This includes IPv4 packets that have the DF bit set and IPv6 packets that are being forwarded and exceed the outgoing link MTU.  When tracking interface statistics, the counter of the outgoing interface is incremented for an unsuccessfully fragmented datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsoutfragcreates
            
            	The number of output datagram fragments that have been generated as a result of IP fragmentation.  When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully fragmented datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsouttransmits
            
            	The total number of IP datagrams that this entity supplied to the lower layers for transmission.  This includes datagrams generated locally and those forwarded by this entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatshcouttransmits
            
            	The total number of IP datagrams that this entity supplied to the lower layers for transmission.  This object counts the same datagrams as ipIfStatsOutTransmits, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatsoutoctets
            
            	The total number of octets in IP datagrams delivered to the lower layers for transmission.  Octets from datagrams counted in ipIfStatsOutTransmits MUST be counted here.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatshcoutoctets
            
            	The total number of octets in IP datagrams delivered to the lower layers for transmission.  This objects counts the same octets as ipIfStatsOutOctets, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatsinmcastpkts
            
            	The number of IP multicast datagrams received.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatshcinmcastpkts
            
            	The number of IP multicast datagrams received.  This object counts the same datagrams as ipIfStatsInMcastPkts, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatsinmcastoctets
            
            	The total number of octets received in IP multicast   datagrams.  Octets from datagrams counted in ipIfStatsInMcastPkts MUST be counted here.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatshcinmcastoctets
            
            	The total number of octets received in IP multicast datagrams.  This object counts the same octets as ipIfStatsInMcastOctets, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatsoutmcastpkts
            
            	The number of IP multicast datagrams transmitted.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatshcoutmcastpkts
            
            	The number of IP multicast datagrams transmitted.  This object counts the same datagrams as ipIfStatsOutMcastPkts, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other   times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatsoutmcastoctets
            
            	The total number of octets transmitted in IP multicast datagrams.  Octets from datagrams counted in ipIfStatsOutMcastPkts MUST be counted here.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatshcoutmcastoctets
            
            	The total number of octets transmitted in IP multicast datagrams.  This object counts the same octets as ipIfStatsOutMcastOctets, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatsinbcastpkts
            
            	The number of IP broadcast datagrams received.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatshcinbcastpkts
            
            	The number of IP broadcast datagrams received.  This object counts the same datagrams as ipIfStatsInBcastPkts, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatsoutbcastpkts
            
            	The number of IP broadcast datagrams transmitted.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatshcoutbcastpkts
            
            	The number of IP broadcast datagrams transmitted.  This object counts the same datagrams as ipIfStatsOutBcastPkts, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatsdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which   any one or more of this entry's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\- initialization of the local management subsystem, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsrefreshrate
            
            	The minimum reasonable polling interval for this entry. This object provides an indication of the minimum amount of time required to update the counters in this entry
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milli-seconds
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IPMIB.Ipifstatstable.Ipifstatsentry, self).__init__()

                self.yang_name = "ipIfStatsEntry"
                self.yang_parent_name = "ipIfStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipifstatsipversion','ipifstatsifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipifstatsipversion', YLeaf(YType.enumeration, 'ipIfStatsIPVersion')),
                    ('ipifstatsifindex', YLeaf(YType.int32, 'ipIfStatsIfIndex')),
                    ('ipifstatsinreceives', YLeaf(YType.uint32, 'ipIfStatsInReceives')),
                    ('ipifstatshcinreceives', YLeaf(YType.uint64, 'ipIfStatsHCInReceives')),
                    ('ipifstatsinoctets', YLeaf(YType.uint32, 'ipIfStatsInOctets')),
                    ('ipifstatshcinoctets', YLeaf(YType.uint64, 'ipIfStatsHCInOctets')),
                    ('ipifstatsinhdrerrors', YLeaf(YType.uint32, 'ipIfStatsInHdrErrors')),
                    ('ipifstatsinnoroutes', YLeaf(YType.uint32, 'ipIfStatsInNoRoutes')),
                    ('ipifstatsinaddrerrors', YLeaf(YType.uint32, 'ipIfStatsInAddrErrors')),
                    ('ipifstatsinunknownprotos', YLeaf(YType.uint32, 'ipIfStatsInUnknownProtos')),
                    ('ipifstatsintruncatedpkts', YLeaf(YType.uint32, 'ipIfStatsInTruncatedPkts')),
                    ('ipifstatsinforwdatagrams', YLeaf(YType.uint32, 'ipIfStatsInForwDatagrams')),
                    ('ipifstatshcinforwdatagrams', YLeaf(YType.uint64, 'ipIfStatsHCInForwDatagrams')),
                    ('ipifstatsreasmreqds', YLeaf(YType.uint32, 'ipIfStatsReasmReqds')),
                    ('ipifstatsreasmoks', YLeaf(YType.uint32, 'ipIfStatsReasmOKs')),
                    ('ipifstatsreasmfails', YLeaf(YType.uint32, 'ipIfStatsReasmFails')),
                    ('ipifstatsindiscards', YLeaf(YType.uint32, 'ipIfStatsInDiscards')),
                    ('ipifstatsindelivers', YLeaf(YType.uint32, 'ipIfStatsInDelivers')),
                    ('ipifstatshcindelivers', YLeaf(YType.uint64, 'ipIfStatsHCInDelivers')),
                    ('ipifstatsoutrequests', YLeaf(YType.uint32, 'ipIfStatsOutRequests')),
                    ('ipifstatshcoutrequests', YLeaf(YType.uint64, 'ipIfStatsHCOutRequests')),
                    ('ipifstatsoutforwdatagrams', YLeaf(YType.uint32, 'ipIfStatsOutForwDatagrams')),
                    ('ipifstatshcoutforwdatagrams', YLeaf(YType.uint64, 'ipIfStatsHCOutForwDatagrams')),
                    ('ipifstatsoutdiscards', YLeaf(YType.uint32, 'ipIfStatsOutDiscards')),
                    ('ipifstatsoutfragreqds', YLeaf(YType.uint32, 'ipIfStatsOutFragReqds')),
                    ('ipifstatsoutfragoks', YLeaf(YType.uint32, 'ipIfStatsOutFragOKs')),
                    ('ipifstatsoutfragfails', YLeaf(YType.uint32, 'ipIfStatsOutFragFails')),
                    ('ipifstatsoutfragcreates', YLeaf(YType.uint32, 'ipIfStatsOutFragCreates')),
                    ('ipifstatsouttransmits', YLeaf(YType.uint32, 'ipIfStatsOutTransmits')),
                    ('ipifstatshcouttransmits', YLeaf(YType.uint64, 'ipIfStatsHCOutTransmits')),
                    ('ipifstatsoutoctets', YLeaf(YType.uint32, 'ipIfStatsOutOctets')),
                    ('ipifstatshcoutoctets', YLeaf(YType.uint64, 'ipIfStatsHCOutOctets')),
                    ('ipifstatsinmcastpkts', YLeaf(YType.uint32, 'ipIfStatsInMcastPkts')),
                    ('ipifstatshcinmcastpkts', YLeaf(YType.uint64, 'ipIfStatsHCInMcastPkts')),
                    ('ipifstatsinmcastoctets', YLeaf(YType.uint32, 'ipIfStatsInMcastOctets')),
                    ('ipifstatshcinmcastoctets', YLeaf(YType.uint64, 'ipIfStatsHCInMcastOctets')),
                    ('ipifstatsoutmcastpkts', YLeaf(YType.uint32, 'ipIfStatsOutMcastPkts')),
                    ('ipifstatshcoutmcastpkts', YLeaf(YType.uint64, 'ipIfStatsHCOutMcastPkts')),
                    ('ipifstatsoutmcastoctets', YLeaf(YType.uint32, 'ipIfStatsOutMcastOctets')),
                    ('ipifstatshcoutmcastoctets', YLeaf(YType.uint64, 'ipIfStatsHCOutMcastOctets')),
                    ('ipifstatsinbcastpkts', YLeaf(YType.uint32, 'ipIfStatsInBcastPkts')),
                    ('ipifstatshcinbcastpkts', YLeaf(YType.uint64, 'ipIfStatsHCInBcastPkts')),
                    ('ipifstatsoutbcastpkts', YLeaf(YType.uint32, 'ipIfStatsOutBcastPkts')),
                    ('ipifstatshcoutbcastpkts', YLeaf(YType.uint64, 'ipIfStatsHCOutBcastPkts')),
                    ('ipifstatsdiscontinuitytime', YLeaf(YType.uint32, 'ipIfStatsDiscontinuityTime')),
                    ('ipifstatsrefreshrate', YLeaf(YType.uint32, 'ipIfStatsRefreshRate')),
                ])
                self.ipifstatsipversion = None
                self.ipifstatsifindex = None
                self.ipifstatsinreceives = None
                self.ipifstatshcinreceives = None
                self.ipifstatsinoctets = None
                self.ipifstatshcinoctets = None
                self.ipifstatsinhdrerrors = None
                self.ipifstatsinnoroutes = None
                self.ipifstatsinaddrerrors = None
                self.ipifstatsinunknownprotos = None
                self.ipifstatsintruncatedpkts = None
                self.ipifstatsinforwdatagrams = None
                self.ipifstatshcinforwdatagrams = None
                self.ipifstatsreasmreqds = None
                self.ipifstatsreasmoks = None
                self.ipifstatsreasmfails = None
                self.ipifstatsindiscards = None
                self.ipifstatsindelivers = None
                self.ipifstatshcindelivers = None
                self.ipifstatsoutrequests = None
                self.ipifstatshcoutrequests = None
                self.ipifstatsoutforwdatagrams = None
                self.ipifstatshcoutforwdatagrams = None
                self.ipifstatsoutdiscards = None
                self.ipifstatsoutfragreqds = None
                self.ipifstatsoutfragoks = None
                self.ipifstatsoutfragfails = None
                self.ipifstatsoutfragcreates = None
                self.ipifstatsouttransmits = None
                self.ipifstatshcouttransmits = None
                self.ipifstatsoutoctets = None
                self.ipifstatshcoutoctets = None
                self.ipifstatsinmcastpkts = None
                self.ipifstatshcinmcastpkts = None
                self.ipifstatsinmcastoctets = None
                self.ipifstatshcinmcastoctets = None
                self.ipifstatsoutmcastpkts = None
                self.ipifstatshcoutmcastpkts = None
                self.ipifstatsoutmcastoctets = None
                self.ipifstatshcoutmcastoctets = None
                self.ipifstatsinbcastpkts = None
                self.ipifstatshcinbcastpkts = None
                self.ipifstatsoutbcastpkts = None
                self.ipifstatshcoutbcastpkts = None
                self.ipifstatsdiscontinuitytime = None
                self.ipifstatsrefreshrate = None
                self._segment_path = lambda: "ipIfStatsEntry" + "[ipIfStatsIPVersion='" + str(self.ipifstatsipversion) + "']" + "[ipIfStatsIfIndex='" + str(self.ipifstatsifindex) + "']"
                self._absolute_path = lambda: "IP-MIB:IP-MIB/ipIfStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMIB.Ipifstatstable.Ipifstatsentry, ['ipifstatsipversion', 'ipifstatsifindex', 'ipifstatsinreceives', 'ipifstatshcinreceives', 'ipifstatsinoctets', 'ipifstatshcinoctets', 'ipifstatsinhdrerrors', 'ipifstatsinnoroutes', 'ipifstatsinaddrerrors', 'ipifstatsinunknownprotos', 'ipifstatsintruncatedpkts', 'ipifstatsinforwdatagrams', 'ipifstatshcinforwdatagrams', 'ipifstatsreasmreqds', 'ipifstatsreasmoks', 'ipifstatsreasmfails', 'ipifstatsindiscards', 'ipifstatsindelivers', 'ipifstatshcindelivers', 'ipifstatsoutrequests', 'ipifstatshcoutrequests', 'ipifstatsoutforwdatagrams', 'ipifstatshcoutforwdatagrams', 'ipifstatsoutdiscards', 'ipifstatsoutfragreqds', 'ipifstatsoutfragoks', 'ipifstatsoutfragfails', 'ipifstatsoutfragcreates', 'ipifstatsouttransmits', 'ipifstatshcouttransmits', 'ipifstatsoutoctets', 'ipifstatshcoutoctets', 'ipifstatsinmcastpkts', 'ipifstatshcinmcastpkts', 'ipifstatsinmcastoctets', 'ipifstatshcinmcastoctets', 'ipifstatsoutmcastpkts', 'ipifstatshcoutmcastpkts', 'ipifstatsoutmcastoctets', 'ipifstatshcoutmcastoctets', 'ipifstatsinbcastpkts', 'ipifstatshcinbcastpkts', 'ipifstatsoutbcastpkts', 'ipifstatshcoutbcastpkts', 'ipifstatsdiscontinuitytime', 'ipifstatsrefreshrate'], name, value)


    class Ipaddressprefixtable(Entity):
        """
        This table allows the user to determine the source of an IP
        address or set of IP addresses, and allows other tables to
        share the information via pointer rather than by copying.
        
        For example, when the node configures both a unicast and
        anycast address for a prefix, the ipAddressPrefix objects
        for those addresses will point to a single row in this
        table.
        
        This table primarily provides support for IPv6 prefixes, and
        several of the objects are less meaningful for IPv4.  The
        table continues to allow IPv4 addresses to allow future
        flexibility.  In order to promote a common configuration,
        this document includes suggestions for default values for
        IPv4 prefixes.  Each of these values may be overridden if an
        object is meaningful to the node.
        
        All prefixes used by this entity should be included in this
        table independent of how the entity learned the prefix.
        (This table isn't limited to prefixes learned from router
        
        
        advertisements.)
        
        .. attribute:: ipaddressprefixentry
        
        	An entry in the ipAddressPrefixTable
        	**type**\: list of  		 :py:class:`Ipaddressprefixentry <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipaddressprefixtable.Ipaddressprefixentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IPMIB.Ipaddressprefixtable, self).__init__()

            self.yang_name = "ipAddressPrefixTable"
            self.yang_parent_name = "IP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ipAddressPrefixEntry", ("ipaddressprefixentry", IPMIB.Ipaddressprefixtable.Ipaddressprefixentry))])
            self._leafs = OrderedDict()

            self.ipaddressprefixentry = YList(self)
            self._segment_path = lambda: "ipAddressPrefixTable"
            self._absolute_path = lambda: "IP-MIB:IP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMIB.Ipaddressprefixtable, [], name, value)


        class Ipaddressprefixentry(Entity):
            """
            An entry in the ipAddressPrefixTable.
            
            .. attribute:: ipaddressprefixifindex  (key)
            
            	The index value that uniquely identifies the interface on which this prefix is configured.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipaddressprefixtype  (key)
            
            	The address type of ipAddressPrefix
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: ipaddressprefixprefix  (key)
            
            	The address prefix.  The address type of this object is specified in ipAddressPrefixType.  The length of this object is the standard length for objects of that type (4 or 16 bytes).  Any bits after ipAddressPrefixLength must be zero.  Implementors need to be aware that, if the size of ipAddressPrefixPrefix exceeds 114 octets, then OIDS of instances of columns in this row will have more than 128 sub\-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: ipaddressprefixlength  (key)
            
            	The prefix length associated with this prefix.  The value 0 has no special meaning for this object.  It simply refers to address '\:\:/0'
            	**type**\: int
            
            	**range:** 0..2040
            
            .. attribute:: ipaddressprefixorigin
            
            	The origin of this prefix
            	**type**\:  :py:class:`IpAddressPrefixOriginTC <ydk.models.cisco_ios_xe.IP_MIB.IpAddressPrefixOriginTC>`
            
            .. attribute:: ipaddressprefixonlinkflag
            
            	This object has the value 'true(1)', if this prefix can be used for on\-link determination; otherwise, the value is 'false(2)'.  The default for IPv4 prefixes is 'true(1)'
            	**type**\: bool
            
            .. attribute:: ipaddressprefixautonomousflag
            
            	Autonomous address configuration flag.  When true(1), indicates that this prefix can be used for autonomous address configuration (i.e., can be used to form a local interface address).  If false(2), it is not used to auto\- configure a local interface address.  The default for IPv4 prefixes is 'false(2)'
            	**type**\: bool
            
            .. attribute:: ipaddressprefixadvpreferredlifetime
            
            	The remaining length of time, in seconds, that this prefix will continue to be preferred, i.e., time until deprecation.  A value of 4,294,967,295 represents infinity.  The address generated from a deprecated prefix should no longer be used as a source address in new communications, but packets received on such an interface are processed as expected.  The default for IPv4 prefixes is 4,294,967,295 (infinity)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: ipaddressprefixadvvalidlifetime
            
            	The remaining length of time, in seconds, that this prefix will continue to be valid, i.e., time until invalidation.  A value of 4,294,967,295 represents infinity.  The address generated from an invalidated prefix should not appear as the destination or source address of a packet.   The default for IPv4 prefixes is 4,294,967,295 (infinity)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IPMIB.Ipaddressprefixtable.Ipaddressprefixentry, self).__init__()

                self.yang_name = "ipAddressPrefixEntry"
                self.yang_parent_name = "ipAddressPrefixTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipaddressprefixifindex','ipaddressprefixtype','ipaddressprefixprefix','ipaddressprefixlength']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipaddressprefixifindex', YLeaf(YType.int32, 'ipAddressPrefixIfIndex')),
                    ('ipaddressprefixtype', YLeaf(YType.enumeration, 'ipAddressPrefixType')),
                    ('ipaddressprefixprefix', YLeaf(YType.str, 'ipAddressPrefixPrefix')),
                    ('ipaddressprefixlength', YLeaf(YType.uint32, 'ipAddressPrefixLength')),
                    ('ipaddressprefixorigin', YLeaf(YType.enumeration, 'ipAddressPrefixOrigin')),
                    ('ipaddressprefixonlinkflag', YLeaf(YType.boolean, 'ipAddressPrefixOnLinkFlag')),
                    ('ipaddressprefixautonomousflag', YLeaf(YType.boolean, 'ipAddressPrefixAutonomousFlag')),
                    ('ipaddressprefixadvpreferredlifetime', YLeaf(YType.uint32, 'ipAddressPrefixAdvPreferredLifetime')),
                    ('ipaddressprefixadvvalidlifetime', YLeaf(YType.uint32, 'ipAddressPrefixAdvValidLifetime')),
                ])
                self.ipaddressprefixifindex = None
                self.ipaddressprefixtype = None
                self.ipaddressprefixprefix = None
                self.ipaddressprefixlength = None
                self.ipaddressprefixorigin = None
                self.ipaddressprefixonlinkflag = None
                self.ipaddressprefixautonomousflag = None
                self.ipaddressprefixadvpreferredlifetime = None
                self.ipaddressprefixadvvalidlifetime = None
                self._segment_path = lambda: "ipAddressPrefixEntry" + "[ipAddressPrefixIfIndex='" + str(self.ipaddressprefixifindex) + "']" + "[ipAddressPrefixType='" + str(self.ipaddressprefixtype) + "']" + "[ipAddressPrefixPrefix='" + str(self.ipaddressprefixprefix) + "']" + "[ipAddressPrefixLength='" + str(self.ipaddressprefixlength) + "']"
                self._absolute_path = lambda: "IP-MIB:IP-MIB/ipAddressPrefixTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMIB.Ipaddressprefixtable.Ipaddressprefixentry, ['ipaddressprefixifindex', 'ipaddressprefixtype', 'ipaddressprefixprefix', 'ipaddressprefixlength', 'ipaddressprefixorigin', 'ipaddressprefixonlinkflag', 'ipaddressprefixautonomousflag', 'ipaddressprefixadvpreferredlifetime', 'ipaddressprefixadvvalidlifetime'], name, value)


    class Ipaddresstable(Entity):
        """
        This table contains addressing information relevant to the
        entity's interfaces.
        
        This table does not contain multicast address information.
        Tables for such information should be contained in multicast
        specific MIBs, such as RFC 3019.
        
        While this table is writable, the user will note that
        several objects, such as ipAddressOrigin, are not.  The
        intention in allowing a user to write to this table is to
        allow them to add or remove any entry that isn't
        
        
        permanent.  The user should be allowed to modify objects
        and entries when that would not cause inconsistencies
        within the table.  Allowing write access to objects, such
        as ipAddressOrigin, could allow a user to insert an entry
        and then label it incorrectly.
        
        Note well\: When including IPv6 link\-local addresses in this
        table, the entry must use an InetAddressType of 'ipv6z' in
        order to differentiate between the possible interfaces.
        
        .. attribute:: ipaddressentry
        
        	An address mapping for a particular interface
        	**type**\: list of  		 :py:class:`Ipaddressentry <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipaddresstable.Ipaddressentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IPMIB.Ipaddresstable, self).__init__()

            self.yang_name = "ipAddressTable"
            self.yang_parent_name = "IP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ipAddressEntry", ("ipaddressentry", IPMIB.Ipaddresstable.Ipaddressentry))])
            self._leafs = OrderedDict()

            self.ipaddressentry = YList(self)
            self._segment_path = lambda: "ipAddressTable"
            self._absolute_path = lambda: "IP-MIB:IP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMIB.Ipaddresstable, [], name, value)


        class Ipaddressentry(Entity):
            """
            An address mapping for a particular interface.
            
            .. attribute:: ipaddressaddrtype  (key)
            
            	The address type of ipAddressAddr
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: ipaddressaddr  (key)
            
            	The IP address to which this entry's addressing information   pertains.  The address type of this object is specified in ipAddressAddrType.  Implementors need to be aware that if the size of ipAddressAddr exceeds 116 octets, then OIDS of instances of columns in this row will have more than 128 sub\-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: ipaddressifindex
            
            	The index value that uniquely identifies the interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipaddresstype
            
            	The type of address.  broadcast(3) is not a valid value for IPv6 addresses (RFC 3513)
            	**type**\:  :py:class:`Ipaddresstype <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipaddresstable.Ipaddressentry.Ipaddresstype>`
            
            .. attribute:: ipaddressprefix
            
            	A pointer to the row in the prefix table to which this address belongs.  May be { 0 0 } if there is no such row
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: ipaddressorigin
            
            	The origin of the address
            	**type**\:  :py:class:`IpAddressOriginTC <ydk.models.cisco_ios_xe.IP_MIB.IpAddressOriginTC>`
            
            .. attribute:: ipaddressstatus
            
            	The status of the address, describing if the address can be used for communication.  In the absence of other information, an IPv4 address is always preferred(1)
            	**type**\:  :py:class:`IpAddressStatusTC <ydk.models.cisco_ios_xe.IP_MIB.IpAddressStatusTC>`
            
            .. attribute:: ipaddresscreated
            
            	The value of sysUpTime at the time this entry was created. If this entry was created prior to the last re\- initialization of the local network management subsystem, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipaddresslastchanged
            
            	The value of sysUpTime at the time this entry was last updated.  If this entry was updated prior to the last re\- initialization of the local network management subsystem, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipaddressrowstatus
            
            	The status of this conceptual row.  The RowStatus TC requires that this DESCRIPTION clause states under which circumstances other objects in this row   can be modified.  The value of this object has no effect on whether other objects in this conceptual row can be modified.  A conceptual row can not be made active until the ipAddressIfIndex has been set to a valid index
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            .. attribute:: ipaddressstoragetype
            
            	The storage type for this conceptual row.  If this object has a value of 'permanent', then no other objects are required to be able to be modified
            	**type**\:  :py:class:`StorageType <ydk.models.cisco_ios_xe.SNMPv2_TC.StorageType>`
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IPMIB.Ipaddresstable.Ipaddressentry, self).__init__()

                self.yang_name = "ipAddressEntry"
                self.yang_parent_name = "ipAddressTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipaddressaddrtype','ipaddressaddr']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipaddressaddrtype', YLeaf(YType.enumeration, 'ipAddressAddrType')),
                    ('ipaddressaddr', YLeaf(YType.str, 'ipAddressAddr')),
                    ('ipaddressifindex', YLeaf(YType.int32, 'ipAddressIfIndex')),
                    ('ipaddresstype', YLeaf(YType.enumeration, 'ipAddressType')),
                    ('ipaddressprefix', YLeaf(YType.str, 'ipAddressPrefix')),
                    ('ipaddressorigin', YLeaf(YType.enumeration, 'ipAddressOrigin')),
                    ('ipaddressstatus', YLeaf(YType.enumeration, 'ipAddressStatus')),
                    ('ipaddresscreated', YLeaf(YType.uint32, 'ipAddressCreated')),
                    ('ipaddresslastchanged', YLeaf(YType.uint32, 'ipAddressLastChanged')),
                    ('ipaddressrowstatus', YLeaf(YType.enumeration, 'ipAddressRowStatus')),
                    ('ipaddressstoragetype', YLeaf(YType.enumeration, 'ipAddressStorageType')),
                ])
                self.ipaddressaddrtype = None
                self.ipaddressaddr = None
                self.ipaddressifindex = None
                self.ipaddresstype = None
                self.ipaddressprefix = None
                self.ipaddressorigin = None
                self.ipaddressstatus = None
                self.ipaddresscreated = None
                self.ipaddresslastchanged = None
                self.ipaddressrowstatus = None
                self.ipaddressstoragetype = None
                self._segment_path = lambda: "ipAddressEntry" + "[ipAddressAddrType='" + str(self.ipaddressaddrtype) + "']" + "[ipAddressAddr='" + str(self.ipaddressaddr) + "']"
                self._absolute_path = lambda: "IP-MIB:IP-MIB/ipAddressTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMIB.Ipaddresstable.Ipaddressentry, ['ipaddressaddrtype', 'ipaddressaddr', 'ipaddressifindex', 'ipaddresstype', 'ipaddressprefix', 'ipaddressorigin', 'ipaddressstatus', 'ipaddresscreated', 'ipaddresslastchanged', 'ipaddressrowstatus', 'ipaddressstoragetype'], name, value)

            class Ipaddresstype(Enum):
                """
                Ipaddresstype (Enum Class)

                The type of address.  broadcast(3) is not a valid value for

                IPv6 addresses (RFC 3513).

                .. data:: unicast = 1

                .. data:: anycast = 2

                .. data:: broadcast = 3

                """

                unicast = Enum.YLeaf(1, "unicast")

                anycast = Enum.YLeaf(2, "anycast")

                broadcast = Enum.YLeaf(3, "broadcast")



    class Ipnettophysicaltable(Entity):
        """
        The IP Address Translation table used for mapping from IP
        addresses to physical addresses.
        
        The Address Translation tables contain the IP address to
        'physical' address equivalences.  Some interfaces do not use
        translation tables for determining address equivalences
        (e.g., DDN\-X.25 has an algorithmic method); if all
        interfaces are of this type, then the Address Translation
        table is empty, i.e., has zero entries.
        
        While many protocols may be used to populate this table, ARP
        and Neighbor Discovery are the most likely
        options.
        
        .. attribute:: ipnettophysicalentry
        
        	Each entry contains one IP address to `physical' address equivalence
        	**type**\: list of  		 :py:class:`Ipnettophysicalentry <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipnettophysicaltable.Ipnettophysicalentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IPMIB.Ipnettophysicaltable, self).__init__()

            self.yang_name = "ipNetToPhysicalTable"
            self.yang_parent_name = "IP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ipNetToPhysicalEntry", ("ipnettophysicalentry", IPMIB.Ipnettophysicaltable.Ipnettophysicalentry))])
            self._leafs = OrderedDict()

            self.ipnettophysicalentry = YList(self)
            self._segment_path = lambda: "ipNetToPhysicalTable"
            self._absolute_path = lambda: "IP-MIB:IP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMIB.Ipnettophysicaltable, [], name, value)


        class Ipnettophysicalentry(Entity):
            """
            Each entry contains one IP address to `physical' address
            equivalence.
            
            .. attribute:: ipnettophysicalifindex  (key)
            
            	The index value that uniquely identifies the interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipnettophysicalnetaddresstype  (key)
            
            	The type of ipNetToPhysicalNetAddress
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: ipnettophysicalnetaddress  (key)
            
            	The IP Address corresponding to the media\-dependent `physical' address.  The address type of this object is specified in ipNetToPhysicalAddressType.  Implementors need to be aware that if the size of   ipNetToPhysicalNetAddress exceeds 115 octets, then OIDS of instances of columns in this row will have more than 128 sub\-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: ipnettophysicalphysaddress
            
            	The media\-dependent `physical' address.  As the entries in this table are typically not persistent when this object is written the entity SHOULD NOT save the change to non\-volatile storage
            	**type**\: str
            
            	**length:** 0..65535
            
            .. attribute:: ipnettophysicallastupdated
            
            	The value of sysUpTime at the time this entry was last updated.  If this entry was updated prior to the last re\- initialization of the local network management subsystem, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipnettophysicaltype
            
            	The type of mapping.  Setting this object to the value invalid(2) has the effect of invalidating the corresponding entry in the ipNetToPhysicalTable.  That is, it effectively dis\- associates the interface identified with said entry from the mapping identified with said entry.  It is an implementation\-specific matter as to whether the agent   removes an invalidated entry from the table.  Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use.  Proper interpretation of such entries requires examination of the relevant ipNetToPhysicalType object.  The 'dynamic(3)' type indicates that the IP address to physical addresses mapping has been dynamically resolved using e.g., IPv4 ARP or the IPv6 Neighbor Discovery protocol.  The 'static(4)' type indicates that the mapping has been statically configured.  Both of these refer to entries that provide mappings for other entities addresses.  The 'local(5)' type indicates that the mapping is provided for an entity's own interface address.  As the entries in this table are typically not persistent when this object is written the entity SHOULD NOT save the change to non\-volatile storage
            	**type**\:  :py:class:`Ipnettophysicaltype <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipnettophysicaltable.Ipnettophysicalentry.Ipnettophysicaltype>`
            
            .. attribute:: ipnettophysicalstate
            
            	The Neighbor Unreachability Detection state for the interface when the address mapping in this entry is used. If Neighbor Unreachability Detection is not in use (e.g. for IPv4), this object is always unknown(6)
            	**type**\:  :py:class:`Ipnettophysicalstate <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipnettophysicaltable.Ipnettophysicalentry.Ipnettophysicalstate>`
            
            .. attribute:: ipnettophysicalrowstatus
            
            	The status of this conceptual row.  The RowStatus TC requires that this DESCRIPTION clause states under which circumstances other objects in this row can be modified.  The value of this object has no effect on whether other objects in this conceptual row can be modified.  A conceptual row can not be made active until the ipNetToPhysicalPhysAddress object has been set.  Note that if the ipNetToPhysicalType is set to 'invalid', the managed node may delete the entry independent of the state of this object
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IPMIB.Ipnettophysicaltable.Ipnettophysicalentry, self).__init__()

                self.yang_name = "ipNetToPhysicalEntry"
                self.yang_parent_name = "ipNetToPhysicalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipnettophysicalifindex','ipnettophysicalnetaddresstype','ipnettophysicalnetaddress']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipnettophysicalifindex', YLeaf(YType.int32, 'ipNetToPhysicalIfIndex')),
                    ('ipnettophysicalnetaddresstype', YLeaf(YType.enumeration, 'ipNetToPhysicalNetAddressType')),
                    ('ipnettophysicalnetaddress', YLeaf(YType.str, 'ipNetToPhysicalNetAddress')),
                    ('ipnettophysicalphysaddress', YLeaf(YType.str, 'ipNetToPhysicalPhysAddress')),
                    ('ipnettophysicallastupdated', YLeaf(YType.uint32, 'ipNetToPhysicalLastUpdated')),
                    ('ipnettophysicaltype', YLeaf(YType.enumeration, 'ipNetToPhysicalType')),
                    ('ipnettophysicalstate', YLeaf(YType.enumeration, 'ipNetToPhysicalState')),
                    ('ipnettophysicalrowstatus', YLeaf(YType.enumeration, 'ipNetToPhysicalRowStatus')),
                ])
                self.ipnettophysicalifindex = None
                self.ipnettophysicalnetaddresstype = None
                self.ipnettophysicalnetaddress = None
                self.ipnettophysicalphysaddress = None
                self.ipnettophysicallastupdated = None
                self.ipnettophysicaltype = None
                self.ipnettophysicalstate = None
                self.ipnettophysicalrowstatus = None
                self._segment_path = lambda: "ipNetToPhysicalEntry" + "[ipNetToPhysicalIfIndex='" + str(self.ipnettophysicalifindex) + "']" + "[ipNetToPhysicalNetAddressType='" + str(self.ipnettophysicalnetaddresstype) + "']" + "[ipNetToPhysicalNetAddress='" + str(self.ipnettophysicalnetaddress) + "']"
                self._absolute_path = lambda: "IP-MIB:IP-MIB/ipNetToPhysicalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMIB.Ipnettophysicaltable.Ipnettophysicalentry, ['ipnettophysicalifindex', 'ipnettophysicalnetaddresstype', 'ipnettophysicalnetaddress', 'ipnettophysicalphysaddress', 'ipnettophysicallastupdated', 'ipnettophysicaltype', 'ipnettophysicalstate', 'ipnettophysicalrowstatus'], name, value)

            class Ipnettophysicalstate(Enum):
                """
                Ipnettophysicalstate (Enum Class)

                The Neighbor Unreachability Detection state for the

                interface when the address mapping in this entry is used.

                If Neighbor Unreachability Detection is not in use (e.g. for

                IPv4), this object is always unknown(6).

                .. data:: reachable = 1

                .. data:: stale = 2

                .. data:: delay = 3

                .. data:: probe = 4

                .. data:: invalid = 5

                .. data:: unknown = 6

                .. data:: incomplete = 7

                """

                reachable = Enum.YLeaf(1, "reachable")

                stale = Enum.YLeaf(2, "stale")

                delay = Enum.YLeaf(3, "delay")

                probe = Enum.YLeaf(4, "probe")

                invalid = Enum.YLeaf(5, "invalid")

                unknown = Enum.YLeaf(6, "unknown")

                incomplete = Enum.YLeaf(7, "incomplete")


            class Ipnettophysicaltype(Enum):
                """
                Ipnettophysicaltype (Enum Class)

                The type of mapping.

                Setting this object to the value invalid(2) has the effect

                of invalidating the corresponding entry in the

                ipNetToPhysicalTable.  That is, it effectively dis\-

                associates the interface identified with said entry from the

                mapping identified with said entry.  It is an

                implementation\-specific matter as to whether the agent

                removes an invalidated entry from the table.  Accordingly,

                management stations must be prepared to receive tabular

                information from agents that corresponds to entries not

                currently in use.  Proper interpretation of such entries

                requires examination of the relevant ipNetToPhysicalType

                object.

                The 'dynamic(3)' type indicates that the IP address to

                physical addresses mapping has been dynamically resolved

                using e.g., IPv4 ARP or the IPv6 Neighbor Discovery

                protocol.

                The 'static(4)' type indicates that the mapping has been

                statically configured.  Both of these refer to entries that

                provide mappings for other entities addresses.

                The 'local(5)' type indicates that the mapping is provided

                for an entity's own interface address.

                As the entries in this table are typically not persistent

                when this object is written the entity SHOULD NOT save the

                change to non\-volatile storage.

                .. data:: other = 1

                .. data:: invalid = 2

                .. data:: dynamic = 3

                .. data:: static = 4

                .. data:: local = 5

                """

                other = Enum.YLeaf(1, "other")

                invalid = Enum.YLeaf(2, "invalid")

                dynamic = Enum.YLeaf(3, "dynamic")

                static = Enum.YLeaf(4, "static")

                local = Enum.YLeaf(5, "local")



    class Ipv6Scopezoneindextable(Entity):
        """
        The table used to describe IPv6 unicast and multicast scope
        zones.
        
        For those objects that have names rather than numbers, the
        names were chosen to coincide with the names used in the
        IPv6 address architecture document. 
        
        .. attribute:: ipv6scopezoneindexentry
        
        	Each entry contains the list of scope identifiers on a given interface
        	**type**\: list of  		 :py:class:`Ipv6Scopezoneindexentry <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipv6Scopezoneindextable.Ipv6Scopezoneindexentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IPMIB.Ipv6Scopezoneindextable, self).__init__()

            self.yang_name = "ipv6ScopeZoneIndexTable"
            self.yang_parent_name = "IP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ipv6ScopeZoneIndexEntry", ("ipv6scopezoneindexentry", IPMIB.Ipv6Scopezoneindextable.Ipv6Scopezoneindexentry))])
            self._leafs = OrderedDict()

            self.ipv6scopezoneindexentry = YList(self)
            self._segment_path = lambda: "ipv6ScopeZoneIndexTable"
            self._absolute_path = lambda: "IP-MIB:IP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMIB.Ipv6Scopezoneindextable, [], name, value)


        class Ipv6Scopezoneindexentry(Entity):
            """
            Each entry contains the list of scope identifiers on a given
            interface.
            
            .. attribute:: ipv6scopezoneindexifindex  (key)
            
            	The index value that uniquely identifies the interface to which these scopes belong.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipv6scopezoneindexlinklocal
            
            	The zone index for the link\-local scope on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindex3
            
            	The zone index for scope 3 on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindexadminlocal
            
            	The zone index for the admin\-local scope on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindexsitelocal
            
            	The zone index for the site\-local scope on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindex6
            
            	The zone index for scope 6 on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindex7
            
            	The zone index for scope 7 on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindexorganizationlocal
            
            	The zone index for the organization\-local scope on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindex9
            
            	The zone index for scope 9 on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindexa
            
            	The zone index for scope A on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindexb
            
            	The zone index for scope B on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindexc
            
            	The zone index for scope C on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindexd
            
            	The zone index for scope D on this interface
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IPMIB.Ipv6Scopezoneindextable.Ipv6Scopezoneindexentry, self).__init__()

                self.yang_name = "ipv6ScopeZoneIndexEntry"
                self.yang_parent_name = "ipv6ScopeZoneIndexTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipv6scopezoneindexifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipv6scopezoneindexifindex', YLeaf(YType.int32, 'ipv6ScopeZoneIndexIfIndex')),
                    ('ipv6scopezoneindexlinklocal', YLeaf(YType.uint32, 'ipv6ScopeZoneIndexLinkLocal')),
                    ('ipv6scopezoneindex3', YLeaf(YType.uint32, 'ipv6ScopeZoneIndex3')),
                    ('ipv6scopezoneindexadminlocal', YLeaf(YType.uint32, 'ipv6ScopeZoneIndexAdminLocal')),
                    ('ipv6scopezoneindexsitelocal', YLeaf(YType.uint32, 'ipv6ScopeZoneIndexSiteLocal')),
                    ('ipv6scopezoneindex6', YLeaf(YType.uint32, 'ipv6ScopeZoneIndex6')),
                    ('ipv6scopezoneindex7', YLeaf(YType.uint32, 'ipv6ScopeZoneIndex7')),
                    ('ipv6scopezoneindexorganizationlocal', YLeaf(YType.uint32, 'ipv6ScopeZoneIndexOrganizationLocal')),
                    ('ipv6scopezoneindex9', YLeaf(YType.uint32, 'ipv6ScopeZoneIndex9')),
                    ('ipv6scopezoneindexa', YLeaf(YType.uint32, 'ipv6ScopeZoneIndexA')),
                    ('ipv6scopezoneindexb', YLeaf(YType.uint32, 'ipv6ScopeZoneIndexB')),
                    ('ipv6scopezoneindexc', YLeaf(YType.uint32, 'ipv6ScopeZoneIndexC')),
                    ('ipv6scopezoneindexd', YLeaf(YType.uint32, 'ipv6ScopeZoneIndexD')),
                ])
                self.ipv6scopezoneindexifindex = None
                self.ipv6scopezoneindexlinklocal = None
                self.ipv6scopezoneindex3 = None
                self.ipv6scopezoneindexadminlocal = None
                self.ipv6scopezoneindexsitelocal = None
                self.ipv6scopezoneindex6 = None
                self.ipv6scopezoneindex7 = None
                self.ipv6scopezoneindexorganizationlocal = None
                self.ipv6scopezoneindex9 = None
                self.ipv6scopezoneindexa = None
                self.ipv6scopezoneindexb = None
                self.ipv6scopezoneindexc = None
                self.ipv6scopezoneindexd = None
                self._segment_path = lambda: "ipv6ScopeZoneIndexEntry" + "[ipv6ScopeZoneIndexIfIndex='" + str(self.ipv6scopezoneindexifindex) + "']"
                self._absolute_path = lambda: "IP-MIB:IP-MIB/ipv6ScopeZoneIndexTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMIB.Ipv6Scopezoneindextable.Ipv6Scopezoneindexentry, ['ipv6scopezoneindexifindex', 'ipv6scopezoneindexlinklocal', 'ipv6scopezoneindex3', 'ipv6scopezoneindexadminlocal', 'ipv6scopezoneindexsitelocal', 'ipv6scopezoneindex6', 'ipv6scopezoneindex7', 'ipv6scopezoneindexorganizationlocal', 'ipv6scopezoneindex9', 'ipv6scopezoneindexa', 'ipv6scopezoneindexb', 'ipv6scopezoneindexc', 'ipv6scopezoneindexd'], name, value)


    class Ipdefaultroutertable(Entity):
        """
        The table used to describe the default routers known to this
        
        
        entity.
        
        .. attribute:: ipdefaultrouterentry
        
        	Each entry contains information about a default router known to this entity
        	**type**\: list of  		 :py:class:`Ipdefaultrouterentry <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipdefaultroutertable.Ipdefaultrouterentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IPMIB.Ipdefaultroutertable, self).__init__()

            self.yang_name = "ipDefaultRouterTable"
            self.yang_parent_name = "IP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ipDefaultRouterEntry", ("ipdefaultrouterentry", IPMIB.Ipdefaultroutertable.Ipdefaultrouterentry))])
            self._leafs = OrderedDict()

            self.ipdefaultrouterentry = YList(self)
            self._segment_path = lambda: "ipDefaultRouterTable"
            self._absolute_path = lambda: "IP-MIB:IP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMIB.Ipdefaultroutertable, [], name, value)


        class Ipdefaultrouterentry(Entity):
            """
            Each entry contains information about a default router known
            to this entity.
            
            .. attribute:: ipdefaultrouteraddresstype  (key)
            
            	The address type for this row
            	**type**\:  :py:class:`InetAddressType <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetAddressType>`
            
            .. attribute:: ipdefaultrouteraddress  (key)
            
            	The IP address of the default router represented by this row.  The address type of this object is specified in ipDefaultRouterAddressType.  Implementers need to be aware that if the size of ipDefaultRouterAddress exceeds 115 octets, then OIDS of instances of columns in this row will have more than 128 sub\-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\: str
            
            	**length:** 0..255
            
            .. attribute:: ipdefaultrouterifindex  (key)
            
            	The index value that uniquely identifies the interface by which the router can be reached.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipdefaultrouterlifetime
            
            	The remaining length of time, in seconds, that this router will continue to be useful as a default router.  A value of zero indicates that it is no longer useful as a default router.  It is left to the implementer of the MIB as to whether a router with a lifetime of zero is removed from the list.  For IPv6, this value should be extracted from the router advertisement messages
            	**type**\: int
            
            	**range:** 0..65535
            
            	**units**\: seconds
            
            .. attribute:: ipdefaultrouterpreference
            
            	An indication of preference given to this router as a default router as described in he Default Router Preferences document.  Treating the value as a 2 bit signed integer allows for simple arithmetic comparisons.  For IPv4 routers or IPv6 routers that are not using the updated router advertisement format, this object is set to medium (0)
            	**type**\:  :py:class:`Ipdefaultrouterpreference <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipdefaultroutertable.Ipdefaultrouterentry.Ipdefaultrouterpreference>`
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IPMIB.Ipdefaultroutertable.Ipdefaultrouterentry, self).__init__()

                self.yang_name = "ipDefaultRouterEntry"
                self.yang_parent_name = "ipDefaultRouterTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipdefaultrouteraddresstype','ipdefaultrouteraddress','ipdefaultrouterifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipdefaultrouteraddresstype', YLeaf(YType.enumeration, 'ipDefaultRouterAddressType')),
                    ('ipdefaultrouteraddress', YLeaf(YType.str, 'ipDefaultRouterAddress')),
                    ('ipdefaultrouterifindex', YLeaf(YType.int32, 'ipDefaultRouterIfIndex')),
                    ('ipdefaultrouterlifetime', YLeaf(YType.uint32, 'ipDefaultRouterLifetime')),
                    ('ipdefaultrouterpreference', YLeaf(YType.enumeration, 'ipDefaultRouterPreference')),
                ])
                self.ipdefaultrouteraddresstype = None
                self.ipdefaultrouteraddress = None
                self.ipdefaultrouterifindex = None
                self.ipdefaultrouterlifetime = None
                self.ipdefaultrouterpreference = None
                self._segment_path = lambda: "ipDefaultRouterEntry" + "[ipDefaultRouterAddressType='" + str(self.ipdefaultrouteraddresstype) + "']" + "[ipDefaultRouterAddress='" + str(self.ipdefaultrouteraddress) + "']" + "[ipDefaultRouterIfIndex='" + str(self.ipdefaultrouterifindex) + "']"
                self._absolute_path = lambda: "IP-MIB:IP-MIB/ipDefaultRouterTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMIB.Ipdefaultroutertable.Ipdefaultrouterentry, ['ipdefaultrouteraddresstype', 'ipdefaultrouteraddress', 'ipdefaultrouterifindex', 'ipdefaultrouterlifetime', 'ipdefaultrouterpreference'], name, value)

            class Ipdefaultrouterpreference(Enum):
                """
                Ipdefaultrouterpreference (Enum Class)

                An indication of preference given to this router as a

                default router as described in he Default Router

                Preferences document.  Treating the value as a

                2 bit signed integer allows for simple arithmetic

                comparisons.

                For IPv4 routers or IPv6 routers that are not using the

                updated router advertisement format, this object is set to

                medium (0).

                .. data:: reserved = -2

                .. data:: low = -1

                .. data:: medium = 0

                .. data:: high = 1

                """

                reserved = Enum.YLeaf(-2, "reserved")

                low = Enum.YLeaf(-1, "low")

                medium = Enum.YLeaf(0, "medium")

                high = Enum.YLeaf(1, "high")



    class Ipv6Routeradverttable(Entity):
        """
        The table containing information used to construct router
        advertisements.
        
        .. attribute:: ipv6routeradvertentry
        
        	An entry containing information used to construct router advertisements.  Information in this table is persistent, and when this object is written, the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of  		 :py:class:`Ipv6Routeradvertentry <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Ipv6Routeradverttable.Ipv6Routeradvertentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IPMIB.Ipv6Routeradverttable, self).__init__()

            self.yang_name = "ipv6RouterAdvertTable"
            self.yang_parent_name = "IP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("ipv6RouterAdvertEntry", ("ipv6routeradvertentry", IPMIB.Ipv6Routeradverttable.Ipv6Routeradvertentry))])
            self._leafs = OrderedDict()

            self.ipv6routeradvertentry = YList(self)
            self._segment_path = lambda: "ipv6RouterAdvertTable"
            self._absolute_path = lambda: "IP-MIB:IP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMIB.Ipv6Routeradverttable, [], name, value)


        class Ipv6Routeradvertentry(Entity):
            """
            An entry containing information used to construct router
            advertisements.
            
            Information in this table is persistent, and when this
            object is written, the entity SHOULD save the change to
            non\-volatile storage.
            
            .. attribute:: ipv6routeradvertifindex  (key)
            
            	The index value that uniquely identifies the interface on which router advertisements constructed with this information will be transmitted.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipv6routeradvertsendadverts
            
            	A flag indicating whether the router sends periodic router advertisements and responds to router solicitations on this interface
            	**type**\: bool
            
            .. attribute:: ipv6routeradvertmaxinterval
            
            	The maximum time allowed between sending unsolicited router   advertisements from this interface
            	**type**\: int
            
            	**range:** 4..1800
            
            	**units**\: seconds
            
            .. attribute:: ipv6routeradvertmininterval
            
            	The minimum time allowed between sending unsolicited router advertisements from this interface.  The default is 0.33 \* ipv6RouterAdvertMaxInterval, however, in the case of a low value for ipv6RouterAdvertMaxInterval, the minimum value for this object is restricted to 3
            	**type**\: int
            
            	**range:** 3..1350
            
            	**units**\: seconds
            
            .. attribute:: ipv6routeradvertmanagedflag
            
            	The true/false value to be placed into the 'managed address configuration' flag field in router advertisements sent from this interface
            	**type**\: bool
            
            .. attribute:: ipv6routeradvertotherconfigflag
            
            	The true/false value to be placed into the 'other stateful configuration' flag field in router advertisements sent from this interface
            	**type**\: bool
            
            .. attribute:: ipv6routeradvertlinkmtu
            
            	The value to be placed in MTU options sent by the router on this interface.  A value of zero indicates that no MTU options are sent
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6routeradvertreachabletime
            
            	The value to be placed in the reachable time field in router advertisement messages sent from this interface.  A value of zero in the router advertisement indicates that the advertisement isn't specifying a value for reachable time
            	**type**\: int
            
            	**range:** 0..3600000
            
            	**units**\: milliseconds
            
            .. attribute:: ipv6routeradvertretransmittime
            
            	The value to be placed in the retransmit timer field in router advertisements sent from this interface.  A value of zero in the router advertisement indicates that the advertisement isn't specifying a value for retrans time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: ipv6routeradvertcurhoplimit
            
            	The default value to be placed in the current hop limit field in router advertisements sent from this interface.   The value should be set to the current diameter of the Internet.  A value of zero in the router advertisement indicates that the advertisement isn't specifying a value for curHopLimit.  The default should be set to the value specified in the IANA web pages (www.iana.org) at the time of implementation
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: ipv6routeradvertdefaultlifetime
            
            	The value to be placed in the router lifetime field of router advertisements sent from this interface.  This value MUST be either 0 or between ipv6RouterAdvertMaxInterval and 9000 seconds.  A value of zero indicates that the router is not to be used as a default router.  The default is 3 \* ipv6RouterAdvertMaxInterval
            	**type**\: int
            
            	**range:** 0..None \| 4..9000
            
            	**units**\: seconds
            
            .. attribute:: ipv6routeradvertrowstatus
            
            	The status of this conceptual row.  As all objects in this conceptual row have default values, a row can be created and made active by setting this object appropriately.  The RowStatus TC requires that this DESCRIPTION clause states under which circumstances other objects in this row can be modified.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:  :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IPMIB.Ipv6Routeradverttable.Ipv6Routeradvertentry, self).__init__()

                self.yang_name = "ipv6RouterAdvertEntry"
                self.yang_parent_name = "ipv6RouterAdvertTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['ipv6routeradvertifindex']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('ipv6routeradvertifindex', YLeaf(YType.int32, 'ipv6RouterAdvertIfIndex')),
                    ('ipv6routeradvertsendadverts', YLeaf(YType.boolean, 'ipv6RouterAdvertSendAdverts')),
                    ('ipv6routeradvertmaxinterval', YLeaf(YType.uint32, 'ipv6RouterAdvertMaxInterval')),
                    ('ipv6routeradvertmininterval', YLeaf(YType.uint32, 'ipv6RouterAdvertMinInterval')),
                    ('ipv6routeradvertmanagedflag', YLeaf(YType.boolean, 'ipv6RouterAdvertManagedFlag')),
                    ('ipv6routeradvertotherconfigflag', YLeaf(YType.boolean, 'ipv6RouterAdvertOtherConfigFlag')),
                    ('ipv6routeradvertlinkmtu', YLeaf(YType.uint32, 'ipv6RouterAdvertLinkMTU')),
                    ('ipv6routeradvertreachabletime', YLeaf(YType.uint32, 'ipv6RouterAdvertReachableTime')),
                    ('ipv6routeradvertretransmittime', YLeaf(YType.uint32, 'ipv6RouterAdvertRetransmitTime')),
                    ('ipv6routeradvertcurhoplimit', YLeaf(YType.uint32, 'ipv6RouterAdvertCurHopLimit')),
                    ('ipv6routeradvertdefaultlifetime', YLeaf(YType.uint32, 'ipv6RouterAdvertDefaultLifetime')),
                    ('ipv6routeradvertrowstatus', YLeaf(YType.enumeration, 'ipv6RouterAdvertRowStatus')),
                ])
                self.ipv6routeradvertifindex = None
                self.ipv6routeradvertsendadverts = None
                self.ipv6routeradvertmaxinterval = None
                self.ipv6routeradvertmininterval = None
                self.ipv6routeradvertmanagedflag = None
                self.ipv6routeradvertotherconfigflag = None
                self.ipv6routeradvertlinkmtu = None
                self.ipv6routeradvertreachabletime = None
                self.ipv6routeradvertretransmittime = None
                self.ipv6routeradvertcurhoplimit = None
                self.ipv6routeradvertdefaultlifetime = None
                self.ipv6routeradvertrowstatus = None
                self._segment_path = lambda: "ipv6RouterAdvertEntry" + "[ipv6RouterAdvertIfIndex='" + str(self.ipv6routeradvertifindex) + "']"
                self._absolute_path = lambda: "IP-MIB:IP-MIB/ipv6RouterAdvertTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMIB.Ipv6Routeradverttable.Ipv6Routeradvertentry, ['ipv6routeradvertifindex', 'ipv6routeradvertsendadverts', 'ipv6routeradvertmaxinterval', 'ipv6routeradvertmininterval', 'ipv6routeradvertmanagedflag', 'ipv6routeradvertotherconfigflag', 'ipv6routeradvertlinkmtu', 'ipv6routeradvertreachabletime', 'ipv6routeradvertretransmittime', 'ipv6routeradvertcurhoplimit', 'ipv6routeradvertdefaultlifetime', 'ipv6routeradvertrowstatus'], name, value)


    class Icmpstatstable(Entity):
        """
        The table of generic system\-wide ICMP counters.
        
        .. attribute:: icmpstatsentry
        
        	A conceptual row in the icmpStatsTable
        	**type**\: list of  		 :py:class:`Icmpstatsentry <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Icmpstatstable.Icmpstatsentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IPMIB.Icmpstatstable, self).__init__()

            self.yang_name = "icmpStatsTable"
            self.yang_parent_name = "IP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("icmpStatsEntry", ("icmpstatsentry", IPMIB.Icmpstatstable.Icmpstatsentry))])
            self._leafs = OrderedDict()

            self.icmpstatsentry = YList(self)
            self._segment_path = lambda: "icmpStatsTable"
            self._absolute_path = lambda: "IP-MIB:IP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMIB.Icmpstatstable, [], name, value)


        class Icmpstatsentry(Entity):
            """
            A conceptual row in the icmpStatsTable.
            
            .. attribute:: icmpstatsipversion  (key)
            
            	The IP version of the statistics
            	**type**\:  :py:class:`IpVersion <ydk.models.ietf.ietf_inet_types.IpVersion>`
            
            .. attribute:: icmpstatsinmsgs
            
            	The total number of ICMP messages that the entity received. Note that this counter includes all those counted by icmpStatsInErrors
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: icmpstatsinerrors
            
            	The number of ICMP messages that the entity received but determined as having ICMP\-specific errors (bad ICMP checksums, bad length, etc.)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: icmpstatsoutmsgs
            
            	The total number of ICMP messages that the entity attempted to send.  Note that this counter includes all those counted by icmpStatsOutErrors
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: icmpstatsouterrors
            
            	The number of ICMP messages that this entity did not send due to problems discovered within ICMP, such as a lack of buffers.  This value should not include errors discovered outside the ICMP layer, such as the inability of IP to route the resultant datagram.  In some implementations, there may be no types of error that contribute to this counter's value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IPMIB.Icmpstatstable.Icmpstatsentry, self).__init__()

                self.yang_name = "icmpStatsEntry"
                self.yang_parent_name = "icmpStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['icmpstatsipversion']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('icmpstatsipversion', YLeaf(YType.enumeration, 'icmpStatsIPVersion')),
                    ('icmpstatsinmsgs', YLeaf(YType.uint32, 'icmpStatsInMsgs')),
                    ('icmpstatsinerrors', YLeaf(YType.uint32, 'icmpStatsInErrors')),
                    ('icmpstatsoutmsgs', YLeaf(YType.uint32, 'icmpStatsOutMsgs')),
                    ('icmpstatsouterrors', YLeaf(YType.uint32, 'icmpStatsOutErrors')),
                ])
                self.icmpstatsipversion = None
                self.icmpstatsinmsgs = None
                self.icmpstatsinerrors = None
                self.icmpstatsoutmsgs = None
                self.icmpstatsouterrors = None
                self._segment_path = lambda: "icmpStatsEntry" + "[icmpStatsIPVersion='" + str(self.icmpstatsipversion) + "']"
                self._absolute_path = lambda: "IP-MIB:IP-MIB/icmpStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMIB.Icmpstatstable.Icmpstatsentry, ['icmpstatsipversion', 'icmpstatsinmsgs', 'icmpstatsinerrors', 'icmpstatsoutmsgs', 'icmpstatsouterrors'], name, value)


    class Icmpmsgstatstable(Entity):
        """
        The table of system\-wide per\-version, per\-message type ICMP
        counters.
        
        .. attribute:: icmpmsgstatsentry
        
        	A conceptual row in the icmpMsgStatsTable.  The system should track each ICMP type value, even if that ICMP type is not supported by the system.  However, a given row need not be instantiated unless a message of that type has been processed, i.e., the row for icmpMsgStatsType=X MAY be instantiated before but MUST be instantiated after the first message with Type=X is received or transmitted.  After receiving or transmitting any succeeding messages with Type=X, the relevant counter must be incremented
        	**type**\: list of  		 :py:class:`Icmpmsgstatsentry <ydk.models.cisco_ios_xe.IP_MIB.IPMIB.Icmpmsgstatstable.Icmpmsgstatsentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IPMIB.Icmpmsgstatstable, self).__init__()

            self.yang_name = "icmpMsgStatsTable"
            self.yang_parent_name = "IP-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("icmpMsgStatsEntry", ("icmpmsgstatsentry", IPMIB.Icmpmsgstatstable.Icmpmsgstatsentry))])
            self._leafs = OrderedDict()

            self.icmpmsgstatsentry = YList(self)
            self._segment_path = lambda: "icmpMsgStatsTable"
            self._absolute_path = lambda: "IP-MIB:IP-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(IPMIB.Icmpmsgstatstable, [], name, value)


        class Icmpmsgstatsentry(Entity):
            """
            A conceptual row in the icmpMsgStatsTable.
            
            The system should track each ICMP type value, even if that
            ICMP type is not supported by the system.  However, a
            given row need not be instantiated unless a message of that
            type has been processed, i.e., the row for
            icmpMsgStatsType=X MAY be instantiated before but MUST be
            instantiated after the first message with Type=X is
            received or transmitted.  After receiving or transmitting
            any succeeding messages with Type=X, the relevant counter
            must be incremented.
            
            .. attribute:: icmpmsgstatsipversion  (key)
            
            	The IP version of the statistics
            	**type**\:  :py:class:`IpVersion <ydk.models.ietf.ietf_inet_types.IpVersion>`
            
            .. attribute:: icmpmsgstatstype  (key)
            
            	The ICMP type field of the message type being counted by this row.  Note that ICMP message types are scoped by the address type in use
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: icmpmsgstatsinpkts
            
            	The number of input packets for this AF and type
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: icmpmsgstatsoutpkts
            
            	The number of output packets for this AF and type
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IPMIB.Icmpmsgstatstable.Icmpmsgstatsentry, self).__init__()

                self.yang_name = "icmpMsgStatsEntry"
                self.yang_parent_name = "icmpMsgStatsTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['icmpmsgstatsipversion','icmpmsgstatstype']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('icmpmsgstatsipversion', YLeaf(YType.enumeration, 'icmpMsgStatsIPVersion')),
                    ('icmpmsgstatstype', YLeaf(YType.int32, 'icmpMsgStatsType')),
                    ('icmpmsgstatsinpkts', YLeaf(YType.uint32, 'icmpMsgStatsInPkts')),
                    ('icmpmsgstatsoutpkts', YLeaf(YType.uint32, 'icmpMsgStatsOutPkts')),
                ])
                self.icmpmsgstatsipversion = None
                self.icmpmsgstatstype = None
                self.icmpmsgstatsinpkts = None
                self.icmpmsgstatsoutpkts = None
                self._segment_path = lambda: "icmpMsgStatsEntry" + "[icmpMsgStatsIPVersion='" + str(self.icmpmsgstatsipversion) + "']" + "[icmpMsgStatsType='" + str(self.icmpmsgstatstype) + "']"
                self._absolute_path = lambda: "IP-MIB:IP-MIB/icmpMsgStatsTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(IPMIB.Icmpmsgstatstable.Icmpmsgstatsentry, ['icmpmsgstatsipversion', 'icmpmsgstatstype', 'icmpmsgstatsinpkts', 'icmpmsgstatsoutpkts'], name, value)

    def clone_ptr(self):
        self._top_entity = IPMIB()
        return self._top_entity

