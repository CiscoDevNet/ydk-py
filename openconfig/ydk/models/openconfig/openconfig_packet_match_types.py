""" openconfig_packet_match_types 

This module defines common types for use in models requiring
data definitions related to packet matches.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class PortNumRange(Enum):
    """
    PortNumRange (Enum Class)

    Port numbers may be represented as a single value,

    an inclusive range as <lower>..<higher>, or as ANY to

    indicate a wildcard.

    .. data:: ANY = 0

    	Indicates any valid port number (e.g., wildcard)

    """

    ANY = Enum.YLeaf(0, "ANY")



class ETHERTYPE(Identity):
    """
    Base identity for commonly used Ethertype values used
    in packet header matches on Ethernet frames.  The Ethertype
    indicates which protocol is encapsulated in the Ethernet
    payload.
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(ETHERTYPE, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:ETHERTYPE")


class IPPROTOCOL(Identity):
    """
    Base identity for commonly used IP protocols used in
    packet header matches
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(IPPROTOCOL, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:IP_PROTOCOL")


class TCPFLAGS(Identity):
    """
    Common TCP flags used in packet header matches
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(TCPFLAGS, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:TCP_FLAGS")


class ETHERTYPEIPV4(Identity):
    """
    IPv4 protocol (0x0800)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(ETHERTYPEIPV4, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:ETHERTYPE_IPV4")


class ETHERTYPEARP(Identity):
    """
    Address resolution protocol (0x0806)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(ETHERTYPEARP, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:ETHERTYPE_ARP")


class ETHERTYPEVLAN(Identity):
    """
    VLAN\-tagged frame (as defined by IEEE 802.1q) (0x8100). Note
    that this value is also used to represent Shortest Path
    Bridging (IEEE 801.1aq) frames.
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(ETHERTYPEVLAN, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:ETHERTYPE_VLAN")


class ETHERTYPEIPV6(Identity):
    """
    IPv6 protocol (0x86DD)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(ETHERTYPEIPV6, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:ETHERTYPE_IPV6")


class ETHERTYPEMPLS(Identity):
    """
    MPLS unicast (0x8847)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(ETHERTYPEMPLS, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:ETHERTYPE_MPLS")


class ETHERTYPELLDP(Identity):
    """
    Link Layer Discovery Protocol (0x88CC)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(ETHERTYPELLDP, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:ETHERTYPE_LLDP")


class ETHERTYPEROCE(Identity):
    """
    RDMA over Converged Ethernet (0x8915)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(ETHERTYPEROCE, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:ETHERTYPE_ROCE")


class IPTCP(Identity):
    """
    Transmission Control Protocol (6)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(IPTCP, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:IP_TCP")


class IPUDP(Identity):
    """
    User Datagram Protocol (17)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(IPUDP, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:IP_UDP")


class IPICMP(Identity):
    """
    Internet Control Message Protocol (1)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(IPICMP, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:IP_ICMP")


class IPIGMP(Identity):
    """
    Internet Group Membership Protocol (2)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(IPIGMP, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:IP_IGMP")


class IPPIM(Identity):
    """
    Protocol Independent Multicast (103)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(IPPIM, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:IP_PIM")


class IPRSVP(Identity):
    """
    Resource Reservation Protocol (46)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(IPRSVP, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:IP_RSVP")


class IPGRE(Identity):
    """
    Generic Routing Encapsulation (47)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(IPGRE, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:IP_GRE")


class IPAUTH(Identity):
    """
    Authentication header, e.g., for IPSEC (51)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(IPAUTH, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:IP_AUTH")


class IPL2TP(Identity):
    """
    Layer Two Tunneling Protocol v.3 (115)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(IPL2TP, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:IP_L2TP")


class TCPSYN(Identity):
    """
    TCP SYN flag
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(TCPSYN, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:TCP_SYN")


class TCPFIN(Identity):
    """
    TCP FIN flag
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(TCPFIN, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:TCP_FIN")


class TCPRST(Identity):
    """
    TCP RST flag
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(TCPRST, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:TCP_RST")


class TCPPSH(Identity):
    """
    TCP push flag
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(TCPPSH, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:TCP_PSH")


class TCPACK(Identity):
    """
    TCP ACK flag
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(TCPACK, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:TCP_ACK")


class TCPURG(Identity):
    """
    TCP urgent flag
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(TCPURG, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:TCP_URG")


class TCPECE(Identity):
    """
    TCP ECN\-Echo flag.  If the SYN flag is set, indicates that
    the TCP peer is ECN\-capable, otherwise indicates that a
    packet with Congestion Experienced flag in the IP header
    is set
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(TCPECE, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:TCP_ECE")


class TCPCWR(Identity):
    """
    TCP Congestion Window Reduced flag
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2016-08-08'

    def __init__(self):
        super(TCPCWR, self).__init__("http://openconfig.net/yang/packet-match-types", "openconfig-packet-match-types", "openconfig-packet-match-types:TCP_CWR")


