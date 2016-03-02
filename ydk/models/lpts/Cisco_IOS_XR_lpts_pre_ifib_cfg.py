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



class LptsFlow_Enum(Enum):
    """
    LptsFlow_Enum

    Lpts flow

    """

    """

    Invalid flow type used for fallback
    configuration

    """
    CONFIG_DEFAULT = 0

    """

    L2TPv2 Fragments

    """
    L2TPV2_FRAGMENT = 1

    """

    Fragments

    """
    FRAGMENT = 2

    """

    OSPF multicast packets on configured interfaces

    """
    OSPF_MULTICAST_KNOWN = 3

    """

    OSPF multicast packets on unconfigured (or
    newly\-configured) interfaces

    """
    OSPF_MULTICAST_DEFAULT = 4

    """

    OSPF unicast packets

    """
    OSPF_UNICAST_KNOWN = 5

    """

    OSPF unicast packets

    """
    OSPF_UNICAST_DEFAULT = 6

    """

    IS\-IS packets on configured interfaces

    """
    ISIS_KNOWN = 7

    """

    IS\-IS packets on unconfigured (or
    newly\-configured) interfaces

    """
    ISIS_DEFAULT = 8

    """

    Packets from established BGP peering sessions

    """
    BGP_KNOWN = 16

    """

    Packets from a configured BGP peer (SYNs or
    newly\-established sessions)

    """
    BGP_CONFIG_PEER = 17

    """

    Packets from unconfigured, newly\-configured, or
    wild\-card BGP peer

    """
    BGP_DEFAULT = 18

    """

    PIM multicast packets on configured interfaces

    """
    PIM_MULTICAST_DEFAULT = 19

    """

    PIM multicast packets on unconfigured (or
    newly\-configured) interfaces

    """
    PIM_MULTICAST_KNOWN = 20

    """

    PIM unicast packets

    """
    PIM_UNICAST = 21

    """

    IGMP packets

    """
    IGMP = 22

    """

    ICMP or ICMPv6 packets with local interest

    """
    ICMP_LOCAL = 23

    """

    ICMP or ICMPv6 packets of interest to
    applications

    """
    ICMP_APP = 24

    """

    ICMP or ICMPv6 packets that are used for
    control/signalling purpose

    """
    ICMP_CONTROL = 25

    """

    Other ICMP or ICMPv6 packets (may be of recent
    interest to applications)

    """
    ICMP_DEFAULT = 26

    """

    ICMP or ICMPv6 echo reply packets (when
    specific entry not present)

    """
    ICMP_APP_DEFAULT = 27

    """

    Packets from an established LDP TCP peering
    session

    """
    LDP_TCP_KNOWN = 28

    """

    Packets from a configured LDP TCP peer (SYNs or
    newly\-established sessions)

    """
    LDP_TCP_CONFIG_PEER = 29

    """

    Packets from an unconfigured, newly\-configured
    or wild\-card LDP TCP peer

    """
    LDP_TCP_DEFAULT = 30

    """

    Unicast LDP UDP packets

    """
    LDP_UDP = 31

    """

    Packets sent to the all\-routers multicast
    address (includes LDP UDP multicast)

    """
    ALL_ROUTERS = 32

    """

    Packets from an established LMP TCP peering
    session

    """
    LMP_TCP_KNOWN = 33

    """

    Packets from a configured LMP TCP peer (SYNs or
    newly\-established sessions)

    """
    LMP_TCP_CONFIG_PEER = 34

    """

    Packets from an unconfigured, newly\-configured
    or wild\-card LMP TCP peer

    """
    LMP_TCP_DEFAULT = 35

    """

    Unicast LMP UDP packets

    """
    LMP_UDP = 36

    """

    RSVP\-over\-UDP packets

    """
    RSVP_UDP = 37

    """

    RSVP (IP protocol 46) packets

    """
    RSVP_DEFAULT = 38

    """

    RSVP (IP protocol 46) packets

    """
    RSVP_KNOWN = 39

    """

    IKE packets

    """
    IKE = 40

    """

    AH or ESP packets with known SPIs

    """
    IPSEC_KNOWN = 41

    """

    AH or ESP packets with unknown or
    newly\-configured SPIs

    """
    IPSEC_DEFAULT = 42

    """

    Packets from an established MSDP session

    """
    MSDP_KNOWN = 44

    """

    Packets from a configured MSDP peer

    """
    MSDP_CONFIG_PEER = 45

    """

    Packets from an uncofigured, newly\-configured
    or wild\-card MSDP peer

    """
    MSDP_DEFAULT = 46

    """

    SNMP packets

    """
    SNMP = 47

    """

    Packets from an established SSH session

    """
    SSH_KNOWN = 48

    """

    Packets from a new or newly\-established SSH
    session

    """
    SSH_DEFAULT = 49

    """

    Packets from an established HTTP session

    """
    HTTP_KNOWN = 50

    """

    Packets from a new or newly\-established HTTP
    session

    """
    HTTP_DEFAULT = 51

    """

    Packets from an established SHTTP session

    """
    SHTTP_KNOWN = 52

    """

    Packets from a new or newly\-established SSHTP
    session

    """
    SHTTP_DEFAULT = 53

    """

    Packets from an established TELNET session

    """
    TELNET_KNOWN = 54

    """

    Packets from a new or newly\-established TELNET
    session

    """
    TELNET_DEFAULT = 55

    """

    Packets from an established CSS session

    """
    CSS_KNOWN = 56

    """

    Packets from a new or newly\-established CSS
    session

    """
    CSS_DEFAULT = 57

    """

    Packets from an established rsh session

    """
    RSH_KNOWN = 58

    """

    Packets from a new or newly\-established rsh
    session

    """
    RSH_DEFAULT = 59

    """

    Packets for established UDP sessions

    """
    UDP_KNOWN = 60

    """

    Packets for configured UDP services

    """
    UDP_LISTEN = 61

    """

    Packets for configured UDP\-based protocol
    sessions

    """
    UDP_CONFIG_PEER = 62

    """

    Packets for unconfigured or newly\-configured
    UDP services

    """
    UDP_DEFAULT = 63

    """

    Packets for established TCP sessions

    """
    TCP_KNOWN = 64

    """

    Packets for configured TCP services

    """
    TCP_LISTEN = 65

    """

    Packets for configured TCP peers

    """
    TCP_CONFIG_PEER = 66

    """

    Packets for unconfigured or newly\-configured
    TCP services

    """
    TCP_DEFAULT = 67

    """

    Packets for configured multicast groups

    """
    MULTICAST_KNOWN = 68

    """

    Packets for unconfigured or newly\-configured
    multicast groups

    """
    MULTICAST_DEFAULT = 69

    """

    Packets for configured IP protocols

    """
    RAW_LISTEN = 70

    """

    Packets for unconfigured or newly\-configured
    IPv4 or IPv6 protocols

    """
    RAW_DEFAULT = 71

    """

    IP SLA packets destined to squid Q #4 for
    timestamping by squid driver

    """
    IPSLA = 72

    """

    L2TPv3 packets.

    """
    L2TPV3 = 75

    """

    PCEP packets.

    """
    PCEP_TCP_DEFAULT = 76

    """

    GRE packets.

    """
    GRE = 77

    """

    VRRP Packets.

    """
    VRRP = 78

    """

    HSRP Packets.

    """
    HSRP = 79

    """

    MPLS ping packet coming or arriving from 3503
    port

    """
    MPLS_PING = 80

    """

    L2TPv2 default packets.

    """
    L2TPV2_DEFAULT = 81

    """

    L2TPv2 known packets.

    """
    L2TPV2_KNOWN = 82

    """

    NTP packets received at 123 port number any
    address.

    """
    NTP_DEFAULT = 86

    """

    NTP packets received at 123 port number known
    address.

    """
    NTP_KNOWN = 87

    """

    AMT packets received at UDP port number 2268.

    """
    AMT = 89


    @staticmethod
    def _meta_info():
        from ydk.models.lpts._meta import _Cisco_IOS_XR_lpts_pre_ifib_cfg as meta
        return meta._meta_table['LptsFlow_Enum']


class LptsPreIFibPrecedenceNumber_Enum(Enum):
    """
    LptsPreIFibPrecedenceNumber_Enum

    Lpts pre i fib precedence number

    """

    """

    Match packets with critical precedence

    """
    CRITICAL = 5

    """

    Match packets with flash precedence

    """
    FLASH = 3

    """

    Match packets with flash override precedence

    """
    FLASH_OVERRIDE = 4

    """

    Match packets with immediate precedence

    """
    IMMEDIATE = 2

    """

    Match packets with internetwork control
    precedence

    """
    INTERNET = 6

    """

    Match packets with network control precedence

    """
    NETWORK = 7

    """

    Match packets with priority precedence

    """
    PRIORITY = 1

    """

    Match packets with routine precedence

    """
    ROUTINE = 0


    @staticmethod
    def _meta_info():
        from ydk.models.lpts._meta import _Cisco_IOS_XR_lpts_pre_ifib_cfg as meta
        return meta._meta_table['LptsPreIFibPrecedenceNumber_Enum']



