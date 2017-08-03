""" IP_MIB 

The MIB module for managing IP and ICMP implementations, but
excluding their management of IP routes.

Copyright (C) The Internet Society (2006).  This version of
this MIB module is part of RFC 4293; see the RFC itself for
full legal notices.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Ipaddressorigintc(Enum):
    """
    Ipaddressorigintc

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


class Ipaddressprefixorigintc(Enum):
    """
    Ipaddressprefixorigintc

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


class Ipaddressstatustc(Enum):
    """
    Ipaddressstatustc

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



class IpMib(Entity):
    """
    
    
    .. attribute:: icmp
    
    	
    	**type**\:   :py:class:`Icmp <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Icmp>`
    
    .. attribute:: icmpmsgstatstable
    
    	The table of system\-wide per\-version, per\-message type ICMP counters
    	**type**\:   :py:class:`Icmpmsgstatstable <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Icmpmsgstatstable>`
    
    .. attribute:: icmpstatstable
    
    	The table of generic system\-wide ICMP counters
    	**type**\:   :py:class:`Icmpstatstable <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Icmpstatstable>`
    
    .. attribute:: ip
    
    	
    	**type**\:   :py:class:`Ip <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ip>`
    
    .. attribute:: ipaddressprefixtable
    
    	This table allows the user to determine the source of an IP address or set of IP addresses, and allows other tables to share the information via pointer rather than by copying.  For example, when the node configures both a unicast and anycast address for a prefix, the ipAddressPrefix objects for those addresses will point to a single row in this table.  This table primarily provides support for IPv6 prefixes, and several of the objects are less meaningful for IPv4.  The table continues to allow IPv4 addresses to allow future flexibility.  In order to promote a common configuration, this document includes suggestions for default values for IPv4 prefixes.  Each of these values may be overridden if an object is meaningful to the node.  All prefixes used by this entity should be included in this table independent of how the entity learned the prefix. (This table isn't limited to prefixes learned from router   advertisements.)
    	**type**\:   :py:class:`Ipaddressprefixtable <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipaddressprefixtable>`
    
    .. attribute:: ipaddresstable
    
    	This table contains addressing information relevant to the entity's interfaces.  This table does not contain multicast address information. Tables for such information should be contained in multicast specific MIBs, such as RFC 3019.  While this table is writable, the user will note that several objects, such as ipAddressOrigin, are not.  The intention in allowing a user to write to this table is to allow them to add or remove any entry that isn't   permanent.  The user should be allowed to modify objects and entries when that would not cause inconsistencies within the table.  Allowing write access to objects, such as ipAddressOrigin, could allow a user to insert an entry and then label it incorrectly.  Note well\: When including IPv6 link\-local addresses in this table, the entry must use an InetAddressType of 'ipv6z' in order to differentiate between the possible interfaces
    	**type**\:   :py:class:`Ipaddresstable <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipaddresstable>`
    
    .. attribute:: ipaddrtable
    
    	The table of addressing information relevant to this entity's IPv4 addresses.  This table has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by the ipAddressTable although several objects that weren't deemed useful weren't carried forward while another (ipAdEntReasmMaxSize) was moved to the ipv4InterfaceTable
    	**type**\:   :py:class:`Ipaddrtable <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipaddrtable>`
    
    	**status**\: deprecated
    
    .. attribute:: ipdefaultroutertable
    
    	The table used to describe the default routers known to this   entity
    	**type**\:   :py:class:`Ipdefaultroutertable <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipdefaultroutertable>`
    
    .. attribute:: ipifstatstable
    
    	The table containing per\-interface traffic statistics.  This table and the ipSystemStatsTable contain similar objects whose difference is in their granularity.  Where this table contains per\-interface statistics, the ipSystemStatsTable contains the same statistics, but counted on a system wide basis
    	**type**\:   :py:class:`Ipifstatstable <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipifstatstable>`
    
    .. attribute:: ipnettomediatable
    
    	The IPv4 Address Translation table used for mapping from IPv4 addresses to physical addresses.  This table has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by the ipNetToPhysicalTable
    	**type**\:   :py:class:`Ipnettomediatable <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipnettomediatable>`
    
    	**status**\: deprecated
    
    .. attribute:: ipnettophysicaltable
    
    	The IP Address Translation table used for mapping from IP addresses to physical addresses.  The Address Translation tables contain the IP address to 'physical' address equivalences.  Some interfaces do not use translation tables for determining address equivalences (e.g., DDN\-X.25 has an algorithmic method); if all interfaces are of this type, then the Address Translation table is empty, i.e., has zero entries.  While many protocols may be used to populate this table, ARP and Neighbor Discovery are the most likely options
    	**type**\:   :py:class:`Ipnettophysicaltable <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipnettophysicaltable>`
    
    .. attribute:: ipsystemstatstable
    
    	The table containing system wide, IP version specific traffic statistics.  This table and the ipIfStatsTable contain similar objects whose difference is in their granularity.  Where this table contains system wide traffic statistics, the ipIfStatsTable contains the same statistics but counted on a per\-interface basis
    	**type**\:   :py:class:`Ipsystemstatstable <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipsystemstatstable>`
    
    .. attribute:: iptrafficstats
    
    	
    	**type**\:   :py:class:`Iptrafficstats <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Iptrafficstats>`
    
    .. attribute:: ipv4interfacetable
    
    	The table containing per\-interface IPv4\-specific information
    	**type**\:   :py:class:`Ipv4Interfacetable <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipv4Interfacetable>`
    
    .. attribute:: ipv6interfacetable
    
    	The table containing per\-interface IPv6\-specific information
    	**type**\:   :py:class:`Ipv6Interfacetable <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipv6Interfacetable>`
    
    .. attribute:: ipv6routeradverttable
    
    	The table containing information used to construct router advertisements
    	**type**\:   :py:class:`Ipv6Routeradverttable <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipv6Routeradverttable>`
    
    .. attribute:: ipv6scopezoneindextable
    
    	The table used to describe IPv6 unicast and multicast scope zones.  For those objects that have names rather than numbers, the names were chosen to coincide with the names used in the IPv6 address architecture document. 
    	**type**\:   :py:class:`Ipv6Scopezoneindextable <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipv6Scopezoneindextable>`
    
    

    """

    _prefix = 'IP-MIB'
    _revision = '2006-02-02'

    def __init__(self):
        super(IpMib, self).__init__()
        self._top_entity = None

        self.yang_name = "IP-MIB"
        self.yang_parent_name = "IP-MIB"

        self.icmp = IpMib.Icmp()
        self.icmp.parent = self
        self._children_name_map["icmp"] = "icmp"
        self._children_yang_names.add("icmp")

        self.icmpmsgstatstable = IpMib.Icmpmsgstatstable()
        self.icmpmsgstatstable.parent = self
        self._children_name_map["icmpmsgstatstable"] = "icmpMsgStatsTable"
        self._children_yang_names.add("icmpMsgStatsTable")

        self.icmpstatstable = IpMib.Icmpstatstable()
        self.icmpstatstable.parent = self
        self._children_name_map["icmpstatstable"] = "icmpStatsTable"
        self._children_yang_names.add("icmpStatsTable")

        self.ip = IpMib.Ip()
        self.ip.parent = self
        self._children_name_map["ip"] = "ip"
        self._children_yang_names.add("ip")

        self.ipaddressprefixtable = IpMib.Ipaddressprefixtable()
        self.ipaddressprefixtable.parent = self
        self._children_name_map["ipaddressprefixtable"] = "ipAddressPrefixTable"
        self._children_yang_names.add("ipAddressPrefixTable")

        self.ipaddresstable = IpMib.Ipaddresstable()
        self.ipaddresstable.parent = self
        self._children_name_map["ipaddresstable"] = "ipAddressTable"
        self._children_yang_names.add("ipAddressTable")

        self.ipaddrtable = IpMib.Ipaddrtable()
        self.ipaddrtable.parent = self
        self._children_name_map["ipaddrtable"] = "ipAddrTable"
        self._children_yang_names.add("ipAddrTable")

        self.ipdefaultroutertable = IpMib.Ipdefaultroutertable()
        self.ipdefaultroutertable.parent = self
        self._children_name_map["ipdefaultroutertable"] = "ipDefaultRouterTable"
        self._children_yang_names.add("ipDefaultRouterTable")

        self.ipifstatstable = IpMib.Ipifstatstable()
        self.ipifstatstable.parent = self
        self._children_name_map["ipifstatstable"] = "ipIfStatsTable"
        self._children_yang_names.add("ipIfStatsTable")

        self.ipnettomediatable = IpMib.Ipnettomediatable()
        self.ipnettomediatable.parent = self
        self._children_name_map["ipnettomediatable"] = "ipNetToMediaTable"
        self._children_yang_names.add("ipNetToMediaTable")

        self.ipnettophysicaltable = IpMib.Ipnettophysicaltable()
        self.ipnettophysicaltable.parent = self
        self._children_name_map["ipnettophysicaltable"] = "ipNetToPhysicalTable"
        self._children_yang_names.add("ipNetToPhysicalTable")

        self.ipsystemstatstable = IpMib.Ipsystemstatstable()
        self.ipsystemstatstable.parent = self
        self._children_name_map["ipsystemstatstable"] = "ipSystemStatsTable"
        self._children_yang_names.add("ipSystemStatsTable")

        self.iptrafficstats = IpMib.Iptrafficstats()
        self.iptrafficstats.parent = self
        self._children_name_map["iptrafficstats"] = "ipTrafficStats"
        self._children_yang_names.add("ipTrafficStats")

        self.ipv4interfacetable = IpMib.Ipv4Interfacetable()
        self.ipv4interfacetable.parent = self
        self._children_name_map["ipv4interfacetable"] = "ipv4InterfaceTable"
        self._children_yang_names.add("ipv4InterfaceTable")

        self.ipv6interfacetable = IpMib.Ipv6Interfacetable()
        self.ipv6interfacetable.parent = self
        self._children_name_map["ipv6interfacetable"] = "ipv6InterfaceTable"
        self._children_yang_names.add("ipv6InterfaceTable")

        self.ipv6routeradverttable = IpMib.Ipv6Routeradverttable()
        self.ipv6routeradverttable.parent = self
        self._children_name_map["ipv6routeradverttable"] = "ipv6RouterAdvertTable"
        self._children_yang_names.add("ipv6RouterAdvertTable")

        self.ipv6scopezoneindextable = IpMib.Ipv6Scopezoneindextable()
        self.ipv6scopezoneindextable.parent = self
        self._children_name_map["ipv6scopezoneindextable"] = "ipv6ScopeZoneIndexTable"
        self._children_yang_names.add("ipv6ScopeZoneIndexTable")


    class Ip(Entity):
        """
        
        
        .. attribute:: ipaddressspinlock
        
        	An advisory lock used to allow cooperating SNMP managers to coordinate their use of the set operation in creating or modifying rows within this table.  In order to use this lock to coordinate the use of set operations, managers should first retrieve ipAddressTableSpinLock.  They should then determine the appropriate row to create or modify.  Finally, they should issue the appropriate set command, including the retrieved value of ipAddressSpinLock.  If another manager has altered the table in the meantime, then the value of ipAddressSpinLock will have changed, and the creation will fail as it will be specifying an incorrect value for ipAddressSpinLock.  It is suggested, but not required, that the ipAddressSpinLock be the first var bind for each set of objects representing a 'row' in a PDU
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        .. attribute:: ipdefaultttl
        
        	The default value inserted into the Time\-To\-Live field of the IPv4 header of datagrams originated at this entity, whenever a TTL value is not supplied by the transport layer   protocol.  When this object is written, the entity should save the change to non\-volatile storage and restore the object from non\-volatile storage upon re\-initialization of the system. Note\: a stronger requirement is not used because this object was previously defined
        	**type**\:  int
        
        	**range:** 1..255
        
        .. attribute:: ipforwarding
        
        	The indication of whether this entity is acting as an IPv4 router in respect to the forwarding of datagrams received by, but not addressed to, this entity.  IPv4 routers forward datagrams.  IPv4 hosts do not (except those source\-routed via the host).  When this object is written, the entity should save the change to non\-volatile storage and restore the object from non\-volatile storage upon re\-initialization of the system. Note\: a stronger requirement is not used because this object was previously defined
        	**type**\:   :py:class:`Ipforwarding <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ip.Ipforwarding>`
        
        .. attribute:: ipforwdatagrams
        
        	The number of input datagrams for which this entity was not their final IPv4 destination, as a result of which an attempt was made to find a route to forward them to that final destination.  In entities which do not act as IPv4 routers, this counter will include only those packets which   were Source\-Routed via this entity, and the Source\-Route option processing was successful.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsInForwDatagrams
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipfragcreates
        
        	The number of IPv4 datagram fragments that have been generated as a result of fragmentation at this entity.  This object has been deprecated as a new IP version neutral table has been added.  It is loosely replaced by ipSystemStatsOutFragCreates
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipfragfails
        
        	The number of IPv4 datagrams that have been discarded because they needed to be fragmented at this entity but could not be, e.g., because their Don't Fragment flag was set.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsOutFragFails
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipfragoks
        
        	The number of IPv4 datagrams that have been successfully fragmented at this entity.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsOutFragOKs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipinaddrerrors
        
        	The number of input datagrams discarded because the IPv4 address in their IPv4 header's destination field was not a valid address to be received at this entity.  This count includes invalid addresses (e.g., 0.0.0.0) and addresses of unsupported Classes (e.g., Class E).  For entities which are not IPv4 routers, and therefore do not forward datagrams, this counter includes datagrams discarded because the destination address was not a local address.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsInAddrErrors
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipindelivers
        
        	The total number of input datagrams successfully delivered to IPv4 user\-protocols (including ICMP).  This object has been deprecated as a new IP version neutral table has been added.  It is loosely replaced by   ipSystemStatsIndelivers
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipindiscards
        
        	The number of input IPv4 datagrams for which no problems were encountered to prevent their continued processing, but which were discarded (e.g., for lack of buffer space).  Note that this counter does not include any datagrams discarded while awaiting re\-assembly.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsInDiscards
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipinhdrerrors
        
        	The number of input datagrams discarded due to errors in their IPv4 headers, including bad checksums, version number mismatch, other format errors, time\-to\-live exceeded, errors discovered in processing their IPv4 options, etc.  This object has been deprecated as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsInHdrErrors
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipinreceives
        
        	The total number of input datagrams received from interfaces, including those received in error.  This object has been deprecated, as a new IP version\-neutral   table has been added.  It is loosely replaced by ipSystemStatsInRecieves
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipinunknownprotos
        
        	The number of locally\-addressed datagrams received successfully but discarded because of an unknown or unsupported protocol.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsInUnknownProtos
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipoutdiscards
        
        	The number of output IPv4 datagrams for which no problem was encountered to prevent their transmission to their destination, but which were discarded (e.g., for lack of buffer space).  Note that this counter would include datagrams counted in ipForwDatagrams if any such packets met this (discretionary) discard criterion.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsOutDiscards
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipoutnoroutes
        
        	The number of IPv4 datagrams discarded because no route could be found to transmit them to their destination.  Note that this counter includes any packets counted in ipForwDatagrams which meet this `no\-route' criterion.  Note that this includes any datagrams which a host cannot route because all of its default routers are down.  This object has been deprecated, as a new IP version\-neutral   table has been added.  It is loosely replaced by ipSystemStatsOutNoRoutes
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipoutrequests
        
        	The total number of IPv4 datagrams which local IPv4 user protocols (including ICMP) supplied to IPv4 in requests for transmission.  Note that this counter does not include any datagrams counted in ipForwDatagrams.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsOutRequests
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipreasmfails
        
        	The number of failures detected by the IPv4 re\-assembly algorithm (for whatever reason\: timed out, errors, etc). Note that this is not necessarily a count of discarded IPv4 fragments since some algorithms (notably the algorithm in RFC 815) can lose track of the number of fragments by combining them as they are received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsReasmFails
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipreasmoks
        
        	The number of IPv4 datagrams successfully re\-assembled.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsReasmOKs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipreasmreqds
        
        	The number of IPv4 fragments received which needed to be reassembled at this entity.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by ipSystemStatsReasmReqds
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipreasmtimeout
        
        	The maximum number of seconds that received fragments are held while they are awaiting reassembly at this entity
        	**type**\:  int
        
        	**range:** \-2147483648..2147483647
        
        	**units**\: seconds
        
        .. attribute:: iproutingdiscards
        
        	The number of routing entries which were chosen to be discarded even though they are valid.  One possible reason for discarding such an entry could be to free\-up buffer space for other routing entries.   This object was defined in pre\-IPv6 versions of the IP MIB. It was implicitly IPv4 only, but the original specifications did not indicate this protocol restriction.  In order to clarify the specifications, this object has been deprecated and a similar, but more thoroughly clarified, object has been added to the IP\-FORWARD\-MIB
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: ipv4interfacetablelastchange
        
        	The value of sysUpTime on the most recent occasion at which a row in the ipv4InterfaceTable was added or deleted, or when an ipv4InterfaceReasmMaxSize or an ipv4InterfaceEnableStatus object was modified.  If new objects are added to the ipv4InterfaceTable that require the ipv4InterfaceTableLastChange to be updated when they are modified, they must specify that requirement in their description clause
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6interfacetablelastchange
        
        	The value of sysUpTime on the most recent occasion at which a row in the ipv6InterfaceTable was added or deleted or when an ipv6InterfaceReasmMaxSize, ipv6InterfaceIdentifier, ipv6InterfaceEnableStatus, ipv6InterfaceReachableTime, ipv6InterfaceRetransmitTime, or ipv6InterfaceForwarding object was modified.  If new objects are added to the ipv6InterfaceTable that require the ipv6InterfaceTableLastChange to be updated when they are modified, they must specify that requirement in their description clause
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: ipv6ipdefaulthoplimit
        
        	The default value inserted into the Hop Limit field of the IPv6 header of datagrams originated at this entity whenever a Hop Limit value is not supplied by the transport layer protocol.  When this object is written, the entity SHOULD save the change to non\-volatile storage and restore the object from non\-volatile storage upon re\-initialization of the system
        	**type**\:  int
        
        	**range:** 0..255
        
        .. attribute:: ipv6ipforwarding
        
        	The indication of whether this entity is acting as an IPv6 router on any interface in respect to the forwarding of datagrams received by, but not addressed to, this entity. IPv6 routers forward datagrams.  IPv6 hosts do not (except those source\-routed via the host).  When this object is written, the entity SHOULD save the change to non\-volatile storage and restore the object from non\-volatile storage upon re\-initialization of the system
        	**type**\:   :py:class:`Ipv6Ipforwarding <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ip.Ipv6Ipforwarding>`
        
        .. attribute:: ipv6routeradvertspinlock
        
        	An advisory lock used to allow cooperating SNMP managers to coordinate their use of the set operation in creating or modifying rows within this table.  In order to use this lock to coordinate the use of set operations, managers should first retrieve ipv6RouterAdvertSpinLock.  They should then determine the appropriate row to create or modify.  Finally, they should issue the appropriate set command including the retrieved value of ipv6RouterAdvertSpinLock.  If another manager has altered the table in the meantime, then the value of ipv6RouterAdvertSpinLock will have changed and the creation will fail as it will be specifying an incorrect value for ipv6RouterAdvertSpinLock.  It is suggested, but not required, that the ipv6RouterAdvertSpinLock be the first var bind for each set of objects representing a 'row' in a PDU
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IpMib.Ip, self).__init__()

            self.yang_name = "ip"
            self.yang_parent_name = "IP-MIB"

            self.ipaddressspinlock = YLeaf(YType.int32, "ipAddressSpinLock")

            self.ipdefaultttl = YLeaf(YType.int32, "ipDefaultTTL")

            self.ipforwarding = YLeaf(YType.enumeration, "ipForwarding")

            self.ipforwdatagrams = YLeaf(YType.uint32, "ipForwDatagrams")

            self.ipfragcreates = YLeaf(YType.uint32, "ipFragCreates")

            self.ipfragfails = YLeaf(YType.uint32, "ipFragFails")

            self.ipfragoks = YLeaf(YType.uint32, "ipFragOKs")

            self.ipinaddrerrors = YLeaf(YType.uint32, "ipInAddrErrors")

            self.ipindelivers = YLeaf(YType.uint32, "ipInDelivers")

            self.ipindiscards = YLeaf(YType.uint32, "ipInDiscards")

            self.ipinhdrerrors = YLeaf(YType.uint32, "ipInHdrErrors")

            self.ipinreceives = YLeaf(YType.uint32, "ipInReceives")

            self.ipinunknownprotos = YLeaf(YType.uint32, "ipInUnknownProtos")

            self.ipoutdiscards = YLeaf(YType.uint32, "ipOutDiscards")

            self.ipoutnoroutes = YLeaf(YType.uint32, "ipOutNoRoutes")

            self.ipoutrequests = YLeaf(YType.uint32, "ipOutRequests")

            self.ipreasmfails = YLeaf(YType.uint32, "ipReasmFails")

            self.ipreasmoks = YLeaf(YType.uint32, "ipReasmOKs")

            self.ipreasmreqds = YLeaf(YType.uint32, "ipReasmReqds")

            self.ipreasmtimeout = YLeaf(YType.int32, "ipReasmTimeout")

            self.iproutingdiscards = YLeaf(YType.uint32, "ipRoutingDiscards")

            self.ipv4interfacetablelastchange = YLeaf(YType.uint32, "ipv4InterfaceTableLastChange")

            self.ipv6interfacetablelastchange = YLeaf(YType.uint32, "ipv6InterfaceTableLastChange")

            self.ipv6ipdefaulthoplimit = YLeaf(YType.int32, "ipv6IpDefaultHopLimit")

            self.ipv6ipforwarding = YLeaf(YType.enumeration, "ipv6IpForwarding")

            self.ipv6routeradvertspinlock = YLeaf(YType.int32, "ipv6RouterAdvertSpinLock")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ipaddressspinlock",
                            "ipdefaultttl",
                            "ipforwarding",
                            "ipforwdatagrams",
                            "ipfragcreates",
                            "ipfragfails",
                            "ipfragoks",
                            "ipinaddrerrors",
                            "ipindelivers",
                            "ipindiscards",
                            "ipinhdrerrors",
                            "ipinreceives",
                            "ipinunknownprotos",
                            "ipoutdiscards",
                            "ipoutnoroutes",
                            "ipoutrequests",
                            "ipreasmfails",
                            "ipreasmoks",
                            "ipreasmreqds",
                            "ipreasmtimeout",
                            "iproutingdiscards",
                            "ipv4interfacetablelastchange",
                            "ipv6interfacetablelastchange",
                            "ipv6ipdefaulthoplimit",
                            "ipv6ipforwarding",
                            "ipv6routeradvertspinlock") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IpMib.Ip, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpMib.Ip, self).__setattr__(name, value)

        class Ipforwarding(Enum):
            """
            Ipforwarding

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
            Ipv6Ipforwarding

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


        def has_data(self):
            return (
                self.ipaddressspinlock.is_set or
                self.ipdefaultttl.is_set or
                self.ipforwarding.is_set or
                self.ipforwdatagrams.is_set or
                self.ipfragcreates.is_set or
                self.ipfragfails.is_set or
                self.ipfragoks.is_set or
                self.ipinaddrerrors.is_set or
                self.ipindelivers.is_set or
                self.ipindiscards.is_set or
                self.ipinhdrerrors.is_set or
                self.ipinreceives.is_set or
                self.ipinunknownprotos.is_set or
                self.ipoutdiscards.is_set or
                self.ipoutnoroutes.is_set or
                self.ipoutrequests.is_set or
                self.ipreasmfails.is_set or
                self.ipreasmoks.is_set or
                self.ipreasmreqds.is_set or
                self.ipreasmtimeout.is_set or
                self.iproutingdiscards.is_set or
                self.ipv4interfacetablelastchange.is_set or
                self.ipv6interfacetablelastchange.is_set or
                self.ipv6ipdefaulthoplimit.is_set or
                self.ipv6ipforwarding.is_set or
                self.ipv6routeradvertspinlock.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ipaddressspinlock.yfilter != YFilter.not_set or
                self.ipdefaultttl.yfilter != YFilter.not_set or
                self.ipforwarding.yfilter != YFilter.not_set or
                self.ipforwdatagrams.yfilter != YFilter.not_set or
                self.ipfragcreates.yfilter != YFilter.not_set or
                self.ipfragfails.yfilter != YFilter.not_set or
                self.ipfragoks.yfilter != YFilter.not_set or
                self.ipinaddrerrors.yfilter != YFilter.not_set or
                self.ipindelivers.yfilter != YFilter.not_set or
                self.ipindiscards.yfilter != YFilter.not_set or
                self.ipinhdrerrors.yfilter != YFilter.not_set or
                self.ipinreceives.yfilter != YFilter.not_set or
                self.ipinunknownprotos.yfilter != YFilter.not_set or
                self.ipoutdiscards.yfilter != YFilter.not_set or
                self.ipoutnoroutes.yfilter != YFilter.not_set or
                self.ipoutrequests.yfilter != YFilter.not_set or
                self.ipreasmfails.yfilter != YFilter.not_set or
                self.ipreasmoks.yfilter != YFilter.not_set or
                self.ipreasmreqds.yfilter != YFilter.not_set or
                self.ipreasmtimeout.yfilter != YFilter.not_set or
                self.iproutingdiscards.yfilter != YFilter.not_set or
                self.ipv4interfacetablelastchange.yfilter != YFilter.not_set or
                self.ipv6interfacetablelastchange.yfilter != YFilter.not_set or
                self.ipv6ipdefaulthoplimit.yfilter != YFilter.not_set or
                self.ipv6ipforwarding.yfilter != YFilter.not_set or
                self.ipv6routeradvertspinlock.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ip" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-MIB:IP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ipaddressspinlock.is_set or self.ipaddressspinlock.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipaddressspinlock.get_name_leafdata())
            if (self.ipdefaultttl.is_set or self.ipdefaultttl.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipdefaultttl.get_name_leafdata())
            if (self.ipforwarding.is_set or self.ipforwarding.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipforwarding.get_name_leafdata())
            if (self.ipforwdatagrams.is_set or self.ipforwdatagrams.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipforwdatagrams.get_name_leafdata())
            if (self.ipfragcreates.is_set or self.ipfragcreates.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipfragcreates.get_name_leafdata())
            if (self.ipfragfails.is_set or self.ipfragfails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipfragfails.get_name_leafdata())
            if (self.ipfragoks.is_set or self.ipfragoks.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipfragoks.get_name_leafdata())
            if (self.ipinaddrerrors.is_set or self.ipinaddrerrors.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipinaddrerrors.get_name_leafdata())
            if (self.ipindelivers.is_set or self.ipindelivers.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipindelivers.get_name_leafdata())
            if (self.ipindiscards.is_set or self.ipindiscards.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipindiscards.get_name_leafdata())
            if (self.ipinhdrerrors.is_set or self.ipinhdrerrors.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipinhdrerrors.get_name_leafdata())
            if (self.ipinreceives.is_set or self.ipinreceives.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipinreceives.get_name_leafdata())
            if (self.ipinunknownprotos.is_set or self.ipinunknownprotos.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipinunknownprotos.get_name_leafdata())
            if (self.ipoutdiscards.is_set or self.ipoutdiscards.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipoutdiscards.get_name_leafdata())
            if (self.ipoutnoroutes.is_set or self.ipoutnoroutes.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipoutnoroutes.get_name_leafdata())
            if (self.ipoutrequests.is_set or self.ipoutrequests.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipoutrequests.get_name_leafdata())
            if (self.ipreasmfails.is_set or self.ipreasmfails.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipreasmfails.get_name_leafdata())
            if (self.ipreasmoks.is_set or self.ipreasmoks.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipreasmoks.get_name_leafdata())
            if (self.ipreasmreqds.is_set or self.ipreasmreqds.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipreasmreqds.get_name_leafdata())
            if (self.ipreasmtimeout.is_set or self.ipreasmtimeout.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipreasmtimeout.get_name_leafdata())
            if (self.iproutingdiscards.is_set or self.iproutingdiscards.yfilter != YFilter.not_set):
                leaf_name_data.append(self.iproutingdiscards.get_name_leafdata())
            if (self.ipv4interfacetablelastchange.is_set or self.ipv4interfacetablelastchange.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv4interfacetablelastchange.get_name_leafdata())
            if (self.ipv6interfacetablelastchange.is_set or self.ipv6interfacetablelastchange.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6interfacetablelastchange.get_name_leafdata())
            if (self.ipv6ipdefaulthoplimit.is_set or self.ipv6ipdefaulthoplimit.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6ipdefaulthoplimit.get_name_leafdata())
            if (self.ipv6ipforwarding.is_set or self.ipv6ipforwarding.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6ipforwarding.get_name_leafdata())
            if (self.ipv6routeradvertspinlock.is_set or self.ipv6routeradvertspinlock.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipv6routeradvertspinlock.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipAddressSpinLock" or name == "ipDefaultTTL" or name == "ipForwarding" or name == "ipForwDatagrams" or name == "ipFragCreates" or name == "ipFragFails" or name == "ipFragOKs" or name == "ipInAddrErrors" or name == "ipInDelivers" or name == "ipInDiscards" or name == "ipInHdrErrors" or name == "ipInReceives" or name == "ipInUnknownProtos" or name == "ipOutDiscards" or name == "ipOutNoRoutes" or name == "ipOutRequests" or name == "ipReasmFails" or name == "ipReasmOKs" or name == "ipReasmReqds" or name == "ipReasmTimeout" or name == "ipRoutingDiscards" or name == "ipv4InterfaceTableLastChange" or name == "ipv6InterfaceTableLastChange" or name == "ipv6IpDefaultHopLimit" or name == "ipv6IpForwarding" or name == "ipv6RouterAdvertSpinLock"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ipAddressSpinLock"):
                self.ipaddressspinlock = value
                self.ipaddressspinlock.value_namespace = name_space
                self.ipaddressspinlock.value_namespace_prefix = name_space_prefix
            if(value_path == "ipDefaultTTL"):
                self.ipdefaultttl = value
                self.ipdefaultttl.value_namespace = name_space
                self.ipdefaultttl.value_namespace_prefix = name_space_prefix
            if(value_path == "ipForwarding"):
                self.ipforwarding = value
                self.ipforwarding.value_namespace = name_space
                self.ipforwarding.value_namespace_prefix = name_space_prefix
            if(value_path == "ipForwDatagrams"):
                self.ipforwdatagrams = value
                self.ipforwdatagrams.value_namespace = name_space
                self.ipforwdatagrams.value_namespace_prefix = name_space_prefix
            if(value_path == "ipFragCreates"):
                self.ipfragcreates = value
                self.ipfragcreates.value_namespace = name_space
                self.ipfragcreates.value_namespace_prefix = name_space_prefix
            if(value_path == "ipFragFails"):
                self.ipfragfails = value
                self.ipfragfails.value_namespace = name_space
                self.ipfragfails.value_namespace_prefix = name_space_prefix
            if(value_path == "ipFragOKs"):
                self.ipfragoks = value
                self.ipfragoks.value_namespace = name_space
                self.ipfragoks.value_namespace_prefix = name_space_prefix
            if(value_path == "ipInAddrErrors"):
                self.ipinaddrerrors = value
                self.ipinaddrerrors.value_namespace = name_space
                self.ipinaddrerrors.value_namespace_prefix = name_space_prefix
            if(value_path == "ipInDelivers"):
                self.ipindelivers = value
                self.ipindelivers.value_namespace = name_space
                self.ipindelivers.value_namespace_prefix = name_space_prefix
            if(value_path == "ipInDiscards"):
                self.ipindiscards = value
                self.ipindiscards.value_namespace = name_space
                self.ipindiscards.value_namespace_prefix = name_space_prefix
            if(value_path == "ipInHdrErrors"):
                self.ipinhdrerrors = value
                self.ipinhdrerrors.value_namespace = name_space
                self.ipinhdrerrors.value_namespace_prefix = name_space_prefix
            if(value_path == "ipInReceives"):
                self.ipinreceives = value
                self.ipinreceives.value_namespace = name_space
                self.ipinreceives.value_namespace_prefix = name_space_prefix
            if(value_path == "ipInUnknownProtos"):
                self.ipinunknownprotos = value
                self.ipinunknownprotos.value_namespace = name_space
                self.ipinunknownprotos.value_namespace_prefix = name_space_prefix
            if(value_path == "ipOutDiscards"):
                self.ipoutdiscards = value
                self.ipoutdiscards.value_namespace = name_space
                self.ipoutdiscards.value_namespace_prefix = name_space_prefix
            if(value_path == "ipOutNoRoutes"):
                self.ipoutnoroutes = value
                self.ipoutnoroutes.value_namespace = name_space
                self.ipoutnoroutes.value_namespace_prefix = name_space_prefix
            if(value_path == "ipOutRequests"):
                self.ipoutrequests = value
                self.ipoutrequests.value_namespace = name_space
                self.ipoutrequests.value_namespace_prefix = name_space_prefix
            if(value_path == "ipReasmFails"):
                self.ipreasmfails = value
                self.ipreasmfails.value_namespace = name_space
                self.ipreasmfails.value_namespace_prefix = name_space_prefix
            if(value_path == "ipReasmOKs"):
                self.ipreasmoks = value
                self.ipreasmoks.value_namespace = name_space
                self.ipreasmoks.value_namespace_prefix = name_space_prefix
            if(value_path == "ipReasmReqds"):
                self.ipreasmreqds = value
                self.ipreasmreqds.value_namespace = name_space
                self.ipreasmreqds.value_namespace_prefix = name_space_prefix
            if(value_path == "ipReasmTimeout"):
                self.ipreasmtimeout = value
                self.ipreasmtimeout.value_namespace = name_space
                self.ipreasmtimeout.value_namespace_prefix = name_space_prefix
            if(value_path == "ipRoutingDiscards"):
                self.iproutingdiscards = value
                self.iproutingdiscards.value_namespace = name_space
                self.iproutingdiscards.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv4InterfaceTableLastChange"):
                self.ipv4interfacetablelastchange = value
                self.ipv4interfacetablelastchange.value_namespace = name_space
                self.ipv4interfacetablelastchange.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6InterfaceTableLastChange"):
                self.ipv6interfacetablelastchange = value
                self.ipv6interfacetablelastchange.value_namespace = name_space
                self.ipv6interfacetablelastchange.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6IpDefaultHopLimit"):
                self.ipv6ipdefaulthoplimit = value
                self.ipv6ipdefaulthoplimit.value_namespace = name_space
                self.ipv6ipdefaulthoplimit.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6IpForwarding"):
                self.ipv6ipforwarding = value
                self.ipv6ipforwarding.value_namespace = name_space
                self.ipv6ipforwarding.value_namespace_prefix = name_space_prefix
            if(value_path == "ipv6RouterAdvertSpinLock"):
                self.ipv6routeradvertspinlock = value
                self.ipv6routeradvertspinlock.value_namespace = name_space
                self.ipv6routeradvertspinlock.value_namespace_prefix = name_space_prefix


    class Iptrafficstats(Entity):
        """
        
        
        .. attribute:: ipifstatstablelastchange
        
        	The value of sysUpTime on the most recent occasion at which a row in the ipIfStatsTable was added or deleted.  If new objects are added to the ipIfStatsTable that require the ipIfStatsTableLastChange to be updated when they are modified, they must specify that requirement in their description clause
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IpMib.Iptrafficstats, self).__init__()

            self.yang_name = "ipTrafficStats"
            self.yang_parent_name = "IP-MIB"

            self.ipifstatstablelastchange = YLeaf(YType.uint32, "ipIfStatsTableLastChange")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("ipifstatstablelastchange") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IpMib.Iptrafficstats, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpMib.Iptrafficstats, self).__setattr__(name, value)

        def has_data(self):
            return self.ipifstatstablelastchange.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.ipifstatstablelastchange.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipTrafficStats" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-MIB:IP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.ipifstatstablelastchange.is_set or self.ipifstatstablelastchange.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ipifstatstablelastchange.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipIfStatsTableLastChange"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "ipIfStatsTableLastChange"):
                self.ipifstatstablelastchange = value
                self.ipifstatstablelastchange.value_namespace = name_space
                self.ipifstatstablelastchange.value_namespace_prefix = name_space_prefix


    class Icmp(Entity):
        """
        
        
        .. attribute:: icmpinaddrmaskreps
        
        	The number of ICMP Address Mask Reply messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpinaddrmasks
        
        	The number of ICMP Address Mask Request messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpindestunreachs
        
        	The number of ICMP Destination Unreachable messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpinechoreps
        
        	The number of ICMP Echo Reply messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpinechos
        
        	The number of ICMP Echo (request) messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpinerrors
        
        	The number of ICMP messages which the entity received but determined as having ICMP\-specific errors (bad ICMP checksums, bad length, etc.).  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by icmpStatsInErrors
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpinmsgs
        
        	The total number of ICMP messages which the entity received. Note that this counter includes all those counted by icmpInErrors.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by icmpStatsInMsgs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpinparmprobs
        
        	The number of ICMP Parameter Problem messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpinredirects
        
        	The number of ICMP Redirect messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpinsrcquenchs
        
        	The number of ICMP Source Quench messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpintimeexcds
        
        	The number of ICMP Time Exceeded messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpintimestampreps
        
        	The number of ICMP Timestamp Reply messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpintimestamps
        
        	The number of ICMP Timestamp (request) messages received.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpoutaddrmaskreps
        
        	The number of ICMP Address Mask Reply messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpoutaddrmasks
        
        	The number of ICMP Address Mask Request messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpoutdestunreachs
        
        	The number of ICMP Destination Unreachable messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpoutechoreps
        
        	The number of ICMP Echo Reply messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpoutechos
        
        	The number of ICMP Echo (request) messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpouterrors
        
        	The number of ICMP messages which this entity did not send due to problems discovered within ICMP, such as a lack of buffers.  This value should not include errors discovered outside the ICMP layer, such as the inability of IP to route the resultant datagram.  In some implementations, there may be no types of error which contribute to this counter's value.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by icmpStatsOutErrors
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpoutmsgs
        
        	The total number of ICMP messages which this entity attempted to send.  Note that this counter includes all those counted by icmpOutErrors.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by icmpStatsOutMsgs
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpoutparmprobs
        
        	The number of ICMP Parameter Problem messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpoutredirects
        
        	The number of ICMP Redirect messages sent.  For a host, this object will always be zero, since hosts do not send redirects.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpoutsrcquenchs
        
        	The number of ICMP Source Quench messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpouttimeexcds
        
        	The number of ICMP Time Exceeded messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpouttimestampreps
        
        	The number of ICMP Timestamp Reply messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        .. attribute:: icmpouttimestamps
        
        	The number of ICMP Timestamp (request) messages sent.  This object has been deprecated, as a new IP version\-neutral table has been added.  It is loosely replaced by a column in the icmpMsgStatsTable
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IpMib.Icmp, self).__init__()

            self.yang_name = "icmp"
            self.yang_parent_name = "IP-MIB"

            self.icmpinaddrmaskreps = YLeaf(YType.uint32, "icmpInAddrMaskReps")

            self.icmpinaddrmasks = YLeaf(YType.uint32, "icmpInAddrMasks")

            self.icmpindestunreachs = YLeaf(YType.uint32, "icmpInDestUnreachs")

            self.icmpinechoreps = YLeaf(YType.uint32, "icmpInEchoReps")

            self.icmpinechos = YLeaf(YType.uint32, "icmpInEchos")

            self.icmpinerrors = YLeaf(YType.uint32, "icmpInErrors")

            self.icmpinmsgs = YLeaf(YType.uint32, "icmpInMsgs")

            self.icmpinparmprobs = YLeaf(YType.uint32, "icmpInParmProbs")

            self.icmpinredirects = YLeaf(YType.uint32, "icmpInRedirects")

            self.icmpinsrcquenchs = YLeaf(YType.uint32, "icmpInSrcQuenchs")

            self.icmpintimeexcds = YLeaf(YType.uint32, "icmpInTimeExcds")

            self.icmpintimestampreps = YLeaf(YType.uint32, "icmpInTimestampReps")

            self.icmpintimestamps = YLeaf(YType.uint32, "icmpInTimestamps")

            self.icmpoutaddrmaskreps = YLeaf(YType.uint32, "icmpOutAddrMaskReps")

            self.icmpoutaddrmasks = YLeaf(YType.uint32, "icmpOutAddrMasks")

            self.icmpoutdestunreachs = YLeaf(YType.uint32, "icmpOutDestUnreachs")

            self.icmpoutechoreps = YLeaf(YType.uint32, "icmpOutEchoReps")

            self.icmpoutechos = YLeaf(YType.uint32, "icmpOutEchos")

            self.icmpouterrors = YLeaf(YType.uint32, "icmpOutErrors")

            self.icmpoutmsgs = YLeaf(YType.uint32, "icmpOutMsgs")

            self.icmpoutparmprobs = YLeaf(YType.uint32, "icmpOutParmProbs")

            self.icmpoutredirects = YLeaf(YType.uint32, "icmpOutRedirects")

            self.icmpoutsrcquenchs = YLeaf(YType.uint32, "icmpOutSrcQuenchs")

            self.icmpouttimeexcds = YLeaf(YType.uint32, "icmpOutTimeExcds")

            self.icmpouttimestampreps = YLeaf(YType.uint32, "icmpOutTimestampReps")

            self.icmpouttimestamps = YLeaf(YType.uint32, "icmpOutTimestamps")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("icmpinaddrmaskreps",
                            "icmpinaddrmasks",
                            "icmpindestunreachs",
                            "icmpinechoreps",
                            "icmpinechos",
                            "icmpinerrors",
                            "icmpinmsgs",
                            "icmpinparmprobs",
                            "icmpinredirects",
                            "icmpinsrcquenchs",
                            "icmpintimeexcds",
                            "icmpintimestampreps",
                            "icmpintimestamps",
                            "icmpoutaddrmaskreps",
                            "icmpoutaddrmasks",
                            "icmpoutdestunreachs",
                            "icmpoutechoreps",
                            "icmpoutechos",
                            "icmpouterrors",
                            "icmpoutmsgs",
                            "icmpoutparmprobs",
                            "icmpoutredirects",
                            "icmpoutsrcquenchs",
                            "icmpouttimeexcds",
                            "icmpouttimestampreps",
                            "icmpouttimestamps") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(IpMib.Icmp, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpMib.Icmp, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.icmpinaddrmaskreps.is_set or
                self.icmpinaddrmasks.is_set or
                self.icmpindestunreachs.is_set or
                self.icmpinechoreps.is_set or
                self.icmpinechos.is_set or
                self.icmpinerrors.is_set or
                self.icmpinmsgs.is_set or
                self.icmpinparmprobs.is_set or
                self.icmpinredirects.is_set or
                self.icmpinsrcquenchs.is_set or
                self.icmpintimeexcds.is_set or
                self.icmpintimestampreps.is_set or
                self.icmpintimestamps.is_set or
                self.icmpoutaddrmaskreps.is_set or
                self.icmpoutaddrmasks.is_set or
                self.icmpoutdestunreachs.is_set or
                self.icmpoutechoreps.is_set or
                self.icmpoutechos.is_set or
                self.icmpouterrors.is_set or
                self.icmpoutmsgs.is_set or
                self.icmpoutparmprobs.is_set or
                self.icmpoutredirects.is_set or
                self.icmpoutsrcquenchs.is_set or
                self.icmpouttimeexcds.is_set or
                self.icmpouttimestampreps.is_set or
                self.icmpouttimestamps.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.icmpinaddrmaskreps.yfilter != YFilter.not_set or
                self.icmpinaddrmasks.yfilter != YFilter.not_set or
                self.icmpindestunreachs.yfilter != YFilter.not_set or
                self.icmpinechoreps.yfilter != YFilter.not_set or
                self.icmpinechos.yfilter != YFilter.not_set or
                self.icmpinerrors.yfilter != YFilter.not_set or
                self.icmpinmsgs.yfilter != YFilter.not_set or
                self.icmpinparmprobs.yfilter != YFilter.not_set or
                self.icmpinredirects.yfilter != YFilter.not_set or
                self.icmpinsrcquenchs.yfilter != YFilter.not_set or
                self.icmpintimeexcds.yfilter != YFilter.not_set or
                self.icmpintimestampreps.yfilter != YFilter.not_set or
                self.icmpintimestamps.yfilter != YFilter.not_set or
                self.icmpoutaddrmaskreps.yfilter != YFilter.not_set or
                self.icmpoutaddrmasks.yfilter != YFilter.not_set or
                self.icmpoutdestunreachs.yfilter != YFilter.not_set or
                self.icmpoutechoreps.yfilter != YFilter.not_set or
                self.icmpoutechos.yfilter != YFilter.not_set or
                self.icmpouterrors.yfilter != YFilter.not_set or
                self.icmpoutmsgs.yfilter != YFilter.not_set or
                self.icmpoutparmprobs.yfilter != YFilter.not_set or
                self.icmpoutredirects.yfilter != YFilter.not_set or
                self.icmpoutsrcquenchs.yfilter != YFilter.not_set or
                self.icmpouttimeexcds.yfilter != YFilter.not_set or
                self.icmpouttimestampreps.yfilter != YFilter.not_set or
                self.icmpouttimestamps.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "icmp" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-MIB:IP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.icmpinaddrmaskreps.is_set or self.icmpinaddrmaskreps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpinaddrmaskreps.get_name_leafdata())
            if (self.icmpinaddrmasks.is_set or self.icmpinaddrmasks.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpinaddrmasks.get_name_leafdata())
            if (self.icmpindestunreachs.is_set or self.icmpindestunreachs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpindestunreachs.get_name_leafdata())
            if (self.icmpinechoreps.is_set or self.icmpinechoreps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpinechoreps.get_name_leafdata())
            if (self.icmpinechos.is_set or self.icmpinechos.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpinechos.get_name_leafdata())
            if (self.icmpinerrors.is_set or self.icmpinerrors.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpinerrors.get_name_leafdata())
            if (self.icmpinmsgs.is_set or self.icmpinmsgs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpinmsgs.get_name_leafdata())
            if (self.icmpinparmprobs.is_set or self.icmpinparmprobs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpinparmprobs.get_name_leafdata())
            if (self.icmpinredirects.is_set or self.icmpinredirects.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpinredirects.get_name_leafdata())
            if (self.icmpinsrcquenchs.is_set or self.icmpinsrcquenchs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpinsrcquenchs.get_name_leafdata())
            if (self.icmpintimeexcds.is_set or self.icmpintimeexcds.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpintimeexcds.get_name_leafdata())
            if (self.icmpintimestampreps.is_set or self.icmpintimestampreps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpintimestampreps.get_name_leafdata())
            if (self.icmpintimestamps.is_set or self.icmpintimestamps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpintimestamps.get_name_leafdata())
            if (self.icmpoutaddrmaskreps.is_set or self.icmpoutaddrmaskreps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpoutaddrmaskreps.get_name_leafdata())
            if (self.icmpoutaddrmasks.is_set or self.icmpoutaddrmasks.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpoutaddrmasks.get_name_leafdata())
            if (self.icmpoutdestunreachs.is_set or self.icmpoutdestunreachs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpoutdestunreachs.get_name_leafdata())
            if (self.icmpoutechoreps.is_set or self.icmpoutechoreps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpoutechoreps.get_name_leafdata())
            if (self.icmpoutechos.is_set or self.icmpoutechos.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpoutechos.get_name_leafdata())
            if (self.icmpouterrors.is_set or self.icmpouterrors.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpouterrors.get_name_leafdata())
            if (self.icmpoutmsgs.is_set or self.icmpoutmsgs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpoutmsgs.get_name_leafdata())
            if (self.icmpoutparmprobs.is_set or self.icmpoutparmprobs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpoutparmprobs.get_name_leafdata())
            if (self.icmpoutredirects.is_set or self.icmpoutredirects.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpoutredirects.get_name_leafdata())
            if (self.icmpoutsrcquenchs.is_set or self.icmpoutsrcquenchs.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpoutsrcquenchs.get_name_leafdata())
            if (self.icmpouttimeexcds.is_set or self.icmpouttimeexcds.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpouttimeexcds.get_name_leafdata())
            if (self.icmpouttimestampreps.is_set or self.icmpouttimestampreps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpouttimestampreps.get_name_leafdata())
            if (self.icmpouttimestamps.is_set or self.icmpouttimestamps.yfilter != YFilter.not_set):
                leaf_name_data.append(self.icmpouttimestamps.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "icmpInAddrMaskReps" or name == "icmpInAddrMasks" or name == "icmpInDestUnreachs" or name == "icmpInEchoReps" or name == "icmpInEchos" or name == "icmpInErrors" or name == "icmpInMsgs" or name == "icmpInParmProbs" or name == "icmpInRedirects" or name == "icmpInSrcQuenchs" or name == "icmpInTimeExcds" or name == "icmpInTimestampReps" or name == "icmpInTimestamps" or name == "icmpOutAddrMaskReps" or name == "icmpOutAddrMasks" or name == "icmpOutDestUnreachs" or name == "icmpOutEchoReps" or name == "icmpOutEchos" or name == "icmpOutErrors" or name == "icmpOutMsgs" or name == "icmpOutParmProbs" or name == "icmpOutRedirects" or name == "icmpOutSrcQuenchs" or name == "icmpOutTimeExcds" or name == "icmpOutTimestampReps" or name == "icmpOutTimestamps"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "icmpInAddrMaskReps"):
                self.icmpinaddrmaskreps = value
                self.icmpinaddrmaskreps.value_namespace = name_space
                self.icmpinaddrmaskreps.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInAddrMasks"):
                self.icmpinaddrmasks = value
                self.icmpinaddrmasks.value_namespace = name_space
                self.icmpinaddrmasks.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInDestUnreachs"):
                self.icmpindestunreachs = value
                self.icmpindestunreachs.value_namespace = name_space
                self.icmpindestunreachs.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInEchoReps"):
                self.icmpinechoreps = value
                self.icmpinechoreps.value_namespace = name_space
                self.icmpinechoreps.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInEchos"):
                self.icmpinechos = value
                self.icmpinechos.value_namespace = name_space
                self.icmpinechos.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInErrors"):
                self.icmpinerrors = value
                self.icmpinerrors.value_namespace = name_space
                self.icmpinerrors.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInMsgs"):
                self.icmpinmsgs = value
                self.icmpinmsgs.value_namespace = name_space
                self.icmpinmsgs.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInParmProbs"):
                self.icmpinparmprobs = value
                self.icmpinparmprobs.value_namespace = name_space
                self.icmpinparmprobs.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInRedirects"):
                self.icmpinredirects = value
                self.icmpinredirects.value_namespace = name_space
                self.icmpinredirects.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInSrcQuenchs"):
                self.icmpinsrcquenchs = value
                self.icmpinsrcquenchs.value_namespace = name_space
                self.icmpinsrcquenchs.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInTimeExcds"):
                self.icmpintimeexcds = value
                self.icmpintimeexcds.value_namespace = name_space
                self.icmpintimeexcds.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInTimestampReps"):
                self.icmpintimestampreps = value
                self.icmpintimestampreps.value_namespace = name_space
                self.icmpintimestampreps.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpInTimestamps"):
                self.icmpintimestamps = value
                self.icmpintimestamps.value_namespace = name_space
                self.icmpintimestamps.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutAddrMaskReps"):
                self.icmpoutaddrmaskreps = value
                self.icmpoutaddrmaskreps.value_namespace = name_space
                self.icmpoutaddrmaskreps.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutAddrMasks"):
                self.icmpoutaddrmasks = value
                self.icmpoutaddrmasks.value_namespace = name_space
                self.icmpoutaddrmasks.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutDestUnreachs"):
                self.icmpoutdestunreachs = value
                self.icmpoutdestunreachs.value_namespace = name_space
                self.icmpoutdestunreachs.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutEchoReps"):
                self.icmpoutechoreps = value
                self.icmpoutechoreps.value_namespace = name_space
                self.icmpoutechoreps.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutEchos"):
                self.icmpoutechos = value
                self.icmpoutechos.value_namespace = name_space
                self.icmpoutechos.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutErrors"):
                self.icmpouterrors = value
                self.icmpouterrors.value_namespace = name_space
                self.icmpouterrors.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutMsgs"):
                self.icmpoutmsgs = value
                self.icmpoutmsgs.value_namespace = name_space
                self.icmpoutmsgs.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutParmProbs"):
                self.icmpoutparmprobs = value
                self.icmpoutparmprobs.value_namespace = name_space
                self.icmpoutparmprobs.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutRedirects"):
                self.icmpoutredirects = value
                self.icmpoutredirects.value_namespace = name_space
                self.icmpoutredirects.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutSrcQuenchs"):
                self.icmpoutsrcquenchs = value
                self.icmpoutsrcquenchs.value_namespace = name_space
                self.icmpoutsrcquenchs.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutTimeExcds"):
                self.icmpouttimeexcds = value
                self.icmpouttimeexcds.value_namespace = name_space
                self.icmpouttimeexcds.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutTimestampReps"):
                self.icmpouttimestampreps = value
                self.icmpouttimestampreps.value_namespace = name_space
                self.icmpouttimestampreps.value_namespace_prefix = name_space_prefix
            if(value_path == "icmpOutTimestamps"):
                self.icmpouttimestamps = value
                self.icmpouttimestamps.value_namespace = name_space
                self.icmpouttimestamps.value_namespace_prefix = name_space_prefix


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
        	**type**\: list of    :py:class:`Ipaddrentry <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipaddrtable.Ipaddrentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IpMib.Ipaddrtable, self).__init__()

            self.yang_name = "ipAddrTable"
            self.yang_parent_name = "IP-MIB"

            self.ipaddrentry = YList(self)

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
                        super(IpMib.Ipaddrtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpMib.Ipaddrtable, self).__setattr__(name, value)


        class Ipaddrentry(Entity):
            """
            The addressing information for one of this entity's IPv4
            addresses.
            
            .. attribute:: ipadentaddr  <key>
            
            	The IPv4 address to which this entry's addressing information pertains
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: ipadentbcastaddr
            
            	The value of the least\-significant bit in the IPv4 broadcast address used for sending datagrams on the (logical) interface associated with the IPv4 address of this entry. For example, when the Internet standard all\-ones broadcast address is used, the value will be 1.  This value applies to both the subnet and network broadcast addresses used by the entity on this (logical) interface
            	**type**\:  int
            
            	**range:** 0..1
            
            	**status**\: deprecated
            
            .. attribute:: ipadentifindex
            
            	The index value which uniquely identifies the interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: ipadentnetmask
            
            	The subnet mask associated with the IPv4 address of this entry.  The value of the mask is an IPv4 address with all the network bits set to 1 and all the hosts bits set to 0
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: ipadentreasmmaxsize
            
            	The size of the largest IPv4 datagram which this entity can re\-assemble from incoming IPv4 fragmented datagrams received on this interface
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IpMib.Ipaddrtable.Ipaddrentry, self).__init__()

                self.yang_name = "ipAddrEntry"
                self.yang_parent_name = "ipAddrTable"

                self.ipadentaddr = YLeaf(YType.str, "ipAdEntAddr")

                self.ipadentbcastaddr = YLeaf(YType.int32, "ipAdEntBcastAddr")

                self.ipadentifindex = YLeaf(YType.int32, "ipAdEntIfIndex")

                self.ipadentnetmask = YLeaf(YType.str, "ipAdEntNetMask")

                self.ipadentreasmmaxsize = YLeaf(YType.int32, "ipAdEntReasmMaxSize")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipadentaddr",
                                "ipadentbcastaddr",
                                "ipadentifindex",
                                "ipadentnetmask",
                                "ipadentreasmmaxsize") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpMib.Ipaddrtable.Ipaddrentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpMib.Ipaddrtable.Ipaddrentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ipadentaddr.is_set or
                    self.ipadentbcastaddr.is_set or
                    self.ipadentifindex.is_set or
                    self.ipadentnetmask.is_set or
                    self.ipadentreasmmaxsize.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipadentaddr.yfilter != YFilter.not_set or
                    self.ipadentbcastaddr.yfilter != YFilter.not_set or
                    self.ipadentifindex.yfilter != YFilter.not_set or
                    self.ipadentnetmask.yfilter != YFilter.not_set or
                    self.ipadentreasmmaxsize.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipAddrEntry" + "[ipAdEntAddr='" + self.ipadentaddr.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IP-MIB:IP-MIB/ipAddrTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipadentaddr.is_set or self.ipadentaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipadentaddr.get_name_leafdata())
                if (self.ipadentbcastaddr.is_set or self.ipadentbcastaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipadentbcastaddr.get_name_leafdata())
                if (self.ipadentifindex.is_set or self.ipadentifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipadentifindex.get_name_leafdata())
                if (self.ipadentnetmask.is_set or self.ipadentnetmask.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipadentnetmask.get_name_leafdata())
                if (self.ipadentreasmmaxsize.is_set or self.ipadentreasmmaxsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipadentreasmmaxsize.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipAdEntAddr" or name == "ipAdEntBcastAddr" or name == "ipAdEntIfIndex" or name == "ipAdEntNetMask" or name == "ipAdEntReasmMaxSize"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipAdEntAddr"):
                    self.ipadentaddr = value
                    self.ipadentaddr.value_namespace = name_space
                    self.ipadentaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAdEntBcastAddr"):
                    self.ipadentbcastaddr = value
                    self.ipadentbcastaddr.value_namespace = name_space
                    self.ipadentbcastaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAdEntIfIndex"):
                    self.ipadentifindex = value
                    self.ipadentifindex.value_namespace = name_space
                    self.ipadentifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAdEntNetMask"):
                    self.ipadentnetmask = value
                    self.ipadentnetmask.value_namespace = name_space
                    self.ipadentnetmask.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAdEntReasmMaxSize"):
                    self.ipadentreasmmaxsize = value
                    self.ipadentreasmmaxsize.value_namespace = name_space
                    self.ipadentreasmmaxsize.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipaddrentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipaddrentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipAddrTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-MIB:IP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipAddrEntry"):
                for c in self.ipaddrentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpMib.Ipaddrtable.Ipaddrentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipaddrentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipAddrEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ipnettomediatable(Entity):
        """
        The IPv4 Address Translation table used for mapping from
        IPv4 addresses to physical addresses.
        
        This table has been deprecated, as a new IP version\-neutral
        table has been added.  It is loosely replaced by the
        ipNetToPhysicalTable.
        
        .. attribute:: ipnettomediaentry
        
        	Each entry contains one IpAddress to `physical' address equivalence
        	**type**\: list of    :py:class:`Ipnettomediaentry <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipnettomediatable.Ipnettomediaentry>`
        
        	**status**\: deprecated
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IpMib.Ipnettomediatable, self).__init__()

            self.yang_name = "ipNetToMediaTable"
            self.yang_parent_name = "IP-MIB"

            self.ipnettomediaentry = YList(self)

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
                        super(IpMib.Ipnettomediatable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpMib.Ipnettomediatable, self).__setattr__(name, value)


        class Ipnettomediaentry(Entity):
            """
            Each entry contains one IpAddress to `physical' address
            equivalence.
            
            .. attribute:: ipnettomediaifindex  <key>
            
            	The interface on which this entry's equivalence is effective.  The interface identified by a particular value of this index is the same interface as identified by the   same value of the IF\-MIB's ifIndex.  This object predates the rule limiting index objects to a max access value of 'not\-accessible' and so continues to use a value of 'read\-create'
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**status**\: deprecated
            
            .. attribute:: ipnettomedianetaddress  <key>
            
            	The IpAddress corresponding to the media\-dependent `physical' address.  This object predates the rule limiting index objects to a max access value of 'not\-accessible' and so continues to use a value of 'read\-create'
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            	**status**\: deprecated
            
            .. attribute:: ipnettomediaphysaddress
            
            	The media\-dependent `physical' address.  This object should return 0 when this entry is in the 'incomplete' state.  As the entries in this table are typically not persistent when this object is written the entity should not save the change to non\-volatile storage.  Note\: a stronger requirement is not used because this object was previously defined
            	**type**\:  str
            
            	**length:** 0..65535
            
            	**status**\: deprecated
            
            .. attribute:: ipnettomediatype
            
            	The type of mapping.  Setting this object to the value invalid(2) has the effect   of invalidating the corresponding entry in the ipNetToMediaTable.  That is, it effectively dis\-associates the interface identified with said entry from the mapping identified with said entry.  It is an implementation\- specific matter as to whether the agent removes an invalidated entry from the table.  Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use.  Proper interpretation of such entries requires examination of the relevant ipNetToMediaType object.  As the entries in this table are typically not persistent when this object is written the entity should not save the change to non\-volatile storage.  Note\: a stronger requirement is not used because this object was previously defined
            	**type**\:   :py:class:`Ipnettomediatype <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipnettomediatable.Ipnettomediaentry.Ipnettomediatype>`
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IpMib.Ipnettomediatable.Ipnettomediaentry, self).__init__()

                self.yang_name = "ipNetToMediaEntry"
                self.yang_parent_name = "ipNetToMediaTable"

                self.ipnettomediaifindex = YLeaf(YType.int32, "ipNetToMediaIfIndex")

                self.ipnettomedianetaddress = YLeaf(YType.str, "ipNetToMediaNetAddress")

                self.ipnettomediaphysaddress = YLeaf(YType.str, "ipNetToMediaPhysAddress")

                self.ipnettomediatype = YLeaf(YType.enumeration, "ipNetToMediaType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipnettomediaifindex",
                                "ipnettomedianetaddress",
                                "ipnettomediaphysaddress",
                                "ipnettomediatype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpMib.Ipnettomediatable.Ipnettomediaentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpMib.Ipnettomediatable.Ipnettomediaentry, self).__setattr__(name, value)

            class Ipnettomediatype(Enum):
                """
                Ipnettomediatype

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


            def has_data(self):
                return (
                    self.ipnettomediaifindex.is_set or
                    self.ipnettomedianetaddress.is_set or
                    self.ipnettomediaphysaddress.is_set or
                    self.ipnettomediatype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipnettomediaifindex.yfilter != YFilter.not_set or
                    self.ipnettomedianetaddress.yfilter != YFilter.not_set or
                    self.ipnettomediaphysaddress.yfilter != YFilter.not_set or
                    self.ipnettomediatype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipNetToMediaEntry" + "[ipNetToMediaIfIndex='" + self.ipnettomediaifindex.get() + "']" + "[ipNetToMediaNetAddress='" + self.ipnettomedianetaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IP-MIB:IP-MIB/ipNetToMediaTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipnettomediaifindex.is_set or self.ipnettomediaifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipnettomediaifindex.get_name_leafdata())
                if (self.ipnettomedianetaddress.is_set or self.ipnettomedianetaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipnettomedianetaddress.get_name_leafdata())
                if (self.ipnettomediaphysaddress.is_set or self.ipnettomediaphysaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipnettomediaphysaddress.get_name_leafdata())
                if (self.ipnettomediatype.is_set or self.ipnettomediatype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipnettomediatype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipNetToMediaIfIndex" or name == "ipNetToMediaNetAddress" or name == "ipNetToMediaPhysAddress" or name == "ipNetToMediaType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipNetToMediaIfIndex"):
                    self.ipnettomediaifindex = value
                    self.ipnettomediaifindex.value_namespace = name_space
                    self.ipnettomediaifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipNetToMediaNetAddress"):
                    self.ipnettomedianetaddress = value
                    self.ipnettomedianetaddress.value_namespace = name_space
                    self.ipnettomedianetaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ipNetToMediaPhysAddress"):
                    self.ipnettomediaphysaddress = value
                    self.ipnettomediaphysaddress.value_namespace = name_space
                    self.ipnettomediaphysaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ipNetToMediaType"):
                    self.ipnettomediatype = value
                    self.ipnettomediatype.value_namespace = name_space
                    self.ipnettomediatype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipnettomediaentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipnettomediaentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipNetToMediaTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-MIB:IP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipNetToMediaEntry"):
                for c in self.ipnettomediaentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpMib.Ipnettomediatable.Ipnettomediaentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipnettomediaentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipNetToMediaEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ipv4Interfacetable(Entity):
        """
        The table containing per\-interface IPv4\-specific
        information.
        
        .. attribute:: ipv4interfaceentry
        
        	An entry containing IPv4\-specific information for a specific interface
        	**type**\: list of    :py:class:`Ipv4Interfaceentry <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipv4Interfacetable.Ipv4Interfaceentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IpMib.Ipv4Interfacetable, self).__init__()

            self.yang_name = "ipv4InterfaceTable"
            self.yang_parent_name = "IP-MIB"

            self.ipv4interfaceentry = YList(self)

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
                        super(IpMib.Ipv4Interfacetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpMib.Ipv4Interfacetable, self).__setattr__(name, value)


        class Ipv4Interfaceentry(Entity):
            """
            An entry containing IPv4\-specific information for a specific
            interface.
            
            .. attribute:: ipv4interfaceifindex  <key>
            
            	The index value that uniquely identifies the interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipv4interfaceenablestatus
            
            	The indication of whether IPv4 is enabled (up) or disabled (down) on this interface.  This object does not affect the state of the interface itself, only its connection to an IPv4 stack.  The IF\-MIB should be used to control the state of the interface
            	**type**\:   :py:class:`Ipv4Interfaceenablestatus <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipv4Interfacetable.Ipv4Interfaceentry.Ipv4Interfaceenablestatus>`
            
            .. attribute:: ipv4interfacereasmmaxsize
            
            	The size of the largest IPv4 datagram that this entity can re\-assemble from incoming IPv4 fragmented datagrams received on this interface
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: ipv4interfaceretransmittime
            
            	The time between retransmissions of ARP requests to a neighbor when resolving the address or when probing the reachability of a neighbor
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IpMib.Ipv4Interfacetable.Ipv4Interfaceentry, self).__init__()

                self.yang_name = "ipv4InterfaceEntry"
                self.yang_parent_name = "ipv4InterfaceTable"

                self.ipv4interfaceifindex = YLeaf(YType.int32, "ipv4InterfaceIfIndex")

                self.ipv4interfaceenablestatus = YLeaf(YType.enumeration, "ipv4InterfaceEnableStatus")

                self.ipv4interfacereasmmaxsize = YLeaf(YType.int32, "ipv4InterfaceReasmMaxSize")

                self.ipv4interfaceretransmittime = YLeaf(YType.uint32, "ipv4InterfaceRetransmitTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipv4interfaceifindex",
                                "ipv4interfaceenablestatus",
                                "ipv4interfacereasmmaxsize",
                                "ipv4interfaceretransmittime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpMib.Ipv4Interfacetable.Ipv4Interfaceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpMib.Ipv4Interfacetable.Ipv4Interfaceentry, self).__setattr__(name, value)

            class Ipv4Interfaceenablestatus(Enum):
                """
                Ipv4Interfaceenablestatus

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


            def has_data(self):
                return (
                    self.ipv4interfaceifindex.is_set or
                    self.ipv4interfaceenablestatus.is_set or
                    self.ipv4interfacereasmmaxsize.is_set or
                    self.ipv4interfaceretransmittime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipv4interfaceifindex.yfilter != YFilter.not_set or
                    self.ipv4interfaceenablestatus.yfilter != YFilter.not_set or
                    self.ipv4interfacereasmmaxsize.yfilter != YFilter.not_set or
                    self.ipv4interfaceretransmittime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv4InterfaceEntry" + "[ipv4InterfaceIfIndex='" + self.ipv4interfaceifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IP-MIB:IP-MIB/ipv4InterfaceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipv4interfaceifindex.is_set or self.ipv4interfaceifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv4interfaceifindex.get_name_leafdata())
                if (self.ipv4interfaceenablestatus.is_set or self.ipv4interfaceenablestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv4interfaceenablestatus.get_name_leafdata())
                if (self.ipv4interfacereasmmaxsize.is_set or self.ipv4interfacereasmmaxsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv4interfacereasmmaxsize.get_name_leafdata())
                if (self.ipv4interfaceretransmittime.is_set or self.ipv4interfaceretransmittime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv4interfaceretransmittime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv4InterfaceIfIndex" or name == "ipv4InterfaceEnableStatus" or name == "ipv4InterfaceReasmMaxSize" or name == "ipv4InterfaceRetransmitTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipv4InterfaceIfIndex"):
                    self.ipv4interfaceifindex = value
                    self.ipv4interfaceifindex.value_namespace = name_space
                    self.ipv4interfaceifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv4InterfaceEnableStatus"):
                    self.ipv4interfaceenablestatus = value
                    self.ipv4interfaceenablestatus.value_namespace = name_space
                    self.ipv4interfaceenablestatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv4InterfaceReasmMaxSize"):
                    self.ipv4interfacereasmmaxsize = value
                    self.ipv4interfacereasmmaxsize.value_namespace = name_space
                    self.ipv4interfacereasmmaxsize.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv4InterfaceRetransmitTime"):
                    self.ipv4interfaceretransmittime = value
                    self.ipv4interfaceretransmittime.value_namespace = name_space
                    self.ipv4interfaceretransmittime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipv4interfaceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipv4interfaceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipv4InterfaceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-MIB:IP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipv4InterfaceEntry"):
                for c in self.ipv4interfaceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpMib.Ipv4Interfacetable.Ipv4Interfaceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipv4interfaceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipv4InterfaceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ipv6Interfacetable(Entity):
        """
        The table containing per\-interface IPv6\-specific
        information.
        
        .. attribute:: ipv6interfaceentry
        
        	An entry containing IPv6\-specific information for a given interface
        	**type**\: list of    :py:class:`Ipv6Interfaceentry <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipv6Interfacetable.Ipv6Interfaceentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IpMib.Ipv6Interfacetable, self).__init__()

            self.yang_name = "ipv6InterfaceTable"
            self.yang_parent_name = "IP-MIB"

            self.ipv6interfaceentry = YList(self)

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
                        super(IpMib.Ipv6Interfacetable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpMib.Ipv6Interfacetable, self).__setattr__(name, value)


        class Ipv6Interfaceentry(Entity):
            """
            An entry containing IPv6\-specific information for a given
            interface.
            
            .. attribute:: ipv6interfaceifindex  <key>
            
            	The index value that uniquely identifies the interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipv6interfaceenablestatus
            
            	The indication of whether IPv6 is enabled (up) or disabled (down) on this interface.  This object does not affect the state of the interface itself, only its connection to an IPv6 stack.  The IF\-MIB should be used to control the state of the interface.  When this object is written, the entity SHOULD save the change to non\-volatile storage and restore the object from non\-volatile storage upon re\-initialization of the system
            	**type**\:   :py:class:`Ipv6Interfaceenablestatus <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipv6Interfacetable.Ipv6Interfaceentry.Ipv6Interfaceenablestatus>`
            
            .. attribute:: ipv6interfaceforwarding
            
            	The indication of whether this entity is acting as an IPv6 router on this interface with respect to the forwarding of datagrams received by, but not addressed to, this entity. IPv6 routers forward datagrams.  IPv6 hosts do not (except those source\-routed via the host).  This object is constrained by ipv6IpForwarding and is ignored if ipv6IpForwarding is set to notForwarding.  Those systems that do not provide per\-interface control of the forwarding function should set this object to forwarding for all interfaces and allow the ipv6IpForwarding object to control the forwarding capability.  When this object is written, the entity SHOULD save the change to non\-volatile storage and restore the object from non\-volatile storage upon re\-initialization of the system
            	**type**\:   :py:class:`Ipv6Interfaceforwarding <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipv6Interfacetable.Ipv6Interfaceentry.Ipv6Interfaceforwarding>`
            
            .. attribute:: ipv6interfaceidentifier
            
            	The Interface Identifier for this interface.  The Interface Identifier is combined with an address prefix to form an interface address.  By default, the Interface Identifier is auto\-configured according to the rules of the link type to which this interface is attached.   A zero length identifier may be used where appropriate.  One possible example is a loopback interface
            	**type**\:  str
            
            .. attribute:: ipv6interfacereachabletime
            
            	The time a neighbor is considered reachable after receiving a reachability confirmation
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: ipv6interfacereasmmaxsize
            
            	The size of the largest IPv6 datagram that this entity can re\-assemble from incoming IPv6 fragmented datagrams received on this interface
            	**type**\:  int
            
            	**range:** 1500..65535
            
            	**units**\: octets
            
            .. attribute:: ipv6interfaceretransmittime
            
            	The time between retransmissions of Neighbor Solicitation messages to a neighbor when resolving the address or when probing the reachability of a neighbor
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IpMib.Ipv6Interfacetable.Ipv6Interfaceentry, self).__init__()

                self.yang_name = "ipv6InterfaceEntry"
                self.yang_parent_name = "ipv6InterfaceTable"

                self.ipv6interfaceifindex = YLeaf(YType.int32, "ipv6InterfaceIfIndex")

                self.ipv6interfaceenablestatus = YLeaf(YType.enumeration, "ipv6InterfaceEnableStatus")

                self.ipv6interfaceforwarding = YLeaf(YType.enumeration, "ipv6InterfaceForwarding")

                self.ipv6interfaceidentifier = YLeaf(YType.str, "ipv6InterfaceIdentifier")

                self.ipv6interfacereachabletime = YLeaf(YType.uint32, "ipv6InterfaceReachableTime")

                self.ipv6interfacereasmmaxsize = YLeaf(YType.uint32, "ipv6InterfaceReasmMaxSize")

                self.ipv6interfaceretransmittime = YLeaf(YType.uint32, "ipv6InterfaceRetransmitTime")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipv6interfaceifindex",
                                "ipv6interfaceenablestatus",
                                "ipv6interfaceforwarding",
                                "ipv6interfaceidentifier",
                                "ipv6interfacereachabletime",
                                "ipv6interfacereasmmaxsize",
                                "ipv6interfaceretransmittime") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpMib.Ipv6Interfacetable.Ipv6Interfaceentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpMib.Ipv6Interfacetable.Ipv6Interfaceentry, self).__setattr__(name, value)

            class Ipv6Interfaceenablestatus(Enum):
                """
                Ipv6Interfaceenablestatus

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
                Ipv6Interfaceforwarding

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


            def has_data(self):
                return (
                    self.ipv6interfaceifindex.is_set or
                    self.ipv6interfaceenablestatus.is_set or
                    self.ipv6interfaceforwarding.is_set or
                    self.ipv6interfaceidentifier.is_set or
                    self.ipv6interfacereachabletime.is_set or
                    self.ipv6interfacereasmmaxsize.is_set or
                    self.ipv6interfaceretransmittime.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipv6interfaceifindex.yfilter != YFilter.not_set or
                    self.ipv6interfaceenablestatus.yfilter != YFilter.not_set or
                    self.ipv6interfaceforwarding.yfilter != YFilter.not_set or
                    self.ipv6interfaceidentifier.yfilter != YFilter.not_set or
                    self.ipv6interfacereachabletime.yfilter != YFilter.not_set or
                    self.ipv6interfacereasmmaxsize.yfilter != YFilter.not_set or
                    self.ipv6interfaceretransmittime.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv6InterfaceEntry" + "[ipv6InterfaceIfIndex='" + self.ipv6interfaceifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IP-MIB:IP-MIB/ipv6InterfaceTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipv6interfaceifindex.is_set or self.ipv6interfaceifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6interfaceifindex.get_name_leafdata())
                if (self.ipv6interfaceenablestatus.is_set or self.ipv6interfaceenablestatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6interfaceenablestatus.get_name_leafdata())
                if (self.ipv6interfaceforwarding.is_set or self.ipv6interfaceforwarding.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6interfaceforwarding.get_name_leafdata())
                if (self.ipv6interfaceidentifier.is_set or self.ipv6interfaceidentifier.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6interfaceidentifier.get_name_leafdata())
                if (self.ipv6interfacereachabletime.is_set or self.ipv6interfacereachabletime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6interfacereachabletime.get_name_leafdata())
                if (self.ipv6interfacereasmmaxsize.is_set or self.ipv6interfacereasmmaxsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6interfacereasmmaxsize.get_name_leafdata())
                if (self.ipv6interfaceretransmittime.is_set or self.ipv6interfaceretransmittime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6interfaceretransmittime.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv6InterfaceIfIndex" or name == "ipv6InterfaceEnableStatus" or name == "ipv6InterfaceForwarding" or name == "ipv6InterfaceIdentifier" or name == "ipv6InterfaceReachableTime" or name == "ipv6InterfaceReasmMaxSize" or name == "ipv6InterfaceRetransmitTime"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipv6InterfaceIfIndex"):
                    self.ipv6interfaceifindex = value
                    self.ipv6interfaceifindex.value_namespace = name_space
                    self.ipv6interfaceifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6InterfaceEnableStatus"):
                    self.ipv6interfaceenablestatus = value
                    self.ipv6interfaceenablestatus.value_namespace = name_space
                    self.ipv6interfaceenablestatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6InterfaceForwarding"):
                    self.ipv6interfaceforwarding = value
                    self.ipv6interfaceforwarding.value_namespace = name_space
                    self.ipv6interfaceforwarding.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6InterfaceIdentifier"):
                    self.ipv6interfaceidentifier = value
                    self.ipv6interfaceidentifier.value_namespace = name_space
                    self.ipv6interfaceidentifier.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6InterfaceReachableTime"):
                    self.ipv6interfacereachabletime = value
                    self.ipv6interfacereachabletime.value_namespace = name_space
                    self.ipv6interfacereachabletime.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6InterfaceReasmMaxSize"):
                    self.ipv6interfacereasmmaxsize = value
                    self.ipv6interfacereasmmaxsize.value_namespace = name_space
                    self.ipv6interfacereasmmaxsize.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6InterfaceRetransmitTime"):
                    self.ipv6interfaceretransmittime = value
                    self.ipv6interfaceretransmittime.value_namespace = name_space
                    self.ipv6interfaceretransmittime.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipv6interfaceentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipv6interfaceentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipv6InterfaceTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-MIB:IP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipv6InterfaceEntry"):
                for c in self.ipv6interfaceentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpMib.Ipv6Interfacetable.Ipv6Interfaceentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipv6interfaceentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipv6InterfaceEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Ipsystemstatsentry <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipsystemstatstable.Ipsystemstatsentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IpMib.Ipsystemstatstable, self).__init__()

            self.yang_name = "ipSystemStatsTable"
            self.yang_parent_name = "IP-MIB"

            self.ipsystemstatsentry = YList(self)

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
                        super(IpMib.Ipsystemstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpMib.Ipsystemstatstable, self).__setattr__(name, value)


        class Ipsystemstatsentry(Entity):
            """
            A statistics entry containing system\-wide objects for a
            particular IP version.
            
            .. attribute:: ipsystemstatsipversion  <key>
            
            	The IP version of this row
            	**type**\:   :py:class:`IpVersion <ydk.models.ietf.ietf_inet_types.IpVersion>`
            
            .. attribute:: ipsystemstatsdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this entry's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\- initialization of the local management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatshcinbcastpkts
            
            	The number of IP broadcast datagrams received.  This object counts the same datagrams as ipSystemStatsInBcastPkts but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of   ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatshcindelivers
            
            	The total number of datagrams successfully delivered to IP user\-protocols (including ICMP).  This object counts the same packets as ipSystemStatsInDelivers, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatshcinforwdatagrams
            
            	The number of input datagrams for which this entity was not their final IP destination and for which this entity attempted to find a route to forward them to that final destination.  This object counts the same packets as ipSystemStatsInForwDatagrams, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatshcinmcastoctets
            
            	The total number of octets received in IP multicast datagrams.  This object counts the same octets as ipSystemStatsInMcastOctets, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatshcinmcastpkts
            
            	The number of IP multicast datagrams received.  This object counts the same datagrams as ipSystemStatsInMcastPkts but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatshcinoctets
            
            	The total number of octets received in input IP datagrams, including those received in error.  This object counts the same octets as ipSystemStatsInOctets, but allows for larger   values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatshcinreceives
            
            	The total number of input IP datagrams received, including those received in error.  This object counts the same datagrams as ipSystemStatsInReceives, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatshcoutbcastpkts
            
            	The number of IP broadcast datagrams transmitted.  This object counts the same datagrams as ipSystemStatsOutBcastPkts, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatshcoutforwdatagrams
            
            	The number of datagrams for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination.  This object counts the same packets as ipSystemStatsOutForwDatagrams, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatshcoutmcastoctets
            
            	The total number of octets transmitted in IP multicast datagrams.  This object counts the same octets as ipSystemStatsOutMcastOctets, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatshcoutmcastpkts
            
            	The number of IP multicast datagrams transmitted.  This object counts the same datagrams as ipSystemStatsOutMcastPkts, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatshcoutoctets
            
            	The total number of octets in IP datagrams delivered to the lower layers for transmission.  This objects counts the same octets as ipSystemStatsOutOctets, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of   ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatshcoutrequests
            
            	The total number of IP datagrams that local IP user\- protocols (including ICMP) supplied to IP in requests for transmission.  This object counts the same packets as ipSystemStatsOutRequests, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatshcouttransmits
            
            	The total number of IP datagrams that this entity supplied to the lower layers for transmission.  This object counts the same datagrams as ipSystemStatsOutTransmits, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipsystemstatsinaddrerrors
            
            	The number of input IP datagrams discarded because the IP address in their IP header's destination field was not a valid address to be received at this entity.  This count includes invalid addresses (e.g., \:\:0).  For entities that are not IP routers and therefore do not forward   datagrams, this counter includes datagrams discarded because the destination address was not a local address.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsinbcastpkts
            
            	The number of IP broadcast datagrams received.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsindelivers
            
            	The total number of datagrams successfully delivered to IP user\-protocols (including ICMP).  When tracking interface statistics, the counter of the interface to which these datagrams were addressed is incremented.  This interface might not be the same as the input interface for some of the datagrams.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsindiscards
            
            	The number of input IP datagrams for which no problems were encountered to prevent their continued processing, but were discarded (e.g., for lack of buffer space).  Note that this counter does not include any datagrams discarded while awaiting re\-assembly.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsinforwdatagrams
            
            	The number of input datagrams for which this entity was not their final IP destination and for which this entity attempted to find a route to forward them to that final destination.  In entities that do not act as IP routers, this counter will include only those datagrams that were Source\-Routed via this entity, and the Source\-Route processing was successful.  When tracking interface statistics, the counter of the incoming interface is incremented for each datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsinhdrerrors
            
            	The number of input IP datagrams discarded due to errors in their IP headers, including version number mismatch, other format errors, hop count exceeded, errors discovered in processing their IP options, etc.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsinmcastoctets
            
            	The total number of octets received in IP multicast datagrams.  Octets from datagrams counted in ipSystemStatsInMcastPkts MUST be counted here.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsinmcastpkts
            
            	The number of IP multicast datagrams received.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsinnoroutes
            
            	The number of input IP datagrams discarded because no route could be found to transmit them to their destination.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsinoctets
            
            	The total number of octets received in input IP datagrams, including those received in error.  Octets from datagrams counted in ipSystemStatsInReceives MUST be counted here.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsinreceives
            
            	The total number of input IP datagrams received, including those received in error.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsintruncatedpkts
            
            	The number of input IP datagrams discarded because the datagram frame didn't carry enough data.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsinunknownprotos
            
            	The number of locally\-addressed IP datagrams received successfully but discarded because of an unknown or unsupported protocol.  When tracking interface statistics, the counter of the interface to which these datagrams were addressed is incremented.  This interface might not be the same as the input interface for some of the datagrams.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsoutbcastpkts
            
            	The number of IP broadcast datagrams transmitted.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsoutdiscards
            
            	The number of output IP datagrams for which no problem was encountered to prevent their transmission to their destination, but were discarded (e.g., for lack of buffer space).  Note that this counter would include   datagrams counted in ipSystemStatsOutForwDatagrams if any such datagrams met this (discretionary) discard criterion.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsoutforwdatagrams
            
            	The number of datagrams for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination.  In entities that do not act as IP routers, this counter will include only those datagrams that were Source\-Routed via this entity, and the Source\-Route processing was successful.  When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully forwarded datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsoutfragcreates
            
            	The number of output datagram fragments that have been generated as a result of IP fragmentation.  When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully fragmented datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsoutfragfails
            
            	The number of IP datagrams that have been discarded because they needed to be fragmented but could not be.  This includes IPv4 packets that have the DF bit set and IPv6 packets that are being forwarded and exceed the outgoing link MTU.  When tracking interface statistics, the counter of the outgoing interface is incremented for an unsuccessfully fragmented datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsoutfragoks
            
            	The number of IP datagrams that have been successfully fragmented.  When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully fragmented datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsoutfragreqds
            
            	The number of IP datagrams that would require fragmentation in order to be transmitted.  When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully fragmented datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsoutmcastoctets
            
            	The total number of octets transmitted in IP multicast datagrams.  Octets from datagrams counted in   ipSystemStatsOutMcastPkts MUST be counted here.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsoutmcastpkts
            
            	The number of IP multicast datagrams transmitted.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsoutnoroutes
            
            	The number of locally generated IP datagrams discarded because no route could be found to transmit them to their destination.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsoutoctets
            
            	The total number of octets in IP datagrams delivered to the lower layers for transmission.  Octets from datagrams counted in ipSystemStatsOutTransmits MUST be counted here.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsoutrequests
            
            	The total number of IP datagrams that local IP user\- protocols (including ICMP) supplied to IP in requests for transmission.  Note that this counter does not include any datagrams counted in ipSystemStatsOutForwDatagrams.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsouttransmits
            
            	The total number of IP datagrams that this entity supplied to the lower layers for transmission.  This includes datagrams generated locally and those forwarded by this entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other   times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsreasmfails
            
            	The number of failures detected by the IP re\-assembly algorithm (for whatever reason\: timed out, errors, etc.). Note that this is not necessarily a count of discarded IP fragments since some algorithms (notably the algorithm in RFC 815) can lose track of the number of fragments by combining them as they are received.  When tracking interface statistics, the counter of the interface to which these fragments were addressed is incremented.  This interface might not be the same as the input interface for some of the fragments.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsreasmoks
            
            	The number of IP datagrams successfully reassembled.  When tracking interface statistics, the counter of the interface to which these datagrams were addressed is incremented.  This interface might not be the same as the input interface for some of the datagrams.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsreasmreqds
            
            	The number of IP fragments received that needed to be reassembled at this interface.  When tracking interface statistics, the counter of the interface to which these fragments were addressed is incremented.  This interface might not be the same as the input interface for some of the fragments.  Discontinuities in the value of this counter can occur at   re\-initialization of the management system, and at other times as indicated by the value of ipSystemStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipsystemstatsrefreshrate
            
            	The minimum reasonable polling interval for this entry. This object provides an indication of the minimum amount of time required to update the counters in this entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milli-seconds
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IpMib.Ipsystemstatstable.Ipsystemstatsentry, self).__init__()

                self.yang_name = "ipSystemStatsEntry"
                self.yang_parent_name = "ipSystemStatsTable"

                self.ipsystemstatsipversion = YLeaf(YType.enumeration, "ipSystemStatsIPVersion")

                self.ipsystemstatsdiscontinuitytime = YLeaf(YType.uint32, "ipSystemStatsDiscontinuityTime")

                self.ipsystemstatshcinbcastpkts = YLeaf(YType.uint64, "ipSystemStatsHCInBcastPkts")

                self.ipsystemstatshcindelivers = YLeaf(YType.uint64, "ipSystemStatsHCInDelivers")

                self.ipsystemstatshcinforwdatagrams = YLeaf(YType.uint64, "ipSystemStatsHCInForwDatagrams")

                self.ipsystemstatshcinmcastoctets = YLeaf(YType.uint64, "ipSystemStatsHCInMcastOctets")

                self.ipsystemstatshcinmcastpkts = YLeaf(YType.uint64, "ipSystemStatsHCInMcastPkts")

                self.ipsystemstatshcinoctets = YLeaf(YType.uint64, "ipSystemStatsHCInOctets")

                self.ipsystemstatshcinreceives = YLeaf(YType.uint64, "ipSystemStatsHCInReceives")

                self.ipsystemstatshcoutbcastpkts = YLeaf(YType.uint64, "ipSystemStatsHCOutBcastPkts")

                self.ipsystemstatshcoutforwdatagrams = YLeaf(YType.uint64, "ipSystemStatsHCOutForwDatagrams")

                self.ipsystemstatshcoutmcastoctets = YLeaf(YType.uint64, "ipSystemStatsHCOutMcastOctets")

                self.ipsystemstatshcoutmcastpkts = YLeaf(YType.uint64, "ipSystemStatsHCOutMcastPkts")

                self.ipsystemstatshcoutoctets = YLeaf(YType.uint64, "ipSystemStatsHCOutOctets")

                self.ipsystemstatshcoutrequests = YLeaf(YType.uint64, "ipSystemStatsHCOutRequests")

                self.ipsystemstatshcouttransmits = YLeaf(YType.uint64, "ipSystemStatsHCOutTransmits")

                self.ipsystemstatsinaddrerrors = YLeaf(YType.uint32, "ipSystemStatsInAddrErrors")

                self.ipsystemstatsinbcastpkts = YLeaf(YType.uint32, "ipSystemStatsInBcastPkts")

                self.ipsystemstatsindelivers = YLeaf(YType.uint32, "ipSystemStatsInDelivers")

                self.ipsystemstatsindiscards = YLeaf(YType.uint32, "ipSystemStatsInDiscards")

                self.ipsystemstatsinforwdatagrams = YLeaf(YType.uint32, "ipSystemStatsInForwDatagrams")

                self.ipsystemstatsinhdrerrors = YLeaf(YType.uint32, "ipSystemStatsInHdrErrors")

                self.ipsystemstatsinmcastoctets = YLeaf(YType.uint32, "ipSystemStatsInMcastOctets")

                self.ipsystemstatsinmcastpkts = YLeaf(YType.uint32, "ipSystemStatsInMcastPkts")

                self.ipsystemstatsinnoroutes = YLeaf(YType.uint32, "ipSystemStatsInNoRoutes")

                self.ipsystemstatsinoctets = YLeaf(YType.uint32, "ipSystemStatsInOctets")

                self.ipsystemstatsinreceives = YLeaf(YType.uint32, "ipSystemStatsInReceives")

                self.ipsystemstatsintruncatedpkts = YLeaf(YType.uint32, "ipSystemStatsInTruncatedPkts")

                self.ipsystemstatsinunknownprotos = YLeaf(YType.uint32, "ipSystemStatsInUnknownProtos")

                self.ipsystemstatsoutbcastpkts = YLeaf(YType.uint32, "ipSystemStatsOutBcastPkts")

                self.ipsystemstatsoutdiscards = YLeaf(YType.uint32, "ipSystemStatsOutDiscards")

                self.ipsystemstatsoutforwdatagrams = YLeaf(YType.uint32, "ipSystemStatsOutForwDatagrams")

                self.ipsystemstatsoutfragcreates = YLeaf(YType.uint32, "ipSystemStatsOutFragCreates")

                self.ipsystemstatsoutfragfails = YLeaf(YType.uint32, "ipSystemStatsOutFragFails")

                self.ipsystemstatsoutfragoks = YLeaf(YType.uint32, "ipSystemStatsOutFragOKs")

                self.ipsystemstatsoutfragreqds = YLeaf(YType.uint32, "ipSystemStatsOutFragReqds")

                self.ipsystemstatsoutmcastoctets = YLeaf(YType.uint32, "ipSystemStatsOutMcastOctets")

                self.ipsystemstatsoutmcastpkts = YLeaf(YType.uint32, "ipSystemStatsOutMcastPkts")

                self.ipsystemstatsoutnoroutes = YLeaf(YType.uint32, "ipSystemStatsOutNoRoutes")

                self.ipsystemstatsoutoctets = YLeaf(YType.uint32, "ipSystemStatsOutOctets")

                self.ipsystemstatsoutrequests = YLeaf(YType.uint32, "ipSystemStatsOutRequests")

                self.ipsystemstatsouttransmits = YLeaf(YType.uint32, "ipSystemStatsOutTransmits")

                self.ipsystemstatsreasmfails = YLeaf(YType.uint32, "ipSystemStatsReasmFails")

                self.ipsystemstatsreasmoks = YLeaf(YType.uint32, "ipSystemStatsReasmOKs")

                self.ipsystemstatsreasmreqds = YLeaf(YType.uint32, "ipSystemStatsReasmReqds")

                self.ipsystemstatsrefreshrate = YLeaf(YType.uint32, "ipSystemStatsRefreshRate")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipsystemstatsipversion",
                                "ipsystemstatsdiscontinuitytime",
                                "ipsystemstatshcinbcastpkts",
                                "ipsystemstatshcindelivers",
                                "ipsystemstatshcinforwdatagrams",
                                "ipsystemstatshcinmcastoctets",
                                "ipsystemstatshcinmcastpkts",
                                "ipsystemstatshcinoctets",
                                "ipsystemstatshcinreceives",
                                "ipsystemstatshcoutbcastpkts",
                                "ipsystemstatshcoutforwdatagrams",
                                "ipsystemstatshcoutmcastoctets",
                                "ipsystemstatshcoutmcastpkts",
                                "ipsystemstatshcoutoctets",
                                "ipsystemstatshcoutrequests",
                                "ipsystemstatshcouttransmits",
                                "ipsystemstatsinaddrerrors",
                                "ipsystemstatsinbcastpkts",
                                "ipsystemstatsindelivers",
                                "ipsystemstatsindiscards",
                                "ipsystemstatsinforwdatagrams",
                                "ipsystemstatsinhdrerrors",
                                "ipsystemstatsinmcastoctets",
                                "ipsystemstatsinmcastpkts",
                                "ipsystemstatsinnoroutes",
                                "ipsystemstatsinoctets",
                                "ipsystemstatsinreceives",
                                "ipsystemstatsintruncatedpkts",
                                "ipsystemstatsinunknownprotos",
                                "ipsystemstatsoutbcastpkts",
                                "ipsystemstatsoutdiscards",
                                "ipsystemstatsoutforwdatagrams",
                                "ipsystemstatsoutfragcreates",
                                "ipsystemstatsoutfragfails",
                                "ipsystemstatsoutfragoks",
                                "ipsystemstatsoutfragreqds",
                                "ipsystemstatsoutmcastoctets",
                                "ipsystemstatsoutmcastpkts",
                                "ipsystemstatsoutnoroutes",
                                "ipsystemstatsoutoctets",
                                "ipsystemstatsoutrequests",
                                "ipsystemstatsouttransmits",
                                "ipsystemstatsreasmfails",
                                "ipsystemstatsreasmoks",
                                "ipsystemstatsreasmreqds",
                                "ipsystemstatsrefreshrate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpMib.Ipsystemstatstable.Ipsystemstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpMib.Ipsystemstatstable.Ipsystemstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ipsystemstatsipversion.is_set or
                    self.ipsystemstatsdiscontinuitytime.is_set or
                    self.ipsystemstatshcinbcastpkts.is_set or
                    self.ipsystemstatshcindelivers.is_set or
                    self.ipsystemstatshcinforwdatagrams.is_set or
                    self.ipsystemstatshcinmcastoctets.is_set or
                    self.ipsystemstatshcinmcastpkts.is_set or
                    self.ipsystemstatshcinoctets.is_set or
                    self.ipsystemstatshcinreceives.is_set or
                    self.ipsystemstatshcoutbcastpkts.is_set or
                    self.ipsystemstatshcoutforwdatagrams.is_set or
                    self.ipsystemstatshcoutmcastoctets.is_set or
                    self.ipsystemstatshcoutmcastpkts.is_set or
                    self.ipsystemstatshcoutoctets.is_set or
                    self.ipsystemstatshcoutrequests.is_set or
                    self.ipsystemstatshcouttransmits.is_set or
                    self.ipsystemstatsinaddrerrors.is_set or
                    self.ipsystemstatsinbcastpkts.is_set or
                    self.ipsystemstatsindelivers.is_set or
                    self.ipsystemstatsindiscards.is_set or
                    self.ipsystemstatsinforwdatagrams.is_set or
                    self.ipsystemstatsinhdrerrors.is_set or
                    self.ipsystemstatsinmcastoctets.is_set or
                    self.ipsystemstatsinmcastpkts.is_set or
                    self.ipsystemstatsinnoroutes.is_set or
                    self.ipsystemstatsinoctets.is_set or
                    self.ipsystemstatsinreceives.is_set or
                    self.ipsystemstatsintruncatedpkts.is_set or
                    self.ipsystemstatsinunknownprotos.is_set or
                    self.ipsystemstatsoutbcastpkts.is_set or
                    self.ipsystemstatsoutdiscards.is_set or
                    self.ipsystemstatsoutforwdatagrams.is_set or
                    self.ipsystemstatsoutfragcreates.is_set or
                    self.ipsystemstatsoutfragfails.is_set or
                    self.ipsystemstatsoutfragoks.is_set or
                    self.ipsystemstatsoutfragreqds.is_set or
                    self.ipsystemstatsoutmcastoctets.is_set or
                    self.ipsystemstatsoutmcastpkts.is_set or
                    self.ipsystemstatsoutnoroutes.is_set or
                    self.ipsystemstatsoutoctets.is_set or
                    self.ipsystemstatsoutrequests.is_set or
                    self.ipsystemstatsouttransmits.is_set or
                    self.ipsystemstatsreasmfails.is_set or
                    self.ipsystemstatsreasmoks.is_set or
                    self.ipsystemstatsreasmreqds.is_set or
                    self.ipsystemstatsrefreshrate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipsystemstatsipversion.yfilter != YFilter.not_set or
                    self.ipsystemstatsdiscontinuitytime.yfilter != YFilter.not_set or
                    self.ipsystemstatshcinbcastpkts.yfilter != YFilter.not_set or
                    self.ipsystemstatshcindelivers.yfilter != YFilter.not_set or
                    self.ipsystemstatshcinforwdatagrams.yfilter != YFilter.not_set or
                    self.ipsystemstatshcinmcastoctets.yfilter != YFilter.not_set or
                    self.ipsystemstatshcinmcastpkts.yfilter != YFilter.not_set or
                    self.ipsystemstatshcinoctets.yfilter != YFilter.not_set or
                    self.ipsystemstatshcinreceives.yfilter != YFilter.not_set or
                    self.ipsystemstatshcoutbcastpkts.yfilter != YFilter.not_set or
                    self.ipsystemstatshcoutforwdatagrams.yfilter != YFilter.not_set or
                    self.ipsystemstatshcoutmcastoctets.yfilter != YFilter.not_set or
                    self.ipsystemstatshcoutmcastpkts.yfilter != YFilter.not_set or
                    self.ipsystemstatshcoutoctets.yfilter != YFilter.not_set or
                    self.ipsystemstatshcoutrequests.yfilter != YFilter.not_set or
                    self.ipsystemstatshcouttransmits.yfilter != YFilter.not_set or
                    self.ipsystemstatsinaddrerrors.yfilter != YFilter.not_set or
                    self.ipsystemstatsinbcastpkts.yfilter != YFilter.not_set or
                    self.ipsystemstatsindelivers.yfilter != YFilter.not_set or
                    self.ipsystemstatsindiscards.yfilter != YFilter.not_set or
                    self.ipsystemstatsinforwdatagrams.yfilter != YFilter.not_set or
                    self.ipsystemstatsinhdrerrors.yfilter != YFilter.not_set or
                    self.ipsystemstatsinmcastoctets.yfilter != YFilter.not_set or
                    self.ipsystemstatsinmcastpkts.yfilter != YFilter.not_set or
                    self.ipsystemstatsinnoroutes.yfilter != YFilter.not_set or
                    self.ipsystemstatsinoctets.yfilter != YFilter.not_set or
                    self.ipsystemstatsinreceives.yfilter != YFilter.not_set or
                    self.ipsystemstatsintruncatedpkts.yfilter != YFilter.not_set or
                    self.ipsystemstatsinunknownprotos.yfilter != YFilter.not_set or
                    self.ipsystemstatsoutbcastpkts.yfilter != YFilter.not_set or
                    self.ipsystemstatsoutdiscards.yfilter != YFilter.not_set or
                    self.ipsystemstatsoutforwdatagrams.yfilter != YFilter.not_set or
                    self.ipsystemstatsoutfragcreates.yfilter != YFilter.not_set or
                    self.ipsystemstatsoutfragfails.yfilter != YFilter.not_set or
                    self.ipsystemstatsoutfragoks.yfilter != YFilter.not_set or
                    self.ipsystemstatsoutfragreqds.yfilter != YFilter.not_set or
                    self.ipsystemstatsoutmcastoctets.yfilter != YFilter.not_set or
                    self.ipsystemstatsoutmcastpkts.yfilter != YFilter.not_set or
                    self.ipsystemstatsoutnoroutes.yfilter != YFilter.not_set or
                    self.ipsystemstatsoutoctets.yfilter != YFilter.not_set or
                    self.ipsystemstatsoutrequests.yfilter != YFilter.not_set or
                    self.ipsystemstatsouttransmits.yfilter != YFilter.not_set or
                    self.ipsystemstatsreasmfails.yfilter != YFilter.not_set or
                    self.ipsystemstatsreasmoks.yfilter != YFilter.not_set or
                    self.ipsystemstatsreasmreqds.yfilter != YFilter.not_set or
                    self.ipsystemstatsrefreshrate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipSystemStatsEntry" + "[ipSystemStatsIPVersion='" + self.ipsystemstatsipversion.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IP-MIB:IP-MIB/ipSystemStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipsystemstatsipversion.is_set or self.ipsystemstatsipversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsipversion.get_name_leafdata())
                if (self.ipsystemstatsdiscontinuitytime.is_set or self.ipsystemstatsdiscontinuitytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsdiscontinuitytime.get_name_leafdata())
                if (self.ipsystemstatshcinbcastpkts.is_set or self.ipsystemstatshcinbcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatshcinbcastpkts.get_name_leafdata())
                if (self.ipsystemstatshcindelivers.is_set or self.ipsystemstatshcindelivers.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatshcindelivers.get_name_leafdata())
                if (self.ipsystemstatshcinforwdatagrams.is_set or self.ipsystemstatshcinforwdatagrams.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatshcinforwdatagrams.get_name_leafdata())
                if (self.ipsystemstatshcinmcastoctets.is_set or self.ipsystemstatshcinmcastoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatshcinmcastoctets.get_name_leafdata())
                if (self.ipsystemstatshcinmcastpkts.is_set or self.ipsystemstatshcinmcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatshcinmcastpkts.get_name_leafdata())
                if (self.ipsystemstatshcinoctets.is_set or self.ipsystemstatshcinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatshcinoctets.get_name_leafdata())
                if (self.ipsystemstatshcinreceives.is_set or self.ipsystemstatshcinreceives.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatshcinreceives.get_name_leafdata())
                if (self.ipsystemstatshcoutbcastpkts.is_set or self.ipsystemstatshcoutbcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatshcoutbcastpkts.get_name_leafdata())
                if (self.ipsystemstatshcoutforwdatagrams.is_set or self.ipsystemstatshcoutforwdatagrams.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatshcoutforwdatagrams.get_name_leafdata())
                if (self.ipsystemstatshcoutmcastoctets.is_set or self.ipsystemstatshcoutmcastoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatshcoutmcastoctets.get_name_leafdata())
                if (self.ipsystemstatshcoutmcastpkts.is_set or self.ipsystemstatshcoutmcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatshcoutmcastpkts.get_name_leafdata())
                if (self.ipsystemstatshcoutoctets.is_set or self.ipsystemstatshcoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatshcoutoctets.get_name_leafdata())
                if (self.ipsystemstatshcoutrequests.is_set or self.ipsystemstatshcoutrequests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatshcoutrequests.get_name_leafdata())
                if (self.ipsystemstatshcouttransmits.is_set or self.ipsystemstatshcouttransmits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatshcouttransmits.get_name_leafdata())
                if (self.ipsystemstatsinaddrerrors.is_set or self.ipsystemstatsinaddrerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsinaddrerrors.get_name_leafdata())
                if (self.ipsystemstatsinbcastpkts.is_set or self.ipsystemstatsinbcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsinbcastpkts.get_name_leafdata())
                if (self.ipsystemstatsindelivers.is_set or self.ipsystemstatsindelivers.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsindelivers.get_name_leafdata())
                if (self.ipsystemstatsindiscards.is_set or self.ipsystemstatsindiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsindiscards.get_name_leafdata())
                if (self.ipsystemstatsinforwdatagrams.is_set or self.ipsystemstatsinforwdatagrams.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsinforwdatagrams.get_name_leafdata())
                if (self.ipsystemstatsinhdrerrors.is_set or self.ipsystemstatsinhdrerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsinhdrerrors.get_name_leafdata())
                if (self.ipsystemstatsinmcastoctets.is_set or self.ipsystemstatsinmcastoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsinmcastoctets.get_name_leafdata())
                if (self.ipsystemstatsinmcastpkts.is_set or self.ipsystemstatsinmcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsinmcastpkts.get_name_leafdata())
                if (self.ipsystemstatsinnoroutes.is_set or self.ipsystemstatsinnoroutes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsinnoroutes.get_name_leafdata())
                if (self.ipsystemstatsinoctets.is_set or self.ipsystemstatsinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsinoctets.get_name_leafdata())
                if (self.ipsystemstatsinreceives.is_set or self.ipsystemstatsinreceives.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsinreceives.get_name_leafdata())
                if (self.ipsystemstatsintruncatedpkts.is_set or self.ipsystemstatsintruncatedpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsintruncatedpkts.get_name_leafdata())
                if (self.ipsystemstatsinunknownprotos.is_set or self.ipsystemstatsinunknownprotos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsinunknownprotos.get_name_leafdata())
                if (self.ipsystemstatsoutbcastpkts.is_set or self.ipsystemstatsoutbcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsoutbcastpkts.get_name_leafdata())
                if (self.ipsystemstatsoutdiscards.is_set or self.ipsystemstatsoutdiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsoutdiscards.get_name_leafdata())
                if (self.ipsystemstatsoutforwdatagrams.is_set or self.ipsystemstatsoutforwdatagrams.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsoutforwdatagrams.get_name_leafdata())
                if (self.ipsystemstatsoutfragcreates.is_set or self.ipsystemstatsoutfragcreates.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsoutfragcreates.get_name_leafdata())
                if (self.ipsystemstatsoutfragfails.is_set or self.ipsystemstatsoutfragfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsoutfragfails.get_name_leafdata())
                if (self.ipsystemstatsoutfragoks.is_set or self.ipsystemstatsoutfragoks.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsoutfragoks.get_name_leafdata())
                if (self.ipsystemstatsoutfragreqds.is_set or self.ipsystemstatsoutfragreqds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsoutfragreqds.get_name_leafdata())
                if (self.ipsystemstatsoutmcastoctets.is_set or self.ipsystemstatsoutmcastoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsoutmcastoctets.get_name_leafdata())
                if (self.ipsystemstatsoutmcastpkts.is_set or self.ipsystemstatsoutmcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsoutmcastpkts.get_name_leafdata())
                if (self.ipsystemstatsoutnoroutes.is_set or self.ipsystemstatsoutnoroutes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsoutnoroutes.get_name_leafdata())
                if (self.ipsystemstatsoutoctets.is_set or self.ipsystemstatsoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsoutoctets.get_name_leafdata())
                if (self.ipsystemstatsoutrequests.is_set or self.ipsystemstatsoutrequests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsoutrequests.get_name_leafdata())
                if (self.ipsystemstatsouttransmits.is_set or self.ipsystemstatsouttransmits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsouttransmits.get_name_leafdata())
                if (self.ipsystemstatsreasmfails.is_set or self.ipsystemstatsreasmfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsreasmfails.get_name_leafdata())
                if (self.ipsystemstatsreasmoks.is_set or self.ipsystemstatsreasmoks.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsreasmoks.get_name_leafdata())
                if (self.ipsystemstatsreasmreqds.is_set or self.ipsystemstatsreasmreqds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsreasmreqds.get_name_leafdata())
                if (self.ipsystemstatsrefreshrate.is_set or self.ipsystemstatsrefreshrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipsystemstatsrefreshrate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipSystemStatsIPVersion" or name == "ipSystemStatsDiscontinuityTime" or name == "ipSystemStatsHCInBcastPkts" or name == "ipSystemStatsHCInDelivers" or name == "ipSystemStatsHCInForwDatagrams" or name == "ipSystemStatsHCInMcastOctets" or name == "ipSystemStatsHCInMcastPkts" or name == "ipSystemStatsHCInOctets" or name == "ipSystemStatsHCInReceives" or name == "ipSystemStatsHCOutBcastPkts" or name == "ipSystemStatsHCOutForwDatagrams" or name == "ipSystemStatsHCOutMcastOctets" or name == "ipSystemStatsHCOutMcastPkts" or name == "ipSystemStatsHCOutOctets" or name == "ipSystemStatsHCOutRequests" or name == "ipSystemStatsHCOutTransmits" or name == "ipSystemStatsInAddrErrors" or name == "ipSystemStatsInBcastPkts" or name == "ipSystemStatsInDelivers" or name == "ipSystemStatsInDiscards" or name == "ipSystemStatsInForwDatagrams" or name == "ipSystemStatsInHdrErrors" or name == "ipSystemStatsInMcastOctets" or name == "ipSystemStatsInMcastPkts" or name == "ipSystemStatsInNoRoutes" or name == "ipSystemStatsInOctets" or name == "ipSystemStatsInReceives" or name == "ipSystemStatsInTruncatedPkts" or name == "ipSystemStatsInUnknownProtos" or name == "ipSystemStatsOutBcastPkts" or name == "ipSystemStatsOutDiscards" or name == "ipSystemStatsOutForwDatagrams" or name == "ipSystemStatsOutFragCreates" or name == "ipSystemStatsOutFragFails" or name == "ipSystemStatsOutFragOKs" or name == "ipSystemStatsOutFragReqds" or name == "ipSystemStatsOutMcastOctets" or name == "ipSystemStatsOutMcastPkts" or name == "ipSystemStatsOutNoRoutes" or name == "ipSystemStatsOutOctets" or name == "ipSystemStatsOutRequests" or name == "ipSystemStatsOutTransmits" or name == "ipSystemStatsReasmFails" or name == "ipSystemStatsReasmOKs" or name == "ipSystemStatsReasmReqds" or name == "ipSystemStatsRefreshRate"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipSystemStatsIPVersion"):
                    self.ipsystemstatsipversion = value
                    self.ipsystemstatsipversion.value_namespace = name_space
                    self.ipsystemstatsipversion.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsDiscontinuityTime"):
                    self.ipsystemstatsdiscontinuitytime = value
                    self.ipsystemstatsdiscontinuitytime.value_namespace = name_space
                    self.ipsystemstatsdiscontinuitytime.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsHCInBcastPkts"):
                    self.ipsystemstatshcinbcastpkts = value
                    self.ipsystemstatshcinbcastpkts.value_namespace = name_space
                    self.ipsystemstatshcinbcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsHCInDelivers"):
                    self.ipsystemstatshcindelivers = value
                    self.ipsystemstatshcindelivers.value_namespace = name_space
                    self.ipsystemstatshcindelivers.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsHCInForwDatagrams"):
                    self.ipsystemstatshcinforwdatagrams = value
                    self.ipsystemstatshcinforwdatagrams.value_namespace = name_space
                    self.ipsystemstatshcinforwdatagrams.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsHCInMcastOctets"):
                    self.ipsystemstatshcinmcastoctets = value
                    self.ipsystemstatshcinmcastoctets.value_namespace = name_space
                    self.ipsystemstatshcinmcastoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsHCInMcastPkts"):
                    self.ipsystemstatshcinmcastpkts = value
                    self.ipsystemstatshcinmcastpkts.value_namespace = name_space
                    self.ipsystemstatshcinmcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsHCInOctets"):
                    self.ipsystemstatshcinoctets = value
                    self.ipsystemstatshcinoctets.value_namespace = name_space
                    self.ipsystemstatshcinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsHCInReceives"):
                    self.ipsystemstatshcinreceives = value
                    self.ipsystemstatshcinreceives.value_namespace = name_space
                    self.ipsystemstatshcinreceives.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsHCOutBcastPkts"):
                    self.ipsystemstatshcoutbcastpkts = value
                    self.ipsystemstatshcoutbcastpkts.value_namespace = name_space
                    self.ipsystemstatshcoutbcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsHCOutForwDatagrams"):
                    self.ipsystemstatshcoutforwdatagrams = value
                    self.ipsystemstatshcoutforwdatagrams.value_namespace = name_space
                    self.ipsystemstatshcoutforwdatagrams.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsHCOutMcastOctets"):
                    self.ipsystemstatshcoutmcastoctets = value
                    self.ipsystemstatshcoutmcastoctets.value_namespace = name_space
                    self.ipsystemstatshcoutmcastoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsHCOutMcastPkts"):
                    self.ipsystemstatshcoutmcastpkts = value
                    self.ipsystemstatshcoutmcastpkts.value_namespace = name_space
                    self.ipsystemstatshcoutmcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsHCOutOctets"):
                    self.ipsystemstatshcoutoctets = value
                    self.ipsystemstatshcoutoctets.value_namespace = name_space
                    self.ipsystemstatshcoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsHCOutRequests"):
                    self.ipsystemstatshcoutrequests = value
                    self.ipsystemstatshcoutrequests.value_namespace = name_space
                    self.ipsystemstatshcoutrequests.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsHCOutTransmits"):
                    self.ipsystemstatshcouttransmits = value
                    self.ipsystemstatshcouttransmits.value_namespace = name_space
                    self.ipsystemstatshcouttransmits.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsInAddrErrors"):
                    self.ipsystemstatsinaddrerrors = value
                    self.ipsystemstatsinaddrerrors.value_namespace = name_space
                    self.ipsystemstatsinaddrerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsInBcastPkts"):
                    self.ipsystemstatsinbcastpkts = value
                    self.ipsystemstatsinbcastpkts.value_namespace = name_space
                    self.ipsystemstatsinbcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsInDelivers"):
                    self.ipsystemstatsindelivers = value
                    self.ipsystemstatsindelivers.value_namespace = name_space
                    self.ipsystemstatsindelivers.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsInDiscards"):
                    self.ipsystemstatsindiscards = value
                    self.ipsystemstatsindiscards.value_namespace = name_space
                    self.ipsystemstatsindiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsInForwDatagrams"):
                    self.ipsystemstatsinforwdatagrams = value
                    self.ipsystemstatsinforwdatagrams.value_namespace = name_space
                    self.ipsystemstatsinforwdatagrams.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsInHdrErrors"):
                    self.ipsystemstatsinhdrerrors = value
                    self.ipsystemstatsinhdrerrors.value_namespace = name_space
                    self.ipsystemstatsinhdrerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsInMcastOctets"):
                    self.ipsystemstatsinmcastoctets = value
                    self.ipsystemstatsinmcastoctets.value_namespace = name_space
                    self.ipsystemstatsinmcastoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsInMcastPkts"):
                    self.ipsystemstatsinmcastpkts = value
                    self.ipsystemstatsinmcastpkts.value_namespace = name_space
                    self.ipsystemstatsinmcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsInNoRoutes"):
                    self.ipsystemstatsinnoroutes = value
                    self.ipsystemstatsinnoroutes.value_namespace = name_space
                    self.ipsystemstatsinnoroutes.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsInOctets"):
                    self.ipsystemstatsinoctets = value
                    self.ipsystemstatsinoctets.value_namespace = name_space
                    self.ipsystemstatsinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsInReceives"):
                    self.ipsystemstatsinreceives = value
                    self.ipsystemstatsinreceives.value_namespace = name_space
                    self.ipsystemstatsinreceives.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsInTruncatedPkts"):
                    self.ipsystemstatsintruncatedpkts = value
                    self.ipsystemstatsintruncatedpkts.value_namespace = name_space
                    self.ipsystemstatsintruncatedpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsInUnknownProtos"):
                    self.ipsystemstatsinunknownprotos = value
                    self.ipsystemstatsinunknownprotos.value_namespace = name_space
                    self.ipsystemstatsinunknownprotos.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsOutBcastPkts"):
                    self.ipsystemstatsoutbcastpkts = value
                    self.ipsystemstatsoutbcastpkts.value_namespace = name_space
                    self.ipsystemstatsoutbcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsOutDiscards"):
                    self.ipsystemstatsoutdiscards = value
                    self.ipsystemstatsoutdiscards.value_namespace = name_space
                    self.ipsystemstatsoutdiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsOutForwDatagrams"):
                    self.ipsystemstatsoutforwdatagrams = value
                    self.ipsystemstatsoutforwdatagrams.value_namespace = name_space
                    self.ipsystemstatsoutforwdatagrams.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsOutFragCreates"):
                    self.ipsystemstatsoutfragcreates = value
                    self.ipsystemstatsoutfragcreates.value_namespace = name_space
                    self.ipsystemstatsoutfragcreates.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsOutFragFails"):
                    self.ipsystemstatsoutfragfails = value
                    self.ipsystemstatsoutfragfails.value_namespace = name_space
                    self.ipsystemstatsoutfragfails.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsOutFragOKs"):
                    self.ipsystemstatsoutfragoks = value
                    self.ipsystemstatsoutfragoks.value_namespace = name_space
                    self.ipsystemstatsoutfragoks.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsOutFragReqds"):
                    self.ipsystemstatsoutfragreqds = value
                    self.ipsystemstatsoutfragreqds.value_namespace = name_space
                    self.ipsystemstatsoutfragreqds.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsOutMcastOctets"):
                    self.ipsystemstatsoutmcastoctets = value
                    self.ipsystemstatsoutmcastoctets.value_namespace = name_space
                    self.ipsystemstatsoutmcastoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsOutMcastPkts"):
                    self.ipsystemstatsoutmcastpkts = value
                    self.ipsystemstatsoutmcastpkts.value_namespace = name_space
                    self.ipsystemstatsoutmcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsOutNoRoutes"):
                    self.ipsystemstatsoutnoroutes = value
                    self.ipsystemstatsoutnoroutes.value_namespace = name_space
                    self.ipsystemstatsoutnoroutes.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsOutOctets"):
                    self.ipsystemstatsoutoctets = value
                    self.ipsystemstatsoutoctets.value_namespace = name_space
                    self.ipsystemstatsoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsOutRequests"):
                    self.ipsystemstatsoutrequests = value
                    self.ipsystemstatsoutrequests.value_namespace = name_space
                    self.ipsystemstatsoutrequests.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsOutTransmits"):
                    self.ipsystemstatsouttransmits = value
                    self.ipsystemstatsouttransmits.value_namespace = name_space
                    self.ipsystemstatsouttransmits.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsReasmFails"):
                    self.ipsystemstatsreasmfails = value
                    self.ipsystemstatsreasmfails.value_namespace = name_space
                    self.ipsystemstatsreasmfails.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsReasmOKs"):
                    self.ipsystemstatsreasmoks = value
                    self.ipsystemstatsreasmoks.value_namespace = name_space
                    self.ipsystemstatsreasmoks.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsReasmReqds"):
                    self.ipsystemstatsreasmreqds = value
                    self.ipsystemstatsreasmreqds.value_namespace = name_space
                    self.ipsystemstatsreasmreqds.value_namespace_prefix = name_space_prefix
                if(value_path == "ipSystemStatsRefreshRate"):
                    self.ipsystemstatsrefreshrate = value
                    self.ipsystemstatsrefreshrate.value_namespace = name_space
                    self.ipsystemstatsrefreshrate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipsystemstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipsystemstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipSystemStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-MIB:IP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipSystemStatsEntry"):
                for c in self.ipsystemstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpMib.Ipsystemstatstable.Ipsystemstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipsystemstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipSystemStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Ipifstatsentry <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipifstatstable.Ipifstatsentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IpMib.Ipifstatstable, self).__init__()

            self.yang_name = "ipIfStatsTable"
            self.yang_parent_name = "IP-MIB"

            self.ipifstatsentry = YList(self)

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
                        super(IpMib.Ipifstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpMib.Ipifstatstable, self).__setattr__(name, value)


        class Ipifstatsentry(Entity):
            """
            An interface statistics entry containing objects for a
            particular interface and version of IP.
            
            .. attribute:: ipifstatsipversion  <key>
            
            	The IP version of this row
            	**type**\:   :py:class:`IpVersion <ydk.models.ietf.ietf_inet_types.IpVersion>`
            
            .. attribute:: ipifstatsifindex  <key>
            
            	The index value that uniquely identifies the interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipifstatsdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which   any one or more of this entry's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\- initialization of the local management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatshcinbcastpkts
            
            	The number of IP broadcast datagrams received.  This object counts the same datagrams as ipIfStatsInBcastPkts, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatshcindelivers
            
            	The total number of datagrams successfully delivered to IP user\-protocols (including ICMP).  This object counts the same packets as ipIfStatsInDelivers, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatshcinforwdatagrams
            
            	The number of input datagrams for which this entity was not their final IP destination and for which this entity attempted to find a route to forward them to that final destination.  This object counts the same packets as   ipIfStatsInForwDatagrams, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatshcinmcastoctets
            
            	The total number of octets received in IP multicast datagrams.  This object counts the same octets as ipIfStatsInMcastOctets, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatshcinmcastpkts
            
            	The number of IP multicast datagrams received.  This object counts the same datagrams as ipIfStatsInMcastPkts, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatshcinoctets
            
            	The total number of octets received in input IP datagrams, including those received in error.  This object counts the same octets as ipIfStatsInOctets, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatshcinreceives
            
            	The total number of input IP datagrams received, including those received in error.  This object counts the same datagrams as ipIfStatsInReceives, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatshcoutbcastpkts
            
            	The number of IP broadcast datagrams transmitted.  This object counts the same datagrams as ipIfStatsOutBcastPkts, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatshcoutforwdatagrams
            
            	The number of datagrams for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination.  This object counts the same packets as ipIfStatsOutForwDatagrams, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of   ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatshcoutmcastoctets
            
            	The total number of octets transmitted in IP multicast datagrams.  This object counts the same octets as ipIfStatsOutMcastOctets, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatshcoutmcastpkts
            
            	The number of IP multicast datagrams transmitted.  This object counts the same datagrams as ipIfStatsOutMcastPkts, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other   times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatshcoutoctets
            
            	The total number of octets in IP datagrams delivered to the lower layers for transmission.  This objects counts the same octets as ipIfStatsOutOctets, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatshcoutrequests
            
            	The total number of IP datagrams that local IP user\- protocols (including ICMP) supplied to IP in requests for transmission.  This object counts the same packets as   ipIfStatsOutRequests, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatshcouttransmits
            
            	The total number of IP datagrams that this entity supplied to the lower layers for transmission.  This object counts the same datagrams as ipIfStatsOutTransmits, but allows for larger values.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: ipifstatsinaddrerrors
            
            	The number of input IP datagrams discarded because the IP address in their IP header's destination field was not a valid address to be received at this entity.  This count includes invalid addresses (e.g., \:\:0).  For entities that are not IP routers and therefore do not forward datagrams, this counter includes datagrams discarded because the destination address was not a local address.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsinbcastpkts
            
            	The number of IP broadcast datagrams received.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsindelivers
            
            	The total number of datagrams successfully delivered to IP user\-protocols (including ICMP).  When tracking interface statistics, the counter of the interface to which these datagrams were addressed is incremented.  This interface might not be the same as the   input interface for some of the datagrams.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsindiscards
            
            	The number of input IP datagrams for which no problems were encountered to prevent their continued processing, but were discarded (e.g., for lack of buffer space).  Note that this counter does not include any datagrams discarded while awaiting re\-assembly.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsinforwdatagrams
            
            	The number of input datagrams for which this entity was not their final IP destination and for which this entity attempted to find a route to forward them to that final destination.  In entities that do not act as IP routers, this counter will include only those datagrams that were Source\-Routed via this entity, and the Source\-Route processing was successful.  When tracking interface statistics, the counter of the incoming interface is incremented for each datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsinhdrerrors
            
            	The number of input IP datagrams discarded due to errors in their IP headers, including version number mismatch, other format errors, hop count exceeded, errors discovered in processing their IP options, etc.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsinmcastoctets
            
            	The total number of octets received in IP multicast   datagrams.  Octets from datagrams counted in ipIfStatsInMcastPkts MUST be counted here.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsinmcastpkts
            
            	The number of IP multicast datagrams received.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsinnoroutes
            
            	The number of input IP datagrams discarded because no route could be found to transmit them to their destination.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsinoctets
            
            	The total number of octets received in input IP datagrams, including those received in error.  Octets from datagrams counted in ipIfStatsInReceives MUST be counted here.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsinreceives
            
            	The total number of input IP datagrams received, including those received in error.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsintruncatedpkts
            
            	The number of input IP datagrams discarded because the datagram frame didn't carry enough data.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsinunknownprotos
            
            	The number of locally\-addressed IP datagrams received successfully but discarded because of an unknown or unsupported protocol.  When tracking interface statistics, the counter of the interface to which these datagrams were addressed is incremented.  This interface might not be the same as the input interface for some of the datagrams.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of   ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsoutbcastpkts
            
            	The number of IP broadcast datagrams transmitted.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsoutdiscards
            
            	The number of output IP datagrams for which no problem was encountered to prevent their transmission to their destination, but were discarded (e.g., for lack of buffer space).  Note that this counter would include datagrams counted in ipIfStatsOutForwDatagrams if any such datagrams met this (discretionary) discard criterion.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsoutforwdatagrams
            
            	The number of datagrams for which this entity was not their final IP destination and for which it was successful in finding a path to their final destination.  In entities that do not act as IP routers, this counter will include only those datagrams that were Source\-Routed via this entity, and the Source\-Route processing was successful.  When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully forwarded datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsoutfragcreates
            
            	The number of output datagram fragments that have been generated as a result of IP fragmentation.  When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully fragmented datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsoutfragfails
            
            	The number of IP datagrams that have been discarded because they needed to be fragmented but could not be.  This includes IPv4 packets that have the DF bit set and IPv6 packets that are being forwarded and exceed the outgoing link MTU.  When tracking interface statistics, the counter of the outgoing interface is incremented for an unsuccessfully fragmented datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsoutfragoks
            
            	The number of IP datagrams that have been successfully fragmented.  When tracking interface statistics, the counter of the   outgoing interface is incremented for a successfully fragmented datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsoutfragreqds
            
            	The number of IP datagrams that would require fragmentation in order to be transmitted.  When tracking interface statistics, the counter of the outgoing interface is incremented for a successfully fragmented datagram.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsoutmcastoctets
            
            	The total number of octets transmitted in IP multicast datagrams.  Octets from datagrams counted in ipIfStatsOutMcastPkts MUST be counted here.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsoutmcastpkts
            
            	The number of IP multicast datagrams transmitted.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsoutoctets
            
            	The total number of octets in IP datagrams delivered to the lower layers for transmission.  Octets from datagrams counted in ipIfStatsOutTransmits MUST be counted here.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsoutrequests
            
            	The total number of IP datagrams that local IP user\- protocols (including ICMP) supplied to IP in requests for transmission.  Note that this counter does not include any datagrams counted in ipIfStatsOutForwDatagrams.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsouttransmits
            
            	The total number of IP datagrams that this entity supplied to the lower layers for transmission.  This includes datagrams generated locally and those forwarded by this entity.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsreasmfails
            
            	The number of failures detected by the IP re\-assembly algorithm (for whatever reason\: timed out, errors, etc.). Note that this is not necessarily a count of discarded IP fragments since some algorithms (notably the algorithm in RFC 815) can lose track of the number of fragments by combining them as they are received.  When tracking interface statistics, the counter of the interface to which these fragments were addressed is incremented.  This interface might not be the same as the input interface for some of the fragments.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsreasmoks
            
            	The number of IP datagrams successfully reassembled.  When tracking interface statistics, the counter of the interface to which these datagrams were addressed is incremented.  This interface might not be the same as the input interface for some of the datagrams.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsreasmreqds
            
            	The number of IP fragments received that needed to be reassembled at this interface.  When tracking interface statistics, the counter of the interface to which these fragments were addressed is incremented.  This interface might not be the same as the input interface for some of the fragments.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, and at other times as indicated by the value of ipIfStatsDiscontinuityTime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipifstatsrefreshrate
            
            	The minimum reasonable polling interval for this entry. This object provides an indication of the minimum amount of time required to update the counters in this entry
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milli-seconds
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IpMib.Ipifstatstable.Ipifstatsentry, self).__init__()

                self.yang_name = "ipIfStatsEntry"
                self.yang_parent_name = "ipIfStatsTable"

                self.ipifstatsipversion = YLeaf(YType.enumeration, "ipIfStatsIPVersion")

                self.ipifstatsifindex = YLeaf(YType.int32, "ipIfStatsIfIndex")

                self.ipifstatsdiscontinuitytime = YLeaf(YType.uint32, "ipIfStatsDiscontinuityTime")

                self.ipifstatshcinbcastpkts = YLeaf(YType.uint64, "ipIfStatsHCInBcastPkts")

                self.ipifstatshcindelivers = YLeaf(YType.uint64, "ipIfStatsHCInDelivers")

                self.ipifstatshcinforwdatagrams = YLeaf(YType.uint64, "ipIfStatsHCInForwDatagrams")

                self.ipifstatshcinmcastoctets = YLeaf(YType.uint64, "ipIfStatsHCInMcastOctets")

                self.ipifstatshcinmcastpkts = YLeaf(YType.uint64, "ipIfStatsHCInMcastPkts")

                self.ipifstatshcinoctets = YLeaf(YType.uint64, "ipIfStatsHCInOctets")

                self.ipifstatshcinreceives = YLeaf(YType.uint64, "ipIfStatsHCInReceives")

                self.ipifstatshcoutbcastpkts = YLeaf(YType.uint64, "ipIfStatsHCOutBcastPkts")

                self.ipifstatshcoutforwdatagrams = YLeaf(YType.uint64, "ipIfStatsHCOutForwDatagrams")

                self.ipifstatshcoutmcastoctets = YLeaf(YType.uint64, "ipIfStatsHCOutMcastOctets")

                self.ipifstatshcoutmcastpkts = YLeaf(YType.uint64, "ipIfStatsHCOutMcastPkts")

                self.ipifstatshcoutoctets = YLeaf(YType.uint64, "ipIfStatsHCOutOctets")

                self.ipifstatshcoutrequests = YLeaf(YType.uint64, "ipIfStatsHCOutRequests")

                self.ipifstatshcouttransmits = YLeaf(YType.uint64, "ipIfStatsHCOutTransmits")

                self.ipifstatsinaddrerrors = YLeaf(YType.uint32, "ipIfStatsInAddrErrors")

                self.ipifstatsinbcastpkts = YLeaf(YType.uint32, "ipIfStatsInBcastPkts")

                self.ipifstatsindelivers = YLeaf(YType.uint32, "ipIfStatsInDelivers")

                self.ipifstatsindiscards = YLeaf(YType.uint32, "ipIfStatsInDiscards")

                self.ipifstatsinforwdatagrams = YLeaf(YType.uint32, "ipIfStatsInForwDatagrams")

                self.ipifstatsinhdrerrors = YLeaf(YType.uint32, "ipIfStatsInHdrErrors")

                self.ipifstatsinmcastoctets = YLeaf(YType.uint32, "ipIfStatsInMcastOctets")

                self.ipifstatsinmcastpkts = YLeaf(YType.uint32, "ipIfStatsInMcastPkts")

                self.ipifstatsinnoroutes = YLeaf(YType.uint32, "ipIfStatsInNoRoutes")

                self.ipifstatsinoctets = YLeaf(YType.uint32, "ipIfStatsInOctets")

                self.ipifstatsinreceives = YLeaf(YType.uint32, "ipIfStatsInReceives")

                self.ipifstatsintruncatedpkts = YLeaf(YType.uint32, "ipIfStatsInTruncatedPkts")

                self.ipifstatsinunknownprotos = YLeaf(YType.uint32, "ipIfStatsInUnknownProtos")

                self.ipifstatsoutbcastpkts = YLeaf(YType.uint32, "ipIfStatsOutBcastPkts")

                self.ipifstatsoutdiscards = YLeaf(YType.uint32, "ipIfStatsOutDiscards")

                self.ipifstatsoutforwdatagrams = YLeaf(YType.uint32, "ipIfStatsOutForwDatagrams")

                self.ipifstatsoutfragcreates = YLeaf(YType.uint32, "ipIfStatsOutFragCreates")

                self.ipifstatsoutfragfails = YLeaf(YType.uint32, "ipIfStatsOutFragFails")

                self.ipifstatsoutfragoks = YLeaf(YType.uint32, "ipIfStatsOutFragOKs")

                self.ipifstatsoutfragreqds = YLeaf(YType.uint32, "ipIfStatsOutFragReqds")

                self.ipifstatsoutmcastoctets = YLeaf(YType.uint32, "ipIfStatsOutMcastOctets")

                self.ipifstatsoutmcastpkts = YLeaf(YType.uint32, "ipIfStatsOutMcastPkts")

                self.ipifstatsoutoctets = YLeaf(YType.uint32, "ipIfStatsOutOctets")

                self.ipifstatsoutrequests = YLeaf(YType.uint32, "ipIfStatsOutRequests")

                self.ipifstatsouttransmits = YLeaf(YType.uint32, "ipIfStatsOutTransmits")

                self.ipifstatsreasmfails = YLeaf(YType.uint32, "ipIfStatsReasmFails")

                self.ipifstatsreasmoks = YLeaf(YType.uint32, "ipIfStatsReasmOKs")

                self.ipifstatsreasmreqds = YLeaf(YType.uint32, "ipIfStatsReasmReqds")

                self.ipifstatsrefreshrate = YLeaf(YType.uint32, "ipIfStatsRefreshRate")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipifstatsipversion",
                                "ipifstatsifindex",
                                "ipifstatsdiscontinuitytime",
                                "ipifstatshcinbcastpkts",
                                "ipifstatshcindelivers",
                                "ipifstatshcinforwdatagrams",
                                "ipifstatshcinmcastoctets",
                                "ipifstatshcinmcastpkts",
                                "ipifstatshcinoctets",
                                "ipifstatshcinreceives",
                                "ipifstatshcoutbcastpkts",
                                "ipifstatshcoutforwdatagrams",
                                "ipifstatshcoutmcastoctets",
                                "ipifstatshcoutmcastpkts",
                                "ipifstatshcoutoctets",
                                "ipifstatshcoutrequests",
                                "ipifstatshcouttransmits",
                                "ipifstatsinaddrerrors",
                                "ipifstatsinbcastpkts",
                                "ipifstatsindelivers",
                                "ipifstatsindiscards",
                                "ipifstatsinforwdatagrams",
                                "ipifstatsinhdrerrors",
                                "ipifstatsinmcastoctets",
                                "ipifstatsinmcastpkts",
                                "ipifstatsinnoroutes",
                                "ipifstatsinoctets",
                                "ipifstatsinreceives",
                                "ipifstatsintruncatedpkts",
                                "ipifstatsinunknownprotos",
                                "ipifstatsoutbcastpkts",
                                "ipifstatsoutdiscards",
                                "ipifstatsoutforwdatagrams",
                                "ipifstatsoutfragcreates",
                                "ipifstatsoutfragfails",
                                "ipifstatsoutfragoks",
                                "ipifstatsoutfragreqds",
                                "ipifstatsoutmcastoctets",
                                "ipifstatsoutmcastpkts",
                                "ipifstatsoutoctets",
                                "ipifstatsoutrequests",
                                "ipifstatsouttransmits",
                                "ipifstatsreasmfails",
                                "ipifstatsreasmoks",
                                "ipifstatsreasmreqds",
                                "ipifstatsrefreshrate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpMib.Ipifstatstable.Ipifstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpMib.Ipifstatstable.Ipifstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ipifstatsipversion.is_set or
                    self.ipifstatsifindex.is_set or
                    self.ipifstatsdiscontinuitytime.is_set or
                    self.ipifstatshcinbcastpkts.is_set or
                    self.ipifstatshcindelivers.is_set or
                    self.ipifstatshcinforwdatagrams.is_set or
                    self.ipifstatshcinmcastoctets.is_set or
                    self.ipifstatshcinmcastpkts.is_set or
                    self.ipifstatshcinoctets.is_set or
                    self.ipifstatshcinreceives.is_set or
                    self.ipifstatshcoutbcastpkts.is_set or
                    self.ipifstatshcoutforwdatagrams.is_set or
                    self.ipifstatshcoutmcastoctets.is_set or
                    self.ipifstatshcoutmcastpkts.is_set or
                    self.ipifstatshcoutoctets.is_set or
                    self.ipifstatshcoutrequests.is_set or
                    self.ipifstatshcouttransmits.is_set or
                    self.ipifstatsinaddrerrors.is_set or
                    self.ipifstatsinbcastpkts.is_set or
                    self.ipifstatsindelivers.is_set or
                    self.ipifstatsindiscards.is_set or
                    self.ipifstatsinforwdatagrams.is_set or
                    self.ipifstatsinhdrerrors.is_set or
                    self.ipifstatsinmcastoctets.is_set or
                    self.ipifstatsinmcastpkts.is_set or
                    self.ipifstatsinnoroutes.is_set or
                    self.ipifstatsinoctets.is_set or
                    self.ipifstatsinreceives.is_set or
                    self.ipifstatsintruncatedpkts.is_set or
                    self.ipifstatsinunknownprotos.is_set or
                    self.ipifstatsoutbcastpkts.is_set or
                    self.ipifstatsoutdiscards.is_set or
                    self.ipifstatsoutforwdatagrams.is_set or
                    self.ipifstatsoutfragcreates.is_set or
                    self.ipifstatsoutfragfails.is_set or
                    self.ipifstatsoutfragoks.is_set or
                    self.ipifstatsoutfragreqds.is_set or
                    self.ipifstatsoutmcastoctets.is_set or
                    self.ipifstatsoutmcastpkts.is_set or
                    self.ipifstatsoutoctets.is_set or
                    self.ipifstatsoutrequests.is_set or
                    self.ipifstatsouttransmits.is_set or
                    self.ipifstatsreasmfails.is_set or
                    self.ipifstatsreasmoks.is_set or
                    self.ipifstatsreasmreqds.is_set or
                    self.ipifstatsrefreshrate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipifstatsipversion.yfilter != YFilter.not_set or
                    self.ipifstatsifindex.yfilter != YFilter.not_set or
                    self.ipifstatsdiscontinuitytime.yfilter != YFilter.not_set or
                    self.ipifstatshcinbcastpkts.yfilter != YFilter.not_set or
                    self.ipifstatshcindelivers.yfilter != YFilter.not_set or
                    self.ipifstatshcinforwdatagrams.yfilter != YFilter.not_set or
                    self.ipifstatshcinmcastoctets.yfilter != YFilter.not_set or
                    self.ipifstatshcinmcastpkts.yfilter != YFilter.not_set or
                    self.ipifstatshcinoctets.yfilter != YFilter.not_set or
                    self.ipifstatshcinreceives.yfilter != YFilter.not_set or
                    self.ipifstatshcoutbcastpkts.yfilter != YFilter.not_set or
                    self.ipifstatshcoutforwdatagrams.yfilter != YFilter.not_set or
                    self.ipifstatshcoutmcastoctets.yfilter != YFilter.not_set or
                    self.ipifstatshcoutmcastpkts.yfilter != YFilter.not_set or
                    self.ipifstatshcoutoctets.yfilter != YFilter.not_set or
                    self.ipifstatshcoutrequests.yfilter != YFilter.not_set or
                    self.ipifstatshcouttransmits.yfilter != YFilter.not_set or
                    self.ipifstatsinaddrerrors.yfilter != YFilter.not_set or
                    self.ipifstatsinbcastpkts.yfilter != YFilter.not_set or
                    self.ipifstatsindelivers.yfilter != YFilter.not_set or
                    self.ipifstatsindiscards.yfilter != YFilter.not_set or
                    self.ipifstatsinforwdatagrams.yfilter != YFilter.not_set or
                    self.ipifstatsinhdrerrors.yfilter != YFilter.not_set or
                    self.ipifstatsinmcastoctets.yfilter != YFilter.not_set or
                    self.ipifstatsinmcastpkts.yfilter != YFilter.not_set or
                    self.ipifstatsinnoroutes.yfilter != YFilter.not_set or
                    self.ipifstatsinoctets.yfilter != YFilter.not_set or
                    self.ipifstatsinreceives.yfilter != YFilter.not_set or
                    self.ipifstatsintruncatedpkts.yfilter != YFilter.not_set or
                    self.ipifstatsinunknownprotos.yfilter != YFilter.not_set or
                    self.ipifstatsoutbcastpkts.yfilter != YFilter.not_set or
                    self.ipifstatsoutdiscards.yfilter != YFilter.not_set or
                    self.ipifstatsoutforwdatagrams.yfilter != YFilter.not_set or
                    self.ipifstatsoutfragcreates.yfilter != YFilter.not_set or
                    self.ipifstatsoutfragfails.yfilter != YFilter.not_set or
                    self.ipifstatsoutfragoks.yfilter != YFilter.not_set or
                    self.ipifstatsoutfragreqds.yfilter != YFilter.not_set or
                    self.ipifstatsoutmcastoctets.yfilter != YFilter.not_set or
                    self.ipifstatsoutmcastpkts.yfilter != YFilter.not_set or
                    self.ipifstatsoutoctets.yfilter != YFilter.not_set or
                    self.ipifstatsoutrequests.yfilter != YFilter.not_set or
                    self.ipifstatsouttransmits.yfilter != YFilter.not_set or
                    self.ipifstatsreasmfails.yfilter != YFilter.not_set or
                    self.ipifstatsreasmoks.yfilter != YFilter.not_set or
                    self.ipifstatsreasmreqds.yfilter != YFilter.not_set or
                    self.ipifstatsrefreshrate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipIfStatsEntry" + "[ipIfStatsIPVersion='" + self.ipifstatsipversion.get() + "']" + "[ipIfStatsIfIndex='" + self.ipifstatsifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IP-MIB:IP-MIB/ipIfStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipifstatsipversion.is_set or self.ipifstatsipversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsipversion.get_name_leafdata())
                if (self.ipifstatsifindex.is_set or self.ipifstatsifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsifindex.get_name_leafdata())
                if (self.ipifstatsdiscontinuitytime.is_set or self.ipifstatsdiscontinuitytime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsdiscontinuitytime.get_name_leafdata())
                if (self.ipifstatshcinbcastpkts.is_set or self.ipifstatshcinbcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatshcinbcastpkts.get_name_leafdata())
                if (self.ipifstatshcindelivers.is_set or self.ipifstatshcindelivers.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatshcindelivers.get_name_leafdata())
                if (self.ipifstatshcinforwdatagrams.is_set or self.ipifstatshcinforwdatagrams.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatshcinforwdatagrams.get_name_leafdata())
                if (self.ipifstatshcinmcastoctets.is_set or self.ipifstatshcinmcastoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatshcinmcastoctets.get_name_leafdata())
                if (self.ipifstatshcinmcastpkts.is_set or self.ipifstatshcinmcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatshcinmcastpkts.get_name_leafdata())
                if (self.ipifstatshcinoctets.is_set or self.ipifstatshcinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatshcinoctets.get_name_leafdata())
                if (self.ipifstatshcinreceives.is_set or self.ipifstatshcinreceives.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatshcinreceives.get_name_leafdata())
                if (self.ipifstatshcoutbcastpkts.is_set or self.ipifstatshcoutbcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatshcoutbcastpkts.get_name_leafdata())
                if (self.ipifstatshcoutforwdatagrams.is_set or self.ipifstatshcoutforwdatagrams.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatshcoutforwdatagrams.get_name_leafdata())
                if (self.ipifstatshcoutmcastoctets.is_set or self.ipifstatshcoutmcastoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatshcoutmcastoctets.get_name_leafdata())
                if (self.ipifstatshcoutmcastpkts.is_set or self.ipifstatshcoutmcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatshcoutmcastpkts.get_name_leafdata())
                if (self.ipifstatshcoutoctets.is_set or self.ipifstatshcoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatshcoutoctets.get_name_leafdata())
                if (self.ipifstatshcoutrequests.is_set or self.ipifstatshcoutrequests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatshcoutrequests.get_name_leafdata())
                if (self.ipifstatshcouttransmits.is_set or self.ipifstatshcouttransmits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatshcouttransmits.get_name_leafdata())
                if (self.ipifstatsinaddrerrors.is_set or self.ipifstatsinaddrerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsinaddrerrors.get_name_leafdata())
                if (self.ipifstatsinbcastpkts.is_set or self.ipifstatsinbcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsinbcastpkts.get_name_leafdata())
                if (self.ipifstatsindelivers.is_set or self.ipifstatsindelivers.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsindelivers.get_name_leafdata())
                if (self.ipifstatsindiscards.is_set or self.ipifstatsindiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsindiscards.get_name_leafdata())
                if (self.ipifstatsinforwdatagrams.is_set or self.ipifstatsinforwdatagrams.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsinforwdatagrams.get_name_leafdata())
                if (self.ipifstatsinhdrerrors.is_set or self.ipifstatsinhdrerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsinhdrerrors.get_name_leafdata())
                if (self.ipifstatsinmcastoctets.is_set or self.ipifstatsinmcastoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsinmcastoctets.get_name_leafdata())
                if (self.ipifstatsinmcastpkts.is_set or self.ipifstatsinmcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsinmcastpkts.get_name_leafdata())
                if (self.ipifstatsinnoroutes.is_set or self.ipifstatsinnoroutes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsinnoroutes.get_name_leafdata())
                if (self.ipifstatsinoctets.is_set or self.ipifstatsinoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsinoctets.get_name_leafdata())
                if (self.ipifstatsinreceives.is_set or self.ipifstatsinreceives.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsinreceives.get_name_leafdata())
                if (self.ipifstatsintruncatedpkts.is_set or self.ipifstatsintruncatedpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsintruncatedpkts.get_name_leafdata())
                if (self.ipifstatsinunknownprotos.is_set or self.ipifstatsinunknownprotos.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsinunknownprotos.get_name_leafdata())
                if (self.ipifstatsoutbcastpkts.is_set or self.ipifstatsoutbcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsoutbcastpkts.get_name_leafdata())
                if (self.ipifstatsoutdiscards.is_set or self.ipifstatsoutdiscards.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsoutdiscards.get_name_leafdata())
                if (self.ipifstatsoutforwdatagrams.is_set or self.ipifstatsoutforwdatagrams.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsoutforwdatagrams.get_name_leafdata())
                if (self.ipifstatsoutfragcreates.is_set or self.ipifstatsoutfragcreates.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsoutfragcreates.get_name_leafdata())
                if (self.ipifstatsoutfragfails.is_set or self.ipifstatsoutfragfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsoutfragfails.get_name_leafdata())
                if (self.ipifstatsoutfragoks.is_set or self.ipifstatsoutfragoks.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsoutfragoks.get_name_leafdata())
                if (self.ipifstatsoutfragreqds.is_set or self.ipifstatsoutfragreqds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsoutfragreqds.get_name_leafdata())
                if (self.ipifstatsoutmcastoctets.is_set or self.ipifstatsoutmcastoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsoutmcastoctets.get_name_leafdata())
                if (self.ipifstatsoutmcastpkts.is_set or self.ipifstatsoutmcastpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsoutmcastpkts.get_name_leafdata())
                if (self.ipifstatsoutoctets.is_set or self.ipifstatsoutoctets.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsoutoctets.get_name_leafdata())
                if (self.ipifstatsoutrequests.is_set or self.ipifstatsoutrequests.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsoutrequests.get_name_leafdata())
                if (self.ipifstatsouttransmits.is_set or self.ipifstatsouttransmits.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsouttransmits.get_name_leafdata())
                if (self.ipifstatsreasmfails.is_set or self.ipifstatsreasmfails.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsreasmfails.get_name_leafdata())
                if (self.ipifstatsreasmoks.is_set or self.ipifstatsreasmoks.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsreasmoks.get_name_leafdata())
                if (self.ipifstatsreasmreqds.is_set or self.ipifstatsreasmreqds.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsreasmreqds.get_name_leafdata())
                if (self.ipifstatsrefreshrate.is_set or self.ipifstatsrefreshrate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipifstatsrefreshrate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipIfStatsIPVersion" or name == "ipIfStatsIfIndex" or name == "ipIfStatsDiscontinuityTime" or name == "ipIfStatsHCInBcastPkts" or name == "ipIfStatsHCInDelivers" or name == "ipIfStatsHCInForwDatagrams" or name == "ipIfStatsHCInMcastOctets" or name == "ipIfStatsHCInMcastPkts" or name == "ipIfStatsHCInOctets" or name == "ipIfStatsHCInReceives" or name == "ipIfStatsHCOutBcastPkts" or name == "ipIfStatsHCOutForwDatagrams" or name == "ipIfStatsHCOutMcastOctets" or name == "ipIfStatsHCOutMcastPkts" or name == "ipIfStatsHCOutOctets" or name == "ipIfStatsHCOutRequests" or name == "ipIfStatsHCOutTransmits" or name == "ipIfStatsInAddrErrors" or name == "ipIfStatsInBcastPkts" or name == "ipIfStatsInDelivers" or name == "ipIfStatsInDiscards" or name == "ipIfStatsInForwDatagrams" or name == "ipIfStatsInHdrErrors" or name == "ipIfStatsInMcastOctets" or name == "ipIfStatsInMcastPkts" or name == "ipIfStatsInNoRoutes" or name == "ipIfStatsInOctets" or name == "ipIfStatsInReceives" or name == "ipIfStatsInTruncatedPkts" or name == "ipIfStatsInUnknownProtos" or name == "ipIfStatsOutBcastPkts" or name == "ipIfStatsOutDiscards" or name == "ipIfStatsOutForwDatagrams" or name == "ipIfStatsOutFragCreates" or name == "ipIfStatsOutFragFails" or name == "ipIfStatsOutFragOKs" or name == "ipIfStatsOutFragReqds" or name == "ipIfStatsOutMcastOctets" or name == "ipIfStatsOutMcastPkts" or name == "ipIfStatsOutOctets" or name == "ipIfStatsOutRequests" or name == "ipIfStatsOutTransmits" or name == "ipIfStatsReasmFails" or name == "ipIfStatsReasmOKs" or name == "ipIfStatsReasmReqds" or name == "ipIfStatsRefreshRate"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipIfStatsIPVersion"):
                    self.ipifstatsipversion = value
                    self.ipifstatsipversion.value_namespace = name_space
                    self.ipifstatsipversion.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsIfIndex"):
                    self.ipifstatsifindex = value
                    self.ipifstatsifindex.value_namespace = name_space
                    self.ipifstatsifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsDiscontinuityTime"):
                    self.ipifstatsdiscontinuitytime = value
                    self.ipifstatsdiscontinuitytime.value_namespace = name_space
                    self.ipifstatsdiscontinuitytime.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsHCInBcastPkts"):
                    self.ipifstatshcinbcastpkts = value
                    self.ipifstatshcinbcastpkts.value_namespace = name_space
                    self.ipifstatshcinbcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsHCInDelivers"):
                    self.ipifstatshcindelivers = value
                    self.ipifstatshcindelivers.value_namespace = name_space
                    self.ipifstatshcindelivers.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsHCInForwDatagrams"):
                    self.ipifstatshcinforwdatagrams = value
                    self.ipifstatshcinforwdatagrams.value_namespace = name_space
                    self.ipifstatshcinforwdatagrams.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsHCInMcastOctets"):
                    self.ipifstatshcinmcastoctets = value
                    self.ipifstatshcinmcastoctets.value_namespace = name_space
                    self.ipifstatshcinmcastoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsHCInMcastPkts"):
                    self.ipifstatshcinmcastpkts = value
                    self.ipifstatshcinmcastpkts.value_namespace = name_space
                    self.ipifstatshcinmcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsHCInOctets"):
                    self.ipifstatshcinoctets = value
                    self.ipifstatshcinoctets.value_namespace = name_space
                    self.ipifstatshcinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsHCInReceives"):
                    self.ipifstatshcinreceives = value
                    self.ipifstatshcinreceives.value_namespace = name_space
                    self.ipifstatshcinreceives.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsHCOutBcastPkts"):
                    self.ipifstatshcoutbcastpkts = value
                    self.ipifstatshcoutbcastpkts.value_namespace = name_space
                    self.ipifstatshcoutbcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsHCOutForwDatagrams"):
                    self.ipifstatshcoutforwdatagrams = value
                    self.ipifstatshcoutforwdatagrams.value_namespace = name_space
                    self.ipifstatshcoutforwdatagrams.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsHCOutMcastOctets"):
                    self.ipifstatshcoutmcastoctets = value
                    self.ipifstatshcoutmcastoctets.value_namespace = name_space
                    self.ipifstatshcoutmcastoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsHCOutMcastPkts"):
                    self.ipifstatshcoutmcastpkts = value
                    self.ipifstatshcoutmcastpkts.value_namespace = name_space
                    self.ipifstatshcoutmcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsHCOutOctets"):
                    self.ipifstatshcoutoctets = value
                    self.ipifstatshcoutoctets.value_namespace = name_space
                    self.ipifstatshcoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsHCOutRequests"):
                    self.ipifstatshcoutrequests = value
                    self.ipifstatshcoutrequests.value_namespace = name_space
                    self.ipifstatshcoutrequests.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsHCOutTransmits"):
                    self.ipifstatshcouttransmits = value
                    self.ipifstatshcouttransmits.value_namespace = name_space
                    self.ipifstatshcouttransmits.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsInAddrErrors"):
                    self.ipifstatsinaddrerrors = value
                    self.ipifstatsinaddrerrors.value_namespace = name_space
                    self.ipifstatsinaddrerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsInBcastPkts"):
                    self.ipifstatsinbcastpkts = value
                    self.ipifstatsinbcastpkts.value_namespace = name_space
                    self.ipifstatsinbcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsInDelivers"):
                    self.ipifstatsindelivers = value
                    self.ipifstatsindelivers.value_namespace = name_space
                    self.ipifstatsindelivers.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsInDiscards"):
                    self.ipifstatsindiscards = value
                    self.ipifstatsindiscards.value_namespace = name_space
                    self.ipifstatsindiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsInForwDatagrams"):
                    self.ipifstatsinforwdatagrams = value
                    self.ipifstatsinforwdatagrams.value_namespace = name_space
                    self.ipifstatsinforwdatagrams.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsInHdrErrors"):
                    self.ipifstatsinhdrerrors = value
                    self.ipifstatsinhdrerrors.value_namespace = name_space
                    self.ipifstatsinhdrerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsInMcastOctets"):
                    self.ipifstatsinmcastoctets = value
                    self.ipifstatsinmcastoctets.value_namespace = name_space
                    self.ipifstatsinmcastoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsInMcastPkts"):
                    self.ipifstatsinmcastpkts = value
                    self.ipifstatsinmcastpkts.value_namespace = name_space
                    self.ipifstatsinmcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsInNoRoutes"):
                    self.ipifstatsinnoroutes = value
                    self.ipifstatsinnoroutes.value_namespace = name_space
                    self.ipifstatsinnoroutes.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsInOctets"):
                    self.ipifstatsinoctets = value
                    self.ipifstatsinoctets.value_namespace = name_space
                    self.ipifstatsinoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsInReceives"):
                    self.ipifstatsinreceives = value
                    self.ipifstatsinreceives.value_namespace = name_space
                    self.ipifstatsinreceives.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsInTruncatedPkts"):
                    self.ipifstatsintruncatedpkts = value
                    self.ipifstatsintruncatedpkts.value_namespace = name_space
                    self.ipifstatsintruncatedpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsInUnknownProtos"):
                    self.ipifstatsinunknownprotos = value
                    self.ipifstatsinunknownprotos.value_namespace = name_space
                    self.ipifstatsinunknownprotos.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsOutBcastPkts"):
                    self.ipifstatsoutbcastpkts = value
                    self.ipifstatsoutbcastpkts.value_namespace = name_space
                    self.ipifstatsoutbcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsOutDiscards"):
                    self.ipifstatsoutdiscards = value
                    self.ipifstatsoutdiscards.value_namespace = name_space
                    self.ipifstatsoutdiscards.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsOutForwDatagrams"):
                    self.ipifstatsoutforwdatagrams = value
                    self.ipifstatsoutforwdatagrams.value_namespace = name_space
                    self.ipifstatsoutforwdatagrams.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsOutFragCreates"):
                    self.ipifstatsoutfragcreates = value
                    self.ipifstatsoutfragcreates.value_namespace = name_space
                    self.ipifstatsoutfragcreates.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsOutFragFails"):
                    self.ipifstatsoutfragfails = value
                    self.ipifstatsoutfragfails.value_namespace = name_space
                    self.ipifstatsoutfragfails.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsOutFragOKs"):
                    self.ipifstatsoutfragoks = value
                    self.ipifstatsoutfragoks.value_namespace = name_space
                    self.ipifstatsoutfragoks.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsOutFragReqds"):
                    self.ipifstatsoutfragreqds = value
                    self.ipifstatsoutfragreqds.value_namespace = name_space
                    self.ipifstatsoutfragreqds.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsOutMcastOctets"):
                    self.ipifstatsoutmcastoctets = value
                    self.ipifstatsoutmcastoctets.value_namespace = name_space
                    self.ipifstatsoutmcastoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsOutMcastPkts"):
                    self.ipifstatsoutmcastpkts = value
                    self.ipifstatsoutmcastpkts.value_namespace = name_space
                    self.ipifstatsoutmcastpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsOutOctets"):
                    self.ipifstatsoutoctets = value
                    self.ipifstatsoutoctets.value_namespace = name_space
                    self.ipifstatsoutoctets.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsOutRequests"):
                    self.ipifstatsoutrequests = value
                    self.ipifstatsoutrequests.value_namespace = name_space
                    self.ipifstatsoutrequests.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsOutTransmits"):
                    self.ipifstatsouttransmits = value
                    self.ipifstatsouttransmits.value_namespace = name_space
                    self.ipifstatsouttransmits.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsReasmFails"):
                    self.ipifstatsreasmfails = value
                    self.ipifstatsreasmfails.value_namespace = name_space
                    self.ipifstatsreasmfails.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsReasmOKs"):
                    self.ipifstatsreasmoks = value
                    self.ipifstatsreasmoks.value_namespace = name_space
                    self.ipifstatsreasmoks.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsReasmReqds"):
                    self.ipifstatsreasmreqds = value
                    self.ipifstatsreasmreqds.value_namespace = name_space
                    self.ipifstatsreasmreqds.value_namespace_prefix = name_space_prefix
                if(value_path == "ipIfStatsRefreshRate"):
                    self.ipifstatsrefreshrate = value
                    self.ipifstatsrefreshrate.value_namespace = name_space
                    self.ipifstatsrefreshrate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipifstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipifstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipIfStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-MIB:IP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipIfStatsEntry"):
                for c in self.ipifstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpMib.Ipifstatstable.Ipifstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipifstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipIfStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Ipaddressprefixentry <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipaddressprefixtable.Ipaddressprefixentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IpMib.Ipaddressprefixtable, self).__init__()

            self.yang_name = "ipAddressPrefixTable"
            self.yang_parent_name = "IP-MIB"

            self.ipaddressprefixentry = YList(self)

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
                        super(IpMib.Ipaddressprefixtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpMib.Ipaddressprefixtable, self).__setattr__(name, value)


        class Ipaddressprefixentry(Entity):
            """
            An entry in the ipAddressPrefixTable.
            
            .. attribute:: ipaddressprefixifindex  <key>
            
            	The index value that uniquely identifies the interface on which this prefix is configured.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipaddressprefixtype  <key>
            
            	The address type of ipAddressPrefix
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ipaddressprefixprefix  <key>
            
            	The address prefix.  The address type of this object is specified in ipAddressPrefixType.  The length of this object is the standard length for objects of that type (4 or 16 bytes).  Any bits after ipAddressPrefixLength must be zero.  Implementors need to be aware that, if the size of ipAddressPrefixPrefix exceeds 114 octets, then OIDS of instances of columns in this row will have more than 128 sub\-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ipaddressprefixlength  <key>
            
            	The prefix length associated with this prefix.  The value 0 has no special meaning for this object.  It simply refers to address '\:\:/0'
            	**type**\:  int
            
            	**range:** 0..2040
            
            .. attribute:: ipaddressprefixadvpreferredlifetime
            
            	The remaining length of time, in seconds, that this prefix will continue to be preferred, i.e., time until deprecation.  A value of 4,294,967,295 represents infinity.  The address generated from a deprecated prefix should no longer be used as a source address in new communications, but packets received on such an interface are processed as expected.  The default for IPv4 prefixes is 4,294,967,295 (infinity)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: ipaddressprefixadvvalidlifetime
            
            	The remaining length of time, in seconds, that this prefix will continue to be valid, i.e., time until invalidation.  A value of 4,294,967,295 represents infinity.  The address generated from an invalidated prefix should not appear as the destination or source address of a packet.   The default for IPv4 prefixes is 4,294,967,295 (infinity)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: ipaddressprefixautonomousflag
            
            	Autonomous address configuration flag.  When true(1), indicates that this prefix can be used for autonomous address configuration (i.e., can be used to form a local interface address).  If false(2), it is not used to auto\- configure a local interface address.  The default for IPv4 prefixes is 'false(2)'
            	**type**\:  bool
            
            .. attribute:: ipaddressprefixonlinkflag
            
            	This object has the value 'true(1)', if this prefix can be used for on\-link determination; otherwise, the value is 'false(2)'.  The default for IPv4 prefixes is 'true(1)'
            	**type**\:  bool
            
            .. attribute:: ipaddressprefixorigin
            
            	The origin of this prefix
            	**type**\:   :py:class:`Ipaddressprefixorigintc <ydk.models.cisco_ios_xe.IP_MIB.Ipaddressprefixorigintc>`
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IpMib.Ipaddressprefixtable.Ipaddressprefixentry, self).__init__()

                self.yang_name = "ipAddressPrefixEntry"
                self.yang_parent_name = "ipAddressPrefixTable"

                self.ipaddressprefixifindex = YLeaf(YType.int32, "ipAddressPrefixIfIndex")

                self.ipaddressprefixtype = YLeaf(YType.enumeration, "ipAddressPrefixType")

                self.ipaddressprefixprefix = YLeaf(YType.str, "ipAddressPrefixPrefix")

                self.ipaddressprefixlength = YLeaf(YType.uint32, "ipAddressPrefixLength")

                self.ipaddressprefixadvpreferredlifetime = YLeaf(YType.uint32, "ipAddressPrefixAdvPreferredLifetime")

                self.ipaddressprefixadvvalidlifetime = YLeaf(YType.uint32, "ipAddressPrefixAdvValidLifetime")

                self.ipaddressprefixautonomousflag = YLeaf(YType.boolean, "ipAddressPrefixAutonomousFlag")

                self.ipaddressprefixonlinkflag = YLeaf(YType.boolean, "ipAddressPrefixOnLinkFlag")

                self.ipaddressprefixorigin = YLeaf(YType.enumeration, "ipAddressPrefixOrigin")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipaddressprefixifindex",
                                "ipaddressprefixtype",
                                "ipaddressprefixprefix",
                                "ipaddressprefixlength",
                                "ipaddressprefixadvpreferredlifetime",
                                "ipaddressprefixadvvalidlifetime",
                                "ipaddressprefixautonomousflag",
                                "ipaddressprefixonlinkflag",
                                "ipaddressprefixorigin") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpMib.Ipaddressprefixtable.Ipaddressprefixentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpMib.Ipaddressprefixtable.Ipaddressprefixentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ipaddressprefixifindex.is_set or
                    self.ipaddressprefixtype.is_set or
                    self.ipaddressprefixprefix.is_set or
                    self.ipaddressprefixlength.is_set or
                    self.ipaddressprefixadvpreferredlifetime.is_set or
                    self.ipaddressprefixadvvalidlifetime.is_set or
                    self.ipaddressprefixautonomousflag.is_set or
                    self.ipaddressprefixonlinkflag.is_set or
                    self.ipaddressprefixorigin.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipaddressprefixifindex.yfilter != YFilter.not_set or
                    self.ipaddressprefixtype.yfilter != YFilter.not_set or
                    self.ipaddressprefixprefix.yfilter != YFilter.not_set or
                    self.ipaddressprefixlength.yfilter != YFilter.not_set or
                    self.ipaddressprefixadvpreferredlifetime.yfilter != YFilter.not_set or
                    self.ipaddressprefixadvvalidlifetime.yfilter != YFilter.not_set or
                    self.ipaddressprefixautonomousflag.yfilter != YFilter.not_set or
                    self.ipaddressprefixonlinkflag.yfilter != YFilter.not_set or
                    self.ipaddressprefixorigin.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipAddressPrefixEntry" + "[ipAddressPrefixIfIndex='" + self.ipaddressprefixifindex.get() + "']" + "[ipAddressPrefixType='" + self.ipaddressprefixtype.get() + "']" + "[ipAddressPrefixPrefix='" + self.ipaddressprefixprefix.get() + "']" + "[ipAddressPrefixLength='" + self.ipaddressprefixlength.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IP-MIB:IP-MIB/ipAddressPrefixTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipaddressprefixifindex.is_set or self.ipaddressprefixifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddressprefixifindex.get_name_leafdata())
                if (self.ipaddressprefixtype.is_set or self.ipaddressprefixtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddressprefixtype.get_name_leafdata())
                if (self.ipaddressprefixprefix.is_set or self.ipaddressprefixprefix.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddressprefixprefix.get_name_leafdata())
                if (self.ipaddressprefixlength.is_set or self.ipaddressprefixlength.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddressprefixlength.get_name_leafdata())
                if (self.ipaddressprefixadvpreferredlifetime.is_set or self.ipaddressprefixadvpreferredlifetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddressprefixadvpreferredlifetime.get_name_leafdata())
                if (self.ipaddressprefixadvvalidlifetime.is_set or self.ipaddressprefixadvvalidlifetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddressprefixadvvalidlifetime.get_name_leafdata())
                if (self.ipaddressprefixautonomousflag.is_set or self.ipaddressprefixautonomousflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddressprefixautonomousflag.get_name_leafdata())
                if (self.ipaddressprefixonlinkflag.is_set or self.ipaddressprefixonlinkflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddressprefixonlinkflag.get_name_leafdata())
                if (self.ipaddressprefixorigin.is_set or self.ipaddressprefixorigin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddressprefixorigin.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipAddressPrefixIfIndex" or name == "ipAddressPrefixType" or name == "ipAddressPrefixPrefix" or name == "ipAddressPrefixLength" or name == "ipAddressPrefixAdvPreferredLifetime" or name == "ipAddressPrefixAdvValidLifetime" or name == "ipAddressPrefixAutonomousFlag" or name == "ipAddressPrefixOnLinkFlag" or name == "ipAddressPrefixOrigin"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipAddressPrefixIfIndex"):
                    self.ipaddressprefixifindex = value
                    self.ipaddressprefixifindex.value_namespace = name_space
                    self.ipaddressprefixifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAddressPrefixType"):
                    self.ipaddressprefixtype = value
                    self.ipaddressprefixtype.value_namespace = name_space
                    self.ipaddressprefixtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAddressPrefixPrefix"):
                    self.ipaddressprefixprefix = value
                    self.ipaddressprefixprefix.value_namespace = name_space
                    self.ipaddressprefixprefix.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAddressPrefixLength"):
                    self.ipaddressprefixlength = value
                    self.ipaddressprefixlength.value_namespace = name_space
                    self.ipaddressprefixlength.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAddressPrefixAdvPreferredLifetime"):
                    self.ipaddressprefixadvpreferredlifetime = value
                    self.ipaddressprefixadvpreferredlifetime.value_namespace = name_space
                    self.ipaddressprefixadvpreferredlifetime.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAddressPrefixAdvValidLifetime"):
                    self.ipaddressprefixadvvalidlifetime = value
                    self.ipaddressprefixadvvalidlifetime.value_namespace = name_space
                    self.ipaddressprefixadvvalidlifetime.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAddressPrefixAutonomousFlag"):
                    self.ipaddressprefixautonomousflag = value
                    self.ipaddressprefixautonomousflag.value_namespace = name_space
                    self.ipaddressprefixautonomousflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAddressPrefixOnLinkFlag"):
                    self.ipaddressprefixonlinkflag = value
                    self.ipaddressprefixonlinkflag.value_namespace = name_space
                    self.ipaddressprefixonlinkflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAddressPrefixOrigin"):
                    self.ipaddressprefixorigin = value
                    self.ipaddressprefixorigin.value_namespace = name_space
                    self.ipaddressprefixorigin.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipaddressprefixentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipaddressprefixentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipAddressPrefixTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-MIB:IP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipAddressPrefixEntry"):
                for c in self.ipaddressprefixentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpMib.Ipaddressprefixtable.Ipaddressprefixentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipaddressprefixentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipAddressPrefixEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Ipaddressentry <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipaddresstable.Ipaddressentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IpMib.Ipaddresstable, self).__init__()

            self.yang_name = "ipAddressTable"
            self.yang_parent_name = "IP-MIB"

            self.ipaddressentry = YList(self)

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
                        super(IpMib.Ipaddresstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpMib.Ipaddresstable, self).__setattr__(name, value)


        class Ipaddressentry(Entity):
            """
            An address mapping for a particular interface.
            
            .. attribute:: ipaddressaddrtype  <key>
            
            	The address type of ipAddressAddr
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ipaddressaddr  <key>
            
            	The IP address to which this entry's addressing information   pertains.  The address type of this object is specified in ipAddressAddrType.  Implementors need to be aware that if the size of ipAddressAddr exceeds 116 octets, then OIDS of instances of columns in this row will have more than 128 sub\-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ipaddresscreated
            
            	The value of sysUpTime at the time this entry was created. If this entry was created prior to the last re\- initialization of the local network management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipaddressifindex
            
            	The index value that uniquely identifies the interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipaddresslastchanged
            
            	The value of sysUpTime at the time this entry was last updated.  If this entry was updated prior to the last re\- initialization of the local network management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipaddressorigin
            
            	The origin of the address
            	**type**\:   :py:class:`Ipaddressorigintc <ydk.models.cisco_ios_xe.IP_MIB.Ipaddressorigintc>`
            
            .. attribute:: ipaddressprefix
            
            	A pointer to the row in the prefix table to which this address belongs.  May be { 0 0 } if there is no such row
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: ipaddressrowstatus
            
            	The status of this conceptual row.  The RowStatus TC requires that this DESCRIPTION clause states under which circumstances other objects in this row   can be modified.  The value of this object has no effect on whether other objects in this conceptual row can be modified.  A conceptual row can not be made active until the ipAddressIfIndex has been set to a valid index
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ipaddressstatus
            
            	The status of the address, describing if the address can be used for communication.  In the absence of other information, an IPv4 address is always preferred(1)
            	**type**\:   :py:class:`Ipaddressstatustc <ydk.models.cisco_ios_xe.IP_MIB.Ipaddressstatustc>`
            
            .. attribute:: ipaddressstoragetype
            
            	The storage type for this conceptual row.  If this object has a value of 'permanent', then no other objects are required to be able to be modified
            	**type**\:   :py:class:`Storagetype <ydk.models.cisco_ios_xe.SNMPv2_TC.Storagetype>`
            
            .. attribute:: ipaddresstype
            
            	The type of address.  broadcast(3) is not a valid value for IPv6 addresses (RFC 3513)
            	**type**\:   :py:class:`Ipaddresstype <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipaddresstable.Ipaddressentry.Ipaddresstype>`
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IpMib.Ipaddresstable.Ipaddressentry, self).__init__()

                self.yang_name = "ipAddressEntry"
                self.yang_parent_name = "ipAddressTable"

                self.ipaddressaddrtype = YLeaf(YType.enumeration, "ipAddressAddrType")

                self.ipaddressaddr = YLeaf(YType.str, "ipAddressAddr")

                self.ipaddresscreated = YLeaf(YType.uint32, "ipAddressCreated")

                self.ipaddressifindex = YLeaf(YType.int32, "ipAddressIfIndex")

                self.ipaddresslastchanged = YLeaf(YType.uint32, "ipAddressLastChanged")

                self.ipaddressorigin = YLeaf(YType.enumeration, "ipAddressOrigin")

                self.ipaddressprefix = YLeaf(YType.str, "ipAddressPrefix")

                self.ipaddressrowstatus = YLeaf(YType.enumeration, "ipAddressRowStatus")

                self.ipaddressstatus = YLeaf(YType.enumeration, "ipAddressStatus")

                self.ipaddressstoragetype = YLeaf(YType.enumeration, "ipAddressStorageType")

                self.ipaddresstype = YLeaf(YType.enumeration, "ipAddressType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipaddressaddrtype",
                                "ipaddressaddr",
                                "ipaddresscreated",
                                "ipaddressifindex",
                                "ipaddresslastchanged",
                                "ipaddressorigin",
                                "ipaddressprefix",
                                "ipaddressrowstatus",
                                "ipaddressstatus",
                                "ipaddressstoragetype",
                                "ipaddresstype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpMib.Ipaddresstable.Ipaddressentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpMib.Ipaddresstable.Ipaddressentry, self).__setattr__(name, value)

            class Ipaddresstype(Enum):
                """
                Ipaddresstype

                The type of address.  broadcast(3) is not a valid value for

                IPv6 addresses (RFC 3513).

                .. data:: unicast = 1

                .. data:: anycast = 2

                .. data:: broadcast = 3

                """

                unicast = Enum.YLeaf(1, "unicast")

                anycast = Enum.YLeaf(2, "anycast")

                broadcast = Enum.YLeaf(3, "broadcast")


            def has_data(self):
                return (
                    self.ipaddressaddrtype.is_set or
                    self.ipaddressaddr.is_set or
                    self.ipaddresscreated.is_set or
                    self.ipaddressifindex.is_set or
                    self.ipaddresslastchanged.is_set or
                    self.ipaddressorigin.is_set or
                    self.ipaddressprefix.is_set or
                    self.ipaddressrowstatus.is_set or
                    self.ipaddressstatus.is_set or
                    self.ipaddressstoragetype.is_set or
                    self.ipaddresstype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipaddressaddrtype.yfilter != YFilter.not_set or
                    self.ipaddressaddr.yfilter != YFilter.not_set or
                    self.ipaddresscreated.yfilter != YFilter.not_set or
                    self.ipaddressifindex.yfilter != YFilter.not_set or
                    self.ipaddresslastchanged.yfilter != YFilter.not_set or
                    self.ipaddressorigin.yfilter != YFilter.not_set or
                    self.ipaddressprefix.yfilter != YFilter.not_set or
                    self.ipaddressrowstatus.yfilter != YFilter.not_set or
                    self.ipaddressstatus.yfilter != YFilter.not_set or
                    self.ipaddressstoragetype.yfilter != YFilter.not_set or
                    self.ipaddresstype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipAddressEntry" + "[ipAddressAddrType='" + self.ipaddressaddrtype.get() + "']" + "[ipAddressAddr='" + self.ipaddressaddr.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IP-MIB:IP-MIB/ipAddressTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipaddressaddrtype.is_set or self.ipaddressaddrtype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddressaddrtype.get_name_leafdata())
                if (self.ipaddressaddr.is_set or self.ipaddressaddr.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddressaddr.get_name_leafdata())
                if (self.ipaddresscreated.is_set or self.ipaddresscreated.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddresscreated.get_name_leafdata())
                if (self.ipaddressifindex.is_set or self.ipaddressifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddressifindex.get_name_leafdata())
                if (self.ipaddresslastchanged.is_set or self.ipaddresslastchanged.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddresslastchanged.get_name_leafdata())
                if (self.ipaddressorigin.is_set or self.ipaddressorigin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddressorigin.get_name_leafdata())
                if (self.ipaddressprefix.is_set or self.ipaddressprefix.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddressprefix.get_name_leafdata())
                if (self.ipaddressrowstatus.is_set or self.ipaddressrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddressrowstatus.get_name_leafdata())
                if (self.ipaddressstatus.is_set or self.ipaddressstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddressstatus.get_name_leafdata())
                if (self.ipaddressstoragetype.is_set or self.ipaddressstoragetype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddressstoragetype.get_name_leafdata())
                if (self.ipaddresstype.is_set or self.ipaddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipaddresstype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipAddressAddrType" or name == "ipAddressAddr" or name == "ipAddressCreated" or name == "ipAddressIfIndex" or name == "ipAddressLastChanged" or name == "ipAddressOrigin" or name == "ipAddressPrefix" or name == "ipAddressRowStatus" or name == "ipAddressStatus" or name == "ipAddressStorageType" or name == "ipAddressType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipAddressAddrType"):
                    self.ipaddressaddrtype = value
                    self.ipaddressaddrtype.value_namespace = name_space
                    self.ipaddressaddrtype.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAddressAddr"):
                    self.ipaddressaddr = value
                    self.ipaddressaddr.value_namespace = name_space
                    self.ipaddressaddr.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAddressCreated"):
                    self.ipaddresscreated = value
                    self.ipaddresscreated.value_namespace = name_space
                    self.ipaddresscreated.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAddressIfIndex"):
                    self.ipaddressifindex = value
                    self.ipaddressifindex.value_namespace = name_space
                    self.ipaddressifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAddressLastChanged"):
                    self.ipaddresslastchanged = value
                    self.ipaddresslastchanged.value_namespace = name_space
                    self.ipaddresslastchanged.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAddressOrigin"):
                    self.ipaddressorigin = value
                    self.ipaddressorigin.value_namespace = name_space
                    self.ipaddressorigin.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAddressPrefix"):
                    self.ipaddressprefix = value
                    self.ipaddressprefix.value_namespace = name_space
                    self.ipaddressprefix.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAddressRowStatus"):
                    self.ipaddressrowstatus = value
                    self.ipaddressrowstatus.value_namespace = name_space
                    self.ipaddressrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAddressStatus"):
                    self.ipaddressstatus = value
                    self.ipaddressstatus.value_namespace = name_space
                    self.ipaddressstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAddressStorageType"):
                    self.ipaddressstoragetype = value
                    self.ipaddressstoragetype.value_namespace = name_space
                    self.ipaddressstoragetype.value_namespace_prefix = name_space_prefix
                if(value_path == "ipAddressType"):
                    self.ipaddresstype = value
                    self.ipaddresstype.value_namespace = name_space
                    self.ipaddresstype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipaddressentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipaddressentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipAddressTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-MIB:IP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipAddressEntry"):
                for c in self.ipaddressentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpMib.Ipaddresstable.Ipaddressentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipaddressentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipAddressEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        	**type**\: list of    :py:class:`Ipnettophysicalentry <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipnettophysicaltable.Ipnettophysicalentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IpMib.Ipnettophysicaltable, self).__init__()

            self.yang_name = "ipNetToPhysicalTable"
            self.yang_parent_name = "IP-MIB"

            self.ipnettophysicalentry = YList(self)

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
                        super(IpMib.Ipnettophysicaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpMib.Ipnettophysicaltable, self).__setattr__(name, value)


        class Ipnettophysicalentry(Entity):
            """
            Each entry contains one IP address to `physical' address
            equivalence.
            
            .. attribute:: ipnettophysicalifindex  <key>
            
            	The index value that uniquely identifies the interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipnettophysicalnetaddresstype  <key>
            
            	The type of ipNetToPhysicalNetAddress
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ipnettophysicalnetaddress  <key>
            
            	The IP Address corresponding to the media\-dependent `physical' address.  The address type of this object is specified in ipNetToPhysicalAddressType.  Implementors need to be aware that if the size of   ipNetToPhysicalNetAddress exceeds 115 octets, then OIDS of instances of columns in this row will have more than 128 sub\-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ipnettophysicallastupdated
            
            	The value of sysUpTime at the time this entry was last updated.  If this entry was updated prior to the last re\- initialization of the local network management subsystem, then this object contains a zero value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipnettophysicalphysaddress
            
            	The media\-dependent `physical' address.  As the entries in this table are typically not persistent when this object is written the entity SHOULD NOT save the change to non\-volatile storage
            	**type**\:  str
            
            	**length:** 0..65535
            
            .. attribute:: ipnettophysicalrowstatus
            
            	The status of this conceptual row.  The RowStatus TC requires that this DESCRIPTION clause states under which circumstances other objects in this row can be modified.  The value of this object has no effect on whether other objects in this conceptual row can be modified.  A conceptual row can not be made active until the ipNetToPhysicalPhysAddress object has been set.  Note that if the ipNetToPhysicalType is set to 'invalid', the managed node may delete the entry independent of the state of this object
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ipnettophysicalstate
            
            	The Neighbor Unreachability Detection state for the interface when the address mapping in this entry is used. If Neighbor Unreachability Detection is not in use (e.g. for IPv4), this object is always unknown(6)
            	**type**\:   :py:class:`Ipnettophysicalstate <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipnettophysicaltable.Ipnettophysicalentry.Ipnettophysicalstate>`
            
            .. attribute:: ipnettophysicaltype
            
            	The type of mapping.  Setting this object to the value invalid(2) has the effect of invalidating the corresponding entry in the ipNetToPhysicalTable.  That is, it effectively dis\- associates the interface identified with said entry from the mapping identified with said entry.  It is an implementation\-specific matter as to whether the agent   removes an invalidated entry from the table.  Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use.  Proper interpretation of such entries requires examination of the relevant ipNetToPhysicalType object.  The 'dynamic(3)' type indicates that the IP address to physical addresses mapping has been dynamically resolved using e.g., IPv4 ARP or the IPv6 Neighbor Discovery protocol.  The 'static(4)' type indicates that the mapping has been statically configured.  Both of these refer to entries that provide mappings for other entities addresses.  The 'local(5)' type indicates that the mapping is provided for an entity's own interface address.  As the entries in this table are typically not persistent when this object is written the entity SHOULD NOT save the change to non\-volatile storage
            	**type**\:   :py:class:`Ipnettophysicaltype <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipnettophysicaltable.Ipnettophysicalentry.Ipnettophysicaltype>`
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IpMib.Ipnettophysicaltable.Ipnettophysicalentry, self).__init__()

                self.yang_name = "ipNetToPhysicalEntry"
                self.yang_parent_name = "ipNetToPhysicalTable"

                self.ipnettophysicalifindex = YLeaf(YType.int32, "ipNetToPhysicalIfIndex")

                self.ipnettophysicalnetaddresstype = YLeaf(YType.enumeration, "ipNetToPhysicalNetAddressType")

                self.ipnettophysicalnetaddress = YLeaf(YType.str, "ipNetToPhysicalNetAddress")

                self.ipnettophysicallastupdated = YLeaf(YType.uint32, "ipNetToPhysicalLastUpdated")

                self.ipnettophysicalphysaddress = YLeaf(YType.str, "ipNetToPhysicalPhysAddress")

                self.ipnettophysicalrowstatus = YLeaf(YType.enumeration, "ipNetToPhysicalRowStatus")

                self.ipnettophysicalstate = YLeaf(YType.enumeration, "ipNetToPhysicalState")

                self.ipnettophysicaltype = YLeaf(YType.enumeration, "ipNetToPhysicalType")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipnettophysicalifindex",
                                "ipnettophysicalnetaddresstype",
                                "ipnettophysicalnetaddress",
                                "ipnettophysicallastupdated",
                                "ipnettophysicalphysaddress",
                                "ipnettophysicalrowstatus",
                                "ipnettophysicalstate",
                                "ipnettophysicaltype") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpMib.Ipnettophysicaltable.Ipnettophysicalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpMib.Ipnettophysicaltable.Ipnettophysicalentry, self).__setattr__(name, value)

            class Ipnettophysicalstate(Enum):
                """
                Ipnettophysicalstate

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
                Ipnettophysicaltype

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


            def has_data(self):
                return (
                    self.ipnettophysicalifindex.is_set or
                    self.ipnettophysicalnetaddresstype.is_set or
                    self.ipnettophysicalnetaddress.is_set or
                    self.ipnettophysicallastupdated.is_set or
                    self.ipnettophysicalphysaddress.is_set or
                    self.ipnettophysicalrowstatus.is_set or
                    self.ipnettophysicalstate.is_set or
                    self.ipnettophysicaltype.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipnettophysicalifindex.yfilter != YFilter.not_set or
                    self.ipnettophysicalnetaddresstype.yfilter != YFilter.not_set or
                    self.ipnettophysicalnetaddress.yfilter != YFilter.not_set or
                    self.ipnettophysicallastupdated.yfilter != YFilter.not_set or
                    self.ipnettophysicalphysaddress.yfilter != YFilter.not_set or
                    self.ipnettophysicalrowstatus.yfilter != YFilter.not_set or
                    self.ipnettophysicalstate.yfilter != YFilter.not_set or
                    self.ipnettophysicaltype.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipNetToPhysicalEntry" + "[ipNetToPhysicalIfIndex='" + self.ipnettophysicalifindex.get() + "']" + "[ipNetToPhysicalNetAddressType='" + self.ipnettophysicalnetaddresstype.get() + "']" + "[ipNetToPhysicalNetAddress='" + self.ipnettophysicalnetaddress.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IP-MIB:IP-MIB/ipNetToPhysicalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipnettophysicalifindex.is_set or self.ipnettophysicalifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipnettophysicalifindex.get_name_leafdata())
                if (self.ipnettophysicalnetaddresstype.is_set or self.ipnettophysicalnetaddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipnettophysicalnetaddresstype.get_name_leafdata())
                if (self.ipnettophysicalnetaddress.is_set or self.ipnettophysicalnetaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipnettophysicalnetaddress.get_name_leafdata())
                if (self.ipnettophysicallastupdated.is_set or self.ipnettophysicallastupdated.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipnettophysicallastupdated.get_name_leafdata())
                if (self.ipnettophysicalphysaddress.is_set or self.ipnettophysicalphysaddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipnettophysicalphysaddress.get_name_leafdata())
                if (self.ipnettophysicalrowstatus.is_set or self.ipnettophysicalrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipnettophysicalrowstatus.get_name_leafdata())
                if (self.ipnettophysicalstate.is_set or self.ipnettophysicalstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipnettophysicalstate.get_name_leafdata())
                if (self.ipnettophysicaltype.is_set or self.ipnettophysicaltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipnettophysicaltype.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipNetToPhysicalIfIndex" or name == "ipNetToPhysicalNetAddressType" or name == "ipNetToPhysicalNetAddress" or name == "ipNetToPhysicalLastUpdated" or name == "ipNetToPhysicalPhysAddress" or name == "ipNetToPhysicalRowStatus" or name == "ipNetToPhysicalState" or name == "ipNetToPhysicalType"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipNetToPhysicalIfIndex"):
                    self.ipnettophysicalifindex = value
                    self.ipnettophysicalifindex.value_namespace = name_space
                    self.ipnettophysicalifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipNetToPhysicalNetAddressType"):
                    self.ipnettophysicalnetaddresstype = value
                    self.ipnettophysicalnetaddresstype.value_namespace = name_space
                    self.ipnettophysicalnetaddresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "ipNetToPhysicalNetAddress"):
                    self.ipnettophysicalnetaddress = value
                    self.ipnettophysicalnetaddress.value_namespace = name_space
                    self.ipnettophysicalnetaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ipNetToPhysicalLastUpdated"):
                    self.ipnettophysicallastupdated = value
                    self.ipnettophysicallastupdated.value_namespace = name_space
                    self.ipnettophysicallastupdated.value_namespace_prefix = name_space_prefix
                if(value_path == "ipNetToPhysicalPhysAddress"):
                    self.ipnettophysicalphysaddress = value
                    self.ipnettophysicalphysaddress.value_namespace = name_space
                    self.ipnettophysicalphysaddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ipNetToPhysicalRowStatus"):
                    self.ipnettophysicalrowstatus = value
                    self.ipnettophysicalrowstatus.value_namespace = name_space
                    self.ipnettophysicalrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ipNetToPhysicalState"):
                    self.ipnettophysicalstate = value
                    self.ipnettophysicalstate.value_namespace = name_space
                    self.ipnettophysicalstate.value_namespace_prefix = name_space_prefix
                if(value_path == "ipNetToPhysicalType"):
                    self.ipnettophysicaltype = value
                    self.ipnettophysicaltype.value_namespace = name_space
                    self.ipnettophysicaltype.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipnettophysicalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipnettophysicalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipNetToPhysicalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-MIB:IP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipNetToPhysicalEntry"):
                for c in self.ipnettophysicalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpMib.Ipnettophysicaltable.Ipnettophysicalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipnettophysicalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipNetToPhysicalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ipv6Scopezoneindextable(Entity):
        """
        The table used to describe IPv6 unicast and multicast scope
        zones.
        
        For those objects that have names rather than numbers, the
        names were chosen to coincide with the names used in the
        IPv6 address architecture document. 
        
        .. attribute:: ipv6scopezoneindexentry
        
        	Each entry contains the list of scope identifiers on a given interface
        	**type**\: list of    :py:class:`Ipv6Scopezoneindexentry <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipv6Scopezoneindextable.Ipv6Scopezoneindexentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IpMib.Ipv6Scopezoneindextable, self).__init__()

            self.yang_name = "ipv6ScopeZoneIndexTable"
            self.yang_parent_name = "IP-MIB"

            self.ipv6scopezoneindexentry = YList(self)

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
                        super(IpMib.Ipv6Scopezoneindextable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpMib.Ipv6Scopezoneindextable, self).__setattr__(name, value)


        class Ipv6Scopezoneindexentry(Entity):
            """
            Each entry contains the list of scope identifiers on a given
            interface.
            
            .. attribute:: ipv6scopezoneindexifindex  <key>
            
            	The index value that uniquely identifies the interface to which these scopes belong.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipv6scopezoneindex3
            
            	The zone index for scope 3 on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindex6
            
            	The zone index for scope 6 on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindex7
            
            	The zone index for scope 7 on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindex9
            
            	The zone index for scope 9 on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindexa
            
            	The zone index for scope A on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindexadminlocal
            
            	The zone index for the admin\-local scope on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindexb
            
            	The zone index for scope B on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindexc
            
            	The zone index for scope C on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindexd
            
            	The zone index for scope D on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindexlinklocal
            
            	The zone index for the link\-local scope on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindexorganizationlocal
            
            	The zone index for the organization\-local scope on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6scopezoneindexsitelocal
            
            	The zone index for the site\-local scope on this interface
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IpMib.Ipv6Scopezoneindextable.Ipv6Scopezoneindexentry, self).__init__()

                self.yang_name = "ipv6ScopeZoneIndexEntry"
                self.yang_parent_name = "ipv6ScopeZoneIndexTable"

                self.ipv6scopezoneindexifindex = YLeaf(YType.int32, "ipv6ScopeZoneIndexIfIndex")

                self.ipv6scopezoneindex3 = YLeaf(YType.uint32, "ipv6ScopeZoneIndex3")

                self.ipv6scopezoneindex6 = YLeaf(YType.uint32, "ipv6ScopeZoneIndex6")

                self.ipv6scopezoneindex7 = YLeaf(YType.uint32, "ipv6ScopeZoneIndex7")

                self.ipv6scopezoneindex9 = YLeaf(YType.uint32, "ipv6ScopeZoneIndex9")

                self.ipv6scopezoneindexa = YLeaf(YType.uint32, "ipv6ScopeZoneIndexA")

                self.ipv6scopezoneindexadminlocal = YLeaf(YType.uint32, "ipv6ScopeZoneIndexAdminLocal")

                self.ipv6scopezoneindexb = YLeaf(YType.uint32, "ipv6ScopeZoneIndexB")

                self.ipv6scopezoneindexc = YLeaf(YType.uint32, "ipv6ScopeZoneIndexC")

                self.ipv6scopezoneindexd = YLeaf(YType.uint32, "ipv6ScopeZoneIndexD")

                self.ipv6scopezoneindexlinklocal = YLeaf(YType.uint32, "ipv6ScopeZoneIndexLinkLocal")

                self.ipv6scopezoneindexorganizationlocal = YLeaf(YType.uint32, "ipv6ScopeZoneIndexOrganizationLocal")

                self.ipv6scopezoneindexsitelocal = YLeaf(YType.uint32, "ipv6ScopeZoneIndexSiteLocal")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipv6scopezoneindexifindex",
                                "ipv6scopezoneindex3",
                                "ipv6scopezoneindex6",
                                "ipv6scopezoneindex7",
                                "ipv6scopezoneindex9",
                                "ipv6scopezoneindexa",
                                "ipv6scopezoneindexadminlocal",
                                "ipv6scopezoneindexb",
                                "ipv6scopezoneindexc",
                                "ipv6scopezoneindexd",
                                "ipv6scopezoneindexlinklocal",
                                "ipv6scopezoneindexorganizationlocal",
                                "ipv6scopezoneindexsitelocal") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpMib.Ipv6Scopezoneindextable.Ipv6Scopezoneindexentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpMib.Ipv6Scopezoneindextable.Ipv6Scopezoneindexentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ipv6scopezoneindexifindex.is_set or
                    self.ipv6scopezoneindex3.is_set or
                    self.ipv6scopezoneindex6.is_set or
                    self.ipv6scopezoneindex7.is_set or
                    self.ipv6scopezoneindex9.is_set or
                    self.ipv6scopezoneindexa.is_set or
                    self.ipv6scopezoneindexadminlocal.is_set or
                    self.ipv6scopezoneindexb.is_set or
                    self.ipv6scopezoneindexc.is_set or
                    self.ipv6scopezoneindexd.is_set or
                    self.ipv6scopezoneindexlinklocal.is_set or
                    self.ipv6scopezoneindexorganizationlocal.is_set or
                    self.ipv6scopezoneindexsitelocal.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipv6scopezoneindexifindex.yfilter != YFilter.not_set or
                    self.ipv6scopezoneindex3.yfilter != YFilter.not_set or
                    self.ipv6scopezoneindex6.yfilter != YFilter.not_set or
                    self.ipv6scopezoneindex7.yfilter != YFilter.not_set or
                    self.ipv6scopezoneindex9.yfilter != YFilter.not_set or
                    self.ipv6scopezoneindexa.yfilter != YFilter.not_set or
                    self.ipv6scopezoneindexadminlocal.yfilter != YFilter.not_set or
                    self.ipv6scopezoneindexb.yfilter != YFilter.not_set or
                    self.ipv6scopezoneindexc.yfilter != YFilter.not_set or
                    self.ipv6scopezoneindexd.yfilter != YFilter.not_set or
                    self.ipv6scopezoneindexlinklocal.yfilter != YFilter.not_set or
                    self.ipv6scopezoneindexorganizationlocal.yfilter != YFilter.not_set or
                    self.ipv6scopezoneindexsitelocal.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv6ScopeZoneIndexEntry" + "[ipv6ScopeZoneIndexIfIndex='" + self.ipv6scopezoneindexifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IP-MIB:IP-MIB/ipv6ScopeZoneIndexTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipv6scopezoneindexifindex.is_set or self.ipv6scopezoneindexifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6scopezoneindexifindex.get_name_leafdata())
                if (self.ipv6scopezoneindex3.is_set or self.ipv6scopezoneindex3.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6scopezoneindex3.get_name_leafdata())
                if (self.ipv6scopezoneindex6.is_set or self.ipv6scopezoneindex6.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6scopezoneindex6.get_name_leafdata())
                if (self.ipv6scopezoneindex7.is_set or self.ipv6scopezoneindex7.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6scopezoneindex7.get_name_leafdata())
                if (self.ipv6scopezoneindex9.is_set or self.ipv6scopezoneindex9.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6scopezoneindex9.get_name_leafdata())
                if (self.ipv6scopezoneindexa.is_set or self.ipv6scopezoneindexa.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6scopezoneindexa.get_name_leafdata())
                if (self.ipv6scopezoneindexadminlocal.is_set or self.ipv6scopezoneindexadminlocal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6scopezoneindexadminlocal.get_name_leafdata())
                if (self.ipv6scopezoneindexb.is_set or self.ipv6scopezoneindexb.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6scopezoneindexb.get_name_leafdata())
                if (self.ipv6scopezoneindexc.is_set or self.ipv6scopezoneindexc.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6scopezoneindexc.get_name_leafdata())
                if (self.ipv6scopezoneindexd.is_set or self.ipv6scopezoneindexd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6scopezoneindexd.get_name_leafdata())
                if (self.ipv6scopezoneindexlinklocal.is_set or self.ipv6scopezoneindexlinklocal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6scopezoneindexlinklocal.get_name_leafdata())
                if (self.ipv6scopezoneindexorganizationlocal.is_set or self.ipv6scopezoneindexorganizationlocal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6scopezoneindexorganizationlocal.get_name_leafdata())
                if (self.ipv6scopezoneindexsitelocal.is_set or self.ipv6scopezoneindexsitelocal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6scopezoneindexsitelocal.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv6ScopeZoneIndexIfIndex" or name == "ipv6ScopeZoneIndex3" or name == "ipv6ScopeZoneIndex6" or name == "ipv6ScopeZoneIndex7" or name == "ipv6ScopeZoneIndex9" or name == "ipv6ScopeZoneIndexA" or name == "ipv6ScopeZoneIndexAdminLocal" or name == "ipv6ScopeZoneIndexB" or name == "ipv6ScopeZoneIndexC" or name == "ipv6ScopeZoneIndexD" or name == "ipv6ScopeZoneIndexLinkLocal" or name == "ipv6ScopeZoneIndexOrganizationLocal" or name == "ipv6ScopeZoneIndexSiteLocal"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipv6ScopeZoneIndexIfIndex"):
                    self.ipv6scopezoneindexifindex = value
                    self.ipv6scopezoneindexifindex.value_namespace = name_space
                    self.ipv6scopezoneindexifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6ScopeZoneIndex3"):
                    self.ipv6scopezoneindex3 = value
                    self.ipv6scopezoneindex3.value_namespace = name_space
                    self.ipv6scopezoneindex3.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6ScopeZoneIndex6"):
                    self.ipv6scopezoneindex6 = value
                    self.ipv6scopezoneindex6.value_namespace = name_space
                    self.ipv6scopezoneindex6.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6ScopeZoneIndex7"):
                    self.ipv6scopezoneindex7 = value
                    self.ipv6scopezoneindex7.value_namespace = name_space
                    self.ipv6scopezoneindex7.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6ScopeZoneIndex9"):
                    self.ipv6scopezoneindex9 = value
                    self.ipv6scopezoneindex9.value_namespace = name_space
                    self.ipv6scopezoneindex9.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6ScopeZoneIndexA"):
                    self.ipv6scopezoneindexa = value
                    self.ipv6scopezoneindexa.value_namespace = name_space
                    self.ipv6scopezoneindexa.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6ScopeZoneIndexAdminLocal"):
                    self.ipv6scopezoneindexadminlocal = value
                    self.ipv6scopezoneindexadminlocal.value_namespace = name_space
                    self.ipv6scopezoneindexadminlocal.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6ScopeZoneIndexB"):
                    self.ipv6scopezoneindexb = value
                    self.ipv6scopezoneindexb.value_namespace = name_space
                    self.ipv6scopezoneindexb.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6ScopeZoneIndexC"):
                    self.ipv6scopezoneindexc = value
                    self.ipv6scopezoneindexc.value_namespace = name_space
                    self.ipv6scopezoneindexc.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6ScopeZoneIndexD"):
                    self.ipv6scopezoneindexd = value
                    self.ipv6scopezoneindexd.value_namespace = name_space
                    self.ipv6scopezoneindexd.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6ScopeZoneIndexLinkLocal"):
                    self.ipv6scopezoneindexlinklocal = value
                    self.ipv6scopezoneindexlinklocal.value_namespace = name_space
                    self.ipv6scopezoneindexlinklocal.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6ScopeZoneIndexOrganizationLocal"):
                    self.ipv6scopezoneindexorganizationlocal = value
                    self.ipv6scopezoneindexorganizationlocal.value_namespace = name_space
                    self.ipv6scopezoneindexorganizationlocal.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6ScopeZoneIndexSiteLocal"):
                    self.ipv6scopezoneindexsitelocal = value
                    self.ipv6scopezoneindexsitelocal.value_namespace = name_space
                    self.ipv6scopezoneindexsitelocal.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipv6scopezoneindexentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipv6scopezoneindexentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipv6ScopeZoneIndexTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-MIB:IP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipv6ScopeZoneIndexEntry"):
                for c in self.ipv6scopezoneindexentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpMib.Ipv6Scopezoneindextable.Ipv6Scopezoneindexentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipv6scopezoneindexentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipv6ScopeZoneIndexEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ipdefaultroutertable(Entity):
        """
        The table used to describe the default routers known to this
        
        
        entity.
        
        .. attribute:: ipdefaultrouterentry
        
        	Each entry contains information about a default router known to this entity
        	**type**\: list of    :py:class:`Ipdefaultrouterentry <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipdefaultroutertable.Ipdefaultrouterentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IpMib.Ipdefaultroutertable, self).__init__()

            self.yang_name = "ipDefaultRouterTable"
            self.yang_parent_name = "IP-MIB"

            self.ipdefaultrouterentry = YList(self)

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
                        super(IpMib.Ipdefaultroutertable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpMib.Ipdefaultroutertable, self).__setattr__(name, value)


        class Ipdefaultrouterentry(Entity):
            """
            Each entry contains information about a default router known
            to this entity.
            
            .. attribute:: ipdefaultrouteraddresstype  <key>
            
            	The address type for this row
            	**type**\:   :py:class:`Inetaddresstype <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.Inetaddresstype>`
            
            .. attribute:: ipdefaultrouteraddress  <key>
            
            	The IP address of the default router represented by this row.  The address type of this object is specified in ipDefaultRouterAddressType.  Implementers need to be aware that if the size of ipDefaultRouterAddress exceeds 115 octets, then OIDS of instances of columns in this row will have more than 128 sub\-identifiers and cannot be accessed using SNMPv1, SNMPv2c, or SNMPv3
            	**type**\:  str
            
            	**length:** 0..255
            
            .. attribute:: ipdefaultrouterifindex  <key>
            
            	The index value that uniquely identifies the interface by which the router can be reached.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipdefaultrouterlifetime
            
            	The remaining length of time, in seconds, that this router will continue to be useful as a default router.  A value of zero indicates that it is no longer useful as a default router.  It is left to the implementer of the MIB as to whether a router with a lifetime of zero is removed from the list.  For IPv6, this value should be extracted from the router advertisement messages
            	**type**\:  int
            
            	**range:** 0..65535
            
            	**units**\: seconds
            
            .. attribute:: ipdefaultrouterpreference
            
            	An indication of preference given to this router as a default router as described in he Default Router Preferences document.  Treating the value as a 2 bit signed integer allows for simple arithmetic comparisons.  For IPv4 routers or IPv6 routers that are not using the updated router advertisement format, this object is set to medium (0)
            	**type**\:   :py:class:`Ipdefaultrouterpreference <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipdefaultroutertable.Ipdefaultrouterentry.Ipdefaultrouterpreference>`
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IpMib.Ipdefaultroutertable.Ipdefaultrouterentry, self).__init__()

                self.yang_name = "ipDefaultRouterEntry"
                self.yang_parent_name = "ipDefaultRouterTable"

                self.ipdefaultrouteraddresstype = YLeaf(YType.enumeration, "ipDefaultRouterAddressType")

                self.ipdefaultrouteraddress = YLeaf(YType.str, "ipDefaultRouterAddress")

                self.ipdefaultrouterifindex = YLeaf(YType.int32, "ipDefaultRouterIfIndex")

                self.ipdefaultrouterlifetime = YLeaf(YType.uint32, "ipDefaultRouterLifetime")

                self.ipdefaultrouterpreference = YLeaf(YType.enumeration, "ipDefaultRouterPreference")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipdefaultrouteraddresstype",
                                "ipdefaultrouteraddress",
                                "ipdefaultrouterifindex",
                                "ipdefaultrouterlifetime",
                                "ipdefaultrouterpreference") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpMib.Ipdefaultroutertable.Ipdefaultrouterentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpMib.Ipdefaultroutertable.Ipdefaultrouterentry, self).__setattr__(name, value)

            class Ipdefaultrouterpreference(Enum):
                """
                Ipdefaultrouterpreference

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


            def has_data(self):
                return (
                    self.ipdefaultrouteraddresstype.is_set or
                    self.ipdefaultrouteraddress.is_set or
                    self.ipdefaultrouterifindex.is_set or
                    self.ipdefaultrouterlifetime.is_set or
                    self.ipdefaultrouterpreference.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipdefaultrouteraddresstype.yfilter != YFilter.not_set or
                    self.ipdefaultrouteraddress.yfilter != YFilter.not_set or
                    self.ipdefaultrouterifindex.yfilter != YFilter.not_set or
                    self.ipdefaultrouterlifetime.yfilter != YFilter.not_set or
                    self.ipdefaultrouterpreference.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipDefaultRouterEntry" + "[ipDefaultRouterAddressType='" + self.ipdefaultrouteraddresstype.get() + "']" + "[ipDefaultRouterAddress='" + self.ipdefaultrouteraddress.get() + "']" + "[ipDefaultRouterIfIndex='" + self.ipdefaultrouterifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IP-MIB:IP-MIB/ipDefaultRouterTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipdefaultrouteraddresstype.is_set or self.ipdefaultrouteraddresstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipdefaultrouteraddresstype.get_name_leafdata())
                if (self.ipdefaultrouteraddress.is_set or self.ipdefaultrouteraddress.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipdefaultrouteraddress.get_name_leafdata())
                if (self.ipdefaultrouterifindex.is_set or self.ipdefaultrouterifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipdefaultrouterifindex.get_name_leafdata())
                if (self.ipdefaultrouterlifetime.is_set or self.ipdefaultrouterlifetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipdefaultrouterlifetime.get_name_leafdata())
                if (self.ipdefaultrouterpreference.is_set or self.ipdefaultrouterpreference.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipdefaultrouterpreference.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipDefaultRouterAddressType" or name == "ipDefaultRouterAddress" or name == "ipDefaultRouterIfIndex" or name == "ipDefaultRouterLifetime" or name == "ipDefaultRouterPreference"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipDefaultRouterAddressType"):
                    self.ipdefaultrouteraddresstype = value
                    self.ipdefaultrouteraddresstype.value_namespace = name_space
                    self.ipdefaultrouteraddresstype.value_namespace_prefix = name_space_prefix
                if(value_path == "ipDefaultRouterAddress"):
                    self.ipdefaultrouteraddress = value
                    self.ipdefaultrouteraddress.value_namespace = name_space
                    self.ipdefaultrouteraddress.value_namespace_prefix = name_space_prefix
                if(value_path == "ipDefaultRouterIfIndex"):
                    self.ipdefaultrouterifindex = value
                    self.ipdefaultrouterifindex.value_namespace = name_space
                    self.ipdefaultrouterifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipDefaultRouterLifetime"):
                    self.ipdefaultrouterlifetime = value
                    self.ipdefaultrouterlifetime.value_namespace = name_space
                    self.ipdefaultrouterlifetime.value_namespace_prefix = name_space_prefix
                if(value_path == "ipDefaultRouterPreference"):
                    self.ipdefaultrouterpreference = value
                    self.ipdefaultrouterpreference.value_namespace = name_space
                    self.ipdefaultrouterpreference.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipdefaultrouterentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipdefaultrouterentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipDefaultRouterTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-MIB:IP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipDefaultRouterEntry"):
                for c in self.ipdefaultrouterentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpMib.Ipdefaultroutertable.Ipdefaultrouterentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipdefaultrouterentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipDefaultRouterEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Ipv6Routeradverttable(Entity):
        """
        The table containing information used to construct router
        advertisements.
        
        .. attribute:: ipv6routeradvertentry
        
        	An entry containing information used to construct router advertisements.  Information in this table is persistent, and when this object is written, the entity SHOULD save the change to non\-volatile storage
        	**type**\: list of    :py:class:`Ipv6Routeradvertentry <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipv6Routeradverttable.Ipv6Routeradvertentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IpMib.Ipv6Routeradverttable, self).__init__()

            self.yang_name = "ipv6RouterAdvertTable"
            self.yang_parent_name = "IP-MIB"

            self.ipv6routeradvertentry = YList(self)

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
                        super(IpMib.Ipv6Routeradverttable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpMib.Ipv6Routeradverttable, self).__setattr__(name, value)


        class Ipv6Routeradvertentry(Entity):
            """
            An entry containing information used to construct router
            advertisements.
            
            Information in this table is persistent, and when this
            object is written, the entity SHOULD save the change to
            non\-volatile storage.
            
            .. attribute:: ipv6routeradvertifindex  <key>
            
            	The index value that uniquely identifies the interface on which router advertisements constructed with this information will be transmitted.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipv6routeradvertcurhoplimit
            
            	The default value to be placed in the current hop limit field in router advertisements sent from this interface.   The value should be set to the current diameter of the Internet.  A value of zero in the router advertisement indicates that the advertisement isn't specifying a value for curHopLimit.  The default should be set to the value specified in the IANA web pages (www.iana.org) at the time of implementation
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: ipv6routeradvertdefaultlifetime
            
            	The value to be placed in the router lifetime field of router advertisements sent from this interface.  This value MUST be either 0 or between ipv6RouterAdvertMaxInterval and 9000 seconds.  A value of zero indicates that the router is not to be used as a default router.  The default is 3 \* ipv6RouterAdvertMaxInterval
            	**type**\:  int
            
            	**range:** 0..None \| 4..9000
            
            	**units**\: seconds
            
            .. attribute:: ipv6routeradvertlinkmtu
            
            	The value to be placed in MTU options sent by the router on this interface.  A value of zero indicates that no MTU options are sent
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: ipv6routeradvertmanagedflag
            
            	The true/false value to be placed into the 'managed address configuration' flag field in router advertisements sent from this interface
            	**type**\:  bool
            
            .. attribute:: ipv6routeradvertmaxinterval
            
            	The maximum time allowed between sending unsolicited router   advertisements from this interface
            	**type**\:  int
            
            	**range:** 4..1800
            
            	**units**\: seconds
            
            .. attribute:: ipv6routeradvertmininterval
            
            	The minimum time allowed between sending unsolicited router advertisements from this interface.  The default is 0.33 \* ipv6RouterAdvertMaxInterval, however, in the case of a low value for ipv6RouterAdvertMaxInterval, the minimum value for this object is restricted to 3
            	**type**\:  int
            
            	**range:** 3..1350
            
            	**units**\: seconds
            
            .. attribute:: ipv6routeradvertotherconfigflag
            
            	The true/false value to be placed into the 'other stateful configuration' flag field in router advertisements sent from this interface
            	**type**\:  bool
            
            .. attribute:: ipv6routeradvertreachabletime
            
            	The value to be placed in the reachable time field in router advertisement messages sent from this interface.  A value of zero in the router advertisement indicates that the advertisement isn't specifying a value for reachable time
            	**type**\:  int
            
            	**range:** 0..3600000
            
            	**units**\: milliseconds
            
            .. attribute:: ipv6routeradvertretransmittime
            
            	The value to be placed in the retransmit timer field in router advertisements sent from this interface.  A value of zero in the router advertisement indicates that the advertisement isn't specifying a value for retrans time
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: ipv6routeradvertrowstatus
            
            	The status of this conceptual row.  As all objects in this conceptual row have default values, a row can be created and made active by setting this object appropriately.  The RowStatus TC requires that this DESCRIPTION clause states under which circumstances other objects in this row can be modified.  The value of this object has no effect on whether other objects in this conceptual row can be modified
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            .. attribute:: ipv6routeradvertsendadverts
            
            	A flag indicating whether the router sends periodic router advertisements and responds to router solicitations on this interface
            	**type**\:  bool
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IpMib.Ipv6Routeradverttable.Ipv6Routeradvertentry, self).__init__()

                self.yang_name = "ipv6RouterAdvertEntry"
                self.yang_parent_name = "ipv6RouterAdvertTable"

                self.ipv6routeradvertifindex = YLeaf(YType.int32, "ipv6RouterAdvertIfIndex")

                self.ipv6routeradvertcurhoplimit = YLeaf(YType.uint32, "ipv6RouterAdvertCurHopLimit")

                self.ipv6routeradvertdefaultlifetime = YLeaf(YType.uint32, "ipv6RouterAdvertDefaultLifetime")

                self.ipv6routeradvertlinkmtu = YLeaf(YType.uint32, "ipv6RouterAdvertLinkMTU")

                self.ipv6routeradvertmanagedflag = YLeaf(YType.boolean, "ipv6RouterAdvertManagedFlag")

                self.ipv6routeradvertmaxinterval = YLeaf(YType.uint32, "ipv6RouterAdvertMaxInterval")

                self.ipv6routeradvertmininterval = YLeaf(YType.uint32, "ipv6RouterAdvertMinInterval")

                self.ipv6routeradvertotherconfigflag = YLeaf(YType.boolean, "ipv6RouterAdvertOtherConfigFlag")

                self.ipv6routeradvertreachabletime = YLeaf(YType.uint32, "ipv6RouterAdvertReachableTime")

                self.ipv6routeradvertretransmittime = YLeaf(YType.uint32, "ipv6RouterAdvertRetransmitTime")

                self.ipv6routeradvertrowstatus = YLeaf(YType.enumeration, "ipv6RouterAdvertRowStatus")

                self.ipv6routeradvertsendadverts = YLeaf(YType.boolean, "ipv6RouterAdvertSendAdverts")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("ipv6routeradvertifindex",
                                "ipv6routeradvertcurhoplimit",
                                "ipv6routeradvertdefaultlifetime",
                                "ipv6routeradvertlinkmtu",
                                "ipv6routeradvertmanagedflag",
                                "ipv6routeradvertmaxinterval",
                                "ipv6routeradvertmininterval",
                                "ipv6routeradvertotherconfigflag",
                                "ipv6routeradvertreachabletime",
                                "ipv6routeradvertretransmittime",
                                "ipv6routeradvertrowstatus",
                                "ipv6routeradvertsendadverts") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpMib.Ipv6Routeradverttable.Ipv6Routeradvertentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpMib.Ipv6Routeradverttable.Ipv6Routeradvertentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.ipv6routeradvertifindex.is_set or
                    self.ipv6routeradvertcurhoplimit.is_set or
                    self.ipv6routeradvertdefaultlifetime.is_set or
                    self.ipv6routeradvertlinkmtu.is_set or
                    self.ipv6routeradvertmanagedflag.is_set or
                    self.ipv6routeradvertmaxinterval.is_set or
                    self.ipv6routeradvertmininterval.is_set or
                    self.ipv6routeradvertotherconfigflag.is_set or
                    self.ipv6routeradvertreachabletime.is_set or
                    self.ipv6routeradvertretransmittime.is_set or
                    self.ipv6routeradvertrowstatus.is_set or
                    self.ipv6routeradvertsendadverts.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.ipv6routeradvertifindex.yfilter != YFilter.not_set or
                    self.ipv6routeradvertcurhoplimit.yfilter != YFilter.not_set or
                    self.ipv6routeradvertdefaultlifetime.yfilter != YFilter.not_set or
                    self.ipv6routeradvertlinkmtu.yfilter != YFilter.not_set or
                    self.ipv6routeradvertmanagedflag.yfilter != YFilter.not_set or
                    self.ipv6routeradvertmaxinterval.yfilter != YFilter.not_set or
                    self.ipv6routeradvertmininterval.yfilter != YFilter.not_set or
                    self.ipv6routeradvertotherconfigflag.yfilter != YFilter.not_set or
                    self.ipv6routeradvertreachabletime.yfilter != YFilter.not_set or
                    self.ipv6routeradvertretransmittime.yfilter != YFilter.not_set or
                    self.ipv6routeradvertrowstatus.yfilter != YFilter.not_set or
                    self.ipv6routeradvertsendadverts.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "ipv6RouterAdvertEntry" + "[ipv6RouterAdvertIfIndex='" + self.ipv6routeradvertifindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IP-MIB:IP-MIB/ipv6RouterAdvertTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.ipv6routeradvertifindex.is_set or self.ipv6routeradvertifindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6routeradvertifindex.get_name_leafdata())
                if (self.ipv6routeradvertcurhoplimit.is_set or self.ipv6routeradvertcurhoplimit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6routeradvertcurhoplimit.get_name_leafdata())
                if (self.ipv6routeradvertdefaultlifetime.is_set or self.ipv6routeradvertdefaultlifetime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6routeradvertdefaultlifetime.get_name_leafdata())
                if (self.ipv6routeradvertlinkmtu.is_set or self.ipv6routeradvertlinkmtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6routeradvertlinkmtu.get_name_leafdata())
                if (self.ipv6routeradvertmanagedflag.is_set or self.ipv6routeradvertmanagedflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6routeradvertmanagedflag.get_name_leafdata())
                if (self.ipv6routeradvertmaxinterval.is_set or self.ipv6routeradvertmaxinterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6routeradvertmaxinterval.get_name_leafdata())
                if (self.ipv6routeradvertmininterval.is_set or self.ipv6routeradvertmininterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6routeradvertmininterval.get_name_leafdata())
                if (self.ipv6routeradvertotherconfigflag.is_set or self.ipv6routeradvertotherconfigflag.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6routeradvertotherconfigflag.get_name_leafdata())
                if (self.ipv6routeradvertreachabletime.is_set or self.ipv6routeradvertreachabletime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6routeradvertreachabletime.get_name_leafdata())
                if (self.ipv6routeradvertretransmittime.is_set or self.ipv6routeradvertretransmittime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6routeradvertretransmittime.get_name_leafdata())
                if (self.ipv6routeradvertrowstatus.is_set or self.ipv6routeradvertrowstatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6routeradvertrowstatus.get_name_leafdata())
                if (self.ipv6routeradvertsendadverts.is_set or self.ipv6routeradvertsendadverts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.ipv6routeradvertsendadverts.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "ipv6RouterAdvertIfIndex" or name == "ipv6RouterAdvertCurHopLimit" or name == "ipv6RouterAdvertDefaultLifetime" or name == "ipv6RouterAdvertLinkMTU" or name == "ipv6RouterAdvertManagedFlag" or name == "ipv6RouterAdvertMaxInterval" or name == "ipv6RouterAdvertMinInterval" or name == "ipv6RouterAdvertOtherConfigFlag" or name == "ipv6RouterAdvertReachableTime" or name == "ipv6RouterAdvertRetransmitTime" or name == "ipv6RouterAdvertRowStatus" or name == "ipv6RouterAdvertSendAdverts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "ipv6RouterAdvertIfIndex"):
                    self.ipv6routeradvertifindex = value
                    self.ipv6routeradvertifindex.value_namespace = name_space
                    self.ipv6routeradvertifindex.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6RouterAdvertCurHopLimit"):
                    self.ipv6routeradvertcurhoplimit = value
                    self.ipv6routeradvertcurhoplimit.value_namespace = name_space
                    self.ipv6routeradvertcurhoplimit.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6RouterAdvertDefaultLifetime"):
                    self.ipv6routeradvertdefaultlifetime = value
                    self.ipv6routeradvertdefaultlifetime.value_namespace = name_space
                    self.ipv6routeradvertdefaultlifetime.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6RouterAdvertLinkMTU"):
                    self.ipv6routeradvertlinkmtu = value
                    self.ipv6routeradvertlinkmtu.value_namespace = name_space
                    self.ipv6routeradvertlinkmtu.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6RouterAdvertManagedFlag"):
                    self.ipv6routeradvertmanagedflag = value
                    self.ipv6routeradvertmanagedflag.value_namespace = name_space
                    self.ipv6routeradvertmanagedflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6RouterAdvertMaxInterval"):
                    self.ipv6routeradvertmaxinterval = value
                    self.ipv6routeradvertmaxinterval.value_namespace = name_space
                    self.ipv6routeradvertmaxinterval.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6RouterAdvertMinInterval"):
                    self.ipv6routeradvertmininterval = value
                    self.ipv6routeradvertmininterval.value_namespace = name_space
                    self.ipv6routeradvertmininterval.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6RouterAdvertOtherConfigFlag"):
                    self.ipv6routeradvertotherconfigflag = value
                    self.ipv6routeradvertotherconfigflag.value_namespace = name_space
                    self.ipv6routeradvertotherconfigflag.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6RouterAdvertReachableTime"):
                    self.ipv6routeradvertreachabletime = value
                    self.ipv6routeradvertreachabletime.value_namespace = name_space
                    self.ipv6routeradvertreachabletime.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6RouterAdvertRetransmitTime"):
                    self.ipv6routeradvertretransmittime = value
                    self.ipv6routeradvertretransmittime.value_namespace = name_space
                    self.ipv6routeradvertretransmittime.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6RouterAdvertRowStatus"):
                    self.ipv6routeradvertrowstatus = value
                    self.ipv6routeradvertrowstatus.value_namespace = name_space
                    self.ipv6routeradvertrowstatus.value_namespace_prefix = name_space_prefix
                if(value_path == "ipv6RouterAdvertSendAdverts"):
                    self.ipv6routeradvertsendadverts = value
                    self.ipv6routeradvertsendadverts.value_namespace = name_space
                    self.ipv6routeradvertsendadverts.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.ipv6routeradvertentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.ipv6routeradvertentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "ipv6RouterAdvertTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-MIB:IP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "ipv6RouterAdvertEntry"):
                for c in self.ipv6routeradvertentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpMib.Ipv6Routeradverttable.Ipv6Routeradvertentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.ipv6routeradvertentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "ipv6RouterAdvertEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Icmpstatstable(Entity):
        """
        The table of generic system\-wide ICMP counters.
        
        .. attribute:: icmpstatsentry
        
        	A conceptual row in the icmpStatsTable
        	**type**\: list of    :py:class:`Icmpstatsentry <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Icmpstatstable.Icmpstatsentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IpMib.Icmpstatstable, self).__init__()

            self.yang_name = "icmpStatsTable"
            self.yang_parent_name = "IP-MIB"

            self.icmpstatsentry = YList(self)

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
                        super(IpMib.Icmpstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpMib.Icmpstatstable, self).__setattr__(name, value)


        class Icmpstatsentry(Entity):
            """
            A conceptual row in the icmpStatsTable.
            
            .. attribute:: icmpstatsipversion  <key>
            
            	The IP version of the statistics
            	**type**\:   :py:class:`IpVersion <ydk.models.ietf.ietf_inet_types.IpVersion>`
            
            .. attribute:: icmpstatsinerrors
            
            	The number of ICMP messages that the entity received but determined as having ICMP\-specific errors (bad ICMP checksums, bad length, etc.)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: icmpstatsinmsgs
            
            	The total number of ICMP messages that the entity received. Note that this counter includes all those counted by icmpStatsInErrors
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: icmpstatsouterrors
            
            	The number of ICMP messages that this entity did not send due to problems discovered within ICMP, such as a lack of buffers.  This value should not include errors discovered outside the ICMP layer, such as the inability of IP to route the resultant datagram.  In some implementations, there may be no types of error that contribute to this counter's value
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: icmpstatsoutmsgs
            
            	The total number of ICMP messages that the entity attempted to send.  Note that this counter includes all those counted by icmpStatsOutErrors
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IpMib.Icmpstatstable.Icmpstatsentry, self).__init__()

                self.yang_name = "icmpStatsEntry"
                self.yang_parent_name = "icmpStatsTable"

                self.icmpstatsipversion = YLeaf(YType.enumeration, "icmpStatsIPVersion")

                self.icmpstatsinerrors = YLeaf(YType.uint32, "icmpStatsInErrors")

                self.icmpstatsinmsgs = YLeaf(YType.uint32, "icmpStatsInMsgs")

                self.icmpstatsouterrors = YLeaf(YType.uint32, "icmpStatsOutErrors")

                self.icmpstatsoutmsgs = YLeaf(YType.uint32, "icmpStatsOutMsgs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("icmpstatsipversion",
                                "icmpstatsinerrors",
                                "icmpstatsinmsgs",
                                "icmpstatsouterrors",
                                "icmpstatsoutmsgs") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpMib.Icmpstatstable.Icmpstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpMib.Icmpstatstable.Icmpstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.icmpstatsipversion.is_set or
                    self.icmpstatsinerrors.is_set or
                    self.icmpstatsinmsgs.is_set or
                    self.icmpstatsouterrors.is_set or
                    self.icmpstatsoutmsgs.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.icmpstatsipversion.yfilter != YFilter.not_set or
                    self.icmpstatsinerrors.yfilter != YFilter.not_set or
                    self.icmpstatsinmsgs.yfilter != YFilter.not_set or
                    self.icmpstatsouterrors.yfilter != YFilter.not_set or
                    self.icmpstatsoutmsgs.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "icmpStatsEntry" + "[icmpStatsIPVersion='" + self.icmpstatsipversion.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IP-MIB:IP-MIB/icmpStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.icmpstatsipversion.is_set or self.icmpstatsipversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.icmpstatsipversion.get_name_leafdata())
                if (self.icmpstatsinerrors.is_set or self.icmpstatsinerrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.icmpstatsinerrors.get_name_leafdata())
                if (self.icmpstatsinmsgs.is_set or self.icmpstatsinmsgs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.icmpstatsinmsgs.get_name_leafdata())
                if (self.icmpstatsouterrors.is_set or self.icmpstatsouterrors.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.icmpstatsouterrors.get_name_leafdata())
                if (self.icmpstatsoutmsgs.is_set or self.icmpstatsoutmsgs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.icmpstatsoutmsgs.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "icmpStatsIPVersion" or name == "icmpStatsInErrors" or name == "icmpStatsInMsgs" or name == "icmpStatsOutErrors" or name == "icmpStatsOutMsgs"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "icmpStatsIPVersion"):
                    self.icmpstatsipversion = value
                    self.icmpstatsipversion.value_namespace = name_space
                    self.icmpstatsipversion.value_namespace_prefix = name_space_prefix
                if(value_path == "icmpStatsInErrors"):
                    self.icmpstatsinerrors = value
                    self.icmpstatsinerrors.value_namespace = name_space
                    self.icmpstatsinerrors.value_namespace_prefix = name_space_prefix
                if(value_path == "icmpStatsInMsgs"):
                    self.icmpstatsinmsgs = value
                    self.icmpstatsinmsgs.value_namespace = name_space
                    self.icmpstatsinmsgs.value_namespace_prefix = name_space_prefix
                if(value_path == "icmpStatsOutErrors"):
                    self.icmpstatsouterrors = value
                    self.icmpstatsouterrors.value_namespace = name_space
                    self.icmpstatsouterrors.value_namespace_prefix = name_space_prefix
                if(value_path == "icmpStatsOutMsgs"):
                    self.icmpstatsoutmsgs = value
                    self.icmpstatsoutmsgs.value_namespace = name_space
                    self.icmpstatsoutmsgs.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.icmpstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.icmpstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "icmpStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-MIB:IP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "icmpStatsEntry"):
                for c in self.icmpstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpMib.Icmpstatstable.Icmpstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.icmpstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "icmpStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Icmpmsgstatstable(Entity):
        """
        The table of system\-wide per\-version, per\-message type ICMP
        counters.
        
        .. attribute:: icmpmsgstatsentry
        
        	A conceptual row in the icmpMsgStatsTable.  The system should track each ICMP type value, even if that ICMP type is not supported by the system.  However, a given row need not be instantiated unless a message of that type has been processed, i.e., the row for icmpMsgStatsType=X MAY be instantiated before but MUST be instantiated after the first message with Type=X is received or transmitted.  After receiving or transmitting any succeeding messages with Type=X, the relevant counter must be incremented
        	**type**\: list of    :py:class:`Icmpmsgstatsentry <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Icmpmsgstatstable.Icmpmsgstatsentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            super(IpMib.Icmpmsgstatstable, self).__init__()

            self.yang_name = "icmpMsgStatsTable"
            self.yang_parent_name = "IP-MIB"

            self.icmpmsgstatsentry = YList(self)

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
                        super(IpMib.Icmpmsgstatstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(IpMib.Icmpmsgstatstable, self).__setattr__(name, value)


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
            
            .. attribute:: icmpmsgstatsipversion  <key>
            
            	The IP version of the statistics
            	**type**\:   :py:class:`IpVersion <ydk.models.ietf.ietf_inet_types.IpVersion>`
            
            .. attribute:: icmpmsgstatstype  <key>
            
            	The ICMP type field of the message type being counted by this row.  Note that ICMP message types are scoped by the address type in use
            	**type**\:  int
            
            	**range:** 0..255
            
            .. attribute:: icmpmsgstatsinpkts
            
            	The number of input packets for this AF and type
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: icmpmsgstatsoutpkts
            
            	The number of output packets for this AF and type
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                super(IpMib.Icmpmsgstatstable.Icmpmsgstatsentry, self).__init__()

                self.yang_name = "icmpMsgStatsEntry"
                self.yang_parent_name = "icmpMsgStatsTable"

                self.icmpmsgstatsipversion = YLeaf(YType.enumeration, "icmpMsgStatsIPVersion")

                self.icmpmsgstatstype = YLeaf(YType.int32, "icmpMsgStatsType")

                self.icmpmsgstatsinpkts = YLeaf(YType.uint32, "icmpMsgStatsInPkts")

                self.icmpmsgstatsoutpkts = YLeaf(YType.uint32, "icmpMsgStatsOutPkts")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("icmpmsgstatsipversion",
                                "icmpmsgstatstype",
                                "icmpmsgstatsinpkts",
                                "icmpmsgstatsoutpkts") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(IpMib.Icmpmsgstatstable.Icmpmsgstatsentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(IpMib.Icmpmsgstatstable.Icmpmsgstatsentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.icmpmsgstatsipversion.is_set or
                    self.icmpmsgstatstype.is_set or
                    self.icmpmsgstatsinpkts.is_set or
                    self.icmpmsgstatsoutpkts.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.icmpmsgstatsipversion.yfilter != YFilter.not_set or
                    self.icmpmsgstatstype.yfilter != YFilter.not_set or
                    self.icmpmsgstatsinpkts.yfilter != YFilter.not_set or
                    self.icmpmsgstatsoutpkts.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "icmpMsgStatsEntry" + "[icmpMsgStatsIPVersion='" + self.icmpmsgstatsipversion.get() + "']" + "[icmpMsgStatsType='" + self.icmpmsgstatstype.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "IP-MIB:IP-MIB/icmpMsgStatsTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.icmpmsgstatsipversion.is_set or self.icmpmsgstatsipversion.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.icmpmsgstatsipversion.get_name_leafdata())
                if (self.icmpmsgstatstype.is_set or self.icmpmsgstatstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.icmpmsgstatstype.get_name_leafdata())
                if (self.icmpmsgstatsinpkts.is_set or self.icmpmsgstatsinpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.icmpmsgstatsinpkts.get_name_leafdata())
                if (self.icmpmsgstatsoutpkts.is_set or self.icmpmsgstatsoutpkts.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.icmpmsgstatsoutpkts.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "icmpMsgStatsIPVersion" or name == "icmpMsgStatsType" or name == "icmpMsgStatsInPkts" or name == "icmpMsgStatsOutPkts"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "icmpMsgStatsIPVersion"):
                    self.icmpmsgstatsipversion = value
                    self.icmpmsgstatsipversion.value_namespace = name_space
                    self.icmpmsgstatsipversion.value_namespace_prefix = name_space_prefix
                if(value_path == "icmpMsgStatsType"):
                    self.icmpmsgstatstype = value
                    self.icmpmsgstatstype.value_namespace = name_space
                    self.icmpmsgstatstype.value_namespace_prefix = name_space_prefix
                if(value_path == "icmpMsgStatsInPkts"):
                    self.icmpmsgstatsinpkts = value
                    self.icmpmsgstatsinpkts.value_namespace = name_space
                    self.icmpmsgstatsinpkts.value_namespace_prefix = name_space_prefix
                if(value_path == "icmpMsgStatsOutPkts"):
                    self.icmpmsgstatsoutpkts = value
                    self.icmpmsgstatsoutpkts.value_namespace = name_space
                    self.icmpmsgstatsoutpkts.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.icmpmsgstatsentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.icmpmsgstatsentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "icmpMsgStatsTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "IP-MIB:IP-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "icmpMsgStatsEntry"):
                for c in self.icmpmsgstatsentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = IpMib.Icmpmsgstatstable.Icmpmsgstatsentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.icmpmsgstatsentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "icmpMsgStatsEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.icmp is not None and self.icmp.has_data()) or
            (self.icmpmsgstatstable is not None and self.icmpmsgstatstable.has_data()) or
            (self.icmpstatstable is not None and self.icmpstatstable.has_data()) or
            (self.ip is not None and self.ip.has_data()) or
            (self.ipaddressprefixtable is not None and self.ipaddressprefixtable.has_data()) or
            (self.ipaddresstable is not None and self.ipaddresstable.has_data()) or
            (self.ipaddrtable is not None and self.ipaddrtable.has_data()) or
            (self.ipdefaultroutertable is not None and self.ipdefaultroutertable.has_data()) or
            (self.ipifstatstable is not None and self.ipifstatstable.has_data()) or
            (self.ipnettomediatable is not None and self.ipnettomediatable.has_data()) or
            (self.ipnettophysicaltable is not None and self.ipnettophysicaltable.has_data()) or
            (self.ipsystemstatstable is not None and self.ipsystemstatstable.has_data()) or
            (self.iptrafficstats is not None and self.iptrafficstats.has_data()) or
            (self.ipv4interfacetable is not None and self.ipv4interfacetable.has_data()) or
            (self.ipv6interfacetable is not None and self.ipv6interfacetable.has_data()) or
            (self.ipv6routeradverttable is not None and self.ipv6routeradverttable.has_data()) or
            (self.ipv6scopezoneindextable is not None and self.ipv6scopezoneindextable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.icmp is not None and self.icmp.has_operation()) or
            (self.icmpmsgstatstable is not None and self.icmpmsgstatstable.has_operation()) or
            (self.icmpstatstable is not None and self.icmpstatstable.has_operation()) or
            (self.ip is not None and self.ip.has_operation()) or
            (self.ipaddressprefixtable is not None and self.ipaddressprefixtable.has_operation()) or
            (self.ipaddresstable is not None and self.ipaddresstable.has_operation()) or
            (self.ipaddrtable is not None and self.ipaddrtable.has_operation()) or
            (self.ipdefaultroutertable is not None and self.ipdefaultroutertable.has_operation()) or
            (self.ipifstatstable is not None and self.ipifstatstable.has_operation()) or
            (self.ipnettomediatable is not None and self.ipnettomediatable.has_operation()) or
            (self.ipnettophysicaltable is not None and self.ipnettophysicaltable.has_operation()) or
            (self.ipsystemstatstable is not None and self.ipsystemstatstable.has_operation()) or
            (self.iptrafficstats is not None and self.iptrafficstats.has_operation()) or
            (self.ipv4interfacetable is not None and self.ipv4interfacetable.has_operation()) or
            (self.ipv6interfacetable is not None and self.ipv6interfacetable.has_operation()) or
            (self.ipv6routeradverttable is not None and self.ipv6routeradverttable.has_operation()) or
            (self.ipv6scopezoneindextable is not None and self.ipv6scopezoneindextable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "IP-MIB:IP-MIB" + path_buffer

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

        if (child_yang_name == "icmp"):
            if (self.icmp is None):
                self.icmp = IpMib.Icmp()
                self.icmp.parent = self
                self._children_name_map["icmp"] = "icmp"
            return self.icmp

        if (child_yang_name == "icmpMsgStatsTable"):
            if (self.icmpmsgstatstable is None):
                self.icmpmsgstatstable = IpMib.Icmpmsgstatstable()
                self.icmpmsgstatstable.parent = self
                self._children_name_map["icmpmsgstatstable"] = "icmpMsgStatsTable"
            return self.icmpmsgstatstable

        if (child_yang_name == "icmpStatsTable"):
            if (self.icmpstatstable is None):
                self.icmpstatstable = IpMib.Icmpstatstable()
                self.icmpstatstable.parent = self
                self._children_name_map["icmpstatstable"] = "icmpStatsTable"
            return self.icmpstatstable

        if (child_yang_name == "ip"):
            if (self.ip is None):
                self.ip = IpMib.Ip()
                self.ip.parent = self
                self._children_name_map["ip"] = "ip"
            return self.ip

        if (child_yang_name == "ipAddressPrefixTable"):
            if (self.ipaddressprefixtable is None):
                self.ipaddressprefixtable = IpMib.Ipaddressprefixtable()
                self.ipaddressprefixtable.parent = self
                self._children_name_map["ipaddressprefixtable"] = "ipAddressPrefixTable"
            return self.ipaddressprefixtable

        if (child_yang_name == "ipAddressTable"):
            if (self.ipaddresstable is None):
                self.ipaddresstable = IpMib.Ipaddresstable()
                self.ipaddresstable.parent = self
                self._children_name_map["ipaddresstable"] = "ipAddressTable"
            return self.ipaddresstable

        if (child_yang_name == "ipAddrTable"):
            if (self.ipaddrtable is None):
                self.ipaddrtable = IpMib.Ipaddrtable()
                self.ipaddrtable.parent = self
                self._children_name_map["ipaddrtable"] = "ipAddrTable"
            return self.ipaddrtable

        if (child_yang_name == "ipDefaultRouterTable"):
            if (self.ipdefaultroutertable is None):
                self.ipdefaultroutertable = IpMib.Ipdefaultroutertable()
                self.ipdefaultroutertable.parent = self
                self._children_name_map["ipdefaultroutertable"] = "ipDefaultRouterTable"
            return self.ipdefaultroutertable

        if (child_yang_name == "ipIfStatsTable"):
            if (self.ipifstatstable is None):
                self.ipifstatstable = IpMib.Ipifstatstable()
                self.ipifstatstable.parent = self
                self._children_name_map["ipifstatstable"] = "ipIfStatsTable"
            return self.ipifstatstable

        if (child_yang_name == "ipNetToMediaTable"):
            if (self.ipnettomediatable is None):
                self.ipnettomediatable = IpMib.Ipnettomediatable()
                self.ipnettomediatable.parent = self
                self._children_name_map["ipnettomediatable"] = "ipNetToMediaTable"
            return self.ipnettomediatable

        if (child_yang_name == "ipNetToPhysicalTable"):
            if (self.ipnettophysicaltable is None):
                self.ipnettophysicaltable = IpMib.Ipnettophysicaltable()
                self.ipnettophysicaltable.parent = self
                self._children_name_map["ipnettophysicaltable"] = "ipNetToPhysicalTable"
            return self.ipnettophysicaltable

        if (child_yang_name == "ipSystemStatsTable"):
            if (self.ipsystemstatstable is None):
                self.ipsystemstatstable = IpMib.Ipsystemstatstable()
                self.ipsystemstatstable.parent = self
                self._children_name_map["ipsystemstatstable"] = "ipSystemStatsTable"
            return self.ipsystemstatstable

        if (child_yang_name == "ipTrafficStats"):
            if (self.iptrafficstats is None):
                self.iptrafficstats = IpMib.Iptrafficstats()
                self.iptrafficstats.parent = self
                self._children_name_map["iptrafficstats"] = "ipTrafficStats"
            return self.iptrafficstats

        if (child_yang_name == "ipv4InterfaceTable"):
            if (self.ipv4interfacetable is None):
                self.ipv4interfacetable = IpMib.Ipv4Interfacetable()
                self.ipv4interfacetable.parent = self
                self._children_name_map["ipv4interfacetable"] = "ipv4InterfaceTable"
            return self.ipv4interfacetable

        if (child_yang_name == "ipv6InterfaceTable"):
            if (self.ipv6interfacetable is None):
                self.ipv6interfacetable = IpMib.Ipv6Interfacetable()
                self.ipv6interfacetable.parent = self
                self._children_name_map["ipv6interfacetable"] = "ipv6InterfaceTable"
            return self.ipv6interfacetable

        if (child_yang_name == "ipv6RouterAdvertTable"):
            if (self.ipv6routeradverttable is None):
                self.ipv6routeradverttable = IpMib.Ipv6Routeradverttable()
                self.ipv6routeradverttable.parent = self
                self._children_name_map["ipv6routeradverttable"] = "ipv6RouterAdvertTable"
            return self.ipv6routeradverttable

        if (child_yang_name == "ipv6ScopeZoneIndexTable"):
            if (self.ipv6scopezoneindextable is None):
                self.ipv6scopezoneindextable = IpMib.Ipv6Scopezoneindextable()
                self.ipv6scopezoneindextable.parent = self
                self._children_name_map["ipv6scopezoneindextable"] = "ipv6ScopeZoneIndexTable"
            return self.ipv6scopezoneindextable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "icmp" or name == "icmpMsgStatsTable" or name == "icmpStatsTable" or name == "ip" or name == "ipAddressPrefixTable" or name == "ipAddressTable" or name == "ipAddrTable" or name == "ipDefaultRouterTable" or name == "ipIfStatsTable" or name == "ipNetToMediaTable" or name == "ipNetToPhysicalTable" or name == "ipSystemStatsTable" or name == "ipTrafficStats" or name == "ipv4InterfaceTable" or name == "ipv6InterfaceTable" or name == "ipv6RouterAdvertTable" or name == "ipv6ScopeZoneIndexTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = IpMib()
        return self._top_entity

