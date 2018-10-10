""" Cisco_IOS_XR_lpts_pre_ifib_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-pre\-ifib package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-lpts\-lib\-cfg
  Cisco\-IOS\-XR\-config\-mda\-cfg
modules with configuration data.

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class LptsDynamicFlowConfig(Enum):
    """
    LptsDynamicFlowConfig (Enum Class)

    Lpts dynamic flow config

    .. data:: flows_config = 0

    	LPTS Flows Limit

    .. data:: platform_config = 1

    	Platform Limit

    """

    flows_config = Enum.YLeaf(0, "flows-config")

    platform_config = Enum.YLeaf(1, "platform-config")


class LptsFlow(Enum):
    """
    LptsFlow (Enum Class)

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

    .. data:: bob_ietf = 97

    	IETF BFD packets over Logical Bundle.

    .. data:: xipc_throt = 98

    	XIPC Throttle Flow.

    .. data:: platform_limit = 99

    	Platform Limit.

    """

    config_default = Enum.YLeaf(0, "config-default")

    l2tpv2_fragment = Enum.YLeaf(1, "l2tpv2-fragment")

    fragment = Enum.YLeaf(2, "fragment")

    ospf_multicast_known = Enum.YLeaf(3, "ospf-multicast-known")

    ospf_multicast_default = Enum.YLeaf(4, "ospf-multicast-default")

    ospf_unicast_known = Enum.YLeaf(5, "ospf-unicast-known")

    ospf_unicast_default = Enum.YLeaf(6, "ospf-unicast-default")

    isis_known = Enum.YLeaf(7, "isis-known")

    isis_default = Enum.YLeaf(8, "isis-default")

    bfd_known = Enum.YLeaf(9, "bfd-known")

    bfd_default = Enum.YLeaf(10, "bfd-default")

    bfd_multipath_known = Enum.YLeaf(11, "bfd-multipath-known")

    bfd_multipath0 = Enum.YLeaf(12, "bfd-multipath0")

    bfd_blb_known = Enum.YLeaf(13, "bfd-blb-known")

    bfd_blb0 = Enum.YLeaf(14, "bfd-blb0")

    bfd_sp0 = Enum.YLeaf(15, "bfd-sp0")

    bgp_known = Enum.YLeaf(16, "bgp-known")

    bgp_config_peer = Enum.YLeaf(17, "bgp-config-peer")

    bgp_default = Enum.YLeaf(18, "bgp-default")

    pim_multicast_default = Enum.YLeaf(19, "pim-multicast-default")

    pim_multicast_known = Enum.YLeaf(20, "pim-multicast-known")

    pim_unicast = Enum.YLeaf(21, "pim-unicast")

    igmp = Enum.YLeaf(22, "igmp")

    icmp_local = Enum.YLeaf(23, "icmp-local")

    icmp_app = Enum.YLeaf(24, "icmp-app")

    icmp_control = Enum.YLeaf(25, "icmp-control")

    icmp_default = Enum.YLeaf(26, "icmp-default")

    icmp_app_default = Enum.YLeaf(27, "icmp-app-default")

    ldp_tcp_known = Enum.YLeaf(28, "ldp-tcp-known")

    ldp_tcp_config_peer = Enum.YLeaf(29, "ldp-tcp-config-peer")

    ldp_tcp_default = Enum.YLeaf(30, "ldp-tcp-default")

    ldp_udp = Enum.YLeaf(31, "ldp-udp")

    all_routers = Enum.YLeaf(32, "all-routers")

    lmp_tcp_known = Enum.YLeaf(33, "lmp-tcp-known")

    lmp_tcp_config_peer = Enum.YLeaf(34, "lmp-tcp-config-peer")

    lmp_tcp_default = Enum.YLeaf(35, "lmp-tcp-default")

    lmp_udp = Enum.YLeaf(36, "lmp-udp")

    rsvp_udp = Enum.YLeaf(37, "rsvp-udp")

    rsvp_default = Enum.YLeaf(38, "rsvp-default")

    rsvp_known = Enum.YLeaf(39, "rsvp-known")

    ike = Enum.YLeaf(40, "ike")

    ipsec_known = Enum.YLeaf(41, "ipsec-known")

    ipsec_default = Enum.YLeaf(42, "ipsec-default")

    ipsec_fragment = Enum.YLeaf(43, "ipsec-fragment")

    msdp_known = Enum.YLeaf(44, "msdp-known")

    msdp_config_peer = Enum.YLeaf(45, "msdp-config-peer")

    msdp_default = Enum.YLeaf(46, "msdp-default")

    snmp = Enum.YLeaf(47, "snmp")

    ssh_known = Enum.YLeaf(48, "ssh-known")

    ssh_default = Enum.YLeaf(49, "ssh-default")

    http_known = Enum.YLeaf(50, "http-known")

    http_default = Enum.YLeaf(51, "http-default")

    shttp_known = Enum.YLeaf(52, "shttp-known")

    shttp_default = Enum.YLeaf(53, "shttp-default")

    telnet_known = Enum.YLeaf(54, "telnet-known")

    telnet_default = Enum.YLeaf(55, "telnet-default")

    css_known = Enum.YLeaf(56, "css-known")

    css_default = Enum.YLeaf(57, "css-default")

    rsh_known = Enum.YLeaf(58, "rsh-known")

    rsh_default = Enum.YLeaf(59, "rsh-default")

    udp_known = Enum.YLeaf(60, "udp-known")

    udp_listen = Enum.YLeaf(61, "udp-listen")

    udp_config_peer = Enum.YLeaf(62, "udp-config-peer")

    udp_default = Enum.YLeaf(63, "udp-default")

    tcp_known = Enum.YLeaf(64, "tcp-known")

    tcp_listen = Enum.YLeaf(65, "tcp-listen")

    tcp_config_peer = Enum.YLeaf(66, "tcp-config-peer")

    tcp_default = Enum.YLeaf(67, "tcp-default")

    multicast_known = Enum.YLeaf(68, "multicast-known")

    multicast_default = Enum.YLeaf(69, "multicast-default")

    raw_listen = Enum.YLeaf(70, "raw-listen")

    raw_default = Enum.YLeaf(71, "raw-default")

    ipsla = Enum.YLeaf(72, "ipsla")

    eigrp = Enum.YLeaf(73, "eigrp")

    rip = Enum.YLeaf(74, "rip")

    l2tpv3 = Enum.YLeaf(75, "l2tpv3")

    pcep_tcp_default = Enum.YLeaf(76, "pcep-tcp-default")

    gre = Enum.YLeaf(77, "gre")

    vrrp = Enum.YLeaf(78, "vrrp")

    hsrp = Enum.YLeaf(79, "hsrp")

    mpls_ping = Enum.YLeaf(80, "mpls-ping")

    l2tpv2_default = Enum.YLeaf(81, "l2tpv2-default")

    l2tpv2_known = Enum.YLeaf(82, "l2tpv2-known")

    dns = Enum.YLeaf(83, "dns")

    radius = Enum.YLeaf(84, "radius")

    tacacs = Enum.YLeaf(85, "tacacs")

    ntp_default = Enum.YLeaf(86, "ntp-default")

    ntp_known = Enum.YLeaf(87, "ntp-known")

    mobile_ipv6 = Enum.YLeaf(88, "mobile-ipv6")

    amt = Enum.YLeaf(89, "amt")

    sdac_tcp = Enum.YLeaf(90, "sdac-tcp")

    radius_coa = Enum.YLeaf(91, "radius-coa")

    rel_udp = Enum.YLeaf(92, "rel-udp")

    dhcp4 = Enum.YLeaf(93, "dhcp4")

    dhcp6 = Enum.YLeaf(94, "dhcp6")

    onepk = Enum.YLeaf(95, "onepk")

    exr = Enum.YLeaf(96, "exr")

    bob_ietf = Enum.YLeaf(97, "bob-ietf")

    xipc_throt = Enum.YLeaf(98, "xipc-throt")

    platform_limit = Enum.YLeaf(99, "platform-limit")


class LptsPreIFibPrecedenceNumber(Enum):
    """
    LptsPreIFibPrecedenceNumber (Enum Class)

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

    critical = Enum.YLeaf(5, "critical")

    flash = Enum.YLeaf(3, "flash")

    flash_override = Enum.YLeaf(4, "flash-override")

    immediate = Enum.YLeaf(2, "immediate")

    internet = Enum.YLeaf(6, "internet")

    network = Enum.YLeaf(7, "network")

    priority = Enum.YLeaf(1, "priority")

    routine = Enum.YLeaf(0, "routine")


class Lptsafi(Enum):
    """
    Lptsafi (Enum Class)

    Lptsafi

    .. data:: ipv4 = 1

    	IPv4 type

    .. data:: ipv6 = 2

    	IPv6 type

    """

    ipv4 = Enum.YLeaf(1, "ipv4")

    ipv6 = Enum.YLeaf(2, "ipv6")



