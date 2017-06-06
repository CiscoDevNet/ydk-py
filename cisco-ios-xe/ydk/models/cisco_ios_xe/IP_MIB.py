""" IP_MIB 

The MIB module for managing IP and ICMP implementations, but
excluding their management of IP routes.

Copyright (C) The Internet Society (2006).  This version of
this MIB module is part of RFC 4293; see the RFC itself for
full legal notices.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class IpaddressorigintcEnum(Enum):
    """
    IpaddressorigintcEnum

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

    other = 1

    manual = 2

    dhcp = 4

    linklayer = 5

    random = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
        return meta._meta_table['IpaddressorigintcEnum']


class IpaddressprefixorigintcEnum(Enum):
    """
    IpaddressprefixorigintcEnum

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

    other = 1

    manual = 2

    wellknown = 3

    dhcp = 4

    routeradv = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
        return meta._meta_table['IpaddressprefixorigintcEnum']


class IpaddressstatustcEnum(Enum):
    """
    IpaddressstatustcEnum

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

    preferred = 1

    deprecated = 2

    invalid = 3

    inaccessible = 4

    unknown = 5

    tentative = 6

    duplicate = 7

    optimistic = 8


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
        return meta._meta_table['IpaddressstatustcEnum']



class IpMib(object):
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
        self.icmp = IpMib.Icmp()
        self.icmp.parent = self
        self.icmpmsgstatstable = IpMib.Icmpmsgstatstable()
        self.icmpmsgstatstable.parent = self
        self.icmpstatstable = IpMib.Icmpstatstable()
        self.icmpstatstable.parent = self
        self.ip = IpMib.Ip()
        self.ip.parent = self
        self.ipaddressprefixtable = IpMib.Ipaddressprefixtable()
        self.ipaddressprefixtable.parent = self
        self.ipaddresstable = IpMib.Ipaddresstable()
        self.ipaddresstable.parent = self
        self.ipaddrtable = IpMib.Ipaddrtable()
        self.ipaddrtable.parent = self
        self.ipdefaultroutertable = IpMib.Ipdefaultroutertable()
        self.ipdefaultroutertable.parent = self
        self.ipifstatstable = IpMib.Ipifstatstable()
        self.ipifstatstable.parent = self
        self.ipnettomediatable = IpMib.Ipnettomediatable()
        self.ipnettomediatable.parent = self
        self.ipnettophysicaltable = IpMib.Ipnettophysicaltable()
        self.ipnettophysicaltable.parent = self
        self.ipsystemstatstable = IpMib.Ipsystemstatstable()
        self.ipsystemstatstable.parent = self
        self.iptrafficstats = IpMib.Iptrafficstats()
        self.iptrafficstats.parent = self
        self.ipv4interfacetable = IpMib.Ipv4Interfacetable()
        self.ipv4interfacetable.parent = self
        self.ipv6interfacetable = IpMib.Ipv6Interfacetable()
        self.ipv6interfacetable.parent = self
        self.ipv6routeradverttable = IpMib.Ipv6Routeradverttable()
        self.ipv6routeradverttable.parent = self
        self.ipv6scopezoneindextable = IpMib.Ipv6Scopezoneindextable()
        self.ipv6scopezoneindextable.parent = self


    class Ip(object):
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
        	**type**\:   :py:class:`IpforwardingEnum <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ip.IpforwardingEnum>`
        
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
        	**type**\:   :py:class:`Ipv6IpforwardingEnum <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ip.Ipv6IpforwardingEnum>`
        
        .. attribute:: ipv6routeradvertspinlock
        
        	An advisory lock used to allow cooperating SNMP managers to coordinate their use of the set operation in creating or modifying rows within this table.  In order to use this lock to coordinate the use of set operations, managers should first retrieve ipv6RouterAdvertSpinLock.  They should then determine the appropriate row to create or modify.  Finally, they should issue the appropriate set command including the retrieved value of ipv6RouterAdvertSpinLock.  If another manager has altered the table in the meantime, then the value of ipv6RouterAdvertSpinLock will have changed and the creation will fail as it will be specifying an incorrect value for ipv6RouterAdvertSpinLock.  It is suggested, but not required, that the ipv6RouterAdvertSpinLock be the first var bind for each set of objects representing a 'row' in a PDU
        	**type**\:  int
        
        	**range:** 0..2147483647
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            self.parent = None
            self.ipaddressspinlock = None
            self.ipdefaultttl = None
            self.ipforwarding = None
            self.ipforwdatagrams = None
            self.ipfragcreates = None
            self.ipfragfails = None
            self.ipfragoks = None
            self.ipinaddrerrors = None
            self.ipindelivers = None
            self.ipindiscards = None
            self.ipinhdrerrors = None
            self.ipinreceives = None
            self.ipinunknownprotos = None
            self.ipoutdiscards = None
            self.ipoutnoroutes = None
            self.ipoutrequests = None
            self.ipreasmfails = None
            self.ipreasmoks = None
            self.ipreasmreqds = None
            self.ipreasmtimeout = None
            self.iproutingdiscards = None
            self.ipv4interfacetablelastchange = None
            self.ipv6interfacetablelastchange = None
            self.ipv6ipdefaulthoplimit = None
            self.ipv6ipforwarding = None
            self.ipv6routeradvertspinlock = None

        class IpforwardingEnum(Enum):
            """
            IpforwardingEnum

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

            forwarding = 1

            notForwarding = 2


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                return meta._meta_table['IpMib.Ip.IpforwardingEnum']


        class Ipv6IpforwardingEnum(Enum):
            """
            Ipv6IpforwardingEnum

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

            forwarding = 1

            notForwarding = 2


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                return meta._meta_table['IpMib.Ip.Ipv6IpforwardingEnum']


        @property
        def _common_path(self):

            return '/IP-MIB:IP-MIB/IP-MIB:ip'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipaddressspinlock is not None:
                return True

            if self.ipdefaultttl is not None:
                return True

            if self.ipforwarding is not None:
                return True

            if self.ipforwdatagrams is not None:
                return True

            if self.ipfragcreates is not None:
                return True

            if self.ipfragfails is not None:
                return True

            if self.ipfragoks is not None:
                return True

            if self.ipinaddrerrors is not None:
                return True

            if self.ipindelivers is not None:
                return True

            if self.ipindiscards is not None:
                return True

            if self.ipinhdrerrors is not None:
                return True

            if self.ipinreceives is not None:
                return True

            if self.ipinunknownprotos is not None:
                return True

            if self.ipoutdiscards is not None:
                return True

            if self.ipoutnoroutes is not None:
                return True

            if self.ipoutrequests is not None:
                return True

            if self.ipreasmfails is not None:
                return True

            if self.ipreasmoks is not None:
                return True

            if self.ipreasmreqds is not None:
                return True

            if self.ipreasmtimeout is not None:
                return True

            if self.iproutingdiscards is not None:
                return True

            if self.ipv4interfacetablelastchange is not None:
                return True

            if self.ipv6interfacetablelastchange is not None:
                return True

            if self.ipv6ipdefaulthoplimit is not None:
                return True

            if self.ipv6ipforwarding is not None:
                return True

            if self.ipv6routeradvertspinlock is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
            return meta._meta_table['IpMib.Ip']['meta_info']


    class Iptrafficstats(object):
        """
        
        
        .. attribute:: ipifstatstablelastchange
        
        	The value of sysUpTime on the most recent occasion at which a row in the ipIfStatsTable was added or deleted.  If new objects are added to the ipIfStatsTable that require the ipIfStatsTableLastChange to be updated when they are modified, they must specify that requirement in their description clause
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            self.parent = None
            self.ipifstatstablelastchange = None

        @property
        def _common_path(self):

            return '/IP-MIB:IP-MIB/IP-MIB:ipTrafficStats'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipifstatstablelastchange is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
            return meta._meta_table['IpMib.Iptrafficstats']['meta_info']


    class Icmp(object):
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
            self.parent = None
            self.icmpinaddrmaskreps = None
            self.icmpinaddrmasks = None
            self.icmpindestunreachs = None
            self.icmpinechoreps = None
            self.icmpinechos = None
            self.icmpinerrors = None
            self.icmpinmsgs = None
            self.icmpinparmprobs = None
            self.icmpinredirects = None
            self.icmpinsrcquenchs = None
            self.icmpintimeexcds = None
            self.icmpintimestampreps = None
            self.icmpintimestamps = None
            self.icmpoutaddrmaskreps = None
            self.icmpoutaddrmasks = None
            self.icmpoutdestunreachs = None
            self.icmpoutechoreps = None
            self.icmpoutechos = None
            self.icmpouterrors = None
            self.icmpoutmsgs = None
            self.icmpoutparmprobs = None
            self.icmpoutredirects = None
            self.icmpoutsrcquenchs = None
            self.icmpouttimeexcds = None
            self.icmpouttimestampreps = None
            self.icmpouttimestamps = None

        @property
        def _common_path(self):

            return '/IP-MIB:IP-MIB/IP-MIB:icmp'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.icmpinaddrmaskreps is not None:
                return True

            if self.icmpinaddrmasks is not None:
                return True

            if self.icmpindestunreachs is not None:
                return True

            if self.icmpinechoreps is not None:
                return True

            if self.icmpinechos is not None:
                return True

            if self.icmpinerrors is not None:
                return True

            if self.icmpinmsgs is not None:
                return True

            if self.icmpinparmprobs is not None:
                return True

            if self.icmpinredirects is not None:
                return True

            if self.icmpinsrcquenchs is not None:
                return True

            if self.icmpintimeexcds is not None:
                return True

            if self.icmpintimestampreps is not None:
                return True

            if self.icmpintimestamps is not None:
                return True

            if self.icmpoutaddrmaskreps is not None:
                return True

            if self.icmpoutaddrmasks is not None:
                return True

            if self.icmpoutdestunreachs is not None:
                return True

            if self.icmpoutechoreps is not None:
                return True

            if self.icmpoutechos is not None:
                return True

            if self.icmpouterrors is not None:
                return True

            if self.icmpoutmsgs is not None:
                return True

            if self.icmpoutparmprobs is not None:
                return True

            if self.icmpoutredirects is not None:
                return True

            if self.icmpoutsrcquenchs is not None:
                return True

            if self.icmpouttimeexcds is not None:
                return True

            if self.icmpouttimestampreps is not None:
                return True

            if self.icmpouttimestamps is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
            return meta._meta_table['IpMib.Icmp']['meta_info']


    class Ipaddrtable(object):
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
            self.parent = None
            self.ipaddrentry = YList()
            self.ipaddrentry.parent = self
            self.ipaddrentry.name = 'ipaddrentry'


        class Ipaddrentry(object):
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
                self.parent = None
                self.ipadentaddr = None
                self.ipadentbcastaddr = None
                self.ipadentifindex = None
                self.ipadentnetmask = None
                self.ipadentreasmmaxsize = None

            @property
            def _common_path(self):
                if self.ipadentaddr is None:
                    raise YPYModelError('Key property ipadentaddr is None')

                return '/IP-MIB:IP-MIB/IP-MIB:ipAddrTable/IP-MIB:ipAddrEntry[IP-MIB:ipAdEntAddr = ' + str(self.ipadentaddr) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipadentaddr is not None:
                    return True

                if self.ipadentbcastaddr is not None:
                    return True

                if self.ipadentifindex is not None:
                    return True

                if self.ipadentnetmask is not None:
                    return True

                if self.ipadentreasmmaxsize is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                return meta._meta_table['IpMib.Ipaddrtable.Ipaddrentry']['meta_info']

        @property
        def _common_path(self):

            return '/IP-MIB:IP-MIB/IP-MIB:ipAddrTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipaddrentry is not None:
                for child_ref in self.ipaddrentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
            return meta._meta_table['IpMib.Ipaddrtable']['meta_info']


    class Ipnettomediatable(object):
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
            self.parent = None
            self.ipnettomediaentry = YList()
            self.ipnettomediaentry.parent = self
            self.ipnettomediaentry.name = 'ipnettomediaentry'


        class Ipnettomediaentry(object):
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
            	**type**\:   :py:class:`IpnettomediatypeEnum <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipnettomediatable.Ipnettomediaentry.IpnettomediatypeEnum>`
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                self.parent = None
                self.ipnettomediaifindex = None
                self.ipnettomedianetaddress = None
                self.ipnettomediaphysaddress = None
                self.ipnettomediatype = None

            class IpnettomediatypeEnum(Enum):
                """
                IpnettomediatypeEnum

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

                other = 1

                invalid = 2

                dynamic = 3

                static = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                    return meta._meta_table['IpMib.Ipnettomediatable.Ipnettomediaentry.IpnettomediatypeEnum']


            @property
            def _common_path(self):
                if self.ipnettomediaifindex is None:
                    raise YPYModelError('Key property ipnettomediaifindex is None')
                if self.ipnettomedianetaddress is None:
                    raise YPYModelError('Key property ipnettomedianetaddress is None')

                return '/IP-MIB:IP-MIB/IP-MIB:ipNetToMediaTable/IP-MIB:ipNetToMediaEntry[IP-MIB:ipNetToMediaIfIndex = ' + str(self.ipnettomediaifindex) + '][IP-MIB:ipNetToMediaNetAddress = ' + str(self.ipnettomedianetaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipnettomediaifindex is not None:
                    return True

                if self.ipnettomedianetaddress is not None:
                    return True

                if self.ipnettomediaphysaddress is not None:
                    return True

                if self.ipnettomediatype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                return meta._meta_table['IpMib.Ipnettomediatable.Ipnettomediaentry']['meta_info']

        @property
        def _common_path(self):

            return '/IP-MIB:IP-MIB/IP-MIB:ipNetToMediaTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipnettomediaentry is not None:
                for child_ref in self.ipnettomediaentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
            return meta._meta_table['IpMib.Ipnettomediatable']['meta_info']


    class Ipv4Interfacetable(object):
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
            self.parent = None
            self.ipv4interfaceentry = YList()
            self.ipv4interfaceentry.parent = self
            self.ipv4interfaceentry.name = 'ipv4interfaceentry'


        class Ipv4Interfaceentry(object):
            """
            An entry containing IPv4\-specific information for a specific
            interface.
            
            .. attribute:: ipv4interfaceifindex  <key>
            
            	The index value that uniquely identifies the interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipv4interfaceenablestatus
            
            	The indication of whether IPv4 is enabled (up) or disabled (down) on this interface.  This object does not affect the state of the interface itself, only its connection to an IPv4 stack.  The IF\-MIB should be used to control the state of the interface
            	**type**\:   :py:class:`Ipv4InterfaceenablestatusEnum <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipv4Interfacetable.Ipv4Interfaceentry.Ipv4InterfaceenablestatusEnum>`
            
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
                self.parent = None
                self.ipv4interfaceifindex = None
                self.ipv4interfaceenablestatus = None
                self.ipv4interfacereasmmaxsize = None
                self.ipv4interfaceretransmittime = None

            class Ipv4InterfaceenablestatusEnum(Enum):
                """
                Ipv4InterfaceenablestatusEnum

                The indication of whether IPv4 is enabled (up) or disabled

                (down) on this interface.  This object does not affect the

                state of the interface itself, only its connection to an

                IPv4 stack.  The IF\-MIB should be used to control the state

                of the interface.

                .. data:: up = 1

                .. data:: down = 2

                """

                up = 1

                down = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                    return meta._meta_table['IpMib.Ipv4Interfacetable.Ipv4Interfaceentry.Ipv4InterfaceenablestatusEnum']


            @property
            def _common_path(self):
                if self.ipv4interfaceifindex is None:
                    raise YPYModelError('Key property ipv4interfaceifindex is None')

                return '/IP-MIB:IP-MIB/IP-MIB:ipv4InterfaceTable/IP-MIB:ipv4InterfaceEntry[IP-MIB:ipv4InterfaceIfIndex = ' + str(self.ipv4interfaceifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipv4interfaceifindex is not None:
                    return True

                if self.ipv4interfaceenablestatus is not None:
                    return True

                if self.ipv4interfacereasmmaxsize is not None:
                    return True

                if self.ipv4interfaceretransmittime is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                return meta._meta_table['IpMib.Ipv4Interfacetable.Ipv4Interfaceentry']['meta_info']

        @property
        def _common_path(self):

            return '/IP-MIB:IP-MIB/IP-MIB:ipv4InterfaceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipv4interfaceentry is not None:
                for child_ref in self.ipv4interfaceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
            return meta._meta_table['IpMib.Ipv4Interfacetable']['meta_info']


    class Ipv6Interfacetable(object):
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
            self.parent = None
            self.ipv6interfaceentry = YList()
            self.ipv6interfaceentry.parent = self
            self.ipv6interfaceentry.name = 'ipv6interfaceentry'


        class Ipv6Interfaceentry(object):
            """
            An entry containing IPv6\-specific information for a given
            interface.
            
            .. attribute:: ipv6interfaceifindex  <key>
            
            	The index value that uniquely identifies the interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipv6interfaceenablestatus
            
            	The indication of whether IPv6 is enabled (up) or disabled (down) on this interface.  This object does not affect the state of the interface itself, only its connection to an IPv6 stack.  The IF\-MIB should be used to control the state of the interface.  When this object is written, the entity SHOULD save the change to non\-volatile storage and restore the object from non\-volatile storage upon re\-initialization of the system
            	**type**\:   :py:class:`Ipv6InterfaceenablestatusEnum <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipv6Interfacetable.Ipv6Interfaceentry.Ipv6InterfaceenablestatusEnum>`
            
            .. attribute:: ipv6interfaceforwarding
            
            	The indication of whether this entity is acting as an IPv6 router on this interface with respect to the forwarding of datagrams received by, but not addressed to, this entity. IPv6 routers forward datagrams.  IPv6 hosts do not (except those source\-routed via the host).  This object is constrained by ipv6IpForwarding and is ignored if ipv6IpForwarding is set to notForwarding.  Those systems that do not provide per\-interface control of the forwarding function should set this object to forwarding for all interfaces and allow the ipv6IpForwarding object to control the forwarding capability.  When this object is written, the entity SHOULD save the change to non\-volatile storage and restore the object from non\-volatile storage upon re\-initialization of the system
            	**type**\:   :py:class:`Ipv6InterfaceforwardingEnum <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipv6Interfacetable.Ipv6Interfaceentry.Ipv6InterfaceforwardingEnum>`
            
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
                self.parent = None
                self.ipv6interfaceifindex = None
                self.ipv6interfaceenablestatus = None
                self.ipv6interfaceforwarding = None
                self.ipv6interfaceidentifier = None
                self.ipv6interfacereachabletime = None
                self.ipv6interfacereasmmaxsize = None
                self.ipv6interfaceretransmittime = None

            class Ipv6InterfaceenablestatusEnum(Enum):
                """
                Ipv6InterfaceenablestatusEnum

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

                up = 1

                down = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                    return meta._meta_table['IpMib.Ipv6Interfacetable.Ipv6Interfaceentry.Ipv6InterfaceenablestatusEnum']


            class Ipv6InterfaceforwardingEnum(Enum):
                """
                Ipv6InterfaceforwardingEnum

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

                forwarding = 1

                notForwarding = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                    return meta._meta_table['IpMib.Ipv6Interfacetable.Ipv6Interfaceentry.Ipv6InterfaceforwardingEnum']


            @property
            def _common_path(self):
                if self.ipv6interfaceifindex is None:
                    raise YPYModelError('Key property ipv6interfaceifindex is None')

                return '/IP-MIB:IP-MIB/IP-MIB:ipv6InterfaceTable/IP-MIB:ipv6InterfaceEntry[IP-MIB:ipv6InterfaceIfIndex = ' + str(self.ipv6interfaceifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipv6interfaceifindex is not None:
                    return True

                if self.ipv6interfaceenablestatus is not None:
                    return True

                if self.ipv6interfaceforwarding is not None:
                    return True

                if self.ipv6interfaceidentifier is not None:
                    return True

                if self.ipv6interfacereachabletime is not None:
                    return True

                if self.ipv6interfacereasmmaxsize is not None:
                    return True

                if self.ipv6interfaceretransmittime is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                return meta._meta_table['IpMib.Ipv6Interfacetable.Ipv6Interfaceentry']['meta_info']

        @property
        def _common_path(self):

            return '/IP-MIB:IP-MIB/IP-MIB:ipv6InterfaceTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipv6interfaceentry is not None:
                for child_ref in self.ipv6interfaceentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
            return meta._meta_table['IpMib.Ipv6Interfacetable']['meta_info']


    class Ipsystemstatstable(object):
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
            self.parent = None
            self.ipsystemstatsentry = YList()
            self.ipsystemstatsentry.parent = self
            self.ipsystemstatsentry.name = 'ipsystemstatsentry'


        class Ipsystemstatsentry(object):
            """
            A statistics entry containing system\-wide objects for a
            particular IP version.
            
            .. attribute:: ipsystemstatsipversion  <key>
            
            	The IP version of this row
            	**type**\:   :py:class:`IpVersionEnum <ydk.models.ietf.ietf_inet_types.IpVersionEnum>`
            
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
                self.parent = None
                self.ipsystemstatsipversion = None
                self.ipsystemstatsdiscontinuitytime = None
                self.ipsystemstatshcinbcastpkts = None
                self.ipsystemstatshcindelivers = None
                self.ipsystemstatshcinforwdatagrams = None
                self.ipsystemstatshcinmcastoctets = None
                self.ipsystemstatshcinmcastpkts = None
                self.ipsystemstatshcinoctets = None
                self.ipsystemstatshcinreceives = None
                self.ipsystemstatshcoutbcastpkts = None
                self.ipsystemstatshcoutforwdatagrams = None
                self.ipsystemstatshcoutmcastoctets = None
                self.ipsystemstatshcoutmcastpkts = None
                self.ipsystemstatshcoutoctets = None
                self.ipsystemstatshcoutrequests = None
                self.ipsystemstatshcouttransmits = None
                self.ipsystemstatsinaddrerrors = None
                self.ipsystemstatsinbcastpkts = None
                self.ipsystemstatsindelivers = None
                self.ipsystemstatsindiscards = None
                self.ipsystemstatsinforwdatagrams = None
                self.ipsystemstatsinhdrerrors = None
                self.ipsystemstatsinmcastoctets = None
                self.ipsystemstatsinmcastpkts = None
                self.ipsystemstatsinnoroutes = None
                self.ipsystemstatsinoctets = None
                self.ipsystemstatsinreceives = None
                self.ipsystemstatsintruncatedpkts = None
                self.ipsystemstatsinunknownprotos = None
                self.ipsystemstatsoutbcastpkts = None
                self.ipsystemstatsoutdiscards = None
                self.ipsystemstatsoutforwdatagrams = None
                self.ipsystemstatsoutfragcreates = None
                self.ipsystemstatsoutfragfails = None
                self.ipsystemstatsoutfragoks = None
                self.ipsystemstatsoutfragreqds = None
                self.ipsystemstatsoutmcastoctets = None
                self.ipsystemstatsoutmcastpkts = None
                self.ipsystemstatsoutnoroutes = None
                self.ipsystemstatsoutoctets = None
                self.ipsystemstatsoutrequests = None
                self.ipsystemstatsouttransmits = None
                self.ipsystemstatsreasmfails = None
                self.ipsystemstatsreasmoks = None
                self.ipsystemstatsreasmreqds = None
                self.ipsystemstatsrefreshrate = None

            @property
            def _common_path(self):
                if self.ipsystemstatsipversion is None:
                    raise YPYModelError('Key property ipsystemstatsipversion is None')

                return '/IP-MIB:IP-MIB/IP-MIB:ipSystemStatsTable/IP-MIB:ipSystemStatsEntry[IP-MIB:ipSystemStatsIPVersion = ' + str(self.ipsystemstatsipversion) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipsystemstatsipversion is not None:
                    return True

                if self.ipsystemstatsdiscontinuitytime is not None:
                    return True

                if self.ipsystemstatshcinbcastpkts is not None:
                    return True

                if self.ipsystemstatshcindelivers is not None:
                    return True

                if self.ipsystemstatshcinforwdatagrams is not None:
                    return True

                if self.ipsystemstatshcinmcastoctets is not None:
                    return True

                if self.ipsystemstatshcinmcastpkts is not None:
                    return True

                if self.ipsystemstatshcinoctets is not None:
                    return True

                if self.ipsystemstatshcinreceives is not None:
                    return True

                if self.ipsystemstatshcoutbcastpkts is not None:
                    return True

                if self.ipsystemstatshcoutforwdatagrams is not None:
                    return True

                if self.ipsystemstatshcoutmcastoctets is not None:
                    return True

                if self.ipsystemstatshcoutmcastpkts is not None:
                    return True

                if self.ipsystemstatshcoutoctets is not None:
                    return True

                if self.ipsystemstatshcoutrequests is not None:
                    return True

                if self.ipsystemstatshcouttransmits is not None:
                    return True

                if self.ipsystemstatsinaddrerrors is not None:
                    return True

                if self.ipsystemstatsinbcastpkts is not None:
                    return True

                if self.ipsystemstatsindelivers is not None:
                    return True

                if self.ipsystemstatsindiscards is not None:
                    return True

                if self.ipsystemstatsinforwdatagrams is not None:
                    return True

                if self.ipsystemstatsinhdrerrors is not None:
                    return True

                if self.ipsystemstatsinmcastoctets is not None:
                    return True

                if self.ipsystemstatsinmcastpkts is not None:
                    return True

                if self.ipsystemstatsinnoroutes is not None:
                    return True

                if self.ipsystemstatsinoctets is not None:
                    return True

                if self.ipsystemstatsinreceives is not None:
                    return True

                if self.ipsystemstatsintruncatedpkts is not None:
                    return True

                if self.ipsystemstatsinunknownprotos is not None:
                    return True

                if self.ipsystemstatsoutbcastpkts is not None:
                    return True

                if self.ipsystemstatsoutdiscards is not None:
                    return True

                if self.ipsystemstatsoutforwdatagrams is not None:
                    return True

                if self.ipsystemstatsoutfragcreates is not None:
                    return True

                if self.ipsystemstatsoutfragfails is not None:
                    return True

                if self.ipsystemstatsoutfragoks is not None:
                    return True

                if self.ipsystemstatsoutfragreqds is not None:
                    return True

                if self.ipsystemstatsoutmcastoctets is not None:
                    return True

                if self.ipsystemstatsoutmcastpkts is not None:
                    return True

                if self.ipsystemstatsoutnoroutes is not None:
                    return True

                if self.ipsystemstatsoutoctets is not None:
                    return True

                if self.ipsystemstatsoutrequests is not None:
                    return True

                if self.ipsystemstatsouttransmits is not None:
                    return True

                if self.ipsystemstatsreasmfails is not None:
                    return True

                if self.ipsystemstatsreasmoks is not None:
                    return True

                if self.ipsystemstatsreasmreqds is not None:
                    return True

                if self.ipsystemstatsrefreshrate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                return meta._meta_table['IpMib.Ipsystemstatstable.Ipsystemstatsentry']['meta_info']

        @property
        def _common_path(self):

            return '/IP-MIB:IP-MIB/IP-MIB:ipSystemStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipsystemstatsentry is not None:
                for child_ref in self.ipsystemstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
            return meta._meta_table['IpMib.Ipsystemstatstable']['meta_info']


    class Ipifstatstable(object):
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
            self.parent = None
            self.ipifstatsentry = YList()
            self.ipifstatsentry.parent = self
            self.ipifstatsentry.name = 'ipifstatsentry'


        class Ipifstatsentry(object):
            """
            An interface statistics entry containing objects for a
            particular interface and version of IP.
            
            .. attribute:: ipifstatsipversion  <key>
            
            	The IP version of this row
            	**type**\:   :py:class:`IpVersionEnum <ydk.models.ietf.ietf_inet_types.IpVersionEnum>`
            
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
                self.parent = None
                self.ipifstatsipversion = None
                self.ipifstatsifindex = None
                self.ipifstatsdiscontinuitytime = None
                self.ipifstatshcinbcastpkts = None
                self.ipifstatshcindelivers = None
                self.ipifstatshcinforwdatagrams = None
                self.ipifstatshcinmcastoctets = None
                self.ipifstatshcinmcastpkts = None
                self.ipifstatshcinoctets = None
                self.ipifstatshcinreceives = None
                self.ipifstatshcoutbcastpkts = None
                self.ipifstatshcoutforwdatagrams = None
                self.ipifstatshcoutmcastoctets = None
                self.ipifstatshcoutmcastpkts = None
                self.ipifstatshcoutoctets = None
                self.ipifstatshcoutrequests = None
                self.ipifstatshcouttransmits = None
                self.ipifstatsinaddrerrors = None
                self.ipifstatsinbcastpkts = None
                self.ipifstatsindelivers = None
                self.ipifstatsindiscards = None
                self.ipifstatsinforwdatagrams = None
                self.ipifstatsinhdrerrors = None
                self.ipifstatsinmcastoctets = None
                self.ipifstatsinmcastpkts = None
                self.ipifstatsinnoroutes = None
                self.ipifstatsinoctets = None
                self.ipifstatsinreceives = None
                self.ipifstatsintruncatedpkts = None
                self.ipifstatsinunknownprotos = None
                self.ipifstatsoutbcastpkts = None
                self.ipifstatsoutdiscards = None
                self.ipifstatsoutforwdatagrams = None
                self.ipifstatsoutfragcreates = None
                self.ipifstatsoutfragfails = None
                self.ipifstatsoutfragoks = None
                self.ipifstatsoutfragreqds = None
                self.ipifstatsoutmcastoctets = None
                self.ipifstatsoutmcastpkts = None
                self.ipifstatsoutoctets = None
                self.ipifstatsoutrequests = None
                self.ipifstatsouttransmits = None
                self.ipifstatsreasmfails = None
                self.ipifstatsreasmoks = None
                self.ipifstatsreasmreqds = None
                self.ipifstatsrefreshrate = None

            @property
            def _common_path(self):
                if self.ipifstatsipversion is None:
                    raise YPYModelError('Key property ipifstatsipversion is None')
                if self.ipifstatsifindex is None:
                    raise YPYModelError('Key property ipifstatsifindex is None')

                return '/IP-MIB:IP-MIB/IP-MIB:ipIfStatsTable/IP-MIB:ipIfStatsEntry[IP-MIB:ipIfStatsIPVersion = ' + str(self.ipifstatsipversion) + '][IP-MIB:ipIfStatsIfIndex = ' + str(self.ipifstatsifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipifstatsipversion is not None:
                    return True

                if self.ipifstatsifindex is not None:
                    return True

                if self.ipifstatsdiscontinuitytime is not None:
                    return True

                if self.ipifstatshcinbcastpkts is not None:
                    return True

                if self.ipifstatshcindelivers is not None:
                    return True

                if self.ipifstatshcinforwdatagrams is not None:
                    return True

                if self.ipifstatshcinmcastoctets is not None:
                    return True

                if self.ipifstatshcinmcastpkts is not None:
                    return True

                if self.ipifstatshcinoctets is not None:
                    return True

                if self.ipifstatshcinreceives is not None:
                    return True

                if self.ipifstatshcoutbcastpkts is not None:
                    return True

                if self.ipifstatshcoutforwdatagrams is not None:
                    return True

                if self.ipifstatshcoutmcastoctets is not None:
                    return True

                if self.ipifstatshcoutmcastpkts is not None:
                    return True

                if self.ipifstatshcoutoctets is not None:
                    return True

                if self.ipifstatshcoutrequests is not None:
                    return True

                if self.ipifstatshcouttransmits is not None:
                    return True

                if self.ipifstatsinaddrerrors is not None:
                    return True

                if self.ipifstatsinbcastpkts is not None:
                    return True

                if self.ipifstatsindelivers is not None:
                    return True

                if self.ipifstatsindiscards is not None:
                    return True

                if self.ipifstatsinforwdatagrams is not None:
                    return True

                if self.ipifstatsinhdrerrors is not None:
                    return True

                if self.ipifstatsinmcastoctets is not None:
                    return True

                if self.ipifstatsinmcastpkts is not None:
                    return True

                if self.ipifstatsinnoroutes is not None:
                    return True

                if self.ipifstatsinoctets is not None:
                    return True

                if self.ipifstatsinreceives is not None:
                    return True

                if self.ipifstatsintruncatedpkts is not None:
                    return True

                if self.ipifstatsinunknownprotos is not None:
                    return True

                if self.ipifstatsoutbcastpkts is not None:
                    return True

                if self.ipifstatsoutdiscards is not None:
                    return True

                if self.ipifstatsoutforwdatagrams is not None:
                    return True

                if self.ipifstatsoutfragcreates is not None:
                    return True

                if self.ipifstatsoutfragfails is not None:
                    return True

                if self.ipifstatsoutfragoks is not None:
                    return True

                if self.ipifstatsoutfragreqds is not None:
                    return True

                if self.ipifstatsoutmcastoctets is not None:
                    return True

                if self.ipifstatsoutmcastpkts is not None:
                    return True

                if self.ipifstatsoutoctets is not None:
                    return True

                if self.ipifstatsoutrequests is not None:
                    return True

                if self.ipifstatsouttransmits is not None:
                    return True

                if self.ipifstatsreasmfails is not None:
                    return True

                if self.ipifstatsreasmoks is not None:
                    return True

                if self.ipifstatsreasmreqds is not None:
                    return True

                if self.ipifstatsrefreshrate is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                return meta._meta_table['IpMib.Ipifstatstable.Ipifstatsentry']['meta_info']

        @property
        def _common_path(self):

            return '/IP-MIB:IP-MIB/IP-MIB:ipIfStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipifstatsentry is not None:
                for child_ref in self.ipifstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
            return meta._meta_table['IpMib.Ipifstatstable']['meta_info']


    class Ipaddressprefixtable(object):
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
            self.parent = None
            self.ipaddressprefixentry = YList()
            self.ipaddressprefixentry.parent = self
            self.ipaddressprefixentry.name = 'ipaddressprefixentry'


        class Ipaddressprefixentry(object):
            """
            An entry in the ipAddressPrefixTable.
            
            .. attribute:: ipaddressprefixifindex  <key>
            
            	The index value that uniquely identifies the interface on which this prefix is configured.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipaddressprefixtype  <key>
            
            	The address type of ipAddressPrefix
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
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
            	**type**\:   :py:class:`IpaddressprefixorigintcEnum <ydk.models.cisco_ios_xe.IP_MIB.IpaddressprefixorigintcEnum>`
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                self.parent = None
                self.ipaddressprefixifindex = None
                self.ipaddressprefixtype = None
                self.ipaddressprefixprefix = None
                self.ipaddressprefixlength = None
                self.ipaddressprefixadvpreferredlifetime = None
                self.ipaddressprefixadvvalidlifetime = None
                self.ipaddressprefixautonomousflag = None
                self.ipaddressprefixonlinkflag = None
                self.ipaddressprefixorigin = None

            @property
            def _common_path(self):
                if self.ipaddressprefixifindex is None:
                    raise YPYModelError('Key property ipaddressprefixifindex is None')
                if self.ipaddressprefixtype is None:
                    raise YPYModelError('Key property ipaddressprefixtype is None')
                if self.ipaddressprefixprefix is None:
                    raise YPYModelError('Key property ipaddressprefixprefix is None')
                if self.ipaddressprefixlength is None:
                    raise YPYModelError('Key property ipaddressprefixlength is None')

                return '/IP-MIB:IP-MIB/IP-MIB:ipAddressPrefixTable/IP-MIB:ipAddressPrefixEntry[IP-MIB:ipAddressPrefixIfIndex = ' + str(self.ipaddressprefixifindex) + '][IP-MIB:ipAddressPrefixType = ' + str(self.ipaddressprefixtype) + '][IP-MIB:ipAddressPrefixPrefix = ' + str(self.ipaddressprefixprefix) + '][IP-MIB:ipAddressPrefixLength = ' + str(self.ipaddressprefixlength) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipaddressprefixifindex is not None:
                    return True

                if self.ipaddressprefixtype is not None:
                    return True

                if self.ipaddressprefixprefix is not None:
                    return True

                if self.ipaddressprefixlength is not None:
                    return True

                if self.ipaddressprefixadvpreferredlifetime is not None:
                    return True

                if self.ipaddressprefixadvvalidlifetime is not None:
                    return True

                if self.ipaddressprefixautonomousflag is not None:
                    return True

                if self.ipaddressprefixonlinkflag is not None:
                    return True

                if self.ipaddressprefixorigin is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                return meta._meta_table['IpMib.Ipaddressprefixtable.Ipaddressprefixentry']['meta_info']

        @property
        def _common_path(self):

            return '/IP-MIB:IP-MIB/IP-MIB:ipAddressPrefixTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipaddressprefixentry is not None:
                for child_ref in self.ipaddressprefixentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
            return meta._meta_table['IpMib.Ipaddressprefixtable']['meta_info']


    class Ipaddresstable(object):
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
            self.parent = None
            self.ipaddressentry = YList()
            self.ipaddressentry.parent = self
            self.ipaddressentry.name = 'ipaddressentry'


        class Ipaddressentry(object):
            """
            An address mapping for a particular interface.
            
            .. attribute:: ipaddressaddrtype  <key>
            
            	The address type of ipAddressAddr
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
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
            	**type**\:   :py:class:`IpaddressorigintcEnum <ydk.models.cisco_ios_xe.IP_MIB.IpaddressorigintcEnum>`
            
            .. attribute:: ipaddressprefix
            
            	A pointer to the row in the prefix table to which this address belongs.  May be { 0 0 } if there is no such row
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: ipaddressrowstatus
            
            	The status of this conceptual row.  The RowStatus TC requires that this DESCRIPTION clause states under which circumstances other objects in this row   can be modified.  The value of this object has no effect on whether other objects in this conceptual row can be modified.  A conceptual row can not be made active until the ipAddressIfIndex has been set to a valid index
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: ipaddressstatus
            
            	The status of the address, describing if the address can be used for communication.  In the absence of other information, an IPv4 address is always preferred(1)
            	**type**\:   :py:class:`IpaddressstatustcEnum <ydk.models.cisco_ios_xe.IP_MIB.IpaddressstatustcEnum>`
            
            .. attribute:: ipaddressstoragetype
            
            	The storage type for this conceptual row.  If this object has a value of 'permanent', then no other objects are required to be able to be modified
            	**type**\:   :py:class:`StoragetypeEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.StoragetypeEnum>`
            
            .. attribute:: ipaddresstype
            
            	The type of address.  broadcast(3) is not a valid value for IPv6 addresses (RFC 3513)
            	**type**\:   :py:class:`IpaddresstypeEnum <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipaddresstable.Ipaddressentry.IpaddresstypeEnum>`
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                self.parent = None
                self.ipaddressaddrtype = None
                self.ipaddressaddr = None
                self.ipaddresscreated = None
                self.ipaddressifindex = None
                self.ipaddresslastchanged = None
                self.ipaddressorigin = None
                self.ipaddressprefix = None
                self.ipaddressrowstatus = None
                self.ipaddressstatus = None
                self.ipaddressstoragetype = None
                self.ipaddresstype = None

            class IpaddresstypeEnum(Enum):
                """
                IpaddresstypeEnum

                The type of address.  broadcast(3) is not a valid value for

                IPv6 addresses (RFC 3513).

                .. data:: unicast = 1

                .. data:: anycast = 2

                .. data:: broadcast = 3

                """

                unicast = 1

                anycast = 2

                broadcast = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                    return meta._meta_table['IpMib.Ipaddresstable.Ipaddressentry.IpaddresstypeEnum']


            @property
            def _common_path(self):
                if self.ipaddressaddrtype is None:
                    raise YPYModelError('Key property ipaddressaddrtype is None')
                if self.ipaddressaddr is None:
                    raise YPYModelError('Key property ipaddressaddr is None')

                return '/IP-MIB:IP-MIB/IP-MIB:ipAddressTable/IP-MIB:ipAddressEntry[IP-MIB:ipAddressAddrType = ' + str(self.ipaddressaddrtype) + '][IP-MIB:ipAddressAddr = ' + str(self.ipaddressaddr) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipaddressaddrtype is not None:
                    return True

                if self.ipaddressaddr is not None:
                    return True

                if self.ipaddresscreated is not None:
                    return True

                if self.ipaddressifindex is not None:
                    return True

                if self.ipaddresslastchanged is not None:
                    return True

                if self.ipaddressorigin is not None:
                    return True

                if self.ipaddressprefix is not None:
                    return True

                if self.ipaddressrowstatus is not None:
                    return True

                if self.ipaddressstatus is not None:
                    return True

                if self.ipaddressstoragetype is not None:
                    return True

                if self.ipaddresstype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                return meta._meta_table['IpMib.Ipaddresstable.Ipaddressentry']['meta_info']

        @property
        def _common_path(self):

            return '/IP-MIB:IP-MIB/IP-MIB:ipAddressTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipaddressentry is not None:
                for child_ref in self.ipaddressentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
            return meta._meta_table['IpMib.Ipaddresstable']['meta_info']


    class Ipnettophysicaltable(object):
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
            self.parent = None
            self.ipnettophysicalentry = YList()
            self.ipnettophysicalentry.parent = self
            self.ipnettophysicalentry.name = 'ipnettophysicalentry'


        class Ipnettophysicalentry(object):
            """
            Each entry contains one IP address to `physical' address
            equivalence.
            
            .. attribute:: ipnettophysicalifindex  <key>
            
            	The index value that uniquely identifies the interface to which this entry is applicable.  The interface identified by a particular value of this index is the same interface as identified by the same value of the IF\-MIB's ifIndex
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: ipnettophysicalnetaddresstype  <key>
            
            	The type of ipNetToPhysicalNetAddress
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: ipnettophysicalstate
            
            	The Neighbor Unreachability Detection state for the interface when the address mapping in this entry is used. If Neighbor Unreachability Detection is not in use (e.g. for IPv4), this object is always unknown(6)
            	**type**\:   :py:class:`IpnettophysicalstateEnum <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipnettophysicaltable.Ipnettophysicalentry.IpnettophysicalstateEnum>`
            
            .. attribute:: ipnettophysicaltype
            
            	The type of mapping.  Setting this object to the value invalid(2) has the effect of invalidating the corresponding entry in the ipNetToPhysicalTable.  That is, it effectively dis\- associates the interface identified with said entry from the mapping identified with said entry.  It is an implementation\-specific matter as to whether the agent   removes an invalidated entry from the table.  Accordingly, management stations must be prepared to receive tabular information from agents that corresponds to entries not currently in use.  Proper interpretation of such entries requires examination of the relevant ipNetToPhysicalType object.  The 'dynamic(3)' type indicates that the IP address to physical addresses mapping has been dynamically resolved using e.g., IPv4 ARP or the IPv6 Neighbor Discovery protocol.  The 'static(4)' type indicates that the mapping has been statically configured.  Both of these refer to entries that provide mappings for other entities addresses.  The 'local(5)' type indicates that the mapping is provided for an entity's own interface address.  As the entries in this table are typically not persistent when this object is written the entity SHOULD NOT save the change to non\-volatile storage
            	**type**\:   :py:class:`IpnettophysicaltypeEnum <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipnettophysicaltable.Ipnettophysicalentry.IpnettophysicaltypeEnum>`
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                self.parent = None
                self.ipnettophysicalifindex = None
                self.ipnettophysicalnetaddresstype = None
                self.ipnettophysicalnetaddress = None
                self.ipnettophysicallastupdated = None
                self.ipnettophysicalphysaddress = None
                self.ipnettophysicalrowstatus = None
                self.ipnettophysicalstate = None
                self.ipnettophysicaltype = None

            class IpnettophysicalstateEnum(Enum):
                """
                IpnettophysicalstateEnum

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

                reachable = 1

                stale = 2

                delay = 3

                probe = 4

                invalid = 5

                unknown = 6

                incomplete = 7


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                    return meta._meta_table['IpMib.Ipnettophysicaltable.Ipnettophysicalentry.IpnettophysicalstateEnum']


            class IpnettophysicaltypeEnum(Enum):
                """
                IpnettophysicaltypeEnum

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

                other = 1

                invalid = 2

                dynamic = 3

                static = 4

                local = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                    return meta._meta_table['IpMib.Ipnettophysicaltable.Ipnettophysicalentry.IpnettophysicaltypeEnum']


            @property
            def _common_path(self):
                if self.ipnettophysicalifindex is None:
                    raise YPYModelError('Key property ipnettophysicalifindex is None')
                if self.ipnettophysicalnetaddresstype is None:
                    raise YPYModelError('Key property ipnettophysicalnetaddresstype is None')
                if self.ipnettophysicalnetaddress is None:
                    raise YPYModelError('Key property ipnettophysicalnetaddress is None')

                return '/IP-MIB:IP-MIB/IP-MIB:ipNetToPhysicalTable/IP-MIB:ipNetToPhysicalEntry[IP-MIB:ipNetToPhysicalIfIndex = ' + str(self.ipnettophysicalifindex) + '][IP-MIB:ipNetToPhysicalNetAddressType = ' + str(self.ipnettophysicalnetaddresstype) + '][IP-MIB:ipNetToPhysicalNetAddress = ' + str(self.ipnettophysicalnetaddress) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipnettophysicalifindex is not None:
                    return True

                if self.ipnettophysicalnetaddresstype is not None:
                    return True

                if self.ipnettophysicalnetaddress is not None:
                    return True

                if self.ipnettophysicallastupdated is not None:
                    return True

                if self.ipnettophysicalphysaddress is not None:
                    return True

                if self.ipnettophysicalrowstatus is not None:
                    return True

                if self.ipnettophysicalstate is not None:
                    return True

                if self.ipnettophysicaltype is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                return meta._meta_table['IpMib.Ipnettophysicaltable.Ipnettophysicalentry']['meta_info']

        @property
        def _common_path(self):

            return '/IP-MIB:IP-MIB/IP-MIB:ipNetToPhysicalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipnettophysicalentry is not None:
                for child_ref in self.ipnettophysicalentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
            return meta._meta_table['IpMib.Ipnettophysicaltable']['meta_info']


    class Ipv6Scopezoneindextable(object):
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
            self.parent = None
            self.ipv6scopezoneindexentry = YList()
            self.ipv6scopezoneindexentry.parent = self
            self.ipv6scopezoneindexentry.name = 'ipv6scopezoneindexentry'


        class Ipv6Scopezoneindexentry(object):
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
                self.parent = None
                self.ipv6scopezoneindexifindex = None
                self.ipv6scopezoneindex3 = None
                self.ipv6scopezoneindex6 = None
                self.ipv6scopezoneindex7 = None
                self.ipv6scopezoneindex9 = None
                self.ipv6scopezoneindexa = None
                self.ipv6scopezoneindexadminlocal = None
                self.ipv6scopezoneindexb = None
                self.ipv6scopezoneindexc = None
                self.ipv6scopezoneindexd = None
                self.ipv6scopezoneindexlinklocal = None
                self.ipv6scopezoneindexorganizationlocal = None
                self.ipv6scopezoneindexsitelocal = None

            @property
            def _common_path(self):
                if self.ipv6scopezoneindexifindex is None:
                    raise YPYModelError('Key property ipv6scopezoneindexifindex is None')

                return '/IP-MIB:IP-MIB/IP-MIB:ipv6ScopeZoneIndexTable/IP-MIB:ipv6ScopeZoneIndexEntry[IP-MIB:ipv6ScopeZoneIndexIfIndex = ' + str(self.ipv6scopezoneindexifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipv6scopezoneindexifindex is not None:
                    return True

                if self.ipv6scopezoneindex3 is not None:
                    return True

                if self.ipv6scopezoneindex6 is not None:
                    return True

                if self.ipv6scopezoneindex7 is not None:
                    return True

                if self.ipv6scopezoneindex9 is not None:
                    return True

                if self.ipv6scopezoneindexa is not None:
                    return True

                if self.ipv6scopezoneindexadminlocal is not None:
                    return True

                if self.ipv6scopezoneindexb is not None:
                    return True

                if self.ipv6scopezoneindexc is not None:
                    return True

                if self.ipv6scopezoneindexd is not None:
                    return True

                if self.ipv6scopezoneindexlinklocal is not None:
                    return True

                if self.ipv6scopezoneindexorganizationlocal is not None:
                    return True

                if self.ipv6scopezoneindexsitelocal is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                return meta._meta_table['IpMib.Ipv6Scopezoneindextable.Ipv6Scopezoneindexentry']['meta_info']

        @property
        def _common_path(self):

            return '/IP-MIB:IP-MIB/IP-MIB:ipv6ScopeZoneIndexTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipv6scopezoneindexentry is not None:
                for child_ref in self.ipv6scopezoneindexentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
            return meta._meta_table['IpMib.Ipv6Scopezoneindextable']['meta_info']


    class Ipdefaultroutertable(object):
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
            self.parent = None
            self.ipdefaultrouterentry = YList()
            self.ipdefaultrouterentry.parent = self
            self.ipdefaultrouterentry.name = 'ipdefaultrouterentry'


        class Ipdefaultrouterentry(object):
            """
            Each entry contains information about a default router known
            to this entity.
            
            .. attribute:: ipdefaultrouteraddresstype  <key>
            
            	The address type for this row
            	**type**\:   :py:class:`InetaddresstypeEnum <ydk.models.cisco_ios_xe.INET_ADDRESS_MIB.InetaddresstypeEnum>`
            
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
            	**type**\:   :py:class:`IpdefaultrouterpreferenceEnum <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Ipdefaultroutertable.Ipdefaultrouterentry.IpdefaultrouterpreferenceEnum>`
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                self.parent = None
                self.ipdefaultrouteraddresstype = None
                self.ipdefaultrouteraddress = None
                self.ipdefaultrouterifindex = None
                self.ipdefaultrouterlifetime = None
                self.ipdefaultrouterpreference = None

            class IpdefaultrouterpreferenceEnum(Enum):
                """
                IpdefaultrouterpreferenceEnum

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

                reserved = -2

                low = -1

                medium = 0

                high = 1


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                    return meta._meta_table['IpMib.Ipdefaultroutertable.Ipdefaultrouterentry.IpdefaultrouterpreferenceEnum']


            @property
            def _common_path(self):
                if self.ipdefaultrouteraddresstype is None:
                    raise YPYModelError('Key property ipdefaultrouteraddresstype is None')
                if self.ipdefaultrouteraddress is None:
                    raise YPYModelError('Key property ipdefaultrouteraddress is None')
                if self.ipdefaultrouterifindex is None:
                    raise YPYModelError('Key property ipdefaultrouterifindex is None')

                return '/IP-MIB:IP-MIB/IP-MIB:ipDefaultRouterTable/IP-MIB:ipDefaultRouterEntry[IP-MIB:ipDefaultRouterAddressType = ' + str(self.ipdefaultrouteraddresstype) + '][IP-MIB:ipDefaultRouterAddress = ' + str(self.ipdefaultrouteraddress) + '][IP-MIB:ipDefaultRouterIfIndex = ' + str(self.ipdefaultrouterifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipdefaultrouteraddresstype is not None:
                    return True

                if self.ipdefaultrouteraddress is not None:
                    return True

                if self.ipdefaultrouterifindex is not None:
                    return True

                if self.ipdefaultrouterlifetime is not None:
                    return True

                if self.ipdefaultrouterpreference is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                return meta._meta_table['IpMib.Ipdefaultroutertable.Ipdefaultrouterentry']['meta_info']

        @property
        def _common_path(self):

            return '/IP-MIB:IP-MIB/IP-MIB:ipDefaultRouterTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipdefaultrouterentry is not None:
                for child_ref in self.ipdefaultrouterentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
            return meta._meta_table['IpMib.Ipdefaultroutertable']['meta_info']


    class Ipv6Routeradverttable(object):
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
            self.parent = None
            self.ipv6routeradvertentry = YList()
            self.ipv6routeradvertentry.parent = self
            self.ipv6routeradvertentry.name = 'ipv6routeradvertentry'


        class Ipv6Routeradvertentry(object):
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
            	**type**\:   :py:class:`RowstatusEnum <ydk.models.cisco_ios_xe.SNMPv2_TC.RowstatusEnum>`
            
            .. attribute:: ipv6routeradvertsendadverts
            
            	A flag indicating whether the router sends periodic router advertisements and responds to router solicitations on this interface
            	**type**\:  bool
            
            

            """

            _prefix = 'IP-MIB'
            _revision = '2006-02-02'

            def __init__(self):
                self.parent = None
                self.ipv6routeradvertifindex = None
                self.ipv6routeradvertcurhoplimit = None
                self.ipv6routeradvertdefaultlifetime = None
                self.ipv6routeradvertlinkmtu = None
                self.ipv6routeradvertmanagedflag = None
                self.ipv6routeradvertmaxinterval = None
                self.ipv6routeradvertmininterval = None
                self.ipv6routeradvertotherconfigflag = None
                self.ipv6routeradvertreachabletime = None
                self.ipv6routeradvertretransmittime = None
                self.ipv6routeradvertrowstatus = None
                self.ipv6routeradvertsendadverts = None

            @property
            def _common_path(self):
                if self.ipv6routeradvertifindex is None:
                    raise YPYModelError('Key property ipv6routeradvertifindex is None')

                return '/IP-MIB:IP-MIB/IP-MIB:ipv6RouterAdvertTable/IP-MIB:ipv6RouterAdvertEntry[IP-MIB:ipv6RouterAdvertIfIndex = ' + str(self.ipv6routeradvertifindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.ipv6routeradvertifindex is not None:
                    return True

                if self.ipv6routeradvertcurhoplimit is not None:
                    return True

                if self.ipv6routeradvertdefaultlifetime is not None:
                    return True

                if self.ipv6routeradvertlinkmtu is not None:
                    return True

                if self.ipv6routeradvertmanagedflag is not None:
                    return True

                if self.ipv6routeradvertmaxinterval is not None:
                    return True

                if self.ipv6routeradvertmininterval is not None:
                    return True

                if self.ipv6routeradvertotherconfigflag is not None:
                    return True

                if self.ipv6routeradvertreachabletime is not None:
                    return True

                if self.ipv6routeradvertretransmittime is not None:
                    return True

                if self.ipv6routeradvertrowstatus is not None:
                    return True

                if self.ipv6routeradvertsendadverts is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                return meta._meta_table['IpMib.Ipv6Routeradverttable.Ipv6Routeradvertentry']['meta_info']

        @property
        def _common_path(self):

            return '/IP-MIB:IP-MIB/IP-MIB:ipv6RouterAdvertTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.ipv6routeradvertentry is not None:
                for child_ref in self.ipv6routeradvertentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
            return meta._meta_table['IpMib.Ipv6Routeradverttable']['meta_info']


    class Icmpstatstable(object):
        """
        The table of generic system\-wide ICMP counters.
        
        .. attribute:: icmpstatsentry
        
        	A conceptual row in the icmpStatsTable
        	**type**\: list of    :py:class:`Icmpstatsentry <ydk.models.cisco_ios_xe.IP_MIB.IpMib.Icmpstatstable.Icmpstatsentry>`
        
        

        """

        _prefix = 'IP-MIB'
        _revision = '2006-02-02'

        def __init__(self):
            self.parent = None
            self.icmpstatsentry = YList()
            self.icmpstatsentry.parent = self
            self.icmpstatsentry.name = 'icmpstatsentry'


        class Icmpstatsentry(object):
            """
            A conceptual row in the icmpStatsTable.
            
            .. attribute:: icmpstatsipversion  <key>
            
            	The IP version of the statistics
            	**type**\:   :py:class:`IpVersionEnum <ydk.models.ietf.ietf_inet_types.IpVersionEnum>`
            
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
                self.parent = None
                self.icmpstatsipversion = None
                self.icmpstatsinerrors = None
                self.icmpstatsinmsgs = None
                self.icmpstatsouterrors = None
                self.icmpstatsoutmsgs = None

            @property
            def _common_path(self):
                if self.icmpstatsipversion is None:
                    raise YPYModelError('Key property icmpstatsipversion is None')

                return '/IP-MIB:IP-MIB/IP-MIB:icmpStatsTable/IP-MIB:icmpStatsEntry[IP-MIB:icmpStatsIPVersion = ' + str(self.icmpstatsipversion) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.icmpstatsipversion is not None:
                    return True

                if self.icmpstatsinerrors is not None:
                    return True

                if self.icmpstatsinmsgs is not None:
                    return True

                if self.icmpstatsouterrors is not None:
                    return True

                if self.icmpstatsoutmsgs is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                return meta._meta_table['IpMib.Icmpstatstable.Icmpstatsentry']['meta_info']

        @property
        def _common_path(self):

            return '/IP-MIB:IP-MIB/IP-MIB:icmpStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.icmpstatsentry is not None:
                for child_ref in self.icmpstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
            return meta._meta_table['IpMib.Icmpstatstable']['meta_info']


    class Icmpmsgstatstable(object):
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
            self.parent = None
            self.icmpmsgstatsentry = YList()
            self.icmpmsgstatsentry.parent = self
            self.icmpmsgstatsentry.name = 'icmpmsgstatsentry'


        class Icmpmsgstatsentry(object):
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
            	**type**\:   :py:class:`IpVersionEnum <ydk.models.ietf.ietf_inet_types.IpVersionEnum>`
            
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
                self.parent = None
                self.icmpmsgstatsipversion = None
                self.icmpmsgstatstype = None
                self.icmpmsgstatsinpkts = None
                self.icmpmsgstatsoutpkts = None

            @property
            def _common_path(self):
                if self.icmpmsgstatsipversion is None:
                    raise YPYModelError('Key property icmpmsgstatsipversion is None')
                if self.icmpmsgstatstype is None:
                    raise YPYModelError('Key property icmpmsgstatstype is None')

                return '/IP-MIB:IP-MIB/IP-MIB:icmpMsgStatsTable/IP-MIB:icmpMsgStatsEntry[IP-MIB:icmpMsgStatsIPVersion = ' + str(self.icmpmsgstatsipversion) + '][IP-MIB:icmpMsgStatsType = ' + str(self.icmpmsgstatstype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.icmpmsgstatsipversion is not None:
                    return True

                if self.icmpmsgstatstype is not None:
                    return True

                if self.icmpmsgstatsinpkts is not None:
                    return True

                if self.icmpmsgstatsoutpkts is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
                return meta._meta_table['IpMib.Icmpmsgstatstable.Icmpmsgstatsentry']['meta_info']

        @property
        def _common_path(self):

            return '/IP-MIB:IP-MIB/IP-MIB:icmpMsgStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.icmpmsgstatsentry is not None:
                for child_ref in self.icmpmsgstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
            return meta._meta_table['IpMib.Icmpmsgstatstable']['meta_info']

    @property
    def _common_path(self):

        return '/IP-MIB:IP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.icmp is not None and self.icmp._has_data():
            return True

        if self.icmpmsgstatstable is not None and self.icmpmsgstatstable._has_data():
            return True

        if self.icmpstatstable is not None and self.icmpstatstable._has_data():
            return True

        if self.ip is not None and self.ip._has_data():
            return True

        if self.ipaddressprefixtable is not None and self.ipaddressprefixtable._has_data():
            return True

        if self.ipaddresstable is not None and self.ipaddresstable._has_data():
            return True

        if self.ipaddrtable is not None and self.ipaddrtable._has_data():
            return True

        if self.ipdefaultroutertable is not None and self.ipdefaultroutertable._has_data():
            return True

        if self.ipifstatstable is not None and self.ipifstatstable._has_data():
            return True

        if self.ipnettomediatable is not None and self.ipnettomediatable._has_data():
            return True

        if self.ipnettophysicaltable is not None and self.ipnettophysicaltable._has_data():
            return True

        if self.ipsystemstatstable is not None and self.ipsystemstatstable._has_data():
            return True

        if self.iptrafficstats is not None and self.iptrafficstats._has_data():
            return True

        if self.ipv4interfacetable is not None and self.ipv4interfacetable._has_data():
            return True

        if self.ipv6interfacetable is not None and self.ipv6interfacetable._has_data():
            return True

        if self.ipv6routeradverttable is not None and self.ipv6routeradverttable._has_data():
            return True

        if self.ipv6scopezoneindextable is not None and self.ipv6scopezoneindextable._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _IP_MIB as meta
        return meta._meta_table['IpMib']['meta_info']


