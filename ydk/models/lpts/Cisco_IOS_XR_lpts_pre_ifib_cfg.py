""" Cisco_IOS_XR_lpts_pre_ifib_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR lpts\-pre\-ifib package configuration.

This YANG module augments the
  Cisco\-IOS\-XR\-lpts\-lib\-cfg
  Cisco\-IOS\-XR\-config\-mda\-cfg
modules with configuration data.

Copyright (c) 2013\-2015 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError



class LptsFlowEnum(Enum):
    """
    LptsFlowEnum

    Lpts flow

    .. data:: CONFIG_DEFAULT = 0

    	Invalid flow type used for fallback

    	configuration

    .. data:: L2TPV2_FRAGMENT = 1

    	L2TPv2 Fragments

    .. data:: FRAGMENT = 2

    	Fragments

    .. data:: OSPF_MULTICAST_KNOWN = 3

    	OSPF multicast packets on configured interfaces

    .. data:: OSPF_MULTICAST_DEFAULT = 4

    	OSPF multicast packets on unconfigured (or

    	newly-configured) interfaces

    .. data:: OSPF_UNICAST_KNOWN = 5

    	OSPF unicast packets

    .. data:: OSPF_UNICAST_DEFAULT = 6

    	OSPF unicast packets

    .. data:: ISIS_KNOWN = 7

    	IS-IS packets on configured interfaces

    .. data:: ISIS_DEFAULT = 8

    	IS-IS packets on unconfigured (or

    	newly-configured) interfaces

    .. data:: BGP_KNOWN = 16

    	Packets from established BGP peering sessions

    .. data:: BGP_CONFIG_PEER = 17

    	Packets from a configured BGP peer (SYNs or

    	newly-established sessions)

    .. data:: BGP_DEFAULT = 18

    	Packets from unconfigured, newly-configured, or

    	wild-card BGP peer

    .. data:: PIM_MULTICAST_DEFAULT = 19

    	PIM multicast packets on configured interfaces

    .. data:: PIM_MULTICAST_KNOWN = 20

    	PIM multicast packets on unconfigured (or

    	newly-configured) interfaces

    .. data:: PIM_UNICAST = 21

    	PIM unicast packets

    .. data:: IGMP = 22

    	IGMP packets

    .. data:: ICMP_LOCAL = 23

    	ICMP or ICMPv6 packets with local interest

    .. data:: ICMP_APP = 24

    	ICMP or ICMPv6 packets of interest to

    	applications

    .. data:: ICMP_CONTROL = 25

    	ICMP or ICMPv6 packets that are used for

    	control/signalling purpose

    .. data:: ICMP_DEFAULT = 26

    	Other ICMP or ICMPv6 packets (may be of recent

    	interest to applications)

    .. data:: ICMP_APP_DEFAULT = 27

    	ICMP or ICMPv6 echo reply packets (when

    	specific entry not present)

    .. data:: LDP_TCP_KNOWN = 28

    	Packets from an established LDP TCP peering

    	session

    .. data:: LDP_TCP_CONFIG_PEER = 29

    	Packets from a configured LDP TCP peer (SYNs or

    	newly-established sessions)

    .. data:: LDP_TCP_DEFAULT = 30

    	Packets from an unconfigured, newly-configured

    	or wild-card LDP TCP peer

    .. data:: LDP_UDP = 31

    	Unicast LDP UDP packets

    .. data:: ALL_ROUTERS = 32

    	Packets sent to the all-routers multicast

    	address (includes LDP UDP multicast)

    .. data:: LMP_TCP_KNOWN = 33

    	Packets from an established LMP TCP peering

    	session

    .. data:: LMP_TCP_CONFIG_PEER = 34

    	Packets from a configured LMP TCP peer (SYNs or

    	newly-established sessions)

    .. data:: LMP_TCP_DEFAULT = 35

    	Packets from an unconfigured, newly-configured

    	or wild-card LMP TCP peer

    .. data:: LMP_UDP = 36

    	Unicast LMP UDP packets

    .. data:: RSVP_UDP = 37

    	RSVP-over-UDP packets

    .. data:: RSVP_DEFAULT = 38

    	RSVP (IP protocol 46) packets

    .. data:: RSVP_KNOWN = 39

    	RSVP (IP protocol 46) packets

    .. data:: IKE = 40

    	IKE packets

    .. data:: IPSEC_KNOWN = 41

    	AH or ESP packets with known SPIs

    .. data:: IPSEC_DEFAULT = 42

    	AH or ESP packets with unknown or

    	newly-configured SPIs

    .. data:: MSDP_KNOWN = 44

    	Packets from an established MSDP session

    .. data:: MSDP_CONFIG_PEER = 45

    	Packets from a configured MSDP peer

    .. data:: MSDP_DEFAULT = 46

    	Packets from an uncofigured, newly-configured

    	or wild-card MSDP peer

    .. data:: SNMP = 47

    	SNMP packets

    .. data:: SSH_KNOWN = 48

    	Packets from an established SSH session

    .. data:: SSH_DEFAULT = 49

    	Packets from a new or newly-established SSH

    	session

    .. data:: HTTP_KNOWN = 50

    	Packets from an established HTTP session

    .. data:: HTTP_DEFAULT = 51

    	Packets from a new or newly-established HTTP

    	session

    .. data:: SHTTP_KNOWN = 52

    	Packets from an established SHTTP session

    .. data:: SHTTP_DEFAULT = 53

    	Packets from a new or newly-established SSHTP

    	session

    .. data:: TELNET_KNOWN = 54

    	Packets from an established TELNET session

    .. data:: TELNET_DEFAULT = 55

    	Packets from a new or newly-established TELNET

    	session

    .. data:: CSS_KNOWN = 56

    	Packets from an established CSS session

    .. data:: CSS_DEFAULT = 57

    	Packets from a new or newly-established CSS

    	session

    .. data:: RSH_KNOWN = 58

    	Packets from an established rsh session

    .. data:: RSH_DEFAULT = 59

    	Packets from a new or newly-established rsh

    	session

    .. data:: UDP_KNOWN = 60

    	Packets for established UDP sessions

    .. data:: UDP_LISTEN = 61

    	Packets for configured UDP services

    .. data:: UDP_CONFIG_PEER = 62

    	Packets for configured UDP-based protocol

    	sessions

    .. data:: UDP_DEFAULT = 63

    	Packets for unconfigured or newly-configured

    	UDP services

    .. data:: TCP_KNOWN = 64

    	Packets for established TCP sessions

    .. data:: TCP_LISTEN = 65

    	Packets for configured TCP services

    .. data:: TCP_CONFIG_PEER = 66

    	Packets for configured TCP peers

    .. data:: TCP_DEFAULT = 67

    	Packets for unconfigured or newly-configured

    	TCP services

    .. data:: MULTICAST_KNOWN = 68

    	Packets for configured multicast groups

    .. data:: MULTICAST_DEFAULT = 69

    	Packets for unconfigured or newly-configured

    	multicast groups

    .. data:: RAW_LISTEN = 70

    	Packets for configured IP protocols

    .. data:: RAW_DEFAULT = 71

    	Packets for unconfigured or newly-configured

    	IPv4 or IPv6 protocols

    .. data:: IPSLA = 72

    	IP SLA packets destined to squid Q #4 for

    	timestamping by squid driver

    .. data:: L2TPV3 = 75

    	L2TPv3 packets.

    .. data:: PCEP_TCP_DEFAULT = 76

    	PCEP packets.

    .. data:: GRE = 77

    	GRE packets.

    .. data:: VRRP = 78

    	VRRP Packets.

    .. data:: HSRP = 79

    	HSRP Packets.

    .. data:: MPLS_PING = 80

    	MPLS ping packet coming or arriving from 3503

    	port

    .. data:: L2TPV2_DEFAULT = 81

    	L2TPv2 default packets.

    .. data:: L2TPV2_KNOWN = 82

    	L2TPv2 known packets.

    .. data:: NTP_DEFAULT = 86

    	NTP packets received at 123 port number any

    	address.

    .. data:: NTP_KNOWN = 87

    	NTP packets received at 123 port number known

    	address.

    .. data:: AMT = 89

    	AMT packets received at UDP port number 2268.

    """

    CONFIG_DEFAULT = 0

    L2TPV2_FRAGMENT = 1

    FRAGMENT = 2

    OSPF_MULTICAST_KNOWN = 3

    OSPF_MULTICAST_DEFAULT = 4

    OSPF_UNICAST_KNOWN = 5

    OSPF_UNICAST_DEFAULT = 6

    ISIS_KNOWN = 7

    ISIS_DEFAULT = 8

    BGP_KNOWN = 16

    BGP_CONFIG_PEER = 17

    BGP_DEFAULT = 18

    PIM_MULTICAST_DEFAULT = 19

    PIM_MULTICAST_KNOWN = 20

    PIM_UNICAST = 21

    IGMP = 22

    ICMP_LOCAL = 23

    ICMP_APP = 24

    ICMP_CONTROL = 25

    ICMP_DEFAULT = 26

    ICMP_APP_DEFAULT = 27

    LDP_TCP_KNOWN = 28

    LDP_TCP_CONFIG_PEER = 29

    LDP_TCP_DEFAULT = 30

    LDP_UDP = 31

    ALL_ROUTERS = 32

    LMP_TCP_KNOWN = 33

    LMP_TCP_CONFIG_PEER = 34

    LMP_TCP_DEFAULT = 35

    LMP_UDP = 36

    RSVP_UDP = 37

    RSVP_DEFAULT = 38

    RSVP_KNOWN = 39

    IKE = 40

    IPSEC_KNOWN = 41

    IPSEC_DEFAULT = 42

    MSDP_KNOWN = 44

    MSDP_CONFIG_PEER = 45

    MSDP_DEFAULT = 46

    SNMP = 47

    SSH_KNOWN = 48

    SSH_DEFAULT = 49

    HTTP_KNOWN = 50

    HTTP_DEFAULT = 51

    SHTTP_KNOWN = 52

    SHTTP_DEFAULT = 53

    TELNET_KNOWN = 54

    TELNET_DEFAULT = 55

    CSS_KNOWN = 56

    CSS_DEFAULT = 57

    RSH_KNOWN = 58

    RSH_DEFAULT = 59

    UDP_KNOWN = 60

    UDP_LISTEN = 61

    UDP_CONFIG_PEER = 62

    UDP_DEFAULT = 63

    TCP_KNOWN = 64

    TCP_LISTEN = 65

    TCP_CONFIG_PEER = 66

    TCP_DEFAULT = 67

    MULTICAST_KNOWN = 68

    MULTICAST_DEFAULT = 69

    RAW_LISTEN = 70

    RAW_DEFAULT = 71

    IPSLA = 72

    L2TPV3 = 75

    PCEP_TCP_DEFAULT = 76

    GRE = 77

    VRRP = 78

    HSRP = 79

    MPLS_PING = 80

    L2TPV2_DEFAULT = 81

    L2TPV2_KNOWN = 82

    NTP_DEFAULT = 86

    NTP_KNOWN = 87

    AMT = 89


    @staticmethod
    def _meta_info():
        from ydk.models.lpts._meta import _Cisco_IOS_XR_lpts_pre_ifib_cfg as meta
        return meta._meta_table['LptsFlowEnum']


class LptsPreIFibPrecedenceNumberEnum(Enum):
    """
    LptsPreIFibPrecedenceNumberEnum

    Lpts pre i fib precedence number

    .. data:: CRITICAL = 5

    	Match packets with critical precedence

    .. data:: FLASH = 3

    	Match packets with flash precedence

    .. data:: FLASH_OVERRIDE = 4

    	Match packets with flash override precedence

    .. data:: IMMEDIATE = 2

    	Match packets with immediate precedence

    .. data:: INTERNET = 6

    	Match packets with internetwork control

    	precedence

    .. data:: NETWORK = 7

    	Match packets with network control precedence

    .. data:: PRIORITY = 1

    	Match packets with priority precedence

    .. data:: ROUTINE = 0

    	Match packets with routine precedence

    """

    CRITICAL = 5

    FLASH = 3

    FLASH_OVERRIDE = 4

    IMMEDIATE = 2

    INTERNET = 6

    NETWORK = 7

    PRIORITY = 1

    ROUTINE = 0


    @staticmethod
    def _meta_info():
        from ydk.models.lpts._meta import _Cisco_IOS_XR_lpts_pre_ifib_cfg as meta
        return meta._meta_table['LptsPreIFibPrecedenceNumberEnum']



