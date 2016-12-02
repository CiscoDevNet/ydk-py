""" Cisco_IOS_XR_lpts_pre_ifib_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-pre\-ifib package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-lpts\-lib\-cfg
  Cisco\-IOS\-XR\-config\-mda\-cfg
modules with configuration data.

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class LptsFlowEnum(Enum):
    """
    LptsFlowEnum

    Lpts flow

    .. data:: config_default = 0

    	Invalid flow type used for fallback

    	configuration

    .. data:: l2tpv2_fragment = 1

    	L2TPv2 Fragments

    .. data:: fragment = 2

    	Fragments

    .. data:: ospf_multicast_known = 3

    	OSPF multicast packets on configured interfaces

    .. data:: ospf_multicast_default = 4

    	OSPF multicast packets on unconfigured (or

    	newly-configured) interfaces

    .. data:: ospf_unicast_known = 5

    	OSPF unicast packets

    .. data:: ospf_unicast_default = 6

    	OSPF unicast packets

    .. data:: isis_known = 7

    	IS-IS packets on configured interfaces

    .. data:: isis_default = 8

    	IS-IS packets on unconfigured (or

    	newly-configured) interfaces

    .. data:: bfd_known = 9

    	BFD packets on configured interfaces

    .. data:: bfd_default = 10

    	BFD packets on unconfigured (or

    	newly-configured) interfaces

    .. data:: bfd_multipath_known = 11

    	BFD multipath packets on configured interfaces

    .. data:: bfd_multipath0 = 12

    	BFD multipath packets on multiple configured

    	interfaces

    .. data:: bfd_blb_known = 13

    	BFD packets over Logical Bundle on configured

    	interfaces

    .. data:: bfd_blb0 = 14

    	BFD packets over Logical Bundle 0

    .. data:: bfd_sp0 = 15

    	BFD packets over Single Path 0

    .. data:: bgp_known = 16

    	Packets from established BGP peering sessions

    .. data:: bgp_config_peer = 17

    	Packets from a configured BGP peer (SYNs or

    	newly-established sessions)

    .. data:: bgp_default = 18

    	Packets from unconfigured, newly-configured, or

    	wild-card BGP peer

    .. data:: pim_multicast_default = 19

    	PIM multicast packets on configured interfaces

    .. data:: pim_multicast_known = 20

    	PIM multicast packets on unconfigured (or

    	newly-configured) interfaces

    .. data:: pim_unicast = 21

    	PIM unicast packets

    .. data:: igmp = 22

    	IGMP packets

    .. data:: icmp_local = 23

    	ICMP or ICMPv6 packets with local interest

    .. data:: icmp_app = 24

    	ICMP or ICMPv6 packets of interest to

    	applications

    .. data:: icmp_control = 25

    	ICMP or ICMPv6 packets that are used for

    	control/signalling purpose

    .. data:: icmp_default = 26

    	Other ICMP or ICMPv6 packets (may be of recent

    	interest to applications)

    .. data:: icmp_app_default = 27

    	ICMP or ICMPv6 echo reply packets (when

    	specific entry not present)

    .. data:: ldp_tcp_known = 28

    	Packets from an established LDP TCP peering

    	session

    .. data:: ldp_tcp_config_peer = 29

    	Packets from a configured LDP TCP peer (SYNs or

    	newly-established sessions)

    .. data:: ldp_tcp_default = 30

    	Packets from an unconfigured, newly-configured

    	or wild-card LDP TCP peer

    .. data:: ldp_udp = 31

    	Unicast LDP UDP packets

    .. data:: all_routers = 32

    	Packets sent to the all-routers multicast

    	address (includes LDP UDP multicast)

    .. data:: lmp_tcp_known = 33

    	Packets from an established LMP TCP peering

    	session

    .. data:: lmp_tcp_config_peer = 34

    	Packets from a configured LMP TCP peer (SYNs or

    	newly-established sessions)

    .. data:: lmp_tcp_default = 35

    	Packets from an unconfigured, newly-configured

    	or wild-card LMP TCP peer

    .. data:: lmp_udp = 36

    	Unicast LMP UDP packets

    .. data:: rsvp_udp = 37

    	RSVP-over-UDP packets

    .. data:: rsvp_default = 38

    	RSVP (IP protocol 46) packets

    .. data:: rsvp_known = 39

    	RSVP (IP protocol 46) packets

    .. data:: ike = 40

    	IKE packets

    .. data:: ipsec_known = 41

    	AH or ESP packets with known SPIs

    .. data:: ipsec_default = 42

    	AH or ESP packets with unknown or

    	newly-configured SPIs

    .. data:: ipsec_fragment = 43

    	AH or ESP fragmented packets

    .. data:: msdp_known = 44

    	Packets from an established MSDP session

    .. data:: msdp_config_peer = 45

    	Packets from a configured MSDP peer

    .. data:: msdp_default = 46

    	Packets from an uncofigured, newly-configured

    	or wild-card MSDP peer

    .. data:: snmp = 47

    	SNMP packets

    .. data:: ssh_known = 48

    	Packets from an established SSH session

    .. data:: ssh_default = 49

    	Packets from a new or newly-established SSH

    	session

    .. data:: http_known = 50

    	Packets from an established HTTP session

    .. data:: http_default = 51

    	Packets from a new or newly-established HTTP

    	session

    .. data:: shttp_known = 52

    	Packets from an established SHTTP session

    .. data:: shttp_default = 53

    	Packets from a new or newly-established SSHTP

    	session

    .. data:: telnet_known = 54

    	Packets from an established TELNET session

    .. data:: telnet_default = 55

    	Packets from a new or newly-established TELNET

    	session

    .. data:: css_known = 56

    	Packets from an established CSS session

    .. data:: css_default = 57

    	Packets from a new or newly-established CSS

    	session

    .. data:: rsh_known = 58

    	Packets from an established rsh session

    .. data:: rsh_default = 59

    	Packets from a new or newly-established rsh

    	session

    .. data:: udp_known = 60

    	Packets for established UDP sessions

    .. data:: udp_listen = 61

    	Packets for configured UDP services

    .. data:: udp_config_peer = 62

    	Packets for configured UDP-based protocol

    	sessions

    .. data:: udp_default = 63

    	Packets for unconfigured or newly-configured

    	UDP services

    .. data:: tcp_known = 64

    	Packets for established TCP sessions

    .. data:: tcp_listen = 65

    	Packets for configured TCP services

    .. data:: tcp_config_peer = 66

    	Packets for configured TCP peers

    .. data:: tcp_default = 67

    	Packets for unconfigured or newly-configured

    	TCP services

    .. data:: multicast_known = 68

    	Packets for configured multicast groups

    .. data:: multicast_default = 69

    	Packets for unconfigured or newly-configured

    	multicast groups

    .. data:: raw_listen = 70

    	Packets for configured IP protocols

    .. data:: raw_default = 71

    	Packets for unconfigured or newly-configured

    	IPv4 or IPv6 protocols

    .. data:: ipsla = 72

    	IP SLA packets destined to squid Q #4 for

    	timestamping by squid driver

    .. data:: eigrp = 73

    	EIGRP packets.

    .. data:: rip = 74

    	RIP packets.

    .. data:: l2tpv3 = 75

    	L2TPv3 packets.

    .. data:: pcep_tcp_default = 76

    	PCEP packets.

    .. data:: gre = 77

    	GRE packets.

    .. data:: vrrp = 78

    	VRRP Packets.

    .. data:: hsrp = 79

    	HSRP Packets.

    .. data:: mpls_ping = 80

    	MPLS ping packet coming or arriving from 3503

    	port

    .. data:: l2tpv2_default = 81

    	L2TPv2 default packets.

    .. data:: l2tpv2_known = 82

    	L2TPv2 known packets.

    .. data:: dns = 83

    	DNS packets.

    .. data:: radius = 84

    	RADIUS packets.

    .. data:: tacacs = 85

    	TACACS packets.

    .. data:: ntp_default = 86

    	NTP packets received at 123 port number any

    	address.

    .. data:: ntp_known = 87

    	NTP packets received at 123 port number known

    	address.

    .. data:: mobile_ipv6 = 88

    	Mobile IPV6 packets.

    .. data:: amt = 89

    	AMT packets received at UDP port number 2268.

    .. data:: sdac_tcp = 90

    	SDAC TCP packets.

    .. data:: radius_coa = 91

    	RADIUS Change of Authorization packets.

    .. data:: rel_udp = 92

    	REL UDP packets.

    .. data:: dhcp4 = 93

    	DHCP IPV4 packets.

    .. data:: dhcp6 = 94

    	DHCP IPV6 packets.

    .. data:: onepk = 95

    	ONEPK packets.

    .. data:: exr = 96

    	EXR packets.

    """

    config_default = 0

    l2tpv2_fragment = 1

    fragment = 2

    ospf_multicast_known = 3

    ospf_multicast_default = 4

    ospf_unicast_known = 5

    ospf_unicast_default = 6

    isis_known = 7

    isis_default = 8

    bfd_known = 9

    bfd_default = 10

    bfd_multipath_known = 11

    bfd_multipath0 = 12

    bfd_blb_known = 13

    bfd_blb0 = 14

    bfd_sp0 = 15

    bgp_known = 16

    bgp_config_peer = 17

    bgp_default = 18

    pim_multicast_default = 19

    pim_multicast_known = 20

    pim_unicast = 21

    igmp = 22

    icmp_local = 23

    icmp_app = 24

    icmp_control = 25

    icmp_default = 26

    icmp_app_default = 27

    ldp_tcp_known = 28

    ldp_tcp_config_peer = 29

    ldp_tcp_default = 30

    ldp_udp = 31

    all_routers = 32

    lmp_tcp_known = 33

    lmp_tcp_config_peer = 34

    lmp_tcp_default = 35

    lmp_udp = 36

    rsvp_udp = 37

    rsvp_default = 38

    rsvp_known = 39

    ike = 40

    ipsec_known = 41

    ipsec_default = 42

    ipsec_fragment = 43

    msdp_known = 44

    msdp_config_peer = 45

    msdp_default = 46

    snmp = 47

    ssh_known = 48

    ssh_default = 49

    http_known = 50

    http_default = 51

    shttp_known = 52

    shttp_default = 53

    telnet_known = 54

    telnet_default = 55

    css_known = 56

    css_default = 57

    rsh_known = 58

    rsh_default = 59

    udp_known = 60

    udp_listen = 61

    udp_config_peer = 62

    udp_default = 63

    tcp_known = 64

    tcp_listen = 65

    tcp_config_peer = 66

    tcp_default = 67

    multicast_known = 68

    multicast_default = 69

    raw_listen = 70

    raw_default = 71

    ipsla = 72

    eigrp = 73

    rip = 74

    l2tpv3 = 75

    pcep_tcp_default = 76

    gre = 77

    vrrp = 78

    hsrp = 79

    mpls_ping = 80

    l2tpv2_default = 81

    l2tpv2_known = 82

    dns = 83

    radius = 84

    tacacs = 85

    ntp_default = 86

    ntp_known = 87

    mobile_ipv6 = 88

    amt = 89

    sdac_tcp = 90

    radius_coa = 91

    rel_udp = 92

    dhcp4 = 93

    dhcp6 = 94

    onepk = 95

    exr = 96


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_cfg as meta
        return meta._meta_table['LptsFlowEnum']


class LptsPreIFibPrecedenceNumberEnum(Enum):
    """
    LptsPreIFibPrecedenceNumberEnum

    Lpts pre i fib precedence number

    .. data:: critical = 5

    	Match packets with critical precedence

    .. data:: flash = 3

    	Match packets with flash precedence

    .. data:: flash_override = 4

    	Match packets with flash override precedence

    .. data:: immediate = 2

    	Match packets with immediate precedence

    .. data:: internet = 6

    	Match packets with internetwork control

    	precedence

    .. data:: network = 7

    	Match packets with network control precedence

    .. data:: priority = 1

    	Match packets with priority precedence

    .. data:: routine = 0

    	Match packets with routine precedence

    """

    critical = 5

    flash = 3

    flash_override = 4

    immediate = 2

    internet = 6

    network = 7

    priority = 1

    routine = 0


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_lpts_pre_ifib_cfg as meta
        return meta._meta_table['LptsPreIFibPrecedenceNumberEnum']



