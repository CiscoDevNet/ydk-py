""" openconfig_packet_match_types 

This module defines common types for use in models requiring
data definitions related to packet matches.

"""
import sys
from collections import OrderedDict

from ydk.types import Entity as _Entity_
from ydk.types import EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
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
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:ETHERTYPE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETHERTYPE, self).__init__(ns, pref, tag)



class IPPROTOCOL(Identity):
    """
    Base identity for commonly used IP protocols used in
    packet header matches
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:IP_PROTOCOL"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IPPROTOCOL, self).__init__(ns, pref, tag)



class TCPFLAGS(Identity):
    """
    Common TCP flags used in packet header matches
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:TCP_FLAGS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TCPFLAGS, self).__init__(ns, pref, tag)



class ETHERTYPEIPV4(ETHERTYPE):
    """
    IPv4 protocol (0x0800)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:ETHERTYPE_IPV4"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETHERTYPEIPV4, self).__init__(ns, pref, tag)



class ETHERTYPEARP(ETHERTYPE):
    """
    Address resolution protocol (0x0806)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:ETHERTYPE_ARP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETHERTYPEARP, self).__init__(ns, pref, tag)



class ETHERTYPEVLAN(ETHERTYPE):
    """
    VLAN\-tagged frame (as defined by IEEE 802.1q) (0x8100). Note
    that this value is also used to represent Shortest Path
    Bridging (IEEE 801.1aq) frames.
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:ETHERTYPE_VLAN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETHERTYPEVLAN, self).__init__(ns, pref, tag)



class ETHERTYPEIPV6(ETHERTYPE):
    """
    IPv6 protocol (0x86DD)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:ETHERTYPE_IPV6"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETHERTYPEIPV6, self).__init__(ns, pref, tag)



class ETHERTYPEMPLS(ETHERTYPE):
    """
    MPLS unicast (0x8847)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:ETHERTYPE_MPLS"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETHERTYPEMPLS, self).__init__(ns, pref, tag)



class ETHERTYPELLDP(ETHERTYPE):
    """
    Link Layer Discovery Protocol (0x88CC)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:ETHERTYPE_LLDP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETHERTYPELLDP, self).__init__(ns, pref, tag)



class ETHERTYPEROCE(ETHERTYPE):
    """
    RDMA over Converged Ethernet (0x8915)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:ETHERTYPE_ROCE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(ETHERTYPEROCE, self).__init__(ns, pref, tag)



class IPTCP(IPPROTOCOL):
    """
    Transmission Control Protocol (6)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:IP_TCP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IPTCP, self).__init__(ns, pref, tag)



class IPUDP(IPPROTOCOL):
    """
    User Datagram Protocol (17)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:IP_UDP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IPUDP, self).__init__(ns, pref, tag)



class IPICMP(IPPROTOCOL):
    """
    Internet Control Message Protocol (1)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:IP_ICMP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IPICMP, self).__init__(ns, pref, tag)



class IPIGMP(IPPROTOCOL):
    """
    Internet Group Membership Protocol (2)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:IP_IGMP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IPIGMP, self).__init__(ns, pref, tag)



class IPPIM(IPPROTOCOL):
    """
    Protocol Independent Multicast (103)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:IP_PIM"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IPPIM, self).__init__(ns, pref, tag)



class IPRSVP(IPPROTOCOL):
    """
    Resource Reservation Protocol (46)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:IP_RSVP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IPRSVP, self).__init__(ns, pref, tag)



class IPGRE(IPPROTOCOL):
    """
    Generic Routing Encapsulation (47)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:IP_GRE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IPGRE, self).__init__(ns, pref, tag)



class IPAUTH(IPPROTOCOL):
    """
    Authentication header, e.g., for IPSEC (51)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:IP_AUTH"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IPAUTH, self).__init__(ns, pref, tag)



class IPL2TP(IPPROTOCOL):
    """
    Layer Two Tunneling Protocol v.3 (115)
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:IP_L2TP"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(IPL2TP, self).__init__(ns, pref, tag)



class TCPSYN(TCPFLAGS):
    """
    TCP SYN flag
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:TCP_SYN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TCPSYN, self).__init__(ns, pref, tag)



class TCPFIN(TCPFLAGS):
    """
    TCP FIN flag
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:TCP_FIN"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TCPFIN, self).__init__(ns, pref, tag)



class TCPRST(TCPFLAGS):
    """
    TCP RST flag
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:TCP_RST"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TCPRST, self).__init__(ns, pref, tag)



class TCPPSH(TCPFLAGS):
    """
    TCP push flag
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:TCP_PSH"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TCPPSH, self).__init__(ns, pref, tag)



class TCPACK(TCPFLAGS):
    """
    TCP ACK flag
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:TCP_ACK"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TCPACK, self).__init__(ns, pref, tag)



class TCPURG(TCPFLAGS):
    """
    TCP urgent flag
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:TCP_URG"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TCPURG, self).__init__(ns, pref, tag)



class TCPECE(TCPFLAGS):
    """
    TCP ECN\-Echo flag.  If the SYN flag is set, indicates that
    the TCP peer is ECN\-capable, otherwise indicates that a
    packet with Congestion Experienced flag in the IP header
    is set
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:TCP_ECE"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TCPECE, self).__init__(ns, pref, tag)



class TCPCWR(TCPFLAGS):
    """
    TCP Congestion Window Reduced flag
    
    

    """

    _prefix = 'oc-pkt-match-types'
    _revision = '2017-05-26'

    def __init__(self, ns="http://openconfig.net/yang/packet-match-types", pref="openconfig-packet-match-types", tag="openconfig-packet-match-types:TCP_CWR"):
        if sys.version_info > (3,):
            super().__init__(ns, pref, tag)
        else:
            super(TCPCWR, self).__init__(ns, pref, tag)



